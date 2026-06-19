#!/usr/bin/env python3
"""
Full automated daily literature review pipeline.
Runs in GitHub Actions (cron/manual) or locally.

Flow:
  1. Read keywords.json
  2. Search arXiv (HTTP API) + S2 (REST API)
  3. Cross-day dedup via seen_papers.json
  4. Merge & dedup → top 10
  5. Download PDFs (arXiv), extract text
  6. LLM (Qwen) → 8-module structured summaries
  7. Generate daily report + rebuild site
  8. Update seen_papers.json
"""

import json, os, re, sys, time, hashlib, subprocess, urllib.request, urllib.parse
from pathlib import Path
from datetime import datetime, timezone, timedelta
from xml.etree import ElementTree
from html import escape

import requests
from openai import OpenAI

# ── Paths ──
REPO_DIR = Path(__file__).parent.resolve()
KEYWORDS_FILE = REPO_DIR / "keywords.json"
SEEN_FILE = REPO_DIR / "seen_papers.json"
REPORTS_DIR = REPO_DIR / "reports"
SITE_SCRIPT = REPO_DIR / "generate_site.py"

# ── Env ──
S2_API_KEY = os.environ.get("S2_API_KEY", "")
LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_MODEL = os.environ.get("LLM_MODEL", "qwen-plus")
LLM_BASE_URL = os.environ.get(
    "LLM_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"
)

TODAY = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")

###############################################################################
# 1. Keywords
###############################################################################
def load_keywords():
    kw = json.loads(KEYWORDS_FILE.read_text(encoding="utf-8"))
    topics = kw.get("topics", [])
    if not topics:
        print("⚠️  keywords.json 中未定义搜索主题")
        sys.exit(0)

    def build_query(topics_list):
        parts = [f'"{t}"' for t in topics_list]
        return " OR ".join(f"({p})" for p in parts)

    return {
        "topics": topics,
        "arxiv_query": build_query(topics) if kw.get("arxiv", {}).get("enabled", True) else None,
        "arxiv_max": kw.get("arxiv", {}).get("max_results", 10),
        "s2_query": build_query(topics) if kw.get("semantic_scholar", {}).get("enabled", True) else None,
        "s2_limit_a": kw.get("semantic_scholar", {}).get("query_a_limit", 30),
        "s2_limit_b": kw.get("semantic_scholar", {}).get("query_b_limit", 20),
    }

###############################################################################
# 2a. arXiv Search
###############################################################################
ARXIV_API = "http://export.arxiv.org/api/query"

def search_arxiv(query, max_results=10):
    """Search arXiv via HTTP API. Returns list of dicts."""
    params = {
        "search_query": f"all:{query}",
        "max_results": str(max_results),
        "sortBy": "submittedDate",
        "sortOrder": "DOCKING",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    print(f"  arXiv URL: {url[:120]}...")
    time.sleep(3)  # arXiv rate limit

    req = urllib.request.Request(url, headers={"User-Agent": "DailyReviewPipeline/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        xml_data = resp.read().decode("utf-8")

    ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ElementTree.fromstring(xml_data)
    papers = []
    for entry in root.findall("a:entry", ns):
        arxiv_id = entry.find("a:id", ns).text.split("/")[-1].split("v")[0]
        title = (entry.find("a:title", ns).text or "").replace("\n", " ").strip()
        published = entry.find("a:published", ns).text[:10] if entry.find("a:published", ns) is not None else ""
        summary = (entry.find("a:summary", ns).text or "").replace("\n", " ").strip()
        authors = [a.find("a:name", ns).text for a in entry.findall("a:author", ns)]
        categories = [c.get("term") for c in entry.findall("a:category", ns)]
        pdf_url = next(
            (l.get("href") for l in entry.findall("a:link", ns) if l.get("title") == "pdf"),
            f"https://arxiv.org/pdf/{arxiv_id}.pdf",
        )
        papers.append({
            "arxiv_id": arxiv_id,
            "title": title,
            "authors": authors,
            "abstract": summary,
            "published": published,
            "categories": categories,
            "pdf_url": pdf_url,
            "source": "arxiv",
        })
    print(f"  → {len(papers)} papers from arXiv")
    return papers


def fallback_search_arxiv(query, max_results=10):
    """Fallback: broader query if primary returns 0."""
    print("  ⚠️  主查询返回 0 篇，尝试更宽泛的 fallback 查询...")
    fallback = (
        '(electrochemistry AND "machine learning") OR '
        '("nuclear quantum effect" AND catalysis) OR '
        '("grand canonical" AND simulation)'
    )
    return search_arxiv(fallback, max_results)

###############################################################################
# 2b. S2 Search
###############################################################################
S2_BULK_API = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"

def search_s2(query, limit=30, sort="relevance", fields=None):
    """Search S2 via bulk search API. Returns list of dicts."""
    if not S2_API_KEY:
        print("  ⚠️  未设置 S2_API_KEY，跳过 S2 检索")
        return [], False

    if fields is None:
        fields = [
            "title", "abstract", "authors", "year", "url",
            "paperId", "citationCount", "publicationDate",
        ]

    headers = {"x-api-key": S2_API_KEY}
    params = {
        "query": query,
        "limit": min(limit, 1000),
        "fields": ",".join(fields),
        "sort": sort,
    }

    url = f"{S2_BULK_API}?{urllib.parse.urlencode(params)}"
    print(f"  S2 URL: {url[:120]}...")

    for attempt in range(3):
        try:
            resp = requests.get(url, headers=headers, timeout=60)
            if resp.status_code == 429:
                wait = 30 * (attempt + 1)
                print(f"  ⚠️  S2 rate limit (429), 等待 {wait}s 后重试 ({attempt+1}/3)")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            data = resp.json()
            papers_raw = data.get("data", [])
            papers = []
            for p in papers_raw:
                pid = p.get("paperId", "")
                papers.append({
                    "s2_id": pid,
                    "title": p.get("title", ""),
                    "authors": [a.get("name", "") for a in p.get("authors", [])],
                    "abstract": p.get("abstract", ""),
                    "year": str(p.get("year", "")),
                    "publicationDate": p.get("publicationDate", ""),
                    "url": p.get("url", f"https://api.semanticscholar.org/CorpusID:{pid}"),
                    "citationCount": p.get("citationCount", 0),
                    "source": "s2",
                    "arxiv_id": None,
                })
            print(f"  → {len(papers)} papers from S2")
            return papers, True
        except requests.exceptions.RequestException as e:
            print(f"  ⚠️  S2 请求失败: {e}")
            if attempt < 2:
                time.sleep(10)
    print("  ✗ S2 所有重试耗尽")
    return [], False

###############################################################################
# 2c. S2 Query B (OA filter)
###############################################################################
def search_s2_oa(query, limit=20):
    """S2 search with open_access_pdf filter."""
    fields = [
        "title", "abstract", "authors", "year", "url",
        "paperId", "citationCount", "publicationDate", "openAccessPdf",
    ]
    papers, ok = search_s2(query, limit=limit, sort="publicationDate", fields=fields)
    return papers, ok

###############################################################################
# 3. Dedup
###############################################################################
def load_seen():
    if SEEN_FILE.exists():
        return json.loads(SEEN_FILE.read_text(encoding="utf-8"))
    return {}

def save_seen(seen):
    SEEN_FILE.write_text(
        json.dumps(seen, ensure_ascii=False, indent=2), encoding="utf-8"
    )

def paper_key(p):
    if p.get("arxiv_id"):
        return f"arxiv:{p['arxiv_id']}"
    if p.get("s2_id"):
        return f"s2:{p['s2_id']}"
    norm = re.sub(r"[^a-z0-9]", "", p.get("title", "").lower())[:40]
    return f"title:{norm}"

def dedup_candidates(papers, seen):
    new_papers = []
    dup_count = 0
    for p in papers:
        key = paper_key(p)
        if key in seen:
            dup_count += 1
        else:
            new_papers.append(p)
    print(f"  → 已过滤 {dup_count} 篇已读论文，剩余 {len(new_papers)} 篇候选")
    return new_papers

###############################################################################
# 4. Merge & Dedup
###############################################################################
def normalize_title(title):
    return re.sub(r"[^a-z0-9]", "", title.lower())

def merge_and_dedup(arxiv_papers, s2_papers):
    all_papers = arxiv_papers + s2_papers
    seen_titles = {}
    merged = []
    for p in all_papers:
        nt = normalize_title(p["title"])
        if nt in seen_titles:
            idx = seen_titles[nt]
            existing = merged[idx]
            # prefer S2 entry (richer metadata)
            if p["source"] == "s2" and existing["source"] == "arxiv":
                merged[idx] = p
        else:
            seen_titles[nt] = len(merged)
            merged.append(p)

    print(f"  → 合并去重后共 {len(merged)} 篇论文")
    # sort: arXiv papers first (newest), then S2 by year
    merged.sort(key=lambda p: (
        0 if p["source"] == "arxiv" else 1,
        p.get("published", p.get("year", "")),
    ), reverse=True)

    return merged[:10]

###############################################################################
# 5. Download PDF & Extract Text
###############################################################################
def download_and_extract(p):
    """Download PDF (arXiv) and extract text. Returns full text or abstract."""
    arxiv_id = p.get("arxiv_id")
    if not arxiv_id:
        print(f"    ⚠️  {p['title'][:50]}... 无 arXiv ID，使用摘要")
        return p.get("abstract", ""), False

    pdf_url = p.get("pdf_url", f"https://arxiv.org/pdf/{arxiv_id}.pdf")
    pdf_path = REPO_DIR / "pdfs" / f"{arxiv_id}.pdf"
    pdf_path.parent.mkdir(exist_ok=True)

    try:
        print(f"    ↓ 下载 PDF: {pdf_url}")
        resp = requests.get(pdf_url, timeout=60, headers={"User-Agent": "DailyReview/1.0"})
        resp.raise_for_status()
        pdf_path.write_bytes(resp.content)
        print(f"    ✓ PDF 已保存 ({len(resp.content)} bytes)")

        # extract text via PyMuPDF
        import fitz
        doc = fitz.open(pdf_path)
        text_parts = []
        for page in doc:
            text_parts.append(page.get_text())
        doc.close()
        full_text = "\n".join(text_parts)
        print(f"    ✓ 提取 {len(full_text)} 字符文本")
        return full_text, True
    except Exception as e:
        print(f"    ✗ PDF 处理失败: {e}")
        return p.get("abstract", ""), False


def truncate_text(text, max_chars=8000):
    """Truncate text for LLM context window."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n\n...[truncated]"

###############################################################################
# 6. LLM Summary (Qwen via OpenAI-compatible API)
###############################################################################
SUMMARIZE_PROMPT = """你是一位计算化学/电催化领域的研究助理。阅读以下论文全文（或摘要），按以下 8 模块输出结构化摘要：

### 1. 论文元信息
标题、第一作者+et al.、期刊/出处、发布日期、年份。

### 2. 核心问题
一句话总结本文试图解决的科学问题。

### 3. 动机与背景
现有方法有什么痛点？为什么这个问题值得解决？

### 4. 方法核心
3-5 个要点，突出方法创新而非实现细节。

### 5. 关键实验与结果
主要数据集/体系、基线方法、最重要的 1-2 个数值结果。

### 6. 创新点
2-3 条，明确与已有工作的差异。

### 7. 局限性
本文的不足或未解决的问题。

### 8. 对你研究的启发
可迁移的思路或方法论启发。

论文："""

BRIEF_PROMPT = """你是一位计算化学/电催化领域的研究助理。阅读以下论文摘要，用 3-4 句话总结：核心问题、方法要点、关键结果、与你研究的相关度（高/中/低）。

论文摘要："""

def llm_summarize(full_text, brief=False):
    """Call Qwen API for structured summary. Returns markdown text."""
    if not LLM_API_KEY:
        print("    ⚠️  未设置 LLM_API_KEY，使用摘要原文替代")
        return ""

    client = OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)
    prompt = BRIEF_PROMPT if brief else SUMMARIZE_PROMPT
    text = truncate_text(full_text, max_chars=6000 if brief else 8000)

    try:
        resp = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": "你是一位严谨的计算化学研究助理，用中文输出结构化摘要。"},
                {"role": "user", "content": prompt + text},
            ],
            temperature=0.3,
            max_tokens=1500,
        )
        result = resp.choices[0].message.content.strip()
        print(f"    ✓ LLM 摘要生成完成 ({len(result)} chars)")
        return result
    except Exception as e:
        print(f"    ✗ LLM API 调用失败: {e}")
        return ""

def infer_tags(title, abstract):
    """Simple tag inference from title+abstract."""
    text = (title + " " + abstract).lower()
    tags = []
    tag_map = {
        "electrochemistry": ["electrochem", "electrode", "potential", "electrocatal"],
        "MLFF": ["machine learning force field", "neural network potential", "mlip", "nnp"],
        "NQE": ["nuclear quantum effect", "nuclear quantum", "rpmd", "ring polymer"],
        "catalysis": ["catalysis", "catalyst", "catalytic"],
        "constant-potential": ["constant potential", "gc-ensemble", "grand canonical"],
        "surface": ["surface", "interface", "adsorption"],
        "dft": ["dft", "density functional"],
        "active-learning": ["active learning"],
        "generative": ["generative", "flow"],
    }
    for tag, keywords in tag_map.items():
        if any(k in text for k in keywords):
            tags.append(tag)
    return tags if tags else ["general"]

###############################################################################
# 7. Generate Daily Report
###############################################################################
def generate_report(papers_with_summaries, stats):
    """Generate daily-summary-{TODAY}.md."""
    reports_dir = REPORTS_DIR
    reports_dir.mkdir(exist_ok=True)

    source_str = "arXiv (last 24h)"
    if stats.get("s2_available"):
        source_str += " + Semantic Scholar (不限日期)"
    else:
        source_str += " + Semantic Scholar (不可用)"

    lines = []
    lines.append(f"# 每日文献追踪报告 - {TODAY}\n")
    lines.append("## 📊 统计概览\n")
    lines.append(f"- 检索源: {source_str}")
    lines.append(f"- 原始候选: {stats['raw_total']} 篇（S2: {stats['s2_count']}, arXiv: {stats['arxiv_count']}）")
    lines.append(f"- 有效去重后: {stats['after_dedup']} 篇")
    lines.append(f"- 下载 PDF: {stats['downloaded']} 篇")
    lines.append(f"- 实际精读: {stats['deep_read']} 篇")
    lines.append("")

    lines.append("## 📑 论文详情（按相关性排序）\n")
    for i, p in enumerate(papers_with_summaries, 1):
        title = p["title"]
        tagline = p.get("summary", "")[:60].replace("\n", " ") if p.get("summary") else ""
        lines.append(f"### {i}. {title} — {tagline}\n")

        venue = p.get("venue", "preprint")
        pub_date = p.get("published") or p.get("publicationDate") or p.get("year", "")
        authors = "; ".join(p.get("authors", [])[:5])
        if len(p.get("authors", [])) > 5:
            authors += " et al."

        lines.append(f"- **来源:** {p.get('arxiv_id', p.get('s2_id', 'N/A'))}")
        lines.append(f"- **期刊/出处:** {venue}")
        lines.append(f"- **发布日期:** {pub_date}")
        lines.append(f"- **作者:** {authors}")

        summary_text = p.get("summary") or ""
        if summary_text:
            if brief := p.get("_brief", False):
                lines.append(f"- **简要摘要:** {summary_text}")
            else:
                lines.append(summary_text)

        has_pdf = p.get("_downloaded", False)
        lines.append(f"- **PDF 状态:** {'✅ 已下载' if has_pdf else '⚠️ 仅摘要'}")

        url = p.get("url") or p.get("pdf_url", "")
        arxiv_id = p.get("arxiv_id", "")
        link = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else url
        lines.append(f"- **原文链接:** {link}")

        tags = p.get("tags", [])
        if tags:
            lines.append(f"- **标签:** {', '.join(tags)}")
        lines.append("")

    # Highlights / Key Gap sections
    lines.append("## 💡 今日亮点\n")
    lines.append("- **最值得精读的一篇:** ...(待补充)")
    lines.append("- **可能与你研究论点冲突的一篇:** ...")
    lines.append("- **值得追踪的作者或团队:** ...\n")

    lines.append("## 📌 Key Gap\n")
    lines.append("{待分析}\n")

    report = "\n".join(lines)
    out_path = reports_dir / f"daily-summary-{TODAY}.md"
    out_path.write_text(report, encoding="utf-8")
    print(f"\n  ✓ 日报已保存: {out_path.name}")
    return report

###############################################################################
# 8. Update seen_papers.json
###############################################################################
def update_seen(papers):
    seen = load_seen()
    for p in papers:
        key = paper_key(p)
        if key not in seen:
            seen[key] = {
                "title": p["title"],
                "date_seen": TODAY,
                "tags": p.get("tags", infer_tags(p["title"], p.get("abstract", ""))),
            }
    save_seen(seen)
    print(f"  ✓ seen_papers.json 已更新 ({len(seen)} 篇总计)")

###############################################################################
# 9. Build Site
###############################################################################
def build_site():
    print("\n  ▶ 运行 generate_site.py...")
    result = subprocess.run(
        [sys.executable, str(SITE_SCRIPT)],
        capture_output=True, text=True, cwd=REPO_DIR,
    )
    for line in result.stdout.split("\n"):
        if line.strip():
            print(f"    {line}")
    if result.returncode != 0:
        print(f"  ✗ generate_site.py 失败:\n{result.stderr}")
    else:
        print("  ✓ 站点已构建")

###############################################################################
# Main
###############################################################################
def main():
    print(f"\n{'='*60}")
    print(f"  📚 每日文献追踪 Pipeline — {TODAY}")
    print(f"{'='*60}\n")

    # 1. Keywords
    print("◆ 1. 加载关键词...")
    kw = load_keywords()
    print(f"   主题 ({len(kw['topics'])}): {', '.join(kw['topics'][:5])}")

    # 2. Search
    print("\n◆ 2a. arXiv 检索...")
    try:
        arxiv_papers = search_arxiv(kw["arxiv_query"], kw["arxiv_max"])
        if not arxiv_papers:
            arxiv_papers = fallback_search_arxiv(kw["arxiv_query"], kw["arxiv_max"])
    except Exception as e:
        print(f"  ✗ arXiv 检索失败: {e}")
        arxiv_papers = []

    s2_available = False
    s2_papers = []
    print("\n◆ 2b. Semantic Scholar 检索...")
    if kw.get("s2_query"):
        if not S2_API_KEY:
            print("  → 跳过 S2（无 API Key）")
        else:
            s2_papers_a, ok = search_s2(kw["s2_query"], kw["s2_limit_a"])
            s2_papers = s2_papers_a
            if ok:
                s2_papers_b, _ = search_s2_oa(kw["s2_query"], kw["s2_limit_b"])
                existing_ids = {p.get("s2_id") for p in s2_papers}
                s2_papers.extend(p for p in s2_papers_b if p.get("s2_id") not in existing_ids)
                s2_available = True
    else:
        print("  → S2 已禁用")

    raw_total = len(arxiv_papers) + len(s2_papers)
    print(f"\n  ✓ 原始候选: {raw_total} 篇")
    if raw_total == 0:
        print("\n⚠️  今日无新论文，任务结束")
        return

    # 3. Dedup
    print("\n◆ 3. 跨天去重...")
    seen = load_seen()
    arxiv_new = dedup_candidates(arxiv_papers, seen)
    s2_new = dedup_candidates(s2_papers, seen)
    after_dedup = len(arxiv_new) + len(s2_new)
    print(f"  → 去重后共 {after_dedup} 篇")

    if after_dedup == 0:
        print("\n⚠️  去重后无新论文，任务结束")
        return

    # 4. Merge
    print("\n◆ 4. 合并去重...")
    top10 = merge_and_dedup(arxiv_new, s2_new)
    print(f"  → TOP {len(top10)} 篇")

    # 5. PDF Download + Summarization
    print("\n◆ 5. 精读/简读论文...")
    deep_read = min(5, len(top10))
    brief_read = max(0, len(top10) - deep_read)

    papers_with_summaries = []
    downloaded_count = 0

    for idx, p in enumerate(top10):
        print(f"\n  [{idx+1}/{len(top10)}] {p['title'][:70]}...")
        is_deep = idx < deep_read

        full_text, downloaded = download_and_extract(p)
        if downloaded:
            downloaded_count += 1
        p["_downloaded"] = downloaded

        print(f"    {'🔍 精读' if is_deep else '📋 简读'}...")
        summary = llm_summarize(full_text, brief=not is_deep)
        p["summary"] = summary
        p["_brief"] = not is_deep
        p["tags"] = infer_tags(p["title"], p.get("abstract", ""))
        p["venue"] = ", ".join(p.get("categories", [])) if p.get("categories") else "arXiv preprint"
        papers_with_summaries.append(p)

        if is_deep and idx < deep_read - 1:
            time.sleep(2)  # rate limit between LLM calls

    # 6. Generate Report
    print("\n◆ 6. 生成日报...")
    stats = {
        "raw_total": raw_total,
        "arxiv_count": len(arxiv_papers),
        "s2_count": len(s2_papers),
        "after_dedup": after_dedup,
        "downloaded": downloaded_count,
        "deep_read": deep_read,
        "s2_available": s2_available,
    }
    generate_report(papers_with_summaries, stats)

    # 7. Update seen_papers
    print("\n◆ 7. 更新已读库...")
    update_seen(papers_with_summaries)

    # 8. Build site
    print("\n◆ 8. 构建站点...")
    build_site()

    print(f"\n{'='*60}")
    print(f"  ✅ Pipeline 完成 — {TODAY}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()

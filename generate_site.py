#!/usr/bin/env python3
"""
Generate a modern card-style HTML site from daily-summary-*.md reports.
Features: day navigation, keyword badges with hyperlinks, keyword aggregation page.
Output: site/index.html + site/keywords.html
"""

import re, json
from pathlib import Path
from html import escape

PROJECT_DIR = Path(__file__).parent
REPORTS_DIR = PROJECT_DIR / "reports"
OUTPUT_DIR = PROJECT_DIR

SEEN_PAPERS_PATH = PROJECT_DIR / "seen_papers.json"

GITHUB_REPO = "yangxl-yuanpei/daily-review-reports"

DAILY_PATTERN = re.compile(r"daily-summary-(\d{4}-\d{2}-\d{2})\.md")

PAPER_BLOCK_RE = re.compile(
    r"### (\d+)\.\s+(.+?)\n"
    r"(.*?)(?=\n### \d+\.|\n## 💡|\n## 📌|$)",
    re.DOTALL,
)

STATS_RE = re.compile(r"-\s*(.+?):\s*(.+)")

def parse_fields(body):
    """Parse - **key**：value or - **key:** value style fields from paper body."""
    fields = {}
    for line in body.split('\n'):
        line = line.strip()
        m = re.match(r'-\s+\*\*(.+?)\*\*(.*)', line)
        if not m:
            continue
        key = m.group(1).strip().rstrip(':：,，')
        rest = m.group(2).strip()
        rest = re.sub(r'^[：:，]?\s*', '', rest)
        if key:
            fields[key] = rest
    return fields

def inline_bold(text):
    """Convert **text** to <strong>text</strong>."""
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)


def load_keyword_index():
    """Load seen_papers.json and build two indexes:
    1. keyword → [(date, title, source_key), ...]  for the keyword page
    2. source_key → [tags, ...]  for daily page badge lookup
    """
    if not SEEN_PAPERS_PATH.exists():
        return {}, {}
    data = json.loads(SEEN_PAPERS_PATH.read_text(encoding="utf-8"))

    kw_index = {}
    tags_lookup = {}
    for key, info in data.items():
        key_lower = key.lower().strip()
        tags = info.get("tags", [])
        date = info.get("date_seen", "unknown")
        title = info.get("title", key)
        tags_lookup[key_lower] = tags

        for tag in tags:
            tag_lower = tag.lower()
            if tag_lower not in kw_index:
                kw_index[tag_lower] = {"tag": tag, "papers": []}
            kw_index[tag_lower]["papers"].append({
                "date": date,
                "title": title,
                "source_key": key,
            })

    for tag in kw_index:
        kw_index[tag]["papers"].sort(key=lambda p: p["date"], reverse=True)

    return kw_index, tags_lookup


def extract_source_key(fields):
    """Extract a normalized source key from paper fields for tag lookup."""
    source = fields.get("来源", "")
    m = re.search(r'arXiv[:\s]*(\d+\.\d+)', source, re.IGNORECASE)
    if m:
        return f"arxiv:{m.group(1)}"
    m = re.search(r'S2 ID[:\s]*(\d+)', source, re.IGNORECASE)
    if m:
        return f"s2:{m.group(1)}"
    return None


def parse_summary(filepath, tags_lookup=None):
    """Parse a daily summary markdown file into structured data."""
    text = filepath.read_text(encoding="utf-8")
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", filepath.name)
    date_str = date_match.group(1) if date_match else "unknown"

    # Extract title
    title_match = re.search(r"#\s+(.+)", text)
    title = title_match.group(1) if title_match else date_str

    # Extract statistics
    stats = {}
    stats_section = re.search(
        r"## 📊 统计概览\n(.*?)(?=\n## )", text, re.DOTALL
    )
    if stats_section:
        for line in stats_section.group(1).strip().split("\n"):
            m = STATS_RE.match(line.strip())
            if m:
                stats[m.group(1).strip()] = m.group(2).strip()

    # Extract papers
    papers = []
    paper_section = re.search(
        r"## 📑 论文详情.*?\n(.*?)(?=\n## 💡|\n## 📌|$)", text, re.DOTALL
    )
    if paper_section:
        block_text = paper_section.group(1)
        # Split on real paper headings: use ⭐ if present, otherwise split on all ### N.
        has_stars = bool(re.search(r"### \d+\.\s+.+?⭐", block_text))
        split_re = r"\n(?=### \d+\.\s+.+?⭐)" if has_stars else r"\n(?=### \d+\.)"
        blocks = re.split(split_re, block_text)
        for block in blocks:
            if not block.strip():
                continue
            header_match = re.match(r"### (\d+)\.\s+(.+?)(?:\n|$)", block)
            if not header_match:
                continue
            num = header_match.group(1)
            title_str = header_match.group(2).strip()
            body = block[header_match.end():]
            fields = parse_fields(body)

            # relevance tag: check structured field first, then fallback to body text
            relevance = ""
            rel_field = fields.get("与你研究的相关度", fields.get("与你研究的相关性", ""))
            if "高" in rel_field and "低" not in rel_field:
                relevance = "high"
            elif "中" in rel_field:
                relevance = "medium"
            elif "低" in rel_field:
                relevance = "low"
            if not relevance:
                body_lower = body.lower()
                if re.search(r'与你研究的相关度[：:].*?[。；;]?\s*\*{0,2}高', body_lower):
                    relevance = "high"
                elif re.search(r'与你研究的相关度[：:].*?[。；;]?\s*\*{0,2}中', body_lower):
                    relevance = "medium"
                elif re.search(r'与你研究的相关度[：:].*?[。；;]?\s*\*{0,2}低', body_lower):
                    relevance = "low"
            if not relevance:
                rel_match = re.search(r'相关度\s*(高|中|低)', body)
                if rel_match:
                    relevance = {"高": "high", "中": "medium", "低": "low"}[rel_match.group(1)]

            # Look up tags from seen_papers.json
            paper_tags = []
            if tags_lookup:
                source_key = extract_source_key(fields)
                if source_key and source_key.lower() in tags_lookup:
                    paper_tags = tags_lookup[source_key.lower()]

            # Generate Google Scholar search URL
            scholar_query = title_str
            author_match = re.match(r'(.+?)\s*[—–-]', title_str)
            if author_match:
                scholar_query = author_match.group(1).strip()
            scholar_url = (
                f"https://scholar.google.com/scholar?q={escape(scholar_query)}"
            )

            papers.append({
                "number": num,
                "title": title_str,
                "fields": fields,
                "relevance": relevance,
                "tags": paper_tags,
                "scholar_url": scholar_url,
                "body": block.strip(),
            })

    # Extract highlights section
    highlights_section = re.search(
        r"## 💡 今日亮点\n(.*?)(?=\n## 📌|$)", text, re.DOTALL
    )
    highlights = highlights_section.group(1).strip() if highlights_section else ""

    # Extract key gap
    gap_section = re.search(r"## 📌 Key Gap\n(.*?)$", text, re.DOTALL)
    key_gap = gap_section.group(1).strip() if gap_section else ""

    return {
        "date": date_str,
        "title": title,
        "stats": stats,
        "papers": papers,
        "highlights": highlights,
        "key_gap": key_gap,
    }

BASE_CSS = """
:root {
  --bg: #f5f7fa;
  --card-bg: #ffffff;
  --text: #1a1a2e;
  --text-secondary: #555;
  --accent: #2563eb;
  --accent-light: #dbeafe;
  --border: #e2e8f0;
  --high: #dc2626;
  --high-bg: #fef2f2;
  --medium: #d97706;
  --medium-bg: #fffbeb;
  --low: #6b7280;
  --low-bg: #f9fafb;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  background: var(--bg); color: var(--text); line-height: 1.7;
  padding: 0;
}
.container { max-width: 1200px; margin: 0 auto; padding: 24px 16px; }
header {
  background: linear-gradient(135deg, #1e3a5f, #2563eb);
  color: white; padding: 32px 0 24px; margin-bottom: 24px;
  border-radius: 0 0 24px 24px;
}
header .container { padding-bottom: 0; }
header h1 { font-size: 1.5rem; font-weight: 700; }
header p { font-size: 0.9rem; opacity: 0.8; margin-top: 4px; }
  .stats-line {
    background: var(--card-bg); border-radius: 10px; padding: 12px 18px;
    margin-bottom: 20px; border: 1px solid var(--border);
    font-size: 0.85rem; color: var(--text);
    text-align: center; line-height: 1.6;
  }
.papers-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 16px; margin-bottom: 24px;
}
.paper-card {
  background: var(--card-bg); border-radius: 12px; padding: 20px;
  border: 1px solid var(--border);
  transition: box-shadow 0.15s;
  display: flex; flex-direction: column;
}
.paper-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.06); }
.paper-card.high { border-left: 4px solid var(--high); }
.paper-card.medium { border-left: 4px solid var(--medium); }
.paper-card.low { border-left: 4px solid var(--low); }
.paper-header { display: flex; justify-content: flex-end; align-items: center; margin-bottom: 8px; }
.relevance-badge {
  padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: 600;
}
.relevance-badge.high { background: var(--high-bg); color: var(--high); }
.relevance-badge.medium { background: var(--medium-bg); color: var(--medium); }
.relevance-badge.low { background: var(--low-bg); color: var(--low); }
.paper-title { font-size: 1rem; font-weight: 600; margin-bottom: 12px; line-height: 1.4; }
.paper-title a { color: inherit; text-decoration: none; }
.paper-title a:hover { color: var(--accent); text-decoration: underline; }
.paper-fields { flex: 1; }
.field { margin-bottom: 8px; font-size: 0.82rem; line-height: 1.5; }
.field-key {
  display: block; font-weight: 600; font-size: 0.72rem;
  text-transform: uppercase; letter-spacing: 0.03em;
  color: var(--text-secondary); margin-bottom: 2px;
}
.field-val { color: var(--text); display: block; }
.field-collapsible .field-val { max-height: 4.5em; overflow: hidden; position: relative; cursor: pointer; }
.field-collapsible .field-val::after { content: '... 点击展开'; position: absolute; bottom: 0; right: 0; background: var(--card-bg); padding: 0 4px; font-size: 0.72rem; color: var(--accent); font-weight: 600; }
.field-collapsible.expanded .field-val { max-height: none; }
.field-collapsible.expanded .field-val::after { content: ''; }
.expand-all-btn { display: inline-block; margin-bottom: 12px; padding: 4px 12px; border-radius: 6px; background: var(--accent-light); color: var(--accent); border: none; font-size: 0.78rem; font-weight: 500; cursor: pointer; transition: all 0.12s; }
.expand-all-btn:hover { background: var(--accent); color: #fff; }
.highlights, .keygap {
  background: var(--card-bg); border-radius: 12px; padding: 20px;
  margin-bottom: 16px; border: 1px solid var(--border);
}
.highlights h3, .keygap h3 { font-size: 1rem; margin-bottom: 8px; }
.highlight-body, .gap-body { font-size: 0.88rem; color: var(--text); line-height: 1.7; display: flex; flex-direction: column; gap: 10px; }
.highlight-body p, .gap-body p { margin-bottom: 6px; }
.highlight-body strong, .gap-body strong { font-weight: 600; }
.highlight-item, .gap-item { background: var(--bg); border-radius: 8px; padding: 12px 14px; border-left: 3px solid var(--accent); }
.highlight-item-key, .gap-item-key { font-weight: 600; font-size: 0.82rem; color: var(--accent); display: block; margin-bottom: 4px; }
.highlight-item-val, .gap-item-val { font-size: 0.88rem; color: var(--text); line-height: 1.7; }
.paper-tags { margin-top: 10px; display: flex; gap: 6px; flex-wrap: wrap; }
.tag-badge {
  display: inline-block; padding: 2px 10px; border-radius: 999px;
  font-size: 0.72rem; font-weight: 500;
  background: var(--accent-light); color: var(--accent);
  text-decoration: none; border: 1px solid transparent;
  transition: all 0.12s;
}
.tag-badge:hover { background: var(--accent); color: #fff; border-color: var(--accent); }
.kw-nav {
  display: inline-block; margin-left: 12px;
  padding: 6px 14px; border-radius: 8px;
  background: rgba(255,255,255,0.15); color: #fff;
  text-decoration: none; font-size: 0.82rem; font-weight: 500;
  transition: background 0.12s;
}
.kw-nav:hover { background: rgba(255,255,255,0.25); }
.day-nav { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 24px; }
.day-link {
  padding: 8px 16px; border: 1px solid var(--border);
  border-radius: 8px; background: var(--card-bg);
  text-decoration: none; font-size: 0.85rem; font-weight: 500;
  color: var(--text); transition: all 0.15s;
}
.day-link:hover { border-color: var(--accent); color: var(--accent); }
.back-link { color: rgba(255,255,255,0.8); text-decoration: none; font-size: 0.85rem; }
.back-link:hover { color: #fff; }
@media (max-width: 640px) {
    .papers-grid { grid-template-columns: 1fr; }
  header h1 { font-size: 1.2rem; }
}
"""

FIELD_MAP = {
    "作者": ["作者"],
    "核心问题": ["核心问题"],
    "主要方法": ["方法核心", "方法要点"],
    "方法创新": ["创新点"],
    "主要结果": ["关键实验与结果", "关键结果"],
}

def render_papers_cards(papers):
    cards = ""
    for p in papers:
        rel_class = p["relevance"]
        fields_html = ""
        for disp_name, aliases in FIELD_MAP.items():
            val = None
            for a in aliases:
                if a in p["fields"]:
                    val = p["fields"][a]
                    break
            if not val:
                continue
            collapsible = ' field-collapsible' if len(val) > 160 else ''
            fields_html += (
                f'<div class="field{collapsible}"><span class="field-key">{escape(disp_name)}</span>'
                f'<span class="field-val">{inline_bold(escape(val))}</span></div>'
            )
        tags_html = ""
        if p.get("tags"):
            tags_html = '<div class="paper-tags">'
            for tag in p["tags"]:
                slug = tag.lower().replace(" ", "-")
                tags_html += f'<a href="keywords.html#{slug}" class="tag-badge">{escape(tag)}</a>'
            tags_html += "</div>"
        paper_url = p['fields'].get('原文链接', '')
        if not paper_url:
            src = p['fields'].get('来源', '')
            arxiv_m = re.search(r'arXiv[:\s]*(\d+\.\d+)', src, re.IGNORECASE)
            if arxiv_m:
                paper_url = f"https://arxiv.org/abs/{arxiv_m.group(1)}"
        if not paper_url:
            paper_url = p['scholar_url']
        cards += f"""
            <div class="paper-card {rel_class}">
                <div class="paper-header">
                    <span class="relevance-badge {rel_class}">{p['relevance'].upper() if p['relevance'] else '?'}</span>
                </div>
                <h3 class="paper-title"><a href="{paper_url}" target="_blank">{escape(p['title'])}</a></h3>
                <div class="paper-fields">{fields_html}</div>
                {tags_html}
            </div>"""
    return cards

def render_structured_items(text, cls):
    if not text:
        return ""
    items = []
    for line in text.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        m = re.match(r'- \*\*(.+?)\*\*[：:]\s*(.*)', line)
        if m:
            items.append((m.group(1).strip(), m.group(2).strip()))
    if not items:
        return f'<div class="{cls}-body">{markdown_to_html(text)}</div>'
    cards = "".join(
        f'<div class="{cls}-item">'
        f'<span class="{cls}-item-key">{escape(k)}</span>'
        f'<span class="{cls}-item-val">{inline_bold(escape(v))}</span>'
        f'</div>'
        for k, v in items
    )
    return f'<div class="{cls}-body">{cards}</div>'

KATEX_HEAD = """<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}]})"></script>"""

TOGGLE_SCRIPT = """<script>
(function(){var b=document.getElementById('expandAllBtn'),e=false;b&&b.addEventListener('click',function(){e=!e;document.querySelectorAll('.field-collapsible').forEach(function(t){t.classList.toggle('expanded',e)});b.textContent=e?'\U0001f4d6 \u6536\u8d77\u5168\u90e8':'\U0001f4d6 \u5c55\u5f00\u5168\u90e8'});document.querySelector('.papers-grid')&&document.querySelector('.papers-grid').addEventListener('click',function(e){var t=e.target.closest('.field-collapsible');t&&t.classList.toggle('expanded')})})();
</script>"""

def render_daily_page(report):
    source = report["stats"].get("检索源", "")
    dedup = report["stats"].get("有效去重后", "")
    reading = report["stats"].get("实际精读", report["stats"].get("精读", ""))
    parts = []
    if source:
        parts.append(f"🔍 {escape(source)}")
    if dedup:
        parts.append(f"📌 有效去重后: {escape(dedup)}")
    if reading:
        parts.append(f"📖 {escape(reading)}")
    stats_line = f'<div class="stats-line">{" | ".join(parts)}</div>' if parts else ""
    papers_html = render_papers_cards(report["papers"])
    highlights_html = f'<div class="highlights"><h3>💡 今日亮点</h3>{render_structured_items(report["highlights"], "highlight")}</div>' if report["highlights"] else ""
    gap_html = f'<div class="keygap"><h3>📌 Key Gap</h3>{render_structured_items(report["key_gap"], "gap")}</div>' if report["key_gap"] else ""

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(report['title'])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{KATEX_HEAD}
<style>{BASE_CSS}</style>
</head>
<body>
<header>
  <div class="container">
    <h1>{escape(report['title'])}</h1>
    <p><a href="index.html" class="back-link">← 返回索引</a> &nbsp; <a href="keywords.html" class="kw-nav">🏷️ 关键词索引</a></p>
  </div>
</header>
<div class="container">
  {stats_line}
  <button class="expand-all-btn" id="expandAllBtn">📖 展开全部</button>
  <div class="papers-grid">{papers_html}</div>
  {highlights_html}
  {gap_html}
</div>
{TOGGLE_SCRIPT}
</body>
</html>"""

def render_index_page(reports, kw_index=None):
    reports_sorted = sorted(reports, key=lambda r: r["date"], reverse=True)
    day_links = "".join(
        f'<a href="{r["date"]}.html" class="day-link">{r["date"]}</a>'
        for r in reports_sorted
    )
    total_papers = sum(len(r["papers"]) for r in reports_sorted)

    kw_section = ""
    if kw_index:
        sorted_tags = sorted(kw_index.keys())
        kw_badges = ""
        for slug in sorted_tags:
            entry = kw_index[slug]
            count = len(entry["papers"])
            kw_badges += f'<a href="keywords.html#{slug}" class="kw-badge">{escape(entry["tag"])}<span class="kw-badge-count">{count}</span></a>'
        kw_section = f"""
  <h2 style="font-size:1.1rem;font-weight:700;margin:24px 0 12px;">🏷️ 关键词</h2>
  <div class="kw-cloud">{kw_badges}</div>"""

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>每日文献追踪</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{BASE_CSS}
.kw-cloud {{
  display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px;
}}
.kw-badge {{
  display: inline-flex; align-items: center; gap: 6px;
  padding: 6px 14px; border-radius: 999px;
  background: var(--accent-light); color: var(--accent);
  text-decoration: none; font-size: 0.82rem; font-weight: 500;
  border: 1px solid transparent; transition: all 0.12s;
}}
.kw-badge:hover {{
  background: var(--accent); color: #fff; border-color: var(--accent);
}}
.kw-badge-count {{
  font-size: 0.7rem; font-weight: 600; opacity: 0.7;
}}
.kw-badge:hover .kw-badge-count {{ opacity: 1; }}
</style>
</head>
<body>
<header>
  <div class="container">
    <h1>📄 每日文献追踪报告</h1>
    <p>arXiv + Semantic Scholar | 自动检索 · 精读 · 关键缺口分析
    <a href="keywords.html" class="kw-nav">🏷️ 关键词索引</a>
    <a href="https://github.com/{GITHUB_REPO}/issues/new?template=keyword-suggestion.md" target="_blank" class="kw-nav">🖊️ 新增关键词</a></p>
  </div>
</header>
<div class="container">
  <div class="day-nav">{day_links}</div>
  <p style="color:var(--text-secondary);font-size:0.85rem;margin-bottom:8px;">共 {len(reports_sorted)} 天报告，{total_papers} 篇论文</p>
  {kw_section}
</div>
</body>
</html>"""

def markdown_to_html(md_text):
    """Simple markdown to HTML conversion for highlights/gap text."""
    lines = md_text.strip().split("\n")
    html_parts = []
    for line in lines:
        line = line.strip()
        if not line:
            html_parts.append("<br>")
        elif line.startswith("- "):
            html_parts.append(f"<li>{inline_bold(escape(line[2:]))}</li>")
        elif line.startswith("**") and ":**" in line:
            parts = line.split(":**", 1)
            key = parts[0].strip("*").strip()
            val = parts[1].strip() if len(parts) > 1 else ""
            html_parts.append(
                f"<p><strong>{escape(key)}:</strong> {inline_bold(escape(val))}</p>"
            )
        else:
            html_parts.append(f"<p>{inline_bold(escape(line))}</p>")
    return "".join(html_parts)

def render_keywords_html(kw_index):
    """Generate keywords.html — a page listing all keywords with their papers."""
    if not kw_index:
        return ""

    sorted_tags = sorted(kw_index.keys())
    total_papers = sum(len(entry["papers"]) for entry in kw_index.values())

    nav_links = "".join(
        f'<a href="#{slug}" class="kw-nav-link">{escape(kw_index[slug]["tag"])}<span class="kw-count">{len(kw_index[slug]["papers"])}</span></a>'
        for slug in sorted_tags
    )

    sections = ""
    for slug in sorted_tags:
        entry = kw_index[slug]
        tag = entry["tag"]
        papers_list = ""
        for p in entry["papers"]:
            papers_list += f"""
            <div class="kw-paper">
                <span class="kw-paper-date">{p["date"]}</span>
                <span class="kw-paper-title">{escape(p["title"])}</span>
            </div>"""

        sections += f"""
        <section id="{slug}" class="kw-section">
            <h2 class="kw-section-title">{escape(tag)} <span class="kw-section-count">{len(entry["papers"])} 篇</span></h2>
            <div class="kw-paper-list">{papers_list}</div>
        </section>"""

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>关键词索引 - 每日文献追踪</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}]}})"></script>
<style>
  :root {{ --bg: #f5f7fa; --card-bg: #fff; --text: #1a1a2e; --text-secondary: #555; --accent: #2563eb; --accent-light: #dbeafe; --border: #e2e8f0; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); line-height: 1.7; padding: 0; }}
  .container {{ max-width: 1000px; margin: 0 auto; padding: 24px 16px; }}

  header {{
    background: linear-gradient(135deg, #1e3a5f, #2563eb);
    color: white; padding: 32px 0 24px; margin-bottom: 24px;
    border-radius: 0 0 24px 24px;
  }}
  header .container {{ padding-bottom: 0; }}
  header h1 {{ font-size: 1.5rem; font-weight: 700; }}
  header p {{ font-size: 0.9rem; opacity: 0.8; margin-top: 4px; }}
  .back-link {{ color: rgba(255,255,255,0.8); text-decoration: none; font-size: 0.85rem; }}
  .back-link:hover {{ color: #fff; }}

  .kw-summary {{ font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 20px; }}

  .kw-nav {{ display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 28px; padding-bottom: 20px; border-bottom: 1px solid var(--border); }}
  .kw-nav-link {{
    padding: 6px 14px; border-radius: 999px; background: var(--card-bg);
    border: 1px solid var(--border); text-decoration: none; font-size: 0.82rem;
    color: var(--text); transition: all 0.12s; display: inline-flex; align-items: center; gap: 6px;
  }}
  .kw-nav-link:hover {{ border-color: var(--accent); color: var(--accent); }}
  .kw-count {{ font-size: 0.7rem; color: var(--text-secondary); font-weight: 600; }}

  .kw-section {{
    background: var(--card-bg); border-radius: 12px; padding: 20px;
    margin-bottom: 16px; border: 1px solid var(--border);
  }}
  .kw-section-title {{ font-size: 1rem; font-weight: 700; margin-bottom: 12px; }}
  .kw-section-count {{ font-size: 0.78rem; font-weight: 400; color: var(--text-secondary); margin-left: 8px; }}

  .kw-paper-list {{ display: flex; flex-direction: column; gap: 6px; }}
  .kw-paper {{
    display: flex; align-items: center; gap: 12px;
    padding: 6px 10px; border-radius: 6px; font-size: 0.85rem;
    transition: background 0.1s;
  }}
  .kw-paper:hover {{ background: var(--bg); }}
  .kw-paper-date {{
    flex-shrink: 0; font-size: 0.75rem; font-weight: 600;
    color: var(--accent); background: var(--accent-light);
    padding: 1px 8px; border-radius: 4px;
  }}
  .kw-paper-title {{ color: var(--text); }}

  @media (max-width: 640px) {{
    header h1 {{ font-size: 1.2rem; }}
  }}
</style>
</head>
<body>
<header>
  <div class="container">
    <h1>🏷️ 关键词索引</h1>
    <p><a href="index.html" class="back-link">← 返回每日报告</a></p>
  </div>
</header>
<div class="container">
  <p class="kw-summary">共 {len(sorted_tags)} 个关键词，涵盖 {total_papers} 篇论文</p>
  <div class="kw-nav">{nav_links}</div>
  {sections}
</div>
</body>
</html>"""


def main():
    reports = []

    kw_index, tags_lookup = load_keyword_index()

    for fp in sorted(REPORTS_DIR.glob("daily-summary-*.md")):
        m = DAILY_PATTERN.match(fp.name)
        if m:
            try:
                parsed = parse_summary(fp, tags_lookup)
                reports.append(parsed)
                print(f"  ✓ {fp.name} ({len(parsed['papers'])} papers)")
            except Exception as e:
                print(f"  ✗ {fp.name}: {e}")

    if not reports:
        print("No daily summaries found.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Generate per-day pages
    for r in reports:
        daily_html = render_daily_page(r)
        path = OUTPUT_DIR / f"{r['date']}.html"
        path.write_text(daily_html, encoding="utf-8")
        print(f"  ✓ {path}")

    # Generate index page
    index_html = render_index_page(reports, kw_index)
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"  ✓ {OUTPUT_DIR / 'index.html'}")

    # Generate keywords page
    kw_html = render_keywords_html(kw_index)
    (OUTPUT_DIR / "keywords.html").write_text(kw_html, encoding="utf-8")
    print(f"  ✓ {OUTPUT_DIR / 'keywords.html'}")

    total = sum(len(r['papers']) for r in reports)
    print(f"\nDone! {len(reports)} daily reports, {total} papers, {len(kw_index)} keywords")

if __name__ == "__main__":
    main()

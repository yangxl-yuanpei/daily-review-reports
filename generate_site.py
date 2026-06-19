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
OUTPUT_DIR = PROJECT_DIR / "site"

SEEN_PAPERS_PATH = PROJECT_DIR / "seen_papers.json"

DAILY_PATTERN = re.compile(r"daily-summary-(\d{4}-\d{2}-\d{2})\.md")

PAPER_BLOCK_RE = re.compile(
    r"### (\d+)\.\s+(.+?)\n"
    r"(.*?)(?=\n### \d+\.|\n## 💡|\n## 📌|$)",
    re.DOTALL,
)

FIELD_RE = re.compile(r"-\s*\*\*(.+?):\*\*\s*(.*)")

STATS_RE = re.compile(r"-\s*(.+?):\s*(.+)")

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
        blocks = re.split(r"\n(?=### \d+\.)", block_text)
        for block in blocks:
            if not block.strip():
                continue
            header_match = re.match(r"### (\d+)\.\s+(.+?)(?:\n|$)", block)
            if not header_match:
                continue
            num = header_match.group(1)
            title_str = header_match.group(2).strip()
            body = block[header_match.end():]
            fields = {}
            for fm in FIELD_RE.finditer(body):
                key = fm.group(1).strip()
                val = fm.group(2).strip()
                fields[key] = val

            # relevance tag
            relevance = ""
            rel_field = fields.get("与你研究的相关性", fields.get("与你研究的相关性:", ""))
            if "高" in rel_field and "低" not in rel_field:
                relevance = "high"
            elif "中" in rel_field:
                relevance = "medium"
            elif "低" in rel_field:
                relevance = "low"

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

def render_html(all_reports):
    """Render all parsed reports into a single modern card-style HTML page.
    Adds keyword badges linking to keywords.html and a nav link to the keyword page.
    """
    reports_sorted = sorted(all_reports, key=lambda r: r["date"], reverse=True)

    # Navigation tabs (day by day)
    nav_items = "".join(
        f'<button class="day-tab {"active" if i==0 else ""}" '
        f'onclick="switchDay({i})">{r["date"]}</button>'
        for i, r in enumerate(reports_sorted)
    )

    # Report content for each day
    day_contents = []
    for ri, report in enumerate(reports_sorted):
        active = "active" if ri == 0 else ""

        # Stats cards
        stats_cards = ""
        for key, val in report["stats"].items():
            stats_cards += f'<div class="stat-card"><div class="stat-label">{escape(key)}</div><div class="stat-value">{escape(val)}</div></div>'

        # Papers
        papers_html = ""
        for p in report["papers"]:
            rel_class = p["relevance"]
            fields_html = ""
            for key, val in p["fields"].items():
                fields_html += (
                    f'<div class="field"><span class="field-key">{escape(key)}</span>'
                    f'<span class="field-val">{escape(val)}</span></div>'
                )

            # Keyword badges
            tags_html = ""
            if p.get("tags"):
                tags_html = '<div class="paper-tags">'
                for tag in p["tags"]:
                    slug = tag.lower().replace(" ", "-")
                    tags_html += f'<a href="keywords.html#{slug}" class="tag-badge">{escape(tag)}</a>'
                tags_html += "</div>"

            papers_html += f"""
            <div class="paper-card {rel_class}">
                <div class="paper-header">
                    <span class="paper-num">#{p['number']}</span>
                    <span class="relevance-badge {rel_class}">{p['relevance'].upper() if p['relevance'] else '?'}</span>
                </div>
                <h3 class="paper-title">{escape(p['title'])}</h3>
                <div class="paper-fields">{fields_html}</div>
                {tags_html}
                <div class="paper-links">
                    <a href="{p['scholar_url']}" target="_blank" class="scholar-link">🔍 Google Scholar</a>
                </div>
            </div>"""

        # Highlights + Key Gap
        highlights_html = ""
        if report["highlights"]:
            highlights_html = f'<div class="highlights"><h3>💡 今日亮点</h3><div class="highlight-body">{markdown_to_html(report["highlights"])}</div></div>'

        gap_html = ""
        if report["key_gap"]:
            gap_html = f'<div class="keygap"><h3>📌 Key Gap</h3><div class="gap-body">{markdown_to_html(report["key_gap"])}</div></div>'

        day_contents.append(f"""
        <div class="day-content {active}" data-day="{ri}">
            <div class="stats-row">{stats_cards}</div>
            <div class="papers-grid">{papers_html}</div>
            {highlights_html}
            {gap_html}
        </div>""")

    day_js = "\n".join(
        f"contents[{i}] = document.getElementById('day-{i}');"
        for i in range(len(reports_sorted))
    )

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>每日文献追踪</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {{
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
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background: var(--bg); color: var(--text); line-height: 1.7;
    padding: 0;
  }}
  .container {{ max-width: 1200px; margin: 0 auto; padding: 24px 16px; }}

  /* Header */
  header {{
    background: linear-gradient(135deg, #1e3a5f, #2563eb);
    color: white; padding: 32px 0 24px; margin-bottom: 24px;
    border-radius: 0 0 24px 24px;
  }}
  header .container {{ padding-bottom: 0; }}
  header h1 {{ font-size: 1.5rem; font-weight: 700; }}
  header p {{ font-size: 0.9rem; opacity: 0.8; margin-top: 4px; }}

  /* Day navigation */
  .day-nav {{
    display: flex; gap: 8px; flex-wrap: wrap;
    margin-bottom: 24px;
  }}
  .day-tab {{
    padding: 8px 16px; border: 1px solid var(--border);
    border-radius: 8px; background: var(--card-bg);
    cursor: pointer; font-size: 0.85rem; font-weight: 500;
    transition: all 0.15s;
  }}
  .day-tab:hover {{ border-color: var(--accent); color: var(--accent); }}
  .day-tab.active {{
    background: var(--accent); color: white; border-color: var(--accent);
  }}

  /* Day content toggle */
  .day-content {{ display: none; }}
  .day-content.active {{ display: block; }}

  /* Stats */
  .stats-row {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 12px; margin-bottom: 24px;
  }}
  .stat-card {{
    background: var(--card-bg); border-radius: 12px; padding: 16px;
    text-align: center; border: 1px solid var(--border);
  }}
  .stat-label {{ font-size: 0.75rem; color: var(--text-secondary); margin-bottom: 4px; }}
  .stat-value {{ font-size: 1.1rem; font-weight: 700; color: var(--accent); }}

  /* Papers grid */
  .papers-grid {{
    display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 16px; margin-bottom: 24px;
  }}
  .paper-card {{
    background: var(--card-bg); border-radius: 12px; padding: 20px;
    border: 1px solid var(--border);
    transition: box-shadow 0.15s;
    display: flex; flex-direction: column;
  }}
  .paper-card:hover {{ box-shadow: 0 4px 12px rgba(0,0,0,0.06); }}
  .paper-card.high {{ border-left: 4px solid var(--high); }}
  .paper-card.medium {{ border-left: 4px solid var(--medium); }}
  .paper-card.low {{ border-left: 4px solid var(--low); }}
  .paper-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }}
  .paper-num {{ font-weight: 700; color: var(--accent); font-size: 0.9rem; }}
  .relevance-badge {{
    padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: 600;
  }}
  .relevance-badge.high {{ background: var(--high-bg); color: var(--high); }}
  .relevance-badge.medium {{ background: var(--medium-bg); color: var(--medium); }}
  .relevance-badge.low {{ background: var(--low-bg); color: var(--low); }}
  .paper-title {{ font-size: 1rem; font-weight: 600; margin-bottom: 12px; line-height: 1.4; }}
  .paper-fields {{ flex: 1; }}
  .field {{
    margin-bottom: 8px; font-size: 0.82rem; line-height: 1.5;
  }}
  .field-key {{
    display: block; font-weight: 600; font-size: 0.72rem;
    text-transform: uppercase; letter-spacing: 0.03em;
    color: var(--text-secondary); margin-bottom: 2px;
  }}
  .field-val {{ color: var(--text); display: block; }}
  .paper-links {{ margin-top: 12px; padding-top: 12px; border-top: 1px solid var(--border); }}
  .scholar-link {{
    color: var(--accent); text-decoration: none; font-size: 0.82rem; font-weight: 500;
  }}
  .scholar-link:hover {{ text-decoration: underline; }}

  /* Highlights + Key Gap */
  .highlights, .keygap {{
    background: var(--card-bg); border-radius: 12px; padding: 20px;
    margin-bottom: 16px; border: 1px solid var(--border);
  }}
  .highlights h3, .keygap h3 {{ font-size: 1rem; margin-bottom: 8px; }}
  .highlight-body, .gap-body {{ font-size: 0.88rem; color: var(--text); line-height: 1.7; }}
  .highlight-body p, .gap-body p {{ margin-bottom: 6px; }}
  .highlight-body strong, .gap-body strong {{ font-weight: 600; }}

  /* Tag badges */
  .paper-tags {{
    margin-top: 10px; display: flex; gap: 6px; flex-wrap: wrap;
  }}
  .tag-badge {{
    display: inline-block; padding: 2px 10px; border-radius: 999px;
    font-size: 0.72rem; font-weight: 500;
    background: var(--accent-light); color: var(--accent);
    text-decoration: none; border: 1px solid transparent;
    transition: all 0.12s;
  }}
  .tag-badge:hover {{
    background: var(--accent); color: #fff; border-color: var(--accent);
  }}

  /* Keywords nav link */
  .kw-nav {{
    display: inline-block; margin-left: 12px;
    padding: 6px 14px; border-radius: 8px;
    background: rgba(255,255,255,0.15); color: #fff;
    text-decoration: none; font-size: 0.82rem; font-weight: 500;
    transition: background 0.12s;
  }}
  .kw-nav:hover {{ background: rgba(255,255,255,0.25); }}

  /* Responsive */
  @media (max-width: 640px) {{
    .papers-grid {{ grid-template-columns: 1fr; }}
    .stats-row {{ grid-template-columns: repeat(2, 1fr); }}
    header h1 {{ font-size: 1.2rem; }}
  }}
</style>
</head>
<body>
<header>
  <div class="container">
    <h1>📄 每日文献追踪报告</h1>
    <p>arXiv + Semantic Scholar | 自动检索 · 精读 · 关键缺口分析
    <a href="keywords.html" class="kw-nav">🏷️ 关键词索引</a></p>
  </div>
</header>
<div class="container">
  <div class="day-nav">{nav_items}</div>
  {''.join(day_contents)}
</div>
<script>
  const contents = {{}};
  {day_js}
  const tabs = document.querySelectorAll('.day-tab');
  tabs.forEach(t => t.addEventListener('click', () => {{
    tabs.forEach(tab => tab.classList.remove('active'));
    t.classList.add('active');
    const idx = Array.from(tabs).indexOf(t);
    document.querySelectorAll('.day-content').forEach(d => d.classList.remove('active'));
    const target = document.querySelector(`.day-content[data-day="${{idx}}"]`);
    if (target) target.classList.add('active');
  }}));
</script>
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
            html_parts.append(f"<li>{escape(line[2:])}</li>")
        elif line.startswith("**") and ":**" in line:
            parts = line.split(":**", 1)
            key = parts[0].strip("*").strip()
            val = parts[1].strip() if len(parts) > 1 else ""
            html_parts.append(
                f"<p><strong>{escape(key)}:</strong> {escape(val)}</p>"
            )
        else:
            html_parts.append(f"<p>{escape(line)}</p>")
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

    html = render_html(reports)
    (OUTPUT_DIR / "index.html").write_text(html, encoding="utf-8")
    print(f"  ✓ {OUTPUT_DIR / 'index.html'}")

    kw_html = render_keywords_html(kw_index)
    (OUTPUT_DIR / "keywords.html").write_text(kw_html, encoding="utf-8")
    print(f"  ✓ {OUTPUT_DIR / 'keywords.html'}")

    print(f"\nDone! {len(reports)} daily reports, {sum(len(r['papers']) for r in reports)} papers, {len(kw_index)} keywords")

if __name__ == "__main__":
    main()

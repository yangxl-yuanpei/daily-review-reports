#!/usr/bin/env python3
"""
Generate a modern card-style HTML site from daily-summary-*.md reports.
Architecture: index.html (day listing) + daily-YYYY-MM-DD.html (per-day detail).
"""

import re, json, hashlib
from pathlib import Path
from datetime import datetime
from html import escape

KEYWORDS_FILE = Path(__file__).parent / "keywords.json"

DESKTOP_DIR = Path("/mnt/c/Users/94474/Desktop/daily-review-reports")
REPORTS_DIR = DESKTOP_DIR / "reports"
OUTPUT_DIR = DESKTOP_DIR  # root for GitHub Pages

DAILY_PATTERN = re.compile(r"daily-summary-(\d{4}-\d{2}-\d{2})\.md")

FIELD_RE = re.compile(r"-\s*\*\*(.+?):\*\*\s*(.*)")

STATS_RE = re.compile(r"-\s*(.+?):\s*(.+)")

def parse_summary(filepath):
    """Parse a daily summary markdown file into structured data."""
    text = filepath.read_text(encoding="utf-8")
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", filepath.name)
    date_str = date_match.group(1) if date_match else "unknown"

    title_match = re.search(r"#\s+(.+)", text)
    title = title_match.group(1) if title_match else date_str

    stats = {}
    stats_section = re.search(
        r"## 📊 统计概览\n(.*?)(?=\n## )", text, re.DOTALL
    )
    if stats_section:
        for line in stats_section.group(1).strip().split("\n"):
            m = STATS_RE.match(line.strip())
            if m:
                stats[m.group(1).strip()] = m.group(2).strip()

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

            relevance = ""
            rel_field = fields.get("与你研究的相关性", fields.get("与你研究的相关性:", ""))
            if "高" in rel_field and "低" not in rel_field:
                relevance = "high"
            elif "中" in rel_field:
                relevance = "medium"
            elif "低" in rel_field:
                relevance = "low"

            original_url = fields.pop("原文链接", "")
            fields.pop("PDF 状态", None)
            fields.pop("来源", None)

            if "期刊/出处" in fields:
                fields["期刊/出处"] = format_venue(fields["期刊/出处"])

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
                "original_url": original_url,
                "scholar_url": scholar_url,
                "body": block.strip(),
            })

    highlights_section = re.search(
        r"## 💡 今日亮点\n(.*?)(?=\n## 📌|$)", text, re.DOTALL
    )
    highlights = highlights_section.group(1).strip() if highlights_section else ""

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

def _render_paper_card(p):
    """Render a single paper card HTML."""
    rel_class = p["relevance"]
    fields_html = ""
    for key, val in p["fields"].items():
        fields_html += (
            f'<div class="field"><span class="field-key">{escape(key)}</span>'
            f'<span class="field-val">{bold_to_html(math_to_html(escape(val)))}</span></div>'
        )

    title_escaped = bold_to_html(escape(p['title']))
    if p['original_url']:
        title_html = f'<a href="{p["original_url"]}" target="_blank" rel="noopener" class="paper-title-link">{title_escaped}</a>'
    else:
        title_html = title_escaped

    return f"""
    <div class="paper-card {rel_class}">
        <div class="paper-header">
            <span class="paper-num">#{p['number']}</span>
            <span class="relevance-badge {rel_class}">{p['relevance'].upper() if p['relevance'] else '?'}</span>
        </div>
        <h3 class="paper-title">{title_html}</h3>
        <div class="paper-fields">{fields_html}</div>
        <div class="paper-links">
            <a href="{p['scholar_url']}" target="_blank" class="scholar-link">🔍 Google Scholar</a>
        </div>
    </div>"""

def load_keywords_for_site():
    """Read current keywords from keywords.json for display."""
    try:
        kw = json.loads(KEYWORDS_FILE.read_text(encoding="utf-8"))
        return kw.get("topics", [])
    except Exception:
        return []

def render_keywords_section(topics):
    if not topics:
        return ""
    items = "".join(
        f'<span class="kw-tag">{escape(t)}</span>' for t in topics
    )
    return f"""
  <div class="keywords-section">
    <div class="kw-header">🔑 当前追踪关键词</div>
    <div class="kw-tags">{items}</div>
    <a href="https://github.com/yangxl-yuanpei/daily-review-reports/issues/new?template=keyword-suggestion.md" target="_blank" class="kw-suggest">+ 建议新关键词</a>
  </div>"""

def render_index(reports_sorted):
    """Render the index page listing all days."""
    day_cards = ""
    for r in reports_sorted:
        paper_count = len(r["papers"])
        link = f"daily-{r['date']}.html"
        day_cards += f"""
        <a href="{link}" class="day-card">
            <div class="day-card-date">{r['date']}</div>
            <div class="day-card-meta">
                <span class="day-card-papers">{paper_count} 篇论文</span>
            </div>
            <div class="day-card-arrow">→</div>
        </a>"""

    topics = load_keywords_for_site()
    kw_section = render_keywords_section(topics)

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
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background: var(--bg); color: var(--text); line-height: 1.7;
  }}
  .container {{ max-width: 800px; margin: 0 auto; padding: 24px 16px; }}

  header {{
    background: linear-gradient(135deg, #1e3a5f, #2563eb);
    color: white; padding: 40px 0 32px; margin-bottom: 32px;
    border-radius: 0 0 24px 24px;
  }}
  header .container {{ padding-bottom: 0; }}
  header h1 {{ font-size: 1.8rem; font-weight: 800; }}
  header p {{ font-size: 0.95rem; opacity: 0.8; margin-top: 4px; }}

  .keywords-section {{
    background: var(--card-bg); border-radius: 12px; padding: 20px 24px;
    margin-bottom: 20px; border: 1px solid var(--border);
  }}
  .kw-header {{
    font-size: 0.85rem; font-weight: 600; color: var(--text-secondary);
    margin-bottom: 10px;
  }}
  .kw-tags {{
    display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 10px;
  }}
  .kw-tag {{
    background: var(--accent-light); color: var(--accent);
    padding: 4px 10px; border-radius: 6px;
    font-size: 0.82rem; font-weight: 500;
  }}
  .kw-suggest {{
    display: inline-block; font-size: 0.8rem; font-weight: 500;
    color: var(--accent); text-decoration: none;
  }}
  .kw-suggest:hover {{ text-decoration: underline; }}

  .day-grid {{
    display: flex; flex-direction: column; gap: 12px;
  }}
  .day-card {{
    display: flex; align-items: center; gap: 16px;
    background: var(--card-bg); border-radius: 12px; padding: 20px 24px;
    border: 1px solid var(--border);
    text-decoration: none; color: var(--text);
    transition: box-shadow 0.15s, border-color 0.15s;
  }}
  .day-card:hover {{
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    border-color: var(--accent);
  }}
  .day-card-date {{
    font-size: 1.15rem; font-weight: 700; color: var(--accent);
    min-width: 100px;
  }}
  .day-card-meta {{
    flex: 1; display: flex; gap: 16px; align-items: center;
  }}
  .day-card-papers {{
    font-size: 0.9rem; font-weight: 600;
    background: var(--accent-light); color: var(--accent);
    padding: 4px 10px; border-radius: 6px;
  }}
  .day-card-arrow {{
    font-size: 1.2rem; color: var(--text-secondary);
    transition: transform 0.15s;
  }}
  .day-card:hover .day-card-arrow {{
    transform: translateX(4px); color: var(--accent);
  }}

  .empty {{ text-align: center; padding: 60px 20px; color: var(--text-secondary); }}

  @media (max-width: 640px) {{
    .day-card {{ flex-wrap: wrap; gap: 8px; }}
    .day-card-date {{ min-width: auto; font-size: 1rem; }}
    .day-card-meta {{ width: 100%; }}
    header h1 {{ font-size: 1.3rem; }}
  }}
</style>
</head>
<body>
<header>
  <div class="container">
    <h1>📄 每日文献追踪报告</h1>
    <p>arXiv + Semantic Scholar | 自动检索 · 精读 · 关键缺口分析</p>
  </div>
</header>
<div class="container">
  {kw_section}
  <div class="day-grid">
    {day_cards if day_cards else '<div class="empty">暂无报告</div>'}
  </div>
</div>
</body>
</html>"""

def render_daily_page(report):
    """Render a single day's full report page."""
    skip_patterns = ("原始候选", "有效去重", "过滤已读", "下载")
    footer_keys = {"检索源", "精读"}
    footer_notes = {}
    stats_cards = ""
    for key, val in report["stats"].items():
        if any(p in key for p in skip_patterns):
            continue
        if any(fk in key for fk in footer_keys):
            footer_notes[key] = val
            continue
        stats_cards += f'<div class="stat-card"><div class="stat-label">{escape(key)}</div><div class="stat-value">{escape(val)}</div></div>'

    papers_html = "".join(_render_paper_card(p) for p in report["papers"])

    highlights_html = ""
    if report["highlights"]:
        highlights_html = f'<div class="highlights"><h3>💡 今日亮点</h3><div class="highlight-body">{markdown_to_html(report["highlights"])}</div></div>'

    gap_html = ""
    if report["key_gap"]:
        gap_html = f'<div class="keygap"><h3>📌 Key Gap</h3><div class="gap-body">{markdown_to_html(report["key_gap"])}</div></div>'

    footer_html = ""
    if footer_notes:
        fmt = {}
        for k, v in footer_notes.items():
            if "检索源" in k:
                fmt[k] = normalize_source(v)
            else:
                fmt[k] = v
        note_parts = " · ".join(f"{k}: {v}" for k, v in fmt.items())
        footer_html = f'<div class="day-footer">{note_parts}</div>'

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>每日文献追踪 - {report['date']}</title>
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
  }}
  .container {{ max-width: 1200px; margin: 0 auto; padding: 24px 16px; }}

  header {{
    background: linear-gradient(135deg, #1e3a5f, #2563eb);
    color: white; padding: 28px 0 20px; margin-bottom: 24px;
    border-radius: 0 0 24px 24px;
  }}
  header .container {{ padding-bottom: 0; }}
  header h1 {{ font-size: 1.4rem; font-weight: 700; }}
  header .back-link {{
    display: inline-block; margin-bottom: 8px; color: rgba(255,255,255,0.7);
    text-decoration: none; font-size: 0.85rem; font-weight: 500;
  }}
  header .back-link:hover {{ color: white; }}

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
  .paper-title-link {{ color: var(--text); text-decoration: none; }}
  .paper-title-link:hover {{ color: var(--accent); text-decoration: underline; }}
  .paper-fields {{ flex: 1; }}
  .field {{ margin-bottom: 8px; font-size: 0.82rem; line-height: 1.5; }}
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

  .highlights, .keygap {{
    background: var(--card-bg); border-radius: 12px; padding: 20px;
    margin-bottom: 16px; border: 1px solid var(--border);
  }}
  .highlights h3, .keygap h3 {{ font-size: 1rem; margin-bottom: 8px; }}
  .highlight-body, .gap-body {{ font-size: 0.88rem; color: var(--text); line-height: 1.7; }}
  .highlight-body p, .gap-body p {{ margin-bottom: 6px; }}
  .highlight-body strong, .gap-body strong {{ font-weight: 600; }}

  .day-footer {{
    margin-top: 24px; padding: 12px 16px; text-align: center;
    font-size: 0.78rem; color: var(--text-secondary);
    border-top: 1px solid var(--border);
  }}

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
    <a href="index.html" class="back-link">← 返回报告列表</a>
    <h1>{report['date']} — {escape(report['title'])}</h1>
  </div>
</header>
<div class="container">
  <div class="stats-row">{stats_cards}</div>
  <div class="papers-grid">{papers_html}</div>
  {highlights_html}
  {gap_html}
  {footer_html}
</div>
</body>
</html>"""

def bold_to_html(text):
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)

def normalize_source(raw):
    """Normalize 检索源 format to a consistent short form."""
    parts = re.split(r'\s*\+\s*', raw)
    names = []
    for p in parts:
        p = p.strip()
        if re.match(r'arXiv', p):
            names.append("arXiv")
        elif re.match(r'Semantic Scholar|S2', p):
            names.append("Semantic Scholar")
        else:
            names.append(p)
    result = " + ".join(names)
    s2_unavail = re.search(r'S2[^+]*不可', raw) or re.search(r's2_available.*false', raw, re.I)
    if s2_unavail:
        result += " (S2 不可用)"
    return result

def format_venue(venue_str):
    m = re.match(r'arXiv:\s*([^,)]+?)(?:,|\s*\(|$)', venue_str.strip())
    if m:
        return f"arXiv ({m.group(1).strip()})"
    return venue_str.strip()

def math_to_html(text):
    text = re.sub(r'_([a-zA-Z0-9])', r'<sub>\1</sub>', text)
    text = re.sub(r'\^([0-9]|[a-zA-Z])', r'<sup>\1</sup>', text)
    return text

def markdown_to_html(md_text):
    lines = md_text.strip().split("\n")
    html_parts = []
    for line in lines:
        line = line.strip()
        if not line:
            html_parts.append("<br>")
        elif line.startswith("- "):
            html_parts.append(f"<li>{bold_to_html(math_to_html(escape(line[2:])))}</li>")
        elif line.startswith("**") and ":**" in line:
            parts = line.split(":**", 1)
            key = parts[0].strip("*").strip()
            val = parts[1].strip() if len(parts) > 1 else ""
            html_parts.append(
                f"<p><strong>{escape(key)}:</strong> {bold_to_html(math_to_html(escape(val)))}</p>"
            )
        else:
            html_parts.append(f"<p>{bold_to_html(math_to_html(escape(line)))}</p>")
    return "".join(html_parts)

def main():
    reports = []
    for fp in sorted(REPORTS_DIR.glob("daily-summary-*.md")):
        m = DAILY_PATTERN.match(fp.name)
        if m:
            try:
                parsed = parse_summary(fp)
                reports.append(parsed)
                print(f"  ✓ {fp.name} ({len(parsed['papers'])} papers)")
            except Exception as e:
                print(f"  ✗ {fp.name}: {e}")

    if not reports:
        print("No daily summaries found.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    reports_sorted = sorted(reports, key=lambda r: r["date"], reverse=True)

    # Generate index.html
    index_html = render_index(reports_sorted)
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"\n  ✓ index.html ({len(reports)} days listed)")

    # Generate per-day pages
    for r in reports_sorted:
        daily_html = render_daily_page(r)
        daily_file = OUTPUT_DIR / f"daily-{r['date']}.html"
        daily_file.write_text(daily_html, encoding="utf-8")
        print(f"  ✓ daily-{r['date']}.html ({len(r['papers'])} papers)")

    print(f"\nDone! Generated {len(reports)} day pages + index.html")
    print(f"  {sum(len(r['papers']) for r in reports)} papers total")
    print(f"  Set GitHub Pages → branch: main, directory: / (root)")

if __name__ == "__main__":
    main()

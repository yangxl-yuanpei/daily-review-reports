#!/usr/bin/env python3
"""
Generate a modern card-style HTML site from daily-summary-*.md reports.
Each paper gets an auto-generated Google Scholar search link.
Output: site/index.html (all reports in one page with day navigation)
"""

import re, json, hashlib
from pathlib import Path
from datetime import datetime
from html import escape

DESKTOP_DIR = Path("/mnt/c/Users/94474/Desktop/daily-review-reports")
REPORTS_DIR = DESKTOP_DIR / "reports"
OUTPUT_DIR = DESKTOP_DIR  # root for GitHub Pages

DAILY_PATTERN = re.compile(r"daily-summary-(\d{4}-\d{2}-\d{2})\.md")

PAPER_BLOCK_RE = re.compile(
    r"### (\d+)\.\s+(.+?)\n"
    r"(.*?)(?=\n### \d+\.|\n## 💡|\n## 📌|$)",
    re.DOTALL,
)

FIELD_RE = re.compile(r"-\s*\*\*(.+?):\*\*\s*(.*)")

STATS_RE = re.compile(r"-\s*(.+?):\s*(.+)")

def parse_summary(filepath):
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

            # Extract and remove fields used for UI
            original_url = fields.pop("原文链接", "")
            fields.pop("PDF 状态", None)
            fields.pop("来源", None)

            # Normalize journal/venue format
            if "期刊/出处" in fields:
                fields["期刊/出处"] = format_venue(fields["期刊/出处"])

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
                "original_url": original_url,
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
    """Render all parsed reports into a single modern card-style HTML page."""
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

        # Stats cards (skip internal tracking fields)
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

        # Papers
        papers_html = ""
        for p in report["papers"]:
            rel_class = p["relevance"]
            fields_html = ""
            for key, val in p["fields"].items():
                fields_html += (
                    f'<div class="field"><span class="field-key">{escape(key)}</span>'
                    f'<span class="field-val">{bold_to_html(math_to_html(escape(val)))}</span></div>'
                )

            # Title as link if original_url exists
            title_escaped = bold_to_html(escape(p['title']))
            if p['original_url']:
                title_html = f'<a href="{p["original_url"]}" target="_blank" rel="noopener" class="paper-title-link">{title_escaped}</a>'
            else:
                title_html = title_escaped

            papers_html += f"""
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

        # Highlights + Key Gap
        highlights_html = ""
        if report["highlights"]:
            highlights_html = f'<div class="highlights"><h3>💡 今日亮点</h3><div class="highlight-body">{markdown_to_html(report["highlights"])}</div></div>'

        gap_html = ""
        if report["key_gap"]:
            gap_html = f'<div class="keygap"><h3>📌 Key Gap</h3><div class="gap-body">{markdown_to_html(report["key_gap"])}</div></div>'

        # Footer note
        footer_html = ""
        if footer_notes:
            note_parts = " · ".join(f"{k}: {v}" for k, v in footer_notes.items())
            footer_html = f'<div class="day-footer">{note_parts}</div>'

        day_contents.append(f"""
        <div class="day-content {active}" data-day="{ri}">
            <div class="stats-row">{stats_cards}</div>
            <div class="papers-grid">{papers_html}</div>
            {highlights_html}
            {gap_html}
            {footer_html}
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
  .paper-title-link {{ color: var(--text); text-decoration: none; }}
  .paper-title-link:hover {{ color: var(--accent); text-decoration: underline; }}
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

  /* Day footer */
  .day-footer {{
    margin-top: 24px; padding: 12px 16px; text-align: center;
    font-size: 0.78rem; color: var(--text-secondary);
    border-top: 1px solid var(--border);
  }}

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
    <p>arXiv + Semantic Scholar | 自动检索 · 精读 · 关键缺口分析</p>
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

def bold_to_html(text):
    """Convert **bold** markdown to <strong> tags."""
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)

def format_venue(venue_str):
    """Normalize venue/journal to standard short format."""
    m = re.match(r'arXiv:\s*([^,)]+?)(?:,|\s*\(|$)', venue_str.strip())
    if m:
        return f"arXiv ({m.group(1).strip()})"
    return venue_str.strip()

def math_to_html(text):
    """Convert scientific notation: _X → <sub>X</sub>, ^X → <sup>X</sup>."""
    text = re.sub(r'_([a-zA-Z0-9])', r'<sub>\1</sub>', text)
    text = re.sub(r'\^([0-9]|[a-zA-Z])', r'<sup>\1</sup>', text)
    return text

def markdown_to_html(md_text):
    """Simple markdown to HTML conversion for highlights/gap text."""
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
    html = render_html(reports)
    (OUTPUT_DIR / "index.html").write_text(html, encoding="utf-8")
    print(f"\nDone! Generated {OUTPUT_DIR / 'index.html'}")
    print(f"  {len(reports)} daily reports, {sum(len(r['papers']) for r in reports)} papers total")
    print(f"  Set GitHub Pages → branch: main, directory: / (root)")

if __name__ == "__main__":
    main()

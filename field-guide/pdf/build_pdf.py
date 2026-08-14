#!/usr/bin/env python3
"""Assemble the field-guide (Ver.2) PM Delivery Guide book.html — Learner and
Combined (Learner + Instructor + Answer Key) editions — then render to PDF
via Chrome headless (same renderer used for the original e-Book).

Usage: /usr/bin/python3 build_pdf.py
"""
import html
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FIELD_GUIDE = os.path.dirname(HERE)
REPO = os.path.dirname(FIELD_GUIDE)

CHAPTERS_DIR = os.path.join(FIELD_GUIDE, "chapters")
APPENDICES_DIR = os.path.join(FIELD_GUIDE, "appendices")

CH_NUMS = [f"{i:02d}" for i in range(0, 11)]  # ch-00 .. ch-10

APPENDICES = [
    "Appendix-A-Artifact-Catalogue.md",
    "Appendix-B-Golden-Rules-Poster.md",
    "Appendix-C-PM-Glossary-Extended.md",
    "Appendix-D-Master-Answer-Key.md",
    "Appendix-E-SDLC-Role-Output-Matrix.md",
    "Appendix-F-Problem-to-Chapter-Index.md",
]

BOOK_HTML = os.path.join(HERE, "book.html")
BOOK_LEARNER_HTML = os.path.join(HERE, "book-learner.html")
BOOK_PDF = os.path.join(HERE, "PM-Delivery-Guide-Complete-Edition.pdf")
BOOK_LEARNER_PDF = os.path.join(HERE, "PM-Delivery-Guide-Learner-Edition.pdf")

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

BOOK_TITLE = "PM Delivery Guide (Ver.2)"
BOOK_SUBTITLE = "Project Delivery Playbook + PM Masterclass — เล่มรวมฉบับสมบูรณ์ (PMBOK 8-aligned)"


# ---------------------------------------------------------------------------
# Markdown -> HTML converter (stdlib only, adapted from e-Book/build_pdf.py)
# ---------------------------------------------------------------------------

def slugify(text):
    s = text.lower()
    s = re.sub(r"[^a-z0-9\u0e00-\u0e7f\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{1,}:?\s*(\|\s*:?-{1,}:?\s*)*\|?\s*$")
HEADING_RE = re.compile(r"^(#{1,4})\s+(.*)$")
BULLET_RE = re.compile(r"^-\s+(.*)$")
NUMBERED_RE = re.compile(r"^\d+\.\s+(.*)$")


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # links -> visible text only
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def cell_align_style(sep_cell):
    sep_cell = sep_cell.strip()
    starts = sep_cell.startswith(":")
    ends = sep_cell.endswith(":")
    if starts and ends:
        return ' style="text-align:center"'
    if ends:
        return ' style="text-align:right"'
    return ""


def md_to_html(text, id_prefix, seen_ids):
    lines = text.split("\n")
    out = []
    i = 0
    n = len(lines)

    def make_id(heading_text):
        base = id_prefix + slugify(heading_text)
        if not base:
            base = id_prefix + "section"
        candidate = base
        k = 2
        while candidate in seen_ids:
            candidate = f"{base}-{k}"
            k += 1
        seen_ids.add(candidate)
        return candidate

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            i += 1
            code_lines = []
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            escaped = html.escape("\n".join(code_lines), quote=False)
            out.append(f"<pre><code>{escaped}</code></pre>")
            continue

        m = HEADING_RE.match(stripped)
        if m:
            level = len(m.group(1))
            heading_text = m.group(2).strip()
            hid = make_id(heading_text)
            out.append(f'<h{level} id="{hid}">{inline(heading_text)}</h{level}>')
            i += 1
            continue

        if "|" in stripped and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1]):
            header_cells = [c.strip() for c in stripped.strip("|").split("|")]
            sep_cells = [c.strip() for c in lines[i + 1].strip().strip("|").split("|")]
            aligns = [cell_align_style(c) for c in sep_cells]
            i += 2
            body_rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                body_rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            thead = "".join(
                f"<th{aligns[j] if j < len(aligns) else ''}>{inline(c)}</th>"
                for j, c in enumerate(header_cells)
            )
            tbody_rows = []
            for row in body_rows:
                tds = "".join(
                    f"<td{aligns[j] if j < len(aligns) else ''}>{inline(c)}</td>"
                    for j, c in enumerate(row)
                )
                tbody_rows.append(f"<tr>{tds}</tr>")
            out.append(
                f"<table><thead><tr>{thead}</tr></thead><tbody>"
                + "".join(tbody_rows)
                + "</tbody></table>"
            )
            continue

        if BULLET_RE.match(stripped):
            items = []
            while i < n and BULLET_RE.match(lines[i].strip()):
                items.append(BULLET_RE.match(lines[i].strip()).group(1))
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(it)}</li>" for it in items) + "</ul>")
            continue

        if NUMBERED_RE.match(stripped):
            items = []
            while i < n and NUMBERED_RE.match(lines[i].strip()):
                items.append(NUMBERED_RE.match(lines[i].strip()).group(1))
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(it)}</li>" for it in items) + "</ol>")
            continue

        out.append(f"<p>{inline(stripped)}</p>")
        i += 1

    return "\n".join(out)


def strip_frontmatter(text):
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                return "\n".join(lines[idx + 1:])
    return text


def convert_file(path, id_prefix, seen_ids):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return md_to_html(strip_frontmatter(text), id_prefix, seen_ids)


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

PRINT_CSS = """
@page {
  size: A4;
  margin: 22mm 20mm 24mm 20mm;
  @bottom-center { content: counter(page); font-size: 9pt; color: #52606d; }
}
@page :first {
  @bottom-center { content: none; }
}
html { font-size: 11pt; }
body {
  font-family: "Sukhumvit Set", "Thonburi", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: #172026; line-height: 1.6; margin: 0;
}
h1 {
  font-size: 20pt; line-height: 1.25; margin: 0 0 14pt; color: #101820;
  break-before: page;
}
h2 { font-size: 15pt; margin: 18pt 0 8pt; padding-top: 6pt; border-top: 1px solid #e5e9ef; break-after: avoid; }
h3 { font-size: 12.5pt; margin: 14pt 0 6pt; break-after: avoid; }
h4 { font-size: 11pt; margin: 12pt 0 5pt; break-after: avoid; }
p, li { font-size: 11pt; line-height: 1.6; orphans: 2; widows: 2; }
a { color: inherit; text-decoration: none; }
table { border-collapse: collapse; width: 100%; margin: 10pt 0; font-size: 9.5pt; break-inside: avoid; }
th, td { border: 1px solid #d9e0e8; padding: 5pt 7pt; vertical-align: top; }
th { background: #eef3f8; text-align: left; }
tr { break-inside: avoid; }
pre {
  background: #101820; color: #f5f7fa; padding: 10pt 12pt; border-radius: 4pt;
  font-size: 9pt; white-space: pre-wrap; word-wrap: break-word; break-inside: avoid;
}
code { font-family: "SF Mono", Menlo, Consolas, monospace; }
p code, li code, td code, th code { background: #eef3f8; padding: 0 3px; border-radius: 3px; }

.cover { text-align: center; padding-top: 55mm; break-after: page; }
.cover h1 { break-before: auto; font-size: 28pt; }
.cover .byline { font-size: 13pt; margin-top: 8mm; }
.cover .edition { font-size: 12pt; margin-top: 4mm; color: #34424c; }
.cover .disclaimer { color: #52606d; font-size: 10pt; margin-top: 10mm; }

.toc { break-after: page; }
.toc h1 { break-before: auto; }
.toc ol { list-style: none; padding-left: 0; margin: 0; }
.toc > ol > li { margin: 10pt 0 2pt; font-weight: 600; }
.toc .sub { list-style: none; padding-left: 14pt; margin: 0 0 6pt; font-weight: 400; }
.toc .sub li { margin: 2pt 0; font-size: 10pt; color: #34424c; }

.part-divider { break-before: page; text-align: center; padding-top: 70mm; background: #fff8e6; }
.part-divider h2 { break-after: auto; border-top: none; font-size: 20pt; }
.part-divider .banner { color: #8a5a00; font-weight: 600; margin-top: 8mm; font-size: 11pt; }
"""


def chapter_label(num):
    names = {
        "00": "PMBOK Primer — กรอบคิดสำหรับเล่มนี้",
        "01": "Pre-sales — จาก Opportunity ถึง Proposal/SOW",
        "02": "Initiation — Charter และ Stakeholder",
        "03": "Requirements, Scope และ WBS",
        "04": "Schedule, Cost และ Resource",
        "05": "Risk, Procurement, Communications และ Quality Plan",
        "06": "Execution — ทีม, คุณภาพ และการควบคุมประจำวัน",
        "07": "Monitoring & Change — EVM และ Integrated Change Control",
        "08": "Verification / UAT — Control Quality และ Release Readiness",
        "09": "Go-Live & Hypercare",
        "10": "Transition & Closure",
    }
    return names.get(num, num)


def build_toc_entry(label, title, learner_id, instr_id=None, ans_id=None, with_subs=True):
    entry = f'<li><a href="#{learner_id}">{html.escape(label + " — " + title, quote=False)}</a>'
    subs = []
    if with_subs and instr_id:
        subs.append(f'<li><a href="#{instr_id}">Instructor Guide</a></li>')
    if with_subs and ans_id:
        subs.append(f'<li><a href="#{ans_id}">Answer Key</a></li>')
    if subs:
        entry += '<ul class="sub">' + "".join(subs) + "</ul>"
    entry += "</li>"
    return entry


def render_pdf(html_path, pdf_path):
    if not os.path.exists(CHROME_BIN):
        print(f"ERROR: Chrome not found at {CHROME_BIN}", file=sys.stderr)
        sys.exit(1)
    url = "file://" + html_path
    cmd = [
        CHROME_BIN, "--headless=new", "--disable-gpu", "--no-sandbox",
        "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}", url,
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)
    print(f"Wrote {pdf_path} ({os.path.getsize(pdf_path)} bytes)")


def main():
    seen_ids = set()

    toc_entries = []
    toc_learner_entries = []
    body_parts = []
    learner_body_parts = []

    for num in CH_NUMS:
        learner_path = os.path.join(CHAPTERS_DIR, f"ch-{num}", f"ch-{num}-learner.md")
        instructor_path = os.path.join(CHAPTERS_DIR, f"ch-{num}", f"ch-{num}-instructor.md")
        answerkey_path = os.path.join(CHAPTERS_DIR, f"ch-{num}", f"ch-{num}-answer-key.md")

        learner_html = convert_file(learner_path, f"ch{num}-", seen_ids)
        instr_html = convert_file(instructor_path, f"instr-{num}-", seen_ids)
        ans_html = convert_file(answerkey_path, f"ans-{num}-", seen_ids)

        learner_id = re.search(r'<h1 id="([^"]+)"', learner_html).group(1)
        instr_id = re.search(r'<h1 id="([^"]+)"', instr_html).group(1)
        ans_id = re.search(r'<h1 id="([^"]+)"', ans_html).group(1)

        toc_entries.append(
            build_toc_entry(f"Ch.{num}", chapter_label(num), learner_id, instr_id, ans_id)
        )
        toc_learner_entries.append(
            build_toc_entry(f"Ch.{num}", chapter_label(num), learner_id, with_subs=False)
        )

        learner_body_parts.append(f'<section class="chapter">{learner_html}</section>')

        divider = f"""<section class="part-divider">
<h2>เอกสารสำหรับผู้สอน — Ch.{num} {html.escape(chapter_label(num), quote=False)}</h2>
<p class="banner">เอกสารสำหรับผู้สอน มีเฉลยและเกณฑ์ให้คะแนน<br>Instructor-only: contains model answers and rubrics</p>
</section>"""
        body_parts.append(f'<section class="chapter">{learner_html}</section>')
        body_parts.append(divider)
        body_parts.append(f'<section class="instructor-section">{instr_html}</section>')
        body_parts.append(f'<section class="instructor-section">{ans_html}</section>')

    # Appendices
    for app in APPENDICES:
        path = os.path.join(APPENDICES_DIR, app)
        app_html = convert_file(path, "appendix-", seen_ids)
        app_id = re.search(r'<h1 id="([^"]+)"', app_html).group(1)
        app_toc = f'<li><a href="#{app_id}">{html.escape(app.replace(".md", ""), quote=False)}</a></li>'
        toc_entries.append(app_toc)
        toc_learner_entries.append(app_toc)
        body_parts.append(f'<section class="chapter">{app_html}</section>')
        learner_body_parts.append(f'<section class="chapter">{app_html}</section>')

    def build_cover(subtitle, edition):
        return f"""<section class="cover">
<h1>{html.escape(BOOK_TITLE, quote=False)}</h1>
<p class="byline">{html.escape(subtitle, quote=False)}</p>
<p class="edition">{html.escape(edition, quote=False)}</p>
<p class="disclaimer">อ้างอิง PMBOK 8th Edition (Principles / Domains / Focus Areas) ประกอบ Playbook V2<br>เอกสารนี้ไม่ใช่เอกสารทางการของ PMI — This is not official PMI material.</p>
</section>"""

    cover_combined = build_cover(
        BOOK_SUBTITLE, "Learner Edition + Instructor Companion — Combined"
    )
    cover_learner = build_cover(
        "Project Delivery Playbook + PM Masterclass — ฉบับผู้เรียน (Learner) (PMBOK 8-aligned)",
        "Learner Edition",
    )

    def build_toc(entries):
        return f"""<section class="toc">
<h1>สารบัญ / Table of Contents</h1>
<ol>
{''.join(entries)}
</ol>
</section>"""

    toc_combined = build_toc(toc_entries)
    toc_learner = build_toc(toc_learner_entries)

    def full_page(cover_html, toc_html, body):
        return f"""<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<title>{html.escape(BOOK_TITLE, quote=False)}</title>
<style>{PRINT_CSS}</style>
</head>
<body>
{cover_html}
{toc_html}
{body}
</body>
</html>
"""

    with open(BOOK_HTML, "w", encoding="utf-8") as f:
        f.write(full_page(cover_combined, toc_combined, "".join(body_parts)))
    print(f"Wrote {BOOK_HTML} ({os.path.getsize(BOOK_HTML)} bytes)")

    with open(BOOK_LEARNER_HTML, "w", encoding="utf-8") as f:
        f.write(full_page(cover_learner, toc_learner, "".join(learner_body_parts)))
    print(f"Wrote {BOOK_LEARNER_HTML} ({os.path.getsize(BOOK_LEARNER_HTML)} bytes)")

    render_pdf(BOOK_HTML, BOOK_PDF)
    render_pdf(BOOK_LEARNER_HTML, BOOK_LEARNER_PDF)


if __name__ == "__main__":
    main()

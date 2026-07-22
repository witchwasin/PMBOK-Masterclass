#!/usr/bin/env python3
"""Assemble the combined Learner + Instructor PMBOK Masterclass book.html,
then render it to PDF (weasyprint if available, Chrome headless otherwise).

Usage: /usr/bin/python3 build_pdf.py
"""
import html
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EBOOK = os.path.dirname(HERE)
REPO = os.path.dirname(EBOOK)

LEARNER_HTML = os.path.join(EBOOK, "release", "PMBOK-Masterclass-Learner.html")
CHAPTERS_DIR = os.path.join(EBOOK, "chapters")
CAPSTONE_DIR = os.path.join(EBOOK, "capstone")

BOOK_HTML = os.path.join(HERE, "book.html")
BOOK_PDF = os.path.join(HERE, "PMBOK-Masterclass-Complete-Edition.pdf")

CHAPTERS = [f"{i:02d}" for i in range(1, 17)]

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


# ---------------------------------------------------------------------------
# Markdown -> HTML converter (stdlib only)
# ---------------------------------------------------------------------------

def slugify(text):
    s = text.lower()
    s = re.sub(r"[^a-z0-9฀-๿\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{1,}:?\s*(\|\s*:?-{1,}:?\s*)*\|?\s*$")
HEADING_RE = re.compile(r"^(#{1,3})\s+(.*)$")
BULLET_RE = re.compile(r"^-\s+(.*)$")
NUMBERED_RE = re.compile(r"^\d+\.\s+(.*)$")


def inline(text):
    """Escape HTML, then apply link/code-span inline rules."""
    text = html.escape(text, quote=False)
    # links: keep the visible text only (targets are external .md files not in the PDF)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # inline code spans
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
    """Convert one Markdown file's body (frontmatter already stripped by caller)
    into an HTML fragment. `seen_ids` is a set shared across the whole book so
    ids stay globally unique."""
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

        # fenced code block
        if stripped.startswith("```"):
            i += 1
            code_lines = []
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing fence
            escaped = html.escape("\n".join(code_lines), quote=False)
            out.append(f"<pre><code>{escaped}</code></pre>")
            continue

        # heading
        m = HEADING_RE.match(stripped)
        if m:
            level = len(m.group(1))
            heading_text = m.group(2).strip()
            hid = make_id(heading_text)
            out.append(f'<h{level} id="{hid}">{inline(heading_text)}</h{level}>')
            i += 1
            continue

        # table: current line has '|' and next line is a separator row
        if "|" in stripped and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1]):
            header_cells = [c.strip() for c in stripped.strip("|").split("|")]
            sep_cells = [c.strip() for c in lines[i + 1].strip().strip("|").split("|")]
            aligns = [cell_align_style(c) for c in sep_cells]
            i += 2
            body_rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                row_cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                body_rows.append(row_cells)
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

        # bullet list
        if BULLET_RE.match(stripped):
            items = []
            while i < n and BULLET_RE.match(lines[i].strip()):
                items.append(BULLET_RE.match(lines[i].strip()).group(1))
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(it)}</li>" for it in items) + "</ul>")
            continue

        # numbered list
        if NUMBERED_RE.match(stripped):
            items = []
            while i < n and NUMBERED_RE.match(lines[i].strip()):
                items.append(NUMBERED_RE.match(lines[i].strip()).group(1))
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(it)}</li>" for it in items) + "</ol>")
            continue

        # plain paragraph line
        out.append(f"<p>{inline(stripped)}</p>")
        i += 1

    return "\n".join(out)


def strip_frontmatter(text):
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                return "\n".join(lines[idx + 1 :])
    return text


def convert_file(path, id_prefix, seen_ids):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    text = strip_frontmatter(text)
    return md_to_html(text, id_prefix, seen_ids)


# ---------------------------------------------------------------------------
# Learner HTML chapter splitter
# ---------------------------------------------------------------------------

H1_RE = re.compile(r'<h1 id="([^"]+)">(.*?)</h1>', re.S)


def split_learner_chapters():
    with open(LEARNER_HTML, encoding="utf-8") as f:
        html_text = f.read()

    main_m = re.search(r"<main>(.*)</main>", html_text, re.S)
    main_content = main_m.group(1)

    matches = list(H1_RE.finditer(main_content))
    # matches[0] is the redundant document title; the rest are Chapter 01..16, Capstone
    chapters = {}
    for idx in range(1, len(matches)):
        start = matches[idx].start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(main_content)
        chap_id = matches[idx].group(1)
        chap_title = re.sub(r"<[^>]+>", "", matches[idx].group(2))
        fragment = main_content[start:end]
        chapters[chap_id] = {"title": chap_title, "html": fragment}
    return chapters


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
  font-size: 22pt; line-height: 1.25; margin: 0 0 14pt; color: #101820;
  break-before: page;
}
h2 { font-size: 15pt; margin: 18pt 0 8pt; padding-top: 6pt; border-top: 1px solid #e5e9ef; break-after: avoid; }
h3 { font-size: 12.5pt; margin: 14pt 0 6pt; break-after: avoid; }
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
.cover h1 { break-before: auto; font-size: 30pt; }
.cover .byline { font-size: 14pt; margin-top: 8mm; }
.cover .edition { font-size: 12pt; margin-top: 4mm; color: #34424c; }
.cover .disclaimer { color: #52606d; font-size: 10pt; margin-top: 10mm; }

.toc { break-after: page; }
.toc h1 { break-before: auto; }
.toc ol { list-style: none; padding-left: 0; margin: 0; }
.toc > ol > li { margin: 10pt 0 2pt; font-weight: 600; }
.toc .sub { list-style: none; padding-left: 14pt; margin: 0 0 6pt; font-weight: 400; }
.toc .sub li { margin: 2pt 0; font-size: 10pt; color: #34424c; }
.toc a::after { content: leader('.') target-counter(attr(href url), page); color: #52606d; }

.part-divider { break-before: page; text-align: center; padding-top: 70mm; background: #fff8e6; }
.part-divider h2 { break-after: auto; border-top: none; font-size: 20pt; }
.part-divider .banner { color: #8a5a00; font-weight: 600; margin-top: 8mm; font-size: 11pt; }
.instructor-section { }
"""


def build_toc_entry(chap_id, title, instr_id, ans_id):
    return f"""<li><a href="#{chap_id}">{html.escape(title, quote=False)}</a>
<ul class="sub">
<li><a href="#{instr_id}">Instructor Guide</a></li>
<li><a href="#{ans_id}">Answer Key</a></li>
</ul></li>"""


def main():
    seen_ids = set()
    learner_chapters = split_learner_chapters()

    toc_entries = []
    body_parts = []

    for num in CHAPTERS:
        chap_key = None
        for k in learner_chapters:
            if k.startswith(f"chapter-{num}-"):
                chap_key = k
                break
        if chap_key is None:
            print(f"WARNING: could not find learner chapter {num} in Learner.html", file=sys.stderr)
            continue
        chap = learner_chapters[chap_key]
        seen_ids.add(chap_key)

        instructor_path = os.path.join(CHAPTERS_DIR, f"lesson-{num}", f"lesson-{num}-instructor.md")
        answerkey_path = os.path.join(CHAPTERS_DIR, f"lesson-{num}", f"lesson-{num}-answer-key.md")

        instr_prefix = f"instr-{num}-"
        ans_prefix = f"ans-{num}-"
        instr_html = convert_file(instructor_path, instr_prefix, seen_ids)
        ans_html = convert_file(answerkey_path, ans_prefix, seen_ids)

        # ids of the first heading (H1) in each converted fragment, for TOC linking
        instr_first_id = re.search(r'<h1 id="([^"]+)"', instr_html).group(1)
        ans_first_id = re.search(r'<h1 id="([^"]+)"', ans_html).group(1)

        toc_entries.append(build_toc_entry(chap_key, chap["title"], instr_first_id, ans_first_id))

        divider = f"""<section class="part-divider">
<h2>เอกสารสำหรับผู้สอน — Chapter {num}</h2>
<p class="banner">เอกสารสำหรับผู้สอน มีเฉลยและเกณฑ์ให้คะแนน<br>Instructor-only: contains model answers and rubrics</p>
</section>"""

        body_parts.append(f'<section class="chapter">{chap["html"]}</section>')
        body_parts.append(divider)
        body_parts.append(f'<section class="instructor-section">{instr_html}</section>')
        body_parts.append(f'<section class="instructor-section">{ans_html}</section>')

    # Capstone
    capstone_key = "capstone" if "capstone" not in seen_ids else None
    cap_match_key = next((k for k in learner_chapters if k.startswith("capstone")), None)
    if cap_match_key is None:
        print("WARNING: could not find capstone in Learner.html", file=sys.stderr)
    else:
        cap = learner_chapters[cap_match_key]
        seen_ids.add(cap_match_key)
        cap_instr_path = os.path.join(CAPSTONE_DIR, "capstone-instructor.md")
        cap_instr_html = convert_file(cap_instr_path, "instr-capstone-", seen_ids)
        cap_instr_first_id = re.search(r'<h1 id="([^"]+)"', cap_instr_html).group(1)

        toc_entries.append(
            f'<li><a href="#{cap_match_key}">{html.escape(cap["title"], quote=False)}</a>'
            f'<ul class="sub"><li><a href="#{cap_instr_first_id}">Instructor Guide</a></li></ul></li>'
        )

        divider = """<section class="part-divider">
<h2>เอกสารสำหรับผู้สอน — Capstone</h2>
<p class="banner">เอกสารสำหรับผู้สอน มีเฉลยและเกณฑ์ให้คะแนน<br>Instructor-only: contains model answers and rubrics</p>
</section>"""
        body_parts.append(f'<section class="chapter">{cap["html"]}</section>')
        body_parts.append(divider)
        body_parts.append(f'<section class="instructor-section">{cap_instr_html}</section>')

    cover = """<section class="cover">
<h1>PMBOK-aligned Practical Masterclass</h1>
<p class="byline">ผู้เรียบเรียง: Witchwasin K.</p>
<p class="edition">Learner Edition + Instructor Companion — Combined</p>
<p class="disclaimer">เอกสารนี้ไม่ใช่เอกสารทางการของ PMI<br>This is not official PMI material.</p>
</section>"""

    toc = f"""<section class="toc">
<h1>สารบัญ / Table of Contents</h1>
<ol>
{''.join(toc_entries)}
</ol>
</section>"""

    full_html = f"""<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<title>PMBOK-aligned Practical Masterclass — Complete Edition</title>
<style>{PRINT_CSS}</style>
</head>
<body>
{cover}
{toc}
{''.join(body_parts)}
</body>
</html>
"""

    with open(BOOK_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Wrote {BOOK_HTML} ({len(full_html)} bytes)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Assemble the field-guide (Ver.2) PM Delivery Guide book.html — Learner and
Combined (Learner + Instructor + Answer Key) editions — then render to PDF
via Chrome headless (same renderer used for the original e-Book).

Layout (Ver.2 typography pass):
  * Running heads via CSS *named pages*: every page carries
    "บทที่ N: ชื่อบท | P{page}" (appendices: "ภาคผนวก X — ชื่อ | P{page}").
    The chapter opener page and the cover suppress the header (:first).
  * Full-bleed cover, chapter opener band + kicker, zebra tables with dark
    header row, blockquote callouts, checkbox lists, styled TOC.

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
# Per-chapter data: running-head labels, kickers, TOC labels
# ---------------------------------------------------------------------------

CH_HEADERS = {
    "00": "บทที่ 0: PMBOK Primer — กรอบคิด A→H",
    "01": "บทที่ 1: Pre-sales — จาก Opportunity ถึง SOW",
    "02": "บทที่ 2: Initiation — Charter และ Stakeholder",
    "03": "บทที่ 3: Requirements, Scope และ WBS",
    "04": "บทที่ 4: Schedule, Cost และ Resource",
    "05": "บทที่ 5: Risk, Procurement, Comms และ Quality Plan",
    "06": "บทที่ 6: Execution — ทีม คุณภาพ ควบคุมประจำวัน",
    "07": "บทที่ 7: Monitoring & Change — EVM และ Change Control",
    "08": "บทที่ 8: Verification / UAT และ Release Readiness",
    "09": "บทที่ 9: Go-Live และ Hypercare",
    "10": "บทที่ 10: Transition, Closure และ Benefit Handover",
}

CH_KICKERS = {
    "00": "ปฐมบท · PRIMER",
    "01": "A · PRE-SALES",
    "02": "B · INITIATION",
    "03": "C · REQUIREMENTS & SCOPE",
    "04": "C · SCHEDULE, COST & RESOURCE",
    "05": "C · RISK, PROCUREMENT, COMMS & QUALITY PLAN",
    "06": "D · EXECUTION",
    "07": "E · MONITORING & CHANGE",
    "08": "F · VERIFICATION / UAT",
    "09": "G · GO-LIVE & HYPERCARE",
    "10": "H · TRANSITION & CLOSURE",
}

APP_HEADERS = {
    "Appendix-A-Artifact-Catalogue.md": "ภาคผนวก A — Artifact Catalogue",
    "Appendix-B-Golden-Rules-Poster.md": "ภาคผนวก B — Golden Rules Poster",
    "Appendix-C-PM-Glossary-Extended.md": "ภาคผนวก C — PM Glossary",
    "Appendix-D-Master-Answer-Key.md": "ภาคผนวก D — Master Answer Key",
    "Appendix-E-SDLC-Role-Output-Matrix.md": "ภาคผนวก E — SDLC Role & Output",
    "Appendix-F-Problem-to-Chapter-Index.md": "ภาคผนวก F — Problem → Chapter",
}

INSTR_KICKER = "INSTRUCTOR COMPANION · เอกสารสำหรับผู้สอน"
ANSKEY_KICKER = "ANSWER KEY · เฉลยและเกณฑ์ให้คะแนน"


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
CHECKBOX_RE = re.compile(r"^\[( |x|X)\]\s*(.*)$")


def inline(text):
    """Escape + inline markdown: links -> text, `code`, **bold**, *italic*.

    Code spans are protected with placeholders first so bold/italic never
    rewrite the inside of a <code> element.
    """
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # links -> visible text

    codes = []

    def keep(m):
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", keep, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    for i, c in enumerate(codes):
        text = text.replace(f"\x00{i}\x00", f"<code>{c}</code>")
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

        if stripped.startswith(">"):
            paras = []
            cur = []
            while i < n and lines[i].strip().startswith(">"):
                content = lines[i].strip()[1:].strip()
                if not content:
                    if cur:
                        paras.append(" ".join(cur))
                        cur = []
                else:
                    cur.append(content)
                i += 1
            if cur:
                paras.append(" ".join(cur))
            inner = "".join(f"<p>{inline(p)}</p>" for p in paras if p)
            out.append(f"<blockquote>{inner}</blockquote>")
            continue

        if BULLET_RE.match(stripped):
            items = []
            is_cb = False
            while i < n and BULLET_RE.match(lines[i].strip()):
                it = BULLET_RE.match(lines[i].strip()).group(1)
                cb = CHECKBOX_RE.match(it)
                if cb:
                    is_cb = True
                    cls = "checked" if cb.group(1) in "xX" else "unchecked"
                    items.append((f"cb {cls}", cb.group(2)))
                else:
                    items.append(("plain", it))
                i += 1
            if is_cb:
                lis = "".join(
                    f'<li class="cb {cls}">{inline(txt)}</li>' for cls, txt in items
                )
                out.append(f'<ul class="checklist">{lis}</ul>')
            else:
                out.append("<ul>" + "".join(f"<li>{inline(t)}</li>" for _, t in items) + "</ul>")
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
# CSS — named pages (running heads) + typography
# ---------------------------------------------------------------------------

def build_css(footer_text):
    rules = []

    # --- base page + cover + footer ---
    rules.append(f"""
@page {{
  size: A4;
  margin: 22mm 18mm 20mm 18mm;
  @bottom-center {{ content: "{footer_text}"; font-size: 7.5pt; color: #8a97a5; }}
}}
@page :first {{ margin: 0; @bottom-center {{ content: none; }} }}
""")

    # --- running heads per chapter / appendix / TOC ---
    # NOTE: Chrome's ":first" only matches the document's very first page, so
    # chapter opener pages get their own page type (chNN-o) *without* a header
    # instead of relying on @page chNN:first.
    head_style = "font-size: 8pt; color: #41566d;"
    rules.append(
        '@page toc { @top-left { content: "สารบัญ / Table of Contents | P" counter(page); '
        + head_style + " } }"
    )

    for num, label in CH_HEADERS.items():
        rules.append(f"@page ch{num}o {{ @top-left {{ content: none; }} }}")  # opener: clean
        rules.append(
            f'@page ch{num} {{ @top-left {{ content: "{label} | P" counter(page); {head_style} }} }}'
        )
        rules.append(
            f'@page ch{num}i {{ @top-left {{ content: "{label} (Instructor) | P" counter(page); {head_style} }} }}'
        )

    for fname, label in APP_HEADERS.items():
        letter = fname.split("-")[1]
        rules.append(
            f'@page appx{letter} {{ @top-left {{ content: "{label} | P" counter(page); {head_style} }} }}'
        )

    # --- page-type assignment rules ---
    rules.append(".pg-toc { page: toc; }")
    for num in CH_NUMS:
        rules.append(f".pg-ch{num}o {{ page: ch{num}o; }}")
        rules.append(f".pg-ch{num} {{ page: ch{num}; }}")
        rules.append(f".pg-ch{num}i {{ page: ch{num}i; }}")
    for fname in APPENDICES:
        letter = fname.split("-")[1]
        rules.append(f".pg-appx{letter} {{ page: appx{letter}; }}")

    # --- typography ---
    rules.append(r"""
html { font-size: 10.5pt; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: "Sukhumvit Set", "Thonburi", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: #1c2a38; line-height: 1.62; margin: 0; background: #ffffff;
}

/* ---- chapter openers ---- */
.opener, .appendix, .instructor-section { break-before: page; }
.chapter-body { }
.opener h1, .chapter-body h1, .appendix h1, .instructor-section h1 {
  break-before: auto; font-size: 19pt; line-height: 1.35; color: #ffffff;
  background: linear-gradient(90deg, #0d1f3c 0%, #17406e 100%);
  padding: 20pt 22pt; margin: 0 0 16pt; border-radius: 6pt;
}
.kicker {
  margin: 0 0 8pt; font-size: 9pt; letter-spacing: 2.5pt;
  text-transform: uppercase; color: #2f6fb0; font-weight: 700;
}

/* ---- section headings ---- */
h2 {
  font-size: 14pt; color: #0d1f3c; margin: 16pt 0 7pt;
  padding: 3pt 0 3pt 9pt; border-left: 4pt solid #2f6fb0; break-after: avoid;
}
h3 { font-size: 12pt; color: #14345e; margin: 12pt 0 5pt; break-after: avoid; }
h4 { font-size: 10.5pt; color: #1b4a7e; margin: 10pt 0 4pt; break-after: avoid; }
p, li { font-size: 10.5pt; line-height: 1.62; orphans: 2; widows: 2; }
a { color: inherit; text-decoration: none; }

/* ---- tables ---- */
table { border-collapse: collapse; width: 100%; margin: 10pt 0; font-size: 9pt; }
th, td { border: 1px solid #c6d3e1; padding: 4.5pt 6.5pt; vertical-align: top; }
th { background: #173a5e; color: #ffffff; font-weight: 600; }
thead { display: table-header-group; }
tbody tr:nth-child(even) td { background: #f2f6fa; }
tr { break-inside: avoid; }

/* ---- blockquote callouts ---- */
blockquote {
  margin: 10pt 0; padding: 8pt 12pt; border-left: 3.5pt solid #2f6fb0;
  background: #eef5fc; border-radius: 0 5pt 5pt 0; break-inside: avoid;
}
blockquote p { margin: 0; }

/* ---- checklists ---- */
ul.checklist { list-style: none; padding-left: 2pt; }
ul.checklist li { margin: 3.5pt 0; }
li.cb.unchecked::before {
  content: ""; display: inline-block; width: 7.5pt; height: 7.5pt;
  border: 1.2pt solid #173a5e; border-radius: 2pt; margin-right: 7pt;
  vertical-align: -1pt; background: #ffffff;
}
li.cb.checked::before {
  content: "\2713"; display: inline-block; width: 7.5pt; height: 7.5pt;
  border: 1.2pt solid #173a5e; border-radius: 2pt; margin-right: 7pt;
  vertical-align: -1pt; color: #173a5e; font-size: 8pt; text-align: center; line-height: 7.5pt;
}

/* ---- code ---- */
pre {
  background: #0f1c2e; color: #eaf1fa; padding: 10pt 12pt; border-radius: 5pt;
  font-size: 8.5pt; white-space: pre-wrap; word-wrap: break-word; break-inside: avoid;
}
code { font-family: "SF Mono", Menlo, Consolas, monospace; }
p code, li code, td code, th code { background: #e8eef5; padding: 0 3px; border-radius: 3px; color: #0d1f3c; }

/* ---- cover ---- */
.cover {
  min-height: 297mm; box-sizing: border-box; color: #ffffff;
  background: linear-gradient(160deg, #0d1f3c 0%, #14345e 55%, #1b4a7e 100%);
  padding: 46mm 26mm 30mm;
}
.cover .brand { font-size: 10pt; letter-spacing: 3pt; text-transform: uppercase; color: #9fc0e8; margin: 0; }
.cover h1 { break-before: auto; font-size: 30pt; line-height: 1.25; margin: 10mm 0 6mm; color: #ffffff; }
.cover .byline { font-size: 12.5pt; color: #d7e5f5; margin: 0; }
.cover .rule { width: 55mm; height: 2.5pt; background: #4e8fd4; margin: 14mm 0; }
.cover .edition {
  display: inline-block; padding: 4pt 14pt; border: 1.5pt solid #9fc0e8;
  border-radius: 20pt; color: #e8f1fb; font-size: 11pt;
}
.cover .disclaimer { color: #8fa8c8; font-size: 8.5pt; margin-top: 20mm; }

/* ---- TOC ---- */
.toc { break-before: page; }
.toc h1 {
  break-before: auto; font-size: 19pt; color: #ffffff;
  background: linear-gradient(90deg, #0d1f3c, #17406e);
  padding: 16pt 22pt; margin: 0 0 16pt; border-radius: 6pt;
}
.toc ol { list-style: none; padding-left: 0; margin: 0; }
.toc > ol > li {
  margin: 0; padding: 6.5pt 2pt; border-bottom: 1px dotted #b9c6d4;
  font-weight: 600; font-size: 10.5pt;
}
.toc > ol > li a { color: #0d1f3c; }
.toc .sub { list-style: none; padding-left: 16pt; margin: 2pt 0 0; }
.toc .sub li { margin: 1.5pt 0; font-size: 9pt; color: #45566b; font-weight: 400; border: none; }

/* ---- instructor part dividers ---- */
.part-divider { break-before: page; text-align: center; padding-top: 62mm; background: #fdf3dc; min-height: 100mm; }
.part-divider h2 { break-after: auto; border-left: none; padding: 0; background: none; font-size: 20pt; color: #7a5200; }
.part-divider .banner { color: #8a5a00; font-weight: 600; margin-top: 8mm; font-size: 11pt; }
""")

    return "\n".join(rules)


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

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


def split_opener(body_html):
    """Split a converted chapter at the first <h2>.

    Returns (opener_html, rest_html). The opener (kicker + h1, plus any intro
    before the first numbered section) becomes a clean title page without a
    running head; the rest flows right after it with the chapter running head.
    """
    m = re.search(r"<h2", body_html)
    if not m:
        return "", body_html
    return body_html[: m.start()], body_html[m.start():]


def chapter_sections(body_html, num, kicker):
    """Build (opener_section, body_section) for a chapter's learner content."""
    kick = f'<p class="kicker">{html.escape(kicker, quote=False)}</p>' if kicker else ""
    opener_html, rest_html = split_opener(body_html)
    if opener_html:
        opener = f'<section class="opener pg-ch{num}o">{kick}{opener_html}</section>'
        body = f'<section class="chapter-body pg-ch{num}">{rest_html}</section>'
    else:
        opener = ""
        body = f'<section class="chapter-body pg-ch{num}">{kick}{body_html}</section>'
    return opener, body


def plain_section(body_html, page_class, kicker=None):
    kick = f'<p class="kicker">{html.escape(kicker, quote=False)}</p>' if kicker else ""
    return f'<section class="{page_class}">{kick}{body_html}</section>'


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

        opener, body = chapter_sections(learner_html, num, CH_KICKERS[num])
        learner_body_parts.append(opener)
        learner_body_parts.append(body)

        divider = f"""<section class="part-divider pg-ch{num}i">
<h2>เอกสารสำหรับผู้สอน — Ch.{num} {html.escape(chapter_label(num), quote=False)}</h2>
<p class="banner">เอกสารสำหรับผู้สอน มีเฉลยและเกณฑ์ให้คะแนน<br>Instructor-only: contains model answers and rubrics</p>
</section>"""
        body_parts.append(opener)
        body_parts.append(body)
        body_parts.append(divider)
        body_parts.append(plain_section(instr_html, f"instructor-section pg-ch{num}i", INSTR_KICKER))
        body_parts.append(plain_section(ans_html, f"instructor-section pg-ch{num}i", ANSKEY_KICKER))

    # Appendices
    for app in APPENDICES:
        path = os.path.join(APPENDICES_DIR, app)
        app_html = convert_file(path, "appendix-", seen_ids)
        app_id = re.search(r'<h1 id="([^"]+)"', app_html).group(1)
        letter = app.split("-")[1]
        app_toc = f'<li><a href="#{app_id}">{html.escape(app.replace(".md", ""), quote=False)}</a></li>'
        toc_entries.append(app_toc)
        toc_learner_entries.append(app_toc)
        body_parts.append(plain_section(app_html, f"appendix pg-appx{letter}"))
        learner_body_parts.append(plain_section(app_html, f"appendix pg-appx{letter}"))

    def build_cover(subtitle, edition):
        return f"""<section class="cover">
<p class="brand">PMBOK 8-Aligned · Project Delivery</p>
<h1>{html.escape(BOOK_TITLE, quote=False)}</h1>
<div class="rule"></div>
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
        return f"""<section class="toc pg-toc">
<h1>สารบัญ / Table of Contents</h1>
<ol>
{''.join(entries)}
</ol>
</section>"""

    toc_combined = build_toc(toc_entries)
    toc_learner = build_toc(toc_learner_entries)

    def full_page(cover_html, toc_html, body, css):
        return f"""<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<title>{html.escape(BOOK_TITLE, quote=False)}</title>
<style>{css}</style>
</head>
<body>
{cover_html}
{toc_html}
{body}
</body>
</html>
"""

    css_combined = build_css("PM Delivery Guide (Ver.2) · Combined Edition")
    css_learner = build_css("PM Delivery Guide (Ver.2) · Learner Edition")

    with open(BOOK_HTML, "w", encoding="utf-8") as f:
        f.write(full_page(cover_combined, toc_combined, "".join(body_parts), css_combined))
    print(f"Wrote {BOOK_HTML} ({os.path.getsize(BOOK_HTML)} bytes)")

    with open(BOOK_LEARNER_HTML, "w", encoding="utf-8") as f:
        f.write(full_page(cover_learner, toc_learner, "".join(learner_body_parts), css_learner))
    print(f"Wrote {BOOK_LEARNER_HTML} ({os.path.getsize(BOOK_LEARNER_HTML)} bytes)")

    render_pdf(BOOK_HTML, BOOK_PDF)
    render_pdf(BOOK_LEARNER_HTML, BOOK_LEARNER_PDF)


if __name__ == "__main__":
    main()

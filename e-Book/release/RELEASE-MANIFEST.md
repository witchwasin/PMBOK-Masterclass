---
document_type: Release Manifest
status: Ready for Release Packaging
author: Witchwasin K.
generated_on: 2026-07-22
---

# PMBOK-aligned Practical Masterclass Release Manifest

ผู้เรียบเรียง: Witchwasin K.

## Release Contents

| File | Purpose | Audience |
|---|---|---|
| [index.html](./index.html) | Release landing page linking the reader files | Learner |
| [PMBOK-Masterclass-Learner.html](./PMBOK-Masterclass-Learner.html) | HTML reader generated from the full learner Markdown | Learner |
| [PMBOK-Masterclass-Learner-Full.md](./PMBOK-Masterclass-Learner-Full.md) | Full learner e-book Markdown, source of truth for release reading | Learner |
| [PMBOK-Masterclass-Learner-eBook.md](./PMBOK-Masterclass-Learner-eBook.md) | Learner e-book front matter and reading guide | Learner |
| [PMBOK-Masterclass-Instructor-Companion.md](./PMBOK-Masterclass-Instructor-Companion.md) | Instructor companion notes | Instructor |
| [../pdf/PMBOK-Masterclass-Complete-Edition.pdf](../pdf/PMBOK-Masterclass-Complete-Edition.pdf) | Combined Learner + Instructor book-style PDF | Learner / Instructor |

## Release Notes

- This package is a PMBOK-aligned Practical Masterclass and is not official PMI material.
- Learner-facing files do not include instructor model answers or rubrics.
- A combined Learner + Instructor book-style PDF is produced by `../pdf/build_pdf.py` (weasyprint if available, Chrome headless otherwise) and stored at `../pdf/PMBOK-Masterclass-Complete-Edition.pdf`. EPUB export is not generated.
- Release files are self-contained for reading and review.

## Verification Snapshot

| Check | Result |
|---|---|
| Learner full word count | 21,604 by `wc -w` |
| Combined PDF export | Produced at `../pdf/PMBOK-Masterclass-Complete-Edition.pdf` |
| Author string | `Witchwasin K.` present in release metadata and reader files |
| Markdown link check | Passed |
| Repository validation | Passed |
| Diff whitespace check | Passed |
| Absolute path hygiene | Passed |
| Learner/instructor separation | Passed |

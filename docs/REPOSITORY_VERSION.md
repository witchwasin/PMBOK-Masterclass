---
title: Repository Version
version: 3.0.0
status: Active
last_updated: 2026-08-15
---

# PMBOK Masterclass — Repository Version

## Current Version: 3.0.0

Repository ประกอบด้วยเนื้อหา 2 ชุดที่อยู่คู่กัน

| ชุด | อิง PMBOK | โครงสร้าง | ขนาด |
|---|---|---|---|
| `lessons/` + `e-Book/` | 6th + 7th | 10 Knowledge Areas | 16 บทเรียน + Capstone |
| `field-guide/` | 8th | Workflow A→H (Pre-sales → Closure) | 11 บท (Ch.0–10) + Appendix A–F |

## Version History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-22 | Initial commit: Lesson 01 + partial Lessons 02–16 + governance files |
| 1.1.0 | 2026-07-22 | Folder restructure (`lessons/`, `governance/`, `references/`) + rebuild Lessons 02–16 |
| 2.0.0 | 2026-07-22 | Lessons 01–16 and Capstone released after Batch 1–3 validation |
| 2.1.0 | 2026-07-22 | e-Book compiled: 16 chapters + Capstone + combined PDF + release package |
| 2.2.0 | 2026-08-13 | `field-guide/` (PM Delivery Guide, PMBOK 8) written: Ch.0–10 + Appendix A–F |
| 2.3.0 | 2026-08-15 | Field-guide typography pass + content deepening across all 11 chapters; PDFs regenerated |
| **3.0.0** | **2026-08-15** | **Public release:** internal planning/QA files removed, `governance/` + `repository/` + `scripts/` consolidated into `docs/`, CC BY-NC 4.0 license added, entry-point READMEs rewritten |

## Structure

```text
README.md · LICENSE
field-guide/   e-Book/   lessons/   capstone/   scenarios/   references/   docs/
```

## Repository Checks

รันก่อน commit ทุกครั้ง:

```bash
bash docs/validate-repository.sh
```

ตรวจ metadata ของบทเรียน, absolute-path leakage และความถูกต้องของ relative link

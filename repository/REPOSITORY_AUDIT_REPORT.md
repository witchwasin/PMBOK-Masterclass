---
title: Repository Audit Report
document_type: Audit Report
audit_date: 2026-07-22
auditor: AI (Claude Opus 4.6)
repository_status: Structured Draft
---

# PMBOK Masterclass — Repository Audit Report

> **Pass 0 Deliverable** — ตรวจสอบก่อนแก้ไข ห้ามเขียน Lesson content ก่อน Audit เสร็จ

---

# 1. File Inventory

## 1.1 Governance Files

| Path | Purpose | Status | Quality | Action Required |
|---|---|---|---|---|
| `governance/CONTENT-RULES.md` | กำหนดกฎเนื้อหา | Exists | ⚠️ บาง (63 บรรทัด) ไม่ครอบคลุม §7 ทั้งหมด | Expand ใน Pass 1 |
| `governance/COURSE-ROADMAP.md` | Course architecture | Exists | ✅ ดี แต่ status ขัดแย้งกับ lesson metadata | Update status ใน Pass 1 |
| `governance/REPOSITORY-VALIDATION-AND-FULL-REBUILD.md` | Rebuild instructions | Exists | ✅ ครบถ้วน (1,317 บรรทัด) | ใช้เป็น execution guide |
| `governance/COURSE_STANDARD.md` | Lesson quality standard | **Missing** | — | Create ใน Pass 1 |
| `governance/STYLE_GUIDE.md` | Writing style rules | **Missing** | — | Create ใน Pass 1 |
| `governance/LESSON_TEMPLATE.md` | Mandatory section template | **Missing** | — | Create ใน Pass 1 |
| `governance/PM_GLOSSARY.md` | Terminology glossary | **Missing** | — | Create ใน Pass 1 |
| `governance/LESSON_INDEX.md` | Lesson index + status | **Missing** | — | Create ใน Pass 1 |
| `governance/AI_CONTINUATION_GUIDE.md` | AI handoff guide | **Missing** | — | Create ใน Pass 1 |
| `governance/REPOSITORY_VERSION.md` | Version tracking | **Missing** | — | Create ใน Pass 1 |

## 1.2 Reference Files

| Path | Purpose | Status | Quality | Action Required |
|---|---|---|---|---|
| `references/PMBOK-Overview.md` | Canonical Source | Exists | ✅ 628 บรรทัด ครบ PM Overview, Predictive, Agile, Hybrid | Keep as-is |

## 1.3 Scenario Files

| Path | Purpose | Status | Action Required |
|---|---|---|---|
| `scenarios/ERP-TRANSFORMATION-CASE.md` | ERP Scenario Master | **Missing** | Create ใน Pass 1 |
| `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` | Hotel Booking Scenario Master | **Missing** | Create ใน Pass 1 |

## 1.4 Repository Audit Files

| Path | Purpose | Status | Action Required |
|---|---|---|---|
| `repository/REPOSITORY_AUDIT_REPORT.md` | This file | Creating now | — |
| `repository/CONTENT_COVERAGE_MATRIX.md` | Content coverage | Creating now | — |
| `repository/TERMINOLOGY_AUDIT.md` | Terminology check | Creating now | — |
| `repository/LESSON_QUALITY_SCORECARD.md` | Lesson quality scores | Creating now | — |
| `repository/PMBOK-EDITION-POSITION.md` | PMBOK edition policy | Creating now | — |
| `repository/REPOSITORY_DECISION_LOG.md` | Decision log | **Missing** | Create ใน Pass 1 |
| `repository/FINAL-VALIDATION-REPORT.md` | Final validation | **Missing** | Create ใน Pass 7 |

## 1.5 Lesson Files

### Lesson 01

| File | Lines | Status | Quality | Action |
|---|---|---|---|---|
| `Lesson-01_1-Blueprint.md` | 476 | Exists | ✅ ดีที่สุดใน repo | Light Revision |
| `Lesson-01_2-Why-PM-Must-Know-PMBOK.md` | 387 | Exists | ✅ Quality baseline | Light Revision (เพิ่ม mandatory sections ที่ขาด) |
| `Lesson-01_3-Assessment.md` | **Missing** | — | — | Create |
| `Lesson-01_4-Source-Mapping.md` | **Missing** | — | — | Create |

### Lesson 02–04 (Foundation)

| File | Lines | Quality | Action |
|---|---|---|---|
| `Lesson-02_1-Blueprint.md` | 215 | ⚠️ ขาด Learner Profile, PM Decisions, Workshop Design, Assessment Design, Source Coverage | Full Rebuild |
| `Lesson-02_2-Project-Management-Overview.md` | 188 | ⚠️ ขาด 12+ mandatory sections | Full Rebuild |
| `Lesson-02_3-Assessment.md` | 332 | ⚠️ เน้น MC/T-F มากกว่า Decision | Full Rebuild |
| `Lesson-02_4-Source-Mapping.md` | 243 | ⚠️ Generic ไม่ map specific sections | Full Rebuild |
| `Lesson-03_1-Blueprint.md` | 209 | ⚠️ เหมือน L02 | Full Rebuild |
| `Lesson-03_2-…Process-Groups.md` | 174 | ⚠️ ขาด 12+ mandatory sections | Full Rebuild |
| `Lesson-03_3-Assessment.md` | 281 | ⚠️ เน้น MC/T-F | Full Rebuild |
| `Lesson-03_4-Source-Mapping.md` | 184 | ⚠️ Generic | Full Rebuild |
| `Lesson-04_1-Blueprint.md` | 195 | ⚠️ เหมือน L02-03 | Full Rebuild |
| `Lesson-04_2-…Knowledge-Areas.md` | 168 | ⚠️ ขาด 12+ mandatory sections | Full Rebuild |
| `Lesson-04_3-Assessment.md` | 305 | ⚠️ เน้น MC/T-F | Full Rebuild |
| `Lesson-04_4-Source-Mapping.md` | 218 | ⚠️ Generic | Full Rebuild |

### Lesson 05–16 (Core + Adaptive)

| Lesson | Blueprint | Lesson Content | Assessment | Source Mapping | Blueprint Quality | Content Quality | Assessment Quality | Mapping Quality |
|---|---|---|---|---|---|---|---|---|
| 05 | 129 lines | 168 lines | 159 lines | 83 lines | ⚠️ Thin | ⚠️ Thin | ⚠️ Template-ish | ⚠️ Generic |
| 06 | 129 lines | 153 lines | 159 lines | 83 lines | ⚠️ Thin | ⚠️ Thin | ⚠️ Template-ish | ⚠️ Generic |
| 07 | 133 lines | 154 lines | 159 lines | 87 lines | ⚠️ Thin | ⚠️ Thin | ⚠️ Template-ish | ⚠️ Generic |
| 08 | 134 lines | 153 lines | 159 lines | 88 lines | ⚠️ Thin | ⚠️ Thin | ⚠️ Template-ish | ⚠️ Generic |
| 09 | 134 lines | 160 lines | 159 lines | 88 lines | ⚠️ Thin | ⚠️ Thin | ⚠️ Template-ish | ⚠️ Generic |
| 10 | 139 lines | 157 lines | 159 lines | 93 lines | ⚠️ Thin | ⚠️ Thin | ⚠️ Template-ish | ⚠️ Generic |
| 11 | 133 lines | 156 lines | 159 lines | 87 lines | ⚠️ Thin | ⚠️ Thin | ⚠️ Template-ish | ⚠️ Generic |
| 12 | 135 lines | 145 lines | 159 lines | 89 lines | ⚠️ Thin | ⚠️ Thin | ⚠️ Template-ish | ⚠️ Generic |
| 13 | 139 lines | 154 lines | 159 lines | 93 lines | ⚠️ Thin | ⚠️ Thin | ⚠️ Template-ish | ⚠️ Generic |
| 14 | 133 lines | 148 lines | 159 lines | 87 lines | ⚠️ Thin | ⚠️ Thin | ⚠️ Template-ish | ⚠️ Generic |
| 15 | 141 lines | 155 lines | 159 lines | 95 lines | ⚠️ Thin | ⚠️ Thin | ⚠️ Template-ish | ⚠️ Generic |
| 16 | 137 lines | 146 lines | 159 lines | 91 lines | ⚠️ Thin | ⚠️ Thin | ⚠️ Template-ish | ⚠️ Generic |

**สิ่งที่สังเกตได้ทันที:**

1. **Lesson 05–16 Assessments ทุกบทมี 159 บรรทัดเท่ากันหมด** → Generated จาก template เดียวกัน ไม่ได้ปรับตาม lesson content
2. **Lesson 05–16 Blueprints มีขนาด ~130 บรรทัดเท่าๆ กัน** → Template-based, ไม่ได้ design เฉพาะบท
3. **Lesson 02–16 Content มีขนาด 145–188 บรรทัด** เทียบกับ Lesson 01 ที่มี 387 บรรทัด → น้อยกว่าครึ่ง

## 1.6 Other Files

| Path | Purpose | Status |
|---|---|---|
| `README.md` | Repo introduction | Exists, ต้อง update หลัง rebuild |
| `e-Book/` | Future e-book | Empty, เว้นไว้ |

---

# 2. Gap Analysis

## 2.1 Missing Concepts (ควรมีแต่ยังไม่มีในบทเรียน)

| Concept | Source | Expected Lesson | Current Status |
|---|---|---|---|
| PM Decision Thinking (structured format) | §7.8 Validation | ทุกบท | ❌ ไม่มีใน L02-16 |
| Workshop (judgement-based) | §7.17 Validation | ทุกบท | ❌ ไม่มี |
| Interview Questions | §7.15 Validation | ทุกบท | ❌ ไม่มี |
| PM Dictionary (per lesson) | §7.16 Validation | ทุกบท | ❌ ไม่มี |
| Executive Summary | §7.19 Validation | ทุกบท | ❌ ไม่มี |
| AI Continuation Context | §7.21 Validation | ทุกบท | ❌ ไม่มี |
| Learning Objectives (observable) | §7.4 Validation | ทุกบท | ❌ L02-16 ไม่มี |
| PM Insight | §7.9 Validation | ทุกบท | ❌ ไม่มี |
| Real Enterprise Example | §7.12 Validation | ทุกบท | ❌ ไม่มี |
| Common Mistakes (vs Misconceptions) | §7.13 Validation | ทุกบท | ❌ ไม่แยก Mistakes vs Misconceptions |
| Source Classification labels | §4 Validation | ทุกบท | ❌ ไม่แยก PMBOK / Best Practice / Enterprise / Teaching / Opinion |
| PMBOK 7 Principles | Canonical Source §1 | L01 or L02 | ⚠️ กล่าวถึงเล็กน้อย ไม่ชัด |
| 12 Agile Principles | Canonical Source §5 | L15 | ⚠️ กล่าวถึงแต่ไม่ครบ |

## 2.2 Overlapping Concepts

| Concept | Lessons ที่ซ้ำ | ปัญหา |
|---|---|---|
| Value Chain (Business Need → Business Value) | L01, L02, L05 | ซ้ำ 3 บท ระดับใกล้เคียงกัน |
| Output vs Outcome | L01, L02 | ซ้ำ 2 บท |
| Tailoring | L01, L05, L16 | ซ้ำ 3 บท ต้องแบ่ง scope ให้ชัด |

## 2.3 Premature Concepts

| Concept | Lesson ที่ปรากฏ | ควรอยู่ใน |
|---|---|---|
| ไม่พบ premature concept ร้ายแรง | — | — |

## 2.4 Unsupported Assertions

| Assertion | Lesson | ปัญหา |
|---|---|---|
| ตัวเลข Budget/Timeline ใน scenarios | L05-16 | ไม่มี Scenario Master ที่ lock ตัวเลข ตัวเลขอาจถูกสร้างขึ้นโดย AI |
| `status: Active` ใน metadata | L02-16 | ขัดแย้งกับ Roadmap ที่ระบุ Draft/Planned |

---

# 3. Root Cause Analysis

## 3.1 ทำไมบทเรียนจึงอ่อน

| Root Cause | หลักฐาน |
|---|---|
| **Generated จาก topic list ไม่ใช่ learning objective** | L02-16 ไม่มี observable Learning Objectives |
| **ไม่มี learner persona** | ไม่มี lesson ใดระบุ intended learner level |
| **ไม่มี narrative progression ข้ามบท** | แต่ละบทเป็นอิสระ ไม่มี scenario state carry-over |
| **ใช้ template เดียวกัน** | Assessment L05-16 ทุกบทมี 159 บรรทัดเท่ากัน, Blueprint L05-16 มีขนาดใกล้เคียงกัน (~130 บรรทัด) |
| **ไม่มี scenario continuity** | ไม่มี Scenario Master, ตัวเลขไม่ lock |
| **ไม่มี cross-lesson memory** | ไม่มี AI Continuation Context |
| **Assessment disconnected จาก lesson** | Assessment ถูก generate แยกจาก lesson content |
| **Source ไม่ถูก map เฉพาะเจาะจง** | Source Mapping L05-16 เป็น generic (~85 บรรทัด) |
| **Lesson boundary ไม่ถูก enforce** | Value Chain ซ้ำใน L01, L02, L05 |
| **ข้าม Audit ไป Rewrite ทันที** | ไม่มี Audit Report ก่อน commit ล่าสุด |

## 3.2 ทำไม Governance จึงขาด

AI รุ่นก่อนอ่าน `REPOSITORY-VALIDATION-AND-FULL-REBUILD.md` แล้ว skip ไป Rewrite ทันที โดยไม่สร้าง:
- Audit Report
- Coverage Matrix
- Course Standard
- Style Guide
- Lesson Template
- PM Glossary
- Scenario Master files

---

# 4. Rebuild Priority

## Classification per Lesson

| Lesson | Classification | เหตุผล |
|---|---|---|
| 01 | **Light Revision** | Strong narrative, ขาด mandatory sections (Workshop, Interview, Dictionary, Executive Summary, AI Context) |
| 02 | **Full Rebuild** | มีโครง 9 steps แต่ขาด 12+ mandatory sections |
| 03 | **Full Rebuild** | เหมือน L02 |
| 04 | **Full Rebuild** | เหมือน L02 |
| 05 | **Full Rebuild** | เหมือน L02 + scenario ตัวเลขไม่ lock |
| 06 | **Full Rebuild** | เหมือน L05 |
| 07 | **Full Rebuild** | เหมือน L05 |
| 08 | **Full Rebuild** | เหมือน L05 |
| 09 | **Full Rebuild** | เหมือน L05 |
| 10 | **Full Rebuild** | เหมือน L05 |
| 11 | **Full Rebuild** | เหมือน L05 |
| 12 | **Full Rebuild** | เหมือน L05 |
| 13 | **Full Rebuild** | เหมือน L05 |
| 14 | **Full Rebuild** | เหมือน L05 |
| 15 | **Full Rebuild** | เหมือน L05 |
| 16 | **Full Rebuild** | เหมือน L05 |

## Rebuild Order

1. Governance + Scenarios (Pass 1)
2. All 16 Blueprints (Pass 2)
3. Lesson Content: Batch A (L01-04) → B (L05-09) → C (L10-14) → D (L15-16) (Pass 3)
4. Assessments & Workshops (Pass 4)
5. Source Mappings (Pass 5)
6. Cross-Lesson Integration (Pass 6)
7. Final Validation (Pass 7)

---

# 5. Critical Issues Summary

| # | Issue | Severity | Impact |
|---|---|---|---|
| 1 | ไม่มี Scenario Master files | 🔴 Critical | ตัวเลข scenario ไม่ lock, ไม่มี continuity |
| 2 | ขาด 12+ mandatory sections ต่อบท | 🔴 Critical | ไม่ถึง Masterclass standard |
| 3 | Assessment เป็น template ไม่ใช่ lesson-specific | 🔴 Critical | ไม่ test decision-making |
| 4 | ไม่มี PM Decision Thinking structure | 🔴 Critical | หยุดที่ Concept→Explanation |
| 5 | Status metadata ขัดแย้ง (`Active` vs `Draft`) | 🟡 Medium | ทำให้เข้าใจผิดว่าพร้อม |
| 6 | Internal links ใช้ absolute path | 🟡 Medium | ใช้ไม่ได้บน GitHub |
| 7 | Governance files ขาดหลายไฟล์ | 🟡 Medium | ไม่มี standard ควบคุม quality |
| 8 | Source Classification ไม่มี | 🟡 Medium | ผู้เรียนไม่รู้ว่าส่วนไหนเป็น PMBOK จริง |
| 9 | L01 ขาด Assessment & Source Mapping files | 🟡 Medium | ไม่ครบ standard package |
| 10 | CONTENT-RULES.md บางเกินไป | 🟡 Medium | ไม่เพียงพอควบคุม 16 บท |

---

# 6. Broken Links

| File | Broken Link | Should Be |
|---|---|---|
| `lessons/lesson-02/Lesson-02_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-03/Lesson-03_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-04/Lesson-04_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-05/Lesson-05_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-06/Lesson-06_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-07/Lesson-07_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-08/Lesson-08_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-09/Lesson-09_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-10/Lesson-10_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-11/Lesson-11_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-12/Lesson-12_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-13/Lesson-13_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-14/Lesson-14_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-15/Lesson-15_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |
| `lessons/lesson-16/Lesson-16_2-…md` | `file:///Users/arm/…/PMBOK-Overview.md` | `../../references/PMBOK-Overview.md` |

**Total: 15 files มี absolute path links**

---

# 7. Next Steps

> Pass 0 เสร็จเมื่อไฟล์ Audit ทั้ง 5 ถูกสร้างครบ:
> 1. ✅ `REPOSITORY_AUDIT_REPORT.md` (this file)
> 2. ⏳ `CONTENT_COVERAGE_MATRIX.md`
> 3. ⏳ `TERMINOLOGY_AUDIT.md`
> 4. ⏳ `LESSON_QUALITY_SCORECARD.md`
> 5. ⏳ `PMBOK-EDITION-POSITION.md`
>
> จากนั้นเข้า Pass 1 — Governance & Architecture

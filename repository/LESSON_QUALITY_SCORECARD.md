---
title: Lesson Quality Scorecard
document_type: Quality Scorecard
baseline_audit_date: 2026-07-22
latest_rescore_date: 2026-07-22
current_release_scope: Lessons 01-05
scoring_standard: "§14.2 of REPOSITORY-VALIDATION-AND-FULL-REBUILD.md"
scale: 0-5
minimum_release_threshold:
  no_category_below: 3
  average_at_least: 4
  source_transparency: 5
  terminology_consistency: 5
  pm_decision_thinking: 4
  assessment_quality: 4
---

# PMBOK Masterclass — Lesson Quality Scorecard

> Current release score อยู่ในส่วนแรก ส่วนคะแนนก่อน rebuild ถูกเก็บไว้เป็น historical baseline และห้ามใช้ตัดสินสถานะปัจจุบัน

## Current Post-Rebuild Score — Batch 1

| Dimension | L01 | L02 | L03 | L04 | L05 |
|---|---:|---:|---:|---:|---:|
| Accuracy | 5 | 5 | 5 | 5 | 5 |
| Depth | 4 | 4 | 4 | 4 | 5 |
| Why-before-What | 5 | 5 | 5 | 5 | 5 |
| Mental Model | 5 | 5 | 5 | 5 | 5 |
| Narrative Flow | 5 | 4 | 4 | 4 | 4 |
| PM Thinking | 4 | 4 | 4 | 4 | 5 |
| PM Decision Thinking | 4 | 4 | 4 | 4 | 5 |
| ERP Continuity | 4 | 5 | 5 | 5 | 5 |
| Hotel Booking Continuity | 4 | 5 | 5 | 5 | 4 |
| Misconception Correction | 5 | 5 | 5 | 5 | 5 |
| Assessment Quality | 4 | 5 | 5 | 5 | 5 |
| Source Transparency | 5 | 5 | 5 | 5 | 5 |
| Terminology Consistency | 5 | 5 | 5 | 5 | 5 |
| Lesson Boundary | 5 | 5 | 5 | 5 | 5 |
| Connection to Adjacent | 5 | 5 | 5 | 5 | 5 |
| **Average** | **4.60** | **4.73** | **4.73** | **4.73** | **4.87** |
| **Release Gate** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

### Rescore Evidence

- Artifact Contract และ governance roles อยู่ใน Blueprint ทุกบท
- Metadata Contract ครบทั้ง Blueprint, Main Lesson, Assessment และ Source Mapping; Strict validator ปฏิเสธ deprecated fields
- learner/instructor assets แยกกันและมี Thinking Walkthrough, Completed Example, Model Answer, Checklist และ Rubric
- Assessment แบบ release ใช้ application/judgement 90% และ retrieval 10%
- Source Mapping ระบุ canonical/scenario/opinion boundaries ของ lesson และ learning assets
- Scenario และ terminology ผ่าน Batch 1 Integration Review
- Narrative ไม่มี Reflection/Bridge ปิดบทก่อน mandatory learning path อีกต่อไป

## Historical Pre-Rebuild Baseline — Superseded

คะแนนด้านล่างบันทึกสภาพก่อน Batch 1 rebuild เท่านั้น ไม่ใช่สถานะ release ปัจจุบัน

---

## Scoring Scale

| Score | Meaning |
|---|---|
| 0 | ไม่มี / Placeholder |
| 1 | มีแต่ไม่ถูกต้องหรือไม่มีคุณภาพ |
| 2 | มีโครง แต่ตื้นหรือไม่ครบ |
| 3 | ใช้ได้ ครบตามพื้นฐาน |
| 4 | ดี มีคุณภาพชัด |
| 5 | ยอดเยี่ยม ถึง Masterclass standard |

**Release Gate:** ไม่มีหมวดต่ำกว่า 3, เฉลี่ย ≥ 4, Source Transparency = 5, Terminology = 5, PM Decision Thinking ≥ 4, Assessment ≥ 4

---

## Lesson 01 — ทำไม Project Manager ต้องรู้ PMBOK

| Dimension | Score | Note |
|---|---|---|
| Accuracy | 4 | ถูกต้องตาม Canonical Source |
| Depth | 4 | เจาะลึกเหตุผลและ Mental Model |
| Why-before-What | 5 | เริ่มจาก PM 3 คน ก่อนเข้า Definition |
| Mental Model | 5 | มี Mental Model ชัดเจน |
| Narrative Flow | 5 | อ่านแล้วต่อเนื่อง มี story |
| PM Thinking | 4 | มีมุมคิดแต่ไม่มี structured format |
| PM Decision Thinking | 2 | ❌ ไม่มี structured Decision format ตาม §7.8 |
| ERP Continuity | 3 | มี ERP แต่ไม่ lock ข้อมูล |
| Hotel Booking Continuity | 3 | มี Hotel Booking แต่ไม่ lock ข้อมูล |
| Misconception Correction | 4 | มีหลายจุด |
| Assessment Quality | 0 | ❌ ไม่มีไฟล์ Assessment |
| Source Transparency | 2 | ❌ ไม่แยก PMBOK / Best Practice / Teaching / Opinion |
| Terminology Consistency | 3 | ใช้ได้แต่ไม่ lock term |
| Lesson Boundary | 4 | ไม่ล้ำ scope |
| Connection to Adjacent | 4 | เชื่อมไป L02 |
| **Average** | **3.2** | ❌ **ไม่ผ่าน Release Gate** (Assessment = 0, Source Transparency = 2) |

**Classification: Light Revision** — เพิ่ม Assessment, Source Mapping, PM Decision Thinking, Source Classification

---

## Lesson 02 — Project Management Overview

| Dimension | Score | Note |
|---|---|---|
| Accuracy | 3 | ถูกต้อง |
| Depth | 2 | หยุดที่ Surface explanation |
| Why-before-What | 3 | มี Opening Question |
| Mental Model | 3 | มี Value Chain |
| Narrative Flow | 2 | อ่านได้แต่ขาด story เหมือน L01 |
| PM Thinking | 2 | มี 3-Question Filter แต่ไม่ลึก |
| PM Decision Thinking | 1 | ❌ ไม่มี structured format |
| ERP Continuity | 2 | มีแต่ไม่ lock ข้อมูล |
| Hotel Booking Continuity | 2 | มีแต่ไม่ lock ข้อมูล |
| Misconception Correction | 3 | มี 4 ข้อ |
| Assessment Quality | 2 | มี MC/T-F/Scenario แต่ไม่มี Decision Case |
| Source Transparency | 1 | ❌ ไม่แยก source classification |
| Terminology Consistency | 2 | ไม่ lock term |
| Lesson Boundary | 3 | OK |
| Connection to Adjacent | 3 | มี Bridge |
| **Average** | **2.2** | ❌ **ไม่ผ่าน Release Gate** |

**Classification: Full Rebuild**

---

## Lesson 03–16 Summary Table

> L03-16 มีปัญหาเชิงโครงสร้างเหมือนกัน จึงสรุปเป็นตาราง

| Dimension | L03 | L04 | L05 | L06 | L07 | L08 | L09 | L10 | L11 | L12 | L13 | L14 | L15 | L16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Accuracy | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| Depth | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Why-before-What | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| Mental Model | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Narrative Flow | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| PM Thinking | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| PM Decision Thinking | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ERP Continuity | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 |
| Hotel Booking Continuity | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Misconception Correction | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 3 |
| Assessment Quality | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Source Transparency | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Terminology | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Lesson Boundary | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| Connection | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 3 |
| **Average** | **2.2** | **2.2** | **2.3** | **2.2** | **2.2** | **2.2** | **2.3** | **2.2** | **2.2** | **2.1** | **2.2** | **2.2** | **2.1** | **2.1** |

**All L03-16: ❌ ไม่ผ่าน Release Gate → Classification: Full Rebuild**

---

## Overall Summary

| Lesson | Average Score | Release Gate | Classification |
|---|---|---|---|
| L01 | 3.2 | ❌ FAIL (Assessment=0, Source=2) | Light Revision |
| L02 | 2.2 | ❌ FAIL | Full Rebuild |
| L03 | 2.2 | ❌ FAIL | Full Rebuild |
| L04 | 2.2 | ❌ FAIL | Full Rebuild |
| L05 | 2.3 | ❌ FAIL | Full Rebuild |
| L06 | 2.2 | ❌ FAIL | Full Rebuild |
| L07 | 2.2 | ❌ FAIL | Full Rebuild |
| L08 | 2.2 | ❌ FAIL | Full Rebuild |
| L09 | 2.3 | ❌ FAIL | Full Rebuild |
| L10 | 2.2 | ❌ FAIL | Full Rebuild |
| L11 | 2.2 | ❌ FAIL | Full Rebuild |
| L12 | 2.1 | ❌ FAIL | Full Rebuild |
| L13 | 2.2 | ❌ FAIL | Full Rebuild |
| L14 | 2.2 | ❌ FAIL | Full Rebuild |
| L15 | 2.1 | ❌ FAIL | Full Rebuild |
| L16 | 2.1 | ❌ FAIL | Full Rebuild |

---

## Major Weaknesses Across All Lessons

| Weakness | Occurrences | Impact |
|---|---|---|
| No structured PM Decision Thinking (§7.8) | 16/16 lessons | 🔴 Critical — จุดอ่อนหลักของ repo |
| No Source Classification labels (§4) | 15/16 lessons | 🔴 Critical — ผู้เรียนไม่รู้ว่าส่วนไหนเป็น PMBOK |
| Assessment ไม่ test decision-making | 15/16 lessons (L01 ไม่มี assessment) | 🔴 Critical |
| No Workshop | 16/16 lessons | 🔴 Critical |
| No Interview Questions | 16/16 lessons | 🟡 Medium |
| No PM Dictionary | 16/16 lessons | 🟡 Medium |
| No Executive Summary | 16/16 lessons | 🟡 Medium |
| No AI Continuation Context | 16/16 lessons | 🟡 Medium |
| No Learning Objectives (observable) | 15/16 lessons | 🟡 Medium |
| Scenario ไม่ lock ข้อมูล | 16/16 lessons | 🔴 Critical |

---

## Target Scores After Rebuild

| Dimension | Current Avg | Target Avg |
|---|---|---|
| Accuracy | 3.0 | 5.0 |
| Depth | 2.1 | 4.0 |
| Why-before-What | 3.1 | 4.5 |
| Mental Model | 2.3 | 4.0 |
| Narrative Flow | 2.3 | 4.5 |
| PM Thinking | 2.1 | 4.0 |
| PM Decision Thinking | 1.1 | 4.0 |
| ERP Continuity | 1.9 | 4.5 |
| Hotel Booking Continuity | 2.0 | 4.5 |
| Misconception | 2.9 | 4.0 |
| Assessment | 1.7 | 4.0 |
| Source Transparency | 1.1 | 5.0 |
| Terminology | 2.1 | 5.0 |
| Boundary | 3.0 | 4.0 |
| Connection | 2.9 | 4.0 |
| **Overall** | **2.2** | **≥ 4.3** |

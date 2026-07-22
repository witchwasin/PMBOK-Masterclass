---
lesson: 4
sequence: 4.1
title: 10 Project Management Knowledge Areas Overview
document_type: Blueprint
difficulty: Foundation
estimated_study_time: 15
status: Active
validation_status: Validated
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 01 — ทำไม Project Manager ต้องรู้ PMBOK
  - Lesson 02 — Project Management Overview
  - Lesson 03 — 5 Project Management Process Groups
related_lessons:
  - Lesson 03 — 5 Project Management Process Groups
  - Lesson 04 — 10 Project Management Knowledge Areas Overview
  - Lesson 05 — Project Integration Management
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
artifact_inputs:
  - ../lesson-03/learner/Artifact-Template.md — Lifecycle and Process Group Map
artifact_outputs:
  - name: PM Coverage and Cross-impact Map
    creator: Learner in Project Manager role
    artifact_owner: Project Manager
    reviewer: Knowledge-area Owners and PMO
    approval_authority: Change Authority or Sponsor according to decision threshold
    approval_evidence: Integrated impact review decision
next_lesson_usage:
  - Lesson 05 ใช้ dependencies, decision owners และ impacts เพื่อร่าง Charter, Governance และ Change Decision Record
acceptance_level:
  incomplete: ลิสต์ Knowledge Areas โดยไม่แสดง dependency หรือ owner
  usable: แสดง impact, missing evidence, owner และ escalation ของการเปลี่ยนแปลงได้
  professional: เชื่อม impacts กับ baseline, governance threshold, recommendation และ decision evidence ได้ครบ
---

# Lesson 04_1 — Blueprint: 10 Project Management Knowledge Areas Overview

## 0. Learner Profile and Prerequisites

- **Learner profile:** ผู้เรียนที่เข้าใจ flow ของ Process Groups แต่ยังมอง scope, schedule, cost และคนเป็นเรื่องแยกส่วน
- **Required prerequisite:** Lesson 01–03
- **Entry evidence:** อธิบายได้ว่า requirement ใหม่หนึ่งข้ออาจกระทบงานมากกว่า timeline
- **Scenario state:** ใช้ baseline ERP v1.0 และ Hotel Booking v1.0 เพื่อแสดง dependency เท่านั้น; ไม่ลงลึก process ของแต่ละ Knowledge Area

## 1. Purpose

Lesson 04 มีหน้าที่สร้าง “แผนที่องค์ความรู้” ของ Project Management ทั้ง 10 ด้าน ก่อนเข้าสู่การเรียนราย Knowledge Area

บทนี้ต้องทำให้ผู้เรียนเข้าใจว่า:

- Project Management ไม่ได้มีเพียง Schedule และ Status
- Knowledge Areas เป็นมุมมองการบริหารที่เชื่อมกัน
- แต่ละ Knowledge Area มีหน้าที่ต่างกัน
- Process Groups บอกว่า “เรากำลังบริหารช่วงไหน”
- Knowledge Areas บอกว่า “เรากำลังบริหารเรื่องอะไร”
- Integration Management ทำหน้าที่เชื่อมผลกระทบทั้งหมดเข้าด้วยกัน
- การตัดสินใจในหนึ่ง Knowledge Area มักกระทบอีกหลาย Knowledge Areas

---

## 2. Opening Question

> ถ้าโครงการตรงเวลาและไม่เกินงบ แต่ผู้ใช้ไม่ยอมใช้ระบบ โครงการนี้บริหารดีแล้วหรือยัง?

คำถามนี้ใช้เปิดบท เพื่อทำให้ผู้เรียนเห็นว่า Schedule และ Cost เป็นเพียงบางมิติของ Project Success

---

## 3. Core Teaching Message

> **Knowledge Areas ไม่ใช่กล่องงานสิบกล่องที่แยกจากกัน แต่เป็นระบบความรับผิดชอบสิบด้านที่ต้องถูกเชื่อมด้วย Integration Management**

---

## 4. Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบายความหมายของ Knowledge Area
2. ระบุ 10 Knowledge Areas ได้
3. อธิบายหน้าที่ระดับภาพรวมของแต่ละ Knowledge Area
4. แยก Process Groups ออกจาก Knowledge Areas
5. อธิบาย Knowledge Area × Process Group Matrix
6. อธิบายเหตุผลที่ Integration Management เป็นแกนกลาง
7. วิเคราะห์ผลกระทบข้าม Knowledge Areas
8. ใช้ ERP และ Hotel Booking วิเคราะห์ Project Health
9. ระบุความเข้าใจผิดที่พบบ่อย
10. เตรียมพร้อมเข้าสู่ Integration Management

---

## 5. Narrative Flow

1. ทบทวนจาก Lesson 03
2. Process Groups บอก “เมื่อไร” และ Knowledge Areas บอก “เรื่องอะไร”
3. ภาพรวม 10 Knowledge Areas
4. Integration Management
5. Stakeholder Management
6. Procurement Management
7. Resource Management
8. Communications Management
9. Scope Management
10. Schedule Management
11. Cost Management
12. Risk Management
13. Quality Management
14. Knowledge Area × Process Group Matrix
15. Interdependency
16. ERP Example
17. Hotel Booking Example
18. Common Misconceptions
19. PM Thinking
20. Reflection
21. Bridge to Lesson 05

---

## 6. 10 Knowledge Areas

1. Project Integration Management
2. Project Stakeholder Management
3. Project Procurement Management
4. Project Resource Management
5. Project Communications Management
6. Project Scope Management
7. Project Schedule Management
8. Project Cost Management
9. Project Risk Management
10. Project Quality Management

ลำดับนี้ยึดตาม Canonical Source ของหลักสูตร

---

## 7. Core Concept

```text
Process Groups = เรากำลังบริหาร “ช่วงไหน”
Knowledge Areas = เรากำลังบริหาร “เรื่องอะไร”
Integration = เรากำลังเชื่อม “ผลกระทบทั้งหมด” อย่างไร
```

---

## 8. Core Scenario A — ERP Transformation

ใช้สอน:

- Scope change กระทบ Schedule, Cost, Quality และ Risk
- Stakeholder resistance กระทบ Adoption
- Procurement decision กระทบ Vendor, Cost และ Timeline
- Data Migration กระทบ Quality และ Go-live
- Resource availability กระทบ Testing
- Communication failure กระทบ Change Management
- Integration ทำหน้าที่รวม Decision

---

## 9. Core Scenario B — Hotel Booking Digital Platform

ใช้สอน:

- Feature scope กระทบ Release Date
- Payment defect กระทบ Quality, Risk และ Business Value
- Inventory integration กระทบ Customer Experience
- Marketing launch กระทบ Schedule และ Readiness
- Hotel Partner engagement กระทบ Data Accuracy
- Cloud cost กระทบ Cost
- Product decision กระทบ Scope, UX และ Conversion

---

## 10. Misconceptions to Correct

- Knowledge Areas คือ Department
- Knowledge Areas ทำงานแยกกัน
- PM ต้องเป็นผู้เชี่ยวชาญลึกที่สุดทุกด้าน
- Scope สำคัญกว่า Quality เสมอ
- Risk เป็นหน้าที่ Risk Manager
- Communication คือส่ง Report
- Stakeholder คือผู้บริหารเท่านั้น
- Procurement คือฝ่ายจัดซื้อเท่านั้น
- Integration คือการรวมเอกสาร
- Knowledge Areas ใช้เฉพาะ Predictive

---

## 11. Boundaries

บทนี้ไม่ลงลึก Process ราย Knowledge Area

หัวข้อต่อไปนี้กล่าวได้ระดับ Overview เท่านั้น:

- Charter
- Change Control
- Stakeholder Grid
- WBS
- Critical Path
- EVM
- Risk Response
- Quality Tools
- Contract Types
- RACI
- Communication Plan

---

## 12. Completion Criteria

Lesson 04 ถือว่าสมบูรณ์เมื่อ:

- ครบ 10 Knowledge Areas
- แยก Process Groups กับ Knowledge Areas
- อธิบาย Integration เป็นแกนกลาง
- แสดงผลกระทบข้าม Knowledge Areas
- ใช้ ERP และ Hotel Booking
- ไม่ลงลึกเกินขอบเขต
- มี Assessment และ Source Mapping
- เชื่อมไป Lesson 05 ได้

---

## 13. PM Decisions to Practise

| Decision | Owner | Inputs / missing information | Options and trade-off | Evidence / next action |
|---|---|---|---|---|
| จะประเมิน scope change แบบแยกทีม หรือ integrated impact review | PM กับ change authority | requirement, WBS, schedule, cost, quality, risk, stakeholder, procurement impacts; ยังไม่รู้ acceptance criteria | แยกทีมเร็วแต่พลาด dependency; integrated review ช้ากว่าแต่เห็นผลกระทบจริง | impact log, change decision, updated baselines |
| ความเสี่ยงใดต้อง escalate | PM / sponsor | probability, impact, risk appetite, contingency; ยังไม่รู้ tolerance ของ sponsor | รับไว้ในทีมรวดเร็วแต่เกิน authority; escalate ปลอดภัยแต่ทำให้ช้า | risk register, escalation record, response owner |
| ใครควรเป็น owner ของ cross-area decision | Sponsor / PM ตาม governance | RACI, authority, affected owners | PM ตัดสินใจเร็วแต่เกิน mandate; committee ตัดสินใจช้ากว่าแต่มี legitimacy | decision rights matrix, meeting decision log |

## 14. Workshop and Assessment Design

**Workshop:** Hotel Booking ต้องเพิ่ม “corporate booking” ก่อน High Season. ผู้เรียนเป็น PM และทำ one-page integrated impact map ครอบคลุม Scope, Schedule, Cost, Quality, Resource, Communication, Risk, Procurement, Stakeholder และ Integration. ระบุข้อมูลที่ขาด, owner, trade-off, และ escalation path. ประเมินจาก dependency (35%), missing information (25%), decision logic (25%), clarity (15%).

**Assessment mix:** Cross-Knowledge Analysis 45%; Artifact Review ของ change request ที่ไม่มี risk/stakeholder impact 30%; Trade-off Case 15%; terminology check 10%. คำตอบต้องแยก “knowledge area ที่ได้รับผลกระทบ” ออกจาก “process group ที่กำลังทำงาน”.

## 15. Source Coverage and Lesson Handoff

| Coverage | Source classification | Boundary |
|---|---|---|
| Ten Knowledge Areas and Integration relationship | `[PMBOK 6]` | ใช้เป็น conceptual map ไม่อ้างว่าเป็น PMBOK 7 structure |
| Cross-functional impact review | `[Best Practice]` | ไม่แทน detailed techniques ใน Lesson 05–14 |
| ERP / Hotel examples | `[Teaching Scenario]` | Scenario Master v1.0 |
| Priority and escalation advice | `[Professional Opinion]` | ต้องเปิดเผย assumption |

**Handoff to Lesson 05:** เมื่อผู้เรียนเห็นความสัมพันธ์ของ areas แล้ว Lesson 05 จะสอน Integration Management ในฐานะการตัดสินใจที่เชื่อมแผนและผลกระทบทั้งหมด ไม่ใช่ “area ที่สิบเอ็ด”.

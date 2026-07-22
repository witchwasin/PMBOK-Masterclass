---
lesson: 8
sequence: 8.1
title: Project Schedule Management
document_type: Blueprint
level: Core
status: Draft
validation_status: Not Validated
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 07
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 08_1 — Blueprint: Project Schedule Management

## 0. Learner Profile, Prerequisites, and Scenario State

- **Learner profile:** ผู้เรียนที่มี scope/WBS แต่ยังมอง schedule เป็นรายการวันที่ ไม่ใช่ model ของ dependency และ uncertainty.
- **Required prerequisite:** Lesson 01–07; ต้องอ่าน WBS เป็น deliverable/work package ได้.
- **Entry evidence:** ระบุได้ว่างานที่ล่าช้า 1 งานอาจไม่กระทบ finish date หากมี float.
- **Scenario state:** ERP baseline: Blueprint 8 สัปดาห์ → Build 12 → SIT 4 → UAT 4 → Final Migration 2 → Parallel Run 4 → Cutover 2; Hotel Booking baseline: Sprint 0–12 และ pilot 3 โรงแรมก่อน full launch.

## 1. Purpose

บทนี้ทำหน้าที่พาผู้เรียนจากภาพรวมในบทก่อนหน้าเข้าสู่ความเข้าใจเชิงลึกของ **Project Schedule Management** โดยยังคงแนวทางการสอนแบบ:

- เริ่มจากคำถามและสถานการณ์
- อธิบายเหตุผลก่อน Definition
- เชื่อม Framework กับ Decision จริง
- ใช้ ERP Transformation และ Hotel Booking Digital Platform
- แก้ความเข้าใจผิด
- ปิดด้วย Reflection และ Assessment

## 2. Opening Question

> งานทุกงานที่ล่าช้า ส่งผลต่อวันจบโครงการเท่ากันหรือไม่?

## 3. Core Teaching Message

> **Schedule Management ไม่ใช่การใส่วันที่ใน Gantt Chart แต่คือการเข้าใจ Logic, Dependency และ Critical Path ของงาน**

## 4. Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบายวัตถุประสงค์ของ Project Schedule Management
2. ระบุองค์ประกอบและกระบวนการสำคัญ
3. เชื่อมแนวคิดกับ 5 Process Groups
4. วิเคราะห์ผลกระทบต่อ Scope, Schedule, Cost, Quality, Risk และ Stakeholder
5. ประยุกต์ใช้กับ ERP Transformation
6. ประยุกต์ใช้กับ Hotel Booking Digital Platform
7. แยก Best Practice ออกจาก Process Theater
8. ระบุ Misconception และข้อควรระวัง
9. ใช้ Professional Judgement และ Tailoring
10. ประเมินความพร้อมของโครงการใน Knowledge Area นี้

## 5. Core Topics

1. Plan Schedule Management
2. Define Activities
3. Sequence Activities
4. Estimate Activity Durations
5. Develop Schedule
6. Control Schedule
7. Milestone
8. Dependency
9. Lead and Lag
10. Critical Path Method
11. Float
12. Analogous Estimating
13. Parametric Estimating
14. Three-point Estimating
15. Bottom-up Estimating
16. Schedule Compression
17. Rolling Wave Planning

## 6. ERP Teaching Focus

- วางลำดับ Process Design → Configuration → SIT → UAT → Cutover → Go-live
- วิเคราะห์ Critical Path ของ Development, SIT และ UAT
- ประเมินผลกระทบเมื่อ Data Migration Delay

## 7. Hotel Booking Teaching Focus

- วาง Dependency ระหว่าง UX, API, Mobile, Web, Payment, Inventory, Beta และ Launch
- ประเมิน Launch Date ที่ Marketing ประกาศ
- วิเคราะห์ Bottleneck ของ Backend และ Payment Integration

## 8. Narrative Flow

1. Opening Scenario
2. Why this Knowledge Area matters
3. Definition and purpose
4. Core Processes
5. Key Artifacts and Decisions
6. ERP Scenario
7. Hotel Booking Scenario
8. Cross-Knowledge Impacts
9. Common Misconceptions
10. PM Thinking
11. Reflection
12. Assessment
13. Bridge to the next lesson

## 9. Misconceptions to Correct

- ทำ Process ครบแล้วแปลว่าบริหารดี
- เอกสารคือเป้าหมาย
- PM ต้องทำงานแทนผู้เชี่ยวชาญ
- Knowledge Area นี้ทำงานแยกจากด้านอื่น
- Tool หรือ Template สามารถแทนการตัดสินใจ
- ทุกโครงการต้องใช้ Artifact ระดับเดียวกัน
- การ Tailor คือการตัดขั้นตอนที่ไม่อยากทำ
- Status Green ด้านเดียวแปลว่า Project Green ทั้งหมด

## 10. Boundaries

บทนี้ลงลึกเฉพาะ Project Schedule Management แต่กล่าวถึง Knowledge Areas อื่นเฉพาะเมื่อจำเป็นต่อการอธิบายผลกระทบข้ามด้าน

ไม่ขยายไปเป็น:

- คู่มือ Tool เฉพาะผลิตภัณฑ์
- Template ระดับองค์กรแบบสมบูรณ์
- ข้อกำหนดกฎหมายเฉพาะกรณีที่ไม่มีใน Canonical Source
- ข้อสรุปตายตัวที่ใช้กับทุก Project

## 11. Completion Criteria

บทถือว่าสมบูรณ์เมื่อ:

- ตอบ Opening Question ได้
- ครอบคลุม Core Topics
- มี ERP และ Hotel Booking
- อธิบาย Decision และ Trade-off
- เชื่อมกับ Outcome และ Business Value
- แก้ Misconception
- มี Assessment และ Source Mapping
- ไม่ขัดกับ Canonical Source

---

## 12. PM Decisions to Practise

| Decision | Owner | Inputs / missing information | Options and trade-off | Evidence / next action |
|---|---|---|---|---|
| Data migration delay กระทบ go-live จริงหรือไม่ | PM / Steering Committee | network logic, float, data quality, SIT/UAT progress; ยังไม่รู้ rework volume | recover within float; fast-track เพิ่ม risk; move go-live ลด defect risk แต่กระทบ fiscal deadline | updated network, recovery plan, approved baseline change |
| จะ lock Hotel launch date ก่อน payment test ผ่านหรือไม่ | Sponsor + Product Owner | payment reliability, High Season value, rollback/support readiness | hold date เพิ่ม marketing certainty แต่เสี่ยง failed booking; defer ลด risk แต่เสีย demand window | release criteria, risk acceptance, stakeholder message |
| จะ compress schedule อย่างไร | PM with delivery leads | critical path, resource availability, quality/risk impact | crashing เร็วแต่เพิ่ม cost; fast-tracking เร็วแต่เพิ่ม rework; de-scope รักษา date แต่ลด value | compression analysis, named risk owner, decision log |

## 13. Workshop and Assessment Design

**Workshop:** SIT ของ ERP เลื่อน 2 สัปดาห์. ผู้เรียนทำ network sketch จาก baseline ระบุ critical path/float ที่ต้องยืนยัน, information gaps, และเสนอ 3 recovery options พร้อมผลต่อ UAT, migration, quality และ budget. ประเมิน schedule logic 35%, uncertainty handling 25%, trade-off 25%, governance 15%.

**Assessment mix:** Critical-path decision case 40%; Artifact Review ของ Gantt ที่ไม่มี dependencies/baseline 30%; Trade-off case เรื่อง Hotel payment readiness 20%; estimation concept check 10%. ห้ามให้คำตอบจากวันที่อย่างเดียวโดยไม่แสดง logic.

## 14. Source Coverage and Handoff

| Coverage | Classification | Boundary |
|---|---|---|
| Activities, sequencing, estimating, develop/control schedule, CPM, float | `[PMBOK 6]` | ไม่สอนเครื่องมือ scheduling เฉพาะราย |
| Rolling wave, release criteria, recovery planning | `[Best Practice]` | ไม่รับประกัน schedule outcome |
| ERP/Hotel timeline | `[Teaching Scenario]` | Scenario Master v1.0 |
| ตัวเลือก compression ที่แนะนำ | `[Professional Opinion]` | ต้องอิง evidence ของโครงการ |

**Handoff to Lesson 09:** Schedule บอกเมื่อจะใช้ทรัพยากรและเงิน แต่ยังไม่บอกว่าค่าใช้จ่ายอยู่ใน baseline หรือมี performance เทียบแผนอย่างไร; Lesson 09 จึงต่อด้วย Cost Management และ Earned Value.

---
lesson: 8
sequence: 8.4
title: Project Schedule Management — Source Mapping
document_type: Source Mapping
difficulty: Core
estimated_study_time: 10
status: Active
validation_status: Validated
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 08 — Project Schedule Management
related_lessons:
  - Lesson 08 — Project Schedule Management
  - Lesson 09 — Project Cost Management and Earned Value
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 08_4 — Source Mapping

## 1. Canonical Source

บทนี้ยึดจาก:

> Knowledge Area 7: Project Schedule Management และ Critical Path Method

## 2. Source-Derived Topics

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

## 3. Teaching Enrichment

ส่วนต่อไปนี้เป็นการขยายเพื่อการสอน:

- Opening Question และ Scenario
- การเชื่อมกับ Business Need, Outcome, Benefit และ Value
- การแยก Fact, Assumption, Decision และ Action
- Cross-Knowledge Impact
- Process Theater
- Tailoring Guidance
- ERP Transformation Scenario
- Hotel Booking Digital Platform Scenario
- Reflection และ Applied Assessment

## 4. ERP Assumptions

- วางลำดับ Process Design → Configuration → SIT → UAT → Cutover → Go-live
- วิเคราะห์ Critical Path ของ Development, SIT และ UAT
- ประเมินผลกระทบเมื่อ Data Migration Delay

รายละเอียดเป็น Teaching Scenario ไม่ใช่ข้อเท็จจริงจากโครงการจริง

## 5. Hotel Booking Assumptions

- วาง Dependency ระหว่าง UX, API, Mobile, Web, Payment, Inventory, Beta และ Launch
- ประเมิน Launch Date ที่ Marketing ประกาศ
- วิเคราะห์ Bottleneck ของ Backend และ Payment Integration

ระบบสมมติประกอบด้วย Mobile App, Customer Web App, Landing Page, Back Office, Booking Engine, Payment, Inventory, Notification และ Reporting

## 6. Content Boundaries

- ไม่อ้างว่าทุกองค์กรต้องใช้ Artifact เหมือนกัน
- ไม่อ้างว่าสมมติฐานของ Scenario เป็นข้อเท็จจริง
- ไม่แทนที่ Policy, Contract, Law หรือ Standard เฉพาะองค์กร
- ไม่ขยาย Tool หรือ Template เฉพาะผลิตภัณฑ์
- ไม่ตัดสิน Approach โดยไม่มีบริบท

## 7. Quality Check

บทนี้ต้อง:

- รักษาความหมายของ Canonical Source
- แยก Source Fact กับ Teaching Enrichment
- มี ERP และ Hotel Booking
- แสดง Cross-Knowledge Impact
- เชื่อม Outcome และ Business Value
- มี Misconception Correction
- มี Assessment
- ระบุ Assumption อย่างชัดเจน

## 8. Repository Standard Source Labels

- **[PMBOK 6]** ใช้สำหรับ process, artifact, baseline, knowledge area และ governance vocabulary
- **[PMBOK 7]** ใช้สำหรับ value delivery, systems thinking, tailoring, adaptability และ stewardship
- **[Teaching Scenario]** ใช้สำหรับ ERP Transformation และ Hotel Booking Platform ที่มาจาก scenario master files
- **[Professional Opinion]** ใช้สำหรับ workshop, decision prompt, misconception correction, rubric และ Thai executive framing

## 9. Mapping Boundary and Continuation Notes

- บทนี้ต้องไม่อ้างว่า teaching scenario เป็นข้อเท็จจริงภายนอก
- บทนี้ต้องไม่แทนที่ policy, contract, law หรือ standard เฉพาะองค์กร
- การเพิ่มเนื้อหาใหม่ต้องรักษา distinction ระหว่าง canonical concept, scenario fact และ instructor interpretation
- Future AI agents must preserve the lesson-specific PM decision logic and keep scenario details aligned with the ERP and Hotel master scenario files

## Learning Asset Mapping

| Asset | Classification | Boundary |
|---|---|---|
| Activity/Network/Schedule Template | `[PMBOK 6]` / `[Best Practice]` | Schedule concepts; no vendor tool instruction |
| ERP/Hotel examples | `[Teaching Scenario]` | Scenario Master v1.0 |
| Walkthrough/Model Answer | `[Professional Opinion]` | Recovery guidance requires local evidence |
| Checklist/Rubric | `[Best Practice]` | Course acceptance standard |

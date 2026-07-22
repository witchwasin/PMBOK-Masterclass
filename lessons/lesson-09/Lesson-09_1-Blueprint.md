---
lesson: 9
sequence: 9.1
title: Project Cost Management and Earned Value
document_type: Blueprint
difficulty: Core
estimated_study_time: 15
status: Active
validation_status: Validated
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 08 — Project Schedule Management
related_lessons:
  - Lesson 08 — Project Schedule Management
  - Lesson 09 — Project Cost Management and Earned Value
  - Lesson 10 — Project Quality Management
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
artifact_inputs:
  - ../lesson-07/learner/Artifact-Template.md — WBS and WBS Dictionary
  - ../lesson-08/learner/Artifact-Template.md — Master Schedule
artifact_outputs:
  - name: Cost Estimate, Cost Baseline and Cost Performance Forecast
    creator: Cost Controller and Project Manager
    artifact_owner: Project Manager
    reviewer: Finance, Workstream Leads and Vendor Commercial Lead
    approval_authority: Sponsor or Steering Committee
    approval_evidence: Approved Cost Baseline and financial decision record
next_lesson_usage:
  - Lesson 10 ใช้ cost constraints, work packages และ schedule gates เพื่อวาง prevention, testing และ acceptance effort
acceptance_level:
  incomplete: ปน Working Budget, Funding Envelope, reserve, actual และ forecast หรือไม่ trace WBS/schedule
  usable: estimate basis, time-phased baseline, reserves, actual, EAC และ variance แยกได้
  professional: มี assumptions, confidence, EVM interpretation, forecast options และ approval evidence
---

# Lesson 09_1 — Blueprint: Project Cost Management and Earned Value

## 1. Purpose

บทนี้ทำหน้าที่พาผู้เรียนจากภาพรวมในบทก่อนหน้าเข้าสู่ความเข้าใจเชิงลึกของ **Project Cost Management and Earned Value** โดยยังคงแนวทางการสอนแบบ:

- เริ่มจากคำถามและสถานการณ์
- อธิบายเหตุผลก่อน Definition
- เชื่อม Framework กับ Decision จริง
- ใช้ ERP Transformation และ Hotel Booking Digital Platform
- แก้ความเข้าใจผิด
- ปิดด้วย Reflection และ Assessment

## 2. Opening Question

> ใช้งบน้อยกว่าแผน แปลว่าโครงการมีสุขภาพดีเสมอหรือไม่?

## 3. Core Teaching Message

> **Cost Management ต้องเชื่อมเงินที่ใช้กับมูลค่างานที่ทำสำเร็จ ไม่ใช่ดูยอดใช้จ่ายเพียงอย่างเดียว**

## 4. Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบายวัตถุประสงค์ของ Project Cost Management and Earned Value
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

1. Plan Cost Management
2. Estimate Costs
3. Determine Budget
4. Control Costs
5. Cost Baseline
6. Management Reserve
7. Contingency Reserve
8. Planned Value (PV)
9. Earned Value (EV)
10. Actual Cost (AC)
11. Schedule Variance (SV)
12. Cost Variance (CV)
13. Schedule Performance Index (SPI)
14. Cost Performance Index (CPI)
15. Forecasting
16. Estimate at Completion
17. Cost of Change

## 6. ERP Teaching Focus

- ต้นทุน License, Vendor, Infrastructure, Data Migration, Training และ Support
- วิเคราะห์กรณีใช้งบน้อยเพราะ UAT ยังไม่เริ่ม
- ใช้ CPI/SPI วิเคราะห์สุขภาพโครงการ

## 7. Hotel Booking Teaching Focus

- ต้นทุน Development, Cloud, Payment Fee, Marketing, Security และ Operation
- วิเคราะห์ Feature เพิ่มที่กระทบทั้ง Build Cost และ Run Cost
- ประเมิน Cost ต่อ Booking และ Cost of Delay

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

บทนี้ลงลึกเฉพาะ Project Cost Management and Earned Value แต่กล่าวถึง Knowledge Areas อื่นเฉพาะเมื่อจำเป็นต่อการอธิบายผลกระทบข้ามด้าน

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

## 12. Learner State, Decision, Practice, and Sources

**Learner state:** ใช้ Lesson 07–08 เพื่ออ่าน WBS/schedule ได้ แต่ยังไม่แยก budget, forecast และ performance. **Decision:** CFO จะอนุมัติ ERP change 2 ล้านบาทหรือไม่; owner คือ Steering Committee; inputs คือ cost baseline, EAC, benefit และ contingency ที่เหลือ; options คือ approve/defer/de-scope พร้อมผลต่อ go-live และ value; evidence คือ change log กับ updated forecast. **Workshop:** วิเคราะห์ ERP CPI/SPI ที่ต่ำกว่า 1 และเขียน executive brief ที่ไม่สรุปจากตัวเลขเดียว. **Assessment:** EVM interpretation 40%, cost-report artifact review 30%, trade-off 20%, recall 10%. **Sources:** cost processes/EVM `[PMBOK 6]`; forecasting `[Best Practice]`; scenario figures `[Teaching Scenario]`; recommendation `[Professional Opinion]`.

**Handoff:** เมื่อรู้ผลของเงินและ performance แล้ว Lesson 10 ถามต่อว่า “ส่งมอบตามงบ” มีความหมายหรือไม่หากคุณภาพไม่ตอบ acceptance.

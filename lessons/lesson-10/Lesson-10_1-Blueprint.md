---
lesson: 10
sequence: 10.1
title: Project Quality Management
document_type: Blueprint
difficulty: Core
estimated_study_time: 15
status: Active
validation_status: Validated
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 09 — Project Cost Management and Earned Value
related_lessons:
  - Lesson 09 — Project Cost Management and Earned Value
  - Lesson 10 — Project Quality Management
  - Lesson 11 — Project Resource Management
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
artifact_inputs:
  - ../lesson-07/learner/Artifact-Template.md — Scope, WBS and Acceptance Inputs
  - ../lesson-08/learner/Artifact-Template.md — Master Schedule and Quality Gates
  - ../lesson-09/learner/Artifact-Template.md — Cost Baseline and Quality Budget Constraints
artifact_outputs:
  - name: Quality Plan, Acceptance Criteria and Test Strategy
    creator: Quality Lead, Business Analyst and Project Manager
    artifact_owner: Quality Manager and Project Manager
    reviewer: Business Owners, IT Operations and System Integrator
    approval_authority: Business Owner
    approval_evidence: Approved quality/test strategy and signed acceptance criteria
next_lesson_usage:
  - Lesson 11 ใช้ quality roles, test workload และ approval responsibilities เพื่อสร้าง Resource Plan และ RACI
acceptance_level:
  incomplete: เท่ากับ quality กับไม่มี defect หรือไม่มี owner, criteria, coverage และ evidence
  usable: quality objective, prevention, QA/QC, acceptance, test levels, severity และ sign-off ครบ
  professional: trace requirement-to-test-to-acceptance, residual risk, go/no-go threshold และ operating handoff ได้
---

# Lesson 10_1 — Blueprint: Project Quality Management

## 1. Purpose

บทนี้ทำหน้าที่พาผู้เรียนจากภาพรวมในบทก่อนหน้าเข้าสู่ความเข้าใจเชิงลึกของ **Project Quality Management** โดยยังคงแนวทางการสอนแบบ:

- เริ่มจากคำถามและสถานการณ์
- อธิบายเหตุผลก่อน Definition
- เชื่อม Framework กับ Decision จริง
- ใช้ ERP Transformation และ Hotel Booking Digital Platform
- แก้ความเข้าใจผิด
- ปิดด้วย Reflection และ Assessment

## 2. Opening Question

> ระบบไม่มี Bug แปลว่าระบบมีคุณภาพแล้วหรือไม่?

## 3. Core Teaching Message

> **Quality ต้องถูกออกแบบเข้าไปใน Deliverable ตั้งแต่ต้น และต้องวัดทั้งความถูกต้อง ความเหมาะสม และความพร้อมต่อการใช้งานจริง**

## 4. Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบายวัตถุประสงค์ของ Project Quality Management
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

1. Plan Quality Management
2. Manage Quality
3. Control Quality
4. Quality vs Grade
5. Verification vs Validation
6. V-Model
7. SIT
8. UAT
9. Performance Test
10. Security Test
11. ISO 25010
12. Functional Suitability
13. Performance Efficiency
14. Compatibility
15. Usability
16. Reliability
17. Security
18. Maintainability
19. Portability
20. Defect Severity
21. Defect Priority
22. Prevention vs Inspection

## 6. ERP Teaching Focus

- Data Accuracy, Process Compliance, Integration, Performance และ Security
- แยก SIT กับ UAT
- ใช้ Severity/Priority จัดการ Defect ก่อน Go-live

## 7. Hotel Booking Teaching Focus

- Booking Accuracy, Payment Reliability, Inventory Consistency, UX, Performance และ Security
- วิเคราะห์ App ที่ไม่ล่มแต่ Conversion ต่ำ
- ทดสอบ Failure Recovery ของ Payment และ Booking Confirmation

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

บทนี้ลงลึกเฉพาะ Project Quality Management แต่กล่าวถึง Knowledge Areas อื่นเฉพาะเมื่อจำเป็นต่อการอธิบายผลกระทบข้ามด้าน

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

**Learner state:** เข้าใจ scope/schedule/cost แล้ว แต่ยังเท่ากับ “ไม่มี defect” กับ quality. **Decision:** จะเลื่อน ERP go-live เพราะ UAT defects หรือ accept residual risk; owner คือ sponsor/business owner; inputs คือ acceptance criteria, defect severity, user readiness และ cost of delay; options คือ fix/defer/go-live with mitigation; evidence คือ quality report และ risk acceptance. **Workshop:** review UAT dashboard ที่สีเขียวแต่ไม่มี coverage/acceptance evidence. **Assessment:** Artifact Review 40%, ambiguous release decision 30%, prevention-versus-inspection trade-off 20%, recall 10%. **Sources:** quality processes `[PMBOK 6]`; prevention/metrics `[Best Practice]`; scenarios `[Teaching Scenario]`; recommendation `[Professional Opinion]`.

**Handoff:** คุณภาพต้องมีคนและ capacity ที่ทำให้เกิดจริง จึงต่อ Lesson 11 เรื่อง resource responsibility และ team performance.

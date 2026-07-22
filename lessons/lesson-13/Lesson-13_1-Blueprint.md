---
lesson: 13
sequence: 13.1
title: Project Risk Management
document_type: Blueprint
difficulty: Core
estimated_study_time: 30
status: Active
validation_status: Validated
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 12 — Project Communications Management
related_lessons:
  - Lesson 14 — Project Procurement Management
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
artifact_inputs:
  - Communication plan, status report and escalation path from Lesson 12
artifact_outputs:
  - name: Risk Register, Response Plan and Issue Log
    creator: PM, Risk Owners and Issue Owners
    artifact_owner: PM
    reviewer: Risk Owners and Issue Owners
    approval_authority: PM within delegated threshold; Steering Committee for appetite, threshold, high/critical responses and excess contingency
    approval_evidence: Risk acceptance, review minutes, escalation record and Change Request ID
next_lesson_usage:
  - Risk allocation and change evidence inform procurement and vendor control.
acceptance_level:
  incomplete: Risks have no owner, trigger or response.
  usable: Risk-to-issue escalation and approved responses can be followed.
  professional: Thresholds, reserves, change control and governance evidence are decision-ready.
---

# Lesson 13_1 — Blueprint: Project Risk Management

## 1. Purpose

บทนี้ทำหน้าที่พาผู้เรียนจากภาพรวมในบทก่อนหน้าเข้าสู่ความเข้าใจเชิงลึกของ **Project Risk Management** โดยยังคงแนวทางการสอนแบบ:

- เริ่มจากคำถามและสถานการณ์
- อธิบายเหตุผลก่อน Definition
- เชื่อม Framework กับ Decision จริง
- ใช้ ERP Transformation และ Hotel Booking Digital Platform
- แก้ความเข้าใจผิด
- ปิดด้วย Reflection และ Assessment

## 2. Opening Question

> ความเสี่ยงที่มีโอกาสเกิดต่ำ ควรถูกละเลยหรือไม่?

## 3. Core Teaching Message

> **Risk Management คือการตัดสินใจล่วงหน้าภายใต้ความไม่แน่นอน ไม่ใช่การรอให้ปัญหาเกิดแล้วจึงบันทึก**

## 4. Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบายวัตถุประสงค์ของ Project Risk Management
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

1. Plan Risk Management
2. Identify Risks
3. Qualitative Risk Analysis
4. Quantitative Risk Analysis
5. Plan Risk Responses
6. Implement Risk Responses
7. Monitor Risks
8. Risk vs Issue
9. Probability
10. Impact
11. Risk Exposure
12. Risk Owner
13. Avoid
14. Mitigate
15. Transfer
16. Accept
17. Contingency
18. Trigger
19. Residual Risk
20. Secondary Risk
21. Opportunity Risk
22. Risk Appetite

## 6. ERP Teaching Focus

- Data Migration, User Adoption, Cutover, Vendor Resource และ Integration
- สร้าง Trigger สำหรับ Go-live Readiness
- วาง Contingency และ Rollback Plan

## 7. Hotel Booking Teaching Focus

- Payment Failure, Inventory Sync, Security Incident, Conversion ต่ำ และ Partner Adoption
- วิเคราะห์ Low Probability–High Impact Security Risk
- วาง Response สำหรับ Cloud Outage และ Overbooking

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

บทนี้ลงลึกเฉพาะ Project Risk Management แต่กล่าวถึง Knowledge Areas อื่นเฉพาะเมื่อจำเป็นต่อการอธิบายผลกระทบข้ามด้าน

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

**Learner state:** เห็น issue แล้วแต่ยังไม่แยก risk, issue, assumption และ trigger. **Decision:** จะตอบสนองต่อ data-migration quality risk อย่างไร; owner คือ PM กับ data owner; inputs คือ likelihood, impact, trigger, reserve และ deadline; options คือ cleanse early/add specialists/accept risk; evidence คือ risk register, response owner และ trigger review. **Workshop:** review risk register ที่มีแต่คำว่า “ทีมไม่พร้อม” แล้วทำให้เป็น actionable risks. **Assessment:** Risk-register artifact review 40%, ambiguous response case 30%, reserve trade-off 20%, recall 10%. **Sources:** risk processes `[PMBOK 6]`; trigger/early-warning practice `[Best Practice]`; scenarios `[Teaching Scenario]`; advice `[Professional Opinion]`.

**Handoff:** Risk response บางอย่างต้องซื้อ expertise หรือ transfer responsibility; Lesson 14 จึงต่อด้วย make-or-buy, contract และ vendor governance.

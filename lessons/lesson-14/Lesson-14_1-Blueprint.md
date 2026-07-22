---
lesson: 14
sequence: 14.1
title: Project Procurement Management
document_type: Blueprint
difficulty: Core
estimated_study_time: 30
status: Active
validation_status: Validated
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 13 — Project Risk Management
related_lessons:
  - Lesson 15 — Agile Project Management
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
artifact_inputs:
  - Risk register, issue log and approved change requests from Lesson 13
artifact_outputs:
  - name: Procurement Plan, Vendor Evaluation and Contract Control Record
    creator: PM, Procurement Manager and Commercial Lead
    artifact_owner: Procurement Manager for commercial artifacts; PM for delivery and acceptance linkage
    reviewer: Legal, Finance, IT and Business Owners
    approval_authority: Procurement Authority or Sponsor according to financial authority
    approval_evidence: Sourcing decision, contract approval, vendor acceptance and payment authorization
next_lesson_usage:
  - Contract constraints and acceptance evidence shape iterative delivery choices.
acceptance_level:
  incomplete: Scope, acceptance or commercial owner is unclear.
  usable: Supplier selection, contract control and acceptance evidence are connected.
  professional: Commercial risk, change and payment controls support a defensible decision.
---

# Lesson 14_1 — Blueprint: Project Procurement Management

## 1. Purpose

บทนี้ทำหน้าที่พาผู้เรียนจากภาพรวมในบทก่อนหน้าเข้าสู่ความเข้าใจเชิงลึกของ **Project Procurement Management** โดยยังคงแนวทางการสอนแบบ:

- เริ่มจากคำถามและสถานการณ์
- อธิบายเหตุผลก่อน Definition
- เชื่อม Framework กับ Decision จริง
- ใช้ ERP Transformation และ Hotel Booking Digital Platform
- แก้ความเข้าใจผิด
- ปิดด้วย Reflection และ Assessment

## 2. Opening Question

> Vendor ส่งมอบตามสัญญาครบ แปลว่า Project ได้สิ่งที่ธุรกิจต้องการแล้วหรือไม่?

## 3. Core Teaching Message

> **Procurement Management ต้องเชื่อม Contract Deliverable กับ Project Outcome ไม่ใช่หยุดที่การซื้อหรือการเซ็นรับ**

## 4. Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบายวัตถุประสงค์ของ Project Procurement Management
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

1. Plan Procurement Management
2. Conduct Procurements
3. Control Procurements
4. Make-or-Buy Analysis
5. TOR / Scope of Work
6. Vendor Selection
7. Contract Types
8. Milestone Payment
9. Acceptance Criteria
10. SLA
11. Vendor Performance
12. Change and Claim
13. Contract Closure
14. Procurement Governance
15. Public Procurement Overview
16. Commercial Risk

## 6. ERP Teaching Focus

- ERP License, System Integrator, Infrastructure, Migration Vendor และ Maintenance
- เชื่อม Milestone Payment กับ Acceptance
- จัดการ Change Request ที่กระทบ Contract

## 7. Hotel Booking Teaching Focus

- Payment Gateway, Cloud, SMS/Email, External Developer, Map API และ Hotel Partner
- วิเคราะห์ Make-or-Buy ของ Booking Engine
- กำหนด SLA สำหรับ Payment และ Notification

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

บทนี้ลงลึกเฉพาะ Project Procurement Management แต่กล่าวถึง Knowledge Areas อื่นเฉพาะเมื่อจำเป็นต่อการอธิบายผลกระทบข้ามด้าน

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

**Learner state:** เข้าใจ vendor เป็นผู้ส่งงาน แต่ยังไม่อ่าน risk allocation และ acceptance ใน contract. **Decision:** จะใช้ fixed-price หรือ T&M สำหรับ ERP customization; owner คือ procurement authority/sponsor; inputs คือ scope maturity, uncertainty, supplier capability, budget tolerance; options คือ fixed/T&M/hybrid; evidence คือ statement of work, acceptance criteria, contract decision. **Workshop:** review change request ของ SI ที่ไม่มี scope boundary และ rate/card impact. **Assessment:** Contract-artifact review 40%, make-or-buy trade-off 30%, supplier-risk case 20%, recall 10%. **Sources:** procurement processes `[PMBOK 6]`; commercial practice `[Enterprise Practice]`; scenarios `[Teaching Scenario]`; advice `[Professional Opinion]`.

**Handoff:** Procurement works differently when delivery is iterative; Lesson 15 introduces Agile mindset, Scrum, and Kanban without claiming one method fits all.

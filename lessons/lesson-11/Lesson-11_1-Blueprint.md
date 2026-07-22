---
lesson: 11
sequence: 11.1
title: Project Resource Management
document_type: Blueprint
difficulty: Core
estimated_study_time: 25
status: Active
validation_status: Validated
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 10 — Project Quality Management
related_lessons:
  - Lesson 12 — Project Communications Management
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
artifact_inputs:
  - Quality and acceptance evidence from Lesson 10
artifact_outputs:
  - name: Consolidated Resource Plan, Organization Chart and RACI
    creator: PM, Resource Manager and Workstream Leads
    artifact_owner: PM
    reviewer: Functional Managers, HR and SI/Vendor Lead
    approval_authority: PM for the consolidated plan; Functional Managers for capacity and resource commitment; Steering Committee for exceptions only
    approval_evidence: Approved resource commitment, RACI sign-off and escalation decision
next_lesson_usage:
  - Communication audiences, accountable roles and escalation path are derived from the approved RACI
acceptance_level:
  incomplete: Roles or capacity commitments are missing or unowned.
  usable: Roles, assignments, capacity and approval evidence are sufficient for execution.
  professional: Conflicts, contingencies and escalation thresholds are explicit and decision-ready.
---

# Lesson 11_1 — Blueprint: Project Resource Management

## 1. Purpose

บทนี้ทำหน้าที่พาผู้เรียนจากภาพรวมในบทก่อนหน้าเข้าสู่ความเข้าใจเชิงลึกของ **Project Resource Management** โดยยังคงแนวทางการสอนแบบ:

- เริ่มจากคำถามและสถานการณ์
- อธิบายเหตุผลก่อน Definition
- เชื่อม Framework กับ Decision จริง
- ใช้ ERP Transformation และ Hotel Booking Digital Platform
- แก้ความเข้าใจผิด
- ปิดด้วย Reflection และ Assessment

## 2. Opening Question

> คนเก่งที่สุด ควรเป็น Owner ของงานสำคัญที่สุดเสมอหรือไม่?

## 3. Core Teaching Message

> **Resource Management คือการทำให้บทบาท ความรับผิดชอบ Capacity และ Team Dynamics เหมาะกับสิ่งที่โครงการต้องส่งมอบ**

## 4. Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบายวัตถุประสงค์ของ Project Resource Management
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

1. Plan Resource Management
2. Estimate Activity Resources
3. Acquire Resources
4. Develop Team
5. Manage Team
6. Control Resources
7. Organization Chart
8. RACI
9. Role Clarity
10. Capacity
11. Shared Resources
12. Team Development
13. Motivation
14. Conflict Management
15. Accountability
16. Resource Calendar

## 6. ERP Teaching Focus

- PM, Process Owner, Key User, BA, Data Team, Technical Team, Tester, Vendor และ Support
- แก้ Key User ถูกดึงกลับไปทำงานประจำ
- ใช้ RACI กำหนด Data Ownership และ Acceptance

## 7. Hotel Booking Teaching Focus

- Product, UX, Mobile, Web, Backend, QA, DevOps, Marketing, Hotel Operation และ Support
- จัดการ Backend Bottleneck
- วาง Capacity ระหว่าง MVP, Launch และ Post-launch Support

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

บทนี้ลงลึกเฉพาะ Project Resource Management แต่กล่าวถึง Knowledge Areas อื่นเฉพาะเมื่อจำเป็นต่อการอธิบายผลกระทบข้ามด้าน

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

**Learner state:** รู้แผนงาน แต่ยังคิดว่าการ assign คนเท่ากับมี capacity. **Decision:** จะย้าย ERP key user ออกจาก BAU เพื่อ UAT หรือปรับ schedule/scope; owner คือ functional manager กับ sponsor; inputs คือ UAT load, production impact, skill gap และ backfill; options คือ dedicate/part-time/backfill/defer; evidence คือ resource commitment และ updated schedule. **Workshop:** สร้าง capacity decision brief จาก key users 80 คนที่ทำงานคู่ขนาน. **Assessment:** resource-plan artifact review 35%, trade-off 35%, conflict/leadership case 20%, recall 10%. **Sources:** resource processes `[PMBOK 6]`; capacity/team practice `[Best Practice]`; scenarios `[Teaching Scenario]`; advice `[Professional Opinion]`.

**Handoff:** เมื่อ roles และ capacity ชัด ผู้เรียนจึงต้องกำหนดว่าใครควรได้รับข้อมูลใด เมื่อใด และอย่างไรใน Lesson 12.

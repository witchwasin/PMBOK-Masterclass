---
lesson: 3
sequence: 3.1
title: 5 Project Management Process Groups
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
related_lessons:
  - Lesson 02 — Project Management Overview
  - Lesson 03 — 5 Project Management Process Groups
  - Lesson 04 — 10 Project Management Knowledge Areas Overview
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
artifact_inputs:
  - ../lesson-02/learner/Artifact-Template.md — Project vs Operation Analysis and Value Chain
artifact_outputs:
  - name: Lifecycle and Process Group Map
    creator: Learner in Project Planner role
    artifact_owner: Project Manager
    reviewer: PMO and Workstream Leads
    approval_authority: Project Manager with Sponsor acknowledgement
    approval_evidence: Reviewed lifecycle map and recorded governance acknowledgement
next_lesson_usage:
  - Lesson 04 ใช้ management activities, decision gates และ feedback loops เพื่อทำ PM Coverage and Cross-impact Map
acceptance_level:
  incomplete: เรียง Process Groups เป็น phase ตายตัวหรือไม่มี feedback/replanning
  usable: แยก phase จาก Process Group และระบุ decisions, evidence และ feedback loops ได้
  professional: เชื่อม lifecycle, governance gates, monitoring signals, closing evidence และ transition อย่างตรวจสอบได้
---

# Lesson 03_1 — Blueprint: 5 Project Management Process Groups

## 0. Learner Profile and Prerequisites

- **Learner profile:** ผู้เรียนที่แยก Project จาก Operation ได้แล้ว แต่เสี่ยงเข้าใจ Process Groups เป็นเส้นตรงหรือเป็น phase ของทุกโครงการ
- **Required prerequisite:** Lesson 01–02; รู้ value chain และความต่างระหว่าง output กับ outcome
- **Entry evidence:** อธิบายได้ว่าเหตุใดงานที่เริ่ม execution แล้วอาจต้องกลับไป planning
- **Scenario state:** ERP อยู่ช่วง initiation/planning; Hotel Booking อยู่ช่วง discovery และ backlog shaping. เหตุการณ์ตัวอย่างต้องไม่ข้าม baseline นี้

## 1. Purpose

Lesson 03 มีหน้าที่ทำให้ผู้เรียนเข้าใจ “การไหลของการบริหารโครงการ” ตั้งแต่การเริ่มต้นไปจนถึงการปิดโครงการ

หัวใจของบทนี้ไม่ใช่การท่องจำชื่อ 5 Process Groups แต่คือการเข้าใจว่า:

- แต่ละกลุ่มกระบวนการมีหน้าที่อะไร
- ทำไม Planning ไม่ได้เกิดครั้งเดียว
- ทำไม Monitoring & Controlling เกิดคู่กับ Executing
- ทำไม Closing ไม่ใช่แค่จัดเอกสาร
- ทำไม Process Groups ไม่ควรถูกตีความเป็น Phase แบบตายตัว
- Project Manager ต้องเชื่อม Decision, Work, Feedback และ Change อย่างไร

---

## 2. Opening Question

> ถ้าโครงการเริ่มทำงานจริงไปแล้ว แต่ยังพบว่าขอบเขตไม่ชัด เราควรกลับไป Planning หรือเดินหน้าต่อ?

คำถามนี้ใช้เปิดบท เพื่อทำลายความเข้าใจผิดว่า Process Groups เป็นเส้นตรงที่ผ่านแล้วห้ามย้อนกลับ

---

## 3. Core Teaching Message

> **Process Groups ไม่ใช่บันไดที่เดินขึ้นทีละขั้นแล้วห้ามย้อนกลับ แต่เป็นวงจรบริหารที่ทำงานร่วมกันตลอดโครงการ**

---

## 4. Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบาย 5 Process Groups ได้
2. แยก Initiating, Planning, Executing, Monitoring & Controlling และ Closing
3. อธิบาย Output สำคัญของแต่ละกลุ่มกระบวนการ
4. อธิบายเหตุผลที่ Planning ต้องเกิดซ้ำ
5. อธิบายความสัมพันธ์ระหว่าง Executing กับ Monitoring & Controlling
6. แยก Process Groups ออกจาก Project Phases
7. วิเคราะห์ Project Flow ด้วยกรณี ERP
8. วิเคราะห์ Product/Platform Flow ด้วยกรณี Hotel Booking
9. ระบุความเข้าใจผิดที่พบบ่อย
10. เตรียมพร้อมเข้าสู่ 10 Knowledge Areas

---

## 5. Narrative Flow

1. ทบทวนจาก Lesson 02
2. Project มีการไหลอย่างไร
3. Process Groups คืออะไร
4. Initiating
5. Planning
6. Executing
7. Monitoring & Controlling
8. Closing
9. Process Groups ไม่เท่ากับ Phases
10. วงจร Iteration และ Feedback
11. ERP Case Flow
12. Hotel Booking Case Flow
13. Common Misconceptions
14. PM Thinking
15. Reflection
16. Bridge to Lesson 04

---

## 6. Core Flow

```text
Initiating
    ↓
Planning
    ↓
Executing
    ↔
Monitoring & Controlling
    ↓
Closing
```

แต่ในทางปฏิบัติ:

```text
Initiating
    ↓
Planning
    ↓
Executing ↔ Monitoring & Controlling
      ↑              ↓
      └──── Replanning ┘
    ↓
Closing
```

---

## 7. Core Scenario A — ERP Transformation

### ใช้เพื่อสอน

- Business Case to Charter
- Stakeholder identification
- Integrated planning
- Vendor and internal team execution
- Data migration and testing
- Change request
- Go-live readiness
- Handover and lessons learned

### Key Questions

- ใครอนุมัติโครงการ?
- Charter มีไว้ทำอะไร?
- Planning ต้องครอบคลุมอะไร?
- ระหว่าง SIT/UAT พบปัญหาควรจัดการอย่างไร?
- Change Request เกิดเมื่อใด?
- Go-live พร้อมจริงหรือไม่?
- Closing ต้องส่งต่ออะไรให้ Operation?

---

## 8. Core Scenario B — Hotel Booking Digital Platform

### ใช้เพื่อสอน

- Product vision and project authorization
- MVP planning
- UX, Mobile, Web, Back Office coordination
- Sprint/iteration execution
- Funnel and quality monitoring
- Scope and priority change
- Launch readiness
- Post-launch stabilization and handover

### Key Questions

- MVP ถูกอนุมัติด้วยเป้าหมายอะไร?
- Planning แบบ Agile ยังต้องมีหรือไม่?
- Conversion ต่ำระหว่าง Beta ควรอยู่ใน Process Group ใด?
- Payment Issue เป็น Execution หรือ Monitoring?
- Feature ใหม่ควรเข้าผ่าน Change Decision อย่างไร?
- Launch แล้วถือว่า Closing หรือไม่?

---

## 9. Misconceptions to Correct

- 5 Process Groups คือ 5 Phases เสมอ
- Planning ทำครั้งเดียวก่อนเริ่ม
- Monitoring คือการทำ Report
- Controlling คือการควบคุมคน
- Closing คือเซ็นรับงาน
- Executing คือทีม Technical ทำงานเท่านั้น
- Initiating คือ Kickoff Meeting
- Agile ไม่มี Planning หรือ Closing
- Change ทุกอย่างคือปัญหา
- เมื่อโครงการเริ่มแล้ว Charter ไม่มีประโยชน์

---

## 10. Boundaries

บทนี้ไม่ลงลึก:

- รายละเอียดราย Process ทั้ง 49/กลุ่มตามแต่ละ Edition
- 10 Knowledge Areas แบบรายบท
- Project Charter Template แบบเต็ม
- WBS
- Schedule Network
- EVM
- Risk Quantitative Analysis
- Procurement Law
- Scrum Event รายละเอียด
- Kanban Metrics

---

## 11. Completion Criteria

Lesson 03 ถือว่าสมบูรณ์เมื่อ:

- ผู้เรียนเข้าใจ 5 Process Groups แบบไม่ท่องจำ
- อธิบาย Output สำคัญของแต่ละกลุ่มได้
- เข้าใจ Iteration และ Replanning
- แยก Process Groups ออกจาก Phases
- มี ERP และ Hotel Booking เป็นตัวอย่างครบ
- มี Misconception Correction
- มี Assessment และ Scenario Analysis
- เชื่อมไป 10 Knowledge Areas ได้

---

## 12. PM Decisions to Practise

| Decision | Owner | Inputs / missing information | Options and trade-off | Evidence / next action |
|---|---|---|---|---|
| พร้อมออกจาก Initiating ไป Planning หรือยัง | Sponsor ร่วมกับ PM | business case, sponsor authority, high-level scope, success measures; ยังไม่รู้ key-user capacity | เริ่มเร็วช่วย deadline แต่เสี่ยง charter คลุมเครือ; รอข้อมูลเพิ่มลด rework แต่เสี่ยง delay | approved charter, named sponsor, planning mandate |
| พบ requirement ใหม่ระหว่าง Executing ต้องทำอย่างไร | Change authority ตาม governance | baseline, impact scope/schedule/cost/risk, urgency; ยังไม่รู้ benefit และ acceptance criteria | ทำทันทีเร็วแต่เสี่ยง scope creep; defer ปลอดภัยแต่กระทบ value; submit change เพื่อมี traceability | change log, impact analysis, recorded decision |
| ปิด phase ได้หรือไม่ | Sponsor / business owner | acceptance evidence, open defects, handover readiness, benefit owner | ปิดตรงเวลาแต่ส่งความเสี่ยงให้ operation; ขยาย hypercare ลด risk แต่ใช้ budget/capacity | acceptance record, transition checklist, lessons learned |

## 13. Workshop Design

**Scenario:** ERP พบว่า key users ยังไม่ยืนยัน master-data ownership แต่ SI ขอเริ่ม build เพื่อรักษา timeline ก่อน 1 ตุลาคม.
**Role:** PM คุณเอกเสนอทางเลือกต่อ Steering Committee.
**Available information:** total timeline 12 เดือน, SI contract, 5 modules, 80 key users ทำงานคู่ขนาน.
**Missing information:** data quality baseline, cost of rework, decision authority ของแต่ละ data domain.
**Decision:** ดำเนิน build, กลับไป planning เฉพาะ data workstream, หรือ change baseline.
**Constraint:** ห้ามเรียก Process Group ว่า phase; ต้องแสดงงานที่ยังเดินคู่ขนาน.
**Expected output:** one-page decision record และ process map ที่ชี้ feedback loop.
**Debrief:** ข้อมูลใดทำให้ “เริ่มงาน” ต่างจาก “พร้อมเริ่มงาน”?
**Evaluation:** logic ของ flow (25%), missing information (25%), trade-off (30%), governance/evidence (20%).

## 14. Assessment Design

- **Ambiguous decision case (40%):** Hotel Booking พบ PCI/payment integration uncertainty กลาง sprint; ระบุ process-group activities ที่ต้องเกิดพร้อมกันและสิ่งที่ต้อง escalate.
- **Artifact review (30%):** Review charter ที่ไม่มี success measure, sponsor authority หรือ transition owner แล้วระบุว่าขาดอะไรเพื่อออกจาก Initiating.
- **Trade-off (20%):** เปรียบเทียบ fast-track testing กับเลื่อน launch โดยวิเคราะห์คุณภาพ ความเสี่ยง และ business value.
- **Retrieval check (10%):** แยก Process Group ออกจาก Project Phase ด้วยตัวอย่าง.

## 15. Source Coverage and Lesson Handoff

| Coverage | Source classification | Boundary |
|---|---|---|
| Five Process Groups, progressive elaboration, change control, closing | `[PMBOK 6]` | ไม่สอน 49 processes หรือ template ราย knowledge area |
| Iteration, feedback loop, transition readiness | `[Best Practice]` | ไม่บอกว่าทุก project ต้องใช้ flow เดียวกัน |
| ERP and Hotel circumstances | `[Teaching Scenario]` | ใช้ Scenario Master v1.0 เท่านั้น |
| ข้อแนะนำว่าต้องมี decision evidence | `[Professional Opinion]` | ไม่อ้างเป็น mandatory PMBOK artifact |

**Handoff to Lesson 04:** Process Groups บอกลักษณะกิจกรรมตามเวลา แต่ยังไม่บอกว่าจะต้องบริหารเรื่องใดบ้าง; Lesson 04 จึงสร้างแผนที่ Knowledge Areas และความเชื่อมโยงระหว่างกัน.

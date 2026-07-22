---
chapter: lesson-15
title: Agile Project Management - Scrum and Kanban
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-15/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 15 — Agile Project Management: Scrum and Kanban

## 1. Opening Scenario

Hotel Booking มี payment risk ที่กระทบ MVP checkout ขณะเดียวกัน marketing ขอ promotion feature เพิ่มเข้ามาก่อน launch ถ้า team รับทุกอย่างเข้า sprint โดยไม่ปกป้อง sprint goal สิ่งที่สำคัญที่สุดต่อการจองและชำระเงินอาจไม่เสถียรพอ

ทีมอาจบอกว่า "เรา Agile อยู่แล้ว เปลี่ยนได้ตลอด" แต่ Agile ไม่ได้แปลว่าเปลี่ยนทุกอย่างโดยไม่มีวินัย Agile ที่ดีต้องมี priority, feedback, Definition of Done และความรับผิดชอบที่ชัดเจน

บทนี้จึงสอน Agile ในฐานะวิธีทำงานที่เรียนรู้เร็วขึ้น ไม่ใช่ข้ออ้างในการเลิกวางแผน

## 2. Why This Matters

โลกของ project ไม่ได้มีแต่ predictive plan ที่นิ่งตั้งแต่ต้น บางงานต้องเรียนรู้จากผู้ใช้จริง ทดลอง release สั้น ๆ และปรับ backlog ตาม evidence

แต่การทำ Agile แบบมีแต่พิธีกรรม เช่น standup, sprint และ board โดยไม่มี product ownership, feedback หรือ delivery discipline จะกลายเป็น Agile theater คือดูเหมือน Agile แต่ไม่ช่วยส่ง value

PM มืออาชีพจึงต้องเข้าใจว่า Scrum, Kanban และ predictive governance ใช้ต่างกันอย่างไร และควรรวมกันอย่างไรโดยไม่ทำให้ control หลุด

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. อธิบาย Agile mindset โดยไม่ตีความว่าไม่มีแผน
2. แยก Scrum, Kanban และ predictive governance
3. ใช้ Product Backlog, Flow Board และ Definition of Done อย่างมี owner
4. ปกป้อง sprint goal ด้วย product priority และ risk evidence
5. สร้าง Product Backlog, Flow Board และ Feedback Evidence เพื่อส่งต่อ Lesson 16

## 4. Beginner Safety

Agile ไม่ได้แปลว่าไม่มีเอกสาร ไม่มีแผน ไม่มี PM skill หรือเปลี่ยน scope ได้ทุกวันโดยไม่มีผลกระทบ

Agile แปลว่าทีมทำงานเป็นรอบสั้น ส่งมอบสิ่งที่ตรวจได้ รับ feedback และปรับแผนตาม evidence โดยยังรักษา quality, risk และ governance ให้พอดีกับบริบท

คำศัพท์ใหม่คือ Agile Mindset, Product Backlog, Sprint Goal, Product Owner, Scrum Master, Definition of Done, Kanban, WIP Limit, Flow Policy และ Feedback Evidence

## 5. Mental Model

```text
Uncertainty / Value Question
-> Backlog Priority
-> Sprint or Flow Policy
-> Working Increment / Flow Item
-> Feedback Evidence
-> Adaptation
-> Governance Check
```

Agile ไม่ได้ตัด governance ทิ้ง แต่เปลี่ยน cadence ของการเรียนรู้และตัดสินใจให้สั้นลง

## 6. Main Lesson

Scrum เหมาะกับ product development ที่ต้องส่งมอบ increment เป็นรอบ มี Product Owner จัดลำดับ backlog, Scrum Master ช่วยให้ทีมทำงานตาม Scrum, และ Developers ส่ง increment ตาม Sprint Goal

Scrum events เช่น Sprint Planning, Daily Scrum, Sprint Review และ Retrospective ไม่ใช่พิธีเพื่อให้ดู Agile แต่เป็นจังหวะวางแผน ตรวจ feedback และปรับปรุง

Kanban เหมาะกับงาน flow/support/incident ที่เข้ามาต่อเนื่อง เช่น defect triage, payment incident, support request หรือ data migration issue Kanban ใช้ visual board, Work in Progress limit, explicit policy และ flow metrics เพื่อจัดการ bottleneck

Flow Board คือ visual board ที่ทีมใช้บริหาร Kanban จริง แสดงสถานะงานแต่ละชิ้นตาม column เช่น To Do, In Progress, Review และ Done พร้อม WIP limit และ policy กำกับแต่ละ column เพื่อให้เห็น bottleneck และ owner ของแต่ละงานชัดเจน ไม่ใช่กระดานที่มีแค่ sticky note ไล่งานโดยไม่มี policy กำกับ

Predictive governance ยังสำคัญเมื่อ scope ชัด contract เข้ม compliance สูง หรือ baseline ต้องควบคุม เช่น ERP migration, procurement, budget และ cutover

## 7. PM Thinking

เมื่อเลือก Agile practice ให้ถาม:

- งานนี้มี uncertainty สูงหรือไม่
- ต้องเรียนรู้จาก user feedback บ่อยแค่ไหน
- PO มี authority จัด priority จริงหรือไม่
- Definition of Done รวม quality/security/acceptance หรือยัง
- งานเป็น sprint feature หรือ flow/support incident
- Vendor/contract constraints จำกัดวิธีทำงานอย่างไร
- Governance/risk control ใดยังต้องมี

Agile ที่ไม่มี owner และ feedback evidence จะกลายเป็นแค่ board ที่สวย

## 8. PM Decision Thinking

```text
Decision: งานนี้ควรใช้ Scrum, Kanban, predictive governance หรือ hybrid practice
Owner: PO จัดลำดับ value; Delivery Team ดู flow; PM ดู governance, risk และ stakeholder alignment
Inputs: requirement uncertainty, release cadence, team maturity, compliance, dependency, support demand, Definition of Done
Options: sprint delivery, Kanban flow, predictive control, hybrid by workstream, defer item, split release
Trade-offs: flexibility vs predictability, speed vs quality, learning vs governance overhead
Evidence: backlog decision, board policy, WIP data, review feedback, release readiness, risk control
```

คำตอบที่ดีต้องแยก ownership: PO ไม่ควรเป็นเจ้าของ flow operational ทุกเรื่อง และ PM ไม่ควรจัด priority product แทน PO โดยไม่มี governance

## 9. ERP Worked Example

ERP โดยรวมอาจใช้ predictive/hybrid governance เพราะมี contract, modules, migration, budget และ go-live deadline แต่บาง workstream ใช้ Agile practices ได้

ตัวอย่าง:

- Kanban board สำหรับ defect flow ระหว่าง SIT และ data migration
- Daily standup 15 นาทีระหว่าง TechConsult และทีมคุณเอกเพื่อเห็น blockers
- Sprint-like feedback สำหรับ configuration prototype
- Review session กับ key users เพื่อยืนยัน process fit ก่อน UAT ใหญ่

ข้อควรระวังคืออย่าเรียกทั้ง ERP ว่า Agile เพียงเพราะใช้ board หรือ standup หาก approval, baseline, procurement และ cutover ยัง predictive อยู่

## 10. Hotel Booking Example or Contrast

Hotel Booking เหมาะกับ Scrum/Kanban มากกว่า ERP เพราะต้องเรียนรู้จาก user behavior, conversion, payment failure และ partner feedback

เมื่อ payment resilience กระทบ MVP checkout และ marketing ขอ promotion feature PO ควรจัด priority โดยดู outcome evidence ถ้า payment risk ยังสูง promotion ควรเลื่อนลง backlog หรือ split ออกเป็น phase หลัง core booking path เสถียร

Kanban อาจใช้กับ payment incident และ support flow ส่วน Scrum ใช้กับ feature development ที่ส่ง increment เป็น sprint

## 11. Watch PM Think

ลำดับคิด:

1. ระบุส่วนของงานที่ต้องเรียนรู้เร็ว
2. แยก feature work ออกจาก flow/support work
3. ตรวจ ownership: PO, Delivery Team, PM, Release Authority
4. ตรวจ Definition of Done ว่ารวม quality/security/acceptance
5. ใช้ feedback evidence ปรับ backlog
6. จำกัด WIP เมื่อ bottleneck เกิด
7. เก็บ governance/risk control ที่ยังจำเป็น

ถ้าทีมมี ceremony ครบแต่ไม่มี feedback ที่เปลี่ยน decision แปลว่ายังไม่ Agile จริง

## 12. Artifact Example

Artifact ของบทนี้คือ:

- Product Backlog
- Flow Board
- Feedback Evidence
- Board Policy
- Release Authority record

ใช้ template ต้นทางได้ที่ [Agile Artifact Template](../../../lessons/lesson-15/learner/Artifact-Template.md)

Artifact นี้ส่งต่อ Lesson 16 เพราะ tailoring ต้องดูว่า agile practice ใดใช้กับ workstream ใดและมี control อะไร

## 13. Workshop

Protect the Hotel Booking Sprint Goal:

payment risk threatens MVP checkout while marketing requests a promotion feature. ให้สร้าง:

- updated backlog
- sprint goal decision
- flow board policy
- blocker response
- feedback request
- Definition of Done check
- governance/risk control ที่ยังต้องมี

ข้อจำกัด: ห้ามให้ PM, PO และ team เป็น co-owner ทุก artifact แบบไม่แยกบทบาท

## 14. Beginner Checkpoint

1. Agile ต่างจากการไม่มีแผนอย่างไร
2. Scrum เหมาะกับงานแบบใด
3. Kanban เหมาะกับงานแบบใด
4. Product Owner เป็น owner ของอะไร
5. Definition of Done ควรรวมอะไรบ้าง

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่าง

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย Agile mindset, Scrum, Kanban, Product Backlog, Sprint Goal, WIP limit และ Definition of Done

### B. Scenario Question

Hotel Booking payment risk กับ promotion feature ให้จัด backlog priority พร้อมเหตุผล

### C. Decision Case

ERP ใช้ Agile practices ตรงไหนได้โดยไม่ทำให้ predictive governance หลุด

### D. Artifact Construction

สร้าง Product Backlog, Flow Board และ Feedback Evidence จาก L14 acceptance/contract constraints

### E. Artifact Review

ตรวจ Agile board ที่มีงานเต็มแต่ไม่มี WIP policy, owner, blocker หรือ feedback evidence แล้วแก้ให้ usable

### F. Reflection

เขียนไม่เกิน 180 คำว่า Agile theater ต่างจาก Agile ที่ส่ง value จริงอย่างไร

Assessment นี้เน้น sprint-goal decision 40%, backlog artifact review 30%, predictability-versus-flexibility trade-off 20% และ recall 10%

## 16. เก็บตกท้ายบท

ประโยคที่ควรจำ:

```text
Agile ไม่ใช่การไม่มีวินัย
Agile คือวินัยที่สั้น เร็ว และเรียนรู้จาก evidence จริง
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Agile ไม่มีแผน | Agile วางแผนบ่อยและปรับจาก feedback |
| Agile ไม่ต้องเอกสาร | เอกสารยังมี แต่พอดีกับ value และ risk |
| Ceremony คือ Agile | Agile อยู่ที่ learning loop และ value delivery |
| Agile ไม่มี PM skill | Integration, risk, stakeholder และ governance ยังจำเป็น |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Agile | แนวคิดคล่องตัว | เรียนรู้และส่ง value เป็นรอบ |
| Product Backlog | รายการงาน product | งานเรียงตาม priority/value |
| Sprint Goal | เป้าหมาย sprint | focus ของรอบส่งมอบ |
| Product Owner | เจ้าของ product priority | ตัดสินลำดับ value |
| Definition of Done | เกณฑ์เสร็จ | เงื่อนไขว่างานเสร็จจริง |
| Kanban | วิธีบริหาร flow | เห็นงาน จำกัด WIP และแก้ bottleneck |
| Flow Board | บอร์ดบริหาร flow | visual board ที่มี column, WIP limit และ policy กำกับ |
| WIP Limit | จำกัดงานค้าง | ป้องกันทีมรับงานเกิน capacity |

## 19. สรุปหนึ่งหน้า

Agile คือการส่งมอบ value เป็นรอบสั้น เรียนรู้จาก feedback และปรับตัวอย่างมีวินัย

Scrum เหมาะกับ product increment ส่วน Kanban เหมาะกับ flow/support/incident work

ERP อาจใช้ agile practices บางส่วนใน hybrid governance ส่วน Hotel Booking ใช้ Agile มากกว่าเพราะต้องเรียนรู้จาก market และ user behavior

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | L14 acceptance and contract constraints |
| Output | PO-owned backlog, Delivery Team-owned flow board and feedback evidence |
| Owner | PO for priority; Delivery Team for operational flow; release authority recorded separately |
| Next lesson use | Lesson 16 ใช้ Agile tools เป็นตัวเลือกใน tailored predictive/agile/hybrid approach |


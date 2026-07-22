---
chapter: lesson-12
title: Project Communications Management
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-12/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 12 — Project Communications Management

## 1. Opening Scenario

ERP data migration เป็นสีแดง แต่ weekly email แสดงเพียง percentage complete ผู้บริหารอ่านแล้วไม่รู้ว่าต้องตัดสินใจอะไร ภายในเมื่อไร และถ้าไม่ตัดสินใจ cutover จะเสี่ยงอย่างไร

ทีม project บอกว่า "ส่งรายงานไปแล้ว" แต่ Sponsor ตอบว่า "ไม่เคยรู้ว่าต้องตัดสินใจเรื่องนี้"

นี่คือความต่างระหว่างการส่งข้อมูลกับการสื่อสารที่ทำให้เกิดความเข้าใจและ action

## 2. Why This Matters

Project Communications Management ไม่ใช่การส่งรายงานให้ครบ distribution list แต่คือการทำให้ข้อมูลที่ถูกต้องไปถึงคนที่ถูกต้องในเวลาที่ถูกต้อง ผ่านช่องทางที่เหมาะสม และนำไปสู่ความเข้าใจ การตัดสินใจ หรือ action ที่ต้องการ

PM ใช้เวลาส่วนใหญ่กับการสื่อสาร แต่การสื่อสารที่มากขึ้นไม่ได้แปลว่าดีขึ้น หากข้อความไม่ชัด ผู้รับไม่ใช่คนตัดสินใจ หรือไม่มี feedback loop

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. แยก data, information, communication, status report และ decision brief
2. เลือก push, pull หรือ interactive communication ให้เหมาะกับผู้รับและสถานการณ์
3. ออกแบบ communication plan จาก stakeholder need, decision need และ feedback loop
4. สร้าง escalation message ที่มี decision ask, evidence และ response record
5. สร้าง Communication Plan, Cadence และ Status Report

## 4. Beginner Safety

ส่ง email แล้วไม่ใช่หลักฐานว่าการสื่อสารสำเร็จ ถ้าไม่มี acknowledgement, decision, action หรือ feedback loop

กับดักอีกอย่างคือส่งข้อมูลชุดเดียวให้ทุก stakeholder ผู้บริหารต้องการ decision brief ทีมงานต้องการ detail ผู้ใช้ต้องการ next action ส่วน vendor ต้องการ defect clarification ถ้าทุกคนได้รายงานเดียวกัน อาจไม่มีใครได้สิ่งที่ต้องใช้จริง

## 5. Mental Model

```text
RACI / Audience
-> Decision Need
-> Message
-> Channel and Cadence
-> Feedback / Acknowledgement
-> Decision or Escalation Record
-> Risk Signal
```

Lesson 11 บอกว่าใครมีบทบาทและอำนาจ Lesson 12 ถามต่อว่าแต่ละคนต้องได้ข้อมูลอะไรเพื่อทำหน้าที่นั้น

## 6. Main Lesson

Data คือสัญญาณดิบ เช่น defect count หรือ percentage complete Information คือ data ที่ถูกจัดให้มีความหมาย Communication คือการส่งสารให้เกิดความเข้าใจและ action

Status Report บอกสถานะตามรอบ Decision Brief ขอการตัดสินใจที่มีขอบเขตชัด เช่น ขอเลือก recovery option ภายในวันศุกร์

รูปแบบการสื่อสารหลัก:

- Push Communication: ส่งข้อมูลออกไป เช่น email, report, announcement
- Pull Communication: ให้ผู้รับดึงข้อมูลเอง เช่น dashboard, wiki, repository
- Interactive Communication: สื่อสารสองทาง เช่น meeting, workshop, call

แผนสื่อสารแบบ 5W1H ควรตอบว่าใครต้องรู้อะไร ทำไม เมื่อไร ผ่านช่องทางใด ใครเป็น owner และ feedback จะถูกจับอย่างไร

## 7. PM Thinking

เมื่อต้องสื่อสารเรื่องสำคัญ ให้ถาม:

- audience ต้องตัดสินใจหรือทำอะไร
- message ควรเป็นข้อมูล สถานะ recommendation หรือ decision brief
- urgency, complexity และ sensitivity เหมาะกับ channel ใด
- ใครเป็น message owner
- ต้องได้ response ภายในเมื่อไร
- acknowledgement, decision และ escalation จะถูกบันทึกที่ไหน

การสื่อสารที่ดีเริ่มจากผู้รับ ไม่ใช่จากสิ่งที่ PM อยากส่ง

## 8. PM Decision Thinking

```text
Decision: เรื่องนี้ควรสื่อสารแบบ dashboard-only, targeted brief, workshop หรือ escalation
Owner: PM ออกแบบ communication system; message owner ส่งสารเฉพาะเรื่อง
Inputs: stakeholder needs, RACI, urgency, complexity, sensitivity, decision required, channel effectiveness
Options: executive summary, dashboard, workshop, meeting, email, read-back, issue escalation
Trade-offs: speed vs understanding, detail vs attention, transparency vs noise
Evidence: communication matrix, distribution record, acknowledgement, decision log, escalation response
```

Dashboard ที่มีสีแดงไม่ใช่ escalation หากไม่มี decision ask และ response record

## 9. ERP Worked Example

ERP มี Sponsor คุณสมชาย, PM คุณเอก, TechConsult, 80 key users และหลาย functional managers

Data migration risk ไม่ควรถูกซ่อนอยู่ใน weekly email หน้า 7 Steering Committee ควรได้รับ one-page decision brief ที่ระบุ:

- decision required by Friday
- impact on cutover and go-live
- three recovery options
- recommendation
- evidence confidence
- consequence if no decision

ส่วน workstream team ต้องได้ defect detail รายวัน key users ต้องได้ UAT impact และ functional managers ต้องเห็น capacity implication

## 10. Hotel Booking Example or Contrast

Hotel Booking มี PO คุณนภา, PM คุณสุทธิ, marketing, product team, hotel partners และ operations

Payment incident ก่อน launch campaign ต้องสื่อสารหลายชั้น Product team ต้องรู้ technical action PO ต้องรู้ release decision Marketing ต้องรู้ campaign risk Hotel partners ต้องรู้ rollout impact Operations/support ต้องมี known issues และ escalation path

ลูกค้าไม่จำเป็นต้องรู้ technical detail ทั้งหมด แต่ถ้ามี service impact ต้องมี message ที่ชัด ซื่อสัตย์ และไม่สร้างความสับสน

## 11. Watch PM Think

ลำดับคิดของ PM:

1. เริ่มจาก RACI และ stakeholder need
2. แยก data, information, status และ decision ask
3. เลือก audience ตามอำนาจและ action ที่ต้องการ
4. เลือก channel ตาม urgency/complexity
5. กำหนด cadence และ owner
6. บันทึก acknowledgement, decision และ escalation
7. ส่งต่อ risk signal ให้ Lesson 13

ถ้า communication artifact ไม่มี decision need หรือ feedback loop ยังไม่ควรถือว่า usable

## 12. Artifact Example

Artifact ของบทนี้คือ:

- Communication Plan
- Cadence
- Status Report
- Decision/Escalation Log

ใช้ template ต้นทางได้ที่ [Communication Artifact Template](../../../lessons/lesson-12/learner/Artifact-Template.md)

Artifact นี้ส่งต่อ Lesson 13 เพราะ risk ที่ไม่ได้ถูกสื่อสารให้ถูกคนทันเวลา จะกลายเป็น issue ที่องค์กรรับมือช้า

## 13. Workshop

เปลี่ยน ERP technical red status ให้เป็น executive decision brief หนึ่งหน้า:

- audience
- decision need
- message
- evidence
- options
- channel/cadence
- owner
- response deadline
- decision/escalation record

ข้อจำกัด: Sponsor อนุมัติ communication plan/cadence ส่วน PM อนุมัติ recurring status report

## 14. Beginner Checkpoint

1. Data ต่างจาก information อย่างไร
2. Status report ต่างจาก decision brief อย่างไร
3. Push, pull และ interactive ใช้ต่างกันอย่างไร
4. Sponsor อนุมัติอะไร และ PM อนุมัติอะไร
5. Escalation ที่ดีต้องมีอะไร

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่าง

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย data, information, communication, push, pull, interactive, status report และ decision brief

### B. Scenario Question

ERP data migration red status ต้องสื่อสารกับ Steering Committee, workstream, key users และ functional managers ต่างกันอย่างไร

### C. Decision Case

Hotel Booking payment incident ก่อน launch campaign ให้เลือก channel และ message สำหรับ PO, marketing, partners, customers และ support

### D. Artifact Construction

สร้าง Communication Plan, Cadence และ Status Report โดยใช้ approved RACI จาก Lesson 11

### E. Artifact Review

ตรวจ weekly report ที่มีเปอร์เซ็นต์แต่ไม่มี decision ask, owner, deadline หรือ escalation path แล้วแก้ให้ใช้ตัดสินใจได้

### F. Reflection

เขียนไม่เกิน 180 คำว่า "ส่งแล้ว" ต่างจาก "สื่อสารสำเร็จ" อย่างไร

Assessment นี้เน้น executive communication 40%, communications-plan artifact review 30%, channel/cadence trade-off 20% และ recall 10%

## 16. เก็บตกท้ายบท

ประโยคที่ควรจำ:

```text
Communication สำเร็จเมื่อผู้รับเข้าใจ ตัดสินใจ หรือดำเนินการได้
ไม่ใช่เมื่อผู้ส่งกด send
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Communication คือส่งข้อมูล | Communication คือ shared understanding plus action |
| Dashboard คือ escalation | Escalation ต้องมี decision ask และ response record |
| รายงานเดียวพอสำหรับทุกคน | ต้อง tailor ตาม audience และ decision need |
| ส่งแล้วคือเสร็จ | ต้อง monitor acknowledgement/action |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Communications Plan | แผนสื่อสาร | ผู้รับ ข้อมูล ความถี่ ช่องทาง owner |
| Push Communication | ส่งออก | email/report/announcement |
| Pull Communication | ดึงเอง | dashboard/wiki/repository |
| Interactive Communication | สองทาง | meeting/workshop/call |
| Status Report | รายงานสถานะ | บอกสถานะตามรอบ |
| Decision Brief | บันทึกขอตัดสินใจ | ขอ decision พร้อม evidence/deadline |
| Escalation | การยกระดับ | ส่งเรื่องให้ authority ตัดสิน |

## 19. สรุปหนึ่งหน้า

Communications Management คือการออกแบบให้ข้อมูลถูกคน ถูกเวลา ถูกช่องทาง และทำให้เกิดความเข้าใจหรือ action

PM ต้องแยก status report ออกจาก decision brief และต้องบันทึก acknowledgement, decision และ escalation

Lesson 12 คือสะพานไป Lesson 13 เพราะ risk ที่ไม่ถูกสื่อสารจะถูกจัดการไม่ทัน

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | Approved RACI and resource commitments from Lesson 11 |
| Output | Communication Plan, Cadence and Status Report |
| Owner | PM |
| Approval | Sponsor for plan/cadence; PM for each status report |
| Next lesson use | Lesson 13 ใช้ status signals and escalation path เพื่อแปลง uncertainty เป็น risk, response และ trigger |


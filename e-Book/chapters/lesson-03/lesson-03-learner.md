---
chapter: lesson-03
title: 5 Project Management Process Groups
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-03/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 03 — 5 Project Management Process Groups

## 1. Opening Scenario

ERP อยู่ช่วง planning แต่ทีม System Integrator เริ่ม prototype แล้ว Data Owner ยังไม่ยืนยัน cleansing rules และ UAT capacity ของ key users ยังไม่ชัด

คุณเอกซึ่งเป็น PM มีแรงกดดันสองด้าน ด้านหนึ่งคือ timeline ต้อง go-live ก่อน 1 ตุลาคม อีกด้านหนึ่งคือถ้าข้อมูล master data ไม่พร้อม การ build ต่ออาจทำให้ rework ใหญ่กว่าเดิม

คำถามคือ:

```text
ถ้าโครงการเริ่มทำงานจริงไปแล้ว แต่พบว่าขอบเขตหรือข้อมูลสำคัญยังไม่ชัด
ควรกลับไป Planning หรือเดินหน้าต่อ
```

ถ้าเรามอง Process Groups เป็นเส้นตรง เราอาจตอบว่า “ผ่าน planning แล้ว ห้ามย้อนกลับ” แต่ถ้าเรามองแบบ PM มืออาชีพ เราจะถามว่า evidence ใหม่กระทบ baseline, decision gate หรือ transition readiness หรือไม่

## 2. Why This Matters

5 Process Groups คือกลุ่มกิจกรรมบริหารโครงการ ไม่ใช่ 5 phases ที่เดินเรียงแล้วห้ามย้อนกลับ

ความเข้าใจผิดที่แพงมากคือการวาดแบบนี้:

```text
Initiating -> Planning -> Executing -> Monitoring -> Closing
```

แล้วคิดว่า Monitoring เริ่มหลังงานเสร็จ หรือ Closing คือประชุมสรุปบทเรียนอย่างเดียว

ในชีวิตจริง Executing กับ Monitoring & Controlling ต้องเกิดคู่กัน เพราะถ้าทำงานโดยไม่อ่าน evidence เราจะรู้ปัญหาช้าเกินไป และถ้า monitor แล้วไม่ control หรือไม่ replan เราก็มีแต่ report ที่ไม่เปลี่ยนการตัดสินใจ

มุมมอง value delivery ทำให้ process มีไว้เพื่อช่วยตัดสินใจ ไม่ใช่เพื่อทำเอกสารให้ครบพิธี

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. อธิบาย 5 Process Groups ได้โดยไม่สับสนกับ project phases
2. แยก Initiating, Planning, Executing, Monitoring & Controlling และ Closing ตามหน้าที่การบริหาร
3. อธิบายว่า Planning เกิดซ้ำได้เมื่อมี evidence ใหม่
4. อธิบายว่า Executing และ Monitoring & Controlling เกิดคู่กันอย่างไร
5. วิเคราะห์ ERP และ Hotel Booking ด้วย feedback loop และ replanning trigger
6. สร้าง Lifecycle and Process Group Map ที่ส่งต่อไป Lesson 04 ได้

## 4. Beginner Safety

คุณควรรู้จาก Lesson 02 แล้วว่า Project ต่างจาก Operation และ Value Chain ต้องมี transition point

บทนี้ยังไม่ต้องจำรายละเอียด process ทั้งหมด ไม่ต้องลงลึก WBS, schedule network, EVM, procurement law หรือ Scrum events

สิ่งที่ต้องระวังคือ:

- อย่าใช้ชื่อ Process Groups เป็นชื่อ phase ทั้งหมด
- อย่าคิดว่า Planning ทำครั้งเดียว
- อย่าคิดว่า Monitoring คือการรายงานย้อนหลังเท่านั้น
- อย่าคิดว่า Closing คือการเซ็นรับหรือประชุมปิดงานเท่านั้น

## 5. Mental Model

ให้มอง Process Groups เป็นระบบบริหารที่ทำงานร่วมกัน

```text
Initiating
    ↓
Planning
    ↓
Executing <-> Monitoring & Controlling
      ↑              ↓
      └── Replanning ┘
    ↓
Closing
```

และให้แยกสองคำนี้ให้ชัด:

- `Project Phase` คือช่วง lifecycle ของงาน เช่น Blueprint, Build, Test, Cutover
- `Process Group` คือกลุ่มกิจกรรมบริหาร เช่น Initiating, Planning, Executing, Monitoring & Controlling, Closing

ใน phase เดียวกันอาจมีหลาย Process Groups เกิดร่วมกันได้ เช่นช่วง Test มี executing test, monitoring defect trend, controlling change, planning retest และ closing phase gate

## 6. Main Lesson

### Initiating

Initiating คือการตั้งต้น project หรือ phase ให้มี authority และเป้าหมายชัด ไม่ใช่แค่ kickoff meeting

Output สำคัญอาจรวม Project Charter และ stakeholder information จุดสำคัญคือใครอนุมัติ ทำไปเพื่ออะไร และ success measure ระดับสูงคืออะไร

ถ้าเริ่ม executing ก่อนมี initiating ที่ดี ทีมอาจมี schedule แต่ไม่มี sponsor authority, decision rule หรือ benefit owner

### Planning

Planning คือการวางแนวทางเพื่อให้บรรลุ objective และสร้าง baseline สำหรับบริหาร scope, schedule, cost, quality, risk, communication และเรื่องอื่น ๆ

Planning ไม่ใช่กิจกรรมครั้งเดียว เพราะข้อมูลโครงการค่อย ๆ ชัดขึ้นตาม evidence จริง สิ่งนี้เรียกว่า progressive elaboration

การ replan เมื่อมี evidence ใหม่ไม่ใช่การไม่มีแผน แต่เป็นการใช้ control เพื่อปรับแผนอย่างมีเหตุผล

### Executing

Executing คือการทำงานเพื่อสร้าง deliverable ตามแผน เช่น configure ERP, migrate data, train users, develop app, run beta หรือ prepare launch

Executing ไม่ใช่เฉพาะ technical work เพราะรวมการประสานคน สื่อสาร จัดการ issue และทำให้ทีมทำงานตามแผนที่ตกลง

### Monitoring & Controlling

Monitoring & Controlling คือการติดตาม วิเคราะห์ variance และตัดสินใจตอบสนอง ไม่ใช่การส่งรายงานเฉย ๆ

ตัวอย่าง evidence เช่น progress, defect trend, migration reconciliation result, payment failure, conversion rate, risk signal และ readiness metric

ถ้า evidence กระทบ baseline ต้องมี change request, impact analysis และ decision owner ที่เหมาะสม

### Closing

Closing คือการปิด project หรือ phase อย่างเป็นทางการ รวม acceptance, handover, contract closure, lessons learned, unresolved item ownership และ transition to operation

Go-live ไม่ใช่ Closing ครบถ้วน หาก support model, operation owner และ benefit review ยังไม่พร้อม

## 7. PM Thinking

เมื่อเกิดความเบี่ยงเบน ให้ถามเป็น flow:

```text
1. ตอนนี้เกิดอะไรใน Executing
2. Evidence จาก Monitoring บอกอะไร
3. กระทบ baseline หรือ charter หรือไม่
4. ต้อง control ด้วย corrective action, preventive action, change request หรือ replan
5. ใครเป็น decision owner
6. Evidence ใดต้อง update ก่อนเดินต่อ
```

คำตอบที่ดีมักไม่ใช่ “หยุดทั้งหมด” หรือ “ลุยทั้งหมด” แต่คือ “งานใดไปต่อได้ งานใดต้อง replan และงานใดต้อง escalate”

## 8. PM Decision Thinking

ตัวอย่าง decision:

```text
Decision: ปัญหาที่พบควรแก้ใน Executing, ส่งเข้า Monitoring & Controlling, replan หรือ escalate กลับไป Sponsor
Owner: PM เสนอ analysis; Sponsor, change authority หรือ steering committee ตัดสินเมื่อกระทบ baseline/charter
Inputs: charter, baseline, actual progress, work performance data, issue log, risk, impact analysis
Options: execute ต่อ, corrective action, preventive action, change request, rebaseline, defer scope
Trade-offs: speed vs control, local fix vs systemic fix, schedule protection vs adoption/readiness
Risk: มอง Process Groups เป็น phase เส้นตรง, ข้าม change control, ซ่อน variance
Evidence: variance data, root cause, user impact, cost/schedule impact, go-live readiness
Next Action: สร้าง decision brief และระบุ Process Group ที่ต้อง activate ต่อ
```

## 9. ERP Worked Example

ใน ERP Transformation ของ SIG ถ้า TechConsult ขอเริ่ม build เพื่อรักษา timeline แต่ Data Owner ยังไม่ยืนยัน cleansing rules PM ไม่ควรตอบว่า “planning จบแล้ว ไปต่อ”

เขาควรแยก:

- Executing: prototype หรือ configuration บางส่วนอาจเดินต่อได้
- Monitoring & Controlling: evidence บอกว่า data ownership และ UAT capacity เป็น risk
- Planning: data workstream, cleansing rule, retest และ quality gate ต้อง replan
- Sponsor escalation: ถ้า replan กระทบ go-live ก่อน 1 ตุลาคมหรือ objective ระดับ charter ต้องเข้า steering committee
- Closing risk: ถ้าไม่แก้ ownership ตอนนี้ handover ไป operation จะไม่เสถียร

ข้อสรุปเชิง PM คืออนุญาตเฉพาะงานที่ไม่สร้าง rework risk สูง และแยกงานที่ต้องกลับไป planning พร้อม evidence ชัดเจน

## 10. Hotel Booking Example or Contrast

ใน Hotel Booking Platform ถ้าช่วง beta พบ payment failure สูง, conversion ต่ำ และผู้ใช้บอกว่า checkout flow ยาว ทั้งที่ marketing ต้องการ launch ตามแผน Process Groups ยังทำงานอยู่ครบ

- Executing: ทีมยัง develop และ fix bug
- Monitoring & Controlling: beta metrics และ user feedback ส่งสัญญาณ risk
- Planning: backlog, release criteria, support plan และ launch readiness ต้องปรับ
- Decision gate: sponsor/product owner ต้องตัดสินใจว่าพร้อม launch, delay หรือ launch แบบจำกัด scope
- Closing/Transition: ถ้าเปิด MVP ต้องส่งต่อ product operations และ stabilization plan

Agile ไม่ได้ยกเลิก Process Groups แต่เปลี่ยน cadence ให้ planning, execution, monitoring และ replanning เกิดถี่ขึ้น

## 11. Watch PM Think

ก่อนสร้าง Lifecycle and Process Group Map ให้คิดตามนี้:

1. นำ project boundary และ value chain จาก Lesson 02 มาใช้ ไม่สร้าง objective ใหม่
2. ตั้ง lifecycle phases จากลักษณะ delivery เช่น Blueprint, Build, Test, Cutover
3. วาง Process Groups ซ้ำในหลาย phase ตาม management need
4. จับคู่ executing activity กับ monitoring signal
5. กำหนด trigger ที่ทำให้ต้อง replan
6. กำหนด closing จาก acceptance, transition, open-item ownership และ benefits handoff

ถ้า map ของคุณเรียง Initiating, Planning, Executing, Monitoring, Closing เป็น phase ทั้งหมด แปลว่ายังไม่ผ่านบทนี้

## 12. Artifact Example

Artifact ของบทนี้คือ `Lifecycle and Process Group Map`

ใช้ template ต้นทางได้ที่ [Lifecycle and Process Group Map Template](../../../lessons/lesson-03/learner/Artifact-Template.md)

Artifact ต้องมี:

- Project boundary from Lesson 02
- Lifecycle phases
- Process Group activity map
- Feedback and replanning
- Closing and transition
- Approval fields

## 13. Workshop

ERP อยู่ช่วง planning แต่ทีม SI เริ่ม prototype แล้ว Data Owner ยังไม่ยืนยัน cleansing rules และ UAT capacity ของ key users ยังไม่ชัด

ให้คุณ:

- ร่าง lifecycle phases ตั้งแต่ initiation ถึง benefits transition
- วาง management activities ลงใน Process Groups
- แสดงว่า Executing กับ Monitoring & Controlling เกิดคู่กันตรงไหน
- ระบุ signal ที่ต้องกลับไป Replanning
- กำหนด exit evidence และ approval authority ของแต่ละ gate

ข้อจำกัด: ห้ามใช้ Process Groups เป็นชื่อ phase ทั้งหมด และห้ามใส่ Planning เพียงครั้งเดียว

## 14. Beginner Checkpoint

ตอบโดยไม่เปิดเฉลย:

1. Process Group ต่างจาก Project Phase อย่างไร
2. Planning เกิดหลัง Initiating ครั้งเดียวหรือไม่
3. Monitoring & Controlling เกิดก่อนหรือหลัง Executing
4. Closing ต้องมีหลักฐานอะไรนอกจาก meeting ปิดงาน
5. Signal แบบใดทำให้ต้อง Replanning

ผ่านเมื่ออธิบาย 4 จาก 5 ข้อและยกตัวอย่างจาก ERP หรือ Hotel Booking ได้

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบายความต่างของ Process Group และ Project Phase พร้อมยกตัวอย่างจาก ERP หรือ Hotel Booking

### B. Scenario Question

ERP data readiness ไม่พอแต่ build เริ่มแล้ว ให้ระบุ Process Groups ที่เกี่ยวข้อง evidence ที่มี/ขาด งานที่ไปต่อได้ งานที่ต้อง replan และ decision owner

### C. Decision Case

Hotel Booking beta พบ payment failure และ conversion ต่ำ ให้เสนอว่าควร execute ต่อ, control, replan, escalate หรือ delay launch อย่างไร พร้อม trade-off

### D. Artifact Construction

สร้าง Lifecycle and Process Group Map ที่มี phases, gates, Process Group activities, feedback triggers, closing evidence และ transition owner

### E. Artifact Review

ตรวจข้อความนี้: “Initiating คือ Phase 1, Planning คือ Phase 2, Executing คือ Phase 3, Monitoring เริ่มหลัง build เสร็จ และ Closing คือประชุมสรุปบทเรียน” ระบุจุดผิดอย่างน้อย 4 จุดและเสนอ flow ใหม่

### F. Reflection

เขียนสั้น ๆ ว่าในโครงการของคุณ Process Group ใดอ่อนที่สุด และส่งผลต่อ decision, evidence หรือ value อย่างไร

Assessment นี้เน้น retrieval 10% และ application/judgement/artifact 90%

## 16. เก็บตกท้ายบท

การกลับไป Planning ไม่ใช่เรื่องน่าอาย ถ้ามี evidence ใหม่ที่ทำให้ baseline เดิมไม่จริงอีกต่อไป

สิ่งที่น่าอายกว่า คือรู้ว่า evidence เปลี่ยนแล้วแต่ยังเดินต่อเพราะกลัวรายงานว่า “ต้อง replan”

สัญญาณเตือน:

- ทีมพูดว่า “ผ่าน planning แล้ว” เพื่อปิดการถกผลกระทบ
- Status report มีแต่ percent complete ไม่มี decision required
- Monitoring เกิดหลังงานเสร็จ ไม่ใช่ระหว่างทำ
- Closing ไม่มี owner หลัง handover
- Agile team ใช้คำว่า sprint เพื่อเลี่ยง launch readiness gate

ประโยคที่ใช้ในที่ประชุม:

```text
นี่ไม่ใช่การย้อนกลับเพราะวางแผนไม่ดี
แต่เป็นการ activate Planning จาก evidence ใหม่ผ่าน Monitoring & Controlling
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Process Groups คือ waterfall phases | เป็น management functions ที่เกิดซ้ำและซ้อนทับได้ |
| Planning ทำครั้งเดียว | Planning ปรับได้ผ่าน evidence และ control |
| Monitoring คือ report | Monitoring & Controlling คือการอ่าน variance และตัดสินใจตอบสนอง |
| Controlling คือควบคุมคน | Controlling คือควบคุมงานเทียบ baseline และ decision |
| Closing คือเซ็นรับ | Closing รวม handover, lessons learned, contract closure และ owner หลังปิด |
| Agile ไม่มี Planning/Closing | Agile ยังมี เพียง cadence และระดับรายละเอียดต่างกัน |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย | ตัวอย่าง Scenario | คำที่มักสับสน |
|---|---|---|---|---|
| Process Group | กลุ่มกระบวนการบริหาร | โหมดการบริหาร 5 กลุ่มที่ใช้ตั้งต้น วางแผน ทำงาน ควบคุม และปิด | Monitoring & Controlling ระหว่าง ERP UAT | Project Phase |
| Project Phase | ระยะของโครงการ | ช่วง lifecycle เช่น Blueprint, Build, Test, Cutover | Hotel Booking Beta phase | Process Group |
| Lifecycle | วงจรชีวิตโครงการ | ลำดับ phase ตั้งแต่เริ่มจนส่งต่อ | ERP Initiation ถึง Hypercare | Process Group |
| Feedback Loop | วงจรข้อมูลย้อนกลับ | evidence จากงานจริงที่ทำให้ต้องปรับ decision | Payment failure ทำให้ปรับ backlog | Status report |
| Progressive Elaboration | การทำให้แผนชัดขึ้นเรื่อย ๆ | ข้อมูลใหม่ทำให้แผนละเอียดขึ้น | Data cleansing rule ชัดหลัง profiling | Scope creep |
| Replanning | การปรับแผนใหม่ | ปรับแผนจาก evidence ผ่าน control | Replan migration retest | ทำงานไร้แผน |
| Work Performance Data | ข้อมูลผลงานจริง | progress, defect, effort, test result | SIT delay 2 weeks | Opinion |
| Change Request | คำขอเปลี่ยนแปลง | ขอปรับ baseline อย่างเป็นทางการ | เพิ่ม approval step ก่อน go-live | Issue |
| Corrective Action | การแก้ให้กลับเข้าแผน | action เพื่อลด variance ที่เกิดแล้ว | เพิ่ม retest cycle | Preventive Action |
| Closing Evidence | หลักฐานการปิดงาน | acceptance, handover, owner, lessons learned | Handover to IT Operations | Closing meeting |

## 19. สรุปหนึ่งหน้า

5 Process Groups คือ Initiating, Planning, Executing, Monitoring & Controlling และ Closing

Process Groups ไม่ใช่ Project Phases; phase คือช่วง lifecycle ส่วน Process Group คือกลุ่มกิจกรรมบริหาร

PM มืออาชีพใช้ Process Groups เพื่อรู้ว่าต้องใช้โหมดบริหารใด ไม่ใช่เพื่อพิสูจน์ว่า “ผ่านขั้นนี้แล้วห้ามย้อน”

ERP ที่ data ownership ยังไม่พร้อมอาจต้องให้บางงาน execute ต่อได้ แต่ data workstream ต้องกลับไป planning พร้อม evidence และ decision owner

Lifecycle and Process Group Map ต้องมี gates, evidence, feedback triggers, owner, closing และ transition เพื่อใช้ต่อใน Lesson 04

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | Project vs Operation Analysis and Value Chain from Lesson 02 |
| Output | Lifecycle and Process Group Map |
| Creator | Learner in Project Planner role |
| Artifact owner | Project Manager |
| Reviewer | PMO and Workstream Leads |
| Approval authority | Project Manager with Sponsor acknowledgement |
| Minimum acceptance | Usable |
| Next lesson use | Lesson 04 ใช้ management activities, decision gates และ feedback loops เพื่อทำ PM Coverage and Cross-impact Map |

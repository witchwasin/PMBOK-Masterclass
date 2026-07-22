---
chapter: lesson-11
title: Project Resource Management
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-11/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 11 — Project Resource Management

## 1. Opening Scenario

ERP ต้องใช้ 80 key users เพื่อทำ UAT แต่ finance และ warehouse ยังต้องปิดงบและดูแลงานประจำตามปกติ Resource plan มีรายชื่อครบ แต่เมื่อถึงเวลาจริง key users ว่างแค่บางช่วง บางคนไม่มี backfill และ functional managers ไม่เคย sign off capacity

นี่คือเหตุผลที่ชื่อคนในแผนไม่เท่ากับ resource ที่พร้อมใช้งาน

Resource Management คือการทำให้บทบาท คน skill capacity authority และ physical resources พร้อมจริงในเวลาที่ project ต้องใช้

## 2. Why This Matters

แผนที่ดีที่สุดยังล้มได้ถ้าคนที่ต้องทำงานไม่ว่าง ไม่มีทักษะ ไม่มีอำนาจตัดสินใจ หรือถูกดึงไปทำงานประจำในช่วง critical

หลายโครงการดูเหมือนมีคนพอใน spreadsheet เพราะทุก task มีชื่อ แต่ชีวิตจริงคนเดียวกันอยู่หลายโครงการ มี BAU duties และไม่มีเวลาพอสำหรับ testing, review หรือ acceptance

PM จึงต้องบริหาร resource ในฐานะข้อจำกัดจริงของ delivery ไม่ใช่ช่องใน template

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. แยก role, person, assignment และ capacity
2. ใช้ RACI เพื่อกำหนด Responsible, Accountable, Consulted และ Informed
3. ประเมิน availability, skill, workload และ ramp-up risk
4. ตัดสินใจ resource gap ด้วย options และ authority ที่ถูกต้อง
5. สร้าง Consolidated Resource Plan, Organization Chart และ RACI

## 4. Beginner Safety

Resource ไม่ใช่เฉพาะคน แต่รวมถึงเครื่องมือ test environment devices licenses meeting rooms และ vendor capacity

RACI ที่ดีควรมี Accountable หนึ่งคนต่อ decision สำคัญ ไม่ใช่ใส่หลายคนเพื่อให้ทุกฝ่ายรู้สึกมีส่วนร่วม เพราะ Accountable หลายคนมักแปลว่าไม่มีใครรับผิดชอบสุดท้ายจริง

PM รวม resource plan ได้ แต่ functional manager เป็นคน commit departmental capacity ส่วน Steering Committee ควรเข้ามาเมื่อมี priority conflict หรือ exception ที่เกินอำนาจปกติ

## 5. Mental Model

```text
Quality Workload
-> Roles and Skills
-> Capacity Commitment
-> RACI
-> Resource Calendar / Histogram
-> Conflict Decision
-> Communication Audiences
```

Lesson 10 บอกว่าต้องมี quality work อะไร Lesson 11 ถามต่อว่าใครจะทำงานนั้น มีเวลาไหม มี skill ไหม และใครตัดสินใจ acceptance

## 6. Main Lesson

Role คือบทบาท เช่น Data Owner, Key User, QA Lead หรือ Release Manager Person คือคนจริงที่รับ role นั้น Assignment คือการมอบหมายงาน ส่วน Capacity คือเวลาหรือกำลังทำงานที่ใช้ได้จริง

RACI ช่วยทำให้ decision clarity:

- Responsible คือคนลงมือทำ
- Accountable คือคนรับผิดชอบผลลัพธ์หรือ decision สุดท้าย
- Consulted คือคนที่ต้องให้ input
- Informed คือคนที่ต้องรับรู้ผล

Resource Calendar แสดง availability ตามเวลา Resource Histogram แสดง demand/load เทียบกับ capacity เมื่อเห็น peak หรือ overload PM จึงเริ่มคุยเรื่อง backfill, overtime, vendor support, training, resequence หรือ scope trade-off ได้ด้วยหลักฐาน

## 7. PM Thinking

เมื่อเจอ resource conflict ให้ถาม:

- gap คือ role, skill, person, capacity หรือ authority
- คนที่ถูก assign ว่างจริงกี่เปอร์เซ็นต์และช่วงใด
- functional manager commit แล้วหรือยัง
- capacity gap กระทบ schedule, quality และ acceptance อย่างไร
- มี backfill หรือ vendor support ได้หรือไม่
- RACI มี Accountable ซ้ำหรือขาดหรือไม่
- ควร escalate เฉพาะ priority conflict ใด

อย่ารีบพูดว่า "เพิ่มคน" เพราะคนเพิ่มโดยไม่มี skill หรือไม่เข้าใจ context อาจเพิ่ม coordination cost มากกว่าช่วยงาน

## 8. PM Decision Thinking

```text
Decision: resource gap นี้ต้อง acquire, reassign, train, backfill, outsource, reduce scope หรือ replan
Owner: PM จัด resource plan; Functional Manager/Sponsor ตัดสิน capacity และ priority conflict
Inputs: RACI, resource calendar, skill matrix, workload, quality plan, schedule, budget, team performance
Options: dedicate, part-time, phased UAT, backfill, overtime, vendor support, defer, scope trade-off
Trade-offs: speed vs ramp-up, expert bottleneck vs quality, team morale vs overtime, cost vs capacity
Evidence: capacity sign-off, resource histogram, RACI approval, updated schedule and decision log
```

PM ที่ดีไม่ขอ resource แบบทั่วไป แต่ขอ capacity ที่เชื่อมกับงานและช่วงเวลาที่ต้องใช้

## 9. ERP Worked Example

ERP มี 80 key users ที่ต้องทำงานคู่กับ BAU ใน finance, sales, warehouse, production และ HR

ถ้า UAT ต้องใช้ 80 key-user test-days แต่ finance month-end close ซ้อนกัน PM ต้องทำให้เห็น workload และ impact อย่างเป็นรูปธรรม

ทางเลือกอาจเป็น:

- phased UAT ตาม module หรือ process
- backfill งานประจำช่วง UAT
- ขอ key users บางกลุ่ม dedicated 50% ใน 4 สัปดาห์
- เพิ่ม vendor support สำหรับ test preparation
- เลื่อน UAT wave ที่กระทบ month-end มากที่สุด

แต่ capacity commitment ต้องมาจาก functional managers ไม่ใช่ PM สั่งเอง

## 10. Hotel Booking Example or Contrast

Hotel Booking ใช้ cross-functional team เช่น Product, UX, Mobile, Web, Backend, QA, DevOps, Marketing, Hotel Operation และ Support

เมื่อ payment defect ใช้ backend และ QA capacity มาก ทีมอาจต้องจำกัด WIP หยุด promotion feature ชั่วคราว หรือเพิ่ม regression testing ก่อน launch

การบริหาร resource ใน Agile environment ไม่ได้แปลว่าไม่มี planning แต่แปลว่าต้องดู flow, bottleneck และ team capacity บ่อยขึ้น

## 11. Watch PM Think

ลำดับคิด:

1. เริ่มจากงานที่ต้องส่งมอบและ quality workload
2. ระบุ role และ skill ที่จำเป็น
3. ตรวจ person assignment และ capacity จริง
4. ทำ RACI ให้ decision owner ชัด
5. หา overload ด้วย calendar/histogram
6. เสนอ options พร้อม cost/schedule/quality impact
7. บันทึก capacity sign-off และ escalation decision

ถ้า RACI ไม่มี Accountable หรือ capacity ไม่มี sign-off resource plan ยังไม่ usable

## 12. Artifact Example

Artifact ของบทนี้คือ:

- Consolidated Resource Plan
- Organization Chart
- RACI
- Capacity Commitment and Exception Log

ใช้ template ต้นทางได้ที่ [Resource Artifact Template](../../../lessons/lesson-11/learner/Artifact-Template.md)

Artifact นี้ส่งต่อ Lesson 12 เพราะ communication plan ต้องรู้ว่าใครเป็น audience ใครต้องตัดสินใจ ใครต้องให้ input และ escalation path อยู่ที่ไหน

## 13. Workshop

ERP UAT Capacity Decision: key users 80 คนมี BAU duties และยังไม่มี backfill cost ให้สร้าง resource decision brief:

- role/resource gap
- RACI impact
- capacity evidence
- options เช่น phased UAT, backfill, overtime, vendor support หรือ reschedule
- owner และ authority
- exception ที่ต้องส่ง Steering Committee

ข้อจำกัด: PM cannot approve a functional department's resource commitment

## 14. Beginner Checkpoint

1. Role ต่างจาก person อย่างไร
2. Capacity commitment ต้องอนุมัติโดยใคร
3. RACI ทำไมควรมี Accountable หนึ่งคน
4. Resource histogram ใช้ตัดสินใจอย่างไร
5. ควร escalate เรื่องใดไป Steering Committee

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่าง

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย role, person, assignment, capacity, RACI, resource calendar และ resource histogram

### B. Scenario Question

ERP finance key users ไม่ว่าง UAT เพราะ month-end close ให้เสนอ resource options และ authority ที่ถูกต้อง

### C. Decision Case

Hotel Booking QA/backend ไม่พอเพราะ payment defect ให้ปรับ flow, WIP, release scope หรือ resource plan อย่างไร

### D. Artifact Construction

สร้าง Consolidated Resource Plan, Organization Chart และ RACI จาก quality/test workload

### E. Artifact Review

ตรวจ resource plan ที่มีชื่อคนครบแต่ไม่มี capacity, skill, authority หรือ sign-off แล้วแก้ให้ usable

### F. Reflection

เขียนไม่เกิน 180 คำว่า resource conflict ที่ดีควรถูก escalate อย่างไรโดยไม่โยนทุกเรื่องให้ Steering Committee

Assessment นี้เน้น resource-plan artifact review 35%, trade-off 35%, conflict/leadership case 20% และ recall 10%

## 16. เก็บตกท้ายบท

ประโยคที่ควรจำ:

```text
มีชื่อในแผนไม่ได้แปลว่ามี capacity
มี capacity ไม่ได้แปลว่ามี authority
และมี authority ไม่ได้แปลว่ามี skill
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| ใส่ชื่อคนครบคือมี resource | ต้องมี capacity, skill และ authority |
| PM อนุมัติ capacity แผนกได้เอง | Functional Manager ต้อง commit |
| RACI คือเอกสาร HR | RACI คือ decision clarity |
| เพิ่มคนแก้ทุกอย่าง | อาจเพิ่ม ramp-up และ coordination load |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Resource Management | บริหารทรัพยากร | ทำให้คน/สิ่งของพร้อมใช้งาน |
| RACI | ตารางบทบาท | Responsible, Accountable, Consulted, Informed |
| Capacity | กำลังทำงานจริง | เวลาและพลังงานที่ใช้ได้ |
| Resource Calendar | ปฏิทินทรัพยากร | availability ตามเวลา |
| Resource Histogram | แผนภาพโหลดทรัพยากร | demand/capacity ตามช่วงเวลา |
| Backfill | คนทดแทนงานประจำ | ลด BAU impact |

## 19. สรุปหนึ่งหน้า

Resource Management ทำให้แผนกลายเป็นงานจริงผ่านคน skill capacity และ authority

PM ต้องเห็น bottleneck ก่อนกลายเป็น delay และต้องแยก capacity commitment จากรายชื่อคนในแผน

RACI ไม่ใช่เอกสาร HR แต่เป็นเครื่องมือทำให้ decision owner ชัดและสื่อสารต่อใน Lesson 12 ได้ถูกคน

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | Quality and acceptance evidence from Lesson 10 |
| Output | Consolidated Resource Plan, Organization Chart and RACI |
| Owner | PM |
| Approval | PM for consolidated plan; Functional Managers for capacity; Steering Committee for exceptions |
| Next lesson use | Lesson 12 ใช้ approved RACI, audiences, accountable roles และ escalation path เพื่อสร้าง Communication Plan |


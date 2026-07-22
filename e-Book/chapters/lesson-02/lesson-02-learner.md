---
chapter: lesson-02
title: Project Management Overview
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-02/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 02 — Project Management Overview

## 1. Opening Scenario

งานทุกอย่างมีวันเริ่มและวันจบของรอบงานได้ แต่ไม่ได้แปลว่างานทุกอย่างเป็น Project

Finance ปิดบัญชีทุกเดือน มี deadline ชัดเจน แต่โดยธรรมชาติแล้วเป็น Operation เพราะเกิดซ้ำและต้องรักษาคุณภาพอย่างต่อเนื่อง

ทีมโรงแรมอัปเดตราคาและห้องว่างทุกวัน มีรอบการทำงานชัดเจน แต่ก็เป็น Operation เพราะเป็นงานประจำที่รักษาระบบบริการให้เดินต่อ

ในทางกลับกัน การเปลี่ยน ERP ทั้งองค์กร หรือการสร้าง Direct Booking Platform ใหม่ เป็น Project เพราะเป็นความพยายามชั่วคราวเพื่อสร้างผลลัพธ์เฉพาะตัวและเปลี่ยน capability ขององค์กร

คำถามเปิดบทนี้คือ:

```text
งานทุกอย่างที่มีวันเริ่มต้นและวันสิ้นสุด เป็น Project ทั้งหมดหรือไม่
```

คำตอบสั้นคือ ไม่ใช่ และการแยกให้ถูกมีผลต่อ governance, funding, owner, success measure และวิธีบริหาร

## 2. Why This Matters

Project มีลักษณะ temporary และ unique คือมีขอบเขตเวลาชัดและสร้าง product, service, result หรือการเปลี่ยนแปลงที่เฉพาะตัว ส่วน Operation คือการดำเนินงานซ้ำต่อเนื่องเพื่อรักษาธุรกิจ

ถ้าองค์กรใช้วิธีบริหารผิดประเภท ผลเสียเกิดได้สองทาง

ทางแรกคือเอาวิธีบริหาร Operation ไปครอบ Project ที่ยังมีความไม่แน่นอนสูง เช่น digital product ใหม่ แล้วบังคับให้ทุกอย่างนิ่งเหมือน SOP ทำให้ทีมเรียนรู้จากผู้ใช้ช้า

ทางที่สองคือเอาวิธีบริหาร Project ไปครอบงานประจำ เช่น ตั้ง steering meeting และเอกสาร project หนา ๆ ให้กับงานที่ควรบริหารด้วย SLA หรือ continuous improvement แทน

ปัญหาที่สามสำคัญที่สุด: ทีมส่งมอบ output เสร็จ แต่ไม่เกิด value เพราะไม่มี transition, operation owner หรือ benefit measure หลังส่งมอบ

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. แยก Project, Operation และ transitional work ได้
2. อธิบายว่า deadline ไม่ใช่เกณฑ์เดียวในการตัดสินว่างานเป็น Project
3. สร้าง Value Chain จาก Business Need ถึง Business Value ได้
4. แยก Output, Outcome, Benefit และ Business Value พร้อม measure/owner ได้
5. อธิบายว่า Functional, Matrix และ Projectized organization มีผลต่ออำนาจ PM อย่างไร
6. สร้าง Project vs Operation Analysis and Value Chain เพื่อส่งต่อ Lesson 03

## 4. Beginner Safety

คุณควรรู้จาก Lesson 01 แล้วว่า PMBOK เป็น framework ไม่ใช่ checklist และ Output ไม่เท่ากับ Value

บทนี้ยังไม่ต้องจำ 5 Process Groups, WBS, schedule network, EVM, risk register หรือ Scrum events รายละเอียดเหล่านั้นจะมาในบทถัด ๆ ไป

ระวังกับดักสำหรับผู้เริ่มต้น:

- ใช้ขนาดงานหรืองบเป็นตัวตัดสินว่าเป็น Project
- คิดว่างานที่มี deadline ต้องเป็น Project เสมอ
- เรียก Go-live ว่า Outcome
- คิดว่า PM ต้องมีอำนาจสั่งทุกคนโดยตรงจึงจะทำงานได้

## 5. Mental Model

ให้ใช้ Value Chain เป็นภาพจำหลัก

```text
Business Need
-> Business Case
-> Project
-> Work
-> Output
-> Outcome
-> Benefit
-> Business Value
-> Transition to Operation
```

บทนี้เพิ่มจาก Lesson 01 อีกหนึ่งชั้น: ไม่ใช่แค่แยก output/outcome/value แต่ต้องถามด้วยว่างานส่วนใดเป็น Project งานส่วนใดเป็น Operation และจุดใดคือ transition ที่ความรับผิดชอบย้ายจาก project team ไปยัง operation owner

## 6. Main Lesson

### Project คืออะไร

Project คือความพยายามชั่วคราวเพื่อสร้าง product, service, result หรือการเปลี่ยนแปลงที่เฉพาะตัว

คำว่า temporary ไม่ได้แปลว่าสั้น โครงการ ERP อาจใช้เวลาประมาณ 12 เดือน ส่วน Hotel Booking Platform อาจใช้เวลาประมาณ 8 เดือน ทั้งสองยังเป็น Project เพราะมีจุดเริ่ม จุดจบ และผลลัพธ์เฉพาะตัว

คำว่า unique ไม่ได้แปลว่าไม่เคยมีใครทำมาก่อน แต่หมายถึงบริบทนี้มีความเฉพาะ เช่น องค์กรนี้ ระบบเดิมนี้ stakeholder ชุดนี้ budget นี้ timeline นี้ และ outcome นี้

### Operation คืออะไร

Operation คือการดำเนินงานต่อเนื่องเพื่อรักษาธุรกิจให้ทำงานได้ เช่น monthly close, daily booking support, incident handling, rate updates หรือ routine reporting

Operation อาจมี deadline และ KPI ได้ แต่ยังไม่ใช่ Project หากธรรมชาติของงานคือทำซ้ำและรักษาบริการ

### Transitional work คืออะไร

Transitional work คือช่วงที่ project output ถูกส่งต่อเข้า operation เช่น hypercare, training handover, support model setup, owner acceptance และ benefits review

ส่วนนี้มักเป็นช่องว่างอันตราย เพราะทีม project คิดว่าส่งของเสร็จแล้ว ส่วน operation ยังไม่พร้อมรับผิดชอบเต็มตัว

### PM ทำอะไรจริง

PM ไม่ได้มีหน้าที่ตามงานอย่างเดียว แต่ต้องเป็นคนเชื่อม decision, owner, evidence และ trade-off

PM ที่ดีจะไม่ถามแค่ “งานเสร็จไหม” แต่ถามว่า:

- งานนี้ควรบริหารเป็น Project, Operation หรือทั้งสองส่วน
- ใครเป็น sponsor, benefit owner และ operation owner
- Output นี้จะสร้าง outcome ผ่านพฤติกรรมหรือ process ใด
- Measure ใดพิสูจน์ว่า benefit เกิดจริง
- ถ้า organization เป็น matrix PM ต้องใช้ escalation และ resource commitment อย่างไร

### โครงสร้างองค์กรมีผลต่ออำนาจ PM อย่างไร

Functional Organization คือองค์กรตามสายงานปกติ ไม่มีตำแหน่ง PM เต็มเวลา งานโครงการถูกดูแลโดย functional manager เป็นหลัก คนที่ทำหน้าที่ PM จึงมีอำนาจตรงน้อย ต้องใช้ influence และอาศัย sponsor ช่วยผลักดัน priority

Matrix Organization แบ่งอำนาจระหว่าง PM และ functional manager โดยมี weak matrix ที่ PM มีอำนาจน้อยใกล้เคียง functional, balanced matrix ที่แชร์อำนาจใกล้เคียงกัน และ strong matrix ที่ PM มีอำนาจมากขึ้นแต่ resource ยังสังกัด functional manager เช่น ERP ที่ key users และ IT ยังขึ้นกับหัวหน้าสายงานเดิมแม้ PM จะสั่งงานประจำวันได้

Projectized Organization จัดทีมเป็น dedicated project team ที่รายงานตรงต่อ PM ทำให้ PM มีอำนาจ resource สูงสุดและตัดสินใจเร็วกว่า แต่ต้องแลกกับ cost ที่สูงขึ้นและทีมอาจขาดการพัฒนาสายอาชีพเชิงลึกแบบ functional home

ไม่มีโครงสร้างใดดีที่สุดเสมอ PM ต้องอ่านโครงสร้างองค์กรก่อนวางแผน authority, escalation path และ resource commitment ที่เป็นจริง ไม่ใช่ที่อยากให้เป็น

## 7. PM Thinking

ใช้ 3-question decision filter นี้เมื่อเจองานใหม่

```text
Question 1: งานนี้คือ Project, Operation หรือทั้งสองส่วน
Question 2: Output, Outcome, Benefit และ Value คืออะไร
Question 3: โครงสร้างองค์กรให้ authority และ resource commitment แก่ PM แค่ไหน
```

ถ้าตอบข้อ 1 ผิด governance ก็ผิดตาม ถ้าตอบข้อ 2 ไม่ชัด status report จะปน delivery กับ value ถ้าตอบข้อ 3 ไม่จริง resource plan จะสวยบนกระดาษแต่ใช้งานไม่ได้

## 8. PM Decision Thinking

ตัวอย่าง decision สำหรับ ERP:

```text
Decision: จะจัด "ลดเวลาปิดงบ" เป็น operational improvement, ERP project หรือ portfolio ที่มีทั้งสองส่วน
Owner: Sponsor และ business owner; PM เสนอ analysis
Inputs: uniqueness, duration, cross-functional dependency, baseline 15 วัน, cost of delay, key-user capacity
Options: แก้รายงานเฉพาะหน้า, เริ่ม ERP เต็ม scope, หรือทำ improvement คู่กับ ERP
Trade-offs: quick fix เร็วแต่ไม่แก้ root cause; ERP สร้าง capability แต่ใช้เวลาและ change effort
Risk: ตัดสินจาก deadline โดยไม่ตั้ง outcome owner
Evidence: business case, outcome KPI, resource commitment, transition plan
Next action: บันทึก classification และ review benefit หลัง go-live
```

Decision ที่ดีไม่ต้องเลือกคำตอบที่ใหญ่ที่สุดเสมอ แต่ต้องชี้ให้เห็นว่าตัวเลือกแต่ละแบบแก้ปัญหาใด ไม่แก้ปัญหาใด และใครรับผิดชอบผลลัพธ์

## 9. ERP Worked Example

ใน ERP Transformation ของ SIG การปิดบัญชีประจำเดือนเป็น Operation เพราะเกิดซ้ำและเป็นงานธุรกิจต่อเนื่อง

การออกแบบ ERP, migrate ข้อมูลจาก 6 legacy systems, สร้าง integration, UAT, training, cutover และ go-live เป็น Project เพราะเป็น temporary initiative เพื่อสร้าง capability ใหม่ให้ทั้งองค์กร

การแก้รายงานชั่วคราวเพื่อช่วย CFO ในไตรมาสหน้าอาจเป็น operational improvement ที่เดินคู่กับ ERP ได้ แต่ต้องไม่ทำให้ทีมหลงคิดว่าแก้ report แล้ว root cause เรื่อง process/data ownership หายไป

Value Chain สำหรับ ERP:

| Stage | Example |
|---|---|
| Business Need | ข้อมูลไม่ตรงกันและปิดงบ 15 วัน |
| Project Output | ERP 5 modules, migrated data, trained users |
| Outcome | ผู้ใช้ทำงานบน process/data กลาง |
| Benefit | ปิดงบภายใน 5 working days |
| Business Value | ผู้บริหารตัดสินใจจากข้อมูลที่น่าเชื่อถือเร็วขึ้น |
| Transition | PM ส่งต่อให้ IT Operations และ Finance Process Owner พร้อม support/benefits review |

## 10. Hotel Booking Example or Contrast

Hotel Booking Platform ของ SHG มี Project phase ที่สร้าง website, mobile app, landing page, back office, payment integration, PMS sync และ launch capability

หลัง launch การรับ booking รายวัน, incident support, rate updates, inventory updates และ product operations เป็น Operation หรือ Product Operation

Value ไม่ได้เกิดเพราะ app อยู่ใน store แต่ต้องดูว่า direct booking เพิ่มจาก 10% ไปสู่ 35% ภายใน 18 เดือนหรือไม่ payment reliable แค่ไหน partner update inventory ทันหรือไม่ และลูกค้าจองสำเร็จจริงหรือไม่

บทเรียนสำคัญคือ digital product อาจมี project เพื่อสร้าง capability และมี operation/product operation เพื่อรักษาและพัฒนาคุณค่าหลัง launch

## 11. Watch PM Think

ดูลำดับคิดก่อนกรอก artifact

1. เริ่มจาก Business Need ไม่เริ่มจากชื่อ solution
2. แยกงานตามธรรมชาติ: temporary/unique หรือ ongoing/repetitive
3. ไม่ใช้ deadline เป็นเกณฑ์เดียว
4. หา transition point ที่ accountability ย้ายจาก project ไป operation
5. สร้าง Value Chain โดยบังคับให้แต่ละ stage มี measure และ owner
6. ตรวจว่า outcome เกิดจาก output จริงหรือเป็นแค่ assumption

ถ้าตารางของคุณมีแต่ output และไม่มี owner หลัง transition ยังไม่ควรถือว่า usable

## 12. Artifact Example

Artifact ของบทนี้คือ `Project vs Operation Analysis and Value Chain`

ใช้ template ต้นทางได้ที่ [Project vs Operation Analysis and Value Chain Template](../../../lessons/lesson-02/learner/Artifact-Template.md)

สิ่งที่ต้องมี:

- Decision context
- Work classification
- Value Chain
- Evidence gaps and governance recommendation
- Approval fields

Artifact นี้รับ input จาก PM Learning Baseline ของ Lesson 01 และจะส่งต่อ project boundary, expected value และ transition point ให้ Lesson 03

## 13. Workshop

CFO ต้องการลดเวลาปิดงบจาก 15 วันเหลือ 5 วัน มีสองข้อเสนอ: แก้รายงานรายเดือนเป็น BAU หรือทำ ERP Transformation 5 modules พร้อมปรับ process/data ownership

ให้สร้าง Project vs Operation Analysis and Value Chain หนึ่งหน้า โดย:

- แยก monthly close, temporary report fix, ERP implementation และ post-go-live support
- ระบุข้อมูลที่ยังขาดก่อนเลือก governance
- แยก Output, Outcome, Benefit และ Value
- ระบุ Sponsor, Benefit Owner และ Operation Owner
- เสนอว่าควรตั้งเป็น project, operation improvement หรือทั้งสองส่วน

ข้อจำกัด: ห้ามสรุปจาก deadline หรือขนาดงบเพียงอย่างเดียว

## 14. Beginner Checkpoint

ตอบโดยไม่เปิดเฉลย:

1. งานที่ทำซ้ำทุกเดือนแต่มี deadline เป็น Project เสมอหรือไม่
2. Project กับ Operation เชื่อมกันตรง Transition อย่างไร
3. “เปิด Mobile App” เป็น Output, Outcome หรือ Benefit
4. “Direct booking จาก 10% เป็น 35% ภายใน 18 เดือน” อยู่ระดับใด
5. Functional, Matrix และ Projectized ส่งผลต่ออำนาจ PM อย่างไร

ผ่านเมื่ออธิบาย 4 จาก 5 ข้อพร้อมเหตุผลและ owner ที่เกี่ยวข้อง

## 15. End-of-Chapter Assessment

### A. Concept Check

เลือกหรืออธิบายคำตอบสั้น ๆ เกี่ยวกับ Project, Operation, Output, Outcome, organization structure และ success measure

### B. Scenario Question

ERP มีทั้ง CFO request เพื่อปิดงบเร็วขึ้นและโครงการ ERP ระยะ 12 เดือน ให้แยกว่าเรื่องใดเป็น operation improvement เรื่องใดเป็น project และเรื่องใดต้องเป็น portfolio-level decision

### C. Decision Case

Hotel Booking launch แล้ว แต่ payment failure สูง, hotel partners update inventory ช้า และ direct booking ยังเพิ่มไม่มาก ให้แยก delivered outputs, lagging outcomes, operation issue และ follow-on improvement/project

### D. Artifact Construction

สร้าง Project vs Operation Analysis and Value Chain สำหรับ ERP หรือ Hotel Booking โดยมี measure/evidence และ accountable owner ทุก stage

### E. Artifact Review

ตรวจ classification ที่ใช้ deadline เป็นเกณฑ์เดียว แล้วแก้ให้ใช้ temporary, unique, ongoing, owner และ transition point

### F. Reflection

เขียน executive brief 5 ประโยคที่แยก business need, output, outcome, owner และ next decision

Assessment นี้เน้น retrieval 20% และ application/judgement/artifact 80%

## 16. เก็บตกท้ายบท

PM มือใหม่มักถามว่า “งานนี้ใหญ่พอจะเป็น Project ไหม” แต่คำถามที่ดีกว่าคือ “งานนี้สร้างการเปลี่ยนแปลงเฉพาะตัวหรือรักษางานประจำ”

สัญญาณเตือน:

- งานประจำถูกตั้งเป็น project ซ้ำ ๆ เพราะไม่มี owner แก้ process
- Project ถูกปิดเมื่อ output ส่งครบ แต่ operation ยังไม่พร้อม
- KPI รายงานแต่ delivery ไม่รายงาน adoption
- PM ใน matrix คิดว่าตัวเองสั่งทุก function ได้โดยไม่มี resource commitment
- Sponsor ขอ value แต่ไม่มี benefit owner

ประโยคที่ใช้ในที่ประชุม:

```text
ขอแยกก่อนว่าส่วนนี้เป็น project work, operation work หรือ transition work
แล้วค่อยกำหนด owner, measure และ governance ให้เหมาะกับธรรมชาติของงาน
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| ทุกงานที่มี deadline คือ Project | Operation ก็มี deadline ได้; ให้ดู temporary/unique กับ ongoing/repetitive |
| Go-live คือ outcome | Go-live เป็น output milestone; outcome คือการเปลี่ยนแปลงจากการใช้ output |
| Projectized organization ดีกว่าเสมอ | โครงสร้างแต่ละแบบมี trade-off เรื่อง authority, speed, expertise และ cost |
| PM คือเจ้าของ benefit คนเดียว | Sponsor, business owner และ operation owner ต้องถือ ownership หลัง handover |
| Transition คือส่งเอกสาร | Transition ต้องมี owner, support, acceptance และ benefit review |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย | ตัวอย่าง Scenario | คำที่มักสับสน |
|---|---|---|---|---|
| Project | โครงการ | งานชั่วคราวที่สร้างผลลัพธ์เฉพาะตัว | ERP implementation 5 modules | Operation |
| Operation | งานประจำ | งานต่อเนื่องที่รักษาบริการหรือกระบวนการ | Monthly close หรือ daily booking support | Project |
| Transitional Work | งานส่งต่อ | งานช่วง project ส่ง output ให้ operation รับผิดชอบ | Hypercare หลัง ERP go-live | Closing |
| Output | ผลส่งมอบ | สิ่งที่ project สร้าง | Mobile app, ERP module | Outcome |
| Outcome | ผลการเปลี่ยนแปลง | สิ่งที่เกิดเมื่อ output ถูกใช้จริง | ลูกค้าจองเองผ่าน platform | Output |
| Benefit | ประโยชน์ที่วัดได้ | ผลดีที่วัดตามเป้าหมาย | Close cycle 15 วันเหลือ 5 วัน | Business Value |
| Business Value | คุณค่าทางธุรกิจ | คุณค่าที่ช่วยเป้าหมายองค์กร | ลด OTA commission และเพิ่ม margin | Output |
| Functional Organization | องค์กรตามสายงาน | PM มีอำนาจตรงน้อย ต้องใช้ influence | Key users ยังขึ้นกับ manager เดิม | Projectized |
| Matrix Organization | องค์กรแบบแบ่งอำนาจ | PM และ functional manager แชร์อำนาจ | ERP strong matrix | Functional |
| Projectized Organization | องค์กรแบบทีมโครงการ | PM มีอำนาจ resource สูงกว่า | Dedicated product delivery team | Matrix |

## 19. สรุปหนึ่งหน้า

Project คือ temporary และ unique ส่วน Operation คือ recurring และ ongoing

Deadline, budget หรือขนาดงานไม่ใช่เกณฑ์เดียวในการเรียกงานว่า Project

Value Chain ต้องเชื่อม Business Need ไปสู่ Output, Outcome, Benefit, Business Value และ Transition to Operation

ERP implementation เป็น Project แต่ monthly close เป็น Operation ส่วน Hotel Booking launch เป็น Project output แต่ booking support หลัง launch เป็น Operation

Artifact ที่ดีต้องมี classification, measure/evidence, owner, governance recommendation และ next decision

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | PM Learning Baseline from Lesson 01; ERP and Hotel Booking scenario facts |
| Output | Project vs Operation Analysis and Value Chain |
| Creator | Learner in PM Analyst role |
| Artifact owner | Sponsor or Business Owner |
| Reviewer | Functional Owner and PM |
| Approval authority | Sponsor |
| Minimum acceptance | Usable |
| Next lesson use | Lesson 03 ใช้ project boundary, expected value และ transition point เพื่อสร้าง Lifecycle and Process Group Map |


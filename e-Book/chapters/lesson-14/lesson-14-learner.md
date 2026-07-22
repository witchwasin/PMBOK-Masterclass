---
chapter: lesson-14
title: Project Procurement Management
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-14/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 14 — Project Procurement Management

## 1. Opening Scenario

System Integrator ขอ time-and-material payment สำหรับ ERP customization ที่ scope boundary ยังไม่ชัด ทีม vendor บอกว่างานทำไปแล้ว PM ฝั่งลูกค้ากังวลว่าไม่จ่ายจะกระทบ relationship ส่วน Finance ถามว่า deliverable นี้ accept แล้วจริงหรือยัง

นี่คือจุดที่ procurement ไม่ใช่แค่การซื้อของหรือเซ็นสัญญา แต่คือการเชื่อม business need, risk allocation, acceptance และ payment authorization เข้าด้วยกัน

ถ้า project จ่ายเงินก่อน acceptance evidence โครงการอาจเสียทั้งงบและอำนาจควบคุม vendor

## 2. Why This Matters

Procurement Management ต้องทำให้สิ่งที่ซื้อจากภายนอกส่งมอบ value ตามที่ project ต้องการ ไม่ใช่แค่มี PO, contract หรือ invoice ครบ

Vendor อาจทำงานตามที่ตนเข้าใจ แต่หาก Statement of Work ไม่ชัด acceptance criteria ไม่มี หรือ change control หลวม ความขัดแย้งจะเกิดตอนจ่ายเงินและตอนส่งมอบ

บทนี้จึงพา risk จาก Lesson 13 มาแปลงเป็น make-or-buy decision, contract control และ vendor governance

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. แยก Procurement Plan, Statement of Work, Contract และ Acceptance Evidence
2. เลือก make-or-buy และ contract type จาก scope maturity/risk
3. วิเคราะห์ Fixed Price, Time and Material และ hybrid commercial trade-off
4. ควบคุม vendor change และ payment ด้วย evidence
5. สร้าง Procurement Plan, Vendor Evaluation และ Contract Control Record

## 4. Beginner Safety

Procurement Plan ไม่ใช่ contract และ contract ไม่ใช่ acceptance

Procurement Manager เป็นเจ้าของ commercial artifacts ส่วน PM เป็นเจ้าของการเชื่อม delivery และ acceptance เข้ากับ project baseline Legal/Finance อาจต้อง review terms, liability และ payment authority

คำศัพท์ใหม่คือ Make-or-Buy, SOW, Fixed Price, Time and Material, Procurement Authority, Acceptance Evidence, Commercial Risk และ Contract Control

## 5. Mental Model

```text
Business Need / Risk
-> Make-or-Buy
-> Procurement Strategy
-> Vendor Evaluation
-> Contract / SOW
-> Delivery and Acceptance Evidence
-> Payment / Change Control
```

อย่าเริ่มจาก contract type ให้เริ่มจากสิ่งที่ project ต้องการซื้อ ความชัดของ scope และ risk ที่ต้องจัดสรร

## 6. Main Lesson

Procurement Management มี 3 กระบวนการหลัก: วางแผน procurement, ดำเนินการจัดหา และควบคุม procurement

Fixed Price เหมาะเมื่อ scope ชัดและผู้ขายรับ risk เรื่องต้นทุนได้ แต่ถ้า scope ยังไม่ชัด ผู้ขายอาจเพิ่ม buffer สูงหรือเกิด dispute ภายหลัง

Time and Material เหมาะกับงานที่ยังต้องเรียนรู้หรือ scope ไม่ชัด แต่ต้องมี rate, cap, approval cadence, acceptance และ change control ไม่เช่นนั้นจะกลายเป็น open-ended spend

Hybrid contract อาจใช้ fixed price สำหรับส่วนที่ชัด และ T&M หรือ milestone-based control สำหรับส่วนที่ยังต้อง discovery

Commercial decision ที่ดีต้องเชื่อม risk allocation กับ behavior ที่ต้องการจาก vendor

## 7. PM Thinking

เมื่อเจอ vendor change/payment request ให้ถาม:

- business need และ scope boundary ชัดหรือไม่
- งานนี้อยู่ใน contract/SOW หรือเป็น change
- acceptance criteria คืออะไร
- vendor ส่ง evidence ใดแล้ว
- payment milestone ผูกกับ deliverable หรือ effort
- commercial owner และ delivery owner คือใคร
- risk ใดควรถูก transfer, share หรือ retain
- authority ตาม financial threshold อยู่ที่ใคร

PM ไม่ควรอนุมัติ payment เพราะ vendor "ทำงานแล้ว" หากยังไม่มี acceptance evidence ที่ตรงกับ contract control

## 8. PM Decision Thinking

```text
Decision: vendor request นี้ควร reject, clarify/re-price, approve controlled change หรือ accept/payment
Owner: Procurement Manager ดู commercial; PM ดู delivery/acceptance; Sponsor/Procurement Authority อนุมัติตาม threshold
Inputs: SOW, contract, scope baseline, risk register, acceptance criteria, vendor evidence, financial authority
Options: reject, clarify, renegotiate, approve change, split milestone, withhold payment pending evidence
Trade-offs: speed vs commercial control, relationship vs baseline discipline, flexibility vs cost exposure
Evidence: contract-control record, accepted deliverable, payment authorization, change log
```

Procurement decision ที่ดีไม่ใช่ทำให้ vendor หรือ project team สบายที่สุด แต่ทำให้ commercial risk และ project outcome อยู่ใน control

## 9. ERP Worked Example

ERP procurement อาจรวม ERP license, TechConsult/System Integrator, infrastructure, migration vendor และ maintenance

กรณี SI ขอ payment สำหรับ customization ที่ scope boundary ไม่ชัด คำตอบที่ดีคือ return for scope clarification ก่อน จากนั้น Procurement Manager ทำ commercial evaluation PM ตรวจ delivery/acceptance impact Legal และ Finance review หากเกี่ยวกับ terms หรือ threshold และ Sponsor อนุมัติหากเกิน procurement authority

Payment release ควรเกิดหลัง accepted deliverable และ authorization ไม่ใช่หลัง vendor ส่ง timesheet อย่างเดียว

ถ้า customization กระทบ baseline ต้องเชื่อมไป Change Control จาก Lesson 05 และ risk/issue จาก Lesson 13

## 10. Hotel Booking Example or Contrast

Hotel Booking procurement อาจเกี่ยวกับ payment gateway, cloud, SMS/email, external developer, map API และ hotel partners

Payment gateway ไม่ควรถูกเลือกจาก transaction fee อย่างเดียว ต้องดู SLA, security obligation, settlement, incident response, refund process, integration support และ launch readiness

Cloud vendor ต้องดู scalability, monitoring, data location, cost forecast และ incident support ส่วน hotel partner onboarding ต้องดู contract terms, inventory responsibility และ support workflow

## 11. Watch PM Think

ลำดับคิด:

1. เริ่มจาก need และ risk ไม่เริ่มจาก vendor preference
2. ตรวจว่า make-or-buy มี rationale หรือไม่
3. เลือก contract approach ตาม scope maturity และ risk
4. ผูก acceptance กับ payment
5. แยก commercial owner จาก delivery/acceptance owner
6. บันทึก change และ authority
7. ส่ง constraints ไป Lesson 15 หาก delivery เป็น iterative

ถ้า artifact ไม่มี acceptance/payment evidence link ยังไม่ควรปล่อย invoice ผ่าน

## 12. Artifact Example

Artifact ของบทนี้คือ:

- Procurement Plan
- Vendor Evaluation
- Contract Control Record
- Acceptance and Payment Evidence

ใช้ template ต้นทางได้ที่ [Procurement Artifact Template](../../../lessons/lesson-14/learner/Artifact-Template.md)

Artifact นี้ส่งต่อ Lesson 15 เพราะ Agile delivery ยังต้องเคารพ contract constraints, acceptance และ vendor controls

## 13. Workshop

Review ERP SI Change Request:

- scope boundary ชัดหรือไม่
- อยู่ใน SOW หรือเป็น change
- contract type/rate/cap ส่งผลอย่างไร
- acceptance condition คืออะไร
- payment evidence พอหรือไม่
- owner/authority คือใคร
- recommendation คือ reject, clarify/re-price หรือ approve controlled change

ข้อจำกัด: ห้ามใช้คำว่า vendor ทำเสร็จแล้วเป็น acceptance evidence โดยลำพัง

## 14. Beginner Checkpoint

1. Procurement Plan ต่างจาก contract อย่างไร
2. Fixed Price เหมาะกับสถานการณ์แบบใด
3. T&M ต้องมี control อะไรเพื่อไม่ให้บานปลาย
4. Vendor deliverable accept โดยใคร
5. Payment ควรถูกผูกกับ evidence ใด

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่าง

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย Procurement Plan, SOW, Contract, Fixed Price, T&M และ Acceptance Evidence

### B. Scenario Question

ERP SI ขอ T&M payment สำหรับ customization scope ไม่ชัด ให้ระบุ missing evidence และ decision path

### C. Decision Case

Hotel Booking payment gateway ควรเลือกจากปัจจัยใดนอกจากราคา และ risk ใดต้องอยู่ใน contract/SLA

### D. Artifact Construction

สร้าง Procurement Plan, Vendor Evaluation และ Contract Control Record จาก L13 risk/approved changes

### E. Artifact Review

ตรวจ procurement record ที่มี vendor invoice แต่ไม่มี accepted deliverable หรือ payment authority แล้วแก้ให้ usable

### F. Reflection

เขียนไม่เกิน 180 คำว่า contract control ช่วยลด scope/cost/risk dispute อย่างไร

Assessment นี้เน้น contract-artifact review 40%, make-or-buy trade-off 30%, supplier-risk case 20% และ recall 10%

## 16. เก็บตกท้ายบท

ประโยคที่ควรจำ:

```text
Vendor delivery ไม่เท่ากับ business acceptance
และ business acceptance ต้องเชื่อมกับ payment authorization
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Procurement Plan คือ contract | Procurement Plan วาง strategy; contract เป็น binding agreement |
| Vendor ทำงานเสร็จเท่ากับ accept | ต้องมี acceptance evidence |
| T&M ไม่มี control | ต้องมี cap, rate, evidence และ change route |
| PM owns commercial approval | Procurement/financial authority อนุมัติตาม threshold |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Make-or-Buy | ทำเองหรือซื้อ | ตัดสินใจใช้ internal หรือ vendor |
| SOW | ขอบเขตงานจัดซื้อ | งาน/ผลลัพธ์ที่ vendor ต้องส่งมอบ |
| Fixed Price | ราคาคงที่ | เหมาะกับ scope ชัด |
| Time and Material | จ่ายตามเวลา/วัสดุ | ยืดหยุ่นแต่ต้องมี control |
| Acceptance Evidence | หลักฐานตรวจรับ | พิสูจน์ว่า deliverable ผ่าน criteria |
| Procurement Authority | ผู้มีอำนาจจัดซื้อ | อนุมัติตาม financial threshold |

## 19. สรุปหนึ่งหน้า

Procurement Management เชื่อม business need, risk allocation, contract deliverable, acceptance และ payment

Fixed Price, T&M และ hybrid ไม่ได้ดีหรือแย่โดยตัวเอง ต้องเลือกจาก scope maturity, uncertainty และ risk

Lesson 14 ปิด Knowledge Areas ด้าน procurement และส่งต่อ constraints ไป Lesson 15 เพื่อใช้ Agile/flow อย่างมี governance

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | L13 risks and approved changes |
| Output | Procurement Plan, Vendor Evaluation and Contract Control Record |
| Owner | Procurement Manager for commercial artifacts; PM for delivery/acceptance linkage |
| Approval | Procurement Authority or Sponsor by financial authority |
| Next lesson use | Lesson 15 ใช้ acceptance and contract constraints เพื่อจัด backlog, flow และ feedback evidence |


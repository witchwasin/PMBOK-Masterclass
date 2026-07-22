---
chapter: lesson-09
title: Project Cost Management and Earned Value
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-09/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 09 — Project Cost Management and Earned Value

## 1. Opening Scenario

ERP ใช้ Working Budget 45 ล้านบาท และมี Total Funding Envelope 60 ล้านบาท รายงานเดือนนี้บอกว่า CPI และ SPI ต่ำกว่า 1 พร้อม Change Request เพิ่มอีก 2 ล้านบาท

ผู้บริหารบางคนอาจถามว่า "ยังมี envelope เหลืออยู่ไม่ใช่หรือ" ส่วนทีมส่งมอบอาจตอบว่า "ใช้เงินจริงยังไม่เกิน" แต่ PM ต้องแยกให้ชัดก่อนว่าเรากำลังพูดถึง funding, cost baseline, reserve, actual cost หรือ forecast

คำถามสำคัญไม่ใช่แค่ว่าเงินหมดหรือยัง แต่คือเงินและเวลาที่ใช้ไปกำลังสร้างงานที่เสร็จจริงตาม value ที่ควรได้หรือไม่

## 2. Why This Matters

Cost Management ไม่ใช่บัญชีหน้าเดียวที่ดูว่าใช้เงินไปเท่าไร แต่เป็นระบบควบคุมว่า project ใช้เงินเมื่อไร เพื่ออะไร ได้งานกลับมาเท่าไร และ forecast จบงานเป็นอย่างไร

ถ้ารายงานปน Working Budget, Funding Envelope, reserve, actual และ forecast เข้าด้วยกัน ผู้บริหารจะตัดสินใจผิดง่าย เช่นอนุมัติ change เพราะคิดว่ายังมีเงิน ทั้งที่ baseline delivery กำลังเกิน control threshold

บทนี้จึงสอนให้ PM อ่านเงินคู่กับงาน ไม่ใช่อ่านเงินแยกจากความก้าวหน้า

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. แยก estimate, budget, cost baseline, contingency reserve และ management reserve
2. อธิบาย Planned Value (PV), Earned Value (EV), Actual Cost (AC), CPI, SPI, EAC และ VAC
3. อ่าน EVM โดยเชื่อม schedule, cost และ deliverable completion
4. ตัดสินใจ cost change ด้วย benefit, forecast, authority และ baseline update
5. สร้าง Cost Estimate, Cost Baseline และ Cost Performance Forecast

## 4. Beginner Safety

อย่าเพิ่งกลัวสูตร EVM สูตรไม่ยากเท่าการตีความ สูตรจะมีประโยชน์ก็ต่อเมื่อคุณเข้าใจว่างานที่เรียกว่า "เสร็จ" วัดจาก deliverable completion ไม่ใช่ความรู้สึกของทีม

กับดักสำคัญคือเงินที่ใช้ไปน้อยไม่ได้แปลว่าประหยัด ถ้างานที่ควรเสร็จยังไม่เสร็จ และเงินที่ยังเหลือใน funding envelope ไม่ได้แปลว่า PM มีอำนาจใช้ reserve ได้เอง

## 5. Mental Model

```text
WBS + Schedule
-> Cost Estimate
-> Time-phased Cost Baseline
-> PV / EV / AC
-> Variance and Forecast
-> Cost Decision / Baseline Update
```

Lesson 08 บอกว่าเวลาใช้เมื่อไร Lesson 09 เพิ่มคำถามว่าเงินจะถูกใช้ตามเวลานั้นอย่างไร และ performance จริงเทียบกับแผนเป็นอย่างไร

## 6. Main Lesson

Estimate คือการประมาณต้นทุนของงาน Budget คือวงเงินที่ได้รับอนุมัติ Cost Baseline คือ budget ที่แบ่งตามเวลาเพื่อใช้ควบคุม performance

Contingency reserve มักเผื่อ risk ที่รู้และวางแผนไว้ ส่วน management reserve อยู่เหนือ baseline และต้องใช้ตาม governance ไม่ใช่เงินที่ PM หยิบมาใช้ได้ทันที

Earned Value Management หรือ EVM ใช้ตัวเลขหลักสามตัว:

- Planned Value (PV): มูลค่างานที่ควรเสร็จตามแผน ณ เวลานั้น
- Earned Value (EV): มูลค่างานที่เสร็จจริงตามเกณฑ์วัด
- Actual Cost (AC): เงินที่ใช้จริง

จากนั้นอ่าน:

- Cost Variance (CV) = EV - AC
- Schedule Variance (SV) = EV - PV
- Cost Performance Index (CPI) = EV / AC
- Schedule Performance Index (SPI) = EV / PV

ตัวเลขต่ำกว่า 1 ไม่ได้บอกทุกคำตอบ แต่บอกว่าต้องวิเคราะห์ cause และ forecast ต่อ

เมื่อต้อง forecast ต้นทุนจบงาน ให้ต่อยอดจาก CPI ปัจจุบัน:

- Estimate at Completion (EAC) = BAC / CPI เมื่อสมมติว่า cost performance ที่ผ่านมาจะดำเนินต่อไปในลักษณะเดิม
- Variance at Completion (VAC) = BAC - EAC บอกว่าเมื่อจบโครงการ ต้นทุนจะสูงหรือต่ำกว่า budget ที่ตั้งไว้เท่าไร

VAC ติดลบแปลว่าโครงการมีแนวโน้มใช้เงินเกิน BAC ถ้า trend ยังเป็นแบบนี้ต่อไป PM ต้องนำตัวเลขนี้ไปเทียบกับ reserve และ funding envelope ก่อนตัดสินใจ ไม่ใช่รอให้ปัญหาชัดตอนปิดโครงการ

## 7. PM Thinking

เมื่อ cost performance แย่ ให้ถาม:

- variance มาจาก cost, schedule หรือ deliverable completion
- งานที่นับ EV มี acceptance evidence จริงหรือไม่
- variance เป็น one-time หรือ trend
- EAC มีแนวโน้มเกิน baseline หรือไม่
- reserve ใดใช้ได้ และใครอนุมัติ
- Change Request 2 ล้านบาทสร้าง benefit หรือปิด risk ใด
- ถ้าอนุมัติ ต้อง update baseline, forecast, procurement หรือ communication ใด

PM ที่ดีไม่ปกป้องตัวเลข แต่ปกป้องความจริงของ decision

## 8. PM Decision Thinking

```text
Decision: จะ approve, defer, de-scope, recover หรือ reforecast cost/change decision
Owner: PM วิเคราะห์; Sponsor, Finance หรือ Change Authority ตัดสินเมื่อเกิน threshold
Inputs: BAC, PV, EV, AC, CPI, SPI, EAC, reserve status, benefit, risk, quality evidence
Options: approve change, use contingency, defer, reduce scope, renegotiate vendor, rebaseline
Trade-offs: protect value vs protect baseline, spend now vs risk later, cost recovery vs quality impact
Evidence: executive cost brief, updated forecast, approved change log, baseline update
```

อย่าใช้ CPI/SPI เป็นคำตอบสุดท้าย ให้ใช้เป็นประตูเข้าสู่การถามต่อ

## 9. ERP Worked Example

ERP มี BAC อยู่ใน Working Budget 45 ล้านบาท ตอนนี้ PV 20, EV 15 และ AC 18 ล้านบาท

คำนวณได้:

- CV = 15 - 18 = -3 ล้านบาท
- SV = 15 - 20 = -5 ล้านบาท
- CPI = 15 / 18 = 0.83
- SPI = 15 / 20 = 0.75
- EAC = BAC / CPI = 45 / 0.83 ≈ 54.2 ล้านบาท
- VAC = BAC - EAC = 45 - 54.2 ≈ -9.2 ล้านบาท

แปลว่าโครงการใช้เงินไม่มีประสิทธิภาพและทำงานช้ากว่าแผนเมื่อเทียบกับมูลค่างานที่เสร็จจริง แต่ยังไม่ควรสรุปว่า "ต้องเพิ่มงบ" ทันที

PM ต้องถามต่อว่า EV ถูกวัดจาก deliverable ที่ผ่านจริงหรือไม่ สาเหตุเป็น data migration, defect, vendor productivity หรือ scope ambiguity และงานที่เหลือมี risk แบบเดียวกันหรือไม่

ถ้า trend ของ CPI ไม่เปลี่ยน โครงการมีแนวโน้มใช้เงินเกิน Working Budget 45 ล้านบาทไปราว 9.2 ล้านบาท ตัวเลขนี้ยังพอรับได้ภายใน Total Funding Envelope 60 ล้านบาท แต่ห้ามนำ envelope มาอ้างว่า delivery budget ยังไม่กดดัน เพราะ 60 ล้านบาทรวมขอบเขตอื่น เช่น license และ management reserve ตาม governance PM ต้องรายงาน VAC นี้ก่อนที่ trend จะกลายเป็นปัญหาจริงตอนปิดโครงการ

## 10. Hotel Booking Example or Contrast

Hotel Booking มี delivery budget 12 ล้านบาท และหลัง launch จะมี cloud/payment operating costs

ถ้า payment defect ทำให้ vendor support เพิ่ม PM ต้องแยก build cost, operating cost และ cost of delay ออกจากกัน เพราะ direct booking target 35% หลัง 18 เดือนต้องดู benefit เทียบกับ total cost of ownership ไม่ใช่ดูเฉพาะ build budget

ตัวอย่างเช่น การจ่าย vendor support เพิ่มอาจดูเหมือน cost overrun แต่ถ้าช่วยลด payment failure ก่อน launch campaign ก็อาจปกป้อง revenue และ trust ได้มากกว่า แต่ decision นี้ยังต้องมี acceptance evidence และ authority

## 11. Watch PM Think

ลำดับคิดก่อนทำ executive cost brief:

1. แยก funding, baseline, reserve, actual และ forecast
2. ตรวจว่า EV วัดจาก work completion ที่มี evidence
3. คำนวณ variance และ index
4. ถาม cause ไม่ใช่ดูตัวเลขเดียว
5. สร้าง options พร้อมผลต่อ schedule, quality และ value
6. ระบุ authority และ baseline/forecast update
7. สื่อสารเป็นภาษาผู้บริหารว่า decision ที่ต้องการคืออะไร

ถ้า report ของคุณยังบอกแค่ "ใช้เงินไปกี่เปอร์เซ็นต์" ยังไม่พอสำหรับ Cost Management

## 12. Artifact Example

Artifact ของบทนี้คือ Cost Artifact Pack:

- Funding Context
- Cost Estimate
- Time-phased Cost Baseline
- Performance and Forecast
- Approval record

ใช้ template ต้นทางได้ที่ [Cost Artifact Pack](../../../lessons/lesson-09/learner/Artifact-Template.md)

Artifact นี้จะส่งต่อ Lesson 10 เพราะ quality effort ต้องใช้เวลาและเงิน หาก cost pressure ทำให้ลด testing โดยไม่มี decision โครงการอาจดูประหยัดแต่เพิ่ม external failure cost หลัง go-live

## 13. Workshop

วิเคราะห์ ERP ที่มี PV 20, EV 15, AC 18 ล้านบาท และ Change Request 2 ล้านบาท

ให้เขียน executive brief หนึ่งหน้า:

- แยก Working Budget 45 ล้านบาท และ Total Funding Envelope 60 ล้านบาท
- คำนวณ CV, SV, CPI, SPI
- ระบุ cause ที่ต้องตรวจเพิ่ม
- สร้าง options approve/defer/de-scope/recover
- ระบุ authority, reserve implication และ baseline/forecast updates

ข้อจำกัด: ห้ามสรุปจาก AC อย่างเดียว และห้ามใช้ funding envelope เพื่อเลี่ยง governance

## 14. Beginner Checkpoint

1. Estimate ต่างจาก budget อย่างไร
2. Cost baseline ต่างจาก funding envelope อย่างไร
3. PV, EV และ AC ใช้ตอบคำถามใด
4. CPI/SPI ต่ำกว่า 1 หมายถึงอะไร
5. PM ใช้ management reserve เองได้หรือไม่

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่าง

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย estimate, budget, baseline, reserve, PV, EV, AC, CPI, SPI, EAC และ VAC

### B. Scenario Question

ERP CPI/SPI ต่ำกว่า 1 ให้ตีความ performance และระบุข้อมูลที่ต้องตรวจเพิ่มก่อนเสนอ decision

### C. Decision Case

Change Request 2 ล้านบาทควร approve, defer หรือ de-scope อย่างไร โดยอ้าง benefit, forecast และ authority

### D. Artifact Construction

สร้าง Cost Estimate, Cost Baseline และ Cost Performance Forecast จาก WBS/Schedule

### E. Artifact Review

ตรวจ cost report ที่ปน funding envelope, working budget, reserve, actual และ forecast แล้วแก้ให้ decision-ready

### F. Reflection

เขียนไม่เกิน 180 คำว่า EVM ช่วยให้ PM อ่าน performance ดีกว่าการดูเงินที่จ่ายไปอย่างเดียวอย่างไร

Assessment นี้เน้น EVM/change decision 40%, artifact construction 30%, artifact review 20% และ recall 10%

## 16. เก็บตกท้ายบท

ประโยคที่ควรจำ:

```text
เงินที่เหลือไม่ได้แปลว่างานดี และเงินที่ใช้ไปไม่ได้แปลว่างานเสร็จ
ต้องอ่านเงินคู่กับ earned value และ forecast เสมอ
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| ใช้เงินน้อยคือดีเสมอ | ต้องเทียบกับ EV และ schedule |
| Funding envelope คือ budget baseline | ต้องแยก funding, reserve และ baseline |
| CPI/SPI ตอบทุกอย่าง | ต้องดู cause, forecast, quality และ risk |
| PM ใช้ reserve ได้ทันที | ต้องดู governance authority |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Estimate | ประมาณการ | คาดต้นทุนงาน |
| Cost Baseline | ฐานควบคุมต้นทุน | งบที่แบ่งตามเวลาเพื่อควบคุม |
| BAC | Budget at Completion | งบรวมตาม baseline |
| PV | Planned Value | มูลค่างานที่ควรเสร็จตามแผน |
| EV | Earned Value | มูลค่างานที่เสร็จจริง |
| AC | Actual Cost | เงินที่ใช้จริง |
| CPI | Cost Performance Index | ประสิทธิภาพต้นทุน |
| SPI | Schedule Performance Index | ประสิทธิภาพเวลา |
| EAC | Estimate at Completion | forecast ต้นทุนจบงาน = BAC / CPI |
| VAC | Variance at Completion | ส่วนต่างงบกับ forecast จบงาน = BAC - EAC |

## 19. สรุปหนึ่งหน้า

Cost Management ทำให้ project อ่านเงิน เวลา และงานที่เสร็จจริงพร้อมกัน

EVM ไม่ใช่สูตรเพื่อโชว์ความซับซ้อน แต่เป็นเครื่องมือถามว่า performance ที่เห็นสะท้อนความจริงหรือไม่

ERP ต้องแยก Working Budget 45 ล้านบาทจาก Total Funding Envelope 60 ล้านบาทเสมอ ส่วน Hotel Booking ต้องแยก build cost จาก operating cost หลัง launch

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Inputs | WBS and Master Schedule |
| Output | Cost Estimate, Cost Baseline and Cost Performance Forecast |
| Owner | PM |
| Approval | Sponsor/Finance/Change Authority ตาม threshold |
| Next lesson use | Lesson 10 ใช้ cost constraints และ schedule gates วาง prevention, testing และ acceptance effort |


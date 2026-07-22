---
chapter: lesson-10
title: Project Quality Management
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-10/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 10 — Project Quality Management

## 1. Opening Scenario

ERP UAT dashboard เป็นสีเขียว แต่เมื่อ PM ถามลึกลงไป กลับพบว่า dashboard ไม่แสดง requirement coverage, defect severity, retest result, data reconciliation หรือ signed business acceptance

ทีมเทคนิคมั่นใจว่า "จำนวน defect เหลือน้อย" Sponsor อยาก go-live ตามกำหนด และผู้ใช้บางกลุ่มยังไม่ได้ทดสอบ scenario สำคัญจริง ๆ

คำถามของบทนี้คือ สีเขียวพอหรือไม่ คำตอบคือไม่พอ ถ้าสีเขียวนั้นไม่ได้เชื่อมกลับไปยัง requirement, test result และ acceptance authority

## 2. Why This Matters

Quality Management ทำให้ project ไม่ได้ส่งมอบแค่ของที่เสร็จ แต่ส่งมอบของที่ตรง requirement และใช้งานได้จริง

โครงการที่ตรงเวลาและไม่เกินงบยังล้มเหลวได้ หากหลัง go-live ผู้ใช้ปิดบัญชีไม่ได้ ลูกค้าจ่ายเงินไม่ได้ หรือ operation ต้องเปิด war room ทุกวันเพื่อแก้ปัญหาที่ควรถูกป้องกันตั้งแต่ design/testing

คุณภาพจึงไม่ใช่เรื่องของ tester ปลายทางเท่านั้น แต่เป็น decision ทางธุรกิจว่าระดับ defect, residual risk และ readiness ใดรับได้ก่อน release

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. แยกคุณภาพ (Quality) ออกจากเกรดหรือระดับความหรูของฟีเจอร์ (Grade)
2. แยกการประกันคุณภาพ (Quality Assurance: QA), การควบคุมคุณภาพ (Quality Control: QC) และ Cost of Quality
3. กำหนด acceptance criteria และ quality gates ที่ trace กับ scope/value
4. ตัดสินใจ go/no-go เมื่อ defect กระทบ release readiness
5. สร้าง Quality Plan, Acceptance Criteria และ Test Strategy เพื่อส่งต่อ Lesson 11

## 4. Beginner Safety

Quality ไม่ได้แปลว่า feature เยอะ ระบบราคาแพง หรือหน้าตาสวยกว่า competitor เสมอไป ระบบที่เรียบง่ายแต่ทำสิ่งสำคัญถูกต้อง เสถียร และผู้ใช้ทำงานจริงได้ อาจมี quality สูงกว่าระบบใหญ่ที่ล่มเมื่อใช้งานจริง

กับดักสำคัญคือใช้จำนวน defect รวมเป็นคำตอบสุดท้าย Defect 20 รายการที่เป็น cosmetic อาจน่ากังวลน้อยกว่า defect เดียวที่ทำให้ payment fail หรือ finance close ผิด

คำศัพท์ใหม่คือ Quality, Grade, QA, QC, Cost of Quality, Acceptance Criteria, Defect Severity, Residual Risk และ Go/No-go

## 5. Mental Model

```text
Requirement / WBS
-> Quality Objective
-> Acceptance Criteria
-> QA / Prevention
-> QC / Test Result
-> Defect and Residual Risk
-> Acceptance / Go-No-Go
```

คุณภาพที่ดีเริ่มตั้งแต่ requirement ไม่ใช่เริ่มเมื่อ tester พบ defect

## 6. Main Lesson

Plan Quality Management คือการกำหนดมาตรฐานคุณภาพ เกณฑ์วัด threshold และ acceptance criteria ตั้งแต่ต้น

Manage Quality หรือ QA คือการดูว่ากระบวนการทำงานช่วยป้องกันปัญหาหรือไม่ เช่น design review, data migration checklist, test readiness gate, root-cause review และ process improvement

Control Quality หรือ QC คือการตรวจผลลัพธ์จริง เช่น test execution, defect log, inspection, reconciliation result และ acceptance evidence

Cost of Quality แบ่งเป็นต้นทุนเพื่อทำให้ถูก เช่น prevention/appraisal และต้นทุนของการทำผิด เช่น rework, incident, customer complaint, lost trust หรือ external failure หลัง go-live

บทเรียนที่ต้องจำคือ QA ป้องกัน QC ตรวจ และ Business Owner ตัดสิน acceptance ตาม criteria ทั้งสามอย่างไม่แทนกัน

## 7. PM Thinking

เมื่อเจอ quality gap PM ควรถาม:

- Requirement ใดได้รับผลกระทบ
- Acceptance criteria คืออะไร
- Defect severity กระทบ value, compliance, user trust หรือ safety แค่ไหน
- มี retest และ regression evidence หรือยัง
- Environment และ data พร้อมจริงหรือไม่
- Residual risk เหลืออะไร และใครมี authority ยอมรับ
- ถ้า go-live ต้องมี workaround, rollback และ support readiness อย่างไร

การตอบว่า "เหลือ defect น้อย" จึงยังไม่ใช่ quality decision หากไม่รู้ severity และ business impact

## 8. PM Decision Thinking

```text
Decision: defect หรือ quality gap นี้ block go-live, accept with workaround, defer หรือ require rework
Owner: PM และ Quality Lead วิเคราะห์; Business Owner/Sponsor ตัดสินเมื่อกระทบ acceptance หรือ release risk
Inputs: requirements, acceptance criteria, test results, severity, retest, regression, data/environment readiness, support readiness
Options: fix now, defer, disable feature, workaround, extend testing, rollback, change acceptance criteria
Trade-offs: go-live speed vs failure cost, workaround vs user trust, quality vs grade, prevention cost vs external failure cost
Evidence: coverage matrix, defect trend, reconciliation result, readiness checklist, signed acceptance
```

คำตอบที่มืออาชีพต้องไม่ใช้ dashboard colour เป็นหลักฐานเดียว

## 9. ERP Worked Example

ERP ต้องย้ายข้อมูลจาก 6 legacy systems และผ่าน SIT/UAT ก่อน go-live

สมมติ finance close process มี master data defect คำถามไม่ใช่ว่า defect นี้มีแค่ 1 รายการหรือไม่ แต่คือ defect นี้กระทบบัญชี audit และความน่าเชื่อถือของข้อมูลผู้บริหารหรือไม่

PM ต้องขอหลักฐานอย่างน้อย:

- requirement/test coverage
- severity and ageing
- retest/regression result
- data reconciliation
- key-user participation
- signed business acceptance
- residual-risk decision หากยังมี known issue

ถ้า UAT sign-off เป็นพิธี แต่ key users ไม่ทดสอบ scenario สำคัญจริง quality evidence ยังไม่พอ

## 10. Hotel Booking Example or Contrast

Hotel Booking ต้องให้ลูกค้าค้นหา เลือกห้อง จอง และชำระเงินได้เชื่อถือได้ เพื่อเพิ่ม direct booking

ถ้า beta พบ payment failure 8% ก่อน launch campaign นี่ไม่ใช่เพียง technical defect แต่เป็น risk ต่อ revenue, customer trust, partner confidence และ support load

PM/PO ต้องดู payment reliability, load test, rollback plan, customer message, hotel partner readiness, incident communication และ support playbook ก่อนเสนอ go/no-go

ฟีเจอร์ promotion อาจดูดี แต่ถ้า checkout ยังไม่เสถียร quality decision ต้องปกป้องเส้นทาง booking หลักก่อน

## 11. Watch PM Think

ลำดับคิดของ PM:

1. เริ่มจาก requirement และ value ที่ต้องปกป้อง
2. แปลงเป็น quality objective และ acceptance criteria
3. แยก QA activity ที่ป้องกันปัญหาออกจาก QC result ที่ตรวจพบ
4. Trace requirement ไป test result และ acceptance
5. อ่าน defect จาก severity และ user impact
6. ระบุ residual risk และ owner
7. เตรียม go/no-go recommendation พร้อม evidence

ถ้า artifact ยังไม่มี requirement-to-test-to-acceptance traceability ถือว่ายังไม่พร้อมใช้เป็น release evidence

## 12. Artifact Example

Artifact ของบทนี้คือ Quality Artifact Pack:

- Quality Objectives
- Prevention, QA and QC activities
- Acceptance Criteria
- Test Strategy
- Residual-risk acceptance
- Approval record

ใช้ template ต้นทางได้ที่ [Quality Artifact Pack](../../../lessons/lesson-10/learner/Artifact-Template.md)

Artifact นี้ส่งต่อ Lesson 11 เพราะ quality ที่ดีต้องใช้คน เวลา skill test environment และ approval responsibility ที่ชัดเจน

## 13. Workshop

ตรวจ ERP UAT dashboard สีเขียวที่ไม่มี coverage/evidence ให้สร้าง quality release decision หนึ่งหน้า:

- missing evidence
- requirement-to-test-to-acceptance trace
- defect severity และ affected value
- go/no-go options
- residual risk
- authority และ next action

ข้อจำกัด: ห้ามใช้จำนวน defect รวม หรือสี dashboard เป็น decision เพียงอย่างเดียว

## 14. Beginner Checkpoint

1. Quality ต่างจาก Grade อย่างไร
2. QA ต่างจาก QC อย่างไร
3. Acceptance criteria ควร trace กับอะไร
4. Defect severity สำคัญกว่าจำนวนรวมอย่างไร
5. Residual risk ใครควรยอมรับ

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่าง

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย Quality, Grade, QA, QC, Cost of Quality, Acceptance Criteria และ Residual Risk

### B. Scenario Question

ERP UAT dashboard เป็นสีเขียวแต่ไม่มี coverage/evidence ให้ระบุสิ่งที่ขาดก่อน go-live decision

### C. Decision Case

Hotel Booking payment failure 8% ก่อน launch campaign ให้เสนอ fix/defer/workaround/no-go พร้อม trade-off

### D. Artifact Construction

สร้าง Quality Plan, Acceptance Criteria และ Test Strategy จาก scope, schedule และ cost constraints

### E. Artifact Review

ตรวจ quality report ที่มี defect count แต่ไม่มี severity, retest, data readiness หรือ acceptance แล้วแก้ให้ decision-ready

### F. Reflection

เขียนไม่เกิน 180 คำว่า prevention cost อาจถูกกว่า external failure cost อย่างไรในโครงการจริง

Assessment นี้เน้น ERP UAT go/no-go 40%, artifact construction 30%, artifact review 20% และ retrieval 10%

## 16. เก็บตกท้ายบท

ประโยคที่ควรจำ:

```text
Quality ไม่ใช่สีเขียวบน dashboard
Quality คือหลักฐานว่าผลงานตรง requirement และใช้งานได้จริง
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Quality คือ feature เยอะ | Quality คือตรง requirement และใช้งานได้จริง |
| Tester รับผิดชอบ quality คนเดียว | Quality เป็นความรับผิดชอบร่วมตั้งแต่ requirement |
| Defect count รวมพอแล้ว | ต้องดู severity, impact, age และ retest |
| UAT sign-off เป็นพิธี | ต้องมี acceptance evidence |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Quality | คุณภาพ | ตรงข้อกำหนดและใช้งานได้จริง |
| Grade | ระดับ/เกรด | ระดับ feature หรือความหรู |
| QA | การประกันคุณภาพ | ดูกระบวนการป้องกัน defect |
| QC | การควบคุมคุณภาพ | ตรวจ deliverable/result |
| Acceptance Criteria | เกณฑ์ตรวจรับ | เงื่อนไขที่บอกว่าผ่านหรือไม่ |
| Defect Severity | ความรุนแรงของ defect | ผลกระทบต่อ value/user/risk |
| Residual Risk | ความเสี่ยงคงเหลือ | risk หลัง mitigation |

## 19. สรุปหนึ่งหน้า

Quality Management ทำให้ผลงานตรง requirement ใช้งานได้จริง และไม่ย้ายต้นทุนไปหลังส่งมอบ

QA ป้องกันปัญหาด้วย process ส่วน QC ตรวจผลลัพธ์จริง Business Owner ตัดสิน acceptance ด้วย evidence

Go-live ที่ดีต้องมอง coverage, severity, retest, readiness, residual risk และ support ไม่ใช่แค่ defect count หรือสี dashboard

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Inputs | Scope/WBS, Schedule Gates and Cost Constraints |
| Output | Quality Plan, Acceptance Criteria and Test Strategy |
| Owner | Quality Manager and PM |
| Approval | Business Owner for acceptance; Sponsor/Steering Committee for release risk |
| Next lesson use | Lesson 11 ใช้ quality roles, test workload และ approval responsibilities เพื่อสร้าง Resource Plan และ RACI |


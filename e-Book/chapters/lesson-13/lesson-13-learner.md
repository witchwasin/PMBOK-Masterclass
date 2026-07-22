---
chapter: lesson-13
title: Project Risk Management
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-13/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 13 — Project Risk Management

## 1. Opening Scenario

ERP data migration เริ่มมีสัญญาณคุณภาพต่ำ Key users ไม่พร้อม และทีมยังบอกว่า "เดี๋ยวค่อยดูตอน UAT" ถ้ารอจนข้อมูลผิดใน UAT เรื่องนี้จะไม่ใช่ risk แล้ว แต่จะกลายเป็น issue ที่กำลังทำให้ go-live เสี่ยง

ความต่างเล็ก ๆ ระหว่าง risk กับ issue มีผลใหญ่กับวิธีบริหาร เพราะ risk ยังมีเวลาตอบสนองล่วงหน้า ส่วน issue ต้องแก้สิ่งที่เกิดขึ้นแล้ว

บทนี้จึงเป็นบทที่พา communication signals จาก Lesson 12 มาแปลงเป็น risk, trigger, response, owner และ escalation path ที่ใช้จริง

## 2. Why This Matters

Risk Management คือการบริหารความไม่แน่นอนอย่างมีระบบ ไม่ใช่การเขียนรายการสิ่งที่กลัวไว้ตอนเริ่มโครงการแล้วเก็บลง folder

Risk ที่ดีต้องมีเหตุการณ์ไม่แน่นอน ผลกระทบ owner trigger response และ review cadence หากขาดสิ่งเหล่านี้ risk register จะเป็นเพียงบันทึกความกังวล ไม่ใช่ระบบตัดสินใจ

PM ที่ดีไม่ได้ทำให้ risk หายไปทั้งหมด แต่ทำให้องค์กรเห็น risk เร็วพอที่จะเลือก response ที่เหมาะ ก่อนต้นทุนการแก้ปัญหาสูงขึ้น

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. แยกความเสี่ยง (Risk), ปัญหาที่เกิดแล้ว (Issue), สมมติฐาน (Assumption) และสัญญาณเตือน (Trigger)
2. เขียน risk statement ที่มี probability, impact และ owner
3. เลือก response strategy และ threshold ที่ตรวจได้
4. รู้ว่าเมื่อใดต้อง escalate หรือสร้าง Change Request
5. สร้าง Risk Register, Response Plan และ Issue Log

## 4. Beginner Safety

Risk ไม่ใช่สิ่งไม่ดีเสมอไป Risk คือความไม่แน่นอนที่อาจมีผลต่อ objective ทั้งด้านลบและด้านบวก

Issue คือสิ่งที่เกิดแล้ว เช่น defect เกิดแล้ว vendor delay แล้ว หรือ key users ไม่มาทดสอบตามแผนแล้ว ถ้าเกิดแล้ว ให้บันทึกเป็น issue และจัดการด้วย owner, action และ escalation ไม่ใช่เรียกว่า risk เพื่อให้ดูยังไม่ร้ายแรง

คำศัพท์ใหม่คือ Risk, Issue, Trigger, Probability, Impact, Risk Owner, Response, Residual Risk, Secondary Risk, Risk Appetite และ Contingency

## 5. Mental Model

```text
Uncertainty
-> Risk Statement
-> Probability / Impact
-> Trigger
-> Response and Owner
-> Monitor
-> Issue / Escalation / Change Request if triggered
```

บทนี้คือการสร้างสายส่งจาก early warning ไปสู่ decision ไม่ใช่การทำ risk register ให้ดูครบช่อง

## 6. Main Lesson

Risk Management มี 7 กระบวนการหลัก: วางแผนบริหาร risk ระบุ risk วิเคราะห์เชิงคุณภาพ วิเคราะห์เชิงปริมาณ วางแผน response ดำเนิน response และ monitor risks

Risk statement ควรเขียนให้เห็น cause, event และ impact เช่น "หาก data cleansing ไม่เสร็จก่อน migration rehearsal จะทำให้ UAT ใช้ข้อมูลไม่เสถียรและเพิ่ม risk ต่อ go-live"

Risk response สำหรับ threat ได้แก่ avoid, mitigate, transfer, accept และ escalate ส่วน opportunity ได้แก่ exploit, enhance, share, accept และ escalate

Accept risk ไม่ได้แปลว่าไม่ทำอะไรเสมอไป Active acceptance อาจมี contingency reserve, trigger และ fallback plan

Risk Owner ควรเป็นคนที่มีความรู้หรืออำนาจพอจะติดตาม response ไม่ใช่ PM เป็น owner ทุก risk โดยอัตโนมัติ

## 7. PM Thinking

เมื่อเจอ red signal ให้ถาม:

- นี่เป็น risk หรือ issue
- trigger สังเกตได้ชัดหรือไม่
- probability และ impact อยู่ระดับใด
- risk owner มีอำนาจดำเนิน response หรือไม่
- response ใช้ reserve, vendor, contract หรือ change control หรือไม่
- residual risk เหลืออะไรหลัง response
- เมื่อ trigger เกิด ต้อง escalate ไปที่ใคร

PM ต้องระวัง risk ที่เขียนกว้างเกินไป เช่น "ทีมไม่พร้อม" เพราะไม่รู้ว่าจะ monitor อย่างไร ให้แตกเป็น risk ที่มี trigger เช่น key users ยืนยัน availability ต่ำกว่า 60% ภายในวันที่กำหนด

## 8. PM Decision Thinking

```text
Decision: risk นี้ควร monitor, mitigate, transfer, accept, escalate หรือแปลงเป็น issue/change
Owner: Risk Owner รับผิดชอบ response; PM ดู integration; governance body ตัดสินเมื่อเกิน threshold
Inputs: risk statement, trigger, probability, impact, response cost, reserve, deadline, dependency
Options: early action, contingency, fallback, transfer to vendor/contract, accept with trigger, escalate
Trade-offs: spend prevention now vs pay recovery later, speed vs certainty, local fix vs baseline change
Evidence: risk register, review minutes, response status, issue log, Change Request ID
```

คำตอบที่ดีต้องบอกว่า "เมื่อไร" risk จะเปลี่ยนสถานะ และ "ใคร" ต้องทำอะไรเมื่อ trigger เกิด

## 9. ERP Worked Example

ERP data migration risk สูงและ key users ไม่พร้อม ตัวอย่าง risk statement:

```text
หาก data cleansing ของ legacy systems สำคัญไม่ผ่าน threshold ก่อน migration rehearsal
UAT จะใช้ข้อมูลที่ไม่น่าเชื่อถือ ทำให้ defect เพิ่มและ go-live ก่อน 1 ตุลาคมเสี่ยง
```

Trigger อาจเป็น data error rate เกิน 3%, reconciliation ไม่ผ่าน, key-user availability ต่ำกว่า threshold หรือ migration rehearsal ไม่ครบตามวันที่กำหนด

ก่อน trigger เกิด PM อาจใช้ mitigation เช่นเพิ่ม data specialist, เพิ่ม daily data review, ขอ functional manager commit key users หรือแบ่ง migration rehearsal เป็น wave

เมื่อ trigger เกิดแล้ว ให้เปิด issue, record escalation decision และสร้าง Change Request หาก scope, schedule, budget หรือ baseline ต้องเปลี่ยน

## 10. Hotel Booking Example or Contrast

Hotel Booking มี payment gateway risk, inventory accuracy risk และ low probability-high impact security risk ก่อน launch

Payment risk อาจมี trigger เช่น payment failure rate เกิน threshold ระหว่าง beta Inventory risk อาจมี trigger เช่น hotel partner update delay เกิน SLA Security risk อาจมี trigger จาก penetration test finding ระดับ critical

Response อาจเป็น payment fallback, security review, inventory reconciliation, partner communication, incident runbook หรือ launch go/no-go gate

Digital product ต้อง monitor risk หลัง launch ต่อ เพราะ direct booking target 35% ภายใน 18 เดือนขึ้นกับ reliability, conversion และ trust ไม่ใช่แค่ launch เสร็จ

## 11. Watch PM Think

ลำดับคิดของ PM:

1. แยก fact, assumption, risk และ issue
2. เขียน risk statement ให้มี event และ impact
3. กำหนด trigger ที่มองเห็นได้
4. ตั้ง risk owner ไม่ใช่ใส่ PM ทุกช่อง
5. เลือก response strategy พร้อม cost/authority
6. ระบุ residual risk และ secondary risk
7. เชื่อม trigger ไป issue log, escalation หรือ change control

ถ้า risk register ไม่มี trigger และ owner มันยังไม่พร้อมใช้ใน meeting จริง

## 12. Artifact Example

Artifact ของบทนี้คือ:

- Risk Register
- Response Plan
- Issue Log
- Change Request IDs where needed

ใช้ template ต้นทางได้ที่ [Risk Artifact Template](../../../lessons/lesson-13/learner/Artifact-Template.md)

Artifact นี้ส่งต่อ Lesson 14 เพราะบาง risk ต้องจัดการผ่าน vendor, contract, insurance, acceptance หรือ transfer strategy

## 13. Workshop

Review risk register ที่เขียนว่า "ทีมไม่พร้อม" และ "data อาจมีปัญหา" ให้แก้เป็น actionable risks:

- risk statement
- trigger
- probability/impact
- risk owner
- response
- threshold
- residual risk
- monitoring cadence
- escalation/change path

ข้อจำกัด: ห้ามใช้ risk register แทน Change Request เมื่อกระทบ baseline

## 14. Beginner Checkpoint

1. Risk ต่างจาก issue อย่างไร
2. Trigger ที่ดีควรมีลักษณะอย่างไร
3. Risk owner ควรเป็นใคร
4. Accept risk แปลว่าไม่ต้องทำอะไรเสมอไปหรือไม่
5. เมื่อ risk กลายเป็น issue ต้องทำอะไรต่อ

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่าง

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย Risk, Issue, Trigger, Risk Owner, Residual Risk และ response strategies

### B. Scenario Question

ERP data migration risk สูง ให้เขียน risk statement, trigger, owner และ response

### C. Decision Case

Hotel Booking payment/security risk ก่อน launch ให้เลือก response strategy และ go/no-go trigger

### D. Artifact Construction

สร้าง Risk Register, Response Plan และ Issue Log จาก communication/status signals ใน Lesson 12

### E. Artifact Review

ตรวจ risk register ที่มีแต่คำกว้าง ๆ ไม่มี owner/trigger/response แล้วแก้ให้ใช้งานได้

### F. Reflection

เขียนไม่เกิน 180 คำว่า risk review ที่ดีช่วยป้องกัน issue อย่างไร

Assessment นี้เน้น risk-register artifact review 40%, ambiguous response case 30%, reserve trade-off 20% และ recall 10%

## 16. เก็บตกท้ายบท

ประโยคที่ควรจำ:

```text
Risk ที่ดีไม่ใช่แค่ถูกเขียน
แต่ต้องพร้อมใช้เมื่อ trigger เกิด
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Risk คือสิ่งไม่ดีเท่านั้น | Risk รวม threats และ opportunities |
| Risk register ทำครั้งเดียว | ต้อง update และ monitor ตลอดโครงการ |
| Risk owner คือ PM เสมอ | ควรเป็นคนที่มีความรู้/อำนาจต่อ risk นั้น |
| Accept risk คือไม่ทำอะไร | Active accept อาจรวม contingency reserve และ trigger |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Risk | ความเสี่ยง | เหตุการณ์ไม่แน่นอนที่กระทบ objective |
| Issue | ปัญหาที่เกิดแล้ว | สิ่งที่ต้องแก้หรือ escalate ตอนนี้ |
| Trigger | สัญญาณเตือน | เงื่อนไขที่บอกว่า risk ใกล้เกิด/เกิดแล้ว |
| Risk Owner | เจ้าของ risk | ผู้ติดตามและดำเนิน response |
| Mitigate | ลดความเสี่ยง | ลด probability หรือ impact |
| Transfer | โอนความเสี่ยง | ส่งบางส่วนให้ vendor/insurance/contract |
| Residual Risk | ความเสี่ยงคงเหลือ | risk หลัง response |

## 19. สรุปหนึ่งหน้า

Risk Management คือการบริหาร uncertainty ก่อนกลายเป็น issue

Risk ที่ใช้งานได้ต้องมี owner, trigger, response, threshold และ review evidence

Lesson 13 ส่งต่อ risk allocation และ change evidence ให้ Lesson 14 เพื่อบริหาร vendor/contract อย่างมีเหตุผล

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | Status signals and escalation path from Lesson 12 |
| Output | Risk Register, Response Plan and Issue Log |
| Owner | PM, Risk Owners and Issue Owners |
| Approval | PM within delegated threshold; Steering Committee/Change Authority when threshold exceeded |
| Next lesson use | Lesson 14 ใช้ risk allocation และ approved changes สำหรับ procurement/vendor control |


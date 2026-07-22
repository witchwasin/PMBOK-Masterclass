---
lesson: 10
sequence: 10.3
title: Project Quality Management — Assessment
document_type: Assessment
difficulty: Core
estimated_study_time: 75
status: Active
validation_status: Validated
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 10 — Project Quality Management
related_lessons:
  - Lesson 10 — Project Quality Management
  - Lesson 11 — Project Resource Management
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 10_3 — Assessment

## Release Assessment Structure — 100 Points

| ส่วน | งาน | คะแนน |
|---|---|---:|
| Decision Case | ERP UAT Go/No-go | 40 |
| Artifact Construction | Quality/Acceptance/Test Strategy | 30 |
| Artifact Review | Green dashboard ไม่มี coverage/evidence | 20 |
| Retrieval Check | Quality/Grade/QA/QC/Acceptance | 10 |

ส่ง [Artifact](learner/Artifact-Template.md) ก่อนเปิด [Model Answer](instructor/Model-Answer.md). ใช้ [Checklist](instructor/Review-Checklist.md) และ [Rubric](instructor/Scoring-Rubric.md); ต้อง ≥70/100 และทุกมิติอย่างน้อย `Usable`.

## Supplementary Practice Question Bank — Ungraded

### ส่วนที่ 1: Concept Check

### ข้อ 1

แก่นสำคัญของ Project Quality Management คือข้อใด?

A. เพิ่ม feature ให้มากที่สุดเท่าที่ทำได้
B. ทำให้ผลส่งมอบตรง requirement ใช้งานได้จริง และป้องกัน defect ตั้งแต่ต้น
C. ให้ tester ตรวจวันสุดท้ายก่อน go-live
D. ยอมรับ defect critical หาก schedule ยัง green

**คำตอบ:** C

### ข้อ 2

ข้อใดถูกต้องเกี่ยวกับ Tailoring?

A. ตัด Process ที่ไม่อยากทำ  
B. ปรับระดับวิธีทำโดยยังรักษาวัตถุประสงค์  
C. ใช้ได้เฉพาะ Agile  
D. ไม่ต้องมีหลักฐาน

**คำตอบ:** B

### ข้อ 3

เมื่อมี Change สิ่งแรกที่ควรทำคืออะไร?

A. ปฏิเสธ  
B. รับทันที  
C. วิเคราะห์ Purpose, Impact, Risk และ Decision Authority  
D. ให้ทีมทำก่อน

**คำตอบ:** C

### ข้อ 4

ข้อใดเป็นสัญญาณของ Process Theater?

A. Artifact ช่วยให้ Decision เร็วขึ้น  
B. Report มี Owner และ Action  
C. เอกสารมีอยู่แต่ไม่มีใครใช้  
D. Risk มี Trigger

**คำตอบ:** C

## ส่วนที่ 2: Topic Matching

อธิบายความหมายและการใช้งานของหัวข้อต่อไปนี้:

1. Plan Quality Management
2. Manage Quality
3. Control Quality
4. Quality vs Grade
5. Verification vs Validation
6. V-Model
7. SIT
8. UAT

## ส่วนที่ 3: ERP Scenario

พิจารณาประเด็น:

- Data Accuracy, Process Compliance, Integration, Performance และ Security
- แยก SIT กับ UAT
- ใช้ Severity/Priority จัดการ Defect ก่อน Go-live

ตอบ:

1. Business Need คืออะไร?
2. Decision ใดต้องเกิด?
3. ใครเป็น Owner?
4. กระทบ Scope, Schedule, Cost, Quality และ Risk อย่างไร?
5. หลักฐานใดต้องมี?
6. Outcome ที่ต้องการคืออะไร?
7. ใครรับช่วงหลัง Project?

## ส่วนที่ 4: Hotel Booking Scenario

พิจารณาประเด็น:

- Booking Accuracy, Payment Reliability, Inventory Consistency, UX, Performance และ Security
- วิเคราะห์ App ที่ไม่ล่มแต่ Conversion ต่ำ
- ทดสอบ Failure Recovery ของ Payment และ Booking Confirmation

ตอบ:

1. Customer Outcome คืออะไร?
2. Technical Dependency คืออะไร?
3. Stakeholder ใดมี Conflict?
4. Metric ใดสะท้อน Outcome?
5. Change ควรเข้า MVP หรือ Phase ถัดไป?
6. Risk หลัง Launch คืออะไร?
7. Operation พร้อมหรือไม่?

## ส่วนที่ 5: True or False

1. PM ต้องเป็น Expert ที่เก่งที่สุดทุกด้าน — **False**  
2. Artifact มีคุณค่าเมื่อช่วย Decision และ Control — **True**  
3. Tailoring คือการไม่ทำสิ่งที่ยาก — **False**  
4. Status Green ด้านเดียวแปลว่า Project Green — **False**  
5. Assumption ควรถูกบันทึกและติดตาม — **True**  
6. Knowledge Area นี้ทำงานแยกจากด้านอื่น — **False**  
7. Outcome สำคัญกว่า Activity Count — **True**  
8. Change ทุกอย่างเป็นผลเสีย — **False**

## ส่วนที่ 6: Applied Exercise

เลือกโครงการจริงและกรอก:

### Current State

สรุปสถานะปัจจุบันของโครงการเป็นข้อเท็จจริง ไม่เกิน 5 บรรทัด ระบุ baseline, delivery status, decision ที่ค้างอยู่ และ stakeholder ที่ได้รับผลกระทบ

### Problem / Opportunity

ระบุประเด็นที่ต้องตัดสินใจในภาษาธุรกิจ เช่น change request, quality gap, schedule risk, vendor issue, adoption risk หรือ opportunity ที่อาจเพิ่ม value

### Owner

ระบุ owner ที่ accountable เพียงหนึ่งคน และระบุผู้ที่ต้อง consulted/informed ตาม RACI หรือ governance

### Key Decision

เขียน decision statement หนึ่งประโยคว่า PM ต้องเสนอให้ approve, reject, defer, replan, escalate, tailor หรือ split phase/release

### Required Evidence

ระบุ evidence ขั้นต่ำที่ต้องมีก่อนตัดสินใจ เช่น baseline, impact analysis, cost/schedule forecast, risk trigger, acceptance criteria, stakeholder readiness หรือ contract clause

### Cross-Knowledge Impact

วิเคราะห์ผลกระทบอย่างน้อย 4 ด้านจาก scope, schedule, cost, quality, risk, resource, communications, stakeholder, procurement และ integration

### Risk

ระบุ risk หากตัดสินใจผิด พร้อม probability, impact, trigger และ owner

### Outcome

ระบุ outcome หรือ business value ที่ decision นี้ควรปกป้องหรือสร้างให้เกิด ไม่ใช่แค่ activity/output

### Tailoring Decision

ระบุว่าต้องเพิ่ม ลด หรือปรับ process/artifact ใดให้เหมาะกับความเสี่ยงและบริบท โดยต้องยังรักษาวัตถุประสงค์การควบคุมเดิม

## ส่วนที่ 7: Final Reflection

> หลังเรียนบทนี้ คุณจะเปลี่ยนวิธีบริหารโครงการเรื่องใดเป็นอันดับแรก และเพราะเหตุใด?

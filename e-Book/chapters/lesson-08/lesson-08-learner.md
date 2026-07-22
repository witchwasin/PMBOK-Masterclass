---
chapter: lesson-08
title: Project Schedule Management
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-08/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 08 — Project Schedule Management

## 1. Opening Scenario

ERP SIT เลื่อน 2 สัปดาห์ ทุกคนเริ่มกังวลว่า go-live ก่อน 1 ตุลาคมจะหลุด แต่เมื่อ PM ขอ schedule logic กลับพบว่าทีมมีเพียง Gantt chart ที่มีแถบสี ไม่มี dependency ชัดเจน ไม่มี float และไม่มีหลักฐานว่า UAT หรือ migration rehearsal ได้รับผลกระทบอย่างไร

ในสถานการณ์แบบนี้ คำตอบว่า "เร่งทีม" หรือ "เลื่อนทั้งแผน" ยังเร็วเกินไป เพราะ PM ยังไม่รู้ว่างานที่เลื่อนอยู่บนสายงานวิกฤตหรือไม่

บทนี้จึงไม่ใช่บทวาดตารางเวลาให้สวย แต่เป็นบทที่ใช้ WBS จาก Lesson 07 สร้างตรรกะของกิจกรรม ความสัมพันธ์ก่อนหลัง และ recovery decision ที่ป้องกันการแก้ปัญหาด้วยความรู้สึก

## 2. Why This Matters

Schedule Management คือการเปลี่ยน work packages ให้กลายเป็นกิจกรรมที่มีลำดับ เวลา owner และ baseline เพื่อใช้ forecast และควบคุม

ตารางเวลาที่ดีต้องตอบได้ว่า ถ้างานหนึ่งช้า งานใดช้าตาม งานใดมีเวลาสำรอง งานใดต้องเสร็จตรงเวลา และ recovery option ใดคุ้มค่ากับต้นทุนและความเสี่ยง

ถ้าตารางมีแค่วันที่ ทีมจะรู้ว่าอยากให้เสร็จเมื่อไร แต่ไม่รู้ว่าจะรักษาวันนั้นอย่างไร

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. อธิบายฐานควบคุมเวลา (Schedule Baseline) และความสัมพันธ์กับ WBS
2. สร้างรายการกิจกรรม (Activity List) จาก work packages
3. วิเคราะห์ dependency, float และ critical path
4. เลือก recovery option เช่น use float, crashing, fast tracking, split release หรือ rebaseline
5. สร้าง Activity List, Dependency Network และ Master Schedule เพื่อส่งต่อ Lesson 09

## 4. Beginner Safety

บทนี้ยังไม่ต้องเป็นผู้เชี่ยวชาญ critical path calculation เต็มรูปแบบ สิ่งที่ต้องทำให้ได้คือคิดอย่างมี logic ก่อนสรุปว่า delay กระทบ milestone หรือไม่

คำศัพท์ใหม่คือ Activity, Dependency, Duration Estimate, Critical Path, Float, Milestone, Schedule Baseline, Crashing และ Fast Tracking

กับดักสำคัญคือคิดว่า Gantt chart คือ schedule ทั้งหมด ในความจริง Gantt เป็นเพียงการแสดงผล ถ้าข้างหลังไม่มี dependency และ estimate basis มันเป็นภาพที่ดูมั่นใจมากกว่าหลักฐาน

## 5. Mental Model

```text
WBS Work Package
-> Activity List
-> Dependency Network
-> Duration Estimate
-> Critical Path / Float
-> Schedule Baseline
-> Forecast / Recovery Decision
```

Lesson 07 บอกว่าเราจะส่งมอบอะไร Lesson 08 ถามต่อว่าเพื่อส่งมอบสิ่งนั้น ต้องทำกิจกรรมใดก่อนหลัง ใช้เวลาประมาณเท่าไร และกิจกรรมใดห้ามพลาด

## 6. Main Lesson

Schedule Management มีงานหลักหลายชั้น เริ่มจากการนิยามกิจกรรมจาก WBS จากนั้นจัดลำดับกิจกรรม ประมาณระยะเวลา สร้าง schedule baseline และควบคุม schedule เมื่อเกิดความคลาดเคลื่อน

Dependency คือความสัมพันธ์ก่อนหลัง เช่น migration rehearsal ต้องรอ cleansed data และ configuration บางส่วนเสร็จ ส่วน UAT ต้องรอ SIT exit criteria และ test data ที่ใช้ได้

Critical Path คือสายกิจกรรมที่กำหนดระยะเวลารวมของ project ถ้ากิจกรรมบนเส้นนี้ช้า milestone ปลายทางมักช้าตาม Float คือเวลาสำรองที่กิจกรรมเลื่อนได้โดยไม่กระทบ milestone ที่กำหนด

Schedule compression มีสองวิธีที่ต้องระวัง:

- Crashing คือเพิ่มทรัพยากรเพื่อย่นเวลา เช่น เพิ่ม data cleansing team หรือ overtime แต่เพิ่มต้นทุนและ coordination risk
- Fast Tracking คือทำงานขนานที่เดิมควรทำต่อกัน เช่นเริ่ม UAT บางส่วนก่อน SIT ปิดครบ แต่เพิ่ม rework และ quality risk

Recovery ยังมีอีกสองทางเลือกที่ไม่ได้เร่งเวลาโดยตรง:

- Split Release คือแบ่งการส่งมอบเป็นรอบย่อยตาม module หรือ user group เช่น แยก UAT เป็น wave เพื่อให้บาง scope เริ่มใช้งานได้ก่อนโดยไม่ต้องรอทุกอย่างเสร็จพร้อมกัน
- Rebaseline คือขออนุมัติเปลี่ยน schedule baseline อย่างเป็นทางการเมื่อ delay เกิน tolerance ที่ float หรือ recovery วิธีอื่นรับไหว

## 7. PM Thinking

เมื่อมี delay PM ควรถาม:

- delay อยู่บน critical path หรือไม่
- float ที่เหลือมีจริงหรือเป็น assumption
- downstream dependency คืออะไร
- recovery option มี mechanism ชัดเจนหรือไม่
- กระทบงบ คุณภาพ resource และ risk ด้านใด
- baseline change ต้องให้ใครอนุมัติ
- ต้องสื่อสาร decision ต่อใครและเมื่อไร

การตอบว่า "ใช้ overtime" โดยไม่บอกว่าจะย่นกิจกรรมใดได้กี่วัน ไม่ใช่ recovery plan แต่เป็นความหวัง

## 8. PM Decision Thinking

```text
Decision: schedule delay นี้ต้อง recover within baseline, change baseline หรือ adjust scope/release
Owner: PM วิเคราะห์ schedule impact; Sponsor/Steering Committee ตัดสินเมื่อกระทบ milestone หรือ baseline
Inputs: WBS, activity list, dependency, duration estimate, critical path, float, resource availability, risk
Options: use float, resequence, crashing, fast tracking, reduce scope, split release, rebaseline
Trade-offs: speed vs cost, speed vs quality, certainty vs learning, milestone pressure vs user readiness
Evidence: updated network, recovery brief, approved baseline change where needed
```

คำตอบที่ดีต้องเห็นทั้ง schedule benefit และผลข้างเคียง เพราะบางครั้ง recovery ที่ทำให้วันไม่เลื่อนอาจทำให้ defect เพิ่มจน go-live ยังไม่พร้อมอยู่ดี

## 9. ERP Worked Example

ERP baseline: Blueprint 8 สัปดาห์, Build 12, SIT 4, UAT 4, Final Migration 2, Parallel Run 4 และ Cutover 2

เมื่อ SIT delay 2 สัปดาห์ PM ต้องไม่สรุปทันทีว่า go-live ก่อน 1 ตุลาคมหลุด แต่ต้องถามว่า delay เกิดกับ test case ใด เกี่ยวกับ migration rehearsal หรือไม่ defect retest ใช้เวลายังไง และ UAT สามารถเริ่มบางส่วนด้วย module ที่ผ่านแล้วได้หรือไม่

ถ้า data cleansing delay กระทบ migration และ UAT จริง recovery อาจเป็น:

- เพิ่ม data cleansing specialist เพื่อย่นงาน แต่กระทบ working budget 45 ล้านบาท
- แยก UAT เป็น wave ตาม module เพื่อลด waiting time
- fast-track report UAT บางส่วนพร้อม retest แต่ต้องเพิ่ม quality gate
- เสนอ rebaseline หาก risk ต่อ finance close และ cutover สูงเกิน tolerance

## 10. Hotel Booking Example or Contrast

Hotel Booking timeline 8 เดือน มี Sprint 0-12, pilot 3 โรงแรม, payment integration, beta, launch และ stabilization

ถ้า payment integration ช้า PM ไม่ควร lock launch date เพียงเพราะ marketing ต้องการ campaign ก่อน high season ต้องดู release criteria, payment reliability, rollback plan, support readiness และ partner communication

Digital product อาจยืดหยุ่นกว่า ERP ในบาง feature แต่ payment และ booking confirmation เป็นเส้นเลือดหลักของ value จึงต้องมี quality gate ชัดเจน

## 11. Watch PM Think

ลำดับคิดก่อนเสนอ recovery:

1. เปิด WBS และ Activity List ดูงานที่เกี่ยวข้อง
2. วาด dependency network แบบหยาบให้เห็นก่อนหลัง
3. ระบุเส้นที่อาจเป็น critical path
4. ตรวจ float และ assumption
5. เสนอ options อย่างน้อย 3 ทาง
6. เขียน trade-off เป็นภาษาธุรกิจ ไม่ใช่ภาษา scheduler อย่างเดียว
7. ระบุ authority หากต้องเปลี่ยน baseline

ถ้าคุณยังบอกไม่ได้ว่า option ใดย่นกิจกรรมใด แปลว่ายังไม่พร้อมเสนอ recovery

## 12. Artifact Example

Artifact ของบทนี้คือ Schedule Artifact Pack:

- Activity List
- Dependency Network
- Master Schedule
- Recovery Options
- Approval record

ใช้ template ต้นทางได้ที่ [Schedule Artifact Pack](../../../lessons/lesson-08/learner/Artifact-Template.md)

Artifact นี้จะส่งต่อ Lesson 09 เพราะ cost baseline ต้องรู้ว่าเงินและ resource ถูกใช้ตามช่วงเวลาใด

## 13. Workshop

ERP SIT delay 2 สัปดาห์ ให้สร้าง schedule recovery brief หนึ่งหน้า โดยระบุ:

- activity ที่ delay และ downstream dependency
- critical path หรือ float ที่ต้องยืนยัน
- information gaps
- 3 recovery options พร้อม cost/quality/resource/risk impact
- authority สำหรับ baseline change
- message ที่ควรส่งให้ Sponsor หรือ Steering Committee

ข้อจำกัด: ห้ามเสนอ "เพิ่มคน" หรือ "เร่งทีม" โดยไม่มี mechanism

## 14. Beginner Checkpoint

1. Activity List ได้ input จากอะไร
2. Critical path ต่างจาก milestone อย่างไร
3. Float ใช้ตัดสิน delay อย่างไร
4. Crashing ต่างจาก fast tracking อย่างไร
5. Baseline change ต้องมี evidence ใด

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่างจาก ERP หรือ Hotel Booking

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย Activity, Dependency, Critical Path, Float, Schedule Baseline, Crashing และ Fast Tracking

### B. Scenario Question

ERP SIT delay 2 สัปดาห์ ให้ระบุข้อมูลที่ต้องรู้ก่อนบอกว่า go-live หลุดหรือไม่

### C. Decision Case

Hotel Booking payment integration ช้าก่อน beta ให้เสนอ recovery option และ trade-off ต่อ launch readiness

### D. Artifact Construction

สร้าง Activity List, Dependency Network และ Master Schedule จาก WBS ของ Lesson 07

### E. Artifact Review

ตรวจ Gantt chart ที่ไม่มี dependency, owner, estimate basis หรือ baseline แล้วระบุว่า decision risk คืออะไร

### F. Reflection

เขียนไม่เกิน 180 คำว่า schedule ที่ดีช่วยให้ทีมตัดสินใจ recovery อย่างไร

Assessment นี้เน้น critical-path decision 40%, artifact construction 30%, artifact review 20% และ estimation concept check 10%

## 16. เก็บตกท้ายบท

Schedule ไม่ใช่คำสัญญาว่าอนาคตจะเป็นไปตามแผน แต่เป็นระบบเตือนเมื่ออนาคตเริ่มเปลี่ยน

ประโยคใช้ในที่ประชุม:

```text
ก่อนสรุปว่า milestone หลุด ขอให้เราดู dependency, float และ recovery option พร้อม trade-off ก่อน
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Gantt คือ schedule | Schedule ต้องมี logic, dependency, owner และ baseline |
| Delay ทุกงานเลื่อน go-live | ต้องดู critical path และ float |
| เพิ่มคนแก้ delay ได้เสมอ | อาจเพิ่ม cost, ramp-up และ coordination risk |
| Fast tracking ฟรี | เพิ่ม rework และ quality risk |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Activity List | รายการกิจกรรม | งานจาก work packages ที่ใช้จัดตาราง |
| Dependency | ความสัมพันธ์ก่อนหลัง | งานใดต้องรอหรือเชื่อมกับงานใด |
| Critical Path | สายงานวิกฤต | เส้นที่กำหนดระยะเวลา project |
| Float | เวลาสำรองของกิจกรรม | เวลาที่เลื่อนได้โดยไม่กระทบ milestone |
| Schedule Baseline | ฐานควบคุมเวลา | ตารางอนุมัติไว้ใช้เทียบจริง |
| Crashing | เร่งด้วยทรัพยากร | เพิ่มคน/เงินเพื่อลดเวลา |
| Fast Tracking | ทำงานขนาน | ซ้อนงานเพื่อประหยัดเวลาแต่เพิ่ม risk |
| Split Release | แบ่งส่งมอบเป็นรอบ | ปล่อยบาง scope ก่อนโดยไม่รอทุกอย่างเสร็จพร้อมกัน |
| Rebaseline | ปรับฐานควบคุมเวลาใหม่ | ขออนุมัติเปลี่ยน schedule baseline เมื่อ delay เกิน tolerance |

## 19. สรุปหนึ่งหน้า

Lesson 08 ใช้ WBS จาก Lesson 07 เพื่อสร้าง activity logic และ schedule baseline

Delay จะน่ากังวลมากหรือน้อยขึ้นกับ critical path, float, downstream dependency และ business milestone

Recovery ที่ดีต้องมี mechanism และ trade-off ไม่ใช่คำสั่งให้ทีม "ทำให้เร็วขึ้น"

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | WBS and WBS Dictionary |
| Output | Activity List, Dependency Network and Master Schedule |
| Owner | PM |
| Approval | Sponsor/Steering Committee for baseline changes |
| Next lesson use | Lesson 09 ใช้ time-phased activities, resource needs และ milestones เพื่อสร้าง Cost Estimate/Baseline |


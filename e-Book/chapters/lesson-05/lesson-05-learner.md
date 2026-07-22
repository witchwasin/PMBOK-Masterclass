---
chapter: lesson-05
title: Project Integration Management
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-05/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 05 — Project Integration Management

## 1. Opening Scenario

ก่อน ERP go-live 3 สัปดาห์ Finance ขอเพิ่ม multi-level approval workflow, TechConsult ต้องขอเวลาและค่าใช้จ่ายเพิ่ม, Operations กังวล data readiness และ Sponsor ยังต้องรักษาเป้าหมายธุรกิจ

ทุกฝ่ายถูกในมุมของตนเอง คำถามคือใครต้องรวมผลกระทบให้เห็นภาพเดียวและพาองค์กรตัดสินใจ

## 2. Why This Matters

Project Integration Management เชื่อม charter, plan, execution, knowledge, monitoring, change control และ closing

ถ้า PM เป็นเพียงคนเดินข่าว project จะดู green แบบผิวเผิน แต่ข้างในมี conflict ระหว่าง scope, schedule, cost, quality, risk, vendor, stakeholder และ operation readiness

บทนี้เป็นจุดเปลี่ยนจากการรู้จักองค์ประกอบของ project ไปสู่การทำหน้าที่ PM จริง เพราะ Integration คือการถือภาพรวมไว้ในมือเดียวโดยไม่ยึดอำนาจตัดสินใจทั้งหมดไว้คนเดียว PM ไม่ต้องเป็นคนตอบแทน Finance, IT, Vendor หรือ Sponsor แต่ต้องทำให้คำตอบของแต่ละฝ่ายอยู่ในรูปแบบที่องค์กรตัดสินใจได้

ถ้า Lesson 04 คือแผนที่ผลกระทบ Lesson 05 คือระบบการตัดสินใจที่จะรับมือกับผลกระทบนั้นอย่างมีวินัย

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้:

1. อธิบาย Integration Management ว่าเป็น decision integration
2. ระบุ 7 core integration processes
3. แยก Charter, Project Management Plan, Issue และ Change Request
4. วิเคราะห์ integrated change control
5. สร้าง Project Charter, Governance Map และ Change Decision Record

## 4. Beginner Safety

คุณควรรู้จาก Lesson 04 แล้วว่า change หนึ่งข้อกระทบหลาย Knowledge Areas ได้ บทนี้ยังไม่ลงลึก stakeholder analysis หรือ risk/issue operation รายละเอียด

ระวังกับดัก: Charter ไม่ใช่ Project Plan, Change Record ไม่ใช่ Issue Log และ PM ไม่ได้อนุมัติทุก change เอง

## 5. Mental Model

```text
Business Need -> Charter -> Integrated Plan -> Work
-> Monitoring Evidence -> Change Decision -> Updated Baseline
-> Closing / Transition
```

Integration คือการทำให้ “ทุกฝ่ายถูกในมุมตัวเอง” กลายเป็น “องค์กรตัดสินใจถูกในภาพรวม”

## 6. Main Lesson

Core processes:

1. Develop Project Charter
2. Develop Project Management Plan
3. Direct and Manage Project Work
4. Manage Project Knowledge
5. Monitor and Control Project Work
6. Perform Integrated Change Control
7. Close Project or Phase

Charter ให้ authority และ business direction ส่วน Project Management Plan รวม baselines และแผนย่อยเพื่อใช้บริหารจริง ไม่ใช่แค่รวมไฟล์

Issue คือปัญหาหรือเหตุการณ์ที่เกิดขึ้นแล้วและกระทบงานอยู่ตอนนี้ เช่น vendor ส่ง environment ช้า หรือ data migration เจอ defect เกินแผน ส่วน Change Request คือคำขอที่เป็นทางการเพื่อปรับ baseline หรือแผน เช่น ขยาย scope, เลื่อน milestone หรือเพิ่มงบ

Issue ทุกตัวไม่จำเป็นต้องกลายเป็น Change Request เสมอไป บาง Issue แก้ได้ภายใน tolerance ของแผนเดิมผ่าน corrective action โดยไม่ต้องเปลี่ยน baseline แต่ Issue ที่กระทบ baseline จริงต้องถูกยกระดับเป็น Change Request เพื่อผ่าน Integrated Change Control ก่อนอนุมัติ Issue Log และ Change Log จึงต้องแยกกัน ไม่ใช่ปนเป็นรายการเดียว

Integrated Change Control ต้องดู purpose, impact, options, authority, decision evidence และ baseline update

Closing ต้องรวม acceptance, knowledge transfer, contract/admin closure, open-item ownership และ transition to operation

สิ่งที่ทำให้ Integration ยากคือข้อมูลจำนวนมากไม่เคยมาพร้อมกันครบถ้วน ในเวลาที่ Finance อยากเพิ่ม workflow ทีม data อาจยังไม่ยืนยัน migration quality, vendor อาจยังไม่ส่ง estimate ที่ตรวจได้ และ Sponsor อาจยังไม่ได้เห็นทางเลือกแบบเทียบผลกระทบ PM จึงต้องแยกสิ่งที่เป็น fact, assumption, missing evidence และ decision needed ออกจากกัน

อีกจุดหนึ่งคือ Integrated Change Control ไม่ได้มีไว้เพื่อปฏิเสธ change แต่มีไว้เพื่อทำให้ change ที่ควรทำถูกอนุมัติด้วยความเข้าใจผลกระทบ และทำให้ change ที่ยังไม่ควรทำถูกเลื่อนหรือแบ่งเฟสอย่างมีเหตุผล

## 7. PM Thinking

เมื่อมี change ให้ถาม:

- change นี้ปกป้องหรือเพิ่ม business value อะไร
- กระทบ baselines ใด
- evidence ใดมีแล้วและขาดอะไร
- options คือ approve, reject, defer, split phase หรือ workaround
- decision authority อยู่ที่ใคร
- หลังตัดสินใจต้อง update plan, baseline, log และ communication ใด

## 8. PM Decision Thinking

```text
Decision: change request ควร approve, reject, defer, split phase หรือ escalate
Owner: PM ทำ impact analysis; CCB/Sponsor ตัดสินตาม governance
Inputs: charter, baselines, reports, change request, risk, quality, contract, stakeholder impact
Options: keep baseline, rebaseline, workaround, phased release, add budget/resource
Trade-offs: business value vs delivery risk, speed vs stability, local request vs enterprise outcome
Evidence: integrated impact log, decision record, updated plan, approved change
```

## 9. ERP Worked Example

ERP ของ SIG มี working budget 45 ล้านบาท, total funding envelope 60 ล้านบาท, 5 modules, TechConsult, 80 key users และ go-live target ก่อน 1 ตุลาคม

Finance ขอเพิ่ม approval workflow ก่อน go-live:

- Scope: ฟีเจอร์อยู่ใน baseline หรือไม่
- Schedule: กระทบ 1 ตุลาคมหรือไม่
- Cost/Procurement: กระทบสัญญาและ working budget หรือไม่
- Quality/Risk: manual workaround เสี่ยง audit/adoption หรือไม่
- Stakeholder: Finance ได้ value แต่ UAT/key users มี capacity จำกัด
- Decision: เสนอ approve now, defer to phase 1.1 หรือ manual workaround พร้อม control

ตัวอย่าง decision record ที่ดีอาจสรุปว่า option A คือ approve ทันทีโดยใช้งบเพิ่มและเลื่อน UAT, option B คือ defer เป็น phase 1.1 หลัง go-live พร้อม manual approval control ชั่วคราว, option C คือทำเฉพาะ approval rule ที่จำเป็นต่อ audit แล้วเก็บ workflow เต็มไว้รอบถัดไป คำแนะนำของ PM ต้องระบุว่าแต่ละ option ทำให้ baseline ใดเปลี่ยน และใครต้องอนุมัติ

## 10. Hotel Booking Example or Contrast

Marketing ขอ dynamic promotion engine ก่อน launch 2 สัปดาห์ ทั้งที่ Hotel Booking ต้องรักษา timeline 8 เดือนและ outcome direct booking 35% ใน 18 เดือน

PM ต้องดู conversion value, payment stability, high season, support readiness และ resource trade-off อาจเสนอ launch core booking พร้อม coupon workaround แล้วจัด dynamic promotion เป็น backlog หลัง stabilization

กรณีนี้ Integration ช่วยป้องกันทีม product จากการไล่ตาม feature ที่น่าสนใจแต่ทำให้ launch risk สูงขึ้น ถ้า payment path ยังไม่เสถียร การเพิ่ม promotion engine อาจเพิ่ม conversion ในกระดาษ แต่ลด conversion จริงเมื่อผู้ใช้ชำระเงินไม่สำเร็จ PM จึงต้องทำให้ทีมเห็น trade-off ระหว่าง growth idea กับ operational readiness

## 11. Watch PM Think

1. เริ่มจาก Business Need และ baselines จาก Lessons 02-04
2. แยก fact, assumption, issue และ change
3. ทำ impact analysis ข้าม Knowledge Areas
4. สร้าง options ไม่ใช่ answer เดียว
5. ระบุ decision owner และ evidence หลังอนุมัติ

สัญญาณว่า PM กำลังทำ Integration ได้ดีคือการประชุมเปลี่ยนจาก “ใครอยากได้อะไร” เป็น “ทางเลือกไหนสร้าง value มากที่สุดเมื่อเทียบกับ risk และ control ที่ต้องรักษา” และเมื่อมีมติแล้ว ทุกคนรู้ว่าต้อง update baseline, log, communication และ handoff ใดต่อ

## 12. Artifact Example

Artifact pack ของบทนี้:

- Project Charter
- Governance and Decision Rights Map
- Change Decision Record

ใช้ template ต้นทางได้ที่ [Integration Artifact Pack](../../../lessons/lesson-05/learner/Artifact-Template.md)

## 13. Workshop

SI เสนอ workflow เพิ่มมูลค่า 2 ล้านบาทและเพิ่ม UAT 3 สัปดาห์ ให้ทำ decision record ที่ระบุ baseline, options, trade-off, missing evidence, owner และ next action

## 14. Beginner Checkpoint

1. Charter ต่างจาก Project Plan อย่างไร
2. Issue ต่างจาก Change Request อย่างไร
3. Integrated Change Control ต้องดู impact ด้านใดบ้าง
4. PM เป็นคนอนุมัติทุก change หรือไม่
5. Closing ต้องมีอะไรนอกจากส่ง deliverable

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย Charter, Plan, Issue, Change และ Integrated Change Control

### B. Scenario Question

ERP approval workflow change ให้ระบุ baselines, authority, missing evidence และ options

### C. Decision Case

Hotel Booking promotion engine ก่อน launch ให้เสนอ approve/defer/split พร้อม trade-off

### D. Artifact Construction

สร้าง Charter/Governance/Change Pack โดยใช้ input จาก Lessons 02-04

### E. Artifact Review

ตรวจ Charter ที่ไม่มี Business Need/PM Authority และ Change Record ที่ไม่มี impact/options/baseline update

### F. Reflection

คุณจะเปลี่ยนวิธีจัดการ change ในโครงการจริงอย่างไร

Assessment นี้เน้น retrieval 10% และ application/judgement/artifact 90%

## 16. เก็บตกท้ายบท

Integration ที่ดีไม่ได้ทำให้ทุกคนได้สิ่งที่ต้องการ แต่ทำให้ทุกคนเห็นผลของทางเลือกก่อนตัดสินใจ

ประโยคใช้ในที่ประชุม:

```text
ขอแยก change นี้เป็น options พร้อม impact, owner, authority และ baseline update
ก่อนสรุปว่าเราจะทำทันที เลื่อน หรือแบ่ง phase
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Integration คือรวมเอกสาร | คือเชื่อม decision และ baseline |
| PM อนุมัติทุก change | Authority ต้องเป็นไปตาม governance |
| Change control ทำให้ช้าเสมอ | ลด rework และทำให้ trade-off โปร่งใส |
| Closing คือส่ง deliverable | รวม acceptance, knowledge, contract และ transition |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย | ตัวอย่าง Scenario | คำที่มักสับสน |
|---|---|---|---|---|
| Project Charter | เอกสารอนุมัติโครงการ | ให้ authority และเป้าหมายระดับสูง | ERP charter โดย Sponsor | Project Plan |
| Project Management Plan | แผนแม่บท | รวม baselines และแผนย่อย | ERP data/UAT/cutover plan | Charter |
| Governance | กลไกตัดสินใจ | ใครตัดสินใจอะไรตาม threshold | Steering Committee | Meeting |
| Decision Rights | สิทธิ์ตัดสินใจ | อำนาจ approve/reject/defer | Change Authority | Responsibility |
| Change Request | คำขอเปลี่ยนแปลง | ขอปรับ baseline/แผนอย่างเป็นทางการ | เพิ่ม approval workflow | Issue |
| Issue | ปัญหาที่เกิดแล้ว | เหตุการณ์ที่กระทบงานอยู่ตอนนี้ ไม่ใช่คำขอเปลี่ยน baseline | Vendor ส่ง environment ช้า | Change Request |
| Impact Analysis | วิเคราะห์ผลกระทบ | ดู scope/schedule/cost/risk ฯลฯ | UAT เพิ่ม 3 สัปดาห์ | Opinion |
| Baseline Update | ปรับฐานควบคุม | update หลังอนุมัติ change | schedule/cost baseline | Status update |
| Close Project or Phase | ปิดโครงการ/เฟส | acceptance, handover, lessons learned | ERP hypercare handoff | Go-live |

## 19. สรุปหนึ่งหน้า

Integration Management เชื่อม project ตั้งแต่ charter ถึง closing

PM เป็น integrator ของ decision ไม่ใช่คนเดินข่าวหรือเจ้าของคำตอบทุกด้าน

Change ที่ดีต้องมี impact, options, authority, decision evidence และ baseline update

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Inputs | Value Chain, Lifecycle Map และ Cross-impact Map |
| Outputs | Project Charter; Governance and Decision Rights Map; Change Decision Record |
| Creator | PM with BA support / PM / Change Coordinator |
| Artifact owners | Sponsor and PM ตาม artifact |
| Reviewers | PMO, Business Owner, Steering Committee, Impact Owners |
| Approval authority | Sponsor / Steering Committee Chair / Change Authority |
| Minimum acceptance | Usable |
| Next lesson use | Lesson 06 ใช้ Charter และ Governance Map เพื่อระบุ Stakeholder, influence, engagement และ approval expectations |

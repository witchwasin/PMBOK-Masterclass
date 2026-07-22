---
chapter: lesson-07
title: Project Scope Management and WBS
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-07/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 07 — Project Scope Management and WBS

## 1. Opening Scenario

CFO ขอ "รายงานบริหารทั้งหมด" ระหว่าง ERP blueprint ฟังดูเหมือนคำขอธรรมดา และหลายทีมอาจตอบทันทีว่า "ได้ครับ เดี๋ยวใส่ใน scope ให้"

แต่สำหรับ PM คำว่า "ทั้งหมด" คือสัญญาณเตือน ไม่ใช่ requirement เพราะยังไม่รู้ว่ารายงานนั้นใช้ตัดสินใจอะไร ใครเป็นผู้ใช้ ข้อมูลมาจากระบบใด ต้องถูกต้องระดับไหน และจะตรวจรับอย่างไร

ถ้า PM รับคำนี้เข้าโครงการโดยไม่ถามต่อ ทีมอาจได้งานเพิ่มจำนวนมากโดยไม่มีขอบเขตควบคุม ตารางเวลาและงบประมาณจะเริ่มเคลื่อน แต่ไม่มีใครรู้ว่าเคลื่อนเพราะ value เพิ่มจริง หรือเพราะ requirement ไม่เคยถูกนิยามให้ชัดตั้งแต่แรก

บทนี้จึงเป็นบทที่พา stakeholder need จาก Lesson 06 มาแปลงเป็น requirement, scope boundary และ Work Breakdown Structure หรือ WBS ที่นำไปวางแผนเวลา ต้นทุน และการตรวจรับได้จริง

## 2. Why This Matters

Project Scope Management ทำให้โครงการตอบคำถามพื้นฐานสามข้อ: เราจะส่งมอบอะไร เราจะไม่ส่งมอบอะไร และจะรู้ได้อย่างไรว่าสิ่งที่ส่งมอบนั้นผ่านแล้ว

ถ้าขอบเขตไม่ชัด ทุกอย่างหลังจากนั้นจะไม่นิ่ง Schedule จะกลายเป็นการเดาวันจากงานที่ยังไม่รู้ขนาด Cost จะเป็นตัวเลขที่ไม่มีฐาน Quality จะไม่มีเกณฑ์ตรวจรับ และ Change Control จะกลายเป็นการเถียงกันว่า "เรื่องนี้เคยอยู่ใน scope ตั้งแต่แรกหรือเปล่า"

Scope ที่ดีไม่ใช่เอกสารยาว แต่เป็นเส้นแบ่งที่ทีม ผู้บริหาร และผู้ใช้งานเข้าใจตรงกันพอที่จะตัดสินใจได้

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. แยกขอบเขตผลิตภัณฑ์ (Product Scope) และขอบเขตโครงการ (Project Scope)
2. อธิบายฐานควบคุมขอบเขต (Scope Baseline), WBS และ WBS Dictionary
3. ใช้กฎ 100% ของ WBS เพื่อแตกงานแบบเน้นสิ่งส่งมอบ
4. วิเคราะห์คำขอเปลี่ยน scope ด้วย baseline, impact และ authority
5. สร้าง Requirements List, Scope Statement, WBS และ WBS Dictionary เพื่อส่งต่อ Lesson 08

## 4. Beginner Safety

บทนี้ไม่ต้องแตกกิจกรรมรายวัน และยังไม่ต้องคำนวณ critical path นั่นเป็นงานของ Lesson 08

สิ่งที่ต้องตั้งหลักให้ได้ก่อนคือ WBS ไม่ใช่ task list และไม่ใช่ผังองค์กร WBS คือการแตก approved scope ออกเป็นสิ่งส่งมอบและ work packages ที่ควบคุมได้

คำศัพท์ใหม่ที่ควรรู้คือ Product Scope, Project Scope, Requirement, Scope Statement, WBS, WBS Dictionary, Validate Scope และ Control Scope

## 5. Mental Model

```text
Stakeholder Need
-> Requirement
-> Scope Boundary
-> Deliverable
-> Work Package
-> Acceptance Criteria
-> Scope Baseline
```

ลองจำภาพนี้ไว้: stakeholder พูดเป็นความต้องการ PM ช่วยแปลงเป็น requirement ที่ตรวจรับได้ จากนั้นจึงสร้าง boundary และแตกเป็น work packages

ถ้าข้ามขั้นตอนนี้ โครงการจะมีงานเต็มไปหมด แต่ไม่มีฐานให้ควบคุม

## 6. Main Lesson

Scope Management มี 6 กระบวนการหลัก ได้แก่ วางแผนการบริหารขอบเขต เก็บรวบรวม requirements นิยาม scope สร้าง WBS ตรวจรับ scope และควบคุม scope

Product Scope คือคุณสมบัติของสิ่งที่จะส่งมอบ เช่น ERP ต้องมี finance module, inventory module หรือรายงานปิดงบ Project Scope คืองานที่ต้องทำเพื่อให้สิ่งนั้นเกิดขึ้น เช่น blueprint, configuration, migration, testing, training และ cutover

Scope Baseline ประกอบด้วย Scope Statement, WBS และ WBS Dictionary

Scope Statement บอก in scope, out of scope, assumptions, constraints และ acceptance โดยรวม WBS แตกงานเป็นชั้น ๆ ให้เห็น deliverables และ work packages ส่วน WBS Dictionary เติมรายละเอียดที่ WBS diagram บอกไม่หมด เช่น owner, description, boundary, assumption, dependency และ acceptance criteria

กฎ 100% ของ WBS หมายถึง WBS ต้องครอบคลุม approved scope ทั้งหมด ไม่ใช่รวมทุกคำขอ ทุกไอเดีย หรือทุกความหวังของ stakeholder

## 7. PM Thinking

เมื่อได้คำขอใหม่ PM ไม่ควรถามแค่ว่า "ทำได้ไหม" แต่ควรถามว่า "คำขอนี้อยู่ใน baseline หรือเป็น change"

คำถามที่ควรใช้:

- คำขอนี้เชื่อมกับ business objective ใด
- Requirement วัดผลหรือตรวจรับได้หรือยัง
- ขอบเขตที่รวมและไม่รวมคืออะไร
- Work package ใดได้รับผลกระทบ
- กระทบเวลา ต้นทุน คุณภาพ ความเสี่ยง และ stakeholder ใด
- หากต้องเพิ่ม scope ใครมีอำนาจอนุมัติ
- ถ้าไม่เพิ่มตอนนี้ จะเลื่อนเป็น phase ถัดไปได้หรือไม่

คำตอบที่ดีไม่จำเป็นต้องปฏิเสธคำขอ แต่ต้องทำให้ trade-off ถูกเห็นก่อนตัดสินใจ

## 8. PM Decision Thinking

```text
Decision: คำขอใหม่นี้อยู่ใน scope baseline หรือเป็น change request
Owner: PM วิเคราะห์ผลกระทบ; Sponsor, Business Owner หรือ CCB ตัดสินตาม threshold
Inputs: requirement, scope statement, WBS, WBS dictionary, acceptance criteria, impact analysis
Options: include now, defer, replace lower-value scope, split phase, reject
Trade-offs: value เพิ่มขึ้น vs schedule/cost/quality risk
Evidence: updated scope baseline, decision record, stakeholder communication
```

PM ที่คิดแบบมืออาชีพจะไม่ตอบจากความเกรงใจ และไม่ใช้คำว่า "งานเล็ก" แทน impact analysis เพราะงานเล็กหลายชิ้นรวมกันอาจทำให้ baseline ใช้ควบคุมไม่ได้

## 9. ERP Worked Example

ERP ของ SIG มี 5 modules, data migration จาก 6 legacy systems, training, parallel run, cutover และ hypercare ส่วน CRM/BI อยู่นอก scope

Sales ขอ margin dashboard ก่อน go-live คำขอนี้อาจมี value จริง แต่ PM ต้องทำให้ชัดก่อนว่า dashboard ใช้ตัดสินใจอะไร ดึงข้อมูลจาก module ใด ต้องใช้ legacy data ที่ยังไม่ cleanse หรือไม่ และใครจะ sign off

ตัวอย่าง requirement ที่ดีขึ้น:

```text
Finance and Sales management need a monthly margin dashboard
using cleansed ERP sales/cost data for approved modules,
with reconciliation variance within accepted threshold,
reviewed by CFO delegate before UAT sign-off.
```

เมื่อ requirement ชัดแล้วจึงแตก WBS เช่น report design, data mapping, calculation rule, reconciliation, UAT, sign-off และ handover

## 10. Hotel Booking Example or Contrast

Hotel Booking MVP มี search, room selection, booking, payment และ back office เพื่อเพิ่ม direct booking จาก 10% เป็น 35% ภายใน 18 เดือน ภายใต้งบ Phase 1 12 ล้านบาทและ timeline 8 เดือน

Marketing ขอ loyalty points ก่อน launch คำถามไม่ใช่ "ฟีเจอร์นี้ดีไหม" แต่คือ "ฟีเจอร์นี้จำเป็นต่อ MVP และ high season launch หรือไม่"

ถ้า loyalty points เพิ่ม conversion สูงและใช้ effort ต่ำ อาจพิจารณา include ได้ แต่ถ้ากระทบ payment readiness หรือ partner onboarding การเลื่อนเป็น phase 2 อาจเป็น decision ที่ดีกว่า หรืออาจ replace feature ที่ value ต่ำกว่าแทนเพิ่ม scope ตรง ๆ

## 11. Watch PM Think

ลำดับคิดของ PM ในบทนี้คือ:

1. ฟัง stakeholder need โดยไม่รีบรับเป็น scope
2. แปลงคำกว้างให้เป็น requirement ที่วัดได้
3. ระบุ in scope, out of scope และ assumption
4. แตก WBS ตาม deliverable ไม่ใช่ตาม department
5. เติม WBS Dictionary ให้ work package มี owner และ acceptance
6. ส่ง impact เข้ากระบวนการตัดสินใจถ้ากระทบ baseline

ถ้า artifact ของคุณยังไม่มี out of scope หรือ acceptance criteria แปลว่ามันยังช่วยป้องกัน scope creep ได้ไม่พอ

## 12. Artifact Example

Artifact ของบทนี้คือ Scope Artifact Pack ประกอบด้วย:

- Requirements List
- Scope Statement
- WBS
- WBS Dictionary
- Approval record

ใช้ template ต้นทางได้ที่ [Scope Artifact Pack](../../../lessons/lesson-07/learner/Artifact-Template.md)

หัวใจของ artifact นี้คือทำให้ Lesson 08 สามารถแตก activities ได้ต่อ ถ้า WBS dictionary ไม่มี owner, dependency และ acceptance schedule จะเริ่มจากฐานที่อ่อนทันที

## 13. Workshop

CFO ขอ "รายงานบริหารทั้งหมด" ระหว่าง ERP blueprint ให้คุณทำงาน 4 อย่าง:

1. เขียนคำถามเพื่อแยก decision need, user, data source และ acceptance criteria
2. แปลงคำขอเป็น requirement slices อย่างน้อย 3 รายการ
3. เขียน scope boundary ว่าอะไรอยู่ในและอยู่นอก phase นี้
4. สร้าง WBS fragment พร้อม WBS Dictionary สำหรับหนึ่ง work package

ข้อจำกัด: ห้ามใช้คำว่า "ทั้งหมด" เป็น requirement และห้ามแตก WBS ตามชื่อแผนกเท่านั้น

## 14. Beginner Checkpoint

ตอบโดยไม่เปิดเฉลย:

1. Product Scope ต่างจาก Project Scope อย่างไร
2. Scope Baseline ประกอบด้วยอะไร
3. WBS ที่ดีควรแตกตามอะไร
4. WBS Dictionary ช่วย Lesson 08 อย่างไร
5. คำขอเพิ่มงานต้องผ่านหลักฐานใดก่อนตัดสินใจ

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่างจาก ERP หรือ Hotel Booking

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย Product Scope, Project Scope, Scope Baseline, WBS และ WBS Dictionary

### B. Scenario Question

ERP margin dashboard ก่อน go-live ให้ระบุ requirement gaps, in/out of scope และ acceptance criteria ที่ต้องถามเพิ่ม

### C. Decision Case

Hotel Booking loyalty points ก่อน launch ให้เสนอ include, defer, replace scope หรือ split phase พร้อม trade-off

### D. Artifact Construction

สร้าง Scope Artifact Pack โดยใช้ input จาก Charter, Stakeholder Register และ Governance Map

### E. Artifact Review

ตรวจ WBS ที่แตกตาม department/activity แล้วแก้ให้เป็น deliverable-oriented WBS

### F. Reflection

เขียนไม่เกิน 180 คำว่า scope clarity ช่วยลดปัญหา schedule/cost/quality ในโครงการจริงอย่างไร

Assessment นี้เน้น terminology 10%, artifact review 35%, decision case 35% และ cross-knowledge analysis 20%

## 16. เก็บตกท้ายบท

Scope ที่ดีไม่ได้ทำให้ stakeholder ขออะไรไม่ได้ แต่ทำให้คำขอทุกอย่างมีทางเข้าที่ถูกต้อง

ประโยคใช้ในที่ประชุม:

```text
ขอแปลงคำขอนี้เป็น requirement ที่ตรวจรับได้ก่อน
แล้วค่อยดูว่าอยู่ใน baseline หรือเป็น change request
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| WBS คือ task list | WBS คือ deliverable/work-package structure |
| Scope ชัดคือเขียนยาว | Scope ชัดคือมี boundary และ acceptance |
| รับ change ด้วยวาจาได้ถ้าเล็ก | ต้องดู baseline และ impact |
| 100% rule คือรวมทุกคำขอ | รวมเฉพาะ approved scope |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Product Scope | ขอบเขตผลิตภัณฑ์ | คุณสมบัติของสิ่งที่จะส่งมอบ |
| Project Scope | ขอบเขตโครงการ | งานที่ต้องทำเพื่อส่งมอบ product |
| Scope Baseline | ฐานควบคุมขอบเขต | Scope statement + WBS + WBS dictionary |
| WBS | โครงสร้างแบ่งงาน | แตก approved scope เป็น work packages |
| WBS Dictionary | พจนานุกรม WBS | รายละเอียด owner, boundary, acceptance |
| Validate Scope | ตรวจรับขอบเขต | ยืนยัน deliverable กับผู้มี authority |
| Control Scope | ควบคุมขอบเขต | จัดการ change ต่อ baseline |

## 19. สรุปหนึ่งหน้า

Scope Management ทำให้ project รู้ว่าจะทำอะไร ไม่ทำอะไร และตรวจรับอย่างไร

WBS ทำให้ scope กลายเป็นโครงสร้างงานที่ควบคุมได้

เมื่อมีคำขอเพิ่มงาน PM ต้องพา stakeholder ไปดู baseline, impact และ trade-off ไม่ใช่ตอบจากความเกรงใจ

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Inputs | Project Charter และ Stakeholder Register |
| Outputs | Requirements List, Scope Statement, WBS, WBS Dictionary |
| Owner | Business Process Owner and PM / PM |
| Approval | Sponsor, Business Owner, CCB ตาม threshold |
| Next lesson use | Lesson 08 ใช้ work packages, owners, acceptance criteria และ constraints เพื่อสร้าง Activity List และ Schedule |


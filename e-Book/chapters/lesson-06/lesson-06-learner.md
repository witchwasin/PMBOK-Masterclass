---
chapter: lesson-06
title: Project Stakeholder Management
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-06/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 06 — Project Stakeholder Management

## 1. Opening Scenario

ERP ของ SIG มี Sponsor, PM, TechConsult, 80 key users, 5 modules และหน่วยงานที่ได้รับผลกระทบหลายฝ่าย หลัง governance ถูกตั้งจาก Lesson 05 แล้ว คำถามถัดไปคือใครมีอิทธิพลต่อการตัดสินใจ การยอมรับระบบ และความสำเร็จจริงหลัง go-live

Stakeholder Management ไม่ใช่การทำให้ทุกคนพอใจ แต่คือการรู้ว่าใครต้องมีส่วนร่วมแบบใด เพื่อให้ project decision, adoption และ benefits เกิดขึ้นได้จริง

## 2. Why This Matters

Project Stakeholder Management ครอบคลุม identify stakeholders, plan stakeholder engagement, manage stakeholder engagement และ monitor stakeholder engagement

Project ที่มี plan ดีอาจล้มเหลวได้ถ้าผู้มีอิทธิพลไม่เข้าใจ ไม่เห็นด้วย หรือไม่ได้รับข้อมูลในเวลาที่ตัดสินใจได้

ในงานจริง stakeholder ไม่ได้มีผลต่อ project เฉพาะตอนอนุมัติเริ่มโครงการ บางคนมีผลต่อการให้ข้อมูล requirement บางคนมีผลต่อการปลด resource บางคนมีผลต่อการยอมรับผลลัพธ์หลัง go-live และบางคนไม่มีตำแหน่งสูงแต่เป็นคนที่ทีมงานเชื่อ PM ต้องเห็นอิทธิพลเหล่านี้ก่อนจะวางแผนสื่อสารหรือขอ decision

บทนี้จึงชวนมอง stakeholder เป็นระบบความสัมพันธ์ ไม่ใช่รายชื่อในตาราง

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้:

1. ระบุ stakeholder ที่มีผลต่อ decision, delivery, adoption และ benefits
2. สร้าง Stakeholder Register ที่ใช้บริหารจริง
3. ใช้ Power-Interest Grid เพื่อเลือก engagement approach
4. วิเคราะห์ current vs desired engagement
5. ออกแบบ Stakeholder Engagement Strategy ที่ผูกกับ governance และ artifact handoff

## 4. Beginner Safety

เริ่มจาก Charter และ Governance Map ของ Lesson 05 ก่อน อย่าเริ่มจากรายชื่อคนแบบลอย ๆ

ระวังกับดัก: stakeholder ไม่ใช่เฉพาะคนที่เข้าประชุม, resistance ไม่ใช่ความผิดส่วนตัวเสมอไป และ communication plan ไม่เท่ากับ engagement strategy

## 5. Mental Model

```text
Governance + Decisions
-> Stakeholders and Influence
-> Current / Desired Engagement
-> Targeted Actions
-> Adoption, Approval, Benefits
```

ถ้า Lesson 05 ตอบว่า “ใครมีสิทธิ์ตัดสินใจ” Lesson 06 จะตอบว่า “ใครต้องถูก engage เพื่อให้ decision นั้นเกิดผล”

## 6. Main Lesson

Stakeholder Management มี 4 process หลัก:

1. Identify Stakeholders
2. Plan Stakeholder Engagement
3. Manage Stakeholder Engagement
4. Monitor Stakeholder Engagement

Stakeholder Register ที่ดีไม่ใช่ contact list แต่ต้องระบุ role, interest, influence, impact, expectations, current engagement, desired engagement และ engagement owner

Power-Interest Grid ช่วยเลือกวิธี engage:

| Power | Interest | Approach |
|---|---|---|
| High | High | Manage closely |
| High | Low | Keep satisfied |
| Low | High | Keep informed |
| Low | Low | Monitor |

Engagement Strategy ต้องระบุ action, message, channel, owner, trigger และ success signal

ระดับ engagement ที่ใช้บ่อยคือ unaware, resistant, neutral, supportive และ leading สถานะเหล่านี้ไม่ใช่ป้ายตัดสินคน แต่เป็นสัญญาณให้ PM เลือกวิธีทำงาน ถ้าผู้ใช้ยัง resistant เพราะ workload เพิ่ม การส่งอีเมล update มากขึ้นอาจไม่ช่วย ต้องมี workshop เพื่อฟัง pain point ปรับ training หรือให้ Sponsor ช่วยอธิบายเหตุผลทางธุรกิจ

Communication คือการส่งและรับข้อมูลให้เข้าใจตรงกัน ส่วน engagement คือการออกแบบปฏิสัมพันธ์เพื่อให้ decision, adoption และ benefit มีโอกาสเกิดขึ้นจริง สองเรื่องนี้เชื่อมกัน แต่ไม่ใช่เรื่องเดียวกัน

## 7. PM Thinking

เมื่อวิเคราะห์ stakeholder ให้ถาม:

- stakeholder นี้มีผลต่อ approval, adoption, operations หรือ benefits ด้านใด
- เขามีอำนาจ formal หรือ informal
- current engagement เป็น unaware, resistant, neutral, supportive หรือ leading
- desired engagement ต้องเปลี่ยนไปถึงระดับใด
- action ใดควรทำก่อน decision สำคัญ
- ใครเป็นเจ้าของ engagement และใช้ช่องทางใด
- success signal คืออะไร

## 8. PM Decision Thinking

```text
Decision: ใครต้องถูก engage ก่อน approval, go-live หรือ scope baseline
Owner: PM วาง strategy; Sponsor/Business Owner ช่วย influence ในจุดที่ PM ไม่มี authority
Inputs: Charter, Governance Map, decision rights, value chain, lifecycle map, stakeholder signals
Options: inform, consult, co-create, escalate, sponsor-led intervention, change champion network
Trade-offs: speed vs buy-in, transparency vs noise, formal authority vs informal influence
Evidence: stakeholder register, engagement assessment, action log, approval expectation
```

## 9. ERP Worked Example

ERP มี Sponsor คุณสมชาย, PM คุณเอก, TechConsult, 80 key users และ 5 modules

Stakeholder groups ที่ควรมอง:

- Sponsor คุณสมชาย: high power/high interest, ต้อง clear decision และ visible sponsorship
- CFO/Finance: high impact ต่อ approval workflow, controls และ acceptance
- Warehouse/Production: high adoption impact จาก process change
- HR: affected module owner และ training/adoption channel
- IT legacy owners: dependency, data migration และ integration risk
- TechConsult: delivery partner, estimate owner, defect resolution
- Key users 80 คน: adoption, UAT evidence และ change champions

ตัวอย่าง engagement strategy: ให้ Sponsor เปิด governance decision, PM run impact workshop, module owners validate acceptance criteria, key users เข้าร่วม UAT readiness checkpoint

ถ้า warehouse lead ต่อต้านเพราะกลัว process ใหม่ทำให้งานหน้าคลังช้าลง PM ไม่ควรแปลว่า “ไม่ให้ความร่วมมือ” ทันที ควรตรวจว่า concern นี้สะท้อน quality criteria, training gap, resource constraint หรือ operational risk หรือไม่ เมื่อเข้าใจสาเหตุ PM อาจเปลี่ยน engagement จากการแจ้งกำหนด UAT เป็นการให้ warehouse ร่วมออกแบบ acceptance scenario ที่พิสูจน์ว่างานจริงไม่สะดุด

## 10. Hotel Booking Example or Contrast

Hotel Booking มี Sponsor คุณจิรา, Product Owner คุณนภา, PM คุณสุทธิ, hotel partners, customers, operations/support, marketing, finance และ payment provider

การเพิ่ม partner dashboard หรือ promotion feature ไม่ใช่แค่ scope decision เพราะ hotel partners ต้องเชื่อมั่น onboarding, customers ต้องใช้งานง่าย, operations ต้อง support ได้ และ payment provider ต้องพร้อมก่อน high season

Engagement ที่ดีอาจแยกเป็น partner pilot, support readiness review, marketing launch alignment และ payment escalation path

สำหรับ Hotel Booking ผู้ใช้ปลายทางอาจไม่อยู่ในห้องประชุม แต่เสียงของเขามาจาก click data, booking drop-off, payment failure และ support tickets ดังนั้น stakeholder engagement ใน digital product ต้องใช้ทั้งคนและ evidence จากพฤติกรรมจริง ไม่ใช่ฟังเฉพาะความเห็นของทีมภายใน

## 11. Watch PM Think

1. เริ่มจาก governance และ decision points
2. ระบุ stakeholder ตาม impact ไม่ใช่ตาม org chart เท่านั้น
3. แยก power, interest, influence และ adoption impact
4. ระบุ current vs desired engagement
5. ออกแบบ action ที่มี owner, trigger และ success signal
6. เชื่อมผลลัพธ์ไป Lesson 07 เพื่อเก็บ requirements และ scope approval

ให้สังเกตว่า stakeholder ที่สำคัญที่สุดอาจเปลี่ยนไปตามช่วง project ตอนเริ่มอาจเป็น Sponsor และ Business Owner ตอนออกแบบอาจเป็น key users ตอนทดสอบอาจเป็น QA และ operations ตอน launch อาจเป็น support และ customer-facing team PM จึงต้อง monitor engagement ไม่ใช่ทำ register ครั้งเดียวแล้วเก็บไว้

## 12. Artifact Example

Artifact ของบทนี้คือ Stakeholder Register and Engagement Strategy

ใช้ template ต้นทางได้ที่ [Stakeholder Artifact Template](../../../lessons/lesson-06/learner/Artifact-Template.md)

## 13. Workshop

ERP ต้องตัดสินใจ approval workflow ก่อน go-live ให้สร้าง stakeholder register และ engagement strategy สำหรับ Sponsor, Finance, Warehouse/Production, IT legacy owner, TechConsult และ key users

สิ่งที่ต้องส่ง:

- stakeholder role และ reason for inclusion
- power/interest classification
- current และ desired engagement
- engagement action ก่อน decision
- owner, channel, trigger และ success signal

## 14. Beginner Checkpoint

1. Stakeholder Register ต่างจาก contact list อย่างไร
2. Power-Interest Grid ช่วยเลือก engagement approach อย่างไร
3. Resistance ควรถูกมองอย่างไร
4. Sponsor มีบทบาทอะไรที่ PM ทำแทนไม่ได้
5. Lesson 06 ส่งต่ออะไรให้ Lesson 07

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย Stakeholder Register, Power-Interest Grid, current vs desired engagement และ engagement owner

### B. Scenario Question

ERP approval workflow change ให้ระบุ stakeholder ที่ต้อง engage ก่อน decision และเหตุผล

### C. Decision Case

Hotel Booking partner onboarding มี resistance จาก hotel partners ให้เสนอ engagement strategy ที่ลด adoption risk

### D. Artifact Construction

สร้าง Stakeholder Register and Engagement Strategy โดยใช้ input จาก Lesson 05

### E. Artifact Review

ตรวจ artifact ที่มีแต่ชื่อและตำแหน่ง แต่ไม่มี influence, desired engagement, action owner หรือ success signal

### F. Reflection

ในโครงการจริงของคุณ ใครเป็น stakeholder ที่มักถูกมองข้าม และผลคืออะไร

Assessment นี้เน้น retrieval 10% และ application/judgement/artifact 90%

## 16. เก็บตกท้ายบท

Stakeholder Management ที่ดีไม่ใช่การส่ง update ถี่ขึ้น แต่คือการใช้ engagement ให้ถูกคน ถูกเวลา และถูก decision

ประโยคใช้ในที่ประชุม:

```text
ก่อนตัดสินใจเรื่องนี้ เราต้องรู้ว่าใครมี influence ต่อ approval, adoption และ operation readiness
และต้อง engage เขาอย่างไรให้ decision นี้ใช้ได้จริง
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Stakeholder คือคนที่อยู่ใน meeting | คือผู้ที่มีผลหรือได้รับผลจาก project |
| Engagement คือส่ง email update | คือออกแบบ interaction เพื่อ support decision/adoption |
| Resistance เป็นปัญหาคน | มักสะท้อน risk, incentive, workload หรือ unclear value |
| Sponsor แค่เซ็นอนุมัติ | Sponsor ต้องช่วย direction, escalation และ visible support |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย | ตัวอย่าง Scenario | คำที่มักสับสน |
|---|---|---|---|---|
| Stakeholder | ผู้มีส่วนได้ส่วนเสีย | ผู้ที่มีผลหรือได้รับผลจาก project | CFO, key users, hotel partners | Attendee |
| Stakeholder Register | ทะเบียน stakeholder | บันทึก role, influence, needs และ strategy | ERP stakeholder register | Contact list |
| Power-Interest Grid | ตารางอำนาจและความสนใจ | ใช้เลือกวิธี engage | Sponsor high/high | Org chart |
| Engagement | การมีส่วนร่วม | ระดับการรับรู้ สนับสนุน หรือมีบทบาท | Supportive key user | Communication |
| Current Engagement | สถานะปัจจุบัน | ตอนนี้ stakeholder อยู่ระดับใด | Resistant warehouse lead | Opinion |
| Desired Engagement | สถานะเป้าหมาย | ต้องให้ถึงระดับใดเพื่อ project สำเร็จ | Supportive module owner | Satisfaction |
| Influence | อิทธิพล | ความสามารถในการผลักหรือขวาง decision/adoption | Informal process expert | Authority |
| Change Champion | ตัวแทนสนับสนุนการเปลี่ยนแปลง | คนช่วยนำ adoption ในหน่วยงาน | Key user lead | Trainer |

## 19. สรุปหนึ่งหน้า

Stakeholder Management ระบุ วางแผน บริหาร และ monitor engagement ของผู้มีส่วนได้ส่วนเสีย

PM ต้องออกแบบ engagement ตาม influence และ decision need ไม่ใช่ส่งข้อมูลเหมือนกันให้ทุกคน

Artifact ที่ดีต้องมี current/desired engagement, action owner, trigger และ success signal

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Inputs | Project Charter และ Governance and Decision Rights Map จาก Lesson 05 |
| Output | Stakeholder Register and Engagement Strategy |
| Creator | PM with Business Lead / Change Lead support |
| Artifact owner | PM |
| Reviewers | Sponsor, Business Owner, Change Lead, Functional Leads |
| Approval authority | Sponsor / Steering Committee for engagement strategy on critical stakeholders |
| Minimum acceptance | Usable |
| Next lesson use | Lesson 07 ใช้ stakeholder needs, decision rights, acceptance roles และ engagement signals เพื่อเก็บ requirements และ approve scope baseline |

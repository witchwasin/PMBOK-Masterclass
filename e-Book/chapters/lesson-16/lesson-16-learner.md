---
chapter: lesson-16
title: Predictive vs Agile vs Hybrid and Tailoring
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-16/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

# Chapter 16 — Predictive vs Agile vs Hybrid and Tailoring

## 1. Opening Scenario

องค์กรประกาศว่า "ทุกโครงการต้อง Agile 100%" เพราะเชื่อว่าจะเร็วขึ้น แต่เมื่อนำแนวคิดเดียวกันไปใช้กับงานที่ scope ชัด compliance สูง contract หนัก และ safety risk สูง ทีมกลับสับสน งบประมาณบาน และ governance ไม่รู้ว่าจะอนุมัติอะไรจากหลักฐานใด

อีกองค์กรหนึ่งทำตรงข้าม บังคับทุก digital product ให้วางแผนละเอียดล่วงหน้า 12 เดือน ทั้งที่ยังไม่รู้ user behavior และ conversion จริง ผลคือส่งของครบแต่ตลาดไม่ตอบรับ

บทสุดท้ายนี้จึงไม่ได้ถามว่า predictive หรือ Agile ใครดีกว่า แต่ถามว่าแต่ละส่วนของงานต้องใช้ control, feedback, cadence และ governance แบบใด

## 2. Why This Matters

Tailoring คือการเลือกและปรับวิธีบริหาร project ให้เหมาะกับ context, value, risk, complexity, stakeholder และองค์กร

Tailoring ไม่ใช่การตัดขั้นตอนที่ไม่อยากทำ และไม่ใช่การตั้งชื่อ approach ให้ดูทันสมัย เช่น "Hybrid" โดยไม่มี boundary หรือ control

PM ที่ดีต้องอธิบายได้ว่า workstream ใดใช้ predictive เพราะอะไร workstream ใดใช้ Agile เพราะอะไร trigger ใดทำให้ต้อง review approach และ governance owner คือใคร

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. แยก predictive, agile และ hybrid approach
2. ใช้ tailoring factors เช่น uncertainty, governance, risk, compliance และ team maturity
3. แยก tailoring ที่มีเหตุผลออกจากการตัด process ตามใจ
4. ออกแบบ hybrid governance by workstream
5. สร้าง Tailored Hybrid Delivery Plan เพื่อใช้ใน capstone

## 4. Beginner Safety

Predictive ไม่ได้แปลว่าล้าสมัย Agile ไม่ได้แปลว่าดีกว่าเสมอ และ Hybrid ไม่ได้แปลว่าทำอะไรก็ได้

คำศัพท์ใหม่คือ Delivery Approach, Predictive, Adaptive/Agile, Hybrid, Tailoring Rationale, Trigger, Cadence, Governance Architecture และ Adaptive Control

กับดักสำคัญคือเลือก approach จากกระแสหรือ ideology เช่น "ผู้บริหารชอบ Agile" หรือ "ทีมคุ้นกับ Waterfall" โดยไม่ดู nature ของงานจริง

## 5. Mental Model

```text
Context
-> Workstream Characteristics
-> Delivery Approach
-> Tailoring Rationale
-> Governance / Cadence / Trigger
-> Evidence
-> Review and Adapt
```

Tailoring ที่ดีไม่ใช่การเลือกครั้งเดียวแล้วจบ แต่ต้องมี trigger เพื่อทบทวนเมื่อ assumption เปลี่ยน

## 6. Main Lesson

Predictive เหมาะเมื่อ scope ชัด change cost สูง compliance/contract เข้ม และต้องใช้ baseline control เช่น construction, compliance-heavy migration, fixed vendor deliverable หรือ cutover

Agile เหมาะเมื่อ uncertainty สูง ต้องเรียนรู้จาก feedback product เปลี่ยนเร็ว และสามารถส่ง increment เป็นรอบได้ เช่น UX, digital feature, conversion experiment หรือ prototype

Hybrid เหมาะเมื่อ project หนึ่งมีหลายธรรมชาติ เช่น ERP ที่ต้อง predictive governance สำหรับ migration/cutover แต่ใช้ iterative feedback กับ configuration หรือ Hotel Booking ที่ใช้ Agile product cycles แต่ยังต้อง predictive control กับ payment/security/launch readiness

Hybrid ที่ดีต้องบอกว่า boundary อยู่ตรงไหน ใครอนุมัติอะไร cadence ใดใช้ review และ evidence ใดบอกว่า approach ยังเหมาะ

## 7. PM Thinking

เมื่อ tailor approach ให้ถาม:

- workstream ใด scope ชัดหรือยังไม่ชัด
- cost of change สูงแค่ไหน
- compliance, security, contract หรือ safety risk ต้อง control ระดับใด
- stakeholder feedback ต้องได้บ่อยแค่ไหน
- team maturity รองรับ Agile หรือ predictive discipline แค่ไหน
- trigger ใดทำให้ต้อง review approach
- governance owner และ approval authority คือใคร

ถ้าตอบคำถามเหล่านี้ไม่ได้ คำว่า Agile, Waterfall หรือ Hybrid ยังเป็น label ไม่ใช่ decision

## 8. PM Decision Thinking

```text
Decision: project/workstream นี้ควรใช้ predictive, agile หรือ hybrid approach และต้อง tailor อะไร
Owner: PM เสนอ tailoring rationale; Sponsor/Steering Committee อนุมัติเมื่อกระทบ control/risk
Inputs: requirement uncertainty, technical uncertainty, compliance, contract, stakeholder access, team maturity, release risk
Options: predictive baseline, Scrum, Kanban, hybrid by workstream, phased governance, experiment with gate
Trade-offs: predictability vs adaptability, speed vs control, documentation effort vs decision evidence
Evidence: tailoring rationale, delivery model, governance map, cadence, feedback loop, risk controls
```

คำตอบที่ดีไม่เลือก approach เดียวทั้ง project หากงานแต่ละส่วนมีธรรมชาติต่างกัน

## 9. ERP Worked Example

ERP เหมาะกับ hybrid delivery by workstream

Predictive governance ใช้กับ master schedule, budget, procurement, data migration, cutover, compliance และ executive gates เพราะ failure cost สูงและต้องมี baseline control

Iterative practice ใช้กับ configuration feedback, dashboard/report prototype, defect Kanban และ user walkthrough เพราะต้องเรียนรู้ว่า process fit กับผู้ใช้จริงหรือไม่

Trigger ที่ควรตั้ง เช่น data quality ต่ำกว่า threshold, UAT readiness ไม่ถึงเกณฑ์, vendor change request เกิน threshold หรือ go-live risk สูงขึ้น

ถ้า material governance change เกิดขึ้น เช่น เลื่อน cutover หรือเปลี่ยน contract baseline ต้องส่ง Sponsor/Steering Committee อนุมัติ

## 10. Hotel Booking Example or Contrast

Hotel Booking เหมาะกับ Agile product development สำหรับ UX, feature, conversion และ partner feedback เพราะ product ต้องเรียนรู้จากพฤติกรรมผู้ใช้

แต่ไม่ใช่ทุกอย่างควร adaptive เท่ากัน Payment, security, privacy, partner onboarding, launch readiness และ incident response ต้องมี gate และ acceptance ที่ชัด

ตัวอย่าง hybrid:

- Scrum สำหรับ booking journey และ conversion features
- Kanban สำหรับ support/payment incident flow
- predictive gate สำหรับ security review, payment readiness และ launch decision
- monthly benefit review หลัง launch เพื่อดู direct booking จาก 10% ไปสู่ 35% ภายใน 18 เดือน

## 11. Watch PM Think

ลำดับคิดของ PM:

1. แยก project เป็น workstreams
2. ประเมิน uncertainty และ risk ของแต่ละ workstream
3. เลือก approach พร้อม rationale
4. กำหนด governance owner และ cadence
5. ตั้ง trigger to review approach
6. ระบุ evidence ที่ใช้ prove readiness
7. เตรียม story สำหรับ executive defense ใน capstone

ถ้า hybrid plan ไม่มี trigger และ approval evidence มันยังเป็นความตั้งใจ ไม่ใช่ governance architecture

## 12. Artifact Example

Artifact ของบทนี้คือ Tailored Hybrid Delivery Plan

ใช้ template ต้นทางได้ที่ [Tailored Hybrid Delivery Plan](../../../lessons/lesson-16/learner/Artifact-Template.md)

Artifact ต้องมี:

- Workstream
- Approach and rationale
- Governance owner
- Trigger to review
- Cadence
- Approval evidence

Artifact นี้เป็นสะพานเข้าสู่ capstone เพราะผู้เรียนต้อง defend readiness recommendation และ comparative tailoring ได้

## 13. Workshop

ออกแบบ Tailored Hybrid Delivery Plan สำหรับ ERP หรือ Hotel Booking:

- แยก workstreams อย่างน้อย 5 ส่วน
- เลือก predictive/agile/hybrid ต่อ workstream
- เขียน rationale โดยอ้าง uncertainty, risk, compliance, contract หรือ feedback need
- ตั้ง trigger และ cadence
- ระบุ governance owner และ approval evidence
- ระบุสิ่งที่ต้องไม่ตัดทิ้งแม้ tailor แล้ว

ข้อจำกัด: ห้ามตอบว่า Agile ทั้งหมดหรือ Waterfall ทั้งหมดโดยไม่มี workstream rationale

## 14. Beginner Checkpoint

1. Predictive เหมาะกับงานแบบใด
2. Agile เหมาะกับงานแบบใด
3. Hybrid ที่ดีต้องมีอะไร
4. Tailoring ต่างจากการตัด process ตามใจอย่างไร
5. Trigger to review approach สำคัญอย่างไร

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่างจาก ERP หรือ Hotel Booking

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย predictive, agile, hybrid, tailoring rationale, trigger, cadence และ adaptive control

### B. Scenario Question

ERP ควรใช้ predictive กับ workstream ใด และ agile practice กับ workstream ใด เพราะอะไร

### C. Decision Case

Hotel Booking ต้อง balance Agile product delivery กับ payment/security launch controls ให้เสนอ hybrid approach

### D. Artifact Construction

สร้าง Tailored Hybrid Delivery Plan โดยใช้ evidence จาก Lessons 11-15

### E. Artifact Review

ตรวจแผนที่เขียนว่า "ใช้ Agile 100%" หรือ "Hybrid ตามสถานการณ์" แต่ไม่มี rationale/trigger/cadence แล้วแก้ให้ decision-ready

### F. Reflection

เขียน executive summary ไม่เกิน 200 คำว่า PM ควรเลือก delivery approach จากบริบท ไม่ใช่จากกระแสอย่างไร

Assessment นี้เน้น tailoring recommendation 40%, hybrid-plan artifact review 30%, governance/adaptive-control trade-off 20% และ recall 10%

## 16. เก็บตกท้ายบท

ประโยคที่ควรจำ:

```text
ไม่มีวิธีเดียวที่ดีที่สุดสำหรับทุกโครงการ
มีแต่วิธีที่เหมาะกับบริบท และต้องทบทวนเมื่อบริบทเปลี่ยน
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Agile ดีที่สุดเสมอ | วิธีที่เหมาะขึ้นกับ context |
| Hybrid คือทำอะไรก็ได้ | ต้องมี architecture, boundary และ control |
| Tailoring คือการตัดงานยาก | ต้องรักษาวัตถุประสงค์ control เดิม |
| ตั้งชื่อ approach ก็พอ | ต้องมี rationale, trigger, cadence และ evidence |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Predictive | วางแผนล่วงหน้า | เหมาะกับ scope ชัดและ control เข้ม |
| Agile | ปรับตัวเป็นรอบ | เหมาะกับ uncertainty และ feedback |
| Hybrid | ผสมตาม workstream | รวม control และ adaptability |
| Tailoring | ปรับให้เหมาะบริบท | เลือก process/artifact ตาม risk/value |
| Trigger | เงื่อนไขทบทวน | สัญญาณว่าต้องปรับ approach |
| Cadence | จังหวะทบทวน | รอบประชุม/review/feedback |
| Governance Architecture | โครง governance | ใครตัดสินใจอะไรด้วยหลักฐานใด |

## 19. สรุปหนึ่งหน้า

Predictive, Agile และ Hybrid เป็นเครื่องมือ ไม่ใช่อุดมการณ์

Tailoring ที่ดีต้องมี rationale, boundary, owner, trigger, cadence และ approval evidence

PM คือ integrator ที่ทำให้ scope, schedule, cost, quality, risk, people, procurement, agility และ value อยู่ในระบบตัดสินใจเดียวกัน

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | L11-L15 governance, flow, risk, acceptance and feedback evidence |
| Output | Tailored Hybrid Delivery Plan |
| Owner | PM owns governance/integration; PO owns product-delivery policy |
| Reviewers | PMO, Architecture, Security, QA, Operations and Vendor |
| Approval | Steering Committee or Sponsor |
| Next use | Capstone ใช้เพื่อป้องกัน methodology dogma และ defend executive readiness recommendation |


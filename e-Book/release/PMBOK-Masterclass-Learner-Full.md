---
title: PMBOK-aligned Practical Masterclass
author: Witchwasin K.
edition: Learner Full Markdown
status: Ready for Release Packaging
generated_on: 2026-07-22
---

# PMBOK-aligned Practical Masterclass

ผู้เรียบเรียง: Witchwasin K.

เอกสารนี้รวมบทเรียนสำหรับผู้เรียนและ capstone ไว้ในไฟล์ Markdown เดียว เพื่อใช้ตรวจอ่านหรือแปลงเป็นรูปแบบเผยแพร่ต่อไป เอกสารนี้ไม่ใช่เอกสารทางการของ PMI



<!-- Source: ../chapters/lesson-01/lesson-01-learner.md -->

# Chapter 01 — ทำไม Project Manager ต้องรู้ PMBOK

## 1. Opening Scenario

ลองนึกถึง Project Manager สามคนที่ได้รับมอบหมายให้ดูแลโครงการเดียวกัน

คนแรกเก่ง Schedule เขาจัด Timeline ได้ละเอียด เห็น dependency เร็ว และตามงานจนทีมส่งตรงเวลา

คนที่สองเก่ง Stakeholder เขาคุยกับ Sponsor ได้ดี รับ Requirement เร็ว และทำให้ผู้บริหารรู้สึกว่าโครงการมีคนดูแล

คนที่สามเก่งเทคนิค เขาคุยกับ Developer และ Vendor รู้เรื่อง เห็นปัญหาระบบก่อนคนอื่น และแก้ technical issue ได้เร็ว

ทั้งสามคนเก่งจริง แต่คำถามคือ ถ้าแต่ละคนมองโครงการผ่านสิ่งที่ตัวเองถนัด ใครกำลังมองภาพรวมทั้งหมด

ใครกำลังมองว่า Business Need ชัดหรือยัง ใครกำลังตรวจว่า Scope ไม่โตโดยไม่มีการตัดสินใจ ใครกำลังดู Risk, Quality, Change, Stakeholder, Procurement, Adoption และ Handover ให้เชื่อมกันจริง

นี่คือเหตุผลที่ Project Manager ต้องรู้ PMBOK ไม่ใช่เพื่อท่องจำคำศัพท์ แต่เพื่อไม่ให้ประสบการณ์ส่วนตัวกลายเป็นกรอบที่จำกัดการมองเห็น

## 2. Why This Matters

ประสบการณ์สำคัญมาก แต่ประสบการณ์อย่างเดียวไม่พอสำหรับโครงการที่ซับซ้อน

PM ที่เคยเจอปัญหาจากจำนวน Developer ไม่เพียงพอ อาจรีบแก้ทุกโครงการด้วยการเพิ่มคน แต่ถ้าโครงการใหม่ล้มเพราะผู้ใช้ไม่ยอมเปลี่ยน process การเพิ่ม Developer ก็ไม่ได้แก้ต้นเหตุ

PM ที่เคยถูก Vendor ส่งมอบช้า อาจให้ความสำคัญกับสัญญาและ penalty มากเป็นพิเศษ แต่ถ้าปัญหาจริงคือ Sponsor ยังไม่ตัดสินใจเรื่อง scope ทีมก็ยังเดินไม่ได้อยู่ดี

ประสบการณ์ทำให้เราเห็น pattern แต่ก็ทำให้เราเผลอใช้คำตอบเดิมกับปัญหาใหม่ได้ PMBOK จึงทำหน้าที่เหมือนแผนที่ของคำถามสำคัญ ช่วยเตือนว่าโครงการไม่ได้มีแค่ schedule หรือ task list แต่เป็นระบบที่มี business, people, decision, risk, value และ operation ต่อเนื่องกัน

PMBOK คือ Project Management Body of Knowledge หรือองค์ความรู้ของวิชาชีพ Project Management ไม่ใช่ methodology เดียว ไม่ใช่ template ชุดหนึ่ง และไม่ใช่ checklist ที่ต้องทำทุกข้อเท่ากันในทุกโครงการ

ประโยคที่ควรจำจากบทนี้คือ:

```text
PMBOK ไม่ได้บอกให้ Project Manager หยุดคิด
แต่ช่วยให้ Project Manager คิดได้ครบขึ้น
```

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. อธิบายได้ว่าทำไมประสบการณ์เฉพาะด้านอาจทำให้ PM มี blind spot
2. อธิบายว่า PMBOK เป็น Body of Knowledge ไม่ใช่ methodology หรือ template
3. แยก Output, Outcome, Benefit และ Business Value ได้
4. อธิบายว่าทำไม Go-live ไม่เท่ากับความสำเร็จเสมอไป
5. ระบุคำถามที่ควรถามก่อนเลือก Predictive, Agile หรือ Hybrid
6. สร้าง PM Learning Baseline ที่มี blind spots, evidence gaps และ learning actions สำหรับ Lesson 02

## 4. Beginner Safety

บทนี้ออกแบบสำหรับผู้เริ่มต้น คุณยังไม่ต้องจำชื่อ Process Groups หรือ Knowledge Areas ทั้งหมด และยังไม่ต้องรู้ว่าเอกสาร PM แต่ละชนิดหน้าตาเป็นอย่างไร

สิ่งที่ต้องตั้งหลักให้ได้ก่อนคือ:

- PMBOK เป็น framework ของความรู้ ไม่ใช่คำสั่งตายตัว
- Project success ต้องมองไกลกว่า “ส่งของครบ”
- งานของ PM คือเชื่อม Business Need ไปสู่ Value ผ่านการตัดสินใจและการประสานคน
- Tailoring คือการปรับระดับ control ให้เหมาะกับความเสี่ยงและบริบท ไม่ใช่การตัดสิ่งที่ไม่อยากทำ

คำศัพท์ใหม่ในบทนี้คือ `PMBOK`, `Framework`, `Tailoring`, `Output`, `Outcome`, `Benefit` และ `Business Value`

## 5. Mental Model

ให้มอง Project Management เป็นเส้นทางจากความต้องการทางธุรกิจไปสู่คุณค่าที่เกิดจริง

```text
Business Need
-> Decision
-> Work
-> Output
-> Adoption / Outcome
-> Benefit
-> Business Value
-> Transition to Operation
```

Framework ช่วยบอกว่าเราต้องถามอะไร ส่วน Professional Judgement ช่วยตัดสินใจว่าจะใช้คำตอบแบบใดในบริบทนี้

ถ้าไม่มี framework เราอาจถามเฉพาะเรื่องที่เราถนัด ถ้าไม่มี judgement เราอาจกรอก template ครบแต่ไม่เกิดการตัดสินใจที่ดี

## 6. Main Lesson

### ประสบการณ์คนเดียวไม่เท่ากับองค์ความรู้ร่วม

องค์กรไม่ควรฝากความสำเร็จของโครงการไว้กับ PM เก่งคนเดียว เพราะถ้าความสำเร็จเกิดจากความสามารถเฉพาะบุคคลทั้งหมด ความรู้นั้นจะถ่ายทอดยากและหายไปเมื่อคนคนนั้นย้ายทีม

Project Management จึงต้องมีภาษากลาง เช่น `Scope`, `Risk`, `Change`, `Deliverable`, `Acceptance` และ `Stakeholder` เพื่อให้ทีมไม่ได้พูดคำเดียวกันแต่หมายถึงคนละเรื่อง

คำว่า “งานเสร็จ” สำหรับ Developer อาจหมายถึงเขียน code เสร็จ สำหรับ Tester อาจหมายถึง test ผ่าน สำหรับ Business อาจหมายถึงผู้ใช้ทำงานจริงได้ และสำหรับผู้บริหารอาจหมายถึง KPI ดีขึ้นแล้ว ถ้าไม่แยกคำเหล่านี้ การรายงานสถานะจะดูดีบนกระดาษแต่ไม่ช่วยให้ตัดสินใจถูก

### PMBOK คืออะไร

PMBOK คือองค์ความรู้ของวิชาชีพ Project Management ใช้เป็นแผนที่ ภาษากลาง คลังความรู้ และฐานของการคิดแบบมืออาชีพ

PMBOK ไม่ได้เดินแทน PM เหมือนแผนที่ไม่ได้ขับรถแทนเรา แต่ช่วยให้เห็นว่าบริเวณใดมีทางแยก จุดเสี่ยง หรือพื้นที่ที่เรายังไม่ได้คิดถึง

### PMBOK ไม่ใช่อะไร

PMBOK ไม่ใช่ methodology เดียว ไม่ได้เท่ากับ Waterfall ไม่ใช่ checklist ที่ยิ่งทำครบยิ่งดี และไม่ได้รับประกันความสำเร็จ

เอกสารมีคุณค่าเมื่อช่วยให้คนคุยกัน ตัดสินใจ ตรวจสอบ หรือควบคุมความเสี่ยงได้ดีขึ้น เอกสารที่ไม่มีใครใช้ไม่ใช่ governance ที่ดี

### จาก Output ไปสู่ Value

หลายโครงการเริ่มจากประโยคที่ฟังเหมือน solution เช่น “เราต้องเปลี่ยน ERP” หรือ “เราต้องมี Mobile App” แต่ PM ต้องย้อนถามว่า Business Need คืออะไร

คำศัพท์สี่คำนี้สำคัญมาก:

- `Output` คือสิ่งที่โครงการสร้าง เช่น ระบบ รายงาน หรือ training package
- `Outcome` คือการเปลี่ยนแปลงที่เกิดเมื่อ output ถูกใช้จริง
- `Benefit` คือประโยชน์ที่วัดได้ เช่น ลดเวลาปิดงบหรือลด commission
- `Business Value` คือคุณค่าที่องค์กรได้รับจาก outcome และ benefit เหล่านั้น

Project ที่ส่ง output ครบแต่ไม่มี outcome อาจยังไม่สำเร็จในเชิงธุรกิจ

## 7. PM Thinking

PM ที่ยังตั้งหลักไม่ดีอาจถามว่า “ต้องใช้ template ไหน” แต่ PM ที่คิดแบบมืออาชีพจะถามว่า “การตัดสินใจนี้ต้องใช้ evidence อะไร และใครเป็น owner หลังส่งมอบ”

ตัวอย่างคำถามที่บทนี้ต้องฝึกให้ติดมือ:

- ปัญหาธุรกิจจริงคืออะไร
- สิ่งที่ผู้บริหารขอเป็น problem, goal หรือ solution
- Output ที่ทีมส่งมอบคืออะไร
- Outcome ที่ business ต้องทำให้เกิดคืออะไร
- Benefit จะวัดเมื่อไร และใครเป็น owner
- หาก assumption สำคัญผิด จะเกิด risk อะไร
- ถ้าใช้ Agile, Predictive หรือ Hybrid เรากำลังแก้ความไม่แน่นอนแบบใด

## 8. PM Decision Thinking

การเลือก governance และ delivery approach ต้องเป็น decision ไม่ใช่รสนิยม

```text
Decision: จะใช้ governance และ delivery approach ใดกับโครงการใหม่
Owner: Sponsor ร่วมกับ PM และ Product Owner เมื่อมี product discovery
Inputs: scope stability, regulation, uncertainty, stakeholder availability, cost of delay, team capability
Options: Predictive, Agile, Hybrid
Trade-offs: predictability, feedback speed, governance complexity, decision latency
Risk: เลือกจากชื่อ framework หรือกระแสนิยมแทน evidence
Evidence: tailoring rationale, working agreement, review trigger
Next action: ทบทวน approach เมื่อ assumption หลักเปลี่ยน
```

คำถามไม่ใช่ “Agile หรือ Waterfall อะไรดีกว่า” แต่คือ “ส่วนใดของโครงการต้องการ feedback เร็ว ส่วนใดต้องการ control เข้ม และความผิดพลาดมีต้นทุนเท่าไร”

## 9. ERP Worked Example

ERP Transformation ของ SIG มี Business Need เพื่อรวมศูนย์ข้อมูลและลดเวลาปิดงบจาก 15 วันเหลือ 5 วัน โครงการมี ERP 5 modules, legacy systems 6 ระบบ, key users 80 คน, working budget 45 ล้านบาท และ total funding envelope 60 ล้านบาท

ถ้าวัดแค่ output โครงการอาจดูสำเร็จเมื่อ ERP go-live, data migration เสร็จ, integration ทำงาน, training จัดครบ และ support plan ถูกส่งมอบ

แต่ outcome ยังต้องพิสูจน์ว่า Finance ใช้ process ใหม่จริง ข้อมูลข้ามฝ่ายสอดคล้องกัน และ monthly close ลดลงได้ตามเป้าหมาย

Benefit owner จึงไม่ควรเป็น PM เพียงคนเดียว หลัง handover เจ้าของ outcome ด้านการปิดงบควรอยู่ที่ CFO หรือ Finance Process Owner โดย PM มีหน้าที่ทำให้ owner, measure และ review date ถูกกำหนดก่อนปิดโครงการ

## 10. Hotel Booking Example or Contrast

Hotel Booking Digital Platform ของ SHG ต้องเพิ่ม direct booking จาก 10% เป็น 35% ภายใน 18 เดือนหลัง launch โดยมี Phase 1 budget 12 ล้านบาท และต้อง launch ก่อน high season

Output อาจประกอบด้วย Customer Web App, Mobile App, Landing Page, Back Office Web Application, Booking Engine, PMS sync, Payment Integration และ notification system

แต่ถ้าลูกค้าเข้า landing page เยอะแล้วไม่จอง หรือจ่ายเงินสำเร็จแต่ booking confirmation ล้มเหลว output ยังไม่สร้าง value ตามเป้าหมาย

โครงการนี้อาจใช้ Agile กับ UX และ booking journey เพราะต้องเรียนรู้จากผู้ใช้ แต่ยังต้องมี control เข้มกับ payment, security, performance และ launch readiness นี่คือตัวอย่างของ tailoring

## 11. Watch PM Think

ดูลำดับคิดของ PM ก่อนสร้าง PM Learning Baseline

1. เริ่มจาก Business Need ไม่เริ่มจาก solution
2. แยก output ที่ทีมส่งมอบจาก outcome ที่ business ต้องใช้ต่อ
3. ถามหา baseline, target, owner และ review timing
4. ระบุ blind spot ของตนเอง เช่น ถนัดเทคนิคจนมองข้าม adoption
5. บันทึก evidence gap แทนการแต่ง assumption ให้ดูครบ

เมื่อคุณยังระบุ benefit owner หรือ evidence gap ไม่ได้ artifact ยังไม่ควรถูกถือว่า usable

## 12. Artifact Example

ในบทนี้ artifact คือ `PM Learning Baseline`

คุณจะไม่ได้สร้างแผนโครงการเต็ม แต่จะสร้าง baseline ของวิธีคิดตัวเองก่อนเรียน เพื่อใช้ตรวจ blind spot ใน Lesson 02

โครงสร้างที่ต้องกรอก:

- Project context
- Current mental model
- Output-outcome assumptions
- Blind spots and evidence gaps
- Approval information

ใช้ template ต้นทางได้ที่ [PM Learning Baseline Template](../../lessons/lesson-01/learner/Artifact-Template.md)

## 13. Workshop

คุณได้รับมอบหมายให้ช่วย ERP Transformation ซึ่งตั้งเป้าลดเวลาปิดงบจาก 15 วันเหลือ 5 วัน ทีมเทคนิคบอกว่า “ติดตั้งระบบครบก็จบ” ขณะที่ Finance กังวลว่าผู้ใช้จะกลับไปทำงานใน Excel

บทบาทของคุณคือ PM คนใหม่ ให้กรอก PM Learning Baseline โดยแยก:

- Output ที่คาดว่าจะส่งมอบ
- Outcome ที่ต้องเกิดหลังใช้ระบบ
- Benefit ที่ต้องวัด
- Owner หลัง handover
- Blind spots อย่างน้อย 2 เรื่อง
- Evidence gaps อย่างน้อย 4 เรื่อง

ข้อจำกัด: ห้ามใช้ “ตรงเวลาและไม่เกินงบ” เป็นเกณฑ์ทั้งหมด และห้ามสมมติว่า Go-live ทำให้เกิด adoption อัตโนมัติ

## 14. Beginner Checkpoint

ตอบโดยไม่เปิดเฉลย:

1. PMBOK เป็น methodology ตายตัวหรือไม่ เพราะอะไร
2. Output ต่างจาก Outcome อย่างไร
3. ใครควรเป็น owner ของ Benefit หลัง handover
4. เหตุใดประสบการณ์เฉพาะด้านอาจทำให้ PM มี blind spot
5. Tailoring ต่างจากการตัดขั้นตอนที่ไม่อยากทำอย่างไร

ผ่าน checkpoint เมื่ออธิบายได้อย่างน้อย 4 ข้อโดยยกเหตุผล ไม่ใช่จำคำจำกัดความ

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบายสั้น ๆ ว่า PMBOK ต่างจาก methodology และ template อย่างไร

### B. Scenario Question

ERP go-live ตรงเวลา แต่ Finance ยังปิดงบ 15 วันเหมือนเดิม คุณจะรายงานความสำเร็จของโครงการอย่างไรให้ไม่ปน output กับ outcome

### C. Decision Case

CEO ขอให้ ERP “ใช้ Agile เพราะเร็วกว่า” ให้เขียนคำถาม 5 ข้อที่ต้องถามก่อนเลือก approach และเสนอ starting approach พร้อม assumption ที่อาจทำให้เปลี่ยนคำแนะนำ

### D. Artifact Construction

กรอก PM Learning Baseline สำหรับ ERP หรือ Hotel Booking โดยระบุ output, outcome, benefit, business value, owner, blind spots และ evidence gaps

### E. Artifact Review

ตรวจประโยคนี้: “Hotel Booking mobile app และ website launch ตรงเวลาในงบ 12 ล้านบาท จึงถือว่า project success” ระบุว่า claim นี้ขาดอะไรบ้าง

### F. Reflection

เขียนไม่เกิน 180 คำว่า framework และประสบการณ์ควรทำงานร่วมกันอย่างไรในบทบาท PM

Assessment นี้เน้น retrieval 10% และ application/judgement/artifact 90%

## 16. เก็บตกท้ายบท

PM มือใหม่มักอยากได้ template เพราะ template ทำให้รู้สึกว่ามีทางเดิน แต่สิ่งที่แยก PM ที่เติบโตเร็วออกจาก PM ที่ทำเอกสารเก่งอย่างเดียวคือความสามารถในการถามว่า “เอกสารนี้ใช้ตัดสินใจอะไร”

สัญญาณเตือนในที่ประชุม:

- ทุกคนพูดว่า “เสร็จ” แต่หมายถึงคนละอย่าง
- ไม่มีใครตอบได้ว่า benefit วัดเมื่อไร
- Sponsor ขอ solution แต่ยังไม่มีใครนิยาม problem
- ทีมเลือก Agile หรือ Waterfall ด้วยคำว่าเร็ว ชิน หรือองค์กรบังคับ โดยไม่มี evidence
- หลัง go-live ไม่มี owner ฝั่ง operation

ประโยคที่ใช้ขอ decision ได้:

```text
ก่อนเลือก approach ขอแยกก่อนว่า scope ส่วนใด stable, ส่วนใดยังต้อง discovery,
ใครเป็น decision owner และเราจะ review assumption นี้เมื่อไร
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| PMBOK คือ Waterfall | PMBOK เป็น body of knowledge; delivery approach ต้อง tailor |
| PM คือคนตามงาน | PM เชื่อม goal, people, decision, risk, change และ value |
| Go-live คือ success | Go-live เป็น output milestone; value ต้องดู adoption/outcome/benefit |
| Agile ไม่ต้องวางแผน | Agile เปลี่ยนจังหวะ planning ไม่ได้ยกเลิก planning |
| ตรงเวลาและไม่เกินงบพอแล้ว | อาจส่งตรงเวลาแต่ไม่มีใครใช้หรือไม่เกิด benefit |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย | ตัวอย่าง Scenario | คำที่มักสับสน |
|---|---|---|---|---|
| PMBOK | องค์ความรู้การบริหารโครงการ | แผนที่และภาษากลางของวิชาชีพ | ใช้ถามว่า ERP ต้องมอง risk, stakeholder, adoption อะไรบ้าง | Methodology |
| Framework | กรอบคิด | โครงช่วยถามให้ครบแต่ไม่ตัดสินแทนเรา | ใช้เลือก control ของ payment/security ใน Hotel Booking | Checklist |
| Tailoring | การปรับให้เหมาะบริบท | เลือกวิธีและระดับ control ตาม risk/uncertainty | Agile กับ UX แต่ control เข้มกับ payment | ตัดขั้นตอน |
| Output | ผลส่งมอบ | สิ่งที่ทีมสร้างหรือส่งให้ตรวจ | ERP go-live หรือ mobile app launch | Outcome |
| Outcome | ผลการเปลี่ยนแปลง | สิ่งที่เกิดเมื่อ output ถูกใช้จริง | Finance ปิดงบได้เร็วขึ้น | Output |
| Benefit | ประโยชน์ที่วัดได้ | ตัวเลขหรือผลดีที่ business ได้รับ | ปิดงบจาก 15 วันเหลือ 5 วัน | Value |
| Business Value | คุณค่าทางธุรกิจ | ผลที่ช่วยเป้าหมายองค์กรจริง | ลด OTA commission และเพิ่ม direct booking | Deliverable |
| Professional Judgement | ดุลยพินิจมืออาชีพ | การตัดสินใจจาก evidence และบริบท | เลือก hybrid เพราะ ERP มีทั้ง compliance และ discovery | ความเห็นลอย ๆ |

## 19. สรุปหนึ่งหน้า

PMBOK คือ body of knowledge ที่ช่วยให้ PM มีภาษากลางและมองโครงการครบมิติ ไม่ใช่ methodology ตายตัว

ประสบการณ์มีค่า แต่หากไม่มี framework PM อาจมองเฉพาะสิ่งที่เคยเจอและพลาดมิติที่ไม่คุ้น

Project success ต้องเชื่อมจาก Business Need ไปสู่ Output, Outcome, Benefit และ Business Value

ERP ที่ go-live แล้วแต่ปิดงบยัง 15 วันไม่ได้พิสูจน์ benefit ตามเป้าหมาย ส่วน Hotel Booking ที่ launch แล้วแต่ลูกค้าไม่จองก็ยังไม่สร้าง direct booking value

Tailoring ที่ดีต้องมี owner, evidence, trade-off และ review trigger ไม่ใช่เลือก approach จากกระแส

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | Learner experience and project assumptions; ERP and Hotel Booking scenario facts |
| Output | PM Learning Baseline |
| Creator | Learner |
| Artifact owner | Learner |
| Reviewer | Instructor or AI Coach |
| Approval authority | Course Assessor |
| Minimum acceptance | Usable |
| Next lesson use | Lesson 02 ใช้ blind spots และ value assumptions เพื่อสร้าง Project vs Operation Analysis and Value Chain |



<!-- Source: ../chapters/lesson-02/lesson-02-learner.md -->

# Chapter 02 — Project Management Overview

## 1. Opening Scenario

งานทุกอย่างมีวันเริ่มและวันจบของรอบงานได้ แต่ไม่ได้แปลว่างานทุกอย่างเป็น Project

Finance ปิดบัญชีทุกเดือน มี deadline ชัดเจน แต่โดยธรรมชาติแล้วเป็น Operation เพราะเกิดซ้ำและต้องรักษาคุณภาพอย่างต่อเนื่อง

ทีมโรงแรมอัปเดตราคาและห้องว่างทุกวัน มีรอบการทำงานชัดเจน แต่ก็เป็น Operation เพราะเป็นงานประจำที่รักษาระบบบริการให้เดินต่อ

ในทางกลับกัน การเปลี่ยน ERP ทั้งองค์กร หรือการสร้าง Direct Booking Platform ใหม่ เป็น Project เพราะเป็นความพยายามชั่วคราวเพื่อสร้างผลลัพธ์เฉพาะตัวและเปลี่ยน capability ขององค์กร

คำถามเปิดบทนี้คือ:

```text
งานทุกอย่างที่มีวันเริ่มต้นและวันสิ้นสุด เป็น Project ทั้งหมดหรือไม่
```

คำตอบสั้นคือ ไม่ใช่ และการแยกให้ถูกมีผลต่อ governance, funding, owner, success measure และวิธีบริหาร

## 2. Why This Matters

Project มีลักษณะ temporary และ unique คือมีขอบเขตเวลาชัดและสร้าง product, service, result หรือการเปลี่ยนแปลงที่เฉพาะตัว ส่วน Operation คือการดำเนินงานซ้ำต่อเนื่องเพื่อรักษาธุรกิจ

ถ้าองค์กรใช้วิธีบริหารผิดประเภท ผลเสียเกิดได้สองทาง

ทางแรกคือเอาวิธีบริหาร Operation ไปครอบ Project ที่ยังมีความไม่แน่นอนสูง เช่น digital product ใหม่ แล้วบังคับให้ทุกอย่างนิ่งเหมือน SOP ทำให้ทีมเรียนรู้จากผู้ใช้ช้า

ทางที่สองคือเอาวิธีบริหาร Project ไปครอบงานประจำ เช่น ตั้ง steering meeting และเอกสาร project หนา ๆ ให้กับงานที่ควรบริหารด้วย SLA หรือ continuous improvement แทน

ปัญหาที่สามสำคัญที่สุด: ทีมส่งมอบ output เสร็จ แต่ไม่เกิด value เพราะไม่มี transition, operation owner หรือ benefit measure หลังส่งมอบ

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. แยก Project, Operation และ transitional work ได้
2. อธิบายว่า deadline ไม่ใช่เกณฑ์เดียวในการตัดสินว่างานเป็น Project
3. สร้าง Value Chain จาก Business Need ถึง Business Value ได้
4. แยก Output, Outcome, Benefit และ Business Value พร้อม measure/owner ได้
5. อธิบายว่า Functional, Matrix และ Projectized organization มีผลต่ออำนาจ PM อย่างไร
6. สร้าง Project vs Operation Analysis and Value Chain เพื่อส่งต่อ Lesson 03

## 4. Beginner Safety

คุณควรรู้จาก Lesson 01 แล้วว่า PMBOK เป็น framework ไม่ใช่ checklist และ Output ไม่เท่ากับ Value

บทนี้ยังไม่ต้องจำ 5 Process Groups, WBS, schedule network, EVM, risk register หรือ Scrum events รายละเอียดเหล่านั้นจะมาในบทถัด ๆ ไป

ระวังกับดักสำหรับผู้เริ่มต้น:

- ใช้ขนาดงานหรืองบเป็นตัวตัดสินว่าเป็น Project
- คิดว่างานที่มี deadline ต้องเป็น Project เสมอ
- เรียก Go-live ว่า Outcome
- คิดว่า PM ต้องมีอำนาจสั่งทุกคนโดยตรงจึงจะทำงานได้

## 5. Mental Model

ให้ใช้ Value Chain เป็นภาพจำหลัก

```text
Business Need
-> Business Case
-> Project
-> Work
-> Output
-> Outcome
-> Benefit
-> Business Value
-> Transition to Operation
```

บทนี้เพิ่มจาก Lesson 01 อีกหนึ่งชั้น: ไม่ใช่แค่แยก output/outcome/value แต่ต้องถามด้วยว่างานส่วนใดเป็น Project งานส่วนใดเป็น Operation และจุดใดคือ transition ที่ความรับผิดชอบย้ายจาก project team ไปยัง operation owner

## 6. Main Lesson

### Project คืออะไร

Project คือความพยายามชั่วคราวเพื่อสร้าง product, service, result หรือการเปลี่ยนแปลงที่เฉพาะตัว

คำว่า temporary ไม่ได้แปลว่าสั้น โครงการ ERP อาจใช้เวลาประมาณ 12 เดือน ส่วน Hotel Booking Platform อาจใช้เวลาประมาณ 8 เดือน ทั้งสองยังเป็น Project เพราะมีจุดเริ่ม จุดจบ และผลลัพธ์เฉพาะตัว

คำว่า unique ไม่ได้แปลว่าไม่เคยมีใครทำมาก่อน แต่หมายถึงบริบทนี้มีความเฉพาะ เช่น องค์กรนี้ ระบบเดิมนี้ stakeholder ชุดนี้ budget นี้ timeline นี้ และ outcome นี้

### Operation คืออะไร

Operation คือการดำเนินงานต่อเนื่องเพื่อรักษาธุรกิจให้ทำงานได้ เช่น monthly close, daily booking support, incident handling, rate updates หรือ routine reporting

Operation อาจมี deadline และ KPI ได้ แต่ยังไม่ใช่ Project หากธรรมชาติของงานคือทำซ้ำและรักษาบริการ

### Transitional work คืออะไร

Transitional work คือช่วงที่ project output ถูกส่งต่อเข้า operation เช่น hypercare, training handover, support model setup, owner acceptance และ benefits review

ส่วนนี้มักเป็นช่องว่างอันตราย เพราะทีม project คิดว่าส่งของเสร็จแล้ว ส่วน operation ยังไม่พร้อมรับผิดชอบเต็มตัว

### PM ทำอะไรจริง

PM ไม่ได้มีหน้าที่ตามงานอย่างเดียว แต่ต้องเป็นคนเชื่อม decision, owner, evidence และ trade-off

PM ที่ดีจะไม่ถามแค่ “งานเสร็จไหม” แต่ถามว่า:

- งานนี้ควรบริหารเป็น Project, Operation หรือทั้งสองส่วน
- ใครเป็น sponsor, benefit owner และ operation owner
- Output นี้จะสร้าง outcome ผ่านพฤติกรรมหรือ process ใด
- Measure ใดพิสูจน์ว่า benefit เกิดจริง
- ถ้า organization เป็น matrix PM ต้องใช้ escalation และ resource commitment อย่างไร

### โครงสร้างองค์กรมีผลต่ออำนาจ PM อย่างไร

Functional Organization คือองค์กรตามสายงานปกติ ไม่มีตำแหน่ง PM เต็มเวลา งานโครงการถูกดูแลโดย functional manager เป็นหลัก คนที่ทำหน้าที่ PM จึงมีอำนาจตรงน้อย ต้องใช้ influence และอาศัย sponsor ช่วยผลักดัน priority

Matrix Organization แบ่งอำนาจระหว่าง PM และ functional manager โดยมี weak matrix ที่ PM มีอำนาจน้อยใกล้เคียง functional, balanced matrix ที่แชร์อำนาจใกล้เคียงกัน และ strong matrix ที่ PM มีอำนาจมากขึ้นแต่ resource ยังสังกัด functional manager เช่น ERP ที่ key users และ IT ยังขึ้นกับหัวหน้าสายงานเดิมแม้ PM จะสั่งงานประจำวันได้

Projectized Organization จัดทีมเป็น dedicated project team ที่รายงานตรงต่อ PM ทำให้ PM มีอำนาจ resource สูงสุดและตัดสินใจเร็วกว่า แต่ต้องแลกกับ cost ที่สูงขึ้นและทีมอาจขาดการพัฒนาสายอาชีพเชิงลึกแบบ functional home

ไม่มีโครงสร้างใดดีที่สุดเสมอ PM ต้องอ่านโครงสร้างองค์กรก่อนวางแผน authority, escalation path และ resource commitment ที่เป็นจริง ไม่ใช่ที่อยากให้เป็น

## 7. PM Thinking

ใช้ 3-question decision filter นี้เมื่อเจองานใหม่

```text
Question 1: งานนี้คือ Project, Operation หรือทั้งสองส่วน
Question 2: Output, Outcome, Benefit และ Value คืออะไร
Question 3: โครงสร้างองค์กรให้ authority และ resource commitment แก่ PM แค่ไหน
```

ถ้าตอบข้อ 1 ผิด governance ก็ผิดตาม ถ้าตอบข้อ 2 ไม่ชัด status report จะปน delivery กับ value ถ้าตอบข้อ 3 ไม่จริง resource plan จะสวยบนกระดาษแต่ใช้งานไม่ได้

## 8. PM Decision Thinking

ตัวอย่าง decision สำหรับ ERP:

```text
Decision: จะจัด "ลดเวลาปิดงบ" เป็น operational improvement, ERP project หรือ portfolio ที่มีทั้งสองส่วน
Owner: Sponsor และ business owner; PM เสนอ analysis
Inputs: uniqueness, duration, cross-functional dependency, baseline 15 วัน, cost of delay, key-user capacity
Options: แก้รายงานเฉพาะหน้า, เริ่ม ERP เต็ม scope, หรือทำ improvement คู่กับ ERP
Trade-offs: quick fix เร็วแต่ไม่แก้ root cause; ERP สร้าง capability แต่ใช้เวลาและ change effort
Risk: ตัดสินจาก deadline โดยไม่ตั้ง outcome owner
Evidence: business case, outcome KPI, resource commitment, transition plan
Next action: บันทึก classification และ review benefit หลัง go-live
```

Decision ที่ดีไม่ต้องเลือกคำตอบที่ใหญ่ที่สุดเสมอ แต่ต้องชี้ให้เห็นว่าตัวเลือกแต่ละแบบแก้ปัญหาใด ไม่แก้ปัญหาใด และใครรับผิดชอบผลลัพธ์

## 9. ERP Worked Example

ใน ERP Transformation ของ SIG การปิดบัญชีประจำเดือนเป็น Operation เพราะเกิดซ้ำและเป็นงานธุรกิจต่อเนื่อง

การออกแบบ ERP, migrate ข้อมูลจาก 6 legacy systems, สร้าง integration, UAT, training, cutover และ go-live เป็น Project เพราะเป็น temporary initiative เพื่อสร้าง capability ใหม่ให้ทั้งองค์กร

การแก้รายงานชั่วคราวเพื่อช่วย CFO ในไตรมาสหน้าอาจเป็น operational improvement ที่เดินคู่กับ ERP ได้ แต่ต้องไม่ทำให้ทีมหลงคิดว่าแก้ report แล้ว root cause เรื่อง process/data ownership หายไป

Value Chain สำหรับ ERP:

| Stage | Example |
|---|---|
| Business Need | ข้อมูลไม่ตรงกันและปิดงบ 15 วัน |
| Project Output | ERP 5 modules, migrated data, trained users |
| Outcome | ผู้ใช้ทำงานบน process/data กลาง |
| Benefit | ปิดงบภายใน 5 working days |
| Business Value | ผู้บริหารตัดสินใจจากข้อมูลที่น่าเชื่อถือเร็วขึ้น |
| Transition | PM ส่งต่อให้ IT Operations และ Finance Process Owner พร้อม support/benefits review |

## 10. Hotel Booking Example or Contrast

Hotel Booking Platform ของ SHG มี Project phase ที่สร้าง website, mobile app, landing page, back office, payment integration, PMS sync และ launch capability

หลัง launch การรับ booking รายวัน, incident support, rate updates, inventory updates และ product operations เป็น Operation หรือ Product Operation

Value ไม่ได้เกิดเพราะ app อยู่ใน store แต่ต้องดูว่า direct booking เพิ่มจาก 10% ไปสู่ 35% ภายใน 18 เดือนหรือไม่ payment reliable แค่ไหน partner update inventory ทันหรือไม่ และลูกค้าจองสำเร็จจริงหรือไม่

บทเรียนสำคัญคือ digital product อาจมี project เพื่อสร้าง capability และมี operation/product operation เพื่อรักษาและพัฒนาคุณค่าหลัง launch

## 11. Watch PM Think

ดูลำดับคิดก่อนกรอก artifact

1. เริ่มจาก Business Need ไม่เริ่มจากชื่อ solution
2. แยกงานตามธรรมชาติ: temporary/unique หรือ ongoing/repetitive
3. ไม่ใช้ deadline เป็นเกณฑ์เดียว
4. หา transition point ที่ accountability ย้ายจาก project ไป operation
5. สร้าง Value Chain โดยบังคับให้แต่ละ stage มี measure และ owner
6. ตรวจว่า outcome เกิดจาก output จริงหรือเป็นแค่ assumption

ถ้าตารางของคุณมีแต่ output และไม่มี owner หลัง transition ยังไม่ควรถือว่า usable

## 12. Artifact Example

Artifact ของบทนี้คือ `Project vs Operation Analysis and Value Chain`

ใช้ template ต้นทางได้ที่ [Project vs Operation Analysis and Value Chain Template](../../lessons/lesson-02/learner/Artifact-Template.md)

สิ่งที่ต้องมี:

- Decision context
- Work classification
- Value Chain
- Evidence gaps and governance recommendation
- Approval fields

Artifact นี้รับ input จาก PM Learning Baseline ของ Lesson 01 และจะส่งต่อ project boundary, expected value และ transition point ให้ Lesson 03

## 13. Workshop

CFO ต้องการลดเวลาปิดงบจาก 15 วันเหลือ 5 วัน มีสองข้อเสนอ: แก้รายงานรายเดือนเป็น BAU หรือทำ ERP Transformation 5 modules พร้อมปรับ process/data ownership

ให้สร้าง Project vs Operation Analysis and Value Chain หนึ่งหน้า โดย:

- แยก monthly close, temporary report fix, ERP implementation และ post-go-live support
- ระบุข้อมูลที่ยังขาดก่อนเลือก governance
- แยก Output, Outcome, Benefit และ Value
- ระบุ Sponsor, Benefit Owner และ Operation Owner
- เสนอว่าควรตั้งเป็น project, operation improvement หรือทั้งสองส่วน

ข้อจำกัด: ห้ามสรุปจาก deadline หรือขนาดงบเพียงอย่างเดียว

## 14. Beginner Checkpoint

ตอบโดยไม่เปิดเฉลย:

1. งานที่ทำซ้ำทุกเดือนแต่มี deadline เป็น Project เสมอหรือไม่
2. Project กับ Operation เชื่อมกันตรง Transition อย่างไร
3. “เปิด Mobile App” เป็น Output, Outcome หรือ Benefit
4. “Direct booking จาก 10% เป็น 35% ภายใน 18 เดือน” อยู่ระดับใด
5. Functional, Matrix และ Projectized ส่งผลต่ออำนาจ PM อย่างไร

ผ่านเมื่ออธิบาย 4 จาก 5 ข้อพร้อมเหตุผลและ owner ที่เกี่ยวข้อง

## 15. End-of-Chapter Assessment

### A. Concept Check

เลือกหรืออธิบายคำตอบสั้น ๆ เกี่ยวกับ Project, Operation, Output, Outcome, organization structure และ success measure

### B. Scenario Question

ERP มีทั้ง CFO request เพื่อปิดงบเร็วขึ้นและโครงการ ERP ระยะ 12 เดือน ให้แยกว่าเรื่องใดเป็น operation improvement เรื่องใดเป็น project และเรื่องใดต้องเป็น portfolio-level decision

### C. Decision Case

Hotel Booking launch แล้ว แต่ payment failure สูง, hotel partners update inventory ช้า และ direct booking ยังเพิ่มไม่มาก ให้แยก delivered outputs, lagging outcomes, operation issue และ follow-on improvement/project

### D. Artifact Construction

สร้าง Project vs Operation Analysis and Value Chain สำหรับ ERP หรือ Hotel Booking โดยมี measure/evidence และ accountable owner ทุก stage

### E. Artifact Review

ตรวจ classification ที่ใช้ deadline เป็นเกณฑ์เดียว แล้วแก้ให้ใช้ temporary, unique, ongoing, owner และ transition point

### F. Reflection

เขียน executive brief 5 ประโยคที่แยก business need, output, outcome, owner และ next decision

Assessment นี้เน้น retrieval 20% และ application/judgement/artifact 80%

## 16. เก็บตกท้ายบท

PM มือใหม่มักถามว่า “งานนี้ใหญ่พอจะเป็น Project ไหม” แต่คำถามที่ดีกว่าคือ “งานนี้สร้างการเปลี่ยนแปลงเฉพาะตัวหรือรักษางานประจำ”

สัญญาณเตือน:

- งานประจำถูกตั้งเป็น project ซ้ำ ๆ เพราะไม่มี owner แก้ process
- Project ถูกปิดเมื่อ output ส่งครบ แต่ operation ยังไม่พร้อม
- KPI รายงานแต่ delivery ไม่รายงาน adoption
- PM ใน matrix คิดว่าตัวเองสั่งทุก function ได้โดยไม่มี resource commitment
- Sponsor ขอ value แต่ไม่มี benefit owner

ประโยคที่ใช้ในที่ประชุม:

```text
ขอแยกก่อนว่าส่วนนี้เป็น project work, operation work หรือ transition work
แล้วค่อยกำหนด owner, measure และ governance ให้เหมาะกับธรรมชาติของงาน
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| ทุกงานที่มี deadline คือ Project | Operation ก็มี deadline ได้; ให้ดู temporary/unique กับ ongoing/repetitive |
| Go-live คือ outcome | Go-live เป็น output milestone; outcome คือการเปลี่ยนแปลงจากการใช้ output |
| Projectized organization ดีกว่าเสมอ | โครงสร้างแต่ละแบบมี trade-off เรื่อง authority, speed, expertise และ cost |
| PM คือเจ้าของ benefit คนเดียว | Sponsor, business owner และ operation owner ต้องถือ ownership หลัง handover |
| Transition คือส่งเอกสาร | Transition ต้องมี owner, support, acceptance และ benefit review |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย | ตัวอย่าง Scenario | คำที่มักสับสน |
|---|---|---|---|---|
| Project | โครงการ | งานชั่วคราวที่สร้างผลลัพธ์เฉพาะตัว | ERP implementation 5 modules | Operation |
| Operation | งานประจำ | งานต่อเนื่องที่รักษาบริการหรือกระบวนการ | Monthly close หรือ daily booking support | Project |
| Transitional Work | งานส่งต่อ | งานช่วง project ส่ง output ให้ operation รับผิดชอบ | Hypercare หลัง ERP go-live | Closing |
| Output | ผลส่งมอบ | สิ่งที่ project สร้าง | Mobile app, ERP module | Outcome |
| Outcome | ผลการเปลี่ยนแปลง | สิ่งที่เกิดเมื่อ output ถูกใช้จริง | ลูกค้าจองเองผ่าน platform | Output |
| Benefit | ประโยชน์ที่วัดได้ | ผลดีที่วัดตามเป้าหมาย | Close cycle 15 วันเหลือ 5 วัน | Business Value |
| Business Value | คุณค่าทางธุรกิจ | คุณค่าที่ช่วยเป้าหมายองค์กร | ลด OTA commission และเพิ่ม margin | Output |
| Functional Organization | องค์กรตามสายงาน | PM มีอำนาจตรงน้อย ต้องใช้ influence | Key users ยังขึ้นกับ manager เดิม | Projectized |
| Matrix Organization | องค์กรแบบแบ่งอำนาจ | PM และ functional manager แชร์อำนาจ | ERP strong matrix | Functional |
| Projectized Organization | องค์กรแบบทีมโครงการ | PM มีอำนาจ resource สูงกว่า | Dedicated product delivery team | Matrix |

## 19. สรุปหนึ่งหน้า

Project คือ temporary และ unique ส่วน Operation คือ recurring และ ongoing

Deadline, budget หรือขนาดงานไม่ใช่เกณฑ์เดียวในการเรียกงานว่า Project

Value Chain ต้องเชื่อม Business Need ไปสู่ Output, Outcome, Benefit, Business Value และ Transition to Operation

ERP implementation เป็น Project แต่ monthly close เป็น Operation ส่วน Hotel Booking launch เป็น Project output แต่ booking support หลัง launch เป็น Operation

Artifact ที่ดีต้องมี classification, measure/evidence, owner, governance recommendation และ next decision

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | PM Learning Baseline from Lesson 01; ERP and Hotel Booking scenario facts |
| Output | Project vs Operation Analysis and Value Chain |
| Creator | Learner in PM Analyst role |
| Artifact owner | Sponsor or Business Owner |
| Reviewer | Functional Owner and PM |
| Approval authority | Sponsor |
| Minimum acceptance | Usable |
| Next lesson use | Lesson 03 ใช้ project boundary, expected value และ transition point เพื่อสร้าง Lifecycle and Process Group Map |



<!-- Source: ../chapters/lesson-03/lesson-03-learner.md -->

# Chapter 03 — 5 Project Management Process Groups

## 1. Opening Scenario

ERP อยู่ช่วง planning แต่ทีม System Integrator เริ่ม prototype แล้ว Data Owner ยังไม่ยืนยัน cleansing rules และ UAT capacity ของ key users ยังไม่ชัด

คุณเอกซึ่งเป็น PM มีแรงกดดันสองด้าน ด้านหนึ่งคือ timeline ต้อง go-live ก่อน 1 ตุลาคม อีกด้านหนึ่งคือถ้าข้อมูล master data ไม่พร้อม การ build ต่ออาจทำให้ rework ใหญ่กว่าเดิม

คำถามคือ:

```text
ถ้าโครงการเริ่มทำงานจริงไปแล้ว แต่พบว่าขอบเขตหรือข้อมูลสำคัญยังไม่ชัด
ควรกลับไป Planning หรือเดินหน้าต่อ
```

ถ้าเรามอง Process Groups เป็นเส้นตรง เราอาจตอบว่า “ผ่าน planning แล้ว ห้ามย้อนกลับ” แต่ถ้าเรามองแบบ PM มืออาชีพ เราจะถามว่า evidence ใหม่กระทบ baseline, decision gate หรือ transition readiness หรือไม่

## 2. Why This Matters

5 Process Groups คือกลุ่มกิจกรรมบริหารโครงการ ไม่ใช่ 5 phases ที่เดินเรียงแล้วห้ามย้อนกลับ

ความเข้าใจผิดที่แพงมากคือการวาดแบบนี้:

```text
Initiating -> Planning -> Executing -> Monitoring -> Closing
```

แล้วคิดว่า Monitoring เริ่มหลังงานเสร็จ หรือ Closing คือประชุมสรุปบทเรียนอย่างเดียว

ในชีวิตจริง Executing กับ Monitoring & Controlling ต้องเกิดคู่กัน เพราะถ้าทำงานโดยไม่อ่าน evidence เราจะรู้ปัญหาช้าเกินไป และถ้า monitor แล้วไม่ control หรือไม่ replan เราก็มีแต่ report ที่ไม่เปลี่ยนการตัดสินใจ

มุมมอง value delivery ทำให้ process มีไว้เพื่อช่วยตัดสินใจ ไม่ใช่เพื่อทำเอกสารให้ครบพิธี

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. อธิบาย 5 Process Groups ได้โดยไม่สับสนกับ project phases
2. แยก Initiating, Planning, Executing, Monitoring & Controlling และ Closing ตามหน้าที่การบริหาร
3. อธิบายว่า Planning เกิดซ้ำได้เมื่อมี evidence ใหม่
4. อธิบายว่า Executing และ Monitoring & Controlling เกิดคู่กันอย่างไร
5. วิเคราะห์ ERP และ Hotel Booking ด้วย feedback loop และ replanning trigger
6. สร้าง Lifecycle and Process Group Map ที่ส่งต่อไป Lesson 04 ได้

## 4. Beginner Safety

คุณควรรู้จาก Lesson 02 แล้วว่า Project ต่างจาก Operation และ Value Chain ต้องมี transition point

บทนี้ยังไม่ต้องจำรายละเอียด process ทั้งหมด ไม่ต้องลงลึก WBS, schedule network, EVM, procurement law หรือ Scrum events

สิ่งที่ต้องระวังคือ:

- อย่าใช้ชื่อ Process Groups เป็นชื่อ phase ทั้งหมด
- อย่าคิดว่า Planning ทำครั้งเดียว
- อย่าคิดว่า Monitoring คือการรายงานย้อนหลังเท่านั้น
- อย่าคิดว่า Closing คือการเซ็นรับหรือประชุมปิดงานเท่านั้น

## 5. Mental Model

ให้มอง Process Groups เป็นระบบบริหารที่ทำงานร่วมกัน

```text
Initiating
    ↓
Planning
    ↓
Executing <-> Monitoring & Controlling
      ↑              ↓
      └── Replanning ┘
    ↓
Closing
```

และให้แยกสองคำนี้ให้ชัด:

- `Project Phase` คือช่วง lifecycle ของงาน เช่น Blueprint, Build, Test, Cutover
- `Process Group` คือกลุ่มกิจกรรมบริหาร เช่น Initiating, Planning, Executing, Monitoring & Controlling, Closing

ใน phase เดียวกันอาจมีหลาย Process Groups เกิดร่วมกันได้ เช่นช่วง Test มี executing test, monitoring defect trend, controlling change, planning retest และ closing phase gate

## 6. Main Lesson

### Initiating

Initiating คือการตั้งต้น project หรือ phase ให้มี authority และเป้าหมายชัด ไม่ใช่แค่ kickoff meeting

Output สำคัญอาจรวม Project Charter และ stakeholder information จุดสำคัญคือใครอนุมัติ ทำไปเพื่ออะไร และ success measure ระดับสูงคืออะไร

ถ้าเริ่ม executing ก่อนมี initiating ที่ดี ทีมอาจมี schedule แต่ไม่มี sponsor authority, decision rule หรือ benefit owner

### Planning

Planning คือการวางแนวทางเพื่อให้บรรลุ objective และสร้าง baseline สำหรับบริหาร scope, schedule, cost, quality, risk, communication และเรื่องอื่น ๆ

Planning ไม่ใช่กิจกรรมครั้งเดียว เพราะข้อมูลโครงการค่อย ๆ ชัดขึ้นตาม evidence จริง สิ่งนี้เรียกว่า progressive elaboration

การ replan เมื่อมี evidence ใหม่ไม่ใช่การไม่มีแผน แต่เป็นการใช้ control เพื่อปรับแผนอย่างมีเหตุผล

### Executing

Executing คือการทำงานเพื่อสร้าง deliverable ตามแผน เช่น configure ERP, migrate data, train users, develop app, run beta หรือ prepare launch

Executing ไม่ใช่เฉพาะ technical work เพราะรวมการประสานคน สื่อสาร จัดการ issue และทำให้ทีมทำงานตามแผนที่ตกลง

### Monitoring & Controlling

Monitoring & Controlling คือการติดตาม วิเคราะห์ variance และตัดสินใจตอบสนอง ไม่ใช่การส่งรายงานเฉย ๆ

ตัวอย่าง evidence เช่น progress, defect trend, migration reconciliation result, payment failure, conversion rate, risk signal และ readiness metric

ถ้า evidence กระทบ baseline ต้องมี change request, impact analysis และ decision owner ที่เหมาะสม

### Closing

Closing คือการปิด project หรือ phase อย่างเป็นทางการ รวม acceptance, handover, contract closure, lessons learned, unresolved item ownership และ transition to operation

Go-live ไม่ใช่ Closing ครบถ้วน หาก support model, operation owner และ benefit review ยังไม่พร้อม

## 7. PM Thinking

เมื่อเกิดความเบี่ยงเบน ให้ถามเป็น flow:

```text
1. ตอนนี้เกิดอะไรใน Executing
2. Evidence จาก Monitoring บอกอะไร
3. กระทบ baseline หรือ charter หรือไม่
4. ต้อง control ด้วย corrective action, preventive action, change request หรือ replan
5. ใครเป็น decision owner
6. Evidence ใดต้อง update ก่อนเดินต่อ
```

คำตอบที่ดีมักไม่ใช่ “หยุดทั้งหมด” หรือ “ลุยทั้งหมด” แต่คือ “งานใดไปต่อได้ งานใดต้อง replan และงานใดต้อง escalate”

## 8. PM Decision Thinking

ตัวอย่าง decision:

```text
Decision: ปัญหาที่พบควรแก้ใน Executing, ส่งเข้า Monitoring & Controlling, replan หรือ escalate กลับไป Sponsor
Owner: PM เสนอ analysis; Sponsor, change authority หรือ steering committee ตัดสินเมื่อกระทบ baseline/charter
Inputs: charter, baseline, actual progress, work performance data, issue log, risk, impact analysis
Options: execute ต่อ, corrective action, preventive action, change request, rebaseline, defer scope
Trade-offs: speed vs control, local fix vs systemic fix, schedule protection vs adoption/readiness
Risk: มอง Process Groups เป็น phase เส้นตรง, ข้าม change control, ซ่อน variance
Evidence: variance data, root cause, user impact, cost/schedule impact, go-live readiness
Next Action: สร้าง decision brief และระบุ Process Group ที่ต้อง activate ต่อ
```

## 9. ERP Worked Example

ใน ERP Transformation ของ SIG ถ้า TechConsult ขอเริ่ม build เพื่อรักษา timeline แต่ Data Owner ยังไม่ยืนยัน cleansing rules PM ไม่ควรตอบว่า “planning จบแล้ว ไปต่อ”

เขาควรแยก:

- Executing: prototype หรือ configuration บางส่วนอาจเดินต่อได้
- Monitoring & Controlling: evidence บอกว่า data ownership และ UAT capacity เป็น risk
- Planning: data workstream, cleansing rule, retest และ quality gate ต้อง replan
- Sponsor escalation: ถ้า replan กระทบ go-live ก่อน 1 ตุลาคมหรือ objective ระดับ charter ต้องเข้า steering committee
- Closing risk: ถ้าไม่แก้ ownership ตอนนี้ handover ไป operation จะไม่เสถียร

ข้อสรุปเชิง PM คืออนุญาตเฉพาะงานที่ไม่สร้าง rework risk สูง และแยกงานที่ต้องกลับไป planning พร้อม evidence ชัดเจน

## 10. Hotel Booking Example or Contrast

ใน Hotel Booking Platform ถ้าช่วง beta พบ payment failure สูง, conversion ต่ำ และผู้ใช้บอกว่า checkout flow ยาว ทั้งที่ marketing ต้องการ launch ตามแผน Process Groups ยังทำงานอยู่ครบ

- Executing: ทีมยัง develop และ fix bug
- Monitoring & Controlling: beta metrics และ user feedback ส่งสัญญาณ risk
- Planning: backlog, release criteria, support plan และ launch readiness ต้องปรับ
- Decision gate: sponsor/product owner ต้องตัดสินใจว่าพร้อม launch, delay หรือ launch แบบจำกัด scope
- Closing/Transition: ถ้าเปิด MVP ต้องส่งต่อ product operations และ stabilization plan

Agile ไม่ได้ยกเลิก Process Groups แต่เปลี่ยน cadence ให้ planning, execution, monitoring และ replanning เกิดถี่ขึ้น

## 11. Watch PM Think

ก่อนสร้าง Lifecycle and Process Group Map ให้คิดตามนี้:

1. นำ project boundary และ value chain จาก Lesson 02 มาใช้ ไม่สร้าง objective ใหม่
2. ตั้ง lifecycle phases จากลักษณะ delivery เช่น Blueprint, Build, Test, Cutover
3. วาง Process Groups ซ้ำในหลาย phase ตาม management need
4. จับคู่ executing activity กับ monitoring signal
5. กำหนด trigger ที่ทำให้ต้อง replan
6. กำหนด closing จาก acceptance, transition, open-item ownership และ benefits handoff

ถ้า map ของคุณเรียง Initiating, Planning, Executing, Monitoring, Closing เป็น phase ทั้งหมด แปลว่ายังไม่ผ่านบทนี้

## 12. Artifact Example

Artifact ของบทนี้คือ `Lifecycle and Process Group Map`

ใช้ template ต้นทางได้ที่ [Lifecycle and Process Group Map Template](../../lessons/lesson-03/learner/Artifact-Template.md)

Artifact ต้องมี:

- Project boundary from Lesson 02
- Lifecycle phases
- Process Group activity map
- Feedback and replanning
- Closing and transition
- Approval fields

## 13. Workshop

ERP อยู่ช่วง planning แต่ทีม SI เริ่ม prototype แล้ว Data Owner ยังไม่ยืนยัน cleansing rules และ UAT capacity ของ key users ยังไม่ชัด

ให้คุณ:

- ร่าง lifecycle phases ตั้งแต่ initiation ถึง benefits transition
- วาง management activities ลงใน Process Groups
- แสดงว่า Executing กับ Monitoring & Controlling เกิดคู่กันตรงไหน
- ระบุ signal ที่ต้องกลับไป Replanning
- กำหนด exit evidence และ approval authority ของแต่ละ gate

ข้อจำกัด: ห้ามใช้ Process Groups เป็นชื่อ phase ทั้งหมด และห้ามใส่ Planning เพียงครั้งเดียว

## 14. Beginner Checkpoint

ตอบโดยไม่เปิดเฉลย:

1. Process Group ต่างจาก Project Phase อย่างไร
2. Planning เกิดหลัง Initiating ครั้งเดียวหรือไม่
3. Monitoring & Controlling เกิดก่อนหรือหลัง Executing
4. Closing ต้องมีหลักฐานอะไรนอกจาก meeting ปิดงาน
5. Signal แบบใดทำให้ต้อง Replanning

ผ่านเมื่ออธิบาย 4 จาก 5 ข้อและยกตัวอย่างจาก ERP หรือ Hotel Booking ได้

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบายความต่างของ Process Group และ Project Phase พร้อมยกตัวอย่างจาก ERP หรือ Hotel Booking

### B. Scenario Question

ERP data readiness ไม่พอแต่ build เริ่มแล้ว ให้ระบุ Process Groups ที่เกี่ยวข้อง evidence ที่มี/ขาด งานที่ไปต่อได้ งานที่ต้อง replan และ decision owner

### C. Decision Case

Hotel Booking beta พบ payment failure และ conversion ต่ำ ให้เสนอว่าควร execute ต่อ, control, replan, escalate หรือ delay launch อย่างไร พร้อม trade-off

### D. Artifact Construction

สร้าง Lifecycle and Process Group Map ที่มี phases, gates, Process Group activities, feedback triggers, closing evidence และ transition owner

### E. Artifact Review

ตรวจข้อความนี้: “Initiating คือ Phase 1, Planning คือ Phase 2, Executing คือ Phase 3, Monitoring เริ่มหลัง build เสร็จ และ Closing คือประชุมสรุปบทเรียน” ระบุจุดผิดอย่างน้อย 4 จุดและเสนอ flow ใหม่

### F. Reflection

เขียนสั้น ๆ ว่าในโครงการของคุณ Process Group ใดอ่อนที่สุด และส่งผลต่อ decision, evidence หรือ value อย่างไร

Assessment นี้เน้น retrieval 10% และ application/judgement/artifact 90%

## 16. เก็บตกท้ายบท

การกลับไป Planning ไม่ใช่เรื่องน่าอาย ถ้ามี evidence ใหม่ที่ทำให้ baseline เดิมไม่จริงอีกต่อไป

สิ่งที่น่าอายกว่า คือรู้ว่า evidence เปลี่ยนแล้วแต่ยังเดินต่อเพราะกลัวรายงานว่า “ต้อง replan”

สัญญาณเตือน:

- ทีมพูดว่า “ผ่าน planning แล้ว” เพื่อปิดการถกผลกระทบ
- Status report มีแต่ percent complete ไม่มี decision required
- Monitoring เกิดหลังงานเสร็จ ไม่ใช่ระหว่างทำ
- Closing ไม่มี owner หลัง handover
- Agile team ใช้คำว่า sprint เพื่อเลี่ยง launch readiness gate

ประโยคที่ใช้ในที่ประชุม:

```text
นี่ไม่ใช่การย้อนกลับเพราะวางแผนไม่ดี
แต่เป็นการ activate Planning จาก evidence ใหม่ผ่าน Monitoring & Controlling
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Process Groups คือ waterfall phases | เป็น management functions ที่เกิดซ้ำและซ้อนทับได้ |
| Planning ทำครั้งเดียว | Planning ปรับได้ผ่าน evidence และ control |
| Monitoring คือ report | Monitoring & Controlling คือการอ่าน variance และตัดสินใจตอบสนอง |
| Controlling คือควบคุมคน | Controlling คือควบคุมงานเทียบ baseline และ decision |
| Closing คือเซ็นรับ | Closing รวม handover, lessons learned, contract closure และ owner หลังปิด |
| Agile ไม่มี Planning/Closing | Agile ยังมี เพียง cadence และระดับรายละเอียดต่างกัน |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย | ตัวอย่าง Scenario | คำที่มักสับสน |
|---|---|---|---|---|
| Process Group | กลุ่มกระบวนการบริหาร | โหมดการบริหาร 5 กลุ่มที่ใช้ตั้งต้น วางแผน ทำงาน ควบคุม และปิด | Monitoring & Controlling ระหว่าง ERP UAT | Project Phase |
| Project Phase | ระยะของโครงการ | ช่วง lifecycle เช่น Blueprint, Build, Test, Cutover | Hotel Booking Beta phase | Process Group |
| Lifecycle | วงจรชีวิตโครงการ | ลำดับ phase ตั้งแต่เริ่มจนส่งต่อ | ERP Initiation ถึง Hypercare | Process Group |
| Feedback Loop | วงจรข้อมูลย้อนกลับ | evidence จากงานจริงที่ทำให้ต้องปรับ decision | Payment failure ทำให้ปรับ backlog | Status report |
| Progressive Elaboration | การทำให้แผนชัดขึ้นเรื่อย ๆ | ข้อมูลใหม่ทำให้แผนละเอียดขึ้น | Data cleansing rule ชัดหลัง profiling | Scope creep |
| Replanning | การปรับแผนใหม่ | ปรับแผนจาก evidence ผ่าน control | Replan migration retest | ทำงานไร้แผน |
| Work Performance Data | ข้อมูลผลงานจริง | progress, defect, effort, test result | SIT delay 2 weeks | Opinion |
| Change Request | คำขอเปลี่ยนแปลง | ขอปรับ baseline อย่างเป็นทางการ | เพิ่ม approval step ก่อน go-live | Issue |
| Corrective Action | การแก้ให้กลับเข้าแผน | action เพื่อลด variance ที่เกิดแล้ว | เพิ่ม retest cycle | Preventive Action |
| Closing Evidence | หลักฐานการปิดงาน | acceptance, handover, owner, lessons learned | Handover to IT Operations | Closing meeting |

## 19. สรุปหนึ่งหน้า

5 Process Groups คือ Initiating, Planning, Executing, Monitoring & Controlling และ Closing

Process Groups ไม่ใช่ Project Phases; phase คือช่วง lifecycle ส่วน Process Group คือกลุ่มกิจกรรมบริหาร

PM มืออาชีพใช้ Process Groups เพื่อรู้ว่าต้องใช้โหมดบริหารใด ไม่ใช่เพื่อพิสูจน์ว่า “ผ่านขั้นนี้แล้วห้ามย้อน”

ERP ที่ data ownership ยังไม่พร้อมอาจต้องให้บางงาน execute ต่อได้ แต่ data workstream ต้องกลับไป planning พร้อม evidence และ decision owner

Lifecycle and Process Group Map ต้องมี gates, evidence, feedback triggers, owner, closing และ transition เพื่อใช้ต่อใน Lesson 04

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | Project vs Operation Analysis and Value Chain from Lesson 02 |
| Output | Lifecycle and Process Group Map |
| Creator | Learner in Project Planner role |
| Artifact owner | Project Manager |
| Reviewer | PMO and Workstream Leads |
| Approval authority | Project Manager with Sponsor acknowledgement |
| Minimum acceptance | Usable |
| Next lesson use | Lesson 04 ใช้ management activities, decision gates และ feedback loops เพื่อทำ PM Coverage and Cross-impact Map |



<!-- Source: ../chapters/lesson-04/lesson-04-learner.md -->

# Chapter 04 — 10 Project Management Knowledge Areas Overview

## 1. Opening Scenario

โครงการอาจตรงเวลาและไม่เกินงบ แต่ยังล้มเหลวได้ ถ้าผู้ใช้ไม่ยอมใช้ระบบ คุณภาพไม่พอ Vendor ไม่พร้อม หรือไม่มีใครรับผิดชอบ adoption หลัง go-live

คำถามเปิดบทนี้คือ:

```text
ถ้าโครงการตรงเวลาและไม่เกินงบ แต่ผู้ใช้ไม่ยอมใช้ระบบ
โครงการนี้บริหารดีแล้วหรือยัง
```

คำตอบคือ “ยังสรุปไม่ได้” เพราะ Schedule และ Cost เป็นเพียงบางมิติของ Project Health

## 2. Why This Matters

Knowledge Areas คือมุมมองหรือกลุ่มองค์ความรู้ที่ PM ต้องบริหาร ไม่ใช่ department และไม่ใช่ checklist แยกสิบกล่อง

PM ที่มองแค่ timeline อาจเห็น project เป็น green ทั้งที่ stakeholder resistance, data quality, resource overload หรือ procurement risk กำลังสะสมอยู่

Lesson 03 สอนว่า Process Groups บอกว่าเรากำลังบริหาร “ช่วงไหน” ส่วน Lesson 04 สอนว่า Knowledge Areas บอกว่าเรากำลังบริหาร “เรื่องอะไร”

ถ้าเปรียบ project เป็นห้องควบคุม Process Groups คือเข็มนาฬิกาที่บอกว่า project อยู่ช่วงเริ่ม วางแผน ลงมือ ควบคุม หรือปิดงาน ส่วน Knowledge Areas คือหน้าปัดคนละชุดที่บอกสุขภาพของงานในมิติต่าง ๆ เช่น ขอบเขต เวลา ต้นทุน คุณภาพ คน ผู้มีส่วนได้ส่วนเสีย และความเสี่ยง PM ที่ดีต้องอ่านหน้าปัดเหล่านี้พร้อมกัน ไม่ใช่จ้องเฉพาะเวลาหรืองบประมาณ

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้:

1. ระบุ 10 Knowledge Areas ได้ในระดับ overview
2. แยก Process Groups ออกจาก Knowledge Areas
3. อธิบายว่า Integration Management เชื่อมผลกระทบข้ามด้านอย่างไร
4. วิเคราะห์ impact ของ change หนึ่งข้อข้ามหลาย Knowledge Areas
5. สร้าง PM Coverage and Cross-impact Map เพื่อส่งต่อ Lesson 05

## 4. Beginner Safety

บทนี้ยังไม่ลงลึกวิธีสร้าง WBS, critical path, EVM, risk response, contract type หรือ communication plan รายละเอียด

สิ่งที่ต้องตั้งหลักให้ได้คือ PM ไม่ต้องเป็น expert ลึกที่สุดทุกด้าน แต่ต้องเห็นว่าแต่ละด้านกระทบกันอย่างไรและใครต้องตัดสินใจ

## 5. Mental Model

ใช้ภาพจำนี้:

```text
Process Groups = เรากำลังบริหาร "ช่วงไหน"
Knowledge Areas = เรากำลังบริหาร "เรื่องอะไร"
Integration = เรากำลังเชื่อม "ผลกระทบทั้งหมด" อย่างไร
```

## 6. Main Lesson

10 Knowledge Areas ตามกรอบหลักของหลักสูตรคือ:

| # | Knowledge Area | หน้าที่ระดับ overview |
|---|---|---|
| 1 | Integration | เชื่อม decision, baseline, change และผลกระทบ |
| 2 | Stakeholder | ระบุและ engage คนที่มีผลต่อโครงการ |
| 3 | Procurement | บริหาร vendor, contract และการจัดซื้อจัดจ้าง |
| 4 | Resource | จัดคน ทีม เครื่องมือ และ capacity |
| 5 | Communications | ส่งข้อมูลให้ถูกคน ถูกเวลา ถูกความหมาย |
| 6 | Scope | กำหนดและควบคุมสิ่งที่จะส่งมอบ |
| 7 | Schedule | วางและควบคุมเวลา |
| 8 | Cost | ประมาณการ งบประมาณ และควบคุมต้นทุน |
| 9 | Risk | จัดการความไม่แน่นอน |
| 10 | Quality | ทำให้ deliverable ตรง criteria และใช้งานได้ |

ข้อผิดพลาดที่พบบ่อยคือ PM ลิสต์ชื่อครบแต่ไม่เห็น dependency เช่น เพิ่ม scope แล้วคิดว่ากระทบแค่ schedule ทั้งที่อาจกระทบ cost, resource, quality, procurement, stakeholder trust และ risk

การเรียน Knowledge Areas จึงไม่ใช่การท่องจำชื่อ 10 เรื่อง แต่คือการฝึกมอง project แบบเชื่อมโยง ถ้าคำขอใหม่มาจากฝ่ายหนึ่ง PM ต้องถามต่อทันทีว่าใครได้ประโยชน์ ใครต้องทำงานเพิ่ม ใครต้อง approve ข้อมูลอะไรยังไม่พร้อม และผลกระทบไปถึง acceptance หรือ operation หลังส่งมอบหรือไม่

ในโลกจริง ปัญหาส่วนใหญ่ไม่ได้ประกาศตัวชัดเจนว่าเป็นปัญหา "Scope" หรือ "Risk" ตั้งแต่แรก ปัญหาอาจเริ่มจาก requirement เล็ก ๆ แต่กลายเป็น contract change หรือเริ่มจาก vendor delay แล้วไปกระทบ stakeholder trust ดังนั้น Knowledge Areas ทำหน้าที่เป็นแผนที่ให้ PM ไล่ผลกระทบ ไม่ใช่เป็นกล่องให้โยนปัญหาเข้าไปแล้วปิดฝา

## 7. PM Thinking

ใช้ Cross-Knowledge Impact Assessment:

```text
1. ปัญหาเริ่มจาก Knowledge Area ใด
2. กระทบ baseline ใด: scope, schedule, cost, quality
3. กระทบคนและ partner ใด
4. เกิด risk หรือ quality gap ใหม่ไหม
5. ใครเป็น impact owner และใครมี approval authority
6. Integration ต้องเสนอ options อะไร
```

## 8. PM Decision Thinking

Systems thinking และ value delivery ทำให้ PM ต้องดู dependency ไม่ใช่แก้ปัญหาใน silo

```text
Decision: change หรือปัญหาหนึ่งข้อควรถูกประเมินข้าม Knowledge Areas ใดบ้าง
Owner: PM ทำ integrated impact assessment; sponsor/change authority ตัดสินเมื่อกระทบ baseline หรือ value
Inputs: requirement, baseline, contract, resource capacity, stakeholder expectation, risk, quality criteria
Options: accept, defer, split release, add resource, negotiate vendor, adjust scope
Risk: ตัดสินจาก schedule/cost อย่างเดียวจนทำลาย quality หรือ stakeholder trust
Evidence: impact map, decision log, updated risk, acceptance criteria, stakeholder readiness
```

## 9. ERP Worked Example

ERP ของ SIG มี 5 modules, data migration จาก 6 legacy systems, 80 key users, working delivery budget 45 ล้านบาท และ go-live target ก่อน 1 ตุลาคม

ถ้าฝ่าย sales ขอเพิ่ม margin analysis report ก่อน go-live PM ต้องดู:

- Scope: report อยู่ใน baseline หรือเป็น change
- Schedule: build/test เพิ่มกระทบ go-live หรือไม่
- Cost/Procurement: TechConsult ต้องคิดค่าเพิ่มหรือไม่
- Resource: key users และ testers มี capacity พอหรือไม่
- Quality/Risk: data migrate ถูกต้องพอให้ report ใช้ได้หรือยัง
- Stakeholder/Communication: sales, finance และ operations เข้าใจ trade-off หรือไม่
- Integration: PM รวมผลกระทบเป็น options ให้ change authority ตัดสิน

จุดที่ต้องระวังคือ sales อาจเห็น report นี้เป็น requirement จำเป็น ส่วน technical team อาจเห็นเป็นงานเพิ่มที่เสี่ยงต่อ go-live ทั้งสองฝ่ายไม่ได้ผิด แต่พูดจาก Knowledge Area คนละมุม PM ต้องแปลมุมเหล่านั้นให้เป็น decision เดียว เช่น ทำทันทีแต่ตัด scope อื่นออก, เลื่อนเป็น release ถัดไป, หรือทำ manual report ชั่วคราวพร้อม risk control

## 10. Hotel Booking Example or Contrast

Hotel Booking ต้องเพิ่ม direct booking จาก 10% เป็น 35% ภายใน 18 เดือน โดย Phase 1 budget 12 ล้านบาทและ timeline 8 เดือน

ถ้า marketing ขอเพิ่ม corporate booking ก่อน high season:

- Scope เพิ่ม feature ใหม่
- Schedule อาจกระทบ launch ก่อน high season
- Cost/resource เพิ่ม dev, QA และ support effort
- Quality/risk กระทบ payment, inventory และ booking flow
- Stakeholder กระทบ marketing, hotel partners, customers และ operations
- Integration ต้องเสนอ include, defer หรือ replace lower-value scope

ถ้า PM ตอบเพียงว่า “developer ทำทันไหม” จะพลาดคำถามสำคัญกว่า คือ corporate booking ช่วยให้ direct booking ขยับจาก 10% ไป 35% ได้มากกว่า core booking flow หรือไม่ และถ้าทำตอนนี้จะทำให้ payment, inventory หรือ partner onboarding เสี่ยงเกิน threshold หรือเปล่า Knowledge Areas ช่วยให้การถกเถียงไม่กลายเป็นความเห็นส่วนตัวของฝ่ายใดฝ่ายหนึ่ง

## 11. Watch PM Think

PM ไม่ถามแค่ว่า “ทำได้ไหม” แต่ถามว่า “ทำแล้วกระทบอะไร ใครต้องรับผิดชอบ และ decision threshold อยู่ตรงไหน”

ถ้า impact map เขียนว่า “กระทบทุกด้านเล็กน้อย” แต่ไม่มี owner หรือ evidence แปลว่ายังเป็น generic analysis

ประโยคที่ใช้ได้จริงคือ “กระทบ schedule เพราะต้องเพิ่ม SIT 5 วัน เจ้าของ evidence คือ QA Lead; กระทบ cost เพราะ vendor estimate เพิ่ม 600,000 บาท เจ้าของ evidence คือ Procurement; กระทบ stakeholder เพราะฝ่ายขายต้องยอมรับ workaround เจ้าของ engagement คือ Business Owner” การระบุแบบนี้ทำให้แผนที่ผลกระทบกลายเป็นเครื่องมือตัดสินใจ ไม่ใช่รายงานสวย ๆ

## 12. Artifact Example

Artifact ของบทนี้คือ `PM Coverage and Cross-impact Map`

ใช้ template ต้นทางได้ที่ [PM Coverage and Cross-impact Map Template](../../lessons/lesson-04/learner/Artifact-Template.md)

ต้องมี change/decision context, impact ราย Knowledge Area, missing evidence, impact owner, options, recommendation และ approval evidence

## 13. Workshop

Hotel Booking ต้องการเพิ่ม corporate booking ก่อน high season ทั้งที่ Phase 1 มีงบ 12 ล้านบาทและ timeline 8 เดือน

ให้สร้าง one-page cross-impact map โดยมีอย่างน้อย 3 options: include, defer, replace scope และระบุ owner/approval/evidence ที่ต้อง update

## 14. Beginner Checkpoint

ตอบโดยไม่เปิดเฉลย:

1. Knowledge Area ต่างจาก Process Group อย่างไร
2. Integration Management ต่างจากการรวมเอกสารอย่างไร
3. Scope change อาจกระทบ Knowledge Areas ใดบ้าง
4. ทำไม Knowledge Areas ไม่ใช่ department
5. PM ต้องเป็น expert ลึกที่สุดทุกด้านหรือไม่

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย Process Group vs Knowledge Area และบทบาท Integration

### B. Scenario Question

ERP UAT พบ request เพิ่ม approval workflow ให้ระบุ Knowledge Areas ที่ได้รับผลกระทบ

### C. Decision Case

Hotel Booking ขอเพิ่ม corporate booking ก่อน high season ให้เสนอ options, trade-offs และ approval route

### D. Artifact Construction

สร้าง PM Coverage and Cross-impact Map จาก lifecycle/gate ของ Lesson 03

### E. Artifact Review

ตรวจ impact analysis ที่เขียน generic และไม่มี owner แล้วแก้ให้ actionable

### F. Reflection

ระบุ Knowledge Area ที่คุณมักมองข้ามและผลกระทบต่อ value

Assessment นี้เน้น retrieval 10% และ application/judgement/artifact 90%

## 16. เก็บตกท้ายบท

Dashboard ที่เขียวทุกช่องไม่ช่วยถ้าช่องที่วัดไม่ครอบคลุม project health จริง PM ต้องกล้าถามว่า “green ด้านไหน และยัง red ด้านไหน”

ประโยคใช้ในที่ประชุม:

```text
ก่อนตัดสินใจ ขอแยก impact ตาม Knowledge Areas พร้อม owner และ evidence
เพื่อไม่ให้ schedule/cost กลบ risk, quality หรือ stakeholder adoption
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Knowledge Areas คือ department | เป็นมุมมองบริหาร ไม่ใช่ผังองค์กร |
| PM ต้องเก่งที่สุดทุกด้าน | PM ต้อง integrate experts และ evidence |
| Scope change กระทบแค่ scope | มักกระทบหลายด้าน |
| Communication คือส่ง report | ต้องทำให้ผู้เกี่ยวข้องเข้าใจ decision/trade-off |
| Integration คือรวมเอกสาร | คือเชื่อม decision และ impact |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย | ตัวอย่าง Scenario | คำที่มักสับสน |
|---|---|---|---|---|
| Knowledge Area | องค์ความรู้/มุมมองบริหาร | เรื่องที่ PM ต้องดูแล | Scope, Schedule, Risk ใน ERP | Department |
| Integration Management | การบูรณาการ | เชื่อมผลกระทบทุกด้าน | เสนอ change options ต่อ CCB | Document aggregation |
| Cross-impact | ผลกระทบข้ามด้าน | change หนึ่งข้อกระทบหลายด้าน | Corporate Booking กระทบ cost/resource/risk | Single impact |
| Impact Owner | เจ้าของผลกระทบ | คนที่ตอบ evidence ของด้านนั้น | QA owner เรื่อง payment test | Approver |
| Approval Authority | ผู้มีอำนาจอนุมัติ | คน/กลุ่มที่ตัดสินใจตาม threshold | Sponsor/Change Authority | Reviewer |
| Baseline | ฐานควบคุมที่อนุมัติ | scope/schedule/cost ที่ใช้เทียบ | ERP go-live baseline | Estimate |
| Project Health | สุขภาพโครงการ | สถานะหลายมิติรวมกัน | Green schedule แต่ red adoption | Percent complete |

## 19. สรุปหนึ่งหน้า

Knowledge Areas บอกว่า PM ต้องบริหารเรื่องอะไร ส่วน Process Groups บอกว่ากำลังบริหารช่วงไหน

ความสำเร็จไม่ได้อยู่ที่ schedule/cost เท่านั้น แต่รวม stakeholder, quality, risk, resource, procurement และ value

Cross-impact map ที่ดีต้องมี concrete impact, missing evidence, owner, options และ approval route

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | Lifecycle and Process Group Map from Lesson 03 |
| Output | PM Coverage and Cross-impact Map |
| Creator | Learner in Project Manager role |
| Artifact owner | Project Manager |
| Reviewer | Knowledge-area Owners and PMO |
| Approval authority | Change Authority or Sponsor according to decision threshold |
| Minimum acceptance | Usable |
| Next lesson use | Lesson 05 ใช้ dependencies, decision owners และ impacts เพื่อร่าง Charter, Governance และ Change Decision Record |



<!-- Source: ../chapters/lesson-05/lesson-05-learner.md -->

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

ใช้ template ต้นทางได้ที่ [Integration Artifact Pack](../../lessons/lesson-05/learner/Artifact-Template.md)

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



<!-- Source: ../chapters/lesson-06/lesson-06-learner.md -->

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

ใช้ template ต้นทางได้ที่ [Stakeholder Artifact Template](../../lessons/lesson-06/learner/Artifact-Template.md)

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



<!-- Source: ../chapters/lesson-07/lesson-07-learner.md -->

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

ใช้ template ต้นทางได้ที่ [Scope Artifact Pack](../../lessons/lesson-07/learner/Artifact-Template.md)

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



<!-- Source: ../chapters/lesson-08/lesson-08-learner.md -->

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

ใช้ template ต้นทางได้ที่ [Schedule Artifact Pack](../../lessons/lesson-08/learner/Artifact-Template.md)

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



<!-- Source: ../chapters/lesson-09/lesson-09-learner.md -->

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

ใช้ template ต้นทางได้ที่ [Cost Artifact Pack](../../lessons/lesson-09/learner/Artifact-Template.md)

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



<!-- Source: ../chapters/lesson-10/lesson-10-learner.md -->

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

ใช้ template ต้นทางได้ที่ [Quality Artifact Pack](../../lessons/lesson-10/learner/Artifact-Template.md)

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



<!-- Source: ../chapters/lesson-11/lesson-11-learner.md -->

# Chapter 11 — Project Resource Management

## 1. Opening Scenario

ERP ต้องใช้ 80 key users เพื่อทำ UAT แต่ finance และ warehouse ยังต้องปิดงบและดูแลงานประจำตามปกติ Resource plan มีรายชื่อครบ แต่เมื่อถึงเวลาจริง key users ว่างแค่บางช่วง บางคนไม่มี backfill และ functional managers ไม่เคย sign off capacity

นี่คือเหตุผลที่ชื่อคนในแผนไม่เท่ากับ resource ที่พร้อมใช้งาน

Resource Management คือการทำให้บทบาท คน skill capacity authority และ physical resources พร้อมจริงในเวลาที่ project ต้องใช้

## 2. Why This Matters

แผนที่ดีที่สุดยังล้มได้ถ้าคนที่ต้องทำงานไม่ว่าง ไม่มีทักษะ ไม่มีอำนาจตัดสินใจ หรือถูกดึงไปทำงานประจำในช่วง critical

หลายโครงการดูเหมือนมีคนพอใน spreadsheet เพราะทุก task มีชื่อ แต่ชีวิตจริงคนเดียวกันอยู่หลายโครงการ มี BAU duties และไม่มีเวลาพอสำหรับ testing, review หรือ acceptance

PM จึงต้องบริหาร resource ในฐานะข้อจำกัดจริงของ delivery ไม่ใช่ช่องใน template

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. แยก role, person, assignment และ capacity
2. ใช้ RACI เพื่อกำหนด Responsible, Accountable, Consulted และ Informed
3. ประเมิน availability, skill, workload และ ramp-up risk
4. ตัดสินใจ resource gap ด้วย options และ authority ที่ถูกต้อง
5. สร้าง Consolidated Resource Plan, Organization Chart และ RACI

## 4. Beginner Safety

Resource ไม่ใช่เฉพาะคน แต่รวมถึงเครื่องมือ test environment devices licenses meeting rooms และ vendor capacity

RACI ที่ดีควรมี Accountable หนึ่งคนต่อ decision สำคัญ ไม่ใช่ใส่หลายคนเพื่อให้ทุกฝ่ายรู้สึกมีส่วนร่วม เพราะ Accountable หลายคนมักแปลว่าไม่มีใครรับผิดชอบสุดท้ายจริง

PM รวม resource plan ได้ แต่ functional manager เป็นคน commit departmental capacity ส่วน Steering Committee ควรเข้ามาเมื่อมี priority conflict หรือ exception ที่เกินอำนาจปกติ

## 5. Mental Model

```text
Quality Workload
-> Roles and Skills
-> Capacity Commitment
-> RACI
-> Resource Calendar / Histogram
-> Conflict Decision
-> Communication Audiences
```

Lesson 10 บอกว่าต้องมี quality work อะไร Lesson 11 ถามต่อว่าใครจะทำงานนั้น มีเวลาไหม มี skill ไหม และใครตัดสินใจ acceptance

## 6. Main Lesson

Role คือบทบาท เช่น Data Owner, Key User, QA Lead หรือ Release Manager Person คือคนจริงที่รับ role นั้น Assignment คือการมอบหมายงาน ส่วน Capacity คือเวลาหรือกำลังทำงานที่ใช้ได้จริง

RACI ช่วยทำให้ decision clarity:

- Responsible คือคนลงมือทำ
- Accountable คือคนรับผิดชอบผลลัพธ์หรือ decision สุดท้าย
- Consulted คือคนที่ต้องให้ input
- Informed คือคนที่ต้องรับรู้ผล

Resource Calendar แสดง availability ตามเวลา Resource Histogram แสดง demand/load เทียบกับ capacity เมื่อเห็น peak หรือ overload PM จึงเริ่มคุยเรื่อง backfill, overtime, vendor support, training, resequence หรือ scope trade-off ได้ด้วยหลักฐาน

## 7. PM Thinking

เมื่อเจอ resource conflict ให้ถาม:

- gap คือ role, skill, person, capacity หรือ authority
- คนที่ถูก assign ว่างจริงกี่เปอร์เซ็นต์และช่วงใด
- functional manager commit แล้วหรือยัง
- capacity gap กระทบ schedule, quality และ acceptance อย่างไร
- มี backfill หรือ vendor support ได้หรือไม่
- RACI มี Accountable ซ้ำหรือขาดหรือไม่
- ควร escalate เฉพาะ priority conflict ใด

อย่ารีบพูดว่า "เพิ่มคน" เพราะคนเพิ่มโดยไม่มี skill หรือไม่เข้าใจ context อาจเพิ่ม coordination cost มากกว่าช่วยงาน

## 8. PM Decision Thinking

```text
Decision: resource gap นี้ต้อง acquire, reassign, train, backfill, outsource, reduce scope หรือ replan
Owner: PM จัด resource plan; Functional Manager/Sponsor ตัดสิน capacity และ priority conflict
Inputs: RACI, resource calendar, skill matrix, workload, quality plan, schedule, budget, team performance
Options: dedicate, part-time, phased UAT, backfill, overtime, vendor support, defer, scope trade-off
Trade-offs: speed vs ramp-up, expert bottleneck vs quality, team morale vs overtime, cost vs capacity
Evidence: capacity sign-off, resource histogram, RACI approval, updated schedule and decision log
```

PM ที่ดีไม่ขอ resource แบบทั่วไป แต่ขอ capacity ที่เชื่อมกับงานและช่วงเวลาที่ต้องใช้

## 9. ERP Worked Example

ERP มี 80 key users ที่ต้องทำงานคู่กับ BAU ใน finance, sales, warehouse, production และ HR

ถ้า UAT ต้องใช้ 80 key-user test-days แต่ finance month-end close ซ้อนกัน PM ต้องทำให้เห็น workload และ impact อย่างเป็นรูปธรรม

ทางเลือกอาจเป็น:

- phased UAT ตาม module หรือ process
- backfill งานประจำช่วง UAT
- ขอ key users บางกลุ่ม dedicated 50% ใน 4 สัปดาห์
- เพิ่ม vendor support สำหรับ test preparation
- เลื่อน UAT wave ที่กระทบ month-end มากที่สุด

แต่ capacity commitment ต้องมาจาก functional managers ไม่ใช่ PM สั่งเอง

## 10. Hotel Booking Example or Contrast

Hotel Booking ใช้ cross-functional team เช่น Product, UX, Mobile, Web, Backend, QA, DevOps, Marketing, Hotel Operation และ Support

เมื่อ payment defect ใช้ backend และ QA capacity มาก ทีมอาจต้องจำกัด WIP หยุด promotion feature ชั่วคราว หรือเพิ่ม regression testing ก่อน launch

การบริหาร resource ใน Agile environment ไม่ได้แปลว่าไม่มี planning แต่แปลว่าต้องดู flow, bottleneck และ team capacity บ่อยขึ้น

## 11. Watch PM Think

ลำดับคิด:

1. เริ่มจากงานที่ต้องส่งมอบและ quality workload
2. ระบุ role และ skill ที่จำเป็น
3. ตรวจ person assignment และ capacity จริง
4. ทำ RACI ให้ decision owner ชัด
5. หา overload ด้วย calendar/histogram
6. เสนอ options พร้อม cost/schedule/quality impact
7. บันทึก capacity sign-off และ escalation decision

ถ้า RACI ไม่มี Accountable หรือ capacity ไม่มี sign-off resource plan ยังไม่ usable

## 12. Artifact Example

Artifact ของบทนี้คือ:

- Consolidated Resource Plan
- Organization Chart
- RACI
- Capacity Commitment and Exception Log

ใช้ template ต้นทางได้ที่ [Resource Artifact Template](../../lessons/lesson-11/learner/Artifact-Template.md)

Artifact นี้ส่งต่อ Lesson 12 เพราะ communication plan ต้องรู้ว่าใครเป็น audience ใครต้องตัดสินใจ ใครต้องให้ input และ escalation path อยู่ที่ไหน

## 13. Workshop

ERP UAT Capacity Decision: key users 80 คนมี BAU duties และยังไม่มี backfill cost ให้สร้าง resource decision brief:

- role/resource gap
- RACI impact
- capacity evidence
- options เช่น phased UAT, backfill, overtime, vendor support หรือ reschedule
- owner และ authority
- exception ที่ต้องส่ง Steering Committee

ข้อจำกัด: PM cannot approve a functional department's resource commitment

## 14. Beginner Checkpoint

1. Role ต่างจาก person อย่างไร
2. Capacity commitment ต้องอนุมัติโดยใคร
3. RACI ทำไมควรมี Accountable หนึ่งคน
4. Resource histogram ใช้ตัดสินใจอย่างไร
5. ควร escalate เรื่องใดไป Steering Committee

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่าง

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย role, person, assignment, capacity, RACI, resource calendar และ resource histogram

### B. Scenario Question

ERP finance key users ไม่ว่าง UAT เพราะ month-end close ให้เสนอ resource options และ authority ที่ถูกต้อง

### C. Decision Case

Hotel Booking QA/backend ไม่พอเพราะ payment defect ให้ปรับ flow, WIP, release scope หรือ resource plan อย่างไร

### D. Artifact Construction

สร้าง Consolidated Resource Plan, Organization Chart และ RACI จาก quality/test workload

### E. Artifact Review

ตรวจ resource plan ที่มีชื่อคนครบแต่ไม่มี capacity, skill, authority หรือ sign-off แล้วแก้ให้ usable

### F. Reflection

เขียนไม่เกิน 180 คำว่า resource conflict ที่ดีควรถูก escalate อย่างไรโดยไม่โยนทุกเรื่องให้ Steering Committee

Assessment นี้เน้น resource-plan artifact review 35%, trade-off 35%, conflict/leadership case 20% และ recall 10%

## 16. เก็บตกท้ายบท

ประโยคที่ควรจำ:

```text
มีชื่อในแผนไม่ได้แปลว่ามี capacity
มี capacity ไม่ได้แปลว่ามี authority
และมี authority ไม่ได้แปลว่ามี skill
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| ใส่ชื่อคนครบคือมี resource | ต้องมี capacity, skill และ authority |
| PM อนุมัติ capacity แผนกได้เอง | Functional Manager ต้อง commit |
| RACI คือเอกสาร HR | RACI คือ decision clarity |
| เพิ่มคนแก้ทุกอย่าง | อาจเพิ่ม ramp-up และ coordination load |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Resource Management | บริหารทรัพยากร | ทำให้คน/สิ่งของพร้อมใช้งาน |
| RACI | ตารางบทบาท | Responsible, Accountable, Consulted, Informed |
| Capacity | กำลังทำงานจริง | เวลาและพลังงานที่ใช้ได้ |
| Resource Calendar | ปฏิทินทรัพยากร | availability ตามเวลา |
| Resource Histogram | แผนภาพโหลดทรัพยากร | demand/capacity ตามช่วงเวลา |
| Backfill | คนทดแทนงานประจำ | ลด BAU impact |

## 19. สรุปหนึ่งหน้า

Resource Management ทำให้แผนกลายเป็นงานจริงผ่านคน skill capacity และ authority

PM ต้องเห็น bottleneck ก่อนกลายเป็น delay และต้องแยก capacity commitment จากรายชื่อคนในแผน

RACI ไม่ใช่เอกสาร HR แต่เป็นเครื่องมือทำให้ decision owner ชัดและสื่อสารต่อใน Lesson 12 ได้ถูกคน

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | Quality and acceptance evidence from Lesson 10 |
| Output | Consolidated Resource Plan, Organization Chart and RACI |
| Owner | PM |
| Approval | PM for consolidated plan; Functional Managers for capacity; Steering Committee for exceptions |
| Next lesson use | Lesson 12 ใช้ approved RACI, audiences, accountable roles และ escalation path เพื่อสร้าง Communication Plan |



<!-- Source: ../chapters/lesson-12/lesson-12-learner.md -->

# Chapter 12 — Project Communications Management

## 1. Opening Scenario

ERP data migration เป็นสีแดง แต่ weekly email แสดงเพียง percentage complete ผู้บริหารอ่านแล้วไม่รู้ว่าต้องตัดสินใจอะไร ภายในเมื่อไร และถ้าไม่ตัดสินใจ cutover จะเสี่ยงอย่างไร

ทีม project บอกว่า "ส่งรายงานไปแล้ว" แต่ Sponsor ตอบว่า "ไม่เคยรู้ว่าต้องตัดสินใจเรื่องนี้"

นี่คือความต่างระหว่างการส่งข้อมูลกับการสื่อสารที่ทำให้เกิดความเข้าใจและ action

## 2. Why This Matters

Project Communications Management ไม่ใช่การส่งรายงานให้ครบ distribution list แต่คือการทำให้ข้อมูลที่ถูกต้องไปถึงคนที่ถูกต้องในเวลาที่ถูกต้อง ผ่านช่องทางที่เหมาะสม และนำไปสู่ความเข้าใจ การตัดสินใจ หรือ action ที่ต้องการ

PM ใช้เวลาส่วนใหญ่กับการสื่อสาร แต่การสื่อสารที่มากขึ้นไม่ได้แปลว่าดีขึ้น หากข้อความไม่ชัด ผู้รับไม่ใช่คนตัดสินใจ หรือไม่มี feedback loop

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. แยก data, information, communication, status report และ decision brief
2. เลือก push, pull หรือ interactive communication ให้เหมาะกับผู้รับและสถานการณ์
3. ออกแบบ communication plan จาก stakeholder need, decision need และ feedback loop
4. สร้าง escalation message ที่มี decision ask, evidence และ response record
5. สร้าง Communication Plan, Cadence และ Status Report

## 4. Beginner Safety

ส่ง email แล้วไม่ใช่หลักฐานว่าการสื่อสารสำเร็จ ถ้าไม่มี acknowledgement, decision, action หรือ feedback loop

กับดักอีกอย่างคือส่งข้อมูลชุดเดียวให้ทุก stakeholder ผู้บริหารต้องการ decision brief ทีมงานต้องการ detail ผู้ใช้ต้องการ next action ส่วน vendor ต้องการ defect clarification ถ้าทุกคนได้รายงานเดียวกัน อาจไม่มีใครได้สิ่งที่ต้องใช้จริง

## 5. Mental Model

```text
RACI / Audience
-> Decision Need
-> Message
-> Channel and Cadence
-> Feedback / Acknowledgement
-> Decision or Escalation Record
-> Risk Signal
```

Lesson 11 บอกว่าใครมีบทบาทและอำนาจ Lesson 12 ถามต่อว่าแต่ละคนต้องได้ข้อมูลอะไรเพื่อทำหน้าที่นั้น

## 6. Main Lesson

Data คือสัญญาณดิบ เช่น defect count หรือ percentage complete Information คือ data ที่ถูกจัดให้มีความหมาย Communication คือการส่งสารให้เกิดความเข้าใจและ action

Status Report บอกสถานะตามรอบ Decision Brief ขอการตัดสินใจที่มีขอบเขตชัด เช่น ขอเลือก recovery option ภายในวันศุกร์

รูปแบบการสื่อสารหลัก:

- Push Communication: ส่งข้อมูลออกไป เช่น email, report, announcement
- Pull Communication: ให้ผู้รับดึงข้อมูลเอง เช่น dashboard, wiki, repository
- Interactive Communication: สื่อสารสองทาง เช่น meeting, workshop, call

แผนสื่อสารแบบ 5W1H ควรตอบว่าใครต้องรู้อะไร ทำไม เมื่อไร ผ่านช่องทางใด ใครเป็น owner และ feedback จะถูกจับอย่างไร

## 7. PM Thinking

เมื่อต้องสื่อสารเรื่องสำคัญ ให้ถาม:

- audience ต้องตัดสินใจหรือทำอะไร
- message ควรเป็นข้อมูล สถานะ recommendation หรือ decision brief
- urgency, complexity และ sensitivity เหมาะกับ channel ใด
- ใครเป็น message owner
- ต้องได้ response ภายในเมื่อไร
- acknowledgement, decision และ escalation จะถูกบันทึกที่ไหน

การสื่อสารที่ดีเริ่มจากผู้รับ ไม่ใช่จากสิ่งที่ PM อยากส่ง

## 8. PM Decision Thinking

```text
Decision: เรื่องนี้ควรสื่อสารแบบ dashboard-only, targeted brief, workshop หรือ escalation
Owner: PM ออกแบบ communication system; message owner ส่งสารเฉพาะเรื่อง
Inputs: stakeholder needs, RACI, urgency, complexity, sensitivity, decision required, channel effectiveness
Options: executive summary, dashboard, workshop, meeting, email, read-back, issue escalation
Trade-offs: speed vs understanding, detail vs attention, transparency vs noise
Evidence: communication matrix, distribution record, acknowledgement, decision log, escalation response
```

Dashboard ที่มีสีแดงไม่ใช่ escalation หากไม่มี decision ask และ response record

## 9. ERP Worked Example

ERP มี Sponsor คุณสมชาย, PM คุณเอก, TechConsult, 80 key users และหลาย functional managers

Data migration risk ไม่ควรถูกซ่อนอยู่ใน weekly email หน้า 7 Steering Committee ควรได้รับ one-page decision brief ที่ระบุ:

- decision required by Friday
- impact on cutover and go-live
- three recovery options
- recommendation
- evidence confidence
- consequence if no decision

ส่วน workstream team ต้องได้ defect detail รายวัน key users ต้องได้ UAT impact และ functional managers ต้องเห็น capacity implication

## 10. Hotel Booking Example or Contrast

Hotel Booking มี PO คุณนภา, PM คุณสุทธิ, marketing, product team, hotel partners และ operations

Payment incident ก่อน launch campaign ต้องสื่อสารหลายชั้น Product team ต้องรู้ technical action PO ต้องรู้ release decision Marketing ต้องรู้ campaign risk Hotel partners ต้องรู้ rollout impact Operations/support ต้องมี known issues และ escalation path

ลูกค้าไม่จำเป็นต้องรู้ technical detail ทั้งหมด แต่ถ้ามี service impact ต้องมี message ที่ชัด ซื่อสัตย์ และไม่สร้างความสับสน

## 11. Watch PM Think

ลำดับคิดของ PM:

1. เริ่มจาก RACI และ stakeholder need
2. แยก data, information, status และ decision ask
3. เลือก audience ตามอำนาจและ action ที่ต้องการ
4. เลือก channel ตาม urgency/complexity
5. กำหนด cadence และ owner
6. บันทึก acknowledgement, decision และ escalation
7. ส่งต่อ risk signal ให้ Lesson 13

ถ้า communication artifact ไม่มี decision need หรือ feedback loop ยังไม่ควรถือว่า usable

## 12. Artifact Example

Artifact ของบทนี้คือ:

- Communication Plan
- Cadence
- Status Report
- Decision/Escalation Log

ใช้ template ต้นทางได้ที่ [Communication Artifact Template](../../lessons/lesson-12/learner/Artifact-Template.md)

Artifact นี้ส่งต่อ Lesson 13 เพราะ risk ที่ไม่ได้ถูกสื่อสารให้ถูกคนทันเวลา จะกลายเป็น issue ที่องค์กรรับมือช้า

## 13. Workshop

เปลี่ยน ERP technical red status ให้เป็น executive decision brief หนึ่งหน้า:

- audience
- decision need
- message
- evidence
- options
- channel/cadence
- owner
- response deadline
- decision/escalation record

ข้อจำกัด: Sponsor อนุมัติ communication plan/cadence ส่วน PM อนุมัติ recurring status report

## 14. Beginner Checkpoint

1. Data ต่างจาก information อย่างไร
2. Status report ต่างจาก decision brief อย่างไร
3. Push, pull และ interactive ใช้ต่างกันอย่างไร
4. Sponsor อนุมัติอะไร และ PM อนุมัติอะไร
5. Escalation ที่ดีต้องมีอะไร

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่าง

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย data, information, communication, push, pull, interactive, status report และ decision brief

### B. Scenario Question

ERP data migration red status ต้องสื่อสารกับ Steering Committee, workstream, key users และ functional managers ต่างกันอย่างไร

### C. Decision Case

Hotel Booking payment incident ก่อน launch campaign ให้เลือก channel และ message สำหรับ PO, marketing, partners, customers และ support

### D. Artifact Construction

สร้าง Communication Plan, Cadence และ Status Report โดยใช้ approved RACI จาก Lesson 11

### E. Artifact Review

ตรวจ weekly report ที่มีเปอร์เซ็นต์แต่ไม่มี decision ask, owner, deadline หรือ escalation path แล้วแก้ให้ใช้ตัดสินใจได้

### F. Reflection

เขียนไม่เกิน 180 คำว่า "ส่งแล้ว" ต่างจาก "สื่อสารสำเร็จ" อย่างไร

Assessment นี้เน้น executive communication 40%, communications-plan artifact review 30%, channel/cadence trade-off 20% และ recall 10%

## 16. เก็บตกท้ายบท

ประโยคที่ควรจำ:

```text
Communication สำเร็จเมื่อผู้รับเข้าใจ ตัดสินใจ หรือดำเนินการได้
ไม่ใช่เมื่อผู้ส่งกด send
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Communication คือส่งข้อมูล | Communication คือ shared understanding plus action |
| Dashboard คือ escalation | Escalation ต้องมี decision ask และ response record |
| รายงานเดียวพอสำหรับทุกคน | ต้อง tailor ตาม audience และ decision need |
| ส่งแล้วคือเสร็จ | ต้อง monitor acknowledgement/action |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Communications Plan | แผนสื่อสาร | ผู้รับ ข้อมูล ความถี่ ช่องทาง owner |
| Push Communication | ส่งออก | email/report/announcement |
| Pull Communication | ดึงเอง | dashboard/wiki/repository |
| Interactive Communication | สองทาง | meeting/workshop/call |
| Status Report | รายงานสถานะ | บอกสถานะตามรอบ |
| Decision Brief | บันทึกขอตัดสินใจ | ขอ decision พร้อม evidence/deadline |
| Escalation | การยกระดับ | ส่งเรื่องให้ authority ตัดสิน |

## 19. สรุปหนึ่งหน้า

Communications Management คือการออกแบบให้ข้อมูลถูกคน ถูกเวลา ถูกช่องทาง และทำให้เกิดความเข้าใจหรือ action

PM ต้องแยก status report ออกจาก decision brief และต้องบันทึก acknowledgement, decision และ escalation

Lesson 12 คือสะพานไป Lesson 13 เพราะ risk ที่ไม่ถูกสื่อสารจะถูกจัดการไม่ทัน

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | Approved RACI and resource commitments from Lesson 11 |
| Output | Communication Plan, Cadence and Status Report |
| Owner | PM |
| Approval | Sponsor for plan/cadence; PM for each status report |
| Next lesson use | Lesson 13 ใช้ status signals and escalation path เพื่อแปลง uncertainty เป็น risk, response และ trigger |



<!-- Source: ../chapters/lesson-13/lesson-13-learner.md -->

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

ใช้ template ต้นทางได้ที่ [Risk Artifact Template](../../lessons/lesson-13/learner/Artifact-Template.md)

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



<!-- Source: ../chapters/lesson-14/lesson-14-learner.md -->

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

ใช้ template ต้นทางได้ที่ [Procurement Artifact Template](../../lessons/lesson-14/learner/Artifact-Template.md)

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



<!-- Source: ../chapters/lesson-15/lesson-15-learner.md -->

# Chapter 15 — Agile Project Management: Scrum and Kanban

## 1. Opening Scenario

Hotel Booking มี payment risk ที่กระทบ MVP checkout ขณะเดียวกัน marketing ขอ promotion feature เพิ่มเข้ามาก่อน launch ถ้า team รับทุกอย่างเข้า sprint โดยไม่ปกป้อง sprint goal สิ่งที่สำคัญที่สุดต่อการจองและชำระเงินอาจไม่เสถียรพอ

ทีมอาจบอกว่า "เรา Agile อยู่แล้ว เปลี่ยนได้ตลอด" แต่ Agile ไม่ได้แปลว่าเปลี่ยนทุกอย่างโดยไม่มีวินัย Agile ที่ดีต้องมี priority, feedback, Definition of Done และความรับผิดชอบที่ชัดเจน

บทนี้จึงสอน Agile ในฐานะวิธีทำงานที่เรียนรู้เร็วขึ้น ไม่ใช่ข้ออ้างในการเลิกวางแผน

## 2. Why This Matters

โลกของ project ไม่ได้มีแต่ predictive plan ที่นิ่งตั้งแต่ต้น บางงานต้องเรียนรู้จากผู้ใช้จริง ทดลอง release สั้น ๆ และปรับ backlog ตาม evidence

แต่การทำ Agile แบบมีแต่พิธีกรรม เช่น standup, sprint และ board โดยไม่มี product ownership, feedback หรือ delivery discipline จะกลายเป็น Agile theater คือดูเหมือน Agile แต่ไม่ช่วยส่ง value

PM มืออาชีพจึงต้องเข้าใจว่า Scrum, Kanban และ predictive governance ใช้ต่างกันอย่างไร และควรรวมกันอย่างไรโดยไม่ทำให้ control หลุด

## 3. Learning Objectives

เมื่อจบบทนี้ คุณควรทำได้ดังนี้

1. อธิบาย Agile mindset โดยไม่ตีความว่าไม่มีแผน
2. แยก Scrum, Kanban และ predictive governance
3. ใช้ Product Backlog, Flow Board และ Definition of Done อย่างมี owner
4. ปกป้อง sprint goal ด้วย product priority และ risk evidence
5. สร้าง Product Backlog, Flow Board และ Feedback Evidence เพื่อส่งต่อ Lesson 16

## 4. Beginner Safety

Agile ไม่ได้แปลว่าไม่มีเอกสาร ไม่มีแผน ไม่มี PM skill หรือเปลี่ยน scope ได้ทุกวันโดยไม่มีผลกระทบ

Agile แปลว่าทีมทำงานเป็นรอบสั้น ส่งมอบสิ่งที่ตรวจได้ รับ feedback และปรับแผนตาม evidence โดยยังรักษา quality, risk และ governance ให้พอดีกับบริบท

คำศัพท์ใหม่คือ Agile Mindset, Product Backlog, Sprint Goal, Product Owner, Scrum Master, Definition of Done, Kanban, WIP Limit, Flow Policy และ Feedback Evidence

## 5. Mental Model

```text
Uncertainty / Value Question
-> Backlog Priority
-> Sprint or Flow Policy
-> Working Increment / Flow Item
-> Feedback Evidence
-> Adaptation
-> Governance Check
```

Agile ไม่ได้ตัด governance ทิ้ง แต่เปลี่ยน cadence ของการเรียนรู้และตัดสินใจให้สั้นลง

## 6. Main Lesson

Scrum เหมาะกับ product development ที่ต้องส่งมอบ increment เป็นรอบ มี Product Owner จัดลำดับ backlog, Scrum Master ช่วยให้ทีมทำงานตาม Scrum, และ Developers ส่ง increment ตาม Sprint Goal

Scrum events เช่น Sprint Planning, Daily Scrum, Sprint Review และ Retrospective ไม่ใช่พิธีเพื่อให้ดู Agile แต่เป็นจังหวะวางแผน ตรวจ feedback และปรับปรุง

Kanban เหมาะกับงาน flow/support/incident ที่เข้ามาต่อเนื่อง เช่น defect triage, payment incident, support request หรือ data migration issue Kanban ใช้ visual board, Work in Progress limit, explicit policy และ flow metrics เพื่อจัดการ bottleneck

Flow Board คือ visual board ที่ทีมใช้บริหาร Kanban จริง แสดงสถานะงานแต่ละชิ้นตาม column เช่น To Do, In Progress, Review และ Done พร้อม WIP limit และ policy กำกับแต่ละ column เพื่อให้เห็น bottleneck และ owner ของแต่ละงานชัดเจน ไม่ใช่กระดานที่มีแค่ sticky note ไล่งานโดยไม่มี policy กำกับ

Predictive governance ยังสำคัญเมื่อ scope ชัด contract เข้ม compliance สูง หรือ baseline ต้องควบคุม เช่น ERP migration, procurement, budget และ cutover

## 7. PM Thinking

เมื่อเลือก Agile practice ให้ถาม:

- งานนี้มี uncertainty สูงหรือไม่
- ต้องเรียนรู้จาก user feedback บ่อยแค่ไหน
- PO มี authority จัด priority จริงหรือไม่
- Definition of Done รวม quality/security/acceptance หรือยัง
- งานเป็น sprint feature หรือ flow/support incident
- Vendor/contract constraints จำกัดวิธีทำงานอย่างไร
- Governance/risk control ใดยังต้องมี

Agile ที่ไม่มี owner และ feedback evidence จะกลายเป็นแค่ board ที่สวย

## 8. PM Decision Thinking

```text
Decision: งานนี้ควรใช้ Scrum, Kanban, predictive governance หรือ hybrid practice
Owner: PO จัดลำดับ value; Delivery Team ดู flow; PM ดู governance, risk และ stakeholder alignment
Inputs: requirement uncertainty, release cadence, team maturity, compliance, dependency, support demand, Definition of Done
Options: sprint delivery, Kanban flow, predictive control, hybrid by workstream, defer item, split release
Trade-offs: flexibility vs predictability, speed vs quality, learning vs governance overhead
Evidence: backlog decision, board policy, WIP data, review feedback, release readiness, risk control
```

คำตอบที่ดีต้องแยก ownership: PO ไม่ควรเป็นเจ้าของ flow operational ทุกเรื่อง และ PM ไม่ควรจัด priority product แทน PO โดยไม่มี governance

## 9. ERP Worked Example

ERP โดยรวมอาจใช้ predictive/hybrid governance เพราะมี contract, modules, migration, budget และ go-live deadline แต่บาง workstream ใช้ Agile practices ได้

ตัวอย่าง:

- Kanban board สำหรับ defect flow ระหว่าง SIT และ data migration
- Daily standup 15 นาทีระหว่าง TechConsult และทีมคุณเอกเพื่อเห็น blockers
- Sprint-like feedback สำหรับ configuration prototype
- Review session กับ key users เพื่อยืนยัน process fit ก่อน UAT ใหญ่

ข้อควรระวังคืออย่าเรียกทั้ง ERP ว่า Agile เพียงเพราะใช้ board หรือ standup หาก approval, baseline, procurement และ cutover ยัง predictive อยู่

## 10. Hotel Booking Example or Contrast

Hotel Booking เหมาะกับ Scrum/Kanban มากกว่า ERP เพราะต้องเรียนรู้จาก user behavior, conversion, payment failure และ partner feedback

เมื่อ payment resilience กระทบ MVP checkout และ marketing ขอ promotion feature PO ควรจัด priority โดยดู outcome evidence ถ้า payment risk ยังสูง promotion ควรเลื่อนลง backlog หรือ split ออกเป็น phase หลัง core booking path เสถียร

Kanban อาจใช้กับ payment incident และ support flow ส่วน Scrum ใช้กับ feature development ที่ส่ง increment เป็น sprint

## 11. Watch PM Think

ลำดับคิด:

1. ระบุส่วนของงานที่ต้องเรียนรู้เร็ว
2. แยก feature work ออกจาก flow/support work
3. ตรวจ ownership: PO, Delivery Team, PM, Release Authority
4. ตรวจ Definition of Done ว่ารวม quality/security/acceptance
5. ใช้ feedback evidence ปรับ backlog
6. จำกัด WIP เมื่อ bottleneck เกิด
7. เก็บ governance/risk control ที่ยังจำเป็น

ถ้าทีมมี ceremony ครบแต่ไม่มี feedback ที่เปลี่ยน decision แปลว่ายังไม่ Agile จริง

## 12. Artifact Example

Artifact ของบทนี้คือ:

- Product Backlog
- Flow Board
- Feedback Evidence
- Board Policy
- Release Authority record

ใช้ template ต้นทางได้ที่ [Agile Artifact Template](../../lessons/lesson-15/learner/Artifact-Template.md)

Artifact นี้ส่งต่อ Lesson 16 เพราะ tailoring ต้องดูว่า agile practice ใดใช้กับ workstream ใดและมี control อะไร

## 13. Workshop

Protect the Hotel Booking Sprint Goal:

payment risk threatens MVP checkout while marketing requests a promotion feature. ให้สร้าง:

- updated backlog
- sprint goal decision
- flow board policy
- blocker response
- feedback request
- Definition of Done check
- governance/risk control ที่ยังต้องมี

ข้อจำกัด: ห้ามให้ PM, PO และ team เป็น co-owner ทุก artifact แบบไม่แยกบทบาท

## 14. Beginner Checkpoint

1. Agile ต่างจากการไม่มีแผนอย่างไร
2. Scrum เหมาะกับงานแบบใด
3. Kanban เหมาะกับงานแบบใด
4. Product Owner เป็น owner ของอะไร
5. Definition of Done ควรรวมอะไรบ้าง

ผ่านเมื่ออธิบายได้อย่างน้อย 4 ข้อพร้อมตัวอย่าง

## 15. End-of-Chapter Assessment

### A. Concept Check

อธิบาย Agile mindset, Scrum, Kanban, Product Backlog, Sprint Goal, WIP limit และ Definition of Done

### B. Scenario Question

Hotel Booking payment risk กับ promotion feature ให้จัด backlog priority พร้อมเหตุผล

### C. Decision Case

ERP ใช้ Agile practices ตรงไหนได้โดยไม่ทำให้ predictive governance หลุด

### D. Artifact Construction

สร้าง Product Backlog, Flow Board และ Feedback Evidence จาก L14 acceptance/contract constraints

### E. Artifact Review

ตรวจ Agile board ที่มีงานเต็มแต่ไม่มี WIP policy, owner, blocker หรือ feedback evidence แล้วแก้ให้ usable

### F. Reflection

เขียนไม่เกิน 180 คำว่า Agile theater ต่างจาก Agile ที่ส่ง value จริงอย่างไร

Assessment นี้เน้น sprint-goal decision 40%, backlog artifact review 30%, predictability-versus-flexibility trade-off 20% และ recall 10%

## 16. เก็บตกท้ายบท

ประโยคที่ควรจำ:

```text
Agile ไม่ใช่การไม่มีวินัย
Agile คือวินัยที่สั้น เร็ว และเรียนรู้จาก evidence จริง
```

## 17. Common Mistakes and Misconceptions

| Misconception | Correction |
|---|---|
| Agile ไม่มีแผน | Agile วางแผนบ่อยและปรับจาก feedback |
| Agile ไม่ต้องเอกสาร | เอกสารยังมี แต่พอดีกับ value และ risk |
| Ceremony คือ Agile | Agile อยู่ที่ learning loop และ value delivery |
| Agile ไม่มี PM skill | Integration, risk, stakeholder และ governance ยังจำเป็น |

## 18. คลังคำศัพท์ประจำบท

| English Term | คำแปลไทย | ความหมายแบบเข้าใจง่าย |
|---|---|---|
| Agile | แนวคิดคล่องตัว | เรียนรู้และส่ง value เป็นรอบ |
| Product Backlog | รายการงาน product | งานเรียงตาม priority/value |
| Sprint Goal | เป้าหมาย sprint | focus ของรอบส่งมอบ |
| Product Owner | เจ้าของ product priority | ตัดสินลำดับ value |
| Definition of Done | เกณฑ์เสร็จ | เงื่อนไขว่างานเสร็จจริง |
| Kanban | วิธีบริหาร flow | เห็นงาน จำกัด WIP และแก้ bottleneck |
| Flow Board | บอร์ดบริหาร flow | visual board ที่มี column, WIP limit และ policy กำกับ |
| WIP Limit | จำกัดงานค้าง | ป้องกันทีมรับงานเกิน capacity |

## 19. สรุปหนึ่งหน้า

Agile คือการส่งมอบ value เป็นรอบสั้น เรียนรู้จาก feedback และปรับตัวอย่างมีวินัย

Scrum เหมาะกับ product increment ส่วน Kanban เหมาะกับ flow/support/incident work

ERP อาจใช้ agile practices บางส่วนใน hybrid governance ส่วน Hotel Booking ใช้ Agile มากกว่าเพราะต้องเรียนรู้จาก market และ user behavior

## 20. Artifact Handoff

| Field | Handoff |
|---|---|
| Input | L14 acceptance and contract constraints |
| Output | PO-owned backlog, Delivery Team-owned flow board and feedback evidence |
| Owner | PO for priority; Delivery Team for operational flow; release authority recorded separately |
| Next lesson use | Lesson 16 ใช้ Agile tools เป็นตัวเลือกใน tailored predictive/agile/hybrid approach |



<!-- Source: ../chapters/lesson-16/lesson-16-learner.md -->

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

ใช้ template ต้นทางได้ที่ [Tailored Hybrid Delivery Plan](../../lessons/lesson-16/learner/Artifact-Template.md)

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



<!-- Source: ../capstone/capstone-learner.md -->

# Capstone — Full Project Management Handover and Launch

## Purpose

เลือกหนึ่งเส้นทางหลัก:

- ERP Full Project Management Handover Package
- Hotel Booking Full Delivery and Launch Package

ส่งลิงก์แบบ relative ไปยัง artifact ต้นทางจาก Lessons 02-16 โดยไม่ต้องคัดลอก artifact เหล่านั้นเข้ามาใน capstone submission

## Sequential Release Gates

1. Artifact completeness: required manifest links, governance role and approval evidence exist; every artifact is at least `Usable`
2. Scenario consistency: facts match scenario master; ERP Working Budget 45 ล้านบาท remains distinct from Funding Envelope 60 ล้านบาท
3. Integration: decisions remain consistent across scope, schedule, cost, quality, resource, communication, risk, procurement, Agile and tailoring
4. Executive defense: deliver a 10-minute brief plus 10-minute questions covering decisions, trade-offs, critical risks and readiness recommendation

## Primary Track Manifest

ใช้ template ต้นทางที่ [Primary Track Submission Manifest Template](../../capstone/learner/Primary-Track-Submission-Manifest-Template.md)

| Requirement | Canonical artifact link (no copy) | Owner / approver | Acceptance/evidence | Gate |
|---|---|---|---|---|
| Business need, charter and benefits | Lessons 02/05 artifacts | Sponsor / PM | approved charter/value evidence | 1-3 |
| Scope/WBS, schedule and cost baseline | Lessons 07-09 artifacts | PM / Sponsor | baseline and forecast evidence | 1-3 |
| Quality and acceptance | Lesson 10 artifact | Business Owner / Quality Manager | signed acceptance criteria | 1-3 |
| Resource plan and RACI | Lesson 11 artifact | PM / Functional Managers | capacity and RACI sign-off | 1-3 |
| Communication/status evidence | Lesson 12 artifact | Sponsor / PM | distribution, decision and escalation records | 1-3 |
| Risk/issue/change evidence | Lesson 13 artifact | Risk Owners / PM / Change Authority | trigger, response and CR IDs | 1-3 |
| Procurement/vendor acceptance | Lesson 14 artifact | Procurement Authority / PM | accepted deliverable and payment evidence | 1-3 |
| Backlog/flow/feedback | Lesson 15 artifact where applicable | PO / Delivery Team | priority and feedback evidence | 1-3 |
| Tailored hybrid delivery plan | Lesson 16 artifact | Sponsor / Steering Committee | rationale, trigger and cadence | 1-3 |
| Cutover/launch/handover and benefit owner | Final handover record | Operations / Benefit Owner | readiness recommendation | 1-4 |

## Comparative Tailoring Memo

สำหรับ scenario ที่ไม่ได้เลือกเป็น primary track ให้เขียน memo 3-5 หน้าเพื่อเปรียบเทียบ:

- delivery approach by workstream
- predictive controls retained
- Agile or flow practices used
- decision triggers and review cadence
- governance owner and approval authority

ใช้ template ต้นทางที่ [Comparative Tailoring Memo Template](../../capstone/learner/Comparative-Tailoring-Memo-Template.md)

## Executive Defense Brief

ใช้ template ต้นทางที่ [Executive Defense Brief Template](../../capstone/learner/Executive-Defense-Brief-Template.md)

ข้อเสนอสุดท้ายต้องเป็นหนึ่งในสามทางเลือก:

- Go
- Conditional Go
- No-go

ระบุหลักฐาน ความเสี่ยงที่ยังไม่ปิด decision ที่ต้องขอ และเจ้าของ benefit realization ให้ชัดเจน

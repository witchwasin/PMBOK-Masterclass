---
chapter: lesson-01
title: ทำไม Project Manager ต้องรู้ PMBOK
edition: Learner
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-01/
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
---

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

ใช้ template ต้นทางได้ที่ [PM Learning Baseline Template](../../../lessons/lesson-01/learner/Artifact-Template.md)

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

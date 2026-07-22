---
lesson: 15
sequence: 15.2
title: Agile Project Management Frameworks (Scrum and Kanban)
document_type: Lesson
difficulty: Core
estimated_study_time: 90
status: Active
validation_status: Validated
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 14 — Project Procurement Management
related_lessons:
  - Lesson 16 — Predictive vs Agile vs Hybrid and Tailoring
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 15_2 — Agile Project Management Frameworks (Scrum and Kanban)

## Beginner Safety

- **ควรรู้แล้ว:** L14 acceptance and contract constraints; **คำศัพท์ใหม่:** backlog, flow, increment.
- **Novice trap:** ใช้ ceremony โดยไม่กำหนด priority, feedback และ release authority.

## Opening Professional Question — ทำไมการวางแผนงานล่วงหน้า 1 ปีอย่างละเอียด ถึงกลับกลายเป็นจุดอ่อนร้ายแรงที่สุดในโลกธุรกิจยุคปัจจุบัน?

ลองพิจารณาคำถามท้าทายในยุคดิจิทัล:

> ในยุคที่พฤติกรรมผู้บริโภคเปลี่ยนแปลงทุกสัปดาห์ คู่แข่งออกฟีเจอร์ใหม่ทุกเดือน และเทคโนโลยีปัญญาประดิษฐ์ (AI) ก้าวกระโดดทุกวัน การยึดติดกับแผนงาน 500 หน้าที่วางไว้เมื่อ 2 ปีที่แล้ว โดยไม่ยอมปรับเปลี่ยนเลย ถือเป็น "วินัยทางการบริหาร" หรือเป็น "การเดินหน้าสู่ความล้มเหลว"?

ในโลกที่ซับซ้อนและเปลี่ยนแปลงรวดเร็ว (VUCA World) แผนงานแบบเดิมที่สมบูรณ์แบบบนกระดาษ อาจกลายเป็นสิ่งที่ไร้ประโยชน์ทันทีเมื่อเปิดตัว

> **คำถามสำคัญคือ:** Agile คืออะไร? มันเป็นเพียง "ความไม่มีระเบียบวินัยที่ไม่ยอมทำเอกสาร" หรือเป็น "ปรัชญาและกรอบการทำงานอย่างมีวินัยที่เน้นการเรียนรู้ ปรับตัว และส่งมอบความคุ้มค่าเร็วที่สุด"?

---

## Why This Matters — การทำ "Agile in Name Only" (Fake Agile)

ความล้มเหลวหลักในการนำ Agile มาใช้ในองค์กร ได้แก่:

1. **ทำตามพิธีกรรมแต่ไม่เปลี่ยน Mindset (Agile Theater):**
   * มีการยืนประชุมสั้น (Daily Standup) ทุกเช้า มีตาราง Scrum Board แต่กระบวนการคิด การอนุมัติ และสัญญายังคงเป็น Waterfall 100%
2. **เข้าใจผิดว่า Agile คือการไม่ต้องทำเอกสารและไม่ต้องวางแผน:**
   * ละเลยการทำ Product Backlog Refinement ขาดข้อตกลงเกณฑ์งานเสร็จ (Definition of Done) จนเกิด Technical Debt มหาศาล
3. **การพยายามนำ Scrum หรือ Kanban ไปบังคับใช้กับงานที่ไม่เหมาะสม:**
   * นำ Scrum ไปใช้กับงานก่อสร้างอาคาร หรือนำ Kanban ไปใช้กับงานที่ต้องการกำหนดการส่งมอบแบบล็อควันคงที่แน่นอน

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบาย Agile mindset และ 4 Agile values โดยไม่ตีความว่า “ไม่มีแผน”
2. แยก Scrum roles, artifacts, events และ Definition of Done
3. อธิบาย Kanban board, WIP limit และ flow management
4. เลือก Scrum, Kanban หรือ hybrid practice ตาม uncertainty และ work type
5. ใช้ ERP และ Hotel Booking scenarios เพื่อแยก agile product work, support flow และ hybrid governance

## 3. เหตุผลและที่มา: จาก Agile Manifesto สู่การส่งมอบความคุ้มค่าอย่างต่อเนื่อง

เหตุใด **Agile Project Management** จึงกลายเป็นมาตรฐานสำคัญของวิชาชีพ PM?

เพราะในการพัฒนาผลิตภัณฑ์ดิจิทัลและนวัตกรรมใหม่ **"สมมติฐานในวันแรกมักจะผิด"** วิธีเดียวที่จะรู้ความจริงคือการส่งมอบผลงานชิ้นเล็ก ๆ ออกไปทดสอบกับตลาดจริงให้เร็วที่สุด (Build-Measure-Learn Loop)

> **Core Rationale:**  
> **Agile ไม่ใช่เครื่องมือหรือเทคนิคเฉพาะ แต่คือ Mindset ที่ขับเคลื่อนด้วย 4 ค่านิยมหลัก (4 Values) และ 12 หลักการ (12 Principles) ที่เน้นการตอบสนองต่อการเปลี่ยนแปลง มากกว่าการทำตามแผนที่วางไว้**

---

## 4. Mental Model: 4 Values of Agile Manifesto & Scrum Cycle

เพื่อสร้างกรอบความคิดที่ถูกต้อง ให้ยึด **4 ค่านิยมหลักของ Agile Manifesto** (อ้างอิงจาก Canonical Source):

```text
1. คนและการมีปฏิสัมพันธ์                 เหนือกว่า   กระบวนการและเครื่องมือ
   (Individuals and Interactions        over       Processes and Tools)

2. ซอฟต์แวร์ที่นำไปใช้งานได้จริง          เหนือกว่า   เอกสารที่ครบถ้วนสมบูรณ์
   (Working Software                    over       Comprehensive Documentation)

3. การร่วมมือทำงานกับลูกค้า              เหนือกว่า   การเจรจาต่อรองสัญญา
   (Customer Collaboration              over       Contract Negotiation)

4. การตอบสนองต่อการเปลี่ยนแปลง         เหนือกว่า   การปฏิบัติตามแผนผูกมัด
   (Responding to Change                over       Following a Plan)
```

*(หมายเหตุ: สิ่งทางขวายังคงมีคุณค่า แต่สิ่งทางซ้ายมีคุณค่ามากกว่า)*

---

## 5. คำศัพท์และ Framework (Scrum vs Kanban ตาม Canonical Source)

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

### 5.1 Scrum Framework (Iterative & Incremental Delivery)
Scrum บริหารงานเป็นรอบเวลาคงที่เรียกว่า **Sprint** (ปกติ 1-4 สัปดาห์) โดยประกอบด้วย:

- **3 Roles:** 
  * *Product Owner (PO):* เจ้าของผลิตภัณฑ์ จัดลำดับความสำคัญใน Backlog (Maximizing Value)
  * *Scrum Master (SM):* โค้ชผู้ดูแลกระบวนการ ขจัดอุปสรรคให้ทีม (Servant Leader)
  * *Developers / Team:* ทีมงานข้ามสายงานผู้ลงมือทำระบบ (Self-Organizing)
- **3 Artifacts:** *Product Backlog*, *Sprint Backlog*, *Increment* (ผลงานที่พร้อมใช้งานได้จริง)
- **5 Events:** *Sprint*, *Sprint Planning*, *Daily Scrum (15 นาที)*, *Sprint Review (Demo)*, *Sprint Retrospective (ปรับปรุงการทำงาน)*

### 5.2 Kanban Framework (Flow-based Delivery)
Kanban เน้นการเห็นภาพการไหลของงาน (Visualize Flow) และการจำกัดปริมาณงานที่ทำพร้อมกัน:
- **Visual Board:** แบ่งช่องสถานะงาน เช่น *To Do → In Progress → Testing → Done*
- **WIP Limits (Work in Progress Limits):** กำหนดจำนวนงานสูงสุดที่ยอมให้ทำพร้อมกันในแต่ละช่อง เพื่อลดการสลับงานไปมา (Context Switching) และกำจัดคอขวด (Bottlenecks)

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏨 Core Scenario B: Hotel Booking Digital Platform (Scrum & Kanban in Practice)

- **Scrum Flow in Mobile App Development:**
  * ทีมพัฒนาใช้ Scrum แบบ **Sprint ละ 2 สัปดาห์**
  * *Sprint 1:* ส่งมอบ Increment หน้าค้นหาโรงแรม (Search)
  * *Sprint 2:* ส่งมอบ Increment หน้าเลือกห้องพักและชำระเงิน (Booking & Payment)
  * ในทุกจบ Sprint ทีมจัด **Sprint Review** นำแอปจริงให้ Stakeholders ทดลองเล่น และทำ **Sprint Retrospective** เพื่อปรับปรุงกระบวนการทำงานใน Sprint ถัดไป
- **Kanban for Support & Maintenance:**
  * สำหรับทีมดูแลระบบและแก้ Incident ใช้ **Kanban Board** ที่มี WIP Limit ไม่เกิน 3 งานในช่อง *In Progress* เพื่อรับประกันว่าบั๊กวิกฤตจะได้รับการแก้ไขและส่งมอบอย่างรวดเร็วที่สุด

### 🏢 Core Scenario A: ERP Transformation (Agile/Hybrid Mindset)

- แม้โครงการ ERP จะใช้วิธีวางแผนหลักแบบ Waterfall แต่สามารถนำ **Daily Standup (15 นาที)** และ **Kanban Board** มาใช้ในการติดตามสถานะงาน Data Migration และการทำ SIT ร่วมกันระหว่าง Vendor กับทีมงานภายใน เพื่อเพิ่มความโปร่งใส

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"Agile หมายถึงไม่มีแผน และสามารถเปลี่ยนสเปคได้ทุกวันตามใจชอบ":**
   * *ความจริง:* ในระหว่างที่ดำเนินการใน Sprint (Sprint Execution) ขอบเขตใน Sprint Backlog จะถูกล็อคไว้ การเปลี่ยนความสำคัญจะทำได้ใน Sprint ถัดไปผ่านการจัดลำดับ Product Backlog โดย Product Owner
2. **"Agile ไม่ต้องการ Project Manager อีกต่อไป":**
   * *ความจริง:* แม้ใน Scrum จะไม่มีชื่อตำแหน่ง PM แต่ทักษะของ PM ด้าน Integration, Risk, Stakeholder, และ Governance ยังคงจำเป็นอย่างยิ่ง โดย PM อาจปรับบทบาทเป็น Product Owner, Scrum Master หรือ Delivery Manager
3. **"Scrum ดีกว่า Kanban เสมอ":**
   * *ความจริง:* Scrum เหมาะกับงานพัฒนาสิ่งใหม่ที่มีจังหวะแน่นอน ส่วน Kanban เหมาะกับงานที่มีคำขอเข้ามาต่อเนื่องและต้องการความยืดหยุ่นสูง ไม่มีตัวใดเหนือกว่า ขึ้นอยู่กับบริบทงาน

---

## 8. PM Thinking & Decision Making

เมื่อต้องพิจารณานำ Agile Framework มาใช้ ให้ PM ใช้ **Agile Readiness Decision Steps**:

```text
Step 1: Assess Uncertainty -> งานมีความไม่แน่นอนด้าน Requirement หรือเทคโนโลยีสูงหรือไม่?
        - ถ้าความไม่แน่นอนสูง -> เลือกใช้ Agile Framework (Scrum/Kanban)
        - ถ้าสเปคแน่นอน 100% ไม่เปลี่ยนเลย -> เลือกใช้ Predictive (Waterfall)

Step 2: Choose Framework ->
        - ต้องการส่งมอบเป็นรอบเวลาแน่นอน (Timeboxed Iterations) -> ใช้ Scrum
        - ต้องการบริหารการไหลของงานต่อเนื่องและลดคอขวด (Continuous Flow) -> ใช้ Kanban

Step 3: Establish Definition of Done (DoD) -> กำหนดเกณฑ์คุณภาพว่า "งานเสร็จสมบูรณ์" หมายถึงอะไร (ต้องผ่าน Test, Code Review, Security Check) เพื่อป้องกัน Tech Debt
```

---

## 9. Reflection & Assessment

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ทีมของคุณในปัจจุบันกำลังทำ **Agile จริง** (เปลี่ยน Mindset และส่งมอบ Value เร็วขึ้น) หรือทำเพียงแค่ **Agile Theater** (ยืนประชุมสั้นแต่กระบวนการคิดยังคงเดิม)?
2. คุณมีการจัดทำ **Sprint Retrospective** เพื่อให้ทีมงานทบทวนและปรับปรุงกระบวนการทำงานร่วมกันเป็นประจำแล้วหรือยัง?

---

### Context for later learning

ในบทสุดท้าย **Lesson 16** เราจะนำองค์ความรู้ทั้งหมดตั้งแต่ Predictive (Waterfall) จนถึง Agile มาประมวลรวมกัน เพื่อสร้าง **Framework ในการเลือกแนวทาง (Tailoring Framework)** ที่เหมาะสมที่สุดสำหรับโครงการของคุณครับ!

## PM Decision Thinking

**[PMBOK 6]** Predictive governance ยังมีประโยชน์เมื่อ scope ชัดและ compliance สูง. **[PMBOK 7]** adaptability และ tailoring ทำให้ Agile เหมาะกับงานที่ต้องเรียนรู้เร็วและส่ง value เป็นรอบ.

| Field | Lesson 15 Application |
|---|---|
| Decision | งานนี้ควรใช้ Scrum, Kanban, predictive governance หรือ hybrid practice |
| Owner | PO จัดลำดับ value; Scrum Master/Delivery lead ดู flow; PM ดู governance, risk และ stakeholder alignment |
| Inputs | requirement uncertainty, release cadence, team maturity, compliance, dependency, support demand, Definition of Done |
| Options | Scrum sprint, Kanban flow, hybrid milestone + agile team, predictive plan |
| Trade-offs | adaptability vs predictability, speed vs governance, WIP focus vs urgent requests |
| Risk | ทำพิธี Agile แต่ decision/contract/governance ยังไม่สนับสนุน learning |
| Evidence | working increment, sprint review feedback, cycle time, WIP, defect trend, backlog health |
| Next Action | เลือก framework พร้อม working agreement และ Definition of Done |

### PM Insight

Agile ไม่ใช่การไม่มีวินัย แต่เป็นวินัยแบบสั้น เร็ว และเรียนรู้จริง. ถ้าไม่มี backlog, owner, DoD, review, feedback และ adaptation สิ่งที่เกิดขึ้นอาจเป็นแค่ Agile theater.

## ERP Scenario

**[Teaching Scenario]** ERP Transformation โดยรวมอาจใช้ predictive/hybrid governance เพราะมี contract, modules, migration และ go-live deadline. แต่บาง workstreams ใช้ agile practices ได้:

- Kanban สำหรับ data cleansing issue flow และ SIT defects
- Daily standup ระหว่าง TechConsult และทีมคุณเอกเพื่อเห็น blockers
- Iterative prototype สำหรับ reporting dashboard
- Sprint-like cadence สำหรับ training material และ user feedback

ข้อควรระวังคืออย่าเรียกทั้ง ERP ว่า Agile เพียงเพราะใช้ board หรือ standup หาก scope/governance ยังเป็น baseline-driven.

## Hotel Booking Scenario

**[Teaching Scenario]** Hotel Booking Platform เหมาะกับ Scrum/Kanban มากกว่าเพราะต้องเรียนรู้จาก user behavior, conversion, payment failure และ partner feedback.

- Scrum เหมาะกับ new feature development เช่น search, booking, payment, back office
- Kanban เหมาะกับ production support, bugs, payment incidents และ partner inventory issues
- PO คุณนภาต้องจัดลำดับ backlog ตาม direct booking value
- Definition of Done ต้องรวม test, security, performance และ analytics readiness

## Real Enterprise Example

**[Enterprise Practice]** องค์กรที่ “ทำ Agile” แต่ยังอนุมัติ requirement ปีละครั้ง, วัดทีมจากเอกสาร, ไม่ให้ลูกค้าดู increment และไม่เปลี่ยน backlog ตาม feedback ไม่ได้ Agile จริง. Agile อยู่ที่ learning loop ไม่ใช่ชื่อ ceremony.

## Common Mistakes

1. ทำ daily standup แต่ไม่มี impediment removal
2. ไม่มี Product Owner ที่ตัดสิน priority ได้จริง
3. ปล่อยให้ WIP สูงจน Kanban board กลายเป็น parking lot
4. ไม่มี Definition of Done ทำให้งาน “done” แต่ยังทดสอบไม่ได้
5. ใช้ Scrum กับ support work ที่เข้ามาไม่เป็นรอบโดยไม่ปรับให้เหมาะ

## Common Misconceptions

| Misconception | Correction |
|---|---|
| Agile ไม่ต้องวางแผน | Agile วางแผนบ่อยและปรับจาก feedback |
| Agile ไม่ต้องเอกสาร | เอกสารยังมี แต่พอดีกับ value และ risk |
| Scrum ดีกว่า Kanban | เลือกตาม work type และ flow |
| Agile ไม่มี PM | PM skill ยังจำเป็น แต่อาจเปลี่ยนบทบาท |

## Interview Questions

### Definition

1. Scrum roles, artifacts และ events มีอะไรบ้าง
2. Kanban WIP limit มีไว้เพื่ออะไร

### Judgement

1. เมื่อใดควรใช้ Scrum และเมื่อใดควรใช้ Kanban
2. ถ้าองค์กรทำ Agile ceremony แต่ delivery ไม่ดี คุณจะ diagnose อย่างไร

### Behavioral

1. เล่าครั้งหนึ่งที่ทีมใช้ feedback ปรับ backlog
2. คุณเคยช่วยทีมลด WIP หรือ bottleneck อย่างไร

### Scenario

1. ใน ERP คุณจะใช้ agile practices ตรงไหนโดยไม่เสีย governance
2. ใน Hotel Booking คุณจะใช้ Scrum/Kanban แยก feature work กับ support อย่างไร

## PM Dictionary

| Term | Meaning |
|---|---|
| Agile | mindset และวิธีทำงานที่เน้น learning, adaptability และ working value |
| Scrum | framework แบบ sprint เพื่อส่ง increment เป็นรอบ |
| Sprint | รอบเวลาคงที่ 1-4 สัปดาห์ |
| Product Backlog | รายการงาน/product needs ที่จัดลำดับโดย PO |
| Sprint Backlog | งานที่ทีมเลือกทำใน sprint |
| Increment | ผลงานที่พร้อมใช้งานตาม Definition of Done |
| Definition of Done | เกณฑ์ว่างานเสร็จจริงอย่างมีคุณภาพ |
| Kanban | วิธีจัดการ flow ด้วย board และ WIP limit |
| WIP Limit | จำนวนงานสูงสุดที่ทำพร้อมกันเพื่อควบคุม flow |
| Retrospective | การทบทวนเพื่อปรับปรุงวิธีทำงาน |

## Workshop

### Scenario

ERP มี defect flow ระหว่าง SIT และ data migration. Hotel Booking ต้องพัฒนา booking features พร้อมจัดการ payment incidents หลัง beta.

### Task

ให้ผู้เรียนทำ framework choice brief 1 หน้า:

1. work type และ uncertainty
2. Scrum/Kanban/hybrid recommendation
3. roles และ decision rights
4. Definition of Done หรือ WIP limit
5. feedback loop
6. governance/risk control ที่ยังต้องมี

### Debrief

คำตอบที่ดีต้องเลือก framework ตามงาน ไม่ใช่ตามความนิยม.

## Assessment

ดูแบบประเมินหลักที่ [Lesson 15 Assessment](./Lesson-15_3-Assessment.md). แบบประเมินควรวัด judgement เรื่อง framework selection, Agile theater diagnosis และ DoD/WIP design.

## Executive Summary

Agile คือการส่งมอบ value เป็นรอบสั้น เรียนรู้จาก feedback และปรับตัวอย่างมีวินัย. Scrum เหมาะกับ product development ที่ต้องส่ง increment เป็น sprint ส่วน Kanban เหมาะกับ flow/support/incident work. PM มืออาชีพไม่ถามว่า Agile หรือไม่ Agile แต่ถามว่างานนี้ต้องใช้ cadence, governance และ feedback แบบใด.

## Lesson Connection

Lesson 14 ปิด Knowledge Areas ด้าน procurement. Lesson 15 เปิดมุม Agile สำหรับงานที่ไม่แน่นอนและต้องเรียนรู้เร็ว. Lesson 16 จะรวม predictive, agile, hybrid และ tailoring เพื่อเลือก approach ที่เหมาะกับบริบทจริง.

## AI Continuation Context

Future AI agents must avoid describing Agile as no planning or no documentation. Use ERP as hybrid/agile-practice example and Hotel Booking as stronger agile product scenario. Keep Scrum and Kanban differentiated by cadence and flow.

## Artifact Handoff

- **Output:** PO-owned backlog, Delivery Team-owned flow board and feedback evidence.
- **Authority:** PO prioritises; Release Authority decides launch.
- **Next use:** L16 tailors the delivery approach from this evidence.

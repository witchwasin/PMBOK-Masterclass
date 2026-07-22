---
lesson: 5
sequence: 5.2
title: Project Integration Management
document_type: Lesson
level: Core
status: Active
validation_status: Validated
version: 1.0
last_updated: 2026-07-22
prerequisite:
  - Lesson 04 — 10 Project Management Knowledge Areas Overview
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 05_2 — Project Integration Management

## Beginner Safety

- **ควรรู้แล้ว:** Value Chain, lifecycle gates และ Cross-impact Map จาก Lessons 02–04
- **ยังไม่ต้องรู้:** Stakeholder analysis รายละเอียดหรือ Risk/Issue operation
- **คำศัพท์ใหม่:** Project Charter, Governance, Decision Rights, Change Request, Impact Analysis, Baseline Update
- **Novice traps:** คิดว่า Charter คือ Project Plan หรือใช้ Change Record แทน Issue Log

## Opening Professional Question — เมื่อทุกฝ่ายต้องการสิ่งที่ไม่ตรงกัน ใครคือผู้เชื่อมประสาน?

ลองจินตนาการถึงประชุมติดตามความคืบหน้าของโครงการขนาดใหญ่ที่มีผู้มีส่วนได้ส่วนเสียจากหลายฝ่ายเข้าร่วม:

- **ฝ่ายธุรกิจ (Business):** *"ตลาดเปลี่ยนแล้ว เราต้องเพิ่มฟีเจอร์การอนุมัติหลายระดับและรายงานรูปแบบใหม่เข้าไปในระบบ ไม่อย่างนั้นเปิดตัวไปก็ไม่มีใครใช้"*
- **ทีมพัฒนาระบบ (Development / Vendor):** *"สเปคเดิมก็แน่นมากแล้ว ถ้าจะเพิ่มฟีเจอร์นี้ เราต้องการเวลาเพิ่มอย่างน้อย 2 เดือน และต้องคิดค่าใช้จ่ายเพิ่ม 1.5 ล้านบาท"*
- **ฝ่ายการเงิน (Finance):** *"งบประมาณปีนี้ถูกล็อคไว้หมดแล้ว ห้ามเพิ่มงบแม้แต่บาทเดียว และต้องปิดโครงการให้ทันไตรมาสนี้เพื่อรับรู้ผลตอบแทน"*
- **ฝ่ายปฏิบัติการ (Operations):** *"จะรีบ Go-live อย่างไรก็ได้ แต่ถ้าระบบยังย้ายข้อมูลเก่ามาไม่ครบ และพนักงานยังใช้ไม่เป็น พวกเราไม่ขอรับมอบระบบมาดูแลเด็ดขาด"*

ในสถานการณ์นี้ ทุกฝ่ายต่างมีเหตุผลที่ถูกต้องในมุมมองของตนเอง:
* Business พูดถูกเรื่องความต้องการทางธุรกิจ
* Dev พูดถูกเรื่องข้อจำกัดทางเทคนิคและเวลา
* Finance พูดถูกเรื่องวินัยทางการเงิน
* Operations พูดถูกเรื่องความพร้อมในการใช้งานจริง

> **คำถามสำคัญคือ:** เมื่อเป้าหมายของแต่ละฝ่ายขัดแย้งกัน ใครคือคนที่มองภาพรวม เชื่อมโยงข้อมูล วิเคราะห์ผลกระทบ และขับเคลื่อนให้เกิดการตัดสินใจเพื่อประโยชน์สูงสุดขององค์กร?

---

## Why This Matters — การบูรณาการแบบผิวเผินและการตกเป็นเหยื่อของความขัดแย้ง

เมื่อองค์กรหรือ PM ขาดความเข้าใจใน **Project Integration Management** มักเกิดปัญหาเชิงโครงสร้างดังนี้:

1. ** Integration เป็นเพียงกระดาษรวบรวมเอกสาร (Document Aggregation):**
   * มองการทำ Project Plan เป็นเพียงการเอาไฟล์จากแผนกต่าง ๆ มาเย็บเล่มรวมกัน โดยไม่ได้วิเคราะห์ว่าแผนเหล่านั้นขัดแย้งกันเองหรือไม่
2. **PM กลายเป็นเพียง "คนเดินข่าว" (Message Carrier):**
   * รวบรวม Status Report จากแต่ละทีมมาแปะรวมกันในสไลด์ โดยไม่ได้วิเคราะห์ความเสี่ยง หรือใช้ดุลยพินิจชั่งน้ำหนักข้อแลกเปลี่ยน (Trade-off)
3. **การหลอกตัวเองด้วยสถานการณ์แบบ "แตงโม" (Watermelon Project Status):**
   * รายงานสถานะภายนอกเป็นสีเขียว (Green Status) เพราะแต่ละแผนกติ๊กส่งงานตามลิสต์ แต่เมื่อลึกลงไปกลับมีความขัดแย้งเชิงโครงสร้างสะสมอยู่ภายใน จนระบบพังทลายในวันเปิดตัว

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบายบทบาท Integration Management ในฐานะระบบเชื่อม decision ทั้งโครงการ
2. ระบุ 7 core integration processes และหน้าที่ระดับภาพรวม
3. ใช้ integrated change control เพื่อวิเคราะห์ scope, schedule, cost, quality, risk, resource และ stakeholder impact
4. แยก project plan ที่รวมเอกสารออกจาก integrated project management plan ที่ใช้ตัดสินใจจริง
5. ใช้ ERP และ Hotel Booking scenarios เพื่อเสนอ trade-off ต่อ sponsor/CCB

## 3. เหตุผลและที่มา: บทบาท System Integrator ของ Project Manager

ทำไม **Project Integration Management** จึงถูกจัดเป็น Knowledge Area แรกของ PMBOK?

เพราะไม่มี Knowledge Area ใดสามารถทำงานโดดเดี่ยวได้ Scope, Schedule, Cost, Quality, Risk, Resource ล้วนส่งผลกระทบถึงกันและกันเสมอ

> **Core Rationale:**  
> **Integration Management คือหัวใจหลักของการเป็น Project Manager** PM ไม่ได้ถูกจ้างมาเพื่อทำสเปคเทคนิคหรือทำบัญชีแข่งกับผู้เชี่ยวชาญ แต่ถูกจ้างมาเพื่อเป็น **System Integrator** ที่ทำให้ทุกองค์ประกอบของโครงการเคลื่อนไปในทิศทางเดียวกันเพื่อส่งมอบ Business Value

---

## 4. Mental Model: Conductor และกระบวนการบูรณาการ 7 ขั้นตอน

เพื่อสร้างกรอบความคิดที่ถูกต้อง ให้เปรียบ PM เหมือน **ผู้อำนวยเพลง (Conductor) ของวงออเคสตรา**:
- นักดนตรีแต่ละคนคือผู้เชี่ยวชาญเฉพาะด้าน (Scope, Schedule, Cost, Quality, Risk)
- PM ไม่จำเป็นต้องเล่นเครื่องดนตรีทุกชิ้นได้เก่งที่สุด แต่ PM คือผู้ควบคุมจังหวะ ความดังเบา และทำให้ทุกคนเล่นประสานเป็นเพลงเดียวกัน

```text
  [ Scope Management ] ───────┐
  [ Schedule Management ] ────┼───► [ Project Integration Management ] ───► Business Value
  [ Cost Management ] ────────┤      (PM as System Integrator)
  [ Risk & Quality ] ─────────┘
```

### การไหลของ 7 Core Integration Processes:
```text
[ Initiating ]   ──►  1. Develop Project Charter
                            │
[ Planning ]     ──►  2. Develop Project Management Plan
                            │
[ Executing ]    ──►  3. Direct and Manage Project Work  |  4. Manage Project Knowledge
                            │
[ Monitoring ]   ──►  5. Monitor and Control Project Work | 6. Perform Integrated Change Control
                            │
[ Closing ]      ──►  7. Close Project or Phase
```

---

## 5. คำศัพท์และ Framework (7 Core Processes ตาม Canonical Source)

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

### 5.1 7 กระบวนการบูรณาการหลัก

1. **Develop Project Charter:** อนุมัติการจัดตั้งโครงการ กำหนดเป้าหมายระดับสูง และมอบอำนาจ (Authority) ให้ PM
2. **Develop Project Management Plan:** รวมแผนย่อยของทุก Knowledge Area และ Baseline เข้าด้วยกันเป็นแผนแม่บทเดียว
3. **Direct and Manage Project Work:** ขับเคลื่อนการลงมือทำจริง สร้าง Deliverables และดำเนินการตาม Change Requests ที่ได้รับอนุมัติ
4. **Manage Project Knowledge:** บรรลุการเรียนรู้ บริหาร **Explicit Knowledge** (เอกสาร/โค้ด) และ **Tacit Knowledge** (ประสบการณ์/ทักษะ) ป้องกันความรู้สูญหาย
5. **Monitor and Control Project Work:** ติดตาม วิเคราะห์ความเบี่ยงเบนเทียบกับ Baseline และคาดการณ์แนวโน้มอนาคต
6. **Perform Integrated Change Control (ICC):** ประเมินผลกระทบข้ามมิติ อนุมัติ/ปฏิเสธ/ชะลอ Change Requests โดย Change Control Board (CCB)
7. **Close Project or Phase:** สรุปกิจกรรมทั้งหมด ตรวจรับงาน ปิดสัญญา และย้ายระบบเข้าสู่การดูแลของ Operations (Transition to Operations)

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (Integrated Change Control)

- **สถานการณ์:** ก่อน Go-live 3 สัปดาห์ ฝ่ายการเงินขอเพิ่มระบบอนุมัติเอกสารแบบ Multi-level Approval Workflow
- **การวิเคราะห์ผลกระทบข้ามมิติ (Integrated Impact Analysis):**
  * *Scope:* เพิ่มกระบวนการพัฒนาโค้ดและปรับสิทธิ์ User
  * *Schedule:* ต้องเลื่อนวัน Go-live ออกไป 1 เดือนกระทบสัญญา Vendor
  * *Risk:* เลื่อน Go-live จะกระทบการปิดบัญชีประจำปีขององค์กร
- **ทางเลือกในการบริหาร Trade-off:**
  * *ทางเลือกที่ 1:* เลื่อน Go-live 1 เดือน เพิ่มงบ 800,000 บาท เพื่อทำฟีเจอร์นี้ให้เสร็จ
  * *ทางเลือกที่ 2 (แนะนำ):* เปิด Go-live ตามวันเดิม โดยใช้กระบวนการอนุมัติแบบ Manual นอกระบบชั่วคราว แล้วนำฟีเจอร์นี้ไปทำใน Phase 1.1 หลัง Go-live 1 เดือน
- **ผลลัพธ์:** PM นำเสนอข้อมูลผลกระทบและทางเลือกให้ CCB ตัดสินใจอย่างโปร่งใส

### 🏨 Core Scenario B: Hotel Booking Digital Platform (Speed vs Stability Trade-off)

- **สถานการณ์:** ฝ่ายการตลาดต้องการเพิ่ม Dynamic Promotion Engine เข้าไปใน Mobile App ก่อนวัน Launch 2 สัปดาห์
- **การวิเคราะห์ผลกระทบข้ามมิติ:**
  * *Speed-to-Market vs Quality:* หากเร่งใส่ฟีเจอร์โดยไม่ได้ทำ Load Test ร่วมกับ Payment Gateway อาจทำให้ระบบจองล่มในช่วงเปิดตัว
- **ทางเลือกในการบริหาร Trade-off:**
  * ปล่อยตัวแอปพลิเคชันเวอร์ชันแรกตามกำหนดเดิมด้วยระบบ Promotion พื้นฐาน แล้วใช้การยิงส่วนลดผ่าน Coupon Code ทาง Marketing แทนการเขียนโค้ดเพิ่ม จากนั้นนำฟีเจอร์นี้ใส่ไว้ใน Priority สัปดาห์ถัดไปใน Product Backlog

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"เอกสารครบ = บริหารโครงการดีแล้ว (Process Theater)":**
   * *ความจริง:* เอกสารเป็นเพียงสื่อกลาง การมีแผนเอกสารหนาแต่ไม่มีใครปฏิบัติตามจริง ไม่ได้ช่วยให้โครงการเกิด Value
2. **" Status Green ในรายงาน = โครงการปลอดภัย (Watermelon Status)":**
   * *ความจริง:* รายงานสถานะจำนวนมากเป็นสีเขียวลวงตา เพราะ PM ตรวจดูเฉพาะงานเสร็จตามรายการ แต่ไม่ได้วิเคราะห์ความเสี่ยงเชิงโครงสร้าง
3. **"การ Tailoring คือการเลือกตัดกระบวนการที่ไม่ยากทำออกตามใจชอบ":**
   * *ความจริง:* การ Tailor คือการปรับลดหรือเพิ่มระดับความเข้มงวดของกระบวนการให้ **เหมาะสมกับระดับความเสี่ยงและบริบทของโครงการ** อย่างมีเหตุผล
4. **"เมื่อส่งมอบระบบ (Output) เสร็จ ถือว่างานของ PM จบสิ้นแล้ว":**
   * *ความจริง:* งานของ PM จะจบลงก็ต่อเมื่อส่งมอบผลงานเข้าสู่งานประจำ (Transition to Operation) และเกิดการสร้าง Outcome/Value ได้จริง

---

## 8. PM Thinking & Integration Decision Framework

เมื่อต้องตัดสินใจในสถานการณ์ขัดแย้ง ให้ PM ใช้ **4-Step Integration Framework**:

```text
Step 1: Systemic Impact Assessment -> การเปลี่ยนแปลงนี้กระทบ Scope, Schedule, Cost, Quality, Risk อย่างไร?
Step 2: Business Value Alignment -> การเปลี่ยนแปลงนี้ยังคงตอบโจทย์ Business Case เดิมหรือไม่?
Step 3: Trade-off Options -> มีทางเลือกใดบ้าง? (ทำทันที / แบ่งเฟส / ปฏิเสธ) แต่ละทางเลือกมีข้อดีข้อเสียอย่างไร?
Step 4: Governance & Decision -> เสนอข้อมูลให้ CCB / Sponsor ตัดสินใจอย่างโปร่งใส และอัปเดต Baseline
```

---

## Guided Reflection During Learning

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการของคุณ กระบวนการ Change Control ดำเนินการอย่างเป็นระบบผ่านการวิเคราะห์ผลกระทบข้ามมิติ หรือเกิดขึ้นจากการสั่งงานปากเปล่าของแต่ละฝ่าย?
2. คุณมีการวางแผนบริหารความรู้ (Manage Project Knowledge) เพื่อป้องกันปัญหาคนสำคัญลาออกแล้วความรู้ในโครงการหายไปหรือไม่?

---

## PM Decision Thinking

**[PMBOK 6]** Integration Management รวม charter, project management plan, execution, knowledge, monitoring, integrated change control และ closing. **[PMBOK 7]** PM ต้องเชื่อม decision กับ value และ stewardship.

| Field | Lesson 05 Application |
|---|---|
| Decision | change request ควร approve, reject, defer, split phase หรือ escalate |
| Owner | PM ทำ impact analysis; CCB/sponsor ตัดสินตาม governance |
| Inputs | charter, baselines, work performance reports, change request, risk, quality, contract, stakeholder impact |
| Options | keep baseline, rebaseline, manual workaround, phased release, add budget/resource, defer scope |
| Trade-offs | business value vs delivery risk, speed vs stability, local request vs enterprise outcome |
| Risk | PM กลายเป็นคนส่งข่าวโดยไม่ integrate impact |
| Evidence | integrated impact log, decision record, updated plan, approved change |
| Next Action | เสนอ option brief และบันทึก decision พร้อม owner |

### PM Insight

Integration คือการทำให้ “ทุกคนถูกในมุมตัวเอง” กลายเป็น “องค์กรตัดสินใจถูกในภาพรวม”. PM ไม่ต้องเป็นผู้เชี่ยวชาญทุกเรื่อง แต่ต้องทำให้ผลกระทบของทุกเรื่องถูกเห็นก่อนตัดสินใจ.

## ERP Scenario

**[Scenario]** ERP Transformation ของคุณสมชายมี working delivery budget 45 ล้านบาท, 5 modules, TechConsult เป็น SI, 80 key users และ go-live target ก่อน 1 ตุลาคม.

ก่อน go-live 3 สัปดาห์ finance ขอเพิ่ม multi-level approval. PM ต้องทำ integrated change control:

- Scope: ฟีเจอร์ใหม่อยู่ใน original scope หรือไม่
- Schedule: หาก build/test เพิ่มกระทบ 1 ตุลาคมอย่างไร
- Cost/Procurement: กระทบสัญญา TechConsult และ working budget 45 ล้านบาทหรือไม่
- Quality/Risk: หาก workaround manual จะเสี่ยง audit หรือ adoption อย่างไร
- Stakeholder: finance ได้ value แต่ operations และ testers มี capacity จำกัด
- Decision: เสนอ CCB ว่า approve now, defer to phase 1.1 หรือ manual workaround พร้อม control

## Hotel Booking Scenario

**[Scenario]** Hotel Booking Platform ต้องรักษา launch 8 เดือนและเป้าหมาย direct booking 35% หลัง 18 เดือน.

Marketing ต้องการ dynamic promotion engine ก่อน launch. PM ต้อง integrate:

- Business value: feature ช่วย conversion จริงหรือเป็น nice-to-have
- Quality: load test กับ payment gateway พร้อมหรือไม่
- Schedule: launch delay กระทบ high season
- Cost/resource: team ต้องหยุดแก้ payment failure หรือไม่
- Stakeholder: marketing ต้องการ campaign แต่ operations ต้องการ stability
- Decision: launch core booking พร้อม coupon workaround แล้วใส่ dynamic promotion ใน backlog หลัง stabilization

## Real Enterprise Example

**[Instructor Interpretation]** องค์กรที่มี project status เขียวแต่ go-live พังมักไม่ได้ขาด report แต่ขาด integration. แต่ละทีมบอกว่างานตนเองเสร็จ แต่ไม่มีใครรวมว่า data, training, vendor readiness, support model และ benefit owner พร้อมจริงหรือไม่.

## Common Mistakes

1. รวมเอกสารย่อยแล้วเรียกว่า integrated plan
2. อนุมัติ change จากผู้บริหารปากเปล่าโดยไม่ดู impact
3. ติดตามงานเสร็จตาม task แต่ไม่ดู readiness ทั้งระบบ
4. ปิด project โดยไม่ส่ง knowledge และ operation ownership
5. ใช้ tailoring เป็นข้ออ้างตัด governance ที่จำเป็น

## Common Misconceptions

| Misconception | Correction |
|---|---|
| Integration คือทำเอกสารรวม | Integration คือทำให้ decision และ baseline เชื่อมกัน |
| PM ต้องตัดสินใจทุก change เอง | PM เสนอ evidence; authority ตัดสินตาม governance |
| Change control ทำให้ช้าเสมอ | Change control ลด rework และทำให้ trade-off โปร่งใส |
| Close project คือส่ง deliverable | Closing รวม acceptance, contract, knowledge และ transition |

## Interview Questions

### Definition

1. Integration Management คืออะไร
2. Integrated Change Control ต่างจากการรับ requirement เพิ่มทั่วไปอย่างไร

### Judgement

1. ถ้า sponsor ขอเพิ่ม scope แต่ budget ไม่เพิ่ม คุณจะทำ impact analysis อย่างไร
2. ถ้า project status green แต่ adoption readiness ไม่พร้อม คุณจะรายงานอย่างไร

### Behavioral

1. เล่าครั้งหนึ่งที่คุณต้องรวมข้อมูลจากหลายทีมเพื่อให้ผู้บริหารตัดสินใจ
2. คุณเคยปฏิเสธหรือ defer change อย่างไรโดยรักษาความสัมพันธ์กับ stakeholder

### Scenario

1. ใน ERP หาก TechConsult ขอเลื่อน data migration คุณจะใช้ ICC อย่างไร
2. ใน Hotel Booking หาก marketing ขอ feature เพิ่มก่อน launch คุณจะเสนอ options อย่างไร

## PM Dictionary

| Term | Meaning |
|---|---|
| Project Charter | เอกสารอนุมัติโครงการและมอบอำนาจ PM |
| Project Management Plan | แผนแม่บทที่รวม baselines และแผนย่อยเพื่อใช้บริหารจริง |
| Direct and Manage Project Work | การขับเคลื่อนงานตามแผนและ approved changes |
| Manage Project Knowledge | การจัดการความรู้ explicit และ tacit ของโครงการ |
| Monitor and Control Project Work | การวิเคราะห์ performance เทียบ baseline และ forecast |
| Integrated Change Control | การประเมินและตัดสิน change request แบบข้ามมิติ |
| Close Project or Phase | การปิด project/phase อย่างเป็นทางการ รวม handover และ lessons learned |

## Workshop

### Scenario

ERP finance ขอเพิ่ม approval workflow ก่อน go-live 3 สัปดาห์. Hotel Booking marketing ขอ dynamic promotion engine ก่อน launch 2 สัปดาห์.

### Task

ให้ผู้เรียนทำ integrated change option brief 1 หน้า โดยระบุ:

1. change request และ business rationale
2. affected baselines และ Knowledge Areas
3. options อย่างน้อย 3 ทาง
4. trade-off, risk และ recommendation
5. decision owner และสิ่งที่ต้อง update หลัง decision

### Debrief

คำตอบที่ดีต้องไม่ใช่แค่ “ทำ/ไม่ทำ” แต่แสดงว่าทางเลือกใดรักษา value และควบคุม risk ได้ดีที่สุด.

### Artifact Learning Path

- **Do:** สร้าง [Integration Artifact Pack](learner/Artifact-Template.md) และทำ [Workshop](learner/Workshop.md)
- **Checkpoint:** ทำ [Beginner Checkpoint](learner/Beginner-Checkpoint.md)
- **Review หลังส่งคำตอบ:** ใช้ [Thinking Walkthrough](instructor/Thinking-Walkthrough.md), [Completed Example](instructor/Completed-Example.md), [Checklist](instructor/Review-Checklist.md) และ [Rubric](instructor/Scoring-Rubric.md)

## Assessment

ดูแบบประเมินหลักที่ [Lesson 05 Assessment](./Lesson-05_3-Assessment.md). แบบประเมินควรวัด judgement เรื่อง integrated change control, cross-impact analysis และ closing/transition มากกว่าการจำชื่อ 7 processes.

## Executive Summary

Project Integration Management คือหัวใจของ PM เพราะทำให้ charter, plan, execution, change, knowledge, control และ closing เดินเป็นระบบเดียวกัน. PM มืออาชีพไม่ใช่คนเดินข่าว แต่เป็นคนทำให้ผลกระทบและ trade-off เห็นชัดพอที่องค์กรจะตัดสินใจได้.

## Lesson Connection

Lesson 04 ให้แผนที่ 10 Knowledge Areas. Lesson 05 เจาะแกนกลางที่เชื่อมทุกด้านเข้าด้วยกัน. Lesson 06 จะต่อไปที่ Stakeholder Management เพราะ decision ที่ integrate ดีจะใช้ไม่ได้ถ้าคนสำคัญไม่เข้าใจ ไม่ยอมรับ หรือไม่ร่วมมือ.

## AI Continuation Context

Future AI agents must treat Integration Management as decision integration, not document aggregation. Preserve ERP budget terminology: Working Budget 45 ล้านบาท and Total Funding Envelope 60 ล้านบาท. Keep Hotel Booking examples tied to launch readiness and direct booking outcome.

## Artifact Handoff

- **Inputs:** Value Chain, Lifecycle Map และ Cross-impact Map
- **Outputs:** Project Charter, Governance and Decision Rights Map, Change Decision Record
- **Governance:** Creator/Owner/Reviewer/Approval Authority แยกตาม Artifact Contract ใน Blueprint
- **Minimum acceptance:** `Usable`
- **Next use:** Lesson 06 ใช้ Charter/Governance เพื่อระบุ Stakeholder, influence และ approval expectations

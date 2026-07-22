---
lesson: 2
sequence: 2.2
title: Project Management Overview
document_type: Lesson
level: Foundation
status: Active
validation_status: Validated
last_reviewed: 2026-07-22
estimated_study_time: 75
related_lessons:
  - Lesson 01 — ทำไม Project Manager ต้องรู้ PMBOK
  - Lesson 03 — 5 Project Management Process Groups
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 01 — ทำไม Project Manager ต้องรู้ PMBOK
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 02_2 — Project Management Overview

## Beginner Safety

- **ควรรู้แล้ว:** PMBOK เป็น framework และ Output ไม่ได้เท่ากับ Value
- **ยังไม่ต้องรู้:** 5 Process Groups, WBS, schedule network หรือ EVM
- **คำศัพท์ใหม่:** Project, Operation, Transition, Output, Outcome, Benefit, Organizational Structure
- **Novice traps:** ใช้ deadline/ขนาดงานตัดสินว่าเป็น Project และเรียก Go-live ว่า Outcome

## Learning Objectives

เมื่อจบบท ผู้เรียนสามารถ (1) จำแนกงานเป็น project, operation หรือ transitional work, (2) สร้าง Value Chain ที่มี measure และ Owner, (3) ระบุ transition responsibility, และ (4) เสนอ governance ให้เหมาะกับ organizational context. `[PMBOK]` `[Best Practice]`

## Opening Professional Question — งานทุกอย่างที่มีวันเริ่มต้นและวันสิ้นสุด เป็น Project ทั้งหมดหรือไม่?

ลองพิจารณาภารกิจต่าง ๆ ภายในองค์กรต่อไปนี้:
- การปิดบัญชีและสรุปงบการเงินประจำเดือน
- การออกรายงานยอดขายรายวันของระบบโรงแรม
- การพัฒนาและเปิดตัว Mobile Application จองห้องพักใหม่
- การเปลี่ยนระบบบริหารจัดการองค์กร (ERP) ทั้งหมด
- การจัดงานสัมมนาประจำปีของบริษัท
- การดูแลแก้ไข Incident ของลูกค้าในแต่ละวัน

เมื่อพิจารณาดู จะพบว่าทุกงานมี "จุดเริ่มต้นและวันสิ้นสุดของรอบงาน" ทั้งสิ้น แต่คำถามสำคัญเชิงการบริหารคือ:

> **งานทุกงานที่มีวันเริ่มและวันจบ ถือเป็น "โครงการ" (Project) ที่ต้องใช้วิธีการบริหารโครงการทั้งหมดหรือไม่?**

ถ้าคำตอบคือไม่ใช่ อะไรคือเส้นแบ่งที่แท้จริงระหว่าง **Project** กับ **Routine Work (Operation)**?

---

## Why This Matters — การบริหารแบบผสมผสานจนเกิดความล้มเหลว

องค์กรจำนวนมากประสบปัญหาโครงการล้มเหลว หรือบริหารงานประจำได้ไม่มีประสิทธิภาพ เพราะ **นำเครื่องมือและการบริหารผิดประเภทไปใช้กับธรรมชาติของงานที่ผิดประเภท**:

1. **นำการบริหารแบบ Operation ไปใช้กับ Project:**
   * พยายามบังคับให้งานที่มีความไม่แน่นอนสูง (เช่น การพัฒนา Digital Product ใหม่) ต้องมีขั้นตอนปฏิบัติคงที่ตายตัวเหมือนงานประจำ ทำให้ขาดความยืดหยุ่นและการนวัตกรรม
2. **นำการบริหารแบบ Project ไปใช้กับ Operation:**
   * ตั้งโครงการและจัดประชุมติดตามสำหรับงานประจำที่เกิดขึ้นซ้ำ ๆ ทุกวัน ทำให้เกิดความสิ้นเปลืองทรัพยากรและเอกสารซ้ำซ้อนโดยไม่จำเป็น
3. **ส่งมอบระบบเสร็จแต่ไม่เกิด Value:**
   * มุ่งเน้นเพียงการส่งมอบผลงาน (Output) ให้เสร็จตามกำหนด แต่ไม่ได้เชื่อมโยงกับวัตถุประสงค์ทางธุรกิจ (Business Value) และไม่ได้เตรียมความพร้อมให้ฝ่ายปฏิบัติการรับช่วงต่อ

---

## 3. เหตุผลและที่มา: ธรรมชาติของความเฉพาะตัวและความชั่วคราว

เหตุใดวิชาชีพ Project Management จึงต้องนิยามคำว่า "Project" ให้ชัดเจน?

เพราะการดำเนินงานขององค์กรประกอบด้วย 2 ขับเคลื่อนหลัก:
- **Operations (งานประจำ):** ทำหน้าที่รักษาและดำเนินธุรกิจในปัจจุบันให้มั่นคง มีประสิทธิภาพ และคาดการณ์ได้ (Keep the Business Running)
- **Projects (โครงการ):** ทำหน้าที่เปลี่ยนแปลง ปรับปรุง หรือสร้างสิ่งใหม่เพื่ออนาคตขององค์กร (Change/Transform the Business)

การเข้าใจที่มานี้ช่วยให้ PM มองเห็นว่า โครงการไม่ได้เกิดขึ้นโดดเดี่ยว แต่ถูกตั้งขึ้นเพื่อตอบสนองต่อ **Business Need** และเปลี่ยนผ่านไปสู่ **Business Value**

---

## 4. Mental Model: กรอบความคิด Value Chain ของการบริหารโครงการ

เพื่อไม่ให้ PM มองโครงการเป็นเพียง "งานที่ต้องทำให้เสร็จ" ให้ใช้ Mental Model สายธารแห่งคุณค่า (Value Chain):

```text
Business Need (ปัญหา/โอกาสทางธุรกิจ)
    ↓
Business Case (เหตุผลเชิงธุรกิจและการลงทุน)
    ↓
Project (การตั้งโครงการและการกำหนดเป้าหมาย)
    ↓
Work (การลงมือปฏิบัติงานและบริหารจัดการ)
    ↓
Output (ผลผลิตหรือสิ่งส่งมอบที่ได้จากโครงการ)
    ↓
Outcome (ผลลัพธ์การเปลี่ยนแปลงจากการนำ Output ไปใช้)
    ↓
Benefit (ประโยชน์ที่องค์กรได้รับจริง)
    ↓
Business Value (คุณค่าทางธุรกิจระยะยาว)
    ↓
Transition to Operation (การส่งมอบเข้าสู่งานประจำ)
```

### การแยกแยะ Output, Outcome, Benefit และ Business Value:
- **Output (ผลผลิต):** ระบบ ERP ใหม่, Mobile App จองโรงแรม (สิ่งที่สร้างเสร็จ)
- **Outcome (ผลลัพธ์):** พนักงานใช้งานระบบ ERP ในการบันทึกข้อมูล, ลูกค้าจองห้องพักผ่าน Mobile App (การเปลี่ยนแปลงพฤติกรรม/กระบวนการ)
- **Benefit (ประโยชน์):** ลดเวลาปิดบัญชีจาก 15 วันเหลือ 5 วัน, เพิ่ม Direct Booking จาก 10% เป็น 35% ภายใน 18 เดือน และลด OTA commission ตามเป้าหมายธุรกิจ (ผลลัพธ์เชิงตัวเลข)
- **Business Value (คุณค่า):** องค์กรมีขีดความสามารถในการแข่งขันสูงขึ้น และมีกำไรสุทธิเพิ่มขึ้นอย่างยั่งยืน

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

### 5.1 คุณสมบัติหลักของ Project (Project Characteristics)
1. **Temporary (ชั่วคราว):** มีจุดเริ่มต้นและจุดสิ้นสุดที่ชัดเจน เมื่อบรรลุวัตถุประสงค์แล้วโครงการจะจบลง
2. **Unique (เอกลักษณ์):** สร้างผลิตภัณฑ์ บริการ ผลลัพธ์ หรือการเปลี่ยนแปลงที่มีความเฉพาะตัว ไม่เคยทำซ้ำในบริบทเดิมเป๊ะ ๆ

### 5.2 ตารางเปรียบเทียบ Project vs Routine Work (Operation)

| ลักษณะ (Dimension) | โครงการ (Project) | งานประจำ (Routine Work / Operation) |
|---|---|---|
| **วัตถุประสงค์** | สร้างสรรค์สิ่งใหม่หรือการเปลี่ยนแปลง (Unique Output) | รักษามาตรฐานและดำเนินงานต่อเนื่อง (Repetitive Result) |
| **ระยะเวลา** | ชั่วคราว มีจุดเริ่มต้นและสิ้นสุดชัดเจน | ดำเนินการต่อเนื่องไม่มีจุดจบกำหนดไว้ |
| **โครงสร้างทีม** | บุคลากรข้ามสายงาน (Multi-disciplinary) | ทำงานตามโครงสร้างแผนกประจำ (Functional Unit) |
| **ความไม่แน่นอน** | สูง มีความเสี่ยงและสมมติฐานที่ต้องพิสูจน์ | ต่ำ กระบวนการชัดเจนและคาดการณ์ผลลัพธ์ได้ |
| **ตัวชี้วัดความสำเร็จ** | บรรลุตาม Objective, Scope, Quality, Benefit | บรรลุตาม SLA, Efficiency, Throughput, Quality Standard |

### 5.3 โครงสร้างองค์กรและอำนาจของ PM (Organizational Structures)
- **Functional Organization:** อำนาจสูงสุดอยู่ที่ Functional Manager, PM เป็นเพียงผู้ประสานงาน (Coordinator)
- **Matrix Organization (Weak / Balanced / Strong):** แบ่งปันอำนาจระหว่าง PM และ Functional Manager
- **Projectized Organization:** PM มีอำนาจสูงสุดในการบริหารทรัพยากรและงบประมาณโครงการ

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation

- **การแยกแยะ Project vs Operation ในบริบท ERP:**
  * **Operation:** การคีย์ใบสั่งซื้อประจำวัน, การปิดบัญชีสิ้นเดือน, การดูแลเซิร์ฟเวอร์ระบบเดิม
  * **Project:** การวางระบบ ERP ใหม่, การ Migrate ข้อมูลจากระบบเดิม, การฝึกอบรมพนักงานทั้งองค์กร
- **Value Chain Analysis:**
  * *Output:* ระบบ ERP โมดูล Finance & Account ที่ติดตั้งเสร็จสมบูรณ์
  * *Outcome:* พนักงานฝ่ายการเงินบันทึกข้อมูลเข้าสู่ระบบใหม่แทนการใช้ Excel
  * *Benefit:* ลดเวลาปิดงบจาก 15 วันเหลือ 5 วัน; การลด error จากการ key ข้อมูลซ้ำ 70% เป็นคนละ KPI ตาม Scenario Master
  * *Transition:* ส่งมอบระบบให้ฝ่าย IT Support ดูแลต่อ และให้ฝ่ายการเงินนำไปใช้ในงานประจำวัน

### 🏨 Core Scenario B: Hotel Booking Digital Platform

- **การแยกแยะ Project vs Operation ในบริบท Digital Product:**
  * **Project Phase:** การออกแบบ UX/UI, การพัฒนา Mobile App (iOS/Android), การเชื่อมต่อ Payment Gateway
  * **Operation Phase:** การดูแล Transaction จองห้องพักประจำวัน, การแก้ไข Incident หน้าจอแอปพลิเคชัน, การอัปเดตราคาห้องพัก
- **Value Chain Analysis:**
  * *Output:* Mobile Application สำหรับจองห้องพักบน App Store และ Play Store
  * *Outcome:* นักท่องเที่ยวค้นหาและกดจองห้องพักสำเร็จด้วยตนเองผ่านมือถือ
  * *Benefit:* ยอดจองตรง (Direct Booking) เพิ่มจาก 10% เป็น 35% ภายใน 18 เดือน
  * *Transition:* ทีมพัฒนาส่งมอบแผนงานดูแลแอปและเวอร์ชันอัปเดตย่อยให้แก่ทีม Product Operations

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"งานที่มี Deadline ทุกงานคือ Project":**
   * *ความจริง:* งานประจำหลายอย่างก็มี Deadline (เช่น ต้องส่งรายงานภาษีทุกวันที่ 15) แต่ไม่ใช่ Project เพราะไม่ได้สร้างสิ่งใหม่หรือมีความเฉพาะตัว
2. **"Go-live หรือส่งมอบ Output ได้ แปลว่าโครงการประสบความสำเร็จแล้ว":**
   * *ความจริง:* หากส่งมอบระบบได้ทันเวลา แต่ไม่มีใครนำไปใช้งาน (เกิด zero adoption) จนไม่เกิด Outcome ทางธุรกิจ ถือว่าโครงการล้มเหลวในมิติของ Value
3. **"Project Manager คือคนตามงานและทำ Gantt Chart เท่านั้น":**
   * *ความจริง:* PM คือผู้บริหารการตัดสินใจ (Decision Integrator), ผู้บริหารความคาดหวัง และผู้รักษาสมดุลระหว่างข้อจำกัดเพื่อให้เกิด Business Value
4. **"Projectized Organization ดีกว่า Functional Organization เสมอ":**
   * *ความจริง:* ไม่มีโครงสร้างใดดีที่สุด ทุกโครงสร้างมี Trade-off องค์กรต้องเลือกให้เหมาะกับประเภทของธุรกิจและระดับความซับซ้อน

---

## 8. PM Thinking & Decision Making

เมื่อ PM ต้องเผชิญกับสถานการณ์จริง ให้ใช้ **3-Question Decision Filter**:

```text
คำถามที่ 1: งานนี้คือ Project หรือ Operation?
   ├── ถ้าเป็น Operation -> ใช้การบริหารแบบ SLA / Standard Operating Procedure (SOP)
   └── ถ้าเป็น Project -> ไปคำถามที่ 2

คำถามที่ 2: อะไรคือ Output และอะไรคือ Outcome ที่ถูกคาดหวัง?
   ├── ตรวจสอบว่า Output ที่กำลังสร้าง จะนำไปสู่การเปลี่ยนแปลงพฤติกรรม (Outcome) อย่างไร
   └── กำหนดแผนการย้ายระบบและการบริหารการเปลี่ยนแปลง (Change Management & Transition)

คำถามที่ 3: โครงสร้างองค์กรปัจจุบันสนับสนุนอำนาจตัดสินใจของ PM แค่ไหน?
   ├── ถ้าเป็น Functional -> PM ต้องเน้นทักษะการเจรจาต่อรอง (Influence without Authority)
   └── ถ้าเป็น Projectized / Strong Matrix -> PM ใช้อำนาจตามที่ได้รับมอบหมายใน Project Charter
```

---

## Guided Reflection During Learning

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการปัจจุบันที่คุณกำลังทำอยู่ สิ่งที่คุณเรียกว่า "สำเร็จ" เป็นเพียงการส่งมอบ **Output** หรือเป็นส่งมอบ **Outcome & Business Value**?
2. คุณมีการวางแผน **Transition to Operation** เพื่อส่งต่อผลงานให้ฝ่ายปฏิบัติการนำไปใช้ประโยชน์ในงานประจำไว้ชัดเจนแล้วหรือยัง?

---

## PM Decision Thinking

**Decision:** จะจัด “ลดเวลาปิดงบ” เป็น operational improvement, ERP project หรือ portfolio ที่มีทั้งสองส่วน.
**Owner:** Sponsor และ business owner; PM เสนอ analysis.
**Inputs:** uniqueness, duration, cross-functional dependency, baseline 15 วัน, cost of delay, capacity key users.
**Assumptions:** root cause ไม่ใช่เพียงรายงานช้า; ERP scope 5 modules ยังคงตาม Scenario Master.
**Options:** แก้รายงานเฉพาะหน้า, เริ่ม ERP เต็ม scope, หรือทำ improvement คู่กับ ERP.
**Trade-offs:** แก้เฉพาะหน้ารวดเร็วแต่ไม่แก้ data/process fragmentation; ERP สร้าง capability แต่ใช้เวลาและ change effort.
**Risk:** ตัดสินจาก deadline โดยไม่ตั้ง outcome owner.
**Evidence:** business case, outcome KPI, resource commitment, transition plan.
**Next Action:** บันทึก classification และ review benefit หลัง go-live. `[Teaching Scenario]` `[Professional Opinion]`

## PM Insight

คำถาม “นี่เป็น project หรือ operation?” ไม่ใช่ exercise ด้านคำศัพท์ แต่กำหนดว่าใครมี authority, funding, governance และ success measure. งานเดียวอาจมี project part ที่สร้าง capability และ operation part ที่รักษาคุณค่าหลัง handover. `[Professional Opinion]`

## ERP Scenario

ERP Scenario Master v1.0 มีเป้าหมายลดเวลาปิดงบ 15 วันเหลือ 5 วัน, รวม 6 legacy systems, และให้ผู้ใช้ทำงานบนระบบเดียวกัน. การปิดบัญชีประจำเดือนคือ operation; การออกแบบ/migrate/train/cutover คือ project. “ระบบ Finance deployed” เป็น output, แต่การปิดงบใน 5 วันและการใช้ข้อมูลเดียวกันเป็น outcome/benefit ที่ต้องมี Finance และ IT operations เป็น owner หลัง transition. `[Teaching Scenario]`

## Hotel Booking Scenario

Hotel Booking MVP เป็น project ที่สร้าง website, mobile app, payment/PMS integrations และ launch capability; การรับ booking, incident support และ rate updates หลัง launch เป็น operation. ผลลัพธ์ที่ต้องพิสูจน์ไม่ใช่เพียง app อยู่ใน store แต่คือ direct booking เพิ่มจาก 10% เป็น 35% ภายใน 18 เดือนและลด OTA commission ตาม Scenario Master. `[Teaching Scenario]`

## Real Enterprise Example

องค์กรอาจส่งมอบ mobile app ตรงกำหนด แต่ถ้าฝ่าย operations ไม่มี support model, marketing ไม่มี acquisition plan, หรือ payment dispute ไม่มี owner ผู้ใช้จะไม่เห็น service ที่เชื่อถือได้. นี่เป็น enterprise pattern เพื่อให้เห็น transition responsibility—not a factual claim about a named company. `[Enterprise Practice]`

## Common Mistakes

- ใช้ deadline เป็นเกณฑ์เดียวในการเรียกงานว่า project
- ตั้ง success KPI เป็น “deploy complete” เท่านั้น
- ส่งมอบให้ operation โดยไม่มี owner, training หรือ acceptance ของกระบวนการ
- คิดว่า PM ต้องมีอำนาจสายบังคับบัญชาจึงจะบริหาร matrix ได้

`[Best Practice]`

## Common Misconceptions

- “ทุกงานที่มีวันจบคือ project” — งานประจำอาจมี cycle/deadline ได้. `[PMBOK]`
- “go-live คือ outcome” — go-live เป็น event/output; outcome ต้องเป็นการเปลี่ยนแปลงที่สังเกตได้. `[PMBOK]`
- “PM คือเจ้าของ benefit คนเดียว” — sponsor/business/operations ต้องถือ ownership ตาม governance. `[Professional Opinion]`

## Interview Questions

### Foundational

**Project ต่างจาก operation อย่างไร?** แนวคำตอบ: project มีความชั่วคราวและสร้างผลลัพธ์เฉพาะ; operation รักษางานต่อเนื่อง. **Warning sign:** ใช้ขนาดหรือ deadline เป็นเกณฑ์เดียว.

### Scenario

**ERP go-live แล้วปิดงบยัง 15 วัน คุณตรวจอะไร?** แนวคำตอบ: adoption, process/data quality, support และ benefit owner. **Warning sign:** ปิดเรื่องเพราะ deployment สำเร็จ.

### Senior PM

**ใน weak matrix คุณได้ resource commitment อย่างไร?** แนวคำตอบ: ทำ evidence-based request, negotiate priorities, establish escalation and RACI. **Warning sign:** บอกว่า PM สั่งทุกทีมได้.

### Executive

**คุณจะรายงาน business value โดยไม่ overclaim อย่างไร?** แนวคำตอบ: แยก output/outcome/benefit, show baseline/owner/review date. **Warning sign:** ใช้ vanity metric.

`[Professional Opinion]`

## PM Dictionary

| Term | Thai explanation | Practical meaning | Common misuse |
|---|---|---|---|
| Project | ความพยายามชั่วคราวเพื่อสร้างผลเฉพาะ | vehicle for change | เรียกทุกงาน deadline ว่า project |
| Operation | งานดำเนินการต่อเนื่อง | sustains service/value | มองว่าไม่เกี่ยวกับ project |
| Output | สิ่งส่งมอบ | system/app/process delivered | เรียกว่า benefit |
| Outcome | การเปลี่ยนแปลงจากการใช้ output | adoption/behaviour/performance | สับสนกับ go-live |
| Transition to Operation | การส่งผ่านความรับผิดชอบ | operating model/owner/support ready | handover เอกสารอย่างเดียว |

`[PMBOK]` — synchronized with `PM_GLOSSARY.md`.

## Workshop

**Scenario:** CFO ต้องการลดเวลาปิดงบภายในไตรมาสหน้า แต่ CEO สนับสนุน ERP ระยะ 12 เดือน.
**Role:** ผู้เรียนเป็น PM analyst ของคุณเอก.
**Available information:** baseline 15 วัน, ERP 5 modules, Working Budget 45 ล้านบาท, 80 key users ทำงานคู่ขนาน.
**Missing information:** root cause of close delay, benefits owner, capacity/backfill, cost of delay.
**Decision:** เสนอ operational improvement, ERP, หรือ portfolio พร้อม rationale.
**Constraints:** ต้องแยก Working Budget 45 จาก Total Funding Envelope 60 ล้านบาท; ห้ามรับประกัน outcome โดยไม่มี adoption evidence.
**Expected output:** one-page option brief, outcome measure, owner, next action.
**Debrief:** การแก้เฉพาะหน้าทำลายหรือสนับสนุน ERP business case อย่างไร?
**Evaluation:** classification/evidence 30%, trade-offs 30%, ownership 20%, clarity 20%. `[Teaching Scenario]`

### Artifact Learning Path

- **Do:** กรอก [Project vs Operation Analysis and Value Chain](learner/Artifact-Template.md)
- **Checkpoint:** ทำ [Beginner Checkpoint](learner/Beginner-Checkpoint.md)
- **Review หลังส่งคำตอบ:** ใช้ [Thinking Walkthrough](instructor/Thinking-Walkthrough.md), [Completed Example](instructor/Completed-Example.md), [Review Checklist](instructor/Review-Checklist.md) และ [Rubric](instructor/Scoring-Rubric.md)

## Assessment

ทำ [Lesson 02 Assessment](Lesson-02_3-Assessment.md). ผู้เรียนต้องผ่าน decision case, artifact review, trade-off และ executive communication; recall questionsต้องไม่เกินครึ่งของคะแนน. `[Teaching Scenario]`

## Executive Summary

| Question | Executive answer |
|---|---|
| Why | เลือก governance และ funding ให้ตรงธรรมชาติของงาน |
| Decision improved | แยก quick operational fix ออกจาก change initiative ที่ต้องมี sponsor |
| Failure prevented | ส่ง system แล้วไร้ adoption/benefit owner |
| Monitor | baseline, adoption, close-cycle days, transition readiness |

`[Professional Opinion]`

## Lesson Connection

Lesson 02 แยก project, operation และ value chain แล้ว; Lesson 03 จะสอน Process Groups เป็นกิจกรรมที่วนซ้ำและทำงานคู่ขนาน ไม่ใช่ phase ที่แข็งตัว. `[PMBOK 6]`

## AI Continuation Context

- **Terms locked:** project, operation, output, outcome, benefit, business value, transition to operation.
- **Scenario state:** ERP and Hotel Scenario Master v1.0 only; no post-launch event added.
- **Decision introduced:** classification/governance decision needs owner, outcome measure, evidence and transition responsibility.
- **Prohibited contradictions:** do not call all deadline-driven work a project; do not equate go-live with value.
- **Next handoff:** Lesson 03 uses the value chain to explain iterative Process Groups.

## Artifact Handoff

- **Input:** PM Learning Baseline และ Scenario Masters
- **Output:** Project vs Operation Analysis and Value Chain
- **Governance:** PM Analyst สร้าง; Sponsor/Business Owner เป็น Owner; Functional Owner/PM ตรวจ; Sponsor อนุมัติ
- **Minimum acceptance:** `Usable`
- **Next use:** Lesson 03 ใช้ project boundary, expected value และ transition point สร้าง Lifecycle and Process Group Map

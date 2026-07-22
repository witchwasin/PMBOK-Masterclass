---
lesson: 6
sequence: 6.2
title: Project Stakeholder Management
document_type: Lesson
difficulty: Core
estimated_study_time: 105
status: Active
validation_status: Validated
version: 1.0
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 05 — Project Integration Management
related_lessons:
  - Lesson 05 — Project Integration Management
  - Lesson 07 — Project Scope Management and WBS
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 06_2 — Project Stakeholder Management

## Beginner Safety

- **ควรรู้แล้ว:** Charter, Governance และ decision rights จาก Lesson 05
- **ยังไม่ต้องรู้:** Resource assignment หรือ Communication Plan รายละเอียด
- **คำศัพท์ใหม่:** Stakeholder, Influence, Current/Desired Engagement, Resistance, Champion
- **Novice traps:** มอง Stakeholder เป็นเพียงรายชื่อหรือคิดว่าทุก resistance แก้ด้วย communication

## Opening Professional Question — ถ้าส่งมอบระบบได้ตามสเปค แต่ผู้บริหารฝ่ายปฏิบัติการไม่ยอมให้พนักงานเข้าใช้อุปกรณ์ โครงการนี้ถือว่าสำเร็จหรือไม่?

ลองพิจารณาเหตุการณ์จริงที่มักเกิดขึ้นในหลายองค์กร:

> ทีมพัฒนาซอฟต์แวร์สามารถส่งมอบระบบบริหารคลังสินค้าใหม่ได้ตรงเวลา 100% แต่เมื่อถึงวัน Go-live ผู้จัดการฝ่ายคลังสินค้ากลับปฏิเสธไม่ให้พนักงานสแกนบาร์โค้ดผ่านระบบใหม่ โดยอ้างว่า "กระบวนการใหม่ทำให้งานช้าลง และไม่มีใครเคยเข้ามาถามความต้องการของคนหน้างานตั้งแต่แรก"

ในมิติเชิงเทคนิค ระบบทำงานได้ถูกต้องตามข้อกำหนด  
แต่ในมิติเชิงผู้คน โครงการนี้กำลังเผชิญหน้ากับ **"แรงต้านของผู้มีส่วนได้ส่วนเสีย" (Stakeholder Resistance)** ที่สามารถทำให้โครงการล้มเหลวลงทันที!

> **คำถามสำคัญคือ:** ผู้มีส่วนได้ส่วนเสีย (Stakeholders) คือใครบ้าง? และเหตุใดการบริหารคนกลุ่มนี้จึงไม่ใช่เรื่องของการ "เอาใจทุกคน" แต่เป็นการบริหารความคาดหวังและการมีส่วนร่วมอย่างมีกลยุทธ์?

---

## Why This Matters — การบริหารคนแบบตั้งรับและการมองคนเพียงกลุ่มเดียว

ความผิดพลาดร้ายแรงเกี่ยวกับการบริหาร Stakeholder ในวิชาชีพ Project Management ได้แก่:

1. **มองว่า Stakeholder คือผู้บริหารระดับสูง (Sponsor) เท่านั้น:**
   * ละเลยกลุ่มผู้ใช้งานจริง (End Users), ฝ่ายปฏิบัติตามกฎระเบียบ (Compliance/Regulator), หรือคู่สัญญาภายนอก (Vendors) จนเกิดปัญหาในภายหลัง
2. **การบริหารแบบตั้งรับ (Reactive Management):**
   * รอให้เกิดความขัดแย้งหรือการต่อต้านก่อน แล้วค่อยเข้าไปแก้ไข แทนที่จะระบุและดึงเข้ามามีส่วนร่วมตั้งแต่ช่วงเริ่มต้น (Initiating Group)
3. **การพยายามทำให้ทุกคนพอใจ 100% (People-Pleasing Trait):**
   * ไม่เข้าใจว่า Stakeholders แต่ละกลุ่มมีเป้าหมายและอำนาจที่ขัดแย้งกัน การบริหารที่ถูกต้องคือการจัดระดับความสำคัญและการสื่อสารอย่างเหมาะสม

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. ระบุ stakeholder ได้เกินกว่ากลุ่ม sponsor และผู้บริหาร
2. ใช้ Power-Interest Grid เพื่อเลือก engagement strategy
3. แยก stakeholder position ออกจาก underlying need
4. ออกแบบ engagement plan ที่สอดคล้องกับอำนาจ ความสนใจ และผลกระทบ
5. ใช้ ERP และ Hotel Booking scenarios เพื่อประเมิน stakeholder risk และ adoption readiness

## 3. เหตุผลและที่มา: ผู้คนคือปัจจัยหลักที่กำหนดความล้มเหลวหรือสำเร็จ

เหตุใด **Project Stakeholder Management** จึงเป็นองค์ความรู้ที่สำคัญอย่างยิ่ง?

เพราะโครงการไม่ได้ดำเนินอยู่ในสุญญากาศ แต่ดำเนินอยู่ท่ามกลางมนุษย์ที่มีความคาดหวัง ผลประโยชน์ ความกลัว และอำนาจที่ต่างกัน

> **Core Rationale:**  
> **"โครงการเปลี่ยนกระบวนการ แต่ผู้คนเปลี่ยนผลลัพธ์"**  
> ไม่ว่าระบบหรือแผนงานจะสมบูรณ์แบบเพียงใด หากผู้มีส่วนได้ส่วนเสียไม่ยอมรับ ไม่ส่งมอบข้อมูล หรือปฏิเสธการนำไปใช้ โครงการก็ไม่สามารถสร้าง Business Value ได้จริง

---

## 4. Mental Model: ผัง Power-Interest Grid และกลยุทธ์การบริหาร 4 ทิศทาง

เพื่อสร้างกรอบความคิดที่คมชัด ให้ใช้ **Power-Interest Grid Matrix** ในการวิเคราะห์และจัดกลยุทธ์รับมือ Stakeholders:

```text
               High Power
                   │
                   │   [ Keep Satisfied ]    │   [ Manage Closely ]
                   │   (เอาใจใส่และดูแล)       │   (บริหารจัดการอย่างใกล้ชิด)
                   │                         │
  Power (อำนาจ)     │   - ผู้บริหารระดับสูงที่ไม่  │   - Project Sponsorหลัก
                   │     ได้คุมโครงการโดยตรง   │   - Head of Operations เจ้าของงาน
                   │                         │
   Low Power ──────┼─────────────────────────┼───────────────────────── High Power
                   │                         │
                   │   [ Monitor ]           │   [ Keep Informed ]
                   │   (เฝ้าติดตาม)            │   (แจ้งข่าวสารอย่างสม่ำเสมอ)
                   │                         │
                   │   - กลุ่มผู้ใช้ภายนอกทั่วไป  │   - End Users คนคีย์ข้อมูลหน้างาน
                   │   - สื่อมวลชน/สาธารณชน    │   - ทีมงาน Support เทคนิค
                   │                         │
                   └─────────────────────────┴─────────────────────────
                                          Interest (ความสนใจ)
```

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

### 5.1 หมวดหมู่ของผู้มีส่วนได้ส่วนเสีย (Stakeholder Categories)
1. **Internal Stakeholders:** Project Sponsor, คณะกรรมการบริหารโครงการ (Steering Committee), คณะทำงานอำนวยการ, คณะทำงานโครงการ, PM
2. **External Stakeholders & Users:** คณะกรรมการตรวจรับพัสดุ, หน่วยงานผู้ใช้ระบบ, บริษัทคู่สัญญา/Vendor, กลุ่มผู้ใช้งานภายใน/ภายนอกองค์กร, ลูกค้า (Customer)
3. **Compliance / Regulator:** หน่วยงานกำกับดูแลตามกฎหมาย, ฝ่ายตรวจสอบภายใน (Audit), ฝ่ายกฎหมาย
4. **Business & System Owners:** เจ้าของระบบธุรกิจ (Business Owner), เจ้าของระบบ IT เดิม (System Owner)

### 5.2 4 Sub-processes ของ Stakeholder Management
1. **Identify Stakeholders:** ระบุรายชื่อผู้เกี่ยวข้องทั้งหมดทั้งภายในและภายนอก (ได้ *Stakeholder Register*)
2. **Plan Stakeholder Engagement:** วางแผนกลยุทธ์การดึงผู้มีส่วนได้ส่วนเสียเข้ามามีส่วนร่วมตามระดับอำนาจและความสนใจ
3. **Manage Stakeholder Engagement:** สื่อสาร ปรับความคาดหวัง และแก้ไขข้อขัดแย้งระหว่างดำเนินโครงการ
4. **Monitor Stakeholder Engagement:** ติดตามความสัมพันธ์และปรับกลยุทธ์เมื่อระดับอำนาจหรือความสนใจของผู้เกี่ยวข้องเปลี่ยนไป

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (บริหารแรงต้านการเปลี่ยนแปลง)

- **วิเคราะห์ Stakeholder:**
  * *CFO & Sponsor (High Power, High Interest):* ต้องการรายงานการเงินที่เร็วขึ้น -> **Manage Closely** (ต้องรายงานความก้าวหน้าและขออนุมัติในจุดสำคัญ)
  * *ฝ่ายบัญชีหน้างาน (Low Power, High Interest):* กังวลว่า ERP ใหม่จะทำให้คีย์งานยากขึ้น -> **Keep Informed & Engage** (ดึงมาร่วมทำ UAT และจัดอบรมอย่างเข้มข้น)
  * *ฝ่าย IT ระบบเดิม (High Power, Low Interest):* กังวลเรื่องการโดนลดบทบาท -> **Keep Satisfied** (ดึงมาเป็นคณะทำงานเปลี่ยนผ่านข้อมูล เพื่อสร้าง Ownership)

### 🏨 Core Scenario B: Hotel Booking Digital Platform (บริหารความคาดหวังคู่ค้า)

- **วิเคราะห์ Stakeholder:**
  * *โรงแรมคู่ค้า / Partner Hotels (High Power, High Interest):* กังวลเรื่องค่าคอมมิชชันและระบบตัดสต็อกห้องพัก -> **Manage Closely** (ต้องจัดประชุมร่วม และมีระบบ Back Office ที่ใช้งานง่าย)
  * *นักท่องเที่ยว / App Users (Low Power, High Interest):* ต้องการจองห้องพักชำระเงินได้รวดเร็ว -> **Keep Informed** (ทดสอบ UX/UI และแจ้งสื่อสารโปรโมชัน)

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **" Stakeholders หมายถึงเฉพาะเจ้านายหรือ Sponsor เท่านั้น":**
   * *ความจริง:* Stakeholder คือทุกคนที่ได้รับผลกระทบทั้งเชิงบวกและเชิงลบ รวมไปถึงผู้ใช้หน้างานและ Vendor
2. **"การบริหาร Stakeholders คือการปฏิบัติต่อทุกคนเท่ากันหมด":**
   * *ความจริง:* ทรัพยากรและเวลามีจำกัด PM ต้องใช้ Power-Interest Grid จัดสรรระดับการดูแลให้เหมาะสม
3. **"เมื่อทำ Stakeholder Register วันแรกเสร็จแล้ว ถือว่างานจบ":**
   * *ความจริง:* อำนาจและความสนใจของคนเปลี่ยนได้ตลอดเวลา (เช่น คนเคย Low Power อาจได้เลื่อนตำแหน่งเป็น High Power) PM ต้องทำ Monitor Engagement อย่างต่อเนื่อง

---

## 8. PM Thinking & Decision Making

เมื่อเกิดความขัดแย้งระหว่าง Stakeholders ให้ PM ใช้ **Stakeholder Alignment Steps**:

```text
Step 1: Map Positions -> ใครต้องการอะไร และทำไมเขาจึงต้องการเช่นนั้น? (Identify Underlying Need)
Step 2: Check Power/Interest -> เขามีผลกระทบต่อความสำเร็จของโครงการระดับใด? (Power Grid)
Step 3: Find Common Ground -> วัตถุประสงค์ใดใน Business Case ที่ทุกฝ่ายเห็นตรงกัน?
Step 4: Execute Engagement Plan -> สื่อสารผ่านช่องทางและรูปแบบที่เหมาะกับ Stakeholder กลุ่มนั้น
```

---

## Guided Reflection During Learning

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการปัจจุบัน คุณได้จัดทำ **Stakeholder Register** และวิเคราะห์ Power-Interest Grid ไว้แล้วหรือยัง?
2. มี Stakeholder กลุ่มใดหรือไม่ที่คุณมองข้ามไปในวันแรก แล้วส่งผลกลับมารบกวนโครงการในวันนี้?

---

## PM Decision Thinking

**[PMBOK 6]** Stakeholder Management ประกอบด้วย identify, plan, manage และ monitor engagement. **[PMBOK 7]** stakeholder engagement เป็นเงื่อนไขสำคัญของ value delivery เพราะ outcome เกิดจากคนใช้และคนรับผลกระทบ.

| Field | Lesson 06 Application |
|---|---|
| Decision | stakeholder กลุ่มใดต้อง manage closely, keep satisfied, keep informed หรือ monitor |
| Owner | PM รับผิดชอบ stakeholder analysis; sponsor ช่วยเปิดทางเมื่อมี power conflict |
| Inputs | stakeholder register, power-interest grid, engagement level, resistance signals, business impact |
| Options | engage early, escalate sponsor, adjust communication, create champion network, defer decision |
| Trade-offs | speed vs buy-in, transparency vs political sensitivity, standard message vs tailored engagement |
| Risk | มองข้าม end users, regulators, vendors หรือ operations จน adoption ล้ม |
| Evidence | attendance, sign-off quality, UAT participation, issue sentiment, training adoption, decision latency |
| Next Action | update engagement plan และ owner ของแต่ละ stakeholder risk |

### PM Insight

Stakeholder management ไม่ใช่การเอาใจทุกคน แต่คือการทำให้คนที่กระทบ value ได้รับการ engage ในระดับที่เหมาะสม. PM ต้องฟังความกลัวและแรงจูงใจใต้คำคัดค้าน ไม่ใช่ดูแค่ตำแหน่งใน organization chart.

## ERP Scenario

**[Teaching Scenario]** ERP Transformation มี sponsor คุณสมชาย, PM คุณเอก, TechConsult, 80 key users และ 5 modules ที่แตะหลายฝ่าย.

Stakeholder risk ที่ต้องจัดการ:

- CFO/Finance: ต้องการ close เร็วและ reporting ถูกต้อง ต้อง manage closely
- Warehouse/Production: อาจกลัว process ใหม่ทำให้งานช้า ต้อง engage ผ่าน UAT และ process walkthrough
- HR: ต้องการ data privacy และ payroll accuracy ต้องมี acceptance criteria ชัด
- IT legacy owners: อาจกังวลบทบาทหลัง ERP ต้อง keep satisfied และให้บทบาท transition
- TechConsult: vendor ที่มี schedule pressure ต้อง manage ผ่าน contract, decision log และ escalation cadence

## Hotel Booking Scenario

**[Teaching Scenario]** Hotel Booking Platform มี sponsor คุณจิรา, PO คุณนภา, PM คุณสุทธิ, hotel partners, customers, operations และ marketing.

Stakeholder risk ที่ต้องจัดการ:

- Hotel partners: inventory accuracy และ commission concern ต้อง manage closely
- Customers: conversion และ payment trust ต้องวัดผ่าน beta feedback
- Operations/support: back office readiness ต้อง engage ก่อน launch
- Marketing: ต้องการ launch campaign แต่ต้องเข้าใจ quality risk
- Finance: ต้องเห็นว่า direct booking outcome ต้องใช้ adoption period ไม่ใช่แค่ go-live

## Real Enterprise Example

**[Professional Opinion]** โครงการที่ “ส่งตามสเปคแต่ไม่มีคนใช้” มักไม่ได้ล้มในวัน go-live แต่ล้มตั้งแต่ตอน stakeholder ที่มีผลต่อ operation ไม่ถูก engage. ผู้ใช้หน้างานไม่ถูกถาม, manager ไม่ได้เห็น benefit, support ไม่ได้เตรียม owner และ sponsor ได้ยินแต่รายงาน delivery.

## Common Mistakes

1. ทำ stakeholder register ครั้งเดียวแล้วไม่ update
2. คิดว่า sponsor คนเดียวแทนเสียงผู้ใช้ทั้งหมดได้
3. ส่ง communication เดียวกันให้ทุกกลุ่ม
4. มอง resistance เป็นนิสัยคน ไม่ใช่ข้อมูลเรื่อง risk/value
5. วัด engagement จากจำนวน meeting ไม่ใช่คุณภาพการตัดสินใจและ adoption evidence

## Common Misconceptions

| Misconception | Correction |
|---|---|
| Stakeholder คือ sponsor | Stakeholder คือทุกคนที่ส่งผลหรือได้รับผลจากโครงการ |
| Engagement คือทำให้ทุกคน happy | Engagement คือจัดการ expectation, influence และ participation |
| User involvement คือเชิญเข้าประชุม | ต้องมี input, validation, ownership และ readiness evidence |
| Resistance เป็นเรื่องลบเสมอ | Resistance อาจเป็นสัญญาณ requirement, risk หรือ change impact |

## Interview Questions

### Definition

1. Stakeholder คือใคร และทำไมไม่ใช่แค่ sponsor
2. Power-Interest Grid ใช้ตัดสิน engagement strategy อย่างไร

### Judgement

1. ถ้า end users ไม่ร่วม UAT แต่ sponsor บอกให้ go-live คุณจะทำอย่างไร
2. ถ้า stakeholder high power แต่ low interest เริ่มขัดขวาง project คุณจะปรับ plan อย่างไร

### Behavioral

1. เล่าครั้งหนึ่งที่คุณจัดการ stakeholder resistance ได้
2. คุณเคยเปลี่ยนวิธีสื่อสารให้เหมาะกับ stakeholder ต่างกลุ่มอย่างไร

### Scenario

1. ใน ERP ถ้า warehouse manager ไม่ยอมปล่อย key users มาทดสอบ คุณจะ engage อย่างไร
2. ใน Hotel Booking ถ้า hotel partners ไม่ update inventory คุณจะจัด stakeholder strategy อย่างไร

## PM Dictionary

| Term | Meaning |
|---|---|
| Stakeholder | บุคคลหรือกลุ่มที่ส่งผลหรือได้รับผลจากโครงการ |
| Stakeholder Register | รายชื่อ ข้อมูล ความคาดหวัง อำนาจ และ strategy ของ stakeholder |
| Power-Interest Grid | เครื่องมือจัดกลุ่ม stakeholder ตามอำนาจและความสนใจ |
| Engagement Plan | แผนการสื่อสาร มีส่วนร่วม และจัดการความคาดหวัง |
| Resistance | สัญญาณคัดค้านหรือไม่ร่วมมือที่ต้องวิเคราะห์สาเหตุ |
| Champion | ผู้สนับสนุนในหน่วยงานที่ช่วยผลักดัน adoption |
| Adoption Readiness | ความพร้อมของคน กระบวนการ และ support ที่จะใช้ผลส่งมอบจริง |

## Workshop

### Scenario

ERP key users ไม่เข้าร่วม UAT เพราะ functional managers กังวลงานประจำ. Hotel partners ไม่ update inventory เพราะ back office ใหม่ดูยุ่งยากและกลัว overbooking.

### Task

ให้ผู้เรียนสร้าง stakeholder action plan 1 หน้า:

1. stakeholder map อย่างน้อย 6 กลุ่ม
2. power/interest classification
3. current vs desired engagement
4. key concern และ underlying need
5. engagement action, owner, cadence และ success signal
6. risk หากไม่ engage

### Debrief

คำตอบที่ดีต้องไม่บอกแค่ “สื่อสารเพิ่ม” แต่ต้องบอกว่าใครต้องรู้อะไร ทำอะไร ตัดสินใจอะไร และ evidence ใดแปลว่า engagement ดีขึ้น.

### Artifact Learning Path

- **Do:** สร้าง [Stakeholder Register and Engagement Strategy](learner/Artifact-Template.md)
- **Checkpoint:** ทำ [Beginner Checkpoint](learner/Beginner-Checkpoint.md)
- **Review หลังส่ง:** ใช้ [Thinking Walkthrough](instructor/Thinking-Walkthrough.md), [Completed Example](instructor/Completed-Example.md), [Checklist](instructor/Review-Checklist.md) และ [Rubric](instructor/Scoring-Rubric.md)

## Assessment

ดูแบบประเมินหลักที่ [Lesson 06 Assessment](./Lesson-06_3-Assessment.md). แบบประเมินควรให้คะแนน judgement จาก stakeholder mapping, resistance diagnosis และ engagement strategy มากกว่าการจำชื่อ grid.

## Executive Summary

Stakeholder Management คือการทำให้คนที่มีผลต่อ value ถูกมองเห็น ถูกเข้าใจ และถูก engage ด้วยวิธีที่เหมาะสม. PM ต้องไม่รอให้เกิดแรงต้านแล้วค่อยแก้ แต่ต้อง monitor engagement เหมือน monitor schedule และ risk.

## Lesson Connection

Lesson 05 สอนให้ integrate decision. Lesson 06 สอนว่าคนคือเงื่อนไขที่ทำให้ decision ใช้ได้จริง. Lesson 07 จะเปลี่ยนความคาดหวังของ stakeholder ให้เป็น scope และ WBS ที่ชัดเจน ตรวจรับได้ และควบคุมได้.

## AI Continuation Context

Future AI agents must keep stakeholder thinking tied to adoption and value, not just communication artifacts. Use ERP key-user participation and Hotel partner inventory behavior as recurring signals of stakeholder engagement quality.

## Artifact Handoff

- **Input:** Project Charter and Governance Map
- **Output:** Stakeholder Register and Engagement Strategy
- **Governance:** PM/BA สร้าง; PM เป็น Owner; Sponsor/Business Change Leads ตรวจ; Sponsor อนุมัติ
- **Minimum acceptance:** `Usable`
- **Next use:** Lesson 07 ใช้ stakeholder needs, decision rights และ acceptance roles เพื่อสร้าง Requirements/Scope

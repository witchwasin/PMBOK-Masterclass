---
lesson: 7
sequence: 7.2
title: Project Scope Management and WBS
document_type: Lesson
level: Core
status: Draft
validation_status: Pending Final Repository Validation
version: 1.0
last_updated: 2026-07-22
prerequisite:
  - Lesson 06 — Project Stakeholder Management
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 07_2 — Project Scope Management and WBS

## Opening Professional Question — ถ้าลูกค้าขอเพิ่มฟีเจอร์เล็กๆ อีก 5 อย่างโดยไม่ขอเพิ่มงบประมาณและเวลา โครงการของคุณจะลงเอยอย่างไร?

ลองพิจารณาเหตุการณ์คลาสสิกที่เกิดขึ้นในแทบทุกโครงการ:

> ระหว่างประชุมติดตามงานสัปดาห์ละครั้ง ผู้บริหารพูดขึ้นว่า *"ไหนๆ ก็พัฒนาระบบใหม่แล้ว ช่วยเพิ่มปุ่มส่งออกรายงาน PDF แบบพิเศษ และระบบแจ้งเตือนผ่าน SMS ให้หน่อยสิ น่าจะใช้เวลาทำแป๊บเดียวเองนะ"*

หาก PM ตอบตกลงด้วยความเกรงใจทีละเล็กทีละน้อย ผ่านไป 3 เดือน โครงการจะพบว่ามีฟีเจอร์เพิ่มขึ้นมาจากข้อตกลงเดิมมากกว่า 30 อย่าง เวลาล่าช้าไป 4 เดือน และงบประมาณบานปลาย!

ปรากฏการณ์นี้ในวิชาชีพบริหารโครงการเรียกว่า **"Scope Creep" (ขอบเขตงานรั่วไหล)**

> **คำถามสำคัญคือ:** เราจะควบคุมขอบเขตงานอย่างไร ให้ทำเฉพาะสิ่งที่จำเป็นต้องทำ (100% Rule) โดยไม่ขาดและไม่เกิน?

---

## Why This Matters — การไม่แยกแยะความต้องการ และขาดโครงสร้างแตกงาน (WBS)

ปัญหาหลักที่ทำให้โครงการเสียการควบคุมด้าน Scope ได้แก่:

1. **การสับสนระหว่าง Product Scope กับ Project Scope:**
   * **Product Scope:** คุณสมบัติและฟังก์ชันของสิ่งที่จะสร้าง (ระบบทำงานอะไรได้บ้าง)
   * **Project Scope:** งานทั้งหมดที่ต้องทำเพื่อส่งมอบสิ่งนั้น (รวมถึงการอบรม การทดสอบ การย้ายข้อมูล และการบริหารจัดการ)
2. **ขอบเขตงานเป็นข้อความกว้างๆ ไม่ถูกย่อยเป็นโครงสร้างงาน (WBS):**
   * เขียนขอบเขตว่า "วางระบบ ERP" โดยไม่เคยนำมาแตกย่อยเป็น Work Packages ชัดเจน ทำให้เกิดงานหล่นหายหรือความเข้าใจไม่ตรงกัน
3. **การยอมรับคำขอโดยไม่ผ่านกระบวนการตรวจรับขอบเขต (Validate Scope):**
   * ไม่มีเกณฑ์การตรวจรับ (Acceptance Criteria) ที่ตกลงกันล่วงหน้า ทำให้เกิดการโต้แย้งในวันส่งมอบงาน

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. แยก product scope ออกจาก project scope
2. อธิบาย scope baseline, WBS และ WBS dictionary
3. ใช้ 100% Rule เพื่อตรวจว่างานครบ ไม่หล่น และไม่เกิน
4. ตัดสินใจเมื่อมี scope change โดยใช้ baseline, impact analysis และ change control
5. ใช้ ERP และ Hotel Booking scenarios เพื่อแยก in scope, out of scope และ phase/release trade-off

## 3. เหตุผลและที่มา: Scope คือฐานรากของ Triple Constraints

เหตุใด **Project Scope Management** จึงเป็นจุดเริ่มต้นของแผนการบริหารทั้งหมด?

เพราะคุณไม่สามารถประมาณการเวลา (**Schedule**) หรือคำนวณงบประมาณ (**Cost**) ได้เลย ตราบใดที่คุณยังไม่รู้ว่า "งานทั้งหมดที่ต้องทำจริง ๆ มีอะไรบ้าง"

> **Core Rationale:**  
> **Scope Management ไม่ใช่การพยายามปฏิเสธงานทุกอย่าง แต่คือการประกันว่าโครงการทำเฉพาะงานที่จำเป็นต้องทำ (Do all the work required, and ONLY the work required)**

---

## 4. Mental Model: กฎ 100% และ Work Breakdown Structure (WBS)

เพื่อสร้างกรอบความคิดที่ถูกต้อง ให้มอง WBS เป็น **"แผนผังการแตกย่อยงานระดับบนลงล่าง" (Decomposition)** ตามกฎ 100% Rule:

```text
                                [ 1.0 ERP Transformation Project ] (100%)
                                                │
         ┌──────────────────────────────────────┼──────────────────────────────────────┐
         ▼                                      ▼                                      ▼
[ 1.1 Process & System ]             [ 1.2 Data Migration ]               [ 1.3 Change & Training ]
         │                                      │                                      │
  ├── 1.1.1 Finance Module               ├── 1.2.1 Legacy Extraction            ├── 1.3.1 Training Material
  └── 1.1.2 Procurement Module           └── 1.2.2 Data Cleansing               └── 1.3.2 User Training (Work Package)
```

### 100% Rule of WBS:
- WBS ต้องรวมงานทั้งหมดของโครงการไว้ 100% (งานใดไม่อยู่ใน WBS ถือว่าไม่อยู่ใน Scope ของโครงการ)
- ผลรวมของงานย่อยในแต่ละระดับล่าง ต้องเท่ากับ 100% ของงานในระดับบนเสมอ

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

### 5.1 6 Sub-processes ของ Scope Management
1. **Plan Scope Management:** วางแผนแนวทางการกำหนดและควบคุม Scope
2. **Collect Requirements:** รวบรวมความต้องการจาก Stakeholders ด้วยเทคนิคต่าง ๆ (Interview, Workshop, Survey)
3. **Define Scope:** จัดทำเอกสาร **Project Scope Statement** ระบุสิ่งที่อยู่ในและนอกขอบเขต (In Scope vs Out of Scope)
4. **Create WBS:** แตกย่อยงานออกเป็นโครงสร้างต้นไม้ จนถึงระดับ **Work Package**
5. **Validate Scope:** กระบวนการให้ลูกค้าหรือ Sponsor ตรวจรับ Deliverables อย่างเป็นทางการ (Accepted Deliverables)
6. **Control Scope:** ติดตามสถานะและควบคุมไม่ให้เกิด Scope Creep

### 5.2 Scope Baseline (ฐานอ้างอิงขอบเขต)
ประกอบด้วย 3 เอกสารสำคัญที่ถูกอนุมัติอย่างเป็นทางการ:
1. **Project Scope Statement**
2. **Work Breakdown Structure (WBS)**
3. **WBS Dictionary** (รายละเอียดคำอธิบายของแต่ละ Work Package)

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (WBS & In/Out of Scope)

- **Define Scope:**
  * *In Scope:* ระบบบัญชีการเงิน (Finance), การขาย (Sales), คลัง/จัดซื้อ (Materials Management), การผลิต (Production), HCM และการย้ายข้อมูลย้อนหลัง 3 ปี
  * *Out of Scope:* CRM, Advanced Analytics / BI หลัง Stabilization, Mobile Application สำหรับ Field Sales และการย้ายข้อมูลย้อนหลังเกิน 3 ปี
- **WBS Decomposition:**
  * แตกย่อยงานย้ายข้อมูลออกเป็น: *สกัดข้อมูลเก่า (Extract) → ล้างข้อมูล (Cleans) → แปลงฟอร์แมต (Transform) → นำเข้า ERP (Load)*

### 🏨 Core Scenario B: Hotel Booking Digital Platform (Scope Management ใน Agile/Hybrid)

- **Requirements to Backlog:**
  * แปลงความต้องการของผู้ใช้ให้กลายเป็น **User Stories** ใน Product Backlog
- **Scope Control:**
  * กำหนดขอบเขตของการเปิดตัวเวอร์ชันแรก (**MVP Scope Baseline**) ให้ชัดเจน ได้แก่ *ระบบค้นหาโรงแรม → ระบบเลือกห้องพัก → ระบบชำระเงิน* ส่วนระบบ Loyalty Points ถูกจัดเป็น Out of Scope สำหรับเปิดตัวเฟสแรก

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"WBS คือการเขียน Timeline หรือ Gantt Chart":**
   * *ความจริง:* WBS คือการแตกย่อย "สิ่งส่งมอบและชิ้นงาน" (Deliverable-oriented) ไม่ใช่การวางลำดับเวลาตามปฏิทิน
2. **"การตามใจลูกค้าด้วยการเพิ่มงานเล็ก ๆ น้อย ๆ เสมอ ถือเป็นบริการที่ดี":**
   * *ความจริง:* การเพิ่ม Scope โดยไม่มีกระบวนการควบคุมการเปลี่ยนแปลง (Change Control) จะทำลายทั้ง Schedule, Cost และ Quality ของโครงการ
3. **" Validate Scope ทำเฉพาะวันสุดท้ายของโครงการ":**
   * *ความจริง:* Validate Scope ควรทำทยอยทำเมื่อแต่ละ Deliverable เสร็จสิ้น เพื่อลดความเสี่ยงการถูกปฏิเสธงานทั้งหมดในวันสุดท้าย

---

## 8. PM Thinking & Decision Making

เมื่อมีคำขอเพิ่มขอบเขตงาน ให้ PM ใช้ **Scope Boundary Decision Filter**:

```text
Step 1: Check Scope Baseline -> คำขอนี้อยู่ใน Project Scope Statement / WBS dictionary หรือไม่?
Step 2: If OUT of Scope -> ชี้แจงขอบเขตเดิมอย่างนุ่มนวล และประเมินผลกระทบ (Impact Analysis)
Step 3: Propose Options ->
        - ทางเลือก A: ดำเนินการผ่านกระบวนการ Change Request (ขอเพิ่มเวลา/งบ)
        - ทางเลือก B: นำไปใส่ไว้ใน Phase ถัดไป (Out of Scope for current release)
        - ทางเลือก C: สลับงานเดิมออก (Scope Trade-off)
```

---

## 9. Reflection & Assessment

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. โครงการปัจจุบันของคุณมีเอกสาร **Scope Statement** ที่ระบุสิ่งที่ "ไม่อยู่ในขอบเขต" (Out of Scope) ชัดเจนแล้วหรือยัง?
2. คุณเคยใช้ **WBS** ในการแตกงานร่วมกับทีม หรือใช้เพียงแค่ความทรงจำในการสั่งงาน?

---

## 🌉 Bridge to Next Lesson: Lesson 08 — Project Schedule Management

เมื่อเรามี **Scope Baseline (WBS)** ที่ระบุงานทั้งหมด 100% แล้ว ขั้นตอนถัดไปคือการนำงานเหล่านั้นมาจัดลำดับการทำงาน ประเมินระยะเวลา และสร้าง **Schedule Baseline** ในบทถัดไป **Lesson 08** ครับ!

## PM Decision Thinking

**[PMBOK 6]** Scope Management ครอบคลุม plan scope, collect requirements, define scope, create WBS, validate scope และ control scope. **[PMBOK 7]** value thinking เตือนว่า scope ต้องผูกกับ outcome ไม่ใช่แค่เก็บ feature.

| Field | Lesson 07 Application |
|---|---|
| Decision | คำขอใหม่นี้อยู่ใน scope baseline หรือเป็น change request |
| Owner | PM วิเคราะห์และควบคุม scope; sponsor/customer/change authority ตัดสิน scope change |
| Inputs | scope statement, WBS, WBS dictionary, requirements, acceptance criteria, baseline, impact analysis |
| Options | accept in current scope, reject, defer to next phase, swap scope, approve with added time/cost |
| Trade-offs | customer satisfaction vs scope creep, feature value vs schedule/cost/quality impact |
| Risk | รับ “งานเล็ก ๆ” ซ้ำจน WBS และ baseline ใช้ควบคุมไม่ได้ |
| Evidence | traceability, acceptance criteria, impact on work packages, change decision |
| Next Action | บันทึก scope decision และ update baseline หากอนุมัติ change |

### PM Insight

Scope Management ที่ดีไม่ใช่การพูดว่า “ไม่ได้” แต่คือการพูดว่า “ได้ ถ้าองค์กรยอมรับ trade-off นี้” หรือ “ควรเลื่อน เพราะ value ยังไม่คุ้มกับ risk”. WBS ทำให้การคุยเรื่องงานไม่ลอยอยู่ในความรู้สึก.

## ERP Scenario

**[Scenario]** ERP Transformation มี 5 modules และ data migration จาก 6 legacy systems. Sales ขอเพิ่ม margin dashboard ก่อน go-live.

Scope decision:

- ถ้า dashboard อยู่ใน original reporting scope และมี acceptance criteria แล้ว ให้จัดเข้ากับ work package เดิม
- ถ้าเป็น report ใหม่ที่ต้องดึง data เพิ่ม ต้องเป็น change request
- ถ้า value สำคัญแต่กระทบ go-live ก่อน 1 ตุลาคม อาจ defer เป็น phase 1.1
- ถ้า sponsor ต้องการทำทันที ต้องประเมิน impact ต่อ schedule, cost, quality, testing และ key-user workload

## Hotel Booking Scenario

**[Scenario]** Hotel Booking MVP มี search, room selection, booking, payment และ back office. Marketing ขอ loyalty points ก่อน launch.

Scope decision:

- Product scope: loyalty points เพิ่ม capability ให้ลูกค้า
- Project scope: ต้องเพิ่ม design, build, test, integration, support และ partner communication
- MVP boundary: หาก direct booking outcome ยังขึ้นกับ payment stability มากกว่า loyalty ควร defer loyalty
- Trade-off: ทำ loyalty ตอนนี้อาจเพิ่ม conversion แต่ทำให้ launch readiness และ quality risk สูงขึ้น

## Real Enterprise Example

**[Instructor Interpretation]** Scope creep มักเริ่มจากคำว่า “แค่นิดเดียว”. ปัญหาไม่ใช่คำขอหนึ่งข้อ แต่คือไม่มีใครนับผลสะสมของคำขอนั้นใน WBS, schedule, test effort, training และ support. PM ที่ดีทำให้ขอบเขตเป็น visible contract ไม่ใช่ memory ของทีม.

## Common Mistakes

1. ใช้ WBS เป็น task list ตามเวลาแทน deliverable-oriented breakdown
2. เขียน in scope แต่ไม่เขียน out of scope
3. ไม่มี acceptance criteria ก่อน validate scope
4. รับ change ด้วยวาจาโดยไม่ update baseline
5. คิดว่า Agile ไม่ต้อง control scope ทั้งที่ต้อง control release/value boundary

## Common Misconceptions

| Misconception | Correction |
|---|---|
| WBS คือ Gantt chart | WBS คือโครงสร้าง deliverables/work packages ไม่ใช่ timeline |
| Scope control คือปฏิเสธลูกค้า | Scope control คือทำให้ trade-off โปร่งใส |
| Requirement ทุกอย่างต้องทำทันที | Requirement ต้องถูกจัดลำดับ value, risk และ release |
| Validate Scope ทำวันสุดท้าย | ควรตรวจรับเป็นระยะตาม deliverables |

## Interview Questions

### Definition

1. Product scope ต่างจาก project scope อย่างไร
2. Scope baseline ประกอบด้วยอะไรบ้าง

### Judgement

1. ถ้าผู้บริหารขอ feature เพิ่มโดยไม่เพิ่มงบ/เวลา คุณจะตอบอย่างไร
2. ถ้า requirement unclear แต่ทีม dev ขอเริ่ม build คุณจะจัดการ scope risk อย่างไร

### Behavioral

1. เล่าครั้งหนึ่งที่คุณจัดการ scope creep
2. คุณเคยทำให้ stakeholder ยอมรับ out-of-scope decision อย่างไร

### Scenario

1. ใน ERP ถ้า report ใหม่ต้องใช้ data จาก legacy system ที่ยังไม่ cleanse คุณจะตัดสินใจอย่างไร
2. ใน Hotel Booking ถ้า loyalty feature ถูกขอเพิ่มก่อน launch คุณจะจัด release boundary อย่างไร

## PM Dictionary

| Term | Meaning |
|---|---|
| Product Scope | คุณสมบัติของ product/service/result ที่จะสร้าง |
| Project Scope | งานทั้งหมดที่ต้องทำเพื่อส่งมอบ product scope |
| Scope Statement | เอกสารระบุ in scope, out of scope, assumptions, constraints และ deliverables |
| WBS | Work Breakdown Structure หรือโครงสร้างแตกงานแบบ deliverable-oriented |
| Work Package | งานระดับล่างสุดใน WBS ที่วางแผนและควบคุมได้ |
| WBS Dictionary | รายละเอียดของ work package เช่น owner, description, acceptance criteria |
| Scope Baseline | Scope statement + WBS + WBS dictionary ที่อนุมัติแล้ว |
| Scope Creep | ขอบเขตงานเพิ่มโดยไม่มีการควบคุม change |
| Validate Scope | การตรวจรับ deliverables อย่างเป็นทางการ |
| Control Scope | การติดตามและควบคุมการเปลี่ยนแปลง scope |

## Workshop

### Scenario

ERP sales ขอ margin dashboard ก่อน go-live. Hotel Booking marketing ขอ loyalty points ก่อน launch.

### Task

ให้ผู้เรียนทำ scope decision sheet 1 หน้า:

1. classify product scope vs project scope
2. ระบุ work packages ที่ได้รับผลกระทบ
3. in scope/out of scope/current phase/next phase
4. acceptance criteria ที่ต้องมี
5. impact ต่อ schedule, cost, quality, risk, stakeholder
6. recommendation และ change control path

### Debrief

คำตอบที่ดีต้องชี้ว่า “งานที่เพิ่ม” ไม่ใช่แค่ feature แต่รวม analysis, build, test, training, support และ acceptance.

## Assessment

ดูแบบประเมินหลักที่ [Lesson 07 Assessment](./Lesson-07_3-Assessment.md). แบบประเมินควรวัด scope boundary judgement, WBS decomposition และ change control มากกว่าการจำ 6 processes.

## Executive Summary

Scope Management ทำให้โครงการรู้ว่าจะทำอะไร ไม่ทำอะไร และตรวจรับอย่างไร. WBS ทำให้ scope กลายเป็นโครงสร้างงานที่ควบคุมได้. เมื่อมีคำขอเพิ่มงาน PM ต้องพา stakeholder ไปดู baseline, impact และ trade-off ไม่ใช่ตอบจากความเกรงใจ.

## Lesson Connection

Lesson 06 เปลี่ยน stakeholder expectations เป็น input. Lesson 07 เปลี่ยน input เหล่านั้นเป็น scope baseline และ WBS. Lesson 08 จะใช้ WBS เป็นฐานในการจัดลำดับงาน ประเมินเวลา และสร้าง schedule baseline.

## AI Continuation Context

Future AI agents must preserve the distinction between product scope and project scope. Keep WBS deliverable-oriented and tie scope decisions to ERP data/reporting changes and Hotel Booking MVP/release boundary decisions.

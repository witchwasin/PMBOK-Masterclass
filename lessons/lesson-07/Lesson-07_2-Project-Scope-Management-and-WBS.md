---
lesson: 7
sequence: 7.2
title: Project Scope Management and WBS
document_type: Lesson
level: Core
status: Active
prerequisite:
  - Lesson 06 — Project Stakeholder Management
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 07_2 — Project Scope Management and WBS

## 1. คำถามเปิดบท: ถ้าลูกค้าขอเพิ่มฟีเจอร์เล็กๆ อีก 5 อย่างโดยไม่ขอเพิ่มงบประมาณและเวลา โครงการของคุณจะลงเอยอย่างไร?

ลองพิจารณาเหตุการณ์คลาสสิกที่เกิดขึ้นในแทบทุกโครงการ:

> ระหว่างประชุมติดตามงานสัปดาห์ละครั้ง ผู้บริหารพูดขึ้นว่า *"ไหนๆ ก็พัฒนาระบบใหม่แล้ว ช่วยเพิ่มปุ่มส่งออกรายงาน PDF แบบพิเศษ และระบบแจ้งเตือนผ่าน SMS ให้หน่อยสิ น่าจะใช้เวลาทำแป๊บเดียวเองนะ"*

หาก PM ตอบตกลงด้วยความเกรงใจทีละเล็กทีละน้อย ผ่านไป 3 เดือน โครงการจะพบว่ามีฟีเจอร์เพิ่มขึ้นมาจากข้อตกลงเดิมมากกว่า 30 อย่าง เวลาล่าช้าไป 4 เดือน และงบประมาณบานปลาย!

ปรากฏการณ์นี้ในวิชาชีพบริหารโครงการเรียกว่า **"Scope Creep" (ขอบเขตงานรั่วไหล)**

> **คำถามสำคัญคือ:** เราจะควบคุมขอบเขตงานอย่างไร ให้ทำเฉพาะสิ่งที่จำเป็นต้องทำ (100% Rule) โดยไม่ขาดและไม่เกิน?

---

## 2. ปัญหาที่ต้องทำความเข้าใจ: การไม่แยกแยะความต้องการ และขาดโครงสร้างแตกงาน (WBS)

ปัญหาหลักที่ทำให้โครงการเสียการควบคุมด้าน Scope ได้แก่:

1. **การสับสนระหว่าง Product Scope กับ Project Scope:**
   * **Product Scope:** คุณสมบัติและฟังก์ชันของสิ่งที่จะสร้าง (ระบบทำงานอะไรได้บ้าง)
   * **Project Scope:** งานทั้งหมดที่ต้องทำเพื่อส่งมอบสิ่งนั้น (รวมถึงการอบรม การทดสอบ การย้ายข้อมูล และการบริหารจัดการ)
2. **ขอบเขตงานเป็นข้อความกว้างๆ ไม่ถูกย่อยเป็นโครงสร้างงาน (WBS):**
   * เขียนขอบเขตว่า "วางระบบ ERP" โดยไม่เคยนำมาแตกย่อยเป็น Work Packages ชัดเจน ทำให้เกิดงานหล่นหายหรือความเข้าใจไม่ตรงกัน
3. **การยอมรับคำขอโดยไม่ผ่านกระบวนการตรวจรับขอบเขต (Validate Scope):**
   * ไม่มีเกณฑ์การตรวจรับ (Acceptance Criteria) ที่ตกลงกันล่วงหน้า ทำให้เกิดการโต้แย้งในวันส่งมอบงาน

---

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

อ้างอิงจาก [references/PMBOK-Overview.md](file:///Users/arm/Documents/GitHub/PMBOK-Masterclass/references/PMBOK-Overview.md):

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
  * *In Scope:* ระบบบัญชีการเงิน (Finance), การจัดซื้อ (Procurement), การย้ายข้อมูลย้อนหลัง 3 ปี
  * *Out of Scope:* ระบบบริหารทรัพยากรบุคคล (HRM Phase 2), การย้ายข้อมูลย้อนหลังเกิน 3 ปี
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

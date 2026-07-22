---
lesson: 5
sequence: 5.2
title: Project Integration Management
document_type: Lesson
level: Core
status: Active
prerequisite:
  - Lesson 04 — 10 Project Management Knowledge Areas Overview
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 05_2 — Project Integration Management

## 1. คำถามเปิดบท: เมื่อทุกฝ่ายต้องการสิ่งที่ไม่ตรงกัน ใครคือผู้เชื่อมประสาน?

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

## 2. ปัญหาที่ต้องทำความเข้าใจ: การบูรณาการแบบผิวเผินและการตกเป็นเหยื่อของความขัดแย้ง

เมื่อองค์กรหรือ PM ขาดความเข้าใจใน **Project Integration Management** มักเกิดปัญหาเชิงโครงสร้างดังนี้:

1. ** Integration เป็นเพียงกระดาษรวบรวมเอกสาร (Document Aggregation):**
   * มองการทำ Project Plan เป็นเพียงการเอาไฟล์จากแผนกต่าง ๆ มาเย็บเล่มรวมกัน โดยไม่ได้วิเคราะห์ว่าแผนเหล่านั้นขัดแย้งกันเองหรือไม่
2. **PM กลายเป็นเพียง "คนเดินข่าว" (Message Carrier):**
   * รวบรวม Status Report จากแต่ละทีมมาแปะรวมกันในสไลด์ โดยไม่ได้วิเคราะห์ความเสี่ยง หรือใช้ดุลยพินิจชั่งน้ำหนักข้อแลกเปลี่ยน (Trade-off)
3. **การหลอกตัวเองด้วยสถานการณ์แบบ "แตงโม" (Watermelon Project Status):**
   * รายงานสถานะภายนอกเป็นสีเขียว (Green Status) เพราะแต่ละแผนกติ๊กส่งงานตามลิสต์ แต่เมื่อลึกลงไปกลับมีความขัดแย้งเชิงโครงสร้างสะสมอยู่ภายใน จนระบบพังทลายในวันเปิดตัว

---

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

อ้างอิงจาก [references/PMBOK-Overview.md](file:///Users/arm/Documents/GitHub/PMBOK-Masterclass/references/PMBOK-Overview.md):

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

## 9. Reflection & Assessment

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการของคุณ กระบวนการ Change Control ดำเนินการอย่างเป็นระบบผ่านการวิเคราะห์ผลกระทบข้ามมิติ หรือเกิดขึ้นจากการสั่งงานปากเปล่าของแต่ละฝ่าย?
2. คุณมีการวางแผนบริหารความรู้ (Manage Project Knowledge) เพื่อป้องกันปัญหาคนสำคัญลาออกแล้วความรู้ในโครงการหายไปหรือไม่?

---

## 🌉 Bridge to Next Lesson: Lesson 06 — Project Stakeholder Management

เมื่อเราเข้าใจกระบวนการบูรณาการ (**Integration Management**) ซึ่งเป็นหัวใจในการเชื่อมโยงทุกมิติแล้ว ปัจจัยสำคัญที่สุดที่จะขับเคลื่อนให้การบูรณาการและการตัดสินใจประสบความสำเร็จก็คือ **"ผู้คน" (People)** 

ในบทถัดไป **Lesson 06: Project Stakeholder Management** เราจะไปเจาะลึกวิธีระบุ วิเคราะห์ และบริหารความคาดหวังของผู้มีส่วนได้ส่วนเสียทุกกลุ่มอย่างมีกลยุทธ์!

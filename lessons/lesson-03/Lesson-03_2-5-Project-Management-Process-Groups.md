---
lesson: 3
sequence: 3.2
title: 5 Project Management Process Groups
document_type: Lesson
level: Foundation
status: Active
prerequisite:
  - Lesson 01 — ทำไม Project Manager ต้องรู้ PMBOK
  - Lesson 02 — Project Management Overview
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 03_2 — 5 Project Management Process Groups

## 1. คำถามเปิดบท: ถ้าโครงการเริ่มทำงานจริงไปแล้ว แต่พบว่าขอบเขตไม่ชัด เราควรกลับไป Planning หรือเดินหน้าต่อ?

ลองจินตนาการถึงสถานการณ์หน้างานของโครงการพัฒนาซอฟต์แวร์หรือการปรับเปลี่ยนระบบองค์กร:

> ทีมงานได้ดำเนินการพัฒนาโปรแกรม (Executing) ไปได้แล้ว 40% แต่นักวิเคราะห์ระบบพบข้อจำกัดใหม่ว่า ขอบเขตงานเดิม (Scope Baseline) ที่วางไว้ในแผน ไม่สามารถรองรับปริมาณ Transaction ของฝ่ายปฏิบัติการในชีวิตจริงได้

ในจุดนี้ มีความคิด 2 ทางเลือกที่มักเกิดขึ้นในทีม:
- **ความคิดแบบที่ 1:** *"เรารูปแบบมาแล้ว ต้องลุยเดินหน้าต่อ ห้ามย้อนกลับไปทำแผนใหม่เด็ดขาด ไม่อย่างนั้นจะเสียเวลาและถูกมองว่าวางแผนไม่ดี"*
- **ความคิดแบบที่ 2:** *"เมื่อพบข้อมูลใหม่ที่ไม่ตรงกับสมมติฐานเดิม เราต้องหยุดเพื่อทบทวนผลกระทบ ปรับแผนงาน (Replanning) และขออนุมัติขอบเขตใหม่ก่อนดำเนินการต่อ"*

> **คำถามสำคัญคือ:** การย้อนกลับไปปรับแผนในระหว่างที่โครงการกำลังดำเนินงานอยู่ ถือเป็นความล้มเหลวของการวางแผน หรือเป็นธรรมชาติที่ปกติและจำเป็นของการบริหารโครงการอย่างเป็นระบบ?

---

## 2. ปัญหาที่ต้องทำความเข้าใจ: การมอง Process Groups เป็น Waterfall Phase ที่ตายตัว

จุดล้มเหลวเชิงความคิดที่พบได้บ่อยที่สุดในวิชาชีพ Project Management คือการสับสนระหว่าง **Process Groups** กับ **Project Phases**:

1. **มองว่า Process Groups เป็นบันไดขั้นบันได (Linear Waterfall):**
   * เข้าใจผิดว่าต้องทำ Initiating ให้เสร็จ 100% -> แล้วทำ Planning 100% -> แล้วทำ Executing -> เมื่อถึง Executing แล้วห้ามแตะต้อง Planning อีกเด็ดขาด
2. **ละเลยการทำ Monitoring & Controlling อย่างต่อเนื่อง:**
   * มองว่าการควบคุมโครงการคือการทำรายงานส่งผู้บริหารในวันสิ้นงวด แทนที่จะเป็นกระบวนการวิเคราะห์ความเบี่ยงเบนและส่งสัญญาณเตือนล่วงหน้า (Early Warning)
3. **เข้าใจว่าการปิดโครงการ (Closing) คือการเซ็นรับงานเพียงอย่างเดียว:**
   * ไม่ได้ทำการส่งมอบเข้าสู่งานประจำ (Transition to Operation), ปิดสัญญา Vendor หรือถอดบทเรียน (Lessons Learned)

---

## 3. เหตุผลและที่มา: วงจรชีวิตและการจัดการความไม่แน่นอน (Feedback & Iteration)

ทำไม PMBOK จึงต้องจัดกลุ่มกระบวนการออกเป็น **5 Process Groups**?

เพราะในการบริหารโครงการ ความไม่แน่นอน (Uncertainty) และความรู้เกี่ยวกับโครงการจะค่อย ๆ ชัดเจนขึ้นตามเวลาที่ผ่านไป (Progressive Elaboration):
- ในวันแรกเริ่มโครงการ ข้อมูลยังมีอยู่อย่างจำกัด (ความเสี่ยงสูงสุด)
- เมื่อลงมือทำ จะเกิดข้อมูลเรียนรู้ใหม่ (Feedback Loop) ที่ทำให้เห็นข้อเท็จจริงที่ไม่เคยรู้มาก่อน

ดังนั้น องค์ความรู้ PMBOK จึงไม่ได้ออกแบบกระบวนการมาเพื่อให้ทำครั้งเดียวทิ้ง แต่จัดกลุ่มกระบวนการเพื่อให้เกิด **"วงจรการกำกับดูแลและการปรับตัวอย่างมีระบบ"** ตลอดอายุโครงการ

---

## 4. Mental Model: วงจรการไหลและการทำงานร่วมกันของ 5 Process Groups

เพื่อไม่ให้สับสน ให้สร้าง Mental Model ของ Process Groups ว่าเป็น **"ระบบเกียร์ที่ทำงานประสานกัน"** ไม่ใช่เส้นตรง:

```text
               ┌────────────────────────────────────────┐
               │                                        │
               ▼                                        │
┌──────────────┐      ┌──────────────┐      ┌───────────┴──┐      ┌──────────────┐
│  Initiating  │ ───► │   Planning   │ ───► │  Executing   │ ───► │   Closing    │
└──────────────┘      └──────────────┘      └──────────────┘      └──────────────┘
                             ▲                      │
                             │   Replanning Loop    │
                             └──────────────────────┘
                             ▲                      │
                             │  Monitor & Control   │
                             └──────────────────────┘
```

### ความสัมพันธ์ระหว่างกระบวนการ:
- **Initiating (การตั้งต้น):** ให้อำนาจและอนุมัติเป้าหมายหลัก
- **Planning (การวางแผน):** กำหนดแนวทางและ Baseline (เกิดขึ้นซ้ำได้เมื่อมี Change)
- **Executing (การลงมือทำ):** ขับเคลื่อนการสร้าง Deliverable
- **Monitoring & Controlling (การติดตามและควบคุม):** ดำเนินการควบคู่กับ Executing ตลอดเวลา เพื่อวัดความเบี่ยงเบนและส่งสัญญาณปรับแผน (Replanning)
- **Closing (การปิดโครงการ):** สรุปผล ส่งมอบงาน และปิดวงจร

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [references/PMBOK-Overview.md](file:///Users/arm/Documents/GitHub/PMBOK-Masterclass/references/PMBOK-Overview.md):

### 5.1 5 Process Groups และ Output สำคัญ

| Process Group | วัตถุประสงค์หลัก (Core Purpose) | Output สำคัญที่ได้ |
|---|---|---|
| **1. Initiating** | กำหนดโครงการใหม่หรือเฟสใหม่ และขออนุมัติเปิดโครงการอย่างเป็นทางการ | Project Charter, Stakeholder Register |
| **2. Planning** | กำหนดขอบเขต วัตถุประสงค์ และวางแนวทางปฏิบัติการเพื่อให้บรรลุเป้าหมาย | Project Management Plan, Scope/Schedule/Cost Baselines |
| **3. Executing** | ปฏิบัติงานตามที่กำหนดไว้ใน Project Management Plan เพื่อสร้างผลส่งมอบ | Deliverables, Work Performance Data, Change Requests |
| **4. Monitoring & Controlling** | ติดตาม ทบทวน และปรับปรุงความก้าวหน้า เพื่อให้สอดคล้องกับ Baseline | Work Performance Reports, Approved Change Requests |
| **5. Closing** | สรุปกิจกรรมทั้งหมดอย่างเป็นทางการเพื่อปิดโครงการหรือเฟส | Final Product/Service Transition, Lessons Learned, Closed Contracts |

### 5.2 ความแตกต่างระหว่าง Process Groups vs Project Phases
- **Project Phases (ระยะของโครงการ):** เป็นขั้นตอนเชิงลำดับเวลาของผลิตภัณฑ์ เช่น *Analysis → Design → Build → Test → Deploy*
- **Process Groups (กลุ่มกระบวนการบริหาร):** เป็นกลุ่มกิจกรรมบริหารที่ **เกิดขึ้นในทุก ๆ Phase** (เช่น ใน Phase Design ก็ต้องมี Initiating, Planning, Executing, Monitoring, Closing ของ Phase นั้น)

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation Process Flow

- **Initiating:** ผู้บริหารสูงสุดอนุมัติ **Project Charter** เปลี่ยนระบบ ERP มอบอำนาจให้ PM และกำหนด Sponsor หลัก
- **Planning:** จัดทำ **Project Management Plan** กำหนดสเปคโมดูลบัญชี แผนย้ายข้อมูล (Data Migration) และแผนอบรมผู้ใช้
- **Executing & Monitoring Loop:**
  * ทีม Vendor ทำการคอนฟิกระบบและเขียนโปรแกรมเชื่อมต่อ (Executing)
  * PM พบว่าผลการทดสอบ System Integration Test (SIT) ช้ากว่าแผน 2 สัปดาห์ (Monitoring)
  * PM ทำการวิเคราะห์หาสาเหตุ พบว่าโครงสร้างข้อมูลเก่าไม่สมบูรณ์ จึงยื่น Change Request ปรับแผนย้ายข้อมูลใหม่ (Replanning)
- **Closing:** ดำเนินการตรวจรับงาน (UAT Sign-off), ย้ายระบบไปสู่ Operation และจัดทำ Lessons Learned บันทึกปัญหาการย้ายข้อมูลไว้ใช้ในเฟสถัดไป

### 🏨 Core Scenario B: Hotel Booking Digital Platform Flow

- **Initiating:** ประกาศวิสัยทัศน์ผลิตภัณฑ์ อนุมัติงบพัฒนา Minimum Viable Product (MVP) แอปพลิเคชันจองโรงแรม
- **Planning:** วางแผนจัดลำดับ Feature ใน Product Backlog กำหนดสเปค Booking Engine และ Payment Gateway
- **Executing & Monitoring Loop (Agile Iteration):**
  * ทีมพัฒนาซอฟต์แวร์ทำงานส่งมอบงานเป็น Sprint ทุก 2 สัปดาห์ (Executing)
  * ทีม Product ติดตามค่า Conversion Rate ในช่วง Beta Test พบว่าผู้ใช้ละทิ้งการจองในหน้าชำระเงินสูง (Monitoring)
  * ทีมทำการปรับเปลี่ยนอันดับความสำคัญใน Backlog ใหม่ ปรับแก้ Checkout Flow ทันทีใน Sprint ถัดไป (Replanning/Adaptive Planning)
- **Closing:** ปิดเฟสการพัฒนา MVP ย้ายระบบขึ้น Production พร้อมส่งมอบเอกสารและวิธีการดูแลระบบให้แก่ทีม Product Operations

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"5 Process Groups คือ 5 ขั้นตอน (Phases) ของโครงการแบบ Waterfall":**
   * *ความจริง:* Process Groups เกิดขึ้นวนซ้ำและซ้อนทับกันตลอดเวลา แม้แต่ในโครงการ Agile ก็มีทั้ง 5 Process Groups อยู่ในทุก ๆ Sprint
2. **"Planning ต้องทำให้เสร็จ 100% ตั้งแต่วันแรกและห้ามแก้ไข":**
   * *ความจริง:* การวางแผนเป็นกระบวนการต่อเนื่อง (Progressive Elaboration) การปรับแผนเมื่อมีข้อมูลใหม่เป็นเรื่องปกติที่ต้องทำผ่านกระบวนการควบคุมการเปลี่ยนแปลง
3. **"Monitoring & Controlling คือการทำรายงานจับผิดทีมงาน":**
   * *ความจริง:* เป้าหมายของ Monitoring & Controlling คือการค้นหาความเบี่ยงเบนตั้งแต่เนิ่น ๆ เพื่อช่วยเหลือและปรับมาตรการแก้ไข (Preventive Action) ก่อนเกิดความเสียหาย
4. **"เมื่อส่งมอบระบบ Go-live แล้ว ถือว่า Closing เสร็จสิ้น":**
   * *ความจริง:* การ Go-live เป็นเพียงส่วนหนึ่งของ Executing/Deployment การ Closing จะสมบูรณ์เมื่อมีการเคลียร์สัญญา ปิดบัญชีโครงการ และส่งมอบเข้าสู่ Operation เรียบร้อยแล้วเท่านั้น

---

## 8. PM Thinking & Decision Making

เมื่อเกิดความเบี่ยงเบนในโครงการ ให้ PM ใช้ **Process Group Flow Decision Checklist**:

```text
1. สภาพการณ์ปัจจุบันอยู่ในกระบวนการใด?
   ├── หากอยู่ใน Executing แล้วพบปัญหา -> อย่าเพิ่งแก้ไขแบบเดาสุ่ม
   └── ให้สลับไปใช้ Monitoring & Controlling เพื่อหาสาเหตุรากเหง้า (Root Cause)

2. ปัญหานั้นกระทบต่อ Baseline (Scope, Schedule, Cost) หรือไม่?
   ├── ถ้าไม่กระทบ Baseline -> แก้ไขในระดับ Executing ได้ทันที
   └── ถ้ากระทบ Baseline -> ต้องผ่านกระบวนการ Change Request และย้อนกลับไป Replanning ใน Planning Group

3. การปรับเปลี่ยนนั้นกระทบต่อวัตถุประสงค์ใน Charter หรือไม่?
   ├── ถ้าไม่กระทบ -> PM และ CCB มีอำนาจอนุมัติปรับแผน
   └── ถ้ากระทบเป้าหมายหลักใน Charter -> ต้องย้อนกลับไปสเกลใน Initiating Group ร่วมกับ Sponsor
```

---

## 9. Reflection & Assessment

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการของคุณ มีกระบวนการใดใน 5 Process Groups ที่มักถูกมองข้ามหรือทำแบบข้ามขั้นตอนมากที่สุด (เช่น ข้าม Initiating ไป Executing เลย หรือไม่มี Closing)?
2. คุณเคยปฏิเสธการปรับแผน (Replanning) เพียงเพราะกลัวถูกมองว่าวางแผนไม่ดีหรือไม่ ทั้งที่ข้อมูลหน้างานชี้ชัดว่าแผนเดิมใช้ไม่ได้แล้ว?

---

## 🌉 Bridge to Next Lesson: Lesson 04 — 10 Project Management Knowledge Areas Overview

เมื่อเราเข้าใจการไหลของกระบวนการบริหารผ่าน **5 Process Groups** แล้ว ในบทถัดไป **Lesson 04** เราจะไปทำความรู้จักกับ **10 Knowledge Areas** (องค์ความรู้ทั้ง 10 ด้านที่ PM ต้องบริหาร) และดูว่าเมื่อนำ 5 Process Groups มาตัดกับ 10 Knowledge Areas จะเกิดเป็น **Process Matrix** ที่ช่วยให้ PM ไม่ลืมบริหารมิติใดมิติหนึ่งได้อย่างไร!

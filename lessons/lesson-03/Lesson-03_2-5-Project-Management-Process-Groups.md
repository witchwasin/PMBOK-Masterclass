---
lesson: 3
sequence: 3.2
title: 5 Project Management Process Groups
document_type: Lesson
level: Foundation
status: Draft
validation_status: Pending Final Repository Validation
version: 1.0
last_updated: 2026-07-22
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

## Opening Professional Question — ถ้าโครงการเริ่มทำงานจริงไปแล้ว แต่พบว่าขอบเขตไม่ชัด เราควรกลับไป Planning หรือเดินหน้าต่อ?

ลองจินตนาการถึงสถานการณ์หน้างานของโครงการพัฒนาซอฟต์แวร์หรือการปรับเปลี่ยนระบบองค์กร:

> ทีมงานได้ดำเนินการพัฒนาโปรแกรม (Executing) ไปได้แล้ว 40% แต่นักวิเคราะห์ระบบพบข้อจำกัดใหม่ว่า ขอบเขตงานเดิม (Scope Baseline) ที่วางไว้ในแผน ไม่สามารถรองรับปริมาณ Transaction ของฝ่ายปฏิบัติการในชีวิตจริงได้

ในจุดนี้ มีความคิด 2 ทางเลือกที่มักเกิดขึ้นในทีม:
- **ความคิดแบบที่ 1:** *"เรารูปแบบมาแล้ว ต้องลุยเดินหน้าต่อ ห้ามย้อนกลับไปทำแผนใหม่เด็ดขาด ไม่อย่างนั้นจะเสียเวลาและถูกมองว่าวางแผนไม่ดี"*
- **ความคิดแบบที่ 2:** *"เมื่อพบข้อมูลใหม่ที่ไม่ตรงกับสมมติฐานเดิม เราต้องหยุดเพื่อทบทวนผลกระทบ ปรับแผนงาน (Replanning) และขออนุมัติขอบเขตใหม่ก่อนดำเนินการต่อ"*

> **คำถามสำคัญคือ:** การย้อนกลับไปปรับแผนในระหว่างที่โครงการกำลังดำเนินงานอยู่ ถือเป็นความล้มเหลวของการวางแผน หรือเป็นธรรมชาติที่ปกติและจำเป็นของการบริหารโครงการอย่างเป็นระบบ?

---

## Why This Matters — การมอง Process Groups เป็น Waterfall Phase ที่ตายตัว

จุดล้มเหลวเชิงความคิดที่พบได้บ่อยที่สุดในวิชาชีพ Project Management คือการสับสนระหว่าง **Process Groups** กับ **Project Phases**:

1. **มองว่า Process Groups เป็นบันไดขั้นบันได (Linear Waterfall):**
   * เข้าใจผิดว่าต้องทำ Initiating ให้เสร็จ 100% -> แล้วทำ Planning 100% -> แล้วทำ Executing -> เมื่อถึง Executing แล้วห้ามแตะต้อง Planning อีกเด็ดขาด
2. **ละเลยการทำ Monitoring & Controlling อย่างต่อเนื่อง:**
   * มองว่าการควบคุมโครงการคือการทำรายงานส่งผู้บริหารในวันสิ้นงวด แทนที่จะเป็นกระบวนการวิเคราะห์ความเบี่ยงเบนและส่งสัญญาณเตือนล่วงหน้า (Early Warning)
3. **เข้าใจว่าการปิดโครงการ (Closing) คือการเซ็นรับงานเพียงอย่างเดียว:**
   * ไม่ได้ทำการส่งมอบเข้าสู่งานประจำ (Transition to Operation), ปิดสัญญา Vendor หรือถอดบทเรียน (Lessons Learned)

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบาย 5 Process Groups ได้โดยไม่สับสนกับ project phases
2. แยก Initiating, Planning, Executing, Monitoring & Controlling และ Closing จากมุมมอง decision flow
3. ตัดสินใจได้ว่าเมื่อพบข้อมูลใหม่ควร execute ต่อ, control, replan หรือ escalate
4. ใช้ ERP และ Hotel Booking scenarios เพื่ออธิบาย feedback loop และ progressive elaboration
5. เชื่อม Lesson 03 ไปสู่ Lesson 04 เรื่อง Knowledge Areas ได้อย่างถูกต้อง

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

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

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

## PM Decision Thinking

**[PMBOK 6]** Process Groups เป็นกลุ่มกิจกรรมบริหาร ไม่ใช่ลำดับ phase แบบแข็งตัว. **[PMBOK 7]** มุมมอง value delivery ทำให้ PM ใช้ process เพื่อช่วยตัดสินใจ ไม่ใช่ทำเอกสารเพื่อให้ครบพิธี.

| Field | Lesson 03 Application |
|---|---|
| Decision | ปัญหาที่พบควรแก้ใน Executing, ส่งเข้า Monitoring & Controlling, replan หรือ escalate กลับไป sponsor |
| Owner | PM เสนอ analysis; sponsor, change authority, หรือ steering committee ตัดสินเมื่อกระทบ baseline/charter |
| Inputs | charter, baseline, actual progress, work performance data, issue log, risk, impact analysis |
| Options | execute ต่อ, corrective action, preventive action, change request, rebaseline, defer scope |
| Trade-offs | speed vs control, local fix vs systemic fix, schedule protection vs adoption/readiness |
| Risk | treating process groups as linear phases; bypassing change control; hiding variance |
| Evidence | variance data, root cause, user impact, cost/schedule impact, go-live readiness |
| Next Action | สร้าง decision brief และระบุ process group ที่ต้อง activate ต่อ |

### PM Insight

Process Groups ที่ดีช่วยให้ PM รู้ว่า “ตอนนี้ต้องใช้โหมดการบริหารแบบไหน” ไม่ใช่บอกว่า “ตอนนี้เราอยู่ขั้นไหนแล้วห้ามย้อนกลับ”. การย้อนกลับไป Planning เพราะมี evidence ใหม่ไม่ใช่ความล้มเหลว แต่เป็นสัญญาณของ control ที่ทำงาน.

## ERP Scenario

**[Scenario]** ใน ERP Transformation ของคุณสมชายและคุณเอก TechConsult ต้องการเริ่ม build เพื่อรักษา timeline go-live ก่อน 1 ตุลาคม แต่ key users ยังไม่ยืนยัน master-data ownership.

ถ้า PM มอง Process Groups เป็น phase แข็งตัว เขาอาจตอบว่า “ผ่าน Planning แล้ว ต้อง build ต่อ”. แต่ถ้ามองแบบ professional PM เขาจะเห็นว่า:

- Executing: SI พร้อม build configuration
- Monitoring & Controlling: evidence ชี้ว่า data ownership ไม่พร้อม
- Planning: ต้อง replan data workstream, decision authority และ quality gate
- Initiating/Sponsor escalation: ถ้า replan กระทบ deadline หรือ charter-level objective ต้องเข้า steering committee
- Closing risk: ถ้าไม่แก้ ownership ตอนนี้ handover หลัง go-live จะล้มเหลว

Decision ที่ถูกต้องจึงไม่ใช่ “หยุดหรือไปต่อ” แบบง่าย ๆ แต่คือ “อนุญาตให้งานใดไปต่อได้ โดยงานใดต้อง replan และใครต้องตัดสินใจ”.

## Hotel Booking Scenario

**[Scenario]** ใน Hotel Booking Platform ทีมคุณสุทธิพบระหว่าง beta ว่า payment failure สูงและ checkout flow ทำให้ conversion ต่ำ ทั้งที่ launch date ถูกประกาศไว้แล้ว.

Process Group thinking ช่วยจัดการดังนี้:

- Executing: ทีมยังพัฒนา feature และแก้ bug
- Monitoring & Controlling: beta metrics แสดง conversion และ payment risk
- Planning: backlog, launch readiness, support plan และ release criteria ต้องถูกปรับ
- Closing: หากเปิด MVP แล้ว ต้องมี transition ไป product operations และ post-launch stabilization

สำหรับ product/digital work การ replan อาจเกิดทุก sprint แต่ยังต้องมี governance ชัดเจนว่า metric ใดทำให้ launch ได้, metric ใดทำให้ delay, และใครเป็น owner ของ outcome หลัง release.

## Real Enterprise Example

**[Instructor Interpretation]** องค์กรจำนวนมากมีปัญหาเพราะเริ่มจาก Executing ก่อนมี Initiating ที่ชัด เช่น “ซื้อระบบมาแล้วค่อยหาว่าใครเป็น sponsor”. ผลคือ PM ถูกบังคับให้ทำ schedule โดยไม่มี charter, stakeholder authority, benefit owner หรือ decision rule. Lesson 03 จึงต้องทำให้ผู้เรียนเห็นว่า Process Groups เป็นระบบป้องกันความสับสนเชิงอำนาจและความรับผิดชอบ.

## Common Mistakes

1. เรียก Process Groups ว่า phases และห้ามย้อนกลับไป planning
2. ทำ charter แบบพิธีการ แต่ไม่ใช้กำหนด authority และ success criteria
3. ทำแผนละเอียด แต่ไม่กำหนด change control
4. ทำ status report โดยไม่วิเคราะห์ variance และ decision required
5. ปิดโครงการเมื่อ vendor ส่งมอบ แต่ไม่ทำ transition to operation

## Common Misconceptions

| Misconception | Correction |
|---|---|
| Process Groups คือ waterfall | Process Groups เป็น management functions ที่เกิดซ้ำได้ |
| Planning เสร็จครั้งเดียว | Planning ปรับได้ผ่าน evidence และ control |
| Monitoring คือรายงานย้อนหลัง | Monitoring & Controlling ใช้ตัดสินใจตอบสนอง variance |
| Closing คือเซ็นรับงาน | Closing รวม handover, contract closure, lessons learned และ ownership |
| Agile ไม่ใช้ Process Groups | Agile ยังมี initiating, planning, executing, monitoring, closing เพียงเปลี่ยน cadence |

## Interview Questions

### Definition

1. อธิบายความแตกต่างระหว่าง Process Groups กับ Project Phases
2. Monitoring & Controlling ต่างจาก Executing อย่างไร

### Judgement

1. ถ้า UAT พบ requirement gap ก่อน go-live 3 สัปดาห์ คุณจะใช้ Process Groups อย่างไรในการตัดสินใจ
2. เมื่อ sponsor กดดันให้ launch แต่ readiness metrics ไม่ผ่าน PM ควรทำอะไร

### Behavioral

1. เล่าครั้งหนึ่งที่คุณต้อง replan หลังพบข้อมูลใหม่ คุณสื่อสารกับ stakeholder อย่างไร
2. คุณเคยปิด project แบบมี transition to operation อย่างไร

### Scenario

1. ใน ERP ถ้า data migration delay 2 สัปดาห์แต่ SI ขอ build ต่อ คุณจะเสนอ decision record อย่างไร
2. ใน Hotel Booking ถ้า payment failure สูงแต่ marketing launch แล้ว คุณจะ activate process group ใดก่อน

## PM Dictionary

| Term | Meaning |
|---|---|
| Process Group | กลุ่มกิจกรรมบริหารโครงการ 5 กลุ่มที่ช่วยตั้งต้น วางแผน ทำงาน ควบคุม และปิดงาน |
| Project Phase | ช่วงของ lifecycle/product delivery เช่น design, build, test, deploy |
| Progressive Elaboration | การทำให้ข้อมูลและแผนชัดขึ้นเมื่อมี evidence ใหม่ |
| Replanning | การปรับแผนอย่างเป็นระบบเมื่อข้อมูลจริงเปลี่ยน |
| Work Performance Data | ข้อมูลดิบจากงานจริง เช่น progress, defect, effort, test result |
| Change Request | คำขอปรับ scope, schedule, cost, quality หรือ baseline |
| Corrective Action | การกระทำเพื่อดึง performance กลับเข้าแผน |
| Preventive Action | การกระทำเพื่อลดโอกาสเกิดปัญหาก่อนเสียหาย |
| Closing | การปิด project/phase อย่างเป็นทางการ รวม handover และ lessons learned |

## Workshop

### Scenario

ERP workstream พบว่า master data ไม่พร้อม แต่ SI ขอเริ่ม build เพื่อรักษา deadline. Hotel Booking beta พบ payment failure สูงแต่ marketing ต้องการ launch ตามแผน.

### Task

ให้ผู้เรียนทำ decision brief 1 หน้า โดยระบุ:

1. process group ที่เกี่ยวข้อง
2. evidence ที่มีและ evidence ที่ยังขาด
3. baseline หรือ charter ที่อาจถูกกระทบ
4. options และ trade-offs
5. owner ของ decision
6. next action ภายใน 48 ชั่วโมง

### Debrief

คำตอบที่ดีต้องไม่ตอบแค่ว่า “กลับไป planning” หรือ “execute ต่อ” แต่ต้องแยกว่างานใดไปต่อได้ งานใดต้อง control และงานใดต้อง escalate.

## Assessment

ดูแบบประเมินหลักที่ [Lesson 03 Assessment](./Lesson-03_3-Assessment.md). ข้อสอบต้องวัดมากกว่าการจำชื่อ 5 Process Groups โดยให้ผู้เรียนตัดสินใจจาก ERP และ Hotel Booking scenarios ว่าควร execute, control, replan, escalate หรือ close อย่างไร.

## Executive Summary

5 Process Groups คือระบบคิดเพื่อกำกับโครงการตั้งแต่เริ่มต้นจนปิดงาน ไม่ใช่ phase แบบเดินเส้นตรง. PM มืออาชีพใช้ Initiating เพื่อทำให้ authority ชัด, Planning เพื่อสร้าง baseline, Executing เพื่อส่งมอบ, Monitoring & Controlling เพื่ออ่าน evidence และ Closing เพื่อส่งต่อ value ไป operation. เมื่อข้อมูลจริงเปลี่ยน การ replan อย่างมีหลักฐานคือความเป็นมืออาชีพ ไม่ใช่การถอยหลัง.

## Lesson Connection

Lesson 02 แยก project, operation, output, outcome และ value. Lesson 03 เพิ่มระบบบริหารให้ PM รู้ว่าต้องใช้ process group ใดในการควบคุมงานและตัดสินใจ. Lesson 04 จะต่อยอดด้วย 10 Knowledge Areas ซึ่งเป็นมิติเนื้อหาที่ PM ต้องบริหารในแต่ละ Process Group.

## AI Continuation Context

Future AI agents must preserve the distinction between Process Groups and Project Phases. Do not describe Initiating, Planning, Executing, Monitoring & Controlling, and Closing as rigid waterfall phases. Keep ERP and Hotel scenarios aligned with the scenario master files, and carry the Lesson 03 bridge into Lesson 04 Knowledge Areas.

---
lesson: 10
sequence: 10.2
title: Project Quality Management
document_type: Lesson
level: Core
status: Draft
validation_status: Pending Final Repository Validation
version: 1.0
last_updated: 2026-07-22
prerequisite:
  - Lesson 09 — Project Cost Management and Earned Value
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 10_2 — Project Quality Management

## Opening Professional Question — ถ้าส่งมอบงานได้ครบตาม Scope ตรงเวลา และไม่เกินงบ แต่เปิดใช้งานวันแรกแล้วระบบล่ม โครงการนี้มีคุณภาพหรือไม่?

ลองพิจารณาความล้มเหลวเชิงคุณภาพที่เกิดขึ้นในชีวิตจริง:

> แอปพลิเคชันจองโรงแรมใหม่ถูกส่งมอบครบทุกฟีเจอร์ในวันเทศกาลปีใหม่ตามกำหนดเป้าหมาย แต่เมื่อมีผู้ใช้งานพร้อมกันเพียง 1,000 คน ระบบชำระเงินกลับค้าง ยอดเงินถูกตัดแต่ไม่เกิดคำสั่งจอง และแอปพลิเคชันเด้งดับตลอดเวลา จนทำให้ลูกค้าแห่กันไปเขียนรีวิว 1 ดาวบน App Store

ในมิติของ **Triple Constraints (Scope, Schedule, Cost)** โครงการนี้ปฏิบัติตามแผนได้ทั้งหมด  
แต่ในมิติของ **Quality (คุณภาพ)** โครงการนี้กลับสร้างความเสียหายร้ายแรงต่อแบรนด์และธุรกิจ!

> **คำถามสำคัญคือ:** "คุณภาพ" (Quality) หมายถึงการทำของให้หรูหราที่สุด (High Grade) หรือหมายถึงการทำให้ตรงตามข้อกำหนดและใช้งานได้จริง (Fitness for Use & Conformance to Requirements)?

---

## Why This Matters — การสับสนระหว่าง QA กับ QC และการตรวจคุณภาพตอนงานเสร็จแล้ว

ปัญหาหลักที่ทำให้การบริหารคุณภาพล้มเหลว ได้แก่:

1. **การสับสนระหว่าง Quality Assurance (QA) กับ Quality Control (QC):**
   * **QA (การประกันคุณภาพ):** โฟกัสที่ "กระบวนการ" (Process-oriented) เพื่อป้องกันไม่ให้เกิดข้อผิดพลาดตั้งแต่วางแผน
   * **QC (การควบคุมคุณภาพ):** โฟกัสที่ "ผลผลิต" (Product-oriented) เพื่อตรวจหาข้อผิดพลาดหลังงานเสร็จ
2. **การพึ่งพาการตรวจหาบั๊กในวันสุดท้าย (Testing at the End):**
   * คิดว่าเรื่องคุณภาพเป็นหน้าที่ของทีม Tester ในช่วงสัปดาห์สุดท้าย ทั้งที่ต้นทุนในการแก้ไขข้อผิดพลาด (Cost of Quality) จะสูงขึ้นมหาศาลหากพบปัญหาในระยะท้าย
3. **การสับสนระหว่าง Quality กับ Grade:**
   * เข้าใจผิดว่าคุณภาพดีคือต้องหรูหราฟู่ฟ่า ทั้งที่แท้จริงแล้ว สินค้าราคาประหยัดที่ไม่มีบั๊กและใช้งานได้ตามสเปค ก็ถือว่ามีคุณภาพสูงตามมาตรฐานได้

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. แยก quality ออกจาก grade
2. แยก Quality Assurance, Quality Control และ Cost of Quality
3. กำหนด acceptance criteria และ quality gates ที่สัมพันธ์กับ scope/value
4. ตัดสินใจเมื่อ defect กระทบ go-live readiness
5. ใช้ ERP และ Hotel Booking scenarios เพื่อประเมิน quality risk, defect severity และ root cause

## 3. เหตุผลและที่มา: ต้นทุนของความผิดพลาด (Cost of Quality — COQ)

เหตุใดวิชาชีพ Project Management จึงเน้นย้ำเรื่อง **"Prevention over Inspection" (การป้องกันสำคัญกว่าการตรวจจับ)**?

เพราะต้นทุนในการแก้ไขข้อผิดพลาดจะเพิ่มขึ้นเป็นระดับทวีคูณ (Exponential Curve) ตามระยะเวลาที่ผ่านไป:

```text
[ Cost to Fix Defects ]
  • แก้ไขช่วง Requirement / Design ──► 1x (ต้นทุนต่ำสุด)
  • แก้ไขช่วง Development / Testing  ──► 10x
  • แก้ไขหลัง Go-live / Production  ──► 100x+ (เกิดความเสียหายต่อแบรนด์และเสียลูกค้า)
```

> **Core Rationale:**  
> **Quality Management ไม่ใช่การตามจับผิดเมื่อเกิดความเสียหาย แต่คือการสร้างกระบวนการเพื่อรับประกันว่า ผลงานส่งมอบตรงตามความต้องการ (Conformance to Requirements) และสามารถนำไปใช้งานได้จริง (Fitness for Use)**

---

## 4. Mental Model: กรอบความสัมพันธ์ระหว่าง QA vs QC และ Cost of Quality

เพื่อสร้างกรอบความคิดที่ถูกต้อง ให้แบ่ง **Cost of Quality (COQ)** ออกเป็น 2 ฝั่งหลัก:

```text
                                  ┌─── 1. Prevention Costs (ค่าป้องกัน): การเทรนนิ่ง, วาง Standard, Code Review
                                  │
      ┌─── Cost of Conformance ───┤
      │    (ค่าใช้จ่ายเพื่อทำถูกต้อง)   │
      │                           └─── 2. Appraisal Costs (ค่าประเมิน): การทดสอบ SIT/UAT, Audit, Inspection
COQ ──┤
      │                           ┌─── 3. Internal Failure Costs (ความผิดพลาดภายใน): แก้บั๊กก่อน Go-live, Rework
      │                           │
      └─── Cost of Non-Conformance ┤
           (ค่าเสียหายจากความผิดพลาด) └─── 4. External Failure Costs (ความผิดพลาดภายนอก): ระบบล่มหลัง Go-live,
                                                                                 เสียค่าปรับ, เสียชื่อเสียง
```

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

### 5.1 3 Sub-processes ของ Quality Management
1. **Plan Quality Management:** ระบุมาตรฐานคุณภาพ เกณฑ์การตรวจรับ (Acceptance Criteria) และกำหนดแนวทาง QA/QC
2. **Manage Quality (Quality Assurance):** ตรวจสอบว่ากระบวนการทำงานปฏิบัติตามมาตรฐานหรือไม่ และปรับปรุงกระบวนการอย่างต่อเนื่อง (Continuous Improvement)
3. **Control Quality (Quality Control):** ตรวจสอบสิ่งส่งมอบจริง (Deliverables) หาจุดบกพร่อง (Defects) และบันทึกผลการทดสอบ

### 5.2 เครื่องมือบริหารคุณภาพหลัก (Quality Tools)
- **Checklist:** รายการตรวจสอบขั้นตอนสำคัญไม่ให้ตกหล่น
- **Cause-and-Effect Diagram (Fishbone Diagram):** วิเคราะห์หาสาเหตุรากเหง้าของปัญหา (Root Cause Analysis)
- **Control Chart:** ติดตามความเสถียรของกระบวนการให้อยู่ในขอบเขตการควบคุม (Control Limits)

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (QA/QC ใน Data Migration & SIT/UAT)

- **Manage Quality (QA Process):**
  * กำหนดมาตรฐานการเขียนโค้ด การทำ Peer Review และการทำ Data Cleansing Rule ก่อนการย้ายข้อมูล
- **Control Quality (QC Inspection):**
  * ดำเนินการทดสอบ **System Integration Test (SIT)** เพื่อตรวจดูความถูกต้องของการเชื่อมต่อข้อมูล และการทำ **User Acceptance Test (UAT)** โดยให้ผู้ใช้งานจริงเซ็นรับรองความถูกต้องของกระบวนการปิดบัญชี

### 🏨 Core Scenario B: Hotel Booking Digital Platform (Automated Testing & Load Test)

- **Performance & Load Testing:**
  * ทำการทดสอบ Stress Test & Load Test จำลองผู้ใช้งานพร้อมกัน 10,000 คน ก่อนวันเปิดตัวจริง เพื่อป้องกันปัญหาระบบล่ม
- **Continuous Integration (CI/CD Quality Gate):**
  * ตั้งระบบตรวจเช็คอัตโนมัติ (Automated Unit Test) หากโค้ดใหม่ไม่ผ่านเกณฑ์ Coverage 80% ระบบจะไม่ยอมให้ Merge เข้าสู่สายการผลิต

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"คุณภาพดี หมายถึงการใส่ออปชันและความหรูหราให้มากที่สุด (High Grade)":**
   * *ความจริง:* สินค้า High Grade ที่เต็มไปด้วยบั๊ก ถือว่ามีคุณภาพต่ำกว่าสินค้า Low Grade ที่ทำงานได้เสถียร 100% ตามข้อกำหนด
2. **"เรื่องคุณภาพเป็นหน้าที่ของทีม QA/Tester เท่านั้น":**
   * *ความจริง:* คุณภาพเป็นหน้าที่ของทุกคนในทีม (Quality is everyone's responsibility) เริ่มตั้งแต่ผู้กำหนด Requirement, Developer จนถึง PM
3. **"การทำ QA/Testing เสียเวลาและทำให้โครงการล่าช้า":**
   * *ความจริง:* การข้ามขั้นตอน Testing อาจช่วยให้ได้ Go-live เร็วขึ้นในวันแรก แต่จะเสียเวลามากกว่ามหาศาลในการตามแก้ปัญหาหลัง Go-live (External Failure Cost)

---

## 8. PM Thinking & Decision Making

เมื่อพบข้อผิดพลาด (Defect) ในโครงการ ให้ PM ใช้ **Quality Defect Decision Steps**:

```text
Step 1: Defect Severity Assessment -> ข้อผิดพลาดนี้อยู่ในระดับใด?
        - Critical (กระทบธุรกรรมหลัก/ความปลอดภัย) -> Block การ Go-live ทันที
        - Major/Minor (กระทบความสะดวก แต่มี Workaround) -> ไป Step 2

Step 2: Evaluate Go-live Readiness ->
        - หากแก้ไขไม่ทันวัน Go-live: อนุญาตให้ Go-live โดยปิดฟังก์ชันที่มีปัญหาไว้ชั่วคราว หรือใช้ Workaround
        - ตั้งเป็น Known Defect ที่ต้องแก้ไขด่วนใน Patch ถัดไป

Step 3: Root Cause Analysis (Fishbone) -> หาสาเหตุรากเหง้าว่าทำไมกระบวนการ QA ถึงปล่อยให้เกิด Defect นี้ขึ้น เพื่อปรับปรุงกระบวนการในอนาคต
```

---

## 9. Reflection & Assessment

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการของคุณ มีการกำหนด **Acceptance Criteria (เกณฑ์การตรวจรับคุณภาพ)** ไว้ชัดเจนตั้งแต่วันแรกของการวางแผนแล้วหรือยัง?
2. โครงการของคุณเน้นหนักไปที่ **Quality Control (การตรวจจับบั๊ก)** หรือ **Quality Assurance (การป้องกันการเกิดบั๊ก)** มากกว่ากัน?

---

## 🌉 Bridge to Next Lesson: Lesson 11 — Project Resource Management

เมื่อเรามีกระบวนการรับประกันคุณภาพที่ชัดเจนแล้ว ปัจจัยขับเคลื่อนที่สำคัญที่สุดในการสร้างผลงานที่มีคุณภาพคือ **"ทีมงานและทรัพยากร" (Resources)** ในบทถัดไป **Lesson 11** เราจะไปดูวิธีการบริหารทรัพยากรคนและอุปกรณ์อย่างมีประสิทธิภาพครับ!

## PM Decision Thinking

**[PMBOK 6]** Quality Management ครอบคลุม plan quality, manage quality และ control quality. **[PMBOK 7]** quality ต้องผูกกับ fitness for use และ stakeholder value ไม่ใช่แค่ผ่าน checklist.

| Field | Lesson 10 Application |
|---|---|
| Decision | defect หรือ quality gap นี้ block go-live, accept with workaround, defer หรือ require rework |
| Owner | PM และ quality lead วิเคราะห์; sponsor/product/business owner ตัดสินเมื่อกระทบ release/value |
| Inputs | acceptance criteria, test results, defect severity, risk, user impact, regulatory impact, support readiness |
| Options | fix now, defer, disable feature, workaround, extend test, roll back, change acceptance criteria |
| Trade-offs | go-live speed vs external failure cost, workaround vs user trust, grade vs quality |
| Risk | ตรวจคุณภาพท้ายโครงการจน defect cost สูงและ adoption เสียหาย |
| Evidence | SIT/UAT results, defect trend, root cause, quality gate status, readiness checklist |
| Next Action | ทำ quality decision record พร้อม severity, owner, deadline และ release decision |

### PM Insight

Quality คือ “ตรงตามข้อกำหนดและใช้งานได้จริง” ไม่ใช่ “หรูที่สุด”. ระบบง่ายแต่เสถียรอาจมี quality สูงกว่าระบบเต็ม feature แต่ล่มเมื่อมีผู้ใช้จริง.

## ERP Scenario

**[Scenario]** ERP ต้องย้ายข้อมูลจาก 6 legacy systems และผ่าน SIT/UAT ก่อน go-live.

Quality decision:

- Master data error ใน finance close process เป็น critical defect เพราะกระทบงบและ audit
- Report alignment issue ที่มี workaround อาจเป็น major defect พร้อม corrective plan
- ถ้า UAT sign-off เป็นพิธีแต่ key users ไม่ทดสอบจริง quality evidence ไม่พอ
- PM ต้องใช้ root cause analysis ว่าปัญหาเกิดจาก data cleansing, mapping, configuration หรือ training

## Hotel Booking Scenario

**[Scenario]** Hotel Booking ต้องให้ลูกค้าจองและชำระเงินได้เชื่อถือได้ เพื่อเพิ่ม direct booking.

Quality decision:

- Payment failure สูงเป็น release blocker เพราะกระทบ revenue และ trust
- UI wording issue อาจแก้ใน patch ถ้าไม่กระทบ booking completion
- Load test ต้องสัมพันธ์กับ marketing campaign volume
- Defect หลัง launch มี external failure cost เช่น refund, review ต่ำ, lost conversion และ brand damage

## Real Enterprise Example

**[Instructor Interpretation]** หลายทีมลด testing เพื่อรักษา deadline แล้วจ่ายแพงหลัง go-live. ปัญหาที่แก้หนึ่งวันใน design อาจกลายเป็น war room หลายสัปดาห์ใน production. Lesson 10 ต้องทำให้ผู้เรียนเห็นว่าคุณภาพเป็น decision ทางธุรกิจ ไม่ใช่ขั้นตอนทางเทคนิคท้ายงาน.

## Common Mistakes

1. ทดสอบท้ายโครงการแทนที่จะสร้าง quality gate ตั้งแต่ requirement/design
2. ใช้ UAT sign-off เป็นพิธีโดยไม่มี acceptance evidence
3. วัดคุณภาพจากจำนวน defect อย่างเดียว ไม่ดู severity และ user impact
4. สับสน quality กับ grade
5. ปล่อย critical defect โดยเรียกว่า known issue แบบไม่มี owner/date

## Common Misconceptions

| Misconception | Correction |
|---|---|
| Quality คือ feature เยอะและ high grade | Quality คือ conformance to requirements และ fitness for use |
| QA คือ tester | QA คือ process assurance; QC คือ product inspection |
| Defect ทุกตัวต้อง block go-live | ต้องดู severity, workaround, risk และ value impact |
| Testing ทำให้ช้า | Prevention และ early testing ลด rework และ external failure cost |

## Interview Questions

### Definition

1. QA ต่างจาก QC อย่างไร
2. Quality ต่างจาก Grade อย่างไร

### Judgement

1. ถ้า defect critical ยังไม่แก้แต่ sponsor ต้องการ go-live คุณจะทำอย่างไร
2. ถ้า UAT ผ่านแต่ผู้ใช้จริงยังไม่มั่นใจ คุณจะอ่าน quality evidence อย่างไร

### Behavioral

1. เล่าครั้งหนึ่งที่คุณหยุด release เพราะ quality risk
2. คุณเคยทำ root cause analysis หลัง defect ใหญ่ ๆ อย่างไร

### Scenario

1. ใน ERP ถ้า master data error กระทบปิดบัญชี คุณจะตัดสิน release อย่างไร
2. ใน Hotel Booking ถ้า payment failure สูง คุณจะรายงาน quality risk อย่างไร

## PM Dictionary

| Term | Meaning |
|---|---|
| Quality | ความสามารถของผลส่งมอบในการตรงข้อกำหนดและใช้งานได้จริง |
| Grade | ระดับคุณสมบัติหรือความหรูของ product |
| Quality Assurance | การประกันว่ากระบวนการสร้างงานมีคุณภาพ |
| Quality Control | การตรวจผลส่งมอบเพื่อหา defect |
| Cost of Quality | ต้นทุนของการทำถูกและต้นทุนของการทำผิด |
| Prevention Cost | ต้นทุนป้องกัน defect |
| Appraisal Cost | ต้นทุนตรวจสอบ/ทดสอบ |
| Internal Failure | defect ก่อนส่งมอบ |
| External Failure | defect หลังส่งมอบหรือหลัง go-live |
| Acceptance Criteria | เกณฑ์ตรวจรับที่ตกลงไว้ |

## Workshop

### Scenario

ERP พบ master data defect ใน UAT. Hotel Booking beta พบ payment failure 8% ก่อน launch campaign.

### Task

ให้ผู้เรียนทำ quality release decision 1 หน้า:

1. defect severity และ affected user/value
2. acceptance criteria ที่ไม่ผ่าน
3. root cause hypothesis
4. options: fix, workaround, defer, block, split release
5. risk of go-live และ risk of delay
6. recommendation, owner และ deadline

### Debrief

คำตอบที่ดีต้องชี้ว่า defect ใดกระทบ value/trust/safety และต้องมี evidence ก่อน release ไม่ใช่อาศัยความหวัง.

## Assessment

ดูแบบประเมินหลักที่ [Lesson 10 Assessment](./Lesson-10_3-Assessment.md). แบบประเมินควรวัด judgement เรื่อง defect severity, quality gate, root cause และ release readiness.

## Executive Summary

Quality Management ทำให้ผลส่งมอบตรงข้อกำหนด ใช้ได้จริง และไม่สร้าง external failure cost. PM ต้องวาง quality ตั้งแต่ต้นด้วย acceptance criteria, QA/QC และ quality gates. การ go-live โดยไม่พร้อมไม่ใช่ความเร็ว แต่เป็นการย้ายต้นทุนไปหลังส่งมอบ.

## Lesson Connection

Lesson 09 อ่าน cost และ progress. Lesson 10 ทำให้เห็นว่างานที่ได้ต้องมีคุณภาพพอใช้จริง. Lesson 11 จะต่อไปที่ Resource Management เพราะคุณภาพเกิดไม่ได้ถ้าคน เวลา skill และ workload ไม่พร้อม.

## AI Continuation Context

Future AI agents must keep Quality separate from Grade and tie quality decisions to release readiness. Use ERP master data/UAT and Hotel Booking payment/load testing as recurring quality examples.

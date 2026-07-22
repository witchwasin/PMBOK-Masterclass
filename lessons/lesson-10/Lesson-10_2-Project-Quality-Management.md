---
lesson: 10
sequence: 10.2
title: Project Quality Management
document_type: Lesson
level: Core
status: Active
prerequisite:
  - Lesson 09 — Project Cost Management and Earned Value
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 10_2 — Project Quality Management

## 1. คำถามเปิดบท: ถ้าส่งมอบงานได้ครบตาม Scope ตรงเวลา และไม่เกินงบ แต่เปิดใช้งานวันแรกแล้วระบบล่ม โครงการนี้มีคุณภาพหรือไม่?

ลองพิจารณาความล้มเหลวเชิงคุณภาพที่เกิดขึ้นในชีวิตจริง:

> แอปพลิเคชันจองโรงแรมใหม่ถูกส่งมอบครบทุกฟีเจอร์ในวันเทศกาลปีใหม่ตามกำหนดเป้าหมาย แต่เมื่อมีผู้ใช้งานพร้อมกันเพียง 1,000 คน ระบบชำระเงินกลับค้าง ยอดเงินถูกตัดแต่ไม่เกิดคำสั่งจอง และแอปพลิเคชันเด้งดับตลอดเวลา จนทำให้ลูกค้าแห่กันไปเขียนรีวิว 1 ดาวบน App Store

ในมิติของ **Triple Constraints (Scope, Schedule, Cost)** โครงการนี้ปฏิบัติตามแผนได้ทั้งหมด  
แต่ในมิติของ **Quality (คุณภาพ)** โครงการนี้กลับสร้างความเสียหายร้ายแรงต่อแบรนด์และธุรกิจ!

> **คำถามสำคัญคือ:** "คุณภาพ" (Quality) หมายถึงการทำของให้หรูหราที่สุด (High Grade) หรือหมายถึงการทำให้ตรงตามข้อกำหนดและใช้งานได้จริง (Fitness for Use & Conformance to Requirements)?

---

## 2. ปัญหาที่ต้องทำความเข้าใจ: การสับสนระหว่าง QA กับ QC และการตรวจคุณภาพตอนงานเสร็จแล้ว

ปัญหาหลักที่ทำให้การบริหารคุณภาพล้มเหลว ได้แก่:

1. **การสับสนระหว่าง Quality Assurance (QA) กับ Quality Control (QC):**
   * **QA (การประกันคุณภาพ):** โฟกัสที่ "กระบวนการ" (Process-oriented) เพื่อป้องกันไม่ให้เกิดข้อผิดพลาดตั้งแต่วางแผน
   * **QC (การควบคุมคุณภาพ):** โฟกัสที่ "ผลผลิต" (Product-oriented) เพื่อตรวจหาข้อผิดพลาดหลังงานเสร็จ
2. **การพึ่งพาการตรวจหาบั๊กในวันสุดท้าย (Testing at the End):**
   * คิดว่าเรื่องคุณภาพเป็นหน้าที่ของทีม Tester ในช่วงสัปดาห์สุดท้าย ทั้งที่ต้นทุนในการแก้ไขข้อผิดพลาด (Cost of Quality) จะสูงขึ้นมหาศาลหากพบปัญหาในระยะท้าย
3. **การสับสนระหว่าง Quality กับ Grade:**
   * เข้าใจผิดว่าคุณภาพดีคือต้องหรูหราฟู่ฟ่า ทั้งที่แท้จริงแล้ว สินค้าราคาประหยัดที่ไม่มีบั๊กและใช้งานได้ตามสเปค ก็ถือว่ามีคุณภาพสูงตามมาตรฐานได้

---

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

อ้างอิงจาก [references/PMBOK-Overview.md](file:///Users/arm/Documents/GitHub/PMBOK-Masterclass/references/PMBOK-Overview.md):

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

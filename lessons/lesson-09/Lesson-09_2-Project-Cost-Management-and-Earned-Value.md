---
lesson: 9
sequence: 9.2
title: Project Cost Management and Earned Value
document_type: Lesson
level: Core
status: Active
prerequisite:
  - Lesson 08 — Project Schedule Management
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 09_2 — Project Cost Management and Earned Value

## 1. คำถามเปิดบท: ถ้างบประมาณถูกใช้ไปแล้ว 50% แต่เวลาผ่านไป 70% โครงการของคุณกำลังประหยัดเงิน หรือกำลังตกอยู่ในอันตราย?

ลองพิจารณาตัวเลขในรายงานงบประมาณของโครงการ:

> PM ได้รับอนุมัติตั้งงบประมาณโครงการไว้ 10 ล้านบาท เมื่อผ่านไปครึ่งทางของระยะเวลาโครงการ ฝ่ายการเงินรายงานว่า *"เพิ่งเบิกจ่ายเงินไปเพียง 4 ล้านบาท (40%) ถือว่าเราควบคุมงบประมาณได้ดีมากและประหยัดงบไปได้ถึง 1 ล้านบาท!"*

ฟังดูเหมือนเป็นข่าวดีใช่หรือไม่?  
แต่ถ้าสืบลึกลงไปแล้วพบว่า **"งานจริงเพิ่งทำเสร็จไปเพียง 20% เท่านั้น"** ภาพความจริงจะเป็นอย่างไร?

> **คำถามสำคัญคือ:** การวัดความก้าวหน้าทางการเงินด้วยการดูแค่ "เงินที่จ่ายไป" (Actual Cost) เทียบกับ "งบที่มี" (Budget) เพียงพอหรือไม่? และเราจะใช้วิธีใดเพื่อวัดประสิทธิภาพทางการเงินและงานที่ทำเสร็จจริงไปพร้อม ๆ กัน?

---

## 2. ปัญหาที่ต้องทำความเข้าใจ: การบริหารงบประมาณแบบการบัญชีหน้าเดียว

จุดล้มเหลวในการบริหารงบประมาณของโครงการ ได้แก่:

1. **การสับสนระหว่าง Financial Accounting กับ Project Cost Management:**
   * ฝ่ายการเงินมองเฉพาะการเบิกจ่ายเงินจริง (Cash Outflow) แต่ PM ต้องมองประสิทธิภาพของงานที่ได้แลกกับเงินที่จ่ายไป
2. **การประมาณการแบบไม่มีสำรองความเสี่ยง (No Contingency Reserve):**
   * ประมาณการค่าใช้จ่ายแบบเป๊ะ ๆ โดยไม่เผื่อเงินสำรองสำหรับความเสี่ยงที่คาดการณ์ได้ (Contingency Reserve) และความเสี่ยงที่คาดการณ์ไม่ได้ (Management Reserve)
3. **การวัดความก้าวหน้าด้วยการ "เดาด้วยสายตา" (Subjective Progress Reporting):**
   * รายงานว่างานเสร็จ 50% โดยไม่มีหลักฐานเชิงปริมาณของผลส่งมอบ (Deliverables) ที่วัดผลได้จริง

---

## 3. เหตุผลและที่มา: ต้นทุนคือวินัยทางการเงินที่สร้างความเชื่อมั่น

เหตุใด **Project Cost Management** จึงเป็นมิติที่ผู้บริหารระดับสูงให้ความสนใจมากที่สุด?

เพราะงบประมาณโครงการคือเงินลงทุนขององค์กร หากงบประมาณบานปลายโดยไม่เกิด Benefit ที่คุ้มค่า โครงการจะทำลาย Business Value ขององค์กรทันที

> **Core Rationale:**  
> **Cost Management ไม่ใช่แค่การประหยัดเงินให้ได้มากที่สุด แต่คือการทำให้มั่นใจว่า ทุกบาททุกสตางค์ถูกใช้อย่างคุ้มค่าและควบคุมให้อยู่ใน Cost Baseline ที่ได้รับการอนุมัติ**

---

## 4. Mental Model: เทคนิค Earned Value Management (EVM Triangle)

เพื่อสร้างกรอบความคิดที่ถูกต้อง ให้ใช้ **Earned Value Management (EVM)** ซึ่งเป็นเทคนิคมาตรฐานในการวัดประสิทธิภาพโครงการด้วย 3 ค่าพื้นฐาน:

```text
[ PV: Planned Value ]  ───► ค่าของงานที่ "ควรจะทำเสร็จ" ตามแผน ณ ปัจจุบัน (แผนบอกว่าควรทำกี่บาท)
[ EV: Earned Value ]   ───► ค่าของงานที่ "ทำเสร็จจริง" ณ ปัจจุบัน (งานจริงที่ได้มีมูลค่ากี่บาท)
[ AC: Actual Cost ]    ───► เงินที่ "จ่ายไปจริง" เพื่อทำงานนั้น ณ ปัจจุบัน (จ่ายเงินจริงไปกี่บาท)
```

```text
                                  ┌─── Cost Variance (CV = EV - AC)
                                  │    • CV > 0 : งบไม่บานปลาย (Under Budget) 🟢
                                  │    • CV < 0 : งบบานปลาย (Over Budget) 🔴
 [ EVM Performance Metrics ] ─────┤
                                  ├─── Schedule Variance (SV = EV - PV)
                                  │    • SV > 0 : เร็วกว่าแผน (Ahead of Schedule) 🟢
                                  │    • SV < 0 : ช้ากว่าแผน (Behind Schedule) 🔴
                                  │
                                  ├─── CPI (Cost Performance Index) = EV / AC (ค่างานที่ได้ต่อ 1 บาทที่จ่าย)
                                  └─── SPI (Schedule Performance Index) = EV / PV (ค่างานที่ได้ต่อ 1 บาทตามแผน)
```

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [references/PMBOK-Overview.md](file:///Users/arm/Documents/GitHub/PMBOK-Masterclass/references/PMBOK-Overview.md):

### 5.1 4 Sub-processes ของ Cost Management
1. **Plan Cost Management:** กำหนดแนวทางการประมาณการ จัดทำงบประมาณ และควบคุม Cost
2. **Estimate Costs:** ประมาณการค่าใช้จ่ายของแต่ละกิจกรรม (เช่น Bottom-up, Analogous, Parametric)
3. **Determine Budget:** รวบรวมประมาณการค่าใช้จ่ายย่อยและเงินสำรอง (Contingency Reserve) เข้าด้วยกันเป็น **Cost Baseline** (S-Curve)
4. **Control Costs:** ติดตามค่าใช้จ่าย ประเมิน EVM และคาดการณ์งบประมาณเมื่อจบโครงการ (EAC - Estimate at Completion)

### 5.2 การแบ่งส่วนงบประมาณโครงการ (Budget Components)
```text
[ Total Project Budget ] = Cost Baseline + Management Reserve
[ Cost Baseline ]        = Control Accounts + Contingency Reserve
[ Control Account ]      = Work Package Cost Estimates
```

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (EVM Calculation)

- **สถานการณ์:** โครงการตั้งงบไว้ 10 ล้านบาท (BAC = 10M) ผ่านไป 6 เดือน:
  * **PV (แผนงาน 6 เดือน):** ควรทำเสร็จ 50% -> PV = 5.0 ล้านบาท
  * **EV (งานเสร็จจริง):** พัฒนาโค้ดและทดสอบเสร็จจริง 30% -> EV = 3.0 ล้านบาท
  * **AC (จ่ายเงินจริง):** จ่ายให้ Vendor และทีมงานไปแล้ว -> AC = 4.0 ล้านบาท
- **วิเคราะห์ EVM:**
  * **CV = EV - AC** = 3.0 - 4.0 = **-1.0 ล้านบาท** (งบบานปลาย Over Budget 🔴)
  * **SV = EV - PV** = 3.0 - 5.0 = **-2.0 ล้านบาท** (งานล่าช้ากว่าแผน Behind Schedule 🔴)
  * **CPI = EV / AC** = 3.0 / 4.0 = **0.75** (ทุก 1 บาทที่จ่ายไป ได้เนื้องานกลับมาเพียง 0.75 บาท)
- **การตัดสินใจ:** PM ต้องรีบเสนอมาตรการควบคุมค่าใช้จ่ายด่วนก่อนงบหมดก่อนจบโครงการ

### 🏨 Core Scenario B: Hotel Booking Digital Platform (Cost Management ใน Cloud Services)

- **Cloud & Operational Cost Control:**
  * บริหารต้นทุนค่าบริการ Cloud Infrastructure (AWS/GCP) และ Payment Gateway Fees
  * ติดตามค่าใช้จ่ายผันแปรตามปริมาณ Transaction ของการจองห้องพัก เพื่อรักษางบประมาณในส่วนของการดำเนินงาน (OpEx)

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"การจ่ายเงินช้าหรือไม่ยอมจ่ายเงิน ให้ผลลัพธ์เดียวกับคำว่าประหยัดงบ":**
   * *ความจริง:* การดึงเช็คหรือจ่ายเงินช้าทำให้ค่า AC ต่ำลวงตา แต่ไม่ได้ช่วยให้ EV เพิ่มขึ้น EVM จะฟ้องความจริงทันทีผ่านค่า CPI และ SPI
2. **"Contingency Reserve คือเงินถุงเงินถังที่เอาไว้ใช้ทำอะไรก็ได้":**
   * *ความจริง:* Contingency Reserve มีไว้สำหรับความเสี่ยงที่ระบุไว้ล่วงหน้า (Known-Unknowns) และต้องผ่านการอนุมัติการใช้ตามกระบวนการ Change Control
3. **"CPI = 1.0 แปลว่าโครงการปลอดภัยสมบูรณ์แบบ":**
   * *ความจริง:* ต้องดูคู่กับ SPI เสมอ เพราะหาก CPI = 1.0 (จ่ายเงินตรงแผน) แต่ SPI = 0.5 (เนื้องานได้ครึ่งเดียว) แสดงว่าโครงการกำลังเกิดปัญหาใหญ่อย่างแน่นอน

---

## 8. PM Thinking & Decision Making

เมื่อค่า CPI หรือ SPI ต่ำกว่า 1.0 ให้ PM ใช้ **EVM Diagnostic Decision Steps**:

```text
Step 1: Check CPI & SPI Index
   ├── กรณี CPI < 1.0 & SPI < 1.0 (วิกฤตคู่) -> งานช้า แถมจ่ายแพงเกินจริง ต้องทบทวนกระบวนการทำงานและ Vendor ด่วน
   ├── กรณี CPI > 1.0 & SPI < 1.0 (จ่ายถูก แต่งานช้า) -> พิจารณาทำ Crashing (เอาเงินที่ประหยัดได้ไปเพิ่มคนเร่งงาน)
   └── กรณี CPI < 1.0 & SPI > 1.0 (งานเร็ว แต่จ่ายแพง) -> ตรวจสอบว่าเกิดการทำ OT หรือซื้อ Tool ราคาแพงเกินจำเป็นหรือไม่

Step 2: Calculate EAC (Estimate at Completion) -> คาดการณ์ว่างบรวมวันจบโครงการจะเป็นเท่าไร?
   ├── EAC = BAC / CPI (หากประสิทธิภาพยังคงเป็นแบบปัจจุบัน)
   └── นำตัวเลข EAC ใหม่เข้าขออนุมัติจาก Sponsor หากเกินงบประมาณเดิมที่ตั้งไว้
```

---

## 9. Reflection & Assessment

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการของคุณ คุณมีการวัดประสิทธิภาพงบประมาณด้วยตัวเลข **Earned Value (EV)** หรือดูเพียงแค่ยอดเงินเบิกจ่ายจากฝ่ายบัญชี?
2. ค่า **CPI** และ **SPI** ของโครงการคุณในปัจจุบันอยู่ที่ระดับใด (สูงกว่า หรือ ต่ำกว่า 1.0)?

---

## 🌉 Bridge to Next Lesson: Lesson 10 — Project Quality Management

เมื่อเราบริหาร **Scope, Schedule, Cost (Triple Constraints)** ได้อย่างเข้มงวดแล้ว มิติสำคัญที่จะรับประกันว่างานที่ทำเสร็จนั้นสามารถใช้งานได้จริงคือ **Project Quality Management** ในบทถัดไป **Lesson 10** ครับ!

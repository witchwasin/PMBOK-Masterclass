---
lesson: 9
sequence: 9.2
title: Project Cost Management and Earned Value
document_type: Lesson
level: Core
status: Draft
validation_status: Pending Final Repository Validation
version: 1.0
last_updated: 2026-07-22
prerequisite:
  - Lesson 08 — Project Schedule Management
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 09_2 — Project Cost Management and Earned Value

## Opening Professional Question — ถ้างบประมาณถูกใช้ไปแล้ว 50% แต่เวลาผ่านไป 70% โครงการของคุณกำลังประหยัดเงิน หรือกำลังตกอยู่ในอันตราย?

ลองพิจารณาตัวเลขในรายงานงบประมาณของโครงการ:

> PM ได้รับอนุมัติตั้งงบประมาณโครงการไว้ 10 ล้านบาท เมื่อผ่านไปครึ่งทางของระยะเวลาโครงการ ฝ่ายการเงินรายงานว่า *"เพิ่งเบิกจ่ายเงินไปเพียง 4 ล้านบาท (40%) ถือว่าเราควบคุมงบประมาณได้ดีมากและประหยัดงบไปได้ถึง 1 ล้านบาท!"*

ฟังดูเหมือนเป็นข่าวดีใช่หรือไม่?  
แต่ถ้าสืบลึกลงไปแล้วพบว่า **"งานจริงเพิ่งทำเสร็จไปเพียง 20% เท่านั้น"** ภาพความจริงจะเป็นอย่างไร?

> **คำถามสำคัญคือ:** การวัดความก้าวหน้าทางการเงินด้วยการดูแค่ "เงินที่จ่ายไป" (Actual Cost) เทียบกับ "งบที่มี" (Budget) เพียงพอหรือไม่? และเราจะใช้วิธีใดเพื่อวัดประสิทธิภาพทางการเงินและงานที่ทำเสร็จจริงไปพร้อม ๆ กัน?

---

## Why This Matters — การบริหารงบประมาณแบบการบัญชีหน้าเดียว

จุดล้มเหลวในการบริหารงบประมาณของโครงการ ได้แก่:

1. **การสับสนระหว่าง Financial Accounting กับ Project Cost Management:**
   * ฝ่ายการเงินมองเฉพาะการเบิกจ่ายเงินจริง (Cash Outflow) แต่ PM ต้องมองประสิทธิภาพของงานที่ได้แลกกับเงินที่จ่ายไป
2. **การประมาณการแบบไม่มีสำรองความเสี่ยง (No Contingency Reserve):**
   * ประมาณการค่าใช้จ่ายแบบเป๊ะ ๆ โดยไม่เผื่อเงินสำรองสำหรับความเสี่ยงที่คาดการณ์ได้ (Contingency Reserve) และความเสี่ยงที่คาดการณ์ไม่ได้ (Management Reserve)
3. **การวัดความก้าวหน้าด้วยการ "เดาด้วยสายตา" (Subjective Progress Reporting):**
   * รายงานว่างานเสร็จ 50% โดยไม่มีหลักฐานเชิงปริมาณของผลส่งมอบ (Deliverables) ที่วัดผลได้จริง

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. แยก cost estimate, cost baseline, contingency reserve และ management reserve
2. อธิบาย PV, EV, AC, CV, SV, CPI, SPI และ EAC ในระดับใช้งาน
3. อ่านสถานะ cost/schedule จาก EVM โดยไม่ถูกหลอกด้วยยอดเงินเบิกจ่าย
4. ตัดสินใจเมื่อ CPI/SPI ต่ำกว่า 1.0 และต้อง recover, reforecast หรือ escalate
5. ใช้ ERP และ Hotel Booking scenarios เพื่อแยก delivery working budget, funding envelope และ operating cost

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

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

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

## PM Decision Thinking

**[PMBOK 6]** Cost Management ครอบคลุม estimate, budget และ control costs. **[PMBOK 7]** value delivery เตือนว่า cost performance ต้องถูกอ่านร่วมกับ progress, risk และ outcome.

| Field | Lesson 09 Application |
|---|---|
| Decision | cost variance เป็นปัญหาจริง, timing issue, reserve usage หรือ value trade-off |
| Owner | PM วิเคราะห์ EVM; sponsor/finance/change authority ตัดสินเมื่อเกิน baseline หรือใช้ reserve |
| Inputs | BAC, PV, EV, AC, CPI, SPI, EAC, reserve status, procurement claims, work completion evidence |
| Options | continue, cost control, crash schedule, reduce scope, use contingency, request change, reforecast |
| Trade-offs | save cash vs delay value, crash schedule vs higher cost, reduce scope vs lower outcome |
| Risk | ดูแค่ AC ต่ำแล้วเข้าใจว่าประหยัด ทั้งที่ EV ต่ำกว่าแผนมาก |
| Evidence | accepted deliverables, EVM metrics, forecast, cost variance root cause |
| Next Action | ทำ EVM diagnostic brief และ update forecast/EAC |

### PM Insight

เงินที่ยังไม่จ่ายไม่ใช่เงินที่ประหยัดเสมอไป. ถ้า EV ต่ำกว่า PV มาก โครงการอาจ “ดูใช้เงินน้อย” เพราะยังทำงานไม่เสร็จ. PM ต้องวัดเงินคู่กับเนื้องานที่ได้รับจริง.

## ERP Scenario

**[Scenario]** ERP Transformation ใช้คำงบแบบล็อก: Working Budget 45 ล้านบาท สำหรับ delivery costs และ Total Funding Envelope 60 ล้านบาท รวม license และ management reserve.

Cost decision:

- หาก AC ใช้ไป 22 ล้านบาท แต่ EV เท่ากับงานมูลค่า 16 ล้านบาท CPI ต่ำกว่า 1.0 แปลว่าใช้เงินไม่มีประสิทธิภาพ
- หาก SPI ต่ำพร้อม CPI ต่ำ ต้องวิเคราะห์ vendor productivity, rework, data quality และ change scope
- ห้ามนำ Total Funding Envelope 60 ล้านบาทมาอ้างว่า working delivery budget ยังไม่เกินโดยไม่ขอ governance
- ถ้าต้องใช้ reserve ต้องระบุ risk trigger, approval และผลต่อ EAC

## Hotel Booking Scenario

**[Scenario]** Hotel Booking Platform มี delivery budget 12 ล้านบาท และหลัง launch จะมี cloud/payment operating costs.

Cost decision:

- ค่า cloud ระหว่าง development อาจอยู่ใน project cost แต่ run-rate หลัง launch เป็น operation/product cost
- ถ้า payment failure ทำให้ต้องเพิ่ม vendor support ต้องวิเคราะห์ว่าเป็น quality recovery หรือ scope growth
- Direct booking outcome 35% หลัง 18 เดือนต้องเทียบ benefit กับ total cost of ownership ไม่ใช่แค่ build budget
- PM ต้องรายงาน delivery cost, forecast, และ post-launch operating cost boundary ให้ชัด

## Real Enterprise Example

**[Instructor Interpretation]** รายงานงบหลายองค์กรบอกว่า “ใช้เงินไป 40%” โดยไม่บอกว่างานได้กี่เปอร์เซ็นต์. ถ้างานจริงได้ 20% โครงการไม่ได้ประหยัด แต่กำลังสะสม delay และอาจใช้เงินก้อนใหญ่ท้ายโครงการ. EVM บังคับให้ PM เอา money กับ earned work มาอยู่ในภาพเดียวกัน.

## Common Mistakes

1. อ่าน cost status จาก actual spend อย่างเดียว
2. ไม่แยก contingency reserve กับ management reserve
3. ไม่ผูก EV กับ accepted deliverables
4. ใช้ CPI/SPI เป็นตัวเลขรายงานแต่ไม่วิเคราะห์ root cause
5. ปะปน project delivery budget กับ operation cost หรือ license envelope

## Common Misconceptions

| Misconception | Correction |
|---|---|
| ใช้เงินน้อยกว่าแผนแปลว่าดี | ต้องดู EV/PV/AC พร้อมกัน |
| CPI ดีแปลว่าทุกอย่างดี | ต้องดู SPI, quality และ scope completion ด้วย |
| Reserve ใช้ได้ตามใจ PM | Reserve ต้องมี trigger และ approval ตาม governance |
| EVM ใช้เฉพาะงานก่อสร้าง | ใช้กับงานที่วัด deliverable completion ได้ รวมถึง ERP/digital |

## Interview Questions

### Definition

1. PV, EV และ AC ต่างกันอย่างไร
2. Cost baseline ต่างจาก total funding envelope อย่างไร

### Judgement

1. ถ้า CPI > 1 แต่ SPI < 1 คุณจะตีความอย่างไร
2. ถ้า EAC เกิน budget คุณจะเสนอ decision ต่อ sponsor อย่างไร

### Behavioral

1. เล่าครั้งหนึ่งที่คุณต้องอธิบาย cost variance ให้ผู้บริหาร
2. คุณเคยแก้ปัญหางบล้นโดยไม่ทำลาย quality หรือ scope อย่างไร

### Scenario

1. ใน ERP ถ้า working budget 45 ล้านบาทเริ่มเสี่ยงเกิน คุณจะทำ EVM diagnostic อย่างไร
2. ใน Hotel Booking ถ้า cloud cost สูงหลัง beta คุณจะแยก project cost กับ operation cost อย่างไร

## PM Dictionary

| Term | Meaning |
|---|---|
| BAC | Budget at Completion หรืองบรวมตาม baseline |
| PV | Planned Value มูลค่างานที่ควรเสร็จตามแผน |
| EV | Earned Value มูลค่างานที่เสร็จจริง |
| AC | Actual Cost เงินที่ใช้จริง |
| CV | Cost Variance = EV - AC |
| SV | Schedule Variance = EV - PV |
| CPI | Cost Performance Index = EV / AC |
| SPI | Schedule Performance Index = EV / PV |
| EAC | Estimate at Completion forecast งบเมื่อจบ |
| Contingency Reserve | เงินสำรองสำหรับ risk ที่ระบุแล้ว |
| Management Reserve | เงินสำรองระดับบริหารสำหรับ unknown unknowns |

## Workshop

### Scenario

ERP มี BAC ใน working budget 45 ล้านบาท ตอนนี้ PV 20, EV 15, AC 18 ล้านบาท. Hotel Booking ใช้งบ build ไป 7 ล้านบาท แต่ payment defect ทำให้ต้องใช้ vendor support เพิ่ม.

### Task

ให้ผู้เรียนทำ cost diagnostic brief 1 หน้า:

1. คำนวณ CV, SV, CPI, SPI
2. ตีความว่าปัญหาคือ cost, schedule หรือทั้งคู่
3. ระบุ root cause ที่ต้องตรวจ
4. เสนอ options และ trade-offs
5. ระบุว่าใช้ contingency/management reserve ได้หรือไม่ และต้องขออนุมัติใคร

### Debrief

คำตอบที่ดีต้องไม่หยุดที่ตัวเลข แต่เชื่อมตัวเลขกับ decision และ governance.

## Assessment

ดูแบบประเมินหลักที่ [Lesson 09 Assessment](./Lesson-09_3-Assessment.md). แบบประเมินควรวัดการคำนวณ EVM และ judgement ว่าควร recover, forecast, request change หรือ escalate อย่างไร.

## Executive Summary

Cost Management ทำให้เงินของโครงการถูกประมาณ ตั้งงบ ควบคุม และ forecast อย่างมีวินัย. EVM ช่วยให้ PM อ่านเงินคู่กับงานที่เสร็จจริง. สถานะงบที่ดีต้องแปลว่าใช้เงินเพื่อสร้าง earned work ไม่ใช่แค่ยังไม่ได้จ่าย.

## Lesson Connection

Lesson 08 สร้าง schedule baseline. Lesson 09 เพิ่ม cost baseline และ EVM เพื่ออ่าน performance ทั้งเวลาและเงิน. Lesson 10 จะต่อไปที่ Quality Management เพราะโครงการที่ตรงเวลาและไม่เกินงบยังล้มได้ถ้าผลงานใช้จริงไม่ได้.

## AI Continuation Context

Future AI agents must preserve ERP budget terminology exactly: Working Budget 45 ล้านบาท for delivery, Total Funding Envelope 60 ล้านบาท including license and management reserve. Keep Hotel Booking cost examples clear between build budget and post-launch operation cost.

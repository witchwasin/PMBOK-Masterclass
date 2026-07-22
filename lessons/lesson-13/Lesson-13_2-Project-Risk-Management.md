---
lesson: 13
sequence: 13.2
title: Project Risk Management
document_type: Lesson
level: Core
status: Draft
validation_status: Pending Final Repository Validation
version: 1.0
last_updated: 2026-07-22
prerequisite:
  - Lesson 12 — Project Communications Management
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 13_2 — Project Risk Management

## Opening Professional Question — ถ้าเหตุการณ์เลวร้ายเกิดขึ้นในโครงการ แล้ว PM พูดว่า "ไม่มีใครคาดคิดว่าเรื่องนี้จะเกิดขึ้น" ใครคือคนผิด?

ลองพิจารณาคำแก้ตัวที่มักได้ยินเมื่อโครงการเกิดวิกฤต:

> โครงการระบบชำระเงินล่าช้าไป 2 เดือนเพราะผู้ให้บริการ Payment Gateway เปลี่ยน API สเปคด่วน PM จึงรายงานต่อผู้บริหารว่า *"เหตุการณ์นี้เป็นปัจจัยภายนอกที่ไม่สามารถคาดเดาได้ จึงไม่ใช่ความผิดของทีมโครงการ"*

ฟังดูเหมือนเป็นเหตุผลที่น่าเห็นใจใช่หรือไม่?  
แต่ในวิชาชีพบริหารโครงการ คำถามคือ: **การเปลี่ยนแปลงของ Vendor ภายนอก เป็นเรื่องที่ไม่สามารถคาดการณ์ล่วงหน้าได้จริง ๆ หรือเป็นความประมาทเลินเล่อที่ไม่ได้เตรียมแผนรับมือ (Risk Response Plan) ไว้ตั้งแต่วันแรก?**

> **คำถามสำคัญคือ:** ความเสี่ยง (Risk) คืออะไร? และเหตุใดการบริหารความเสี่ยงจึงไม่ใช่การ "นั่งทำนายอนาคตแบบหมอดู" แต่เป็นการเตรียมความพร้อมและมาตรการตอบสนองอย่างเป็นวิทยาศาสตร์?

---

## Why This Matters — การสับสนระหว่าง Risk กับ Issue และการบริหารแบบ Firefighting

ความล้มเหลวหลักในการบริหารความเสี่ยง ได้แก่:

1. **การสับสนระหว่าง Risk กับ Issue:**
   * **Risk (ความเสี่ยง):** เหตุการณ์ไม่แน่นอนที่ *ยังไม่เกิดขึ้น* ในปัจจุบัน แต่ถ้าเกิดขึ้นจะมีผลกระทบต่อเป้าหมาย
   * **Issue (ปัญหา/ประเด็น):** เหตุการณ์ที่ *เกิดขึ้นแล้วในปัจจุบัน* และกำลังสร้างความเสียหายอยู่
2. **การทำ Risk Register ทิ้งไว้ในแฟ้ม (Paper-based Risk Management):**
   * ระบุความเสี่ยงใส่ตารางในวันแรกของโครงการ แล้วไม่เคยเปิดขึ้นมาทบทวนหรืออัปเดตอีกเลย จนกระทั่งความเสี่ยงกลายเป็น Issue วิกฤต
3. **มองความเสี่ยงเฉพาะในเชิงลบ (Negative Threat):**
   * ละเลยความเสี่ยงเชิงบวกหรือโอกาส (Positive Opportunity) ที่สามารถนำมาใช้ประโยชน์เพื่อเร่งโครงการให้เสร็จเร็วขึ้นหรือใช้น้อยลงได้

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. แยก risk ออกจาก issue และ assumption
2. ใช้ probability-impact thinking เพื่อจัดลำดับความเสี่ยง
3. เลือก response strategy สำหรับ threats และ opportunities
4. กำหนด risk owner, trigger, response และ monitoring cadence
5. ใช้ ERP และ Hotel Booking scenarios เพื่อวิเคราะห์ data, vendor, payment, adoption และ launch risks

## 3. เหตุผลและที่มา: ความไม่แน่นอนคือสิ่งเดียวที่แน่นอนในโครงการ

เหตุใด **Project Risk Management** จึงเป็นเครื่องมือแยกแยะระหว่าง PM มือสมัครเล่น กับ PM มืออาชีพ?

เพราะโครงการคือการสร้างสิ่งใหม่ภายใต้สภาพแวดล้อมที่เปลี่ยนแปลงตลอดเวลา หาก PM รอให้ปัญหาเกิดแล้วค่อยตามแก้ (Firefighting Mode) โครงการจะสูญเสียทั้งงบประมาณ เวลา และความน่าเชื่อถือ

> **Core Rationale:**  
> **Risk Management คือการเพิ่มโอกาสในการประสบความสำเร็จ โดยการเพิ่มโอกาสและผลกระทบของเหตุการณ์เชิงบวก (Opportunities) และลดโอกาสและผลกระทบของเหตุการณ์เชิงลบ (Threats)**

---

## 4. Mental Model: เมทริกซ์โอกาสและผลกระทบ (Probability-Impact Matrix) และกลยุทธ์รับมือ

เพื่อสร้างกรอบความคิดที่ถูกต้อง ให้ประเมินความเสี่ยงด้วย **Probability & Impact Matrix**:

```text
High Impact
     ▲
     │   [ Medium Risk ]            │   [ HIGH RISK / CRITICAL ]
     │   • วางแผนมาตรการป้องกัน       │   • ต้องมีแผนรับมือ (Response Plan)
     │                               │   • ติดตามใกล้ชิดโดย PM
     │                               │
     ├─── ─── ─── ─── ─── ─── ─── ───┼─── ─── ─── ─── ─── ─── ─── ───
     │   [ LOW RISK ]                │   [ Medium Risk ]
     │   • บันทึกใน Watchlist         │   • กำหนดเจ้าของความเสี่ยง (Risk Owner)
     │   • เฝ้าระวังตามรอบ             │
     └───────────────────────────────┴───────────────────────────────► High Probability
```

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

### 5.1 7 Sub-processes ของ Risk Management
1. **Plan Risk Management:** กำหนดแนวทางและกรอบการบริหารความเสี่ยง
2. **Identify Risks:** ระบุความเสี่ยงทั้งหมดที่เป็นไปได้ (ได้ *Risk Register*)
3. **Perform Qualitative Risk Analysis:** จัดลำดับความเสี่ยงด้วย Probability & Impact Matrix
4. **Perform Quantitative Risk Analysis:** คำนวณตัวเลขผลกระทบทางการเงิน (เช่น EMV - Expected Monetary Value)
5. **Plan Risk Responses:** วางแผนมาตรการรับมือความเสี่ยงและกำหนด **Risk Owner**
6. **Implement Risk Responses:** ดำเนินการตามมาตรการเมื่อเกิดสัญญาณเตือน (Risk Triggers)
7. **Monitor Risks:** ติดตามความเสี่ยงเดิม ค้นหาความเสี่ยงใหม่ และทบทวนประสิทธิผลของมาตรการ

### 5.2 กลยุทธ์การรับมือความเสี่ยง (Risk Response Strategies)

| ประเภทความเสี่ยง | กลยุทธ์การรับมือ (Response Strategy) | อธิบายและตัวอย่าง |
|---|---|---|
| **Threats (เชิงลบ)** | **1. Escalate** | ยกระดับให้ผู้บริหาร/Sponsor ตัดสินใจเนื่องจากเกินอำนาจ PM |
| | **2. Avoid** | ปรับเปลี่ยนแผนงานเพื่อเลี่ยงความเสี่ยงนั้น 100% |
| | **3. Transfer** | โอนย้ายความเสี่ยงไปให้ผู้อื่น (เช่น ซื้อประกัน, ทำสัญญา Fixed-price กับ Vendor) |
| | **4. Mitigate** | ลดโอกาสเกิดหรือลดความรุนแรงของผลกระทบ (เช่น ทำการทดสอบชั่วคราว, เพิ่ม Backup) |
| | **5. Accept** | ยอมรับความเสี่ยง (Passive = เฝ้าระวัง / Active = ตั้งงบสำรอง Contingency Reserve) |
| **Opportunities (เชิงบวก)** | **Exploit / Share / Enhance / Accept** | ดึงโอกาสมาใช้ประโยชน์ เช่น ใช้เทคโนโลยีใหม่เพื่อลดเวลา |

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (Data Cleansing & Legacy Risk)

- **Identify Risk:** มีความเสี่ยงที่ข้อมูลลูกค้าในระบบเดิมจะมีความซ้ำซ้อนและไม่สมบูรณ์ ทำให้ย้ายเข้า ERP ใหม่ไม่ผ่าน
- **Risk Strategy (Mitigation):** จัดทำโปรแกรมล้างข้อมูลอัตโนมัติ (Data Cleansing Script) และทำการทดสอบ Mock Migration ล่วงหน้า 3 รอบ เพื่อลดโอกาสเกิดปัญหาในวัน Go-live จริง

### 🏨 Core Scenario B: Hotel Booking Digital Platform (Third-party API Risk)

- **Identify Risk:** ผู้ให้บริการ Payment Gateway อาจเกิดปัญหาระบบขัดข้องในช่วงวันหยุดเทศกาลที่มี Transaction สูง
- **Risk Strategy (Transfer/Mitigation & Contingency):** เชื่อมต่อระบบชำระเงินสำรองอีก 1 ราย (Fallback Gateway) เพื่อสลับช่องทางชำระเงินให้อัตโนมัติทันทีหากค่ายแรกเกิดปัญหา

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"การบริหารความเสี่ยงคือการทำให้ความเสี่ยงในโครงการกลายเป็นศูนย์ (Zero Risk)":**
   * *ความจริง:* ทุกโครงการมีความเสี่ยง การกำจัดความเสี่ยง 100% อาจต้องใช้เงินและเวลาจนโครงการไม่คุ้มที่จะทำ เป้าหมายคือการรักษาระดับความเสี่ยงให้อยู่ในระดับที่ยอมรับได้ (Risk Tolerance)
2. **"เมื่อเขียน Risk Register เสร็จแล้ว ถือว่าจบหน้าที่บริหารความเสี่ยง":**
   * *ความจริง:* Risk Register ต้องเป็นเอกสารที่มีชีวิต (Living Document) ที่ต้องนำมาทบทวนในประชุมโครงการทุกสัปดาห์
3. **"เมื่อเกิดความเสี่ยงขึ้น ให้ PM คิดวิธีแก้ปัญหาคนเดียว":**
   * *ความจริง:* ความเสี่ยงแต่ละข้อต้องมี **Risk Owner** ที่ชัดเจน ซึ่งเป็นผู้เชี่ยวชาญเฉพาะด้านที่ได้รับมอบหมายให้ติดตามและรับผิดชอบความเสี่ยงนั้น

---

## 8. PM Thinking & Decision Making

เมื่อต้องรับมือกับความเสี่ยงในโครงการ ให้ PM ใช้ **Risk Response Decision Steps**:

```text
Step 1: Risk Identification -> เกิดอะไรขึ้น? โอกาสเกิดเท่าไร? ผลกระทบสม่ำเสมอแค่ไหน?
Step 2: Risk Scoring -> คำนวณ Risk Score = Probability × Impact
Step 3: Assign Risk Owner -> กำหนดตัวบุคคลที่เหมาะสมที่สุดในการติดตามความเสี่ยงข้อนี้
Step 4: Formulate Strategy -> 
        - ถ้าผลกระทบสูงมาก แต่เลี่ยงไม่ได้ -> Transfer (ทำสัญญาโอนเสี่ยง/ทำประกัน)
        - ถ้าผลกระทบสูง และเลี่ยงได้ -> Avoid / Mitigate (ปรับแผนเพื่อลดโอกาสเกิด)
Step 5: Set Trigger Points -> กำหนดสัญญาณเตือนว่า เมื่อไรที่ต้องเริ่มใช้แผนรับมือด่วน (Contingency Plan)
```

---

## 9. Reflection & Assessment

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการของคุณ มีการจัดทำเอกสาร **Risk Register** และกำหนด **Risk Owner** ของความเสี่ยงแต่ละข้อไว้อย่างชัดเจนแล้วหรือยัง?
2. ความเสี่ยงที่สำคัญที่สุด 3 อันดับแรกของโครงการคุณในปัจจุบันคืออะไร และมีแผนรับมือเตรียมไว้แล้วหรือยัง?

---

## 🌉 Bridge to Next Lesson: Lesson 14 — Project Procurement Management

เมื่อเราวิเคราะห์ความเสี่ยงแล้ว พบว่าความเสี่ยงบางประการต้องใช้กลยุทธ์โอนย้าย (Transfer) หรืออาศัยความเชี่ยวชาญจากภายนอก เครื่องมือที่เราต้องใช้คือ **Project Procurement Management** ในบทถัดไป **Lesson 14** ครับ!

## PM Decision Thinking

**[PMBOK 6]** Risk Management ครอบคลุม plan, identify, qualitative/quantitative analysis, response, implement และ monitor. **[PMBOK 7]** uncertainty และ adaptability ทำให้ risk เป็นระบบตัดสินใจต่อเนื่อง.

| Field | Lesson 13 Application |
|---|---|
| Decision | risk นี้ควร avoid, mitigate, transfer, accept, escalate หรือ exploit/enhance |
| Owner | PM ดู risk system; risk owner รับผิดชอบ response; sponsor ตัดสิน risk เกิน tolerance |
| Inputs | risk statement, probability, impact, trigger, owner, response cost, contingency, tolerance |
| Options | prevent, reduce impact, transfer to vendor/insurance, accept with reserve, escalate, use opportunity |
| Trade-offs | response cost vs exposure, speed vs certainty, transfer vs control, mitigation vs contingency |
| Risk | risk register ไม่ถูกใช้จน risk กลายเป็น issue โดยไม่มี owner |
| Evidence | trigger status, trend, residual risk, response effectiveness, issue conversion |
| Next Action | update risk register และ activate response เมื่อ trigger เกิด |

### PM Insight

Risk Management ไม่ใช่การทำนายอนาคตให้ถูกทุกข้อ แต่คือการทำให้องค์กรไม่ตกใจเมื่ออนาคตไม่เป็นไปตามแผน. Risk ที่ไม่มี owner และ trigger เป็นแค่ข้อความ ไม่ใช่การบริหาร.

## ERP Scenario

**[Scenario]** ERP Transformation มี data migration จาก 6 legacy systems, 80 key users, SI TechConsult และ go-live target ก่อน 1 ตุลาคม.

Risk examples:

- Data quality risk: legacy data ไม่สะอาด ทำให้ migration fail; response คือ mock migration, data owner และ cleansing gate
- Key-user availability risk: UAT/training ไม่พอ; response คือ capacity agreement และ backfill
- Vendor dependency risk: TechConsult resource ไม่พอ; response คือ contract escalation และ delivery milestone
- Go-live readiness risk: support owner ไม่ชัด; response คือ readiness checklist และ transition owner

## Hotel Booking Scenario

**[Scenario]** Hotel Booking Platform พึ่ง payment gateway, hotel partner inventory และ launch campaign เพื่อสร้าง direct booking outcome.

Risk examples:

- Payment gateway outage: transfer/mitigate ด้วย fallback provider และ monitoring
- Inventory accuracy risk: mitigate ด้วย partner onboarding และ validation rule
- Conversion risk: monitor beta funnel และ run UX experiment
- Launch overload risk: load test ก่อน campaign และ contingency rollback

## Real Enterprise Example

**[Instructor Interpretation]** ความเสี่ยงที่มีอยู่ใน slide แต่ไม่มี owner, trigger และ response budget จะไม่ช่วยเมื่อเกิดเหตุจริง. PM ต้องทำให้ risk ถูกพูดถึงเป็นจังหวะปกติของ project ไม่ใช่เฉพาะตอนมี crisis.

## Common Mistakes

1. เขียน risk เป็นปัญหาที่เกิดแล้ว
2. ไม่มี risk owner ที่รับผิดชอบ response จริง
3. ให้ทุก risk เป็น high จนไม่มี priority
4. ไม่มี trigger ที่บอกว่าเมื่อไรต้องลงมือ
5. ไม่ทบทวน residual risk หลัง implement response

## Common Misconceptions

| Misconception | Correction |
|---|---|
| Risk คือสิ่งไม่ดีเท่านั้น | Risk รวม threats และ opportunities |
| Risk register ทำครั้งเดียว | ต้อง update และ monitor ตลอดโครงการ |
| Risk owner คือ PM เสมอ | ควรเป็นคนที่มีความรู้/อำนาจต่อ risk นั้น |
| Accept risk คือไม่ทำอะไร | Active accept อาจรวม contingency reserve และ trigger |

## Interview Questions

### Definition

1. Risk ต่างจาก issue อย่างไร
2. Probability-impact matrix ใช้จัดลำดับ risk อย่างไร

### Judgement

1. คุณจะเลือก transfer แทน mitigate เมื่อใด
2. ถ้า risk เกิน authority ของ PM คุณจะ escalate อย่างไร

### Behavioral

1. เล่าครั้งหนึ่งที่คุณ identify risk ก่อนกลายเป็น issue
2. คุณเคยจัด risk review ให้ทีมอย่างไร

### Scenario

1. ใน ERP ถ้า data migration risk สูง คุณจะกำหนด trigger และ response อย่างไร
2. ใน Hotel Booking ถ้า payment gateway risk สูง คุณจะเลือก response strategy ใด

## PM Dictionary

| Term | Meaning |
|---|---|
| Risk | เหตุการณ์ไม่แน่นอนที่หากเกิดจะกระทบ objective |
| Issue | เหตุการณ์ที่เกิดขึ้นแล้วและต้องจัดการ |
| Probability | โอกาสเกิด |
| Impact | ผลกระทบหากเกิด |
| Risk Owner | ผู้รับผิดชอบติดตามและดำเนิน response |
| Trigger | สัญญาณเตือนว่าต้อง activate response |
| Mitigate | ลดโอกาสหรือผลกระทบของ threat |
| Transfer | โอนความเสี่ยงบางส่วนให้ภายนอก เช่น vendor/insurance |
| Accept | ยอมรับ risk โดยมีหรือไม่มี contingency |
| Residual Risk | ความเสี่ยงที่เหลือหลัง response |

## Workshop

### Scenario

ERP data migration risk สูงและ key users ไม่พร้อม. Hotel Booking payment gateway และ inventory accuracy เสี่ยงก่อน launch.

### Task

ให้ผู้เรียนทำ risk response plan 1 หน้า:

1. risk statement
2. probability/impact score
3. risk owner
4. response strategy
5. trigger
6. contingency/reserve implication
7. residual risk และ monitoring cadence

### Debrief

คำตอบที่ดีต้องมี owner และ trigger ไม่ใช่แค่ “ติดตามอย่างใกล้ชิด”.

## Assessment

ดูแบบประเมินหลักที่ [Lesson 13 Assessment](./Lesson-13_3-Assessment.md). แบบประเมินควรวัด judgement เรื่อง risk/issue distinction, response strategy และ trigger/owner design.

## Executive Summary

Risk Management คือการบริหารความไม่แน่นอนอย่างมีระบบ. PM ต้อง identify, analyze, assign owner, plan response, implement และ monitor risk อย่างต่อเนื่อง. Risk ที่ดีไม่ใช่แค่ถูกเขียน แต่ต้องพร้อมใช้เมื่อ trigger เกิด.

## Lesson Connection

Lesson 12 ทำให้ risk สื่อสารได้ถูกคน. Lesson 13 ทำให้ risk ถูกบริหารก่อนกลายเป็น issue. Lesson 14 จะต่อไปที่ Procurement Management เพราะ risk บางอย่างถูกจัดการผ่าน vendor, contract และ transfer strategy.

## AI Continuation Context

Future AI agents must keep Risk Management as a living decision process with owner, trigger and response. Use ERP data migration/key-user risk and Hotel Booking payment/inventory risk as recurring examples.

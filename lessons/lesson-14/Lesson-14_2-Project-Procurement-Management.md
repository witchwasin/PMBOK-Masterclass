---
lesson: 14
sequence: 14.2
title: Project Procurement Management
document_type: Lesson
difficulty: Core
estimated_study_time: 85
status: Active
validation_status: Validated
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 13 — Project Risk Management
related_lessons:
  - Lesson 15 — Agile Project Management
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 14_2 — Project Procurement Management

## Beginner Safety

- **ควรรู้แล้ว:** L13 risk/change evidence; **คำศัพท์ใหม่:** SOW, acceptance, payment authorization.
- **Novice trap:** เซ็นรับงาน vendor ไม่เท่ากับ business acceptance หรืออนุมัติจ่ายเงิน.

## Opening Professional Question — ถ้า Vendor ส่งมอบงานล่าช้าไป 3 เดือน แล้วชี้หน้าบอกว่า "ในสัญญาไม่ได้ระบุสเปคเรื่องนี้ไว้" ใครคือคนที่ต้องรับผิดชอบ?

ลองพิจารณาข้อพิพาทสัญญาคลาสสิกในโครงการจัดซื้อจัดจ้าง:

> บริษัทว่าจ้าง Vendor ภายนอกมาพัฒนาระบบ แต่เมื่อถึงวันตรวจรับงาน Vendor กลับส่งมอบระบบที่ไม่สามารถรองรับผู้ใช้งานพร้อมกันเกิน 50 คนได้ เมื่อ PM ทวงถาม Vendor ตอบอย่างภาคภูมิใจว่า *"ในสัญญา และเอกสาร TOR ระบุเฉพาะฟังก์ชันการทำงาน แต่ไม่ได้ระบุข้อกำหนดด้านประสิทธิภาพ (Non-functional Performance) ไว้ ดังนั้นถ้าต้องการให้ทำเพิ่ม ต้องเซ็นสัญญาฉบับใหม่และจ่ายเงินเพิ่ม 1 ล้านบาท"*

ในมิติของ Vendor พวกเขาทำถูกต้องตามลายลักษณ์อักษรในสัญญา  
แต่ในมิติของโครงการ PM กำลังตกอยู่ในฝันร้ายของการบริหารผู้ขายที่ไม่ครอบคลุม!

> **คำถามสำคัญคือ:** การบริหารการจัดซื้อจัดจ้าง (Procurement Management) คือหน้าที่ของ "ฝ่ายจัดซื้อ" เพียงอย่างเดียว หรือเป็นหน้าที่ของ PM ที่ต้องบริหารข้อตกลง สัญญา สิ่งส่งมอบ และความสัมพันธ์กับผู้ขายตลอดอายุโครงการ?

---

## Why This Matters — การปล่อยให้สัญญาเป็นเรื่องของฝ่ายกฎหมาย และการบริหารแบบทิ้งขว้าง

ปัญหาหลักในการบริหารการจัดซื้อจัดจ้าง ได้แก่:

1. **PM ถอนตัวออกจากการร่างสัญญากับ Vendor (TOR & Contract Formulation):**
   * ปล่อยให้ฝ่ายจัดซื้อหรือฝ่ายกฎหมายเป็นผู้เจรจาสัญญาโดยไม่มีสเปคการทำงานจริงและความเข้าใจเชิงเทคนิค ทำให้สัญญาขัดกับความเป็นจริงหน้างาน
2. **การคัดเลือกสัญญาผิดประเภท (Wrong Contract Type Selection):**
   * เลือกใช้สัญญาแบบราคาคงที่ (Fixed-price) กับงานที่มีความไม่แน่นอนสูง จน Vendor ขาดทุนและทิ้งงาน หรือเลือกใช้สัญญาแบบคิดตามจริง (Time & Material) กับงานที่ควบคุมงบยากจนงบบานปลาย
3. **การขาดการตรวจรับและควบคุมคุณภาพสิ่งส่งมอบระหว่างทาง (Mid-term Control):**
   * ไม่เคยติดตามความก้าวหน้าของ Vendor ระหว่างทาง รอตรวจรับทีเดียววันสิ้นสุดสัญญา จนแก้ไขอะไรไม่ทัน

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบาย procurement lifecycle ตั้งแต่ plan, conduct ถึง control procurements
2. ทำ make-or-buy analysis ในระดับ PM decision
3. เลือก contract type ให้เหมาะกับ scope certainty และ risk allocation
4. กำหนด acceptance criteria, milestone payment และ vendor performance control
5. ใช้ ERP และ Hotel Booking scenarios เพื่อบริหาร SI/vendor/API/provider risk

## 3. เหตุผลและที่มา: สัญญาคือเครื่องมือบริหารความเสี่ยงและความสัมพันธ์

เหตุใด **Project Procurement Management** จึงมีความสำคัญอย่างยิ่งต่อโครงการในยุคปัจจุบัน?

เพราะไม่มีองค์กรใดที่มีทรัพยากรและความเชี่ยวชาญครบทุกด้านภายในตนเอง โครงการส่วนใหญ่จึงต้องพึ่งพาผู้ขาย ผู้รับจ้าง และคู่สัญญาภายนอก (Vendors & Suppliers)

> **Core Rationale:**  
> **Procurement Management ไม่ใช่แค่การออกใบสั่งซื้อ (PO) แต่คือกระบวนการจัดหาผลิตภัณฑ์ บริการ หรือผลลัพธ์จากภายนอกองค์กร การบริหารสัญญาข้อตกลง และการรับประกันว่าคู่สัญญาปฏิบัติตามข้อตกลงเพื่อส่งมอบ Value ตามที่ตกลงไว้**

---

## 4. Mental Model: ประเภทของสัญญาและการกระจายความเสี่ยง (Contract Spectrum)

เพื่อสร้างกรอบความคิดที่ถูกต้อง ให้มองประเภทของสัญญาเป็นการกระจายความเสี่ยงระหว่าง **ผู้ว่าจ้าง (Buyer)** และ **ผู้ขาย (Seller)**:

```text
[ Buyer Risk สูงสุด ]                                                      [ Seller Risk สูงสุด ]
         │                                                                          │
         ▼                                                                          ▼
┌───────────────────────────┐      ┌───────────────────────────┐      ┌───────────────────────────┐
│ Cost-Reimbursable (CR)    │      │ Time & Material (T&M)     │      │ Fixed-Price (FP)          │
│ (สัญญาจ่ายตามทุนจริง + ค่าแรง)│      │ (คิดตามเวลาและทรัพยากรจริง)  │      │ (สัญญาจ้างเหมาราคาคงที่)   │
└───────────────────────────┘      └───────────────────────────┘      └───────────────────────────┘
• เหมาะกับ: งานวิจัย/ไม่แน่นอนสูง     • เหมาะกับ: งานที่ต้องการคนเสริม    • เหมาะกับ: สเปคชัดเจน 100%
• Buyer รับความเสี่ยงเรื่องงบ       • กำหนด上限 (Cap) ได้               • Seller รับความเสี่ยงเรื่องงบ
```

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

### 5.1 3 Sub-processes ของ Procurement Management
1. **Plan Procurement Management:** กำหนดว่าจะซื้ออะไร ซื้ออย่างไร คัดเลือกประเภทสัญญา และจัดทำเอกสารประกวดราคา (TOR/RFP)
2. **Conduct Procurements:** เผยแพร่เอกสาร รับข้อเสนอ คัดเลือกผู้ขาย เจรจาต่อรอง และเซ็นสัญญา
3. **Control Procurements:** บริหารความสัมพันธ์ ติดตามผลงาน ตรวจรับสิ่งส่งมอบ อนุมัติการจ่ายเงิน และปิดสัญญา (Procurement Closure)

### 5.2 ภาพรวมการจัดซื้อจัดจ้างภาครัฐ (10 ขั้นตอนตาม Canonical Source)
```text
1. จัดทำแผนจัดซื้อจัดจ้างประจำปี ──► 2. ทำร่าง TOR/สเปค ──► 3. รายงานขอซื้อขอจ้าง ──► 4. แต่งตั้งคณะกรรมการ ──► 5. ดำเนินการคัดเลือก
                                                                                                           │
10. บริหารสัญญา & ตรวจรับ ◄── 9. ทำสัญญา/ข้อตกลง ◄── 8. ประกาศผลผู้ชนะ ◄── 7. อนุมัติสั่งซื้อสั่งจ้าง ◄── 6. พิจารณาผลคัดเลือก
```

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (Vendor & Contract Management)

- **Contract Selection & TOR:**
  * ใช้สัญญาแบบ **Firm Fixed Price (FFP)** สำหรับการติดตั้งโมดูลมาตรฐาน แต่กำหนดเกณฑ์การจ่ายเงินเป็นงวด ๆ ตาม **Deliverable Milestones** (เช่น งวดที่ 1: Blue Print, งวดที่ 2: Config & SIT, งวดที่ 3: UAT & Go-live)
- **Control Procurement:**
  * PM ร่วมกับคณะกรรมการตรวจรับพัสดุ เข้าตรวจเช็คผลการทำ SIT ของ Vendor อย่างละเอียดก่อนอนุมัติจ่ายเงินงวดที่ 2 เพื่อป้องกันปัญหา Vendor ทิ้งงานในงวดสุดท้าย

### 🏨 Core Scenario B: Hotel Booking Digital Platform (Agile T&M Contract)

- **Time & Material with Cap (T&M):**
  * ว่าจ้างบริษัท Outsource พัฒนา Mobile App แบบ Agile สัญญาคิดค่าแรงรายเดือนตามจริง (T&M) แต่กำหนดกรอบงบประมาณสูงสุด (Not-to-Exceed Cap) และกำหนดสิทธิ์ในทรัพย์สินทางปัญญา (IP Rights) ไว้ในสัญญาอย่างชัดเจน

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"สัญญาแบบราคาคงที่ (Fixed Price) ปลอดภัยสำหรับผู้ว่าจ้าง 100% เสมอ":**
   * *ความจริง:* หากสเปคใน TOR ไม่ชัดเจน สัญญา Fixed Price จะนำไปสู่การทะเลาะเรื่อง Change Order และในที่สุด Vendor อาจยอมโดนยึดมัดจำและทิ้งงาน ซึ่งสร้างความเสียหายต่อโครงการมากกว่า
2. **"เรื่องสัญญาและการตรวจรับเป็นหน้าที่ของฝ่ายจัดซื้อ ไม่เกี่ยวกับ PM":**
   * *ความจริง:* ฝ่ายจัดซื้อดูเรื่องระเบียบและเอกสาร แต่ PM คือคนที่รู้ดีที่สุดว่าสิ่งส่งมอบตรงตามความต้องการทางเทคนิคและสเปคของโครงการหรือไม่
3. **"การปิดโครงการ (Project Close) สามารถทำได้โดยไม่ต้องปิดสัญญา Vendor":**
   * *ความจริง:* การปิดโครงการจะสมบูรณ์ได้ ต้องผ่านกระบวนการ **Procurement Closure** เคลียร์เงินประกันการชำระเงิน และออกหนังสือรับรองงานให้ Vendor เรียบร้อยก่อน

---

## 8. PM Thinking & Decision Making

เมื่อต้องจัดหาและบริหาร Vendor ให้ PM ใช้ **Procurement Decision Steps**:

```text
Step 1: Make-or-Buy Analysis -> งานนี้ควรทำเองภายในองค์กร (Make) หรือว่าจ้างภายนอก (Buy)?
        - ถ้าเน้น Core Competency & ความลับองค์กร -> Make (ทำเอง)
        - ถ้าขาดทักษะ & ต้องการความเร็ว -> Buy (ว่าจ้างภายนอก)

Step 2: Select Contract Type ->
        - สเปคชัดเจน ไม่เปลี่ยน -> Fixed Price (FP)
        - ต้องการผู้เชี่ยวชาญชั่วคราว -> Time & Material (T&M)
        - งานทดลอง/วิจัย -> Cost Reimbursable (CR)

Step 3: Milestone-based Control -> แบ่งการจ่ายเงินตามผลงานที่ตรวจรับจริง (Accepted Deliverables) ไม่จ่ายเงินล่วงหน้าโดยไม่มีหลักฐานงาน
```

---

## 9. Reflection & Assessment

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการของคุณ มีการจัดทำเอกสาร **TOR / สเปค** ที่ระบุเกณฑ์การตรวจรับงานของ Vendor ไว้ชัดเจนแล้วหรือยัง?
2. คุณเคยประสบปัญหา Vendor ส่งมอบงานล่าช้าหรือไม่ และได้มีการระบุค่าปรับ (Liquidated Damages) ไว้ในสัญญาหรือไม่?

---

### Context for later learning

เมื่อเราเรียนรู้ 10 Knowledge Areas ในรูปแบบ Predictive (Waterfall) ครบถ้วนแล้ว ในบทถัดไป **Lesson 15** เราจะไปเจาะลึกโลกของ **Agile Project Management** (Scrum & Kanban) เพื่อดูแนวทางการบริหารโครงการที่มีความยืดหยุ่นสูงในยุคดิจิทัลครับ!

## PM Decision Thinking

**[PMBOK 6]** Procurement Management ครอบคลุม plan, conduct และ control procurements. **[PMBOK 7]** stewardship และ risk thinking ทำให้ contract เป็นเครื่องมือจัดการ value, risk และ accountability.

| Field | Lesson 14 Application |
|---|---|
| Decision | งานนี้ควร make, buy, outsource บางส่วน หรือใช้ hybrid vendor model |
| Owner | PM วิเคราะห์ delivery need; procurement/legal ดู process/contract; sponsor อนุมัติ commercial decision |
| Inputs | scope certainty, requirements, acceptance criteria, market capability, risk, budget, timeline, IP/security needs |
| Options | fixed price, T&M with cap, cost reimbursable, managed service, framework agreement |
| Trade-offs | price certainty vs flexibility, vendor risk vs buyer control, speed vs contract clarity |
| Risk | TOR ไม่ชัด ทำให้ vendor ส่งงานตามสัญญาแต่ไม่ตรง value |
| Evidence | vendor proposal, evaluation criteria, contract terms, milestone acceptance, performance data |
| Next Action | ทำ procurement decision record และ contract control plan |

### PM Insight

Procurement ไม่ใช่แค่ซื้อของ แต่คือการกำหนดว่า risk และ accountability จะอยู่ที่ใคร. สัญญาที่ดีต้องช่วยให้ project control ได้ ไม่ใช่แค่ชนะการประกวดราคา.

## ERP Scenario

**[Teaching Scenario]** ERP Transformation ใช้ SI TechConsult สำหรับ 5 modules, data migration และ go-live support.

Procurement decision:

- Module configuration ที่ scope ชัดอาจใช้ fixed price พร้อม milestone acceptance
- Change requests และ uncertain integration อาจต้องมี rate card หรือ T&M with cap
- Milestone payment ควรผูกกับ accepted deliverables เช่น blueprint, SIT, UAT, cutover readiness
- Contract ต้องระบุ data migration quality, performance, support handover และ defect liability
- PM ต้อง control procurement ร่วมกับ procurement committee ไม่ใช่รอตรวจรับงวดสุดท้าย

## Hotel Booking Scenario

**[Teaching Scenario]** Hotel Booking Platform พึ่ง payment gateway, cloud service, outsource/mobile team และ hotel partner integrations.

Procurement decision:

- Payment gateway ต้องมี SLA, uptime, incident response และ fallback rights
- Agile development vendor อาจใช้ T&M with cap พร้อม sprint review และ acceptance criteria
- Cloud cost ต้องแยก project build cost กับ operating run-rate
- IP rights, source code access และ security/privacy clauses ต้องชัดก่อน launch

## Real Enterprise Example

**[Enterprise Practice]** Vendor dispute มักไม่ได้เริ่มตอน vendor ส่งงาน แต่เริ่มตอน TOR ไม่ระบุ performance, security, data quality หรือ acceptance criteria. PM ต้องช่วยทำให้ requirement เชิงบริหารกลายเป็น contract language ที่ตรวจรับได้.

## Common Mistakes

1. ปล่อยให้ TOR ไม่มี non-functional requirements
2. เลือก fixed price ทั้งที่ scope ยังไม่นิ่ง
3. จ่าย milestone ตามเวลา ไม่ใช่ accepted deliverables
4. ไม่กำหนด change order process
5. ปิด project โดยไม่ปิด procurement/contract obligations

## Common Misconceptions

| Misconception | Correction |
|---|---|
| Procurement เป็นงานฝ่ายจัดซื้อเท่านั้น | PM ต้องดู requirement, deliverable และ acceptance |
| Fixed price ปลอดภัยที่สุดเสมอ | Fixed price เสี่ยง conflict ถ้า scope ไม่ชัด |
| T&M คุมไม่ได้ | T&M with cap, cadence และ acceptance controls คุมได้ |
| Vendor รับ risk ทั้งหมดได้ | บาง risk ยังอยู่กับ buyer เช่น requirement clarity และ adoption |

## Interview Questions

### Definition

1. Fixed price, T&M และ cost reimbursable ต่างกันอย่างไร
2. Make-or-buy analysis คืออะไร

### Judgement

1. คุณจะเลือก fixed price เมื่อใด และจะหลีกเลี่ยงเมื่อใด
2. ถ้า vendor ส่งงานตรง contract แต่ไม่ตรง business need คุณจะจัดการอย่างไร

### Behavioral

1. เล่าครั้งหนึ่งที่คุณบริหาร vendor performance
2. คุณเคยทำ acceptance criteria ใน TOR อย่างไร

### Scenario

1. ใน ERP คุณจะกำหนด milestone payment ให้ TechConsult อย่างไร
2. ใน Hotel Booking คุณจะกำหนด SLA ของ payment gateway อย่างไร

## PM Dictionary

| Term | Meaning |
|---|---|
| Procurement Management | การจัดหาและบริหารสินค้าหรือบริการจากภายนอก |
| Make-or-Buy Analysis | การตัดสินใจทำเองหรือซื้อ/จ้างภายนอก |
| TOR/RFP | เอกสารกำหนดขอบเขตและเชิญเสนอราคา |
| Fixed Price | สัญญาราคาคงที่ เหมาะกับ scope ชัด |
| Time and Material | สัญญาคิดตามเวลา/ทรัพยากร มักใช้กับงานยืดหยุ่น |
| Cost Reimbursable | สัญญาจ่ายตามต้นทุนจริงบวก fee |
| SLA | Service Level Agreement หรือระดับบริการที่ตกลง |
| Acceptance Criteria | เกณฑ์ตรวจรับที่ vendor ต้องผ่าน |
| Procurement Closure | การปิดสัญญาและ obligations อย่างเป็นทางการ |

## Workshop

### Scenario

ERP ต้องทำสัญญากับ TechConsult. Hotel Booking ต้องเลือก payment gateway และ outsource mobile team.

### Task

ให้ผู้เรียนทำ procurement decision sheet 1 หน้า:

1. make-or-buy rationale
2. recommended contract type
3. acceptance criteria
4. milestone/payment controls
5. vendor risks และ response
6. procurement closure requirements

### Debrief

คำตอบที่ดีต้องผูก contract กับ deliverable, risk และ acceptance ไม่ใช่ดูราคาอย่างเดียว.

## Assessment

ดูแบบประเมินหลักที่ [Lesson 14 Assessment](./Lesson-14_3-Assessment.md). แบบประเมินควรวัด judgement เรื่อง contract type, vendor risk, acceptance criteria และ procurement control.

## Executive Summary

Procurement Management ทำให้การใช้ vendor เป็นระบบที่ควบคุม value และ risk ได้. PM ต้องมีส่วนกับ scope, TOR, contract type, acceptance และ vendor performance. สัญญาที่ชัดช่วยป้องกัน dispute และทำให้การตรวจรับเชื่อมกับผลส่งมอบจริง.

## Lesson Connection

Lesson 13 สอน risk response รวมถึง transfer. Lesson 14 แสดง procurement เป็นหนึ่งในกลไก transfer/control risk ผ่าน vendor และ contract. Lesson 15 จะต่อไปที่ Agile/Scrum/Kanban เพื่อบริหารงานที่มีความไม่แน่นอนสูงและต้องเรียนรู้เป็นรอบสั้น.

## AI Continuation Context

Future AI agents must keep procurement tied to PM decision, vendor risk and acceptance criteria. Use TechConsult ERP contract and Hotel Booking payment/development vendors as recurring procurement examples.

## Artifact Handoff

- **Output:** Procurement Plan, vendor evaluation and contract-control evidence.
- **Authority:** Procurement Authority/Sponsor approves commercially; PM connects delivery and acceptance.
- **Next use:** L15 uses contract constraints and acceptance evidence in iterative delivery.

---
lesson: 4
sequence: 4.2
title: 10 Project Management Knowledge Areas Overview
document_type: Lesson
difficulty: Foundation
estimated_study_time: 90
status: Active
validation_status: Validated
version: 1.0
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 01 — ทำไม Project Manager ต้องรู้ PMBOK
  - Lesson 02 — Project Management Overview
  - Lesson 03 — 5 Project Management Process Groups
related_lessons:
  - Lesson 03 — 5 Project Management Process Groups
  - Lesson 05 — Project Integration Management
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 04_2 — 10 Project Management Knowledge Areas Overview

## Beginner Safety

- **ควรรู้แล้ว:** Process Groups, lifecycle gate และ feedback loop จาก Lesson 03
- **ยังไม่ต้องรู้:** วิธีสร้าง WBS, EVM, contract หรือ risk analysis รายละเอียด
- **คำศัพท์ใหม่:** Knowledge Area, Integration, Cross-impact, Impact Owner, Approval Authority
- **Novice traps:** มอง Knowledge Areas เป็น department หรือ checklist แยกสิบชุด

## Opening Professional Question — ถ้าโครงการตรงเวลาและไม่เกินงบ แต่ผู้ใช้ไม่ยอมใช้ระบบ โครงการนี้บริหารดีแล้วหรือยัง?

ลองจินตนาการถึงเหตุการณ์ในองค์กร:

> ทีมโครงการสามารถพัฒนาระบบใหม่และเปิดใช้งานได้ตรงตามกำหนดวัน Go-live เป๊ะ และค่าใช้จ่ายทั้งหมดอยู่ภายใต้งบประมาณที่ได้รับอนุมัติ 100% แต่หลังจากผ่านไป 3 เดือน กลับพบว่าพนักงานปฏิเสธการใช้งานระบบใหม่ และแอบกลับไปใช้ไฟล์ Excel เดิมในการทำงาน เพราะระบบใหม่ใช้งานยากและไม่ตอบโจทย์กระบวนการทำงานจริง

ในมิติของ **Time (Schedule)** และ **Cost (Budget)** โครงการนี้สอบผ่านอย่างงดงาม  
แต่ในมิติของ **Stakeholder, Quality, Risk** และ **Business Value** โครงการนี้กลับล้มเหลวอย่างรุนแรง!

> **คำถามสำคัญคือ:** การบริหารโครงการให้ประสบความสำเร็จ อาศัยเพียงการติดตาม Schedule และ Budget เท่านั้นหรือไม่? ถ้าไม่ใช่ PM ต้องครอบคลุมองค์ความรู้ด้านใดบ้างเพื่อไม่ให้เกิดจุดโหว่ที่ทำลายโครงการ?

---

## Why This Matters — การบริหารแบบ "สายตามองสั้น" (Tunnel Vision)

จุดล้มเหลวที่ PM จำนวนมากมักตกหลุมพราง คือการโฟกัสเฉพาะเรื่องที่ตนเองถนัดหรือเรื่องที่ผู้บริหารตามจี้เป็นหลัก:

1. **โฟกัสเฉพาะ Triple Constraints (Scope, Schedule, Cost) แต่ลืมองค์ประกอบรอบข้าง:**
   * ละเลยการบริหารผู้มีส่วนได้ส่วนเสีย (Stakeholders) จนเกิดแรงต้าน
   * ละเลยการบริหารทรัพยากร (Resource) จนทีมงานเกิดภาวะ Burnout
   * ละเลยการสื่อสาร (Communications) จนเกิดความเข้าใจไม่ตรงกันทั้งองค์กร
2. **มององค์ความรู้แต่ละด้านแยกจากกันเป็นกล่องๆ (Silo Management):**
   * ปรับแก้ Scope โดยไม่คิดถึงผลกระทบต่อ Risk, Quality หรือ Resource
   * ตัดงบประมาณ (Cost) ลง โดยคิดว่าจะไม่กระทบต่อขอบเขตงาน (Scope) หรือคุณภาพ (Quality)
3. **ขาดศูนย์กลางในการเชื่อมโยงการตัดสินใจ (Lack of Integration):**
   * ไม่มีใครทำหน้าที่เป็น Integrator เพื่อประเมินภาพรวม ทำให้เกิดความขัดแย้งระหว่างทีมงานข้ามสายงาน

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. ระบุ 10 Knowledge Areas และบทบาทของแต่ละด้านในระดับ overview
2. แยก Process Groups ออกจาก Knowledge Areas
3. อธิบายว่า Integration Management เชื่อมผลกระทบข้ามด้านอย่างไร
4. วิเคราะห์ผลกระทบของ change หนึ่งข้อที่กระทบ scope, schedule, cost, quality, risk, resource, stakeholder, communication และ procurement
5. ใช้ ERP และ Hotel Booking scenarios เพื่ออ่าน project health แบบหลายมิติ

## 3. เหตุผลและที่มา: มิติการบริหาร 10 ด้านของการบริหารโครงการ

ทำไมมาตรฐาน PMBOK จึงต้องกำหนดองค์ความรู้ออกเป็น **10 Knowledge Areas**?

เพราะโครงการเป็นระบบที่มีความซับซ้อนหลายมิติ การบริหารให้เกิด Business Value ไม่ใช่เรื่องของโชคช่วย แต่เกิดจากการรับประกันว่า **"ทุกมิติที่จำเป็นได้รับการดูแลอย่างมีระบบ"**

- **Process Groups (Lesson 03):** บอกว่า *"เรากำลังบริหารในช่วงเวลาไหน"* (Initiating → Planning → Executing → Monitoring → Closing)
- **Knowledge Areas (Lesson 04):** บอกว่า *"เรากำลังบริหารในเรื่องอะไร"* (Scope, Schedule, Cost, Quality, Risk ฯลฯ)
- **Integration Management:** ทำหน้าที่เป็น *"กาวเชื่อม"* นำการตัดสินใจของทุกเรื่องมารวมกันเพื่อประโยชน์สูงสุดของโครงการ

---

## 4. Mental Model: ภาพรวมและ Matrix ของ 10 Knowledge Areas

เพื่อสร้างกรอบความคิดที่ชัดเจน ให้มองว่า **Knowledge Areas ไม่ใช่แผนกงาน 10 แผนก** แต่เป็น **"กล้อง 10 เลนส์"** ที่ PM ต้องใช้ส่องดูสุขภาพของโครงการอยู่เสมอ:

```text
               ┌─────────────────────────────────────────────────────────┐
               │              1. INTEGRATION MANAGEMENT                  │
               │            (ศูนย์กลางการเชื่อมโยงและการตัดสินใจ)             │
               └────────────────────────────┬────────────────────────────┘
                                            │
    ┌───────────────────────────────────────┼───────────────────────────────────────┐
    │                                       │                                       │
    ▼                                       ▼                                       ▼
[ Core Baseline Triangle ]             [ Quality & Risk Filter ]              [ Enablers & Stakeholders ]
• 6. Scope Management                  • 9. Risk Management                   • 2. Stakeholder Management
• 7. Schedule Management               • 10. Quality Management               • 3. Procurement Management
• 8. Cost Management                                                          • 4. Resource Management
                                                                              • 5. Communications Management
```

### Knowledge Area × Process Group Matrix:
เมื่อนำ 5 Process Groups มาตัดกับ 10 Knowledge Areas จะเกิดเป็น **ตารางเมทริกซ์กระบวนการบริหาร (Process Matrix)** ที่ระบุว่าในแต่ละช่วงเวลา PM ต้องทำกิจกรรมอะไรในมิติใดบ้าง โดยมี **Integration Management** เป็นตัวเชื่อมร้อยทุกมิติ

---

## 5. คำศัพท์และ Framework (ภาพรวม 10 Knowledge Areas ตาม Canonical Source)

อ้างอิงลำดับและนิยามจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

| ลำดับ | Knowledge Area | หน้าที่หลักและเป้าหมายการบริหาร (Core Focus) |
|---|---|---|
| **1** | **Project Integration Management** | ศูนย์กลางในการรวบรวม ตัดสินใจ และจัดทิศทางให้ทุกมิติเคลื่อนไปสู่เป้าหมายเดียวกัน |
| **2** | **Project Stakeholder Management** | ระบุ วิเคราะห์ และบริหารความคาดหวังของคนทุกกลุ่มที่มีส่วนได้ส่วนเสียกับโครงการ |
| **3** | **Project Procurement Management** | บริหารการจัดซื้อจัดจ้าง ผู้ขาย (Vendor) และสัญญาข้อตกลงภายนอกองค์กร |
| **4** | **Project Resource Management** | จัดสรร บริหารทีมงาน อุปกรณ์ เครื่องมือ และสถานที่ให้เพียงพอและมีประสิทธิภาพ |
| **5** | **Project Communications Management** | วางแผน สื่อสาร และกระจายข้อมูลข่าวสารให้ถูกคน ถูกเวลา และถูกช่องทาง |
| **6** | **Project Scope Management** | กำหนด รวบรวม และควบคุมขอบเขตงานให้ทำเฉพาะสิ่งที่จำเป็นเท่านั้น (No Scope Creep) |
| **7** | **Project Schedule Management** | วางแผน ประเมินเวลา และควบคุมระยะเวลาดำเนินงานให้ส่งมอบได้ทันตามกำหนด |
| **8** | **Project Cost Management** | ประมาณการ จัดทำงบประมาณ และควบคุมค่าใช้จ่ายให้อยู่ในงบประมาณที่ได้รับอนุมัติ |
| **9** | **Project Risk Management** | ระบุ ประเมิน และวางมาตรการรับมือกับความไม่แน่นอนทั้งเชิงบวก (Opportunity) และเชิงลบ (Threat) |
| **10** | **Project Quality Management** | กำหนดและควบคุมมาตรฐานเพื่อให้ผลงานตรงตามความต้องการและเงื่อนไขการตรวจรับ |

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (ผลกระทบข้าม Knowledge Areas)

ในโครงการ ERP หากฝ่ายธุรกิจขอเพิ่มรายงานวิเคราะห์ข้อมูลการขายด่วนก่อน Go-live (**Scope Change**):
- **Scope Impact:** เพิ่มงานพัฒนา Report 10 หน้า
- **Schedule Impact:** ต้องใช้เวลาเพิ่ม 2 สัปดาห์ กระทบต่อวัน Go-live เดิม (**Schedule**)
- **Cost Impact:** ต้องจ่ายเงินเพิ่มให้ Vendor พัฒนาโค้ด (**Procurement & Cost**)
- **Resource Impact:** ทีม Tester ต้องทำงานล่วงเวลาจนเกิดความเครียด (**Resource**)
- **Quality & Risk Impact:** หากเร่งทำโดยไม่ได้ทดสอบ UAT อาจเกิดข้อมูลผิดพลาดในการปิดบัญชี (**Quality & Risk**)
- **Stakeholder & Communication Impact:** ผู้บริหารฝ่ายการเงินไม่พอใจที่วัน Go-live เลื่อนออกไป (**Stakeholder & Communication**)

> **Integration Thinking:** PM ทำหน้าที่ประเมินผลกระทบข้ามทั้ง 10 มิตินี้ และนำข้อมูลเสนอ Change Control Board เพื่อตัดสินใจทางเลือกที่ดีที่สุด

### 🏨 Core Scenario B: Hotel Booking Digital Platform (ผลกระทบข้าม Knowledge Areas)

ในโครงการพัฒนาแอปจองโรงแรม หากพบปัญหาระบบ Payment Gateway ขัดข้องบ่อยครั้งในสัปดาห์ทดสอบ:
- **Quality & Risk:** ความผิดพลาดใน Payment Gateway เป็นความเสี่ยงสูงสุดต่อ Conversion และแบรนด์
- **Procurement & Resource:** PM ต้องเข้าไปเร่งรัดบริการจาก Vendor ผู้ให้บริการระบบชำระเงิน (**Procurement**) และจัดสรร Dev ฝ่าย Backend เข้าไปช่วยแก้ไขร่วมกัน (**Resource**)
- **Communication & Stakeholder:** PM สื่อสารสถานะความเสี่ยงให้ฝ่ายการตลาด (Marketing) รับทราบ เพื่อปรับตารางการยิงโฆษณาเปิดตัวแอปออกไปก่อน จนกว่าระบบชำระเงินจะเสถียร 100% (**Communication & Stakeholder**)

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"Knowledge Areas คือแผนกงาน 10 แผนกในองค์กร":**
   * *ความจริง:* Knowledge Areas คือ **มิติการมองและความรับผิดชอบของ PM** ไม่ใช่การตั้งแผนกขึ้นมา 10 แผนก
2. **"PM ต้องเป็นผู้เชี่ยวชาญเชิงลึกที่สุดในทุก Knowledge Area":**
   * *ความจริง:* PM ไม่จำเป็นต้องเป็นคนที่เขียนโค้ดเก่งที่สุด รู้นิติกรรมสัญญาดีที่สุด หรือทำบัญชีเก่งที่สุด แต่ PM ต้องเข้าใจหลักการและสามารถ **บูรณาการ (Integrate)** ความเชี่ยวชาญจากคนอื่นได้
3. **"Scope และ Schedule สำคัญกว่า Quality และ Risk เสมอ":**
   * *ความจริง:* การส่งมอบงานตรงเวลา แต่ได้ระบบที่มีบั๊กและไม่มีความเสถียร (Quality ล้มเหลว) จะส่งผลเสียต่อธุรกิจมากกว่าการขอปรับ Schedule อย่างมีเหตุผล
4. **"Communication คือการส่ง Status Report ประจำสัปดาห์เท่านั้น":**
   * *ความจริง:* การสื่อสารรวมถึงการรับฟัง การทำความเข้าใจอารมณ์ความรู้สึกของผู้มีส่วนได้ส่วนเสีย และการสร้างการรับรู้เพื่อให้เกิดการยอมรับการเปลี่ยนแปลง (Change Adoption)

---

## 8. PM Thinking & Decision Making

เมื่อเกิดเหตุการณ์เปลี่ยนแปลงในโครงการ ให้ PM ใช้ **Cross-Knowledge Impact Assessment**:

```text
เมื่อมีความเปลี่ยนแปลงหรือปัญหาเกิดขึ้นใน Knowledge Area ใดก็ตาม:

Step 1: Identify Primary Area -> ปัญหาเริ่มต้นเกิดขึ้นในมิติใด? (เช่น Scope เพิ่มขึ้น)
Step 2: Trace Baseline Impacts -> กระทบต่อ Triple Constraints ที่เหลืออย่างไร? (Schedule? Cost?)
Step 3: Trace People & Partner Impacts -> กระทบต่อคนและผู้ซื้อขายอย่างไร? (Stakeholder? Resource? Procurement?)
Step 4: Trace Risk & Quality Impacts -> เกิดความเสี่ยงใหม่หรือกระทบคุณภาพหรือไม่? (Risk? Quality?)
Step 5: Integrate Decision -> นำผลกระทบทั้งหมดมาประเมินร่วมกันใน Integration Management เพื่อตัดสินใจทางเลือกที่เหมาะสม
```

---

## Guided Reflection During Learning

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในการทำงานปัจจุบัน คุณมักจะให้ความสำคัญกับ Knowledge Area ใดมากที่สุด และมักมองข้าม Knowledge Area ใดไป?
2. คุณเคยเห็นโครงการที่ตรงเวลาและไม่เกินงบ แต่นับเป็นความล้มเหลวเพราะมองข้าม Stakeholder หรือ Quality หรือไม่?

---

## PM Decision Thinking

**[PMBOK 6]** Knowledge Areas ช่วยให้ PM ไม่ลืมมิติสำคัญของงานบริหารโครงการ. **[PMBOK 7]** Systems thinking และ value delivery ทำให้ PM ต้องดู dependency ข้ามด้าน ไม่ใช่แก้ปัญหาใน silo.

| Field | Lesson 04 Application |
|---|---|
| Decision | change หรือปัญหาหนึ่งข้อควรถูกประเมินข้าม Knowledge Areas ใดบ้าง |
| Owner | PM ทำ integrated impact assessment; sponsor/change authority ตัดสินเมื่อกระทบ baseline หรือ value |
| Inputs | requirement, baseline, vendor contract, resource capacity, stakeholder expectation, risk, quality criteria |
| Options | accept change, defer, split release, add resource, negotiate vendor, adjust scope, update risk response |
| Trade-offs | speed vs quality, scope value vs schedule risk, cost saving vs adoption, vendor dependency vs internal control |
| Risk | ตัดสินจาก schedule/cost อย่างเดียวจนทำลาย quality, stakeholder trust หรือ business value |
| Evidence | impact map, decision log, updated risk register, acceptance criteria, stakeholder readiness |
| Next Action | ทำ one-page cross-knowledge impact map ก่อนเสนอ decision |

### PM Insight

Knowledge Areas ไม่ได้มีไว้ให้ PM ท่องชื่อครบ 10 ข้อ แต่มีไว้เตือนว่า “ทุกการตัดสินใจมีแรงกระเพื่อม”. ถ้าเพิ่ม scope โดยไม่ดู quality, risk, resource และ stakeholder โครงการอาจดู green ใน dashboard แต่แดงในโลกจริง.

## ERP Scenario

**[Teaching Scenario]** ERP Transformation มี working delivery budget 45 ล้านบาท, scope 5 modules, data migration จาก 6 legacy systems, 80 key users และ go-live target ก่อน 1 ตุลาคม.

เมื่อฝ่าย sales ขอเพิ่มรายงาน margin analysis ก่อน go-live PM ต้องดูผลกระทบข้าม Knowledge Areas:

- Scope: report เพิ่มเข้า scope หรือเป็น post-go-live enhancement
- Schedule: build/test เพิ่มกระทบ go-live หรือไม่
- Cost/Procurement: TechConsult ต้องคิดค่าเปลี่ยนแปลงหรือใช้ effort ในสัญญาเดิม
- Resource: key users และ testers มี capacity พอหรือไม่
- Quality: report ใช้ data ที่ migrate แล้วถูกต้องหรือยัง
- Risk: หากเร่งทำอาจเพิ่ม defect และ adoption issue
- Stakeholder/Communication: sales ต้องเข้าใจ trade-off กับ finance/warehouse priorities
- Integration: PM รวม impact ทั้งหมดเป็น decision option ให้ steering committee

## Hotel Booking Scenario

**[Teaching Scenario]** Hotel Booking Platform มีเป้าหมายเพิ่ม direct booking จาก 10% เป็น 35% หลัง 18 เดือน ภายใต้งบ 12 ล้านบาทและ timeline 8 เดือน.

เมื่อ marketing ขอเพิ่ม corporate booking feature ก่อน launch:

- Scope: feature ใหม่มี value แต่เพิ่ม complexity
- Schedule: launch อาจเลื่อนก่อน high season
- Cost: cloud, payment, QA และ vendor effort อาจเพิ่ม
- Quality/Risk: checkout flow และ inventory accuracy เสี่ยงเสียหาย
- Resource: team อาจต้องหยุดแก้ payment failure เพื่อทำ feature ใหม่
- Stakeholder: marketing, hotel partners, operations และ finance อาจมี priority ต่างกัน
- Communication: sponsor ต้องเห็นว่า direct booking outcome อาจดีขึ้นหรือแย่ลง
- Integration: PM ต้องเสนอ release option เช่น defer feature, pilot เฉพาะ corporate accounts หรือ split phase

## Real Enterprise Example

**[Professional Opinion]** โครงการจำนวนมากไม่ล้มเพราะ PM ไม่รู้ schedule แต่ล้มเพราะไม่มีใครมอง dependency รอบ schedule. ตัวอย่างเช่น vendor ส่งของทัน แต่ user training ไม่พร้อม, data quality ไม่ผ่าน, support team ไม่มี owner และ sponsor ยังบอกว่า project green เพราะ timeline ไม่หลุด. Lesson 04 ต้องทำให้ผู้เรียนอ่าน project health เป็นระบบ ไม่ใช่อ่านแค่วันที่และงบ.

## Common Mistakes

1. จำชื่อ Knowledge Areas ได้ แต่ไม่ใช้วิเคราะห์ dependency
2. คิดว่า Integration Management คือรวบรวมเอกสาร
3. ให้ scope/schedule/cost กลบ quality, risk และ stakeholder adoption
4. ปล่อยให้แต่ละทีมวิเคราะห์ impact เฉพาะมุมตัวเอง
5. ไม่แยก working budget, reserve และ funding envelope ในการตัดสินใจ

## Common Misconceptions

| Misconception | Correction |
|---|---|
| Knowledge Areas คือ department | เป็นมุมมองบริหาร ไม่ใช่ผังองค์กร |
| PM ต้องเก่งที่สุดทุกด้าน | PM ต้อง integrate experts และ decision evidence |
| Scope change กระทบแค่ scope | มักกระทบ schedule, cost, quality, risk, resource และ stakeholder |
| Communication คือส่ง report | Communication คือทำให้ผู้เกี่ยวข้องเข้าใจ decision และ trade-off |
| Risk เป็นงานของ risk manager | PM ต้องทำให้ risk ถูกเห็น ถูก owner และถูกตอบสนอง |

## Interview Questions

### Definition

1. Knowledge Area คืออะไร และต่างจาก Process Group อย่างไร
2. ทำไม Integration Management ถึงเป็นแกนกลางของ 10 Knowledge Areas

### Judgement

1. ถ้ามี scope change ก่อน go-live คุณจะทำ impact assessment ครอบคลุมด้านใดบ้าง
2. ถ้า project ตรงเวลาแต่ adoption ต่ำ คุณจะอ่าน Knowledge Areas ใดเป็นพิเศษ

### Behavioral

1. เล่าครั้งหนึ่งที่คุณต้องเชื่อมการตัดสินใจระหว่างทีม business, technology และ vendor
2. คุณเคยทำให้ stakeholder เห็น trade-off ข้าม scope, schedule, cost และ quality อย่างไร

### Scenario

1. ใน ERP หาก data migration ไม่พร้อมแต่ schedule ยัง green คุณจะ escalate อย่างไร
2. ใน Hotel Booking หาก payment failure สูงแต่ marketing ต้องการ launch คุณจะใช้ Knowledge Areas ใดในการอธิบาย decision

## PM Dictionary

| Term | Meaning |
|---|---|
| Knowledge Area | กลุ่มองค์ความรู้หรือมุมมองบริหารที่ PM ต้องดูแล |
| Integration Management | การเชื่อม decision, baseline, change และผลกระทบทุกด้านเข้าด้วยกัน |
| Stakeholder Management | การระบุ วิเคราะห์ และดูแลผู้มีส่วนได้ส่วนเสีย |
| Procurement Management | การบริหาร vendor, contract และการจัดซื้อจัดจ้าง |
| Resource Management | การบริหารคน ทีม เครื่องมือ และ capacity |
| Communications Management | การวางแผนและส่งข้อมูลให้ถูกคน ถูกเวลา ถูกความหมาย |
| Scope Management | การกำหนดและควบคุมสิ่งที่จะส่งมอบ |
| Schedule Management | การวางและควบคุมเวลา |
| Cost Management | การประมาณการ งบประมาณ และควบคุมต้นทุน |
| Risk Management | การจัดการความไม่แน่นอนที่กระทบเป้าหมาย |
| Quality Management | การกำหนดและควบคุมมาตรฐานของผลส่งมอบ |

## Workshop

### Scenario

Hotel Booking ต้องการเพิ่ม corporate booking ก่อน high season ขณะเดียวกัน payment failure ยังสูง. ERP ต้องการเพิ่ม sales margin report ก่อน go-live แต่ data migration ยังไม่ stable.

### Task

ให้ผู้เรียนทำ cross-knowledge impact map 1 หน้า โดยต้องครอบคลุม:

1. primary Knowledge Area ที่เป็นจุดเริ่มปัญหา
2. downstream impact อย่างน้อย 6 Knowledge Areas
3. evidence ที่ยังขาด
4. options และ trade-offs
5. decision owner และ escalation path
6. recommendation ที่ไม่ใช้ schedule/cost เป็นเกณฑ์เดียว

### Debrief

คำตอบที่ดีต้องเห็น dependency และระบุ decision ที่ทำได้จริง ไม่ใช่เขียนครบ 10 ชื่อโดยไม่มี trade-off.

### Artifact Learning Path

- **Do:** สร้าง [PM Coverage and Cross-impact Map](learner/Artifact-Template.md)
- **Checkpoint:** ทำ [Beginner Checkpoint](learner/Beginner-Checkpoint.md)
- **Review หลังส่งคำตอบ:** ใช้ [Thinking Walkthrough](instructor/Thinking-Walkthrough.md), [Completed Example](instructor/Completed-Example.md) และ [Rubric](instructor/Scoring-Rubric.md)

## Assessment

ดูแบบประเมินหลักที่ [Lesson 04 Assessment](./Lesson-04_3-Assessment.md). Assessment ต้องวัดทั้งการระบุ 10 Knowledge Areas และการตัดสินใจจาก scenario ที่มีผลกระทบข้ามด้าน โดย judgement-based questions ควรมีน้ำหนักเกินครึ่ง.

## Executive Summary

10 Knowledge Areas คือแผนที่ความรับผิดชอบของ PM. Process Groups บอกว่า PM กำลังบริหารช่วงไหน ส่วน Knowledge Areas บอกว่า PM กำลังบริหารเรื่องอะไร. Integration Management เป็นแกนที่รวมผลกระทบจากทุกด้านเพื่อให้ decision ไม่ติด silo และยังผูกกับ value จริง.

## Lesson Connection

Lesson 03 ทำให้ผู้เรียนเข้าใจ flow ของ 5 Process Groups. Lesson 04 เพิ่มมิติ 10 Knowledge Areas ให้เห็นว่าในแต่ละช่วง PM ต้องบริหารเรื่องใดบ้าง. Lesson 05 จะเจาะ Project Integration Management ซึ่งเป็นกลไกเชื่อม charter, plan, execution, control, change และ closing.

## AI Continuation Context

Future AI agents must keep Lesson 04 at overview depth. Do not expand into detailed processes for each Knowledge Area here. Preserve the course ordering from the canonical source and use Integration Management as the bridge to Lesson 05. Keep ERP Working Budget 45 ล้านบาท separate from Total Funding Envelope 60 ล้านบาท.

## Artifact Handoff

- **Input:** Lifecycle and Process Group Map
- **Output:** PM Coverage and Cross-impact Map
- **Governance:** PM สร้างและเป็น Owner; Knowledge-area Owners/PMO ตรวจ; Change Authority/Sponsor อนุมัติ
- **Minimum acceptance:** `Usable`
- **Next use:** Lesson 05 ใช้ dependencies และ decision owners สร้าง Charter, Governance และ Change Decision Record

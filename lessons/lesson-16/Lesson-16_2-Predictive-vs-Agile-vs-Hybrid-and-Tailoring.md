---
lesson: 16
sequence: 16.2
title: Predictive vs Agile vs Hybrid and Tailoring
document_type: Lesson
level: Core
status: Draft
validation_status: Pending Final Repository Validation
version: 1.0
last_updated: 2026-07-22
prerequisite:
  - Lesson 15 — Agile Project Management Frameworks (Scrum and Kanban)
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 16_2 — Predictive vs Agile vs Hybrid and Tailoring

## Opening Professional Question — ถ้าสูตรสำเร็จเดียวไม่ได้ผลกับทุกโครงการ แล้ว PM จะเลือกระหว่าง Predictive, Agile หรือ Hybrid อย่างไรให้เหมาะกับงานจริง?

ลองพิจารณาคำถามสำคัญชี้ชะตาโครงการ:

> องค์กรแห่งหนึ่งประกาศนโยบายบังคับว่า *"นับจากนี้ไป ทุกโครงการในบริษัทจะต้องใช้ Agile 100% ทั้งหมด"* แต่เมื่อทีมนำไปใช้กับโครงการสร้างโรงงานและติดตั้งเครื่องจักรขนาดใหญ่ ผลลัพธ์กลับกลายเป็นความสับสน งบประมาณบานปลาย และเกิดความเสี่ยงด้านความปลอดภัย!

เหตุใดกรอบการทำงานที่ดีที่สุดในโครงการหนึ่ง จึงกลายเป็นสิ่งที่สร้างความล้มเหลวในอีกโครงการหนึ่ง?

> **คำถามสำคัญคือ:** ในฐานะ Project Manager มืออาชีพ เราจะประเมินบริบทของโครงการอย่างไร เพื่อเลือก ปรับแต่ง (Tailor) และผสมผสานแนวทางบริหารจัดการ (Waterfall vs Agile vs Hybrid) ให้ตอบโจทย์องค์กรได้อย่างแท้จริง?

---

## Why This Matters — สงครามทางความคิด (Methodology Dogma) และการสับสนเรื่อง Tailoring

จุดล้มเหลวในการเลือกระบบบริหารโครงการ ได้แก่:

1. **การยึดติดในลัทธิเครื่องมือ (Methodology Dogma):**
   * ทะเลาะกันว่า Predictive ดีกว่า หรือ Agile ดีกว่า โดยไม่เคยพิจารณาธรรมชาติของงาน ความเสี่ยง และบริบทขององค์กร
2. **การเข้าใจผิดว่าการ Tailoring คือการตัดกระบวนการตามใจชอบ:**
   * ตัดกระบวนการที่ไม่อยากทำออก แล้วอ้างว่าเป็นการ "Tailor" จนเกิดจุดโหว่ในการควบคุมความเสี่ยงและการกำกับดูแล (Governance)
3. **การทำ Hybrid แบบมั่วซั่ว (Messy Hybrid):**
   * นำส่วนที่แย่ที่สุดของ Waterfall (ความล่าช้า เอกสารเยอะ) มารวมกับส่วนที่แย่ที่สุดของ Agile (ไม่มีเกณฑ์เสร็จ ขาดการวางแผน) จนกลายเป็นความล้มเหลวคูณสอง

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. เปรียบเทียบ predictive, agile และ hybrid delivery approaches
2. ใช้ tailoring factors เพื่อเลือก approach ตาม uncertainty, governance, risk และ product type
3. แยก tailoring ที่มีเหตุผลออกจากการตัด process ตามใจ
4. ออกแบบ hybrid boundary ระหว่าง governance, contract, delivery cadence และ feedback
5. ใช้ ERP และ Hotel Booking scenarios เพื่อสรุป approach recommendation แบบมืออาชีพ

## 3. เหตุผลและที่มา: ไม่มีเครื่องมือใดที่เหมาะกับทุกสถานการณ์ (No Silver Bullet)

เหตุใดมาตรฐาน PMBOK ยุคใหม่จึงเน้นย้ำเรื่อง **"Tailoring & Delivery Approaches"**?

เพราะโครงการในโลกจริงมีสเปกตรัม (Spectrum) ความไม่แน่นอนที่แตกต่างกัน ตั้งแต่โครงการที่มีข้อกำหนดชัดเจน 100% ไปจนถึงโครงการนวัตกรรมที่เต็มไปด้วยสมมติฐาน

> **Core Rationale:**  
> **ไม่มีวิธีบริหารโครงการแบบใดที่ดีที่สุด มีเพียงวิธีที่เหมาะสมที่สุดสำหรับบริบทนั้น ๆ (Context-driven Selection) หน้าที่ของ PM คือการใช้ดุลยพินิจปรับแต่ง (Tailoring) กระบวนการ เครื่องมือ และเอกสาร ให้พอดีกับระดับความเสี่ยงและความซับซ้อนของโครงการ**

---

## 4. Mental Model: สเปกตรัมการส่งมอบ (Delivery Approach Spectrum)

เพื่อสร้างกรอบความคิดที่ถูกต้อง ให้มองแนวทางการส่งมอบงานเป็น **สเปกตรัมความยืดหยุ่น (Spectrum of Flexibility)**:

```text
[ Predictive / Waterfall ] ───────────────► [ Hybrid Approach ] ───────────────► [ Agile / Adaptive ]
• Requirements ชัดเจนตั้งแต่แรก            • ผสมผสานตามความเหมาะสม               • Requirements เปลี่ยนแปลงสูง
• ความเสี่ยงเรื่องความปลอดภัยสูง             • เช่น วางแผนภาพรวมแบบ Predictive      • เน้นส่งมอบเนื้องานเร็ว (Speed)
• การเปลี่ยนแปลงมีราคาแพง                 แต่พัฒนาซอฟต์แวร์ย่อยแบบ Agile        • เรียนรู้และปรับตัวต่อเนื่อง
```

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

### 5.1 ตารางเปรียบเทียบ Predictive vs Agile vs Hybrid

| มิติ (Dimension) | Predictive (Waterfall) | Hybrid | Agile (Adaptive) |
|---|---|---|---|
| **ข้อกำหนด (Requirements)** | ชัดเจน วางแผนล่วงหน้า 100% | ชัดเจนบางส่วน ปรับเปลี่ยนได้ | ไม่แน่นอน เปลี่ยนแปลงสูง |
| **การส่งมอบ (Delivery)** | ส่งมอบครั้งเดียวตอนจบโครงการ | ส่งมอบเป็นระยะตามเฟส | ส่งมอบถี่ ๆ เป็น Increment |
| **การบริหารความเสี่ยง** | วิเคราะห์และป้องกันล่วงหน้า | ผสมผสานมาตรการป้องกันและการปรับตัว | ปรับตัวตาม Feedback ทันที |
| **บทบาทลูกค้า/ผู้ใช้** | มีส่วนร่วมช่วงเริ่มและตรวจรับ | มีส่วนร่วมในจุด Milestone สำคัญ | มีส่วนร่วมสม่ำเสมอตลอดโครงการ |
| **การวัดความสำเร็จ** | ทำตามแผน (Scope/Schedule/Cost) | บรรลุ Milestone & Value | ส่งมอบ Business Value & Outcome |

### 5.2 ปัจจัยการปรับแต่ง (Tailoring Factors Matrix)
เมื่อ PM ต้องเลือกระดับการ Tailor ให้พิจารณา 4 ปัจจัยหลัก:
1. **Product/Deliverable Characteristics:** ผลิตภัณฑ์เป็นระบบกายภาพ หรือซอฟต์แวร์ดิจิทัล?
2. **Project Team Factors:** ทีมงานมีทักษะ ทัศนคติ และความคุ้นเคยกับ Agile ระดับใด?
3. **Organizational Governance:** องค์กรต้องการเอกสารอนุมัติงบและข้อบังคับกฎหมายเข้มงวดเพียงใด?
4. **Market & Environmental Volatility:** ตลาดและความต้องการเปลี่ยนแปลงรวดเร็วแค่ไหน?

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (Hybrid Approach)

- **การประยุกต์ใช้ Hybrid ในโครงการใหญ่ระดับ Enterprise:**
  * **Predictive Governance:** ใช้ Predictive ในการวางแผนภาพรวม (Master Schedule), การบริหารงบประมาณ, การคัดเลือก Vendor (Procurement), และการทำ Data Migration ซึ่งต้องการความถูกต้อง 100%
  * **Agile Execution:** ใช้ Agile/Scrum ในช่วงการคอนฟิกระบบและการพัฒนาโค้ดปรับแต่ง (Customization) เพื่อให้ผู้ใช้ได้ทดลองเล่นและป้อน Feedback ได้เร็วขึ้นก่อนวัน Go-live

### 🏨 Core Scenario B: Hotel Booking Digital Platform (Hybrid to Agile Selection)

- **การประยุกต์ใช้ Hybrid ในโครงการ Digital Product:**
  * **Agile Product Development:** พัฒนา Mobile App และ Web App ด้วย Agile/Scrum สลับการปล่อยเวอร์ชันย่อยทุก 2 สัปดาห์
  * **Predictive Integration:** ใช้แผนการทำงานแบบ Predictive กับการเชื่อมต่อระบบ Payment Gateway และการทำสัญญาจัดซื้อจัดจ้างกับธนาคารและ Partner โรงแรม ซึ่งมีกำหนดการและข้อตกลงที่แน่นอน

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"Agile คืออนาคต และ Waterfall เป็นสิ่งที่ล้าสมัยแล้ว":**
   * *ความจริง:* โครงสร้างพื้นฐาน งานวิศวกรรม หรือโครงการที่มีความเสี่ยงความปลอดภัยสูง ยังคงต้องพึ่งพาแนวคิดแบบ Predictive การเลือกวิธีขึ้นอยู่กับความเหมาะสมของงาน ไม่ใช่เทรนด์
2. **"การทำ Hybrid คือการไม่ต้องปฏิบัติตามมาตรฐานใดเลย":**
   * *ความจริง:* Hybrid ที่ดีต้องมีสถาปัตยกรรมกระบวนการที่ชัดเจน (Clear Governance Architecture) ไม่ใช่การปล่อยปละละเลยโดยอ้างคำว่า Hybrid
3. **"กระบวนการ PMBOK ห้ามแก้ไขหรือตัดออก":**
   * *ความจริง:* มาตรฐาน PMBOK ออกแบบมาเพื่อให้ถูก Tailor เสมอ ไม่มีโครงการใดในโลกที่ใช้กระบวนการทั้ง 49 กระบวนการอย่างเข้มข้นเท่ากันทั้งหมด

---

## 8. PM Thinking & Decision Making (The Ultimate PM Mastery Framework)

เมื่อ PM ต้องสรุปแนวทางบริหารโครงการ ให้ใช้ **Tailoring Decision Steps**:

```text
Step 1: Analyze Uncertainty & Complexity ->
        - ความต้องการนิ่งแค่ไหน? เทคโนโลยีคุ้นเคยแค่ไหน?
        - High Uncertainty -> เอนเอียงไปทาง Agile
        - Low Uncertainty -> เอนเอียงไปทาง Predictive

Step 2: Define Hybrid Boundaries ->
        - ส่วนใดต้องล็อคเกณฑ์ Governance / Contract? -> ใช้ Predictive Controls
        - ส่วนใดต้องการ Speed-to-Market & Iteration? -> ใช้ Agile Sprints

Step 3: Document Tailoring Rationale -> บันทึกเหตุผลการปรับลด/เพิ่มกระบวนการไว้ใน Project Management Plan
Step 4: Focus on Business Value -> ทบทวนเสมอว่า ไม่ว่าจะเลือกแนวทางใด เป้าหมายสูงสุดคือการส่งมอบ Outcome & Business Value ให้องค์กร!
```

---

## 📝 9. Summary & Final Course Conclusion (ปัจฉิมบท PMBOK Masterclass)

ยินดีด้วยครับ! คุณได้เดินทางผ่านหลักสูตร **PMBOK Masterclass** ทั้ง 16 บทเรียนเรียบร้อยแล้ว สรุปหัวใจสำคัญของวิชาชีพ Project Management ได้ดังนี้:

1. **PM Thinking over Process:** การเป็น PM มืออาชีพ ไม่ใช่การท่องจำนิยาม แต่คือการเข้าใจเหตุผล คิดเชื่อมโยง และใช้ดุลยพินิจบริหารการตัดสินใจ
2. **Value Chain Orientation:** โครงการไม่ได้สำเร็จเพียงเพราะส่งมอบ Output แต่สำเร็จเมื่อสิ่งที่ส่งมอบเกิด **Outcome, Benefit และ Business Value** ที่แท้จริง
3. **Integrator Role:** PM คือ System Integrator ที่รักษาสมดุลของข้อจำกัด (Scope, Schedule, Cost, Quality, Risk, People, Procurement) เพื่อนำพาองค์กรไปสู่อนาคตที่ดีกว่า

ขอให้คุณนำทักษะ กรอบความคิด และเครื่องมือทั้งหมดจากหลักสูตรนี้ ไปประยุกต์ใช้ในการขับเคลื่อนโครงการจริงให้ประสบความสำเร็จอย่างยั่งยืนครับ!

## PM Decision Thinking

**[PMBOK 6]** predictive planning, baselines และ process discipline ยังสำคัญเมื่อ scope ชัดและ governance เข้ม. **[PMBOK 7]** tailoring, value delivery และ adaptability ช่วยให้ PM เลือกวิธีให้พอดีกับบริบท.

| Field | Lesson 16 Application |
|---|---|
| Decision | โครงการนี้ควรใช้ predictive, agile หรือ hybrid approach และต้อง tailor อะไร |
| Owner | PM เสนอ tailoring rationale; sponsor/governance body อนุมัติ approach เมื่อกระทบ control/risk |
| Inputs | requirement uncertainty, technical uncertainty, compliance, contract, stakeholder access, team maturity, release risk |
| Options | predictive, agile, hybrid, phased rollout, pilot, dual-track discovery/delivery |
| Trade-offs | predictability vs adaptability, documentation vs speed, governance vs learning, contract control vs collaboration |
| Risk | เลือก approach ตามแฟชั่นหรือ ideology แทนบริบทจริง |
| Evidence | tailoring rationale, delivery model, governance map, cadence, feedback loop, risk controls |
| Next Action | บันทึก delivery approach decision ใน project management plan |

### PM Insight

PM มืออาชีพไม่ถามว่า Waterfall หรือ Agile ใครชนะ แต่ถามว่า “ส่วนใดของงานต้องการ certainty และส่วนใดต้องการ learning”. Tailoring ที่ดีเพิ่มความเหมาะสม; tailoring ที่แย่ลดการควบคุมโดยไม่มีเหตุผล.

## ERP Scenario

**[Scenario]** ERP Transformation มี 5 modules, TechConsult, data migration, 80 key users, working budget 45 ล้านบาท และ go-live target ก่อน 1 ตุลาคม.

Recommended approach: Hybrid.

- Predictive controls: charter, scope baseline, budget, procurement, data migration, cutover, go-live governance
- Agile practices: prototype reports, iterative training feedback, Kanban for SIT defects/data cleansing, short-cycle UAT issue resolution
- Tailoring rationale: ERP ต้องการ control สูงเพราะ integration และ go-live risk แต่ยังต้องเรียนรู้จาก users เพื่อ adoption
- Governance boundary: change ที่กระทบ baseline เข้า CCB; backlog/defect reprioritization ใน workstream ทำได้ใน cadence ที่ตกลง

## Hotel Booking Scenario

**[Scenario]** Hotel Booking Platform มีเป้าหมาย direct booking 35% หลัง 18 เดือน และต้องเรียนรู้จาก user behavior, conversion, payment reliability และ partner adoption.

Recommended approach: Agile with selective predictive controls.

- Agile controls: Scrum สำหรับ feature development, Kanban สำหรับ support/incident, continuous analytics feedback
- Predictive controls: vendor contract, payment integration milestones, security/privacy compliance, launch readiness gates
- Tailoring rationale: product value ต้องเรียนรู้เป็นรอบ แต่ payment/security/compliance ต้องมี gate ชัด
- Governance boundary: release decision ใช้ product metrics + quality gates + sponsor risk tolerance

## Real Enterprise Example

**[Instructor Interpretation]** องค์กรที่บังคับทุก project ให้ Agile 100% หรือ Waterfall 100% กำลังละเลยธรรมชาติของงาน. การสร้างโรงงาน ระบบบัญชี ERP และ mobile product มี uncertainty, compliance และ feedback cadence ต่างกัน. Approach ที่ดีต้องอธิบายเหตุผลได้ ไม่ใช่เป็นคำสั่งจาก trend.

## Common Mistakes

1. เลือก approach ตามแฟชั่นหรือคำสั่งองค์กรโดยไม่วิเคราะห์บริบท
2. ใช้คำว่า hybrid เพื่อปิดบัง process ที่ไม่ชัด
3. ตัด governance ที่จำเป็นแล้วเรียกว่า tailoring
4. บังคับ Scrum กับงาน flow/support ที่เหมาะกับ Kanban
5. ใช้ predictive กับ product discovery ที่ requirement ยังไม่รู้จริง

## Common Misconceptions

| Misconception | Correction |
|---|---|
| Agile ดีกว่า Predictive เสมอ | ขึ้นกับ uncertainty, risk และ governance |
| Predictive ล้าสมัย | ยังเหมาะกับงานที่ scope/contract/compliance ชัด |
| Hybrid คือทำอะไรก็ได้ | Hybrid ต้องมี boundary และ decision rights |
| Tailoring คือตัดเอกสาร | Tailoring คือปรับ process ให้พอดีกับ risk/value |

## Interview Questions

### Definition

1. Predictive, Agile และ Hybrid ต่างกันอย่างไร
2. Tailoring คืออะไร และไม่ใช่อะไร

### Judgement

1. คุณจะเลือก hybrid approach เมื่อใด
2. ถ้าองค์กรบังคับใช้ Agile กับงาน compliance สูง คุณจะเสนออย่างไร

### Behavioral

1. เล่าครั้งหนึ่งที่คุณปรับวิธีบริหารโครงการให้เหมาะกับบริบท
2. คุณเคยอธิบาย tailoring rationale ต่อ sponsor อย่างไร

### Scenario

1. ใน ERP คุณจะกำหนดส่วน predictive และ agile อย่างไร
2. ใน Hotel Booking คุณจะใช้ governance gate ใดแม้ทีมทำ Agile

## PM Dictionary

| Term | Meaning |
|---|---|
| Predictive | approach ที่วางแผนล่วงหน้าและควบคุม baseline ชัด |
| Agile/Adaptive | approach ที่ส่งมอบเป็นรอบและปรับจาก feedback |
| Hybrid | การผสม approach โดยมี boundary และ rationale |
| Tailoring | การปรับ process/tool/artifact ให้เหมาะกับบริบทและ risk |
| Governance | กติกา decision, approval และ control ของ project |
| Delivery Cadence | จังหวะการส่งมอบงาน |
| Feedback Loop | วงจรรับข้อมูลจริงเพื่อปรับแผนหรือ backlog |
| Risk Tolerance | ระดับความเสี่ยงที่องค์กรยอมรับได้ |

## Workshop

### Scenario

เลือก delivery approach สำหรับ ERP Transformation และ Hotel Booking Platform.

### Task

ให้ผู้เรียนทำ tailoring recommendation 1 หน้า:

1. uncertainty และ governance profile
2. recommended approach
3. predictive controls ที่ต้องมี
4. agile practices ที่เหมาะ
5. hybrid boundary และ decision rights
6. risks หากเลือก approach ผิด

### Debrief

คำตอบที่ดีต้องอธิบายเหตุผลและ boundary ไม่ใช่เลือกจาก preference.

## Assessment

ดูแบบประเมินหลักที่ [Lesson 16 Assessment](./Lesson-16_3-Assessment.md). แบบประเมินควรวัด judgement เรื่อง approach selection, tailoring rationale และ hybrid governance boundary.

## Executive Summary

Predictive, Agile และ Hybrid เป็นเครื่องมือ ไม่ใช่ศาสนา. PM มืออาชีพเลือก approach จาก uncertainty, governance, risk, product type, team maturity และ value feedback. Tailoring ที่ดีทำให้ process พอดีกับงานและยังรักษา control ที่จำเป็น.

## Lesson Connection

Lesson 15 สอน Agile/Scrum/Kanban. Lesson 16 รวมทั้งหลักสูตรกลับมาเป็น PM decision framework: เข้าใจ value, process, Knowledge Areas, people, risk, vendor, agile และ tailoring เพื่อเลือกวิธีที่เหมาะกับงานจริง.

## AI Continuation Context

Future AI agents must preserve Lesson 16 as the course capstone. Do not present a single best methodology. Use ERP as hybrid with predictive governance and Hotel Booking as agile product delivery with selective predictive controls.

---
lesson: 12
sequence: 12.2
title: Project Communications Management
document_type: Lesson
difficulty: Core
estimated_study_time: 75
status: Active
validation_status: Validated
last_reviewed: 2026-07-22
intended_learner_level: Beginner PM
prerequisite:
  - Lesson 11 — Project Resource Management
related_lessons:
  - Lesson 13 — Project Risk Management
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 12_2 — Project Communications Management

## Beginner Safety

- **ควรรู้แล้ว:** L11 RACI; **คำศัพท์ใหม่:** cadence, status, decision brief.
- **Novice trap:** ส่งข้อมูลไม่ได้เท่ากับผู้รับเข้าใจหรือตัดสินใจได้.

## Opening Professional Question — ถ้า PM ส่งรายงานความก้าวหน้าทางอีเมลทุกสัปดาห์ แต่ผู้บริหารกลับบอกว่า "ไม่เคยรู้เรื่องปัญหานี้มาก่อนเลย" สื่อสารผิดพลาดที่ใคร?

ลองพิจารณาความล้มเหลวในการสื่อสารที่เกิดขึ้นบ่อยครั้ง:

> PM ส่งรายงานประจำสัปดาห์ความยาว 20 หน้าทางอีเมลให้ผู้บริหารทุกคนตามตารางเวลาเป๊ะ แต่น้อยคนนักที่จะเปิดอ่าน และเมื่อเกิดปัญหาวิกฤตจนต้องเลื่อน Go-live ผู้บริหารระดับสูงกลับต่อว่า PM ว่า *"ทำไมไม่เคยรายงานเรื่องนี้ให้ทราบเลย!"* ขณะที่ PM ก็สวนกลับว่า *"ส่งรายงานให้ทุกสัปดาห์แล้วครับ อยู่ในภาคผนวกหน้า 18"*

ในมุมของ PM การส่งอีเมลคือการ "สื่อสารเสร็จสิ้นแล้ว" (Broadcast Complete)  
แต่ในมุมของผู้รับ การได้รับเอกสารที่อ่านไม่รู้เรื่องหรือไม่ตรงประเด็น ถือว่า **"ยังไม่ได้เกิดการสื่อสารขึ้นจริง"!**

> **คำถามสำคัญคือ:** การบริหารการสื่อสาร (Communications Management) คือการ "ส่งข้อมูลออกไป" (Sending Data) หรือการทำให้มั่นใจว่า "เกิดความเข้าใจที่ถูกต้องตรงกัน" (Ensuring Shared Understanding)?

---

## Why This Matters — การสื่อสารแบบท่วมท้นและการเลือกใช้สื่อผิดประเภท

ปัญหาหลักที่ทำให้การสื่อสารในโครงการล้มเหลว ได้แก่:

1. **Information Overload (ข้อมูลท่วมท้นจนไร้ประโยชน์):**
   * ส่งข้อมูลทุกอย่างให้ทุกคนอ่าน โดยไม่ย่อยเนื้อหาให้เหมาะกับระดับของผู้รับ (เช่น ส่ง Log บั๊กเทคนิค 100 ข้อให้ CFO อ่าน)
2. **การสับสนระหว่าง Communication กับ Reporting:**
   * สรุปรายงานเป็นตัวเลขใส่ตาราง แต่ไม่เคยอธิบายว่าตัวเลขเหล่านั้นหมายความว่าอย่างไร และต้องการให้ผู้รับตัดสินใจเรื่องใด
3. **การเลือกใช้รูปแบบการสื่อสารที่ไม่เหมาะสม (Wrong Communication Channel):**
   * ใช้อีเมลในการแก้ปัญหาความขัดแย้งที่ละเอียดอ่อน หรือใช้การประชุม 2 ชั่วโมงเพื่อแจ้งข่าวสารสั้น ๆ ที่ควรส่งทางข้อความ

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. แยก communication ออกจาก reporting และ broadcasting
2. เลือก push, pull หรือ interactive communication ให้เหมาะกับข้อมูลและผู้รับ
3. ออกแบบ communication plan จาก stakeholder needs, decision needs และ feedback loop
4. สื่อสาร risk/issue/status ให้ผู้บริหารเห็น decision required
5. ใช้ ERP และ Hotel Booking scenarios เพื่อปรับสารตาม executive, key users, vendors, product team และ partners

## 3. เหตุผลและที่มา: PM ใช้เวลามากกว่า 90% ของการทำงานไปกับการสื่อสาร

เหตุใด **Project Communications Management** จึงเป็นทักษะชี้ขาดความรอดของ PM?

ผลการศึกษาด้านบริหารโครงการระบุว่า Project Manager ใช้เวลาในวันทำงานมากกว่า **90% ไปกับการสื่อสาร** (พูดคุย, ประชุม, เขียนรายงาน, เจรจาต่อรอง, สร้างความเข้าใจ)

> **Core Rationale:**  
> **Communications Management คือการทำให้แน่ใจว่า ข้อมูลที่ถูกต้อง ถูกส่งไปให้คนที่ถูกต้อง ในเวลาที่ถูกต้อง ผ่านช่องทางที่ถูกต้อง และด้วยรูปแบบที่ประหยัดต้นทุนที่สุด เพื่อให้เกิดความเข้าใจและปฏิกิริยาตอบสนองที่ต้องการ**

---

## 4. Mental Model: รูปแบบการสื่อสาร 3 ทิศทาง และโมเดลการส่งสาร

เพื่อสร้างกรอบความคิดที่ถูกต้อง ให้แบ่งรูปแบบการสื่อสารออกเป็น **3 รูปแบบหลัก (Communication Methods)**:

```text
                                  ┌─── 1. Push Communication (ส่งฝ่ายเดียว)
                                  │    • อีเมล, เอกสารแจ้งข่าวสาร, Status Report
                                  │    • เหมาะกับ: ข้อมูลทั่วไป ผู้รับจำนวนมาก
                                  │
[ Communication Methods ] ────────┼─── 2. Pull Communication (ให้ดึงข้อมูลเอง)
                                  │    • Intranet, Central Dashboard, Wiki, Cloud Folder
                                  │    • เหมาะกับ: ข้อมูลปริมาณมาก อ้างอิงเมื่อต้องการ
                                  │
                                  └─── 3. Interactive Communication (สื่อสารสองทาง)
                                       • ประชุมหน้าต่อหน้า, VDO Conference, โทรศัพท์
                                       • เหมาะกับ: เรื่องซับซ้อน, ความขัดแย้ง, การตัดสินใจด่วน
```

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

### 5.1 3 Sub-processes ของ Communications Management
1. **Plan Communications Management:** วางแผนแนวทาง ช่องทาง ความถี่ และรูปแบบการสื่อสาร (ได้ *Communications Management Plan*)
2. **Manage Communications:** สร้าง รวบรวม กระจาย จัดเก็บ และกำจัดข้อมูลโครงการตามแผนที่วางไว้
3. **Monitor Communications:** ตรวจสอบว่าการสื่อสารมีประสิทธิภาพหรือไม่ และปรับปรุงรูปแบบเมื่อเกิดความเข้าใจคลาดเคลื่อน

### 5.2 องค์ประกอบของแผนการสื่อสาร (Communications Management Plan)
- **Who:** ใครบ้างที่ต้องการข้อมูล? (Stakeholder)
- **What:** เขาต้องการข้อมูลอะไร? (Information Needs - เช่น สรุปบริหาร / รายละเอียดเทคนิค)
- **When:** ต้องการถี่แค่ไหน? (Frequency - รายวัน, รายสัปดาห์, รายเดือน)
- **How:** ส่งผ่านช่องทางใด? (Channel - อีเมล, ประชุม, Dashboard)
- **By Whom:** ใครเป็นผู้รับผิดชอบในการส่งข้อมูล? (Owner)

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (Tailored Executive Reporting)

- **การย่อยข้อมูลสื่อสารตามระดับ Stakeholders:**
  * *Steering Committee / Executives:* ส่งสรุป **Executive Dashboard 1 หน้า** เน้นเฉพาะ Milestone, Risk หลัก, และเรื่องที่ต้องการอนุมัติ (Interactive Meeting 30 นาที/เดือน)
  * *ทีมงานคีย์ข้อมูลหน้างาน:* จัดทำ **Infographic Guide** และวิดีโอสั้น 3 นาทีอธิบายวิธีคีย์ข้อมูลใหม่

### 🏨 Core Scenario B: Hotel Booking Digital Platform (Agile Information Radiators)

- **Information Radiators & Central Dashboard:**
  * ใช้ **Jira / Trello Dashboard** และ **Burndown Chart** เป็นการสื่อสารแบบ Pull Communication ให้ทีมพัฒนาและ Product Owner เข้ามาดูสถานะงานแบบ Real-time โดยไม่ต้องเสียเวลาเขียนรายงานประจำวัน

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"การส่งอีเมลออกไปแล้ว ถือว่าเกิดการสื่อสารขึ้นสมบูรณ์แล้ว":**
   * *ความจริง:* การส่งอีเมลเป็นเพียงการ Push ข้อมูล การสื่อสารจะสมบูรณ์ก็ต่อเมื่อผู้รับได้รับ เข้าใจความหมาย และปฏิกิริยาตอบกลับตรงตามวัตถุประสงค์
2. **"ยิ่งจัดประชุมบ่อยเท่าไร การสื่อสารยิ่งมีประสิทธิภาพ":**
   * *ความจริง:* การประชุมที่ไร้ Agenda และไม่มี Action Items คือการฆาตกรรมเวลาทำงานของทีมงาน สื่อสารเท่าที่จำเป็นและมีเป้าหมายชัดเจน
3. **"PM ต้องเป็นผู้ส่งข้อมูลทุกเรื่องด้วยตนเอง":**
   * *ความจริง:* PM คือผู้วางระบบการสื่อสารและกำกับดูแล ไม่จำเป็นต้องเป็นคนเขียนเอกสารเทคนิคหรือตอบคำถามทุกข้อด้วยตนเอง

---

## 8. PM Thinking & Decision Making

เมื่อต้องวางแผนการสื่อสารในสถานการณ์สำคัญ ให้ PM ใช้ **5W1H Communication Matrix**:

```text
Step 1: Stakeholder Analysis -> ผู้รับข่าวสารนี้คือใคร? (Executive / Dev / User / External)
Step 2: Message Goal -> วัตถุประสงค์ของการสื่อสารนี้คืออะไร? (เพื่อแจ้งให้ทราบ / เพื่อขอการตัดสินใจ / เพื่อเตือนความเสี่ยง)
Step 3: Choose Format -> 
        - หากต้องการขออนุมัติด่วน -> Interactive Meeting + 1-page Summary
        - หากต้องการแจ้งสถิติทั่วไป -> Push Email / Pull Dashboard
Step 4: Feedback Loop -> ตรวจสอบว่าผู้รับเข้าใจตรงกันหรือไม่ โดยให้ผู้รับสรุปความเข้าใจกลับมา (Read-back)
```

---

## 9. Reflection & Assessment

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการของคุณ มีเอกสาร **Communications Management Plan** ที่ระบุช่องทางและความถี่การสื่อสารชัดเจนแล้วหรือยัง?
2. รายงานความก้าวหน้าที่คุณส่งให้ผู้บริหารในปัจจุบัน มีความยาวเกินไปจนผู้บริหารไม่อ่าน หรือย่อยมาเฉพาะจุดที่ต้องตัดสินใจแล้ว?

---

### Context for later learning

เมื่อเราสร้างระบบการสื่อสารที่โปร่งใสและครอบคลุมแล้ว เครื่องมือสำคัญที่จะช่วยให้เราคาดการณ์และรับมือกับความไม่แน่นอนล่วงหน้าคือ **Project Risk Management** ในบทถัดไป **Lesson 13** ครับ!

## PM Decision Thinking

**[PMBOK 6]** Communications Management ครอบคลุม plan, manage และ monitor communications. **[PMBOK 7]** stakeholder engagement และ systems thinking ทำให้ communication ต้องสร้างความเข้าใจและ action ไม่ใช่แค่ส่งข้อมูล.

| Field | Lesson 12 Application |
|---|---|
| Decision | ข้อมูลนี้ต้อง push, pull, interactive หรือ escalate |
| Owner | PM ออกแบบ communication system; message owner ส่งข้อมูลเฉพาะเรื่อง |
| Inputs | stakeholder needs, urgency, complexity, sensitivity, decision required, channel effectiveness |
| Options | executive summary, dashboard, workshop, meeting, email, read-back, issue escalation |
| Trade-offs | speed vs clarity, transparency vs overload, broad broadcast vs tailored message |
| Risk | ส่งข้อมูลเยอะแต่ผู้รับไม่เข้าใจ decision ที่ต้องทำ |
| Evidence | response quality, decision latency, misunderstanding, meeting actions, dashboard usage |
| Next Action | ปรับ communication matrix และ feedback loop |

### PM Insight

Communication ที่ดีวัดจากความเข้าใจและ action ที่เกิดขึ้น ไม่ใช่จำนวนหน้ารายงาน. ถ้าผู้บริหารไม่รู้ว่าต้องตัดสินใจอะไร รายงาน 20 หน้าก็ยังสื่อสารไม่สำเร็จ.

## ERP Scenario

**[Teaching Scenario]** ERP Transformation มี sponsor คุณสมชาย, PM คุณเอก, TechConsult, 80 key users และหลาย functional managers.

Communication design:

- Steering Committee: dashboard 1 หน้า เน้น milestone, budget, top risks, decisions required
- Key users: task-focused communication เช่น UAT schedule, training guide, issue escalation
- Functional managers: capacity impact และ decision deadline
- TechConsult: working-level issue log, change log, contract/action owner
- Sponsor: exception-based escalation เมื่อ go-live, budget หรือ adoption risk เกิน tolerance

## Hotel Booking Scenario

**[Teaching Scenario]** Hotel Booking Platform มี PO คุณนภา, PM คุณสุทธิ, marketing, product team, hotel partners และ operations.

Communication design:

- Product team: pull dashboard เช่น backlog, burndown, defect trend
- PO/marketing: interactive release decision meeting เมื่อ conversion/payment readiness เสี่ยง
- Hotel partners: concise rollout guide และ inventory readiness reminders
- Operations/support: known issues, support playbook และ launch escalation path
- Sponsor คุณจิรา: outcome-focused update เรื่อง direct booking, launch readiness และ risk

## Real Enterprise Example

**[Enterprise Practice]** “ส่งอีเมลแล้ว” ไม่ใช่หลักฐานว่าเกิด communication. หาก message อยู่ท้าย attachment, ไม่มี decision ask, ไม่มี owner และไม่มี feedback loop PM ควรถือว่ายังไม่ได้สื่อสารในเชิงบริหาร.

## Common Mistakes

1. ส่งข้อมูลเหมือนกันให้ทุก stakeholder
2. ทำ report ยาวแต่ไม่ระบุ decision required
3. ใช้อีเมลแก้ conflict ที่ต้อง interactive
4. ไม่มี feedback loop หรือ read-back สำหรับเรื่องสำคัญ
5. ไม่ monitor ว่าช่องทางเดิมยังใช้ได้ผลหรือไม่

## Common Misconceptions

| Misconception | Correction |
|---|---|
| Communication คือส่งข้อมูล | Communication คือทำให้เข้าใจและเกิด action ที่ถูกต้อง |
| รายงานยาวคือโปร่งใส | โปร่งใสคือเห็นสาระ ความเสี่ยง และ decision |
| PM ต้องสื่อสารทุกเรื่องเอง | PM ออกแบบระบบและ owner ของ message |
| Dashboard แทนการประชุมได้ทุกกรณี | เรื่องซับซ้อนหรือ conflict ต้อง interactive |

## Interview Questions

### Definition

1. Push, pull และ interactive communication ต่างกันอย่างไร
2. Communications plan ควรมีองค์ประกอบใดบ้าง

### Judgement

1. ถ้าผู้บริหารไม่อ่านรายงาน คุณจะปรับ communication อย่างไร
2. ถ้า risk สำคัญถูกซ่อนในรายละเอียด คุณจะ escalate อย่างไร

### Behavioral

1. เล่าครั้งหนึ่งที่คุณปรับ communication ให้ stakeholder เข้าใจดีขึ้น
2. คุณเคยสื่อสารข่าวร้ายของ project อย่างไร

### Scenario

1. ใน ERP ถ้า data migration risk ต้องใช้ sponsor decision คุณจะสื่อสารอย่างไร
2. ใน Hotel Booking ถ้า payment failure กระทบ launch campaign คุณจะเลือก channel ใด

## PM Dictionary

| Term | Meaning |
|---|---|
| Communications Management Plan | แผนกำหนดผู้รับ ข้อมูล ความถี่ ช่องทาง และ owner |
| Push Communication | ส่งข้อมูลไปยังผู้รับ เช่น email/report |
| Pull Communication | ให้ผู้รับดึงข้อมูลเอง เช่น dashboard/wiki |
| Interactive Communication | สื่อสารสองทาง เช่น meeting/workshop/call |
| Feedback Loop | วิธีตรวจว่าผู้รับเข้าใจและตอบสนองถูกต้อง |
| Information Overload | ข้อมูลมากเกินจนไม่ช่วยตัดสินใจ |
| Decision Required | ประเด็นที่ผู้รับต้องตัดสินใจหรืออนุมัติ |
| Information Radiator | dashboard/visual ที่ให้ทีมเห็นสถานะร่วมกัน |

## Workshop

### Scenario

ERP data migration เสี่ยงเลื่อน go-live. Hotel Booking payment failure เสี่ยงทำให้ launch campaign เสียหาย.

### Task

ให้ผู้เรียนทำ communication matrix 1 หน้า:

1. stakeholder group
2. message objective
3. information needed
4. channel/method
5. frequency/timing
6. feedback loop
7. decision/action required

### Debrief

คำตอบที่ดีต้องเลือกช่องทางตามความซับซ้อนและความเร่ง ไม่ใช่ส่งทุกอย่างทาง email.

## Assessment

ดูแบบประเมินหลักที่ [Lesson 12 Assessment](./Lesson-12_3-Assessment.md). แบบประเมินควรวัด judgement เรื่อง channel choice, executive messaging, escalation และ feedback loop.

## Executive Summary

Communications Management คือการทำให้ข้อมูลที่ถูกต้องไปถึงคนที่ถูกต้องในรูปแบบที่ทำให้เข้าใจและตัดสินใจได้. PM ต้องออกแบบ communication ตาม stakeholder need, urgency และ complexity พร้อม monitor ว่าการสื่อสารได้ผลจริงหรือไม่.

## Lesson Connection

Lesson 11 ทำให้บทบาทและ resource ชัด. Lesson 12 ทำให้ข้อมูล decision และ feedback ไหลอย่างถูกต้อง. Lesson 13 จะใช้ communication เป็นฐานในการทำ risk management เพราะ risk ที่ไม่ถูกสื่อสารคือ risk ที่องค์กรไม่มีทางจัดการได้ทัน.

## AI Continuation Context

Future AI agents must treat communication as shared understanding plus action. Keep ERP executive/key-user communication and Hotel Booking dashboard/launch communication as recurring examples.

## Artifact Handoff

- **Output:** Sponsor-approved Communication Plan/Cadence and PM-approved Status Report.
- **Evidence:** distribution, decision and escalation records.
- **Next use:** L13 turns material signals into risks, triggers and issues.

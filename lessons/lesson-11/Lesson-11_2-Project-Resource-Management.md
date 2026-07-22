---
lesson: 11
sequence: 11.2
title: Project Resource Management
document_type: Lesson
level: Core
status: Draft
validation_status: Pending Final Repository Validation
version: 1.0
last_updated: 2026-07-22
prerequisite:
  - Lesson 10 — Project Quality Management
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 11_2 — Project Resource Management

## Opening Professional Question — ถ้าคนในทีมแย่งกันทำงานอย่างสับสน และไม่มีใครรู้ว่าใครมีอำนาจตัดสินใจในงานชิ้นไหน โครงการจะดำเนินไปได้อย่างไร?

ลองพิจารณาความวุ่นวายที่เกิดขึ้นในทีมโครงการ:

> ในการประชุมพัฒนาซอฟต์แวร์เมื่อเกิดปัญหาขัดข้องทางเทคนิค นักวิเคราะห์ระบบชี้ไปที่ Developer, Developer ชี้ไปที่ Tester, และ Tester ชี้ไปที่ Vendor โดยไม่มีใครยอมรับผิดชอบในการแก้ไขปัญหา และเมื่อ PM ถามหาเอกสารสเปค ทุกคนกลับตอบว่า *"คิดว่าอีกคนหนึ่งทำไปแล้ว"*

ปรากฏการณ์นี้เกิดขึ้นเพราะ **"ความไม่ชัดเจนในบทบาทและความรับผิดชอบ" (Unclear Roles & Responsibilities)**

> **คำถามสำคัญคือ:** การบริหารทรัพยากร (Resource Management) หมายถึงการคำนวณจำนวนคนและอุปกรณ์ลงในตารางเพียงอย่างเดียว หรือรวมถึงการสร้างทีม การพัฒนาศักยภาพ การกำหนดอำนาจหน้าที่ (RACI) และการบริหารความขัดแย้ง?

---

## Why This Matters — การมองคนเป็นเพียง "ตัวเลขทรัพยากร" (Resource Overhead)

ความล้มเหลวหลักในการบริหารทรัพยากรโครงการ ได้แก่:

1. **การปฏิบัติต่อมนุษย์เหมือนเป็นสิ่งของ (Fungible Units):**
   * คิดว่าการเปลี่ยนตัว Senior Developer ออก แล้วใส่ Junior Developer เข้าไป 2 คน จะได้เนื้องานเท่าเดิม โดยไม่คำนึงถึงทักษะ ประสบการณ์ และช่วงเวลาปรับตัว (Onboarding)
2. **บทบาทและหน้าที่ทับซ้อนหรือหลุดหาย (Role Confusion):**
   * ไม่มีตารางกำหนดชัดเจนว่าใครเป็นผู้ลงมือทำ (Responsible), ใครเป็นผู้อนุมัติ (Accountable), ใครต้องถูกปรึกษา (Consulted) และใครต้องถูกแจ้งข่าว (Informed)
3. **การหลีกเลี่ยงหรือไม่สามารถจัดการความขัดแย้งในทีม (Conflict Avoidance):**
   * ปล่อยให้ความขัดแย้งระหว่างสมาชิกในทีมลุกลามจนทำลายบรรยากาศการทำงานและขวัญกำลังใจของทีมงาน

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. แยก human resources และ physical resources ในบริบทโครงการ
2. ใช้ RACI เพื่อกำหนด Responsible, Accountable, Consulted และ Informed
3. ประเมิน capacity, skill, availability และ ramp-up risk
4. เลือกวิธีจัดการ conflict ให้เหมาะกับสถานการณ์
5. ใช้ ERP และ Hotel Booking scenarios เพื่อจัดการ key-user workload, agile team และ vendor/resource constraints

## 3. เหตุผลและที่มา: ทรัพยากรมนุษย์และกายภาพเป็นตัวขับเคลื่อนผลงานจริง

เหตุใด **Project Resource Management** จึงเป็นหัวใจสำคัญในการนำแผนงานไปสู่การปฏิบัติ?

เพราะแผนงาน เอกสาร และตารางเวลาทั้งหมด จะไม่มีทางกลายเป็นความจริงได้ หากปราศจาก **"คน"** ที่ลงมือปฏิบัติงาน และ **"ทรัพยากรกายภาพ"** (เครื่องมือ, อุปกรณ์, เซิร์ฟเวอร์, สถานที่) ที่สนับสนุนการทำงาน

> **Core Rationale:**  
> **Resource Management มีเป้าหมายเพื่อให้แน่ใจว่า ทรัพยากรที่จำเป็นทั้งหมด (ทั้งคนและสิ่งของ) พร้อมใช้งานในเวลาที่ถูกต้อง ถูกจัดสรรอย่างคุ้มค่า และทีมงานมีความพร้อมทั้งทักษะและกำลังใจในการส่งมอบงาน**

---

## 4. Mental Model: โครงสร้างกำหนดหน้าที่ RACI Matrix

เพื่อสร้างกรอบความคิดที่ชัดเจน ให้ใช้ **RACI Matrix** ในการกำหนดบทบาทสำหรับทุกกิจกรรมสำคัญ:

```text
[ RACI Definitions ]
• R = Responsible : ผู้ลงมือปฏิบัติงานจริงให้เสร็จ (ทำ)
• A = Accountable  : ผู้มีอำนาจตัดสินใจและรับผิดชอบผลงานสูงสุด (ต้องมีเพียง 1 คนต่อกิจกรรม!)
• C = Consulted    : ผู้ให้ข้อมูลและคำปรึกษาเชิงลึกก่อนทำงาน (ถาม)
• I = Informed     : ผู้รับทราบความก้าวหน้าและผลลัพธ์ (บอก)
```

### ตัวอย่าง RACI Matrix Table:

| กิจกรรม (Activity) | Project Manager | Lead Dev | Business Analyst | Quality Assurance | Sponsor |
|---|---|---|---|---|---|
| **รวบรวม Requirements** | A | C | **R** | C | I |
| **ออกแบบ Architecture** | A | **R** | C | C | I |
| **ทดสอบระบบ UAT** | A | C | C | **R** | I |
| **อนุมัติวัน Go-live** | C | C | C | C | **A / R** |

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

### 5.1 6 Sub-processes ของ Resource Management
1. **Plan Resource Management:** วางแผนแนวทางการจัดหา บริหาร และคัดเลือกทรัพยากร
2. **Estimate Activity Resources:** ประมาณการจำนวนประเภทของทีมงาน เครื่องมือ และอุปกรณ์ที่ต้องใช้
3. **Acquire Resources:** จัดหาและคัดเลือกทีมงานและอุปกรณ์กายภาพเข้าสู่โครงการ
4. **Develop Team:** พัฒนาทักษะ สร้างแรงจูงใจ และสร้างบรรยากาศการทำงานร่วมกัน (Team Building)
5. **Manage Team:** ติดตามผลงาน ให้ Feedback บริหารความขัดแย้ง และปรับปรุงการทำงานของทีม
6. **Control Resources:** ติดตามการใช้ทรัพยากรกายภาพให้อยู่ในแผนและแก้ไขเมื่อเกิดการขาดแคลน

### 5.2 การบริหารความขัดแย้ง (Conflict Management 5 Techniques)
- **Withdraw/Avoid:** ถอยห่างหรือชะลอการเผชิญหน้า
- **Smooth/Accommodate:** เน้นจุดที่เห็นตรงกันเพื่อรักษาความสัมพันธ์
- **Compromise/Reconcile:** ต่อรองหาทางออกคนละครึ่งทาง
- **Force/Direct:** ใช้อำนาจตัดสินใจสั่งการด่วน (ใช้เมื่อเกิดวิกฤต)
- **Collaborate/Problem Solve (Best Approach):** รวมพลังหาสาเหตุรากเหง้าเพื่อแก้ปัญหาร่วมกัน

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (Cross-Functional Resource Matrix)

- **ความท้าทายเรื่องทรัพยากร:**
  * ฝ่ายการเงินและฝ่ายจัดซื้อต้องแบ่งเวลาพนักงานมาร่วมทำโครงการ ERP ควบคู่ไปกับการทำงานประจำวัน (Operation)
- **การแก้ปัญหาของ PM:**
  * จัดทำ **Resource Histograms** แสดงภาระงาน เพื่อตกลงกับ Functional Manager ในการดึงตัวพนักงานมาทำโครงการแบบ Part-time 40% อย่างชัดเจน โดยไม่กระทบงานประจำวัน

### 🏨 Core Scenario B: Hotel Booking Digital Platform (Agile Self-Organizing Team)

- **Cross-Functional Pod:**
  * จัดทีมพัฒนาแบบข้ามสายงาน (Cross-functional Team) ประกอบด้วย UX Designer, Frontend Dev, Backend Dev, และ QA ทำงานร่วมกันในโต๊ะเดียวกัน
- **Team Motivation & Empowerment:**
  * ให้อำนาจทีมในการตัดสินใจแก้ปัญหาเชิงเทคนิคด้วยตนเอง (Empowered Team) โดย PM ทำหน้าที่เป็นผู้ขจัดอุปสรรค (Servant Leader / Obstacle Remover)

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"กิจกรรมหนึ่งกิจกรรมสามารถมี Accountable (A) ได้หลายคน":**
   * *ความจริง:* กิจกรรมหนึ่ง ๆ ต้องมี **Accountable (A) เพียง 1 คนเท่านั้น** หากมี A หลายคน จะไม่มีใครยอมรับผิดชอบจริงเมื่อเกิดปัญหา
2. **"ความขัดแย้งในทีมเป็นเรื่องเลวร้ายที่ต้องกำจัดให้หมดสิ้น":**
   * *ความจริง:* ความขัดแย้งเชิงความคิด (Task Conflict) นำไปสู่นวัตกรรมและการตัดสินใจที่ดีขึ้น PM ต้องบริหารความขัดแย้งให้สร้างสรรค์ ไม่ให้ลุกลามเป็นความขัดแย้งส่วนตัว (Relationship Conflict)
3. **"การเพิ่มคนในโครงการช่วงท้ายจะช่วยให้งานเสร็จเร็วขึ้นเสมอ":**
   * *ความจริง:* การเพิ่มคนใหม่ต้องเสียเวลาในการสอนงาน (Ramp-up Time) และเพิ่มช่องทางการสื่อสาร ซึ่งอาจทำให้งานช้าลงกว่าเดิม

---

## 8. PM Thinking & Decision Making

เมื่อเกิดความขัดแย้งหรือปัญหาทรัพยากรในทีม ให้ PM ใช้ **Resource Conflict Decision Steps**:

```text
Step 1: Identify Conflict Source -> ความขัดแย้งเกิดจากเรื่องใด?
        - เกิดจากเป้าหมาย/ทรัพยากรขัดแย้งกัน (Task)
        - เกิดจากสไตล์การทำงาน/อารมณ์ส่วนบุคคล (Relationship)

Step 2: Choose Conflict Resolution Technique ->
        - หากต้องการผลลัพธ์ยั่งยืน -> ใช้ Collaborate / Problem Solve (เปิดอกคุยหา Root Cause)
        - หากเกิดสถานการณ์ฉุกเฉินต้องตัดสินใจทันที -> ใช้ Force / Direct

Step 3: Update RACI Matrix & Resource Plan -> หากมีการปรับบทบาทหน้าที่ ให้สื่อสารผัง RACI ใหม่แก่ทุกคนทันที
```

---

## 9. Reflection & Assessment

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการของคุณ มีเอกสาร **RACI Matrix** ที่ระบุผู้รับผิดชอบสูงสุด (A) ของแต่ละงานย่อยชัดเจนแล้วหรือยัง?
2. เมื่อเกิดความขัดแย้งในทีม คุณมักเลือกใช้วิธีหลีกเลี่ยง (Avoid), การใช้อำนาจสั่งการ (Force), หรือการหาสาเหตุร่วมกัน (Collaborate)?

---

## 🌉 Bridge to Next Lesson: Lesson 12 — Project Communications Management

เมื่อเราจัดโครงสร้างบทบาททีมงาน (**RACI**) เรียบร้อยแล้ว ช่องทางและวิธีการที่จะทำให้ทุกคนทำงานร่วมกันได้อย่างราบรื่นคือ **Project Communications Management** ในบทถัดไป **Lesson 12** ครับ!

## PM Decision Thinking

**[PMBOK 6]** Resource Management ครอบคลุม plan, estimate, acquire, develop, manage team และ control resources. **[PMBOK 7]** team, leadership และ stewardship ทำให้ PM ต้องบริหารคนอย่างมีบริบท ไม่ใช่ใช้คนเป็นตัวเลขแทนกันได้.

| Field | Lesson 11 Application |
|---|---|
| Decision | resource gap นี้ต้อง acquire, reassign, train, escalate, reduce scope หรือ replan |
| Owner | PM จัด resource plan; functional manager/sponsor ตัดสิน capacity และ priority conflict |
| Inputs | RACI, resource calendar, skill matrix, workload, team performance, conflict source, physical resource availability |
| Options | add resource, change allocation, outsource, train, reduce workload, sequence work, negotiate priority |
| Trade-offs | speed vs ramp-up, expert bottleneck vs quality, team morale vs overtime, cost vs capacity |
| Risk | คิดว่าคนแทนกันได้ทันทีและมองข้าม onboarding/coordination cost |
| Evidence | utilization, resource histogram, burndown, defect trend, absenteeism, decision delay |
| Next Action | update RACI/resource plan และ escalate capacity conflict ด้วย evidence |

### PM Insight

Resource Management คือการทำให้คนที่ถูกต้อง พร้อมด้วย skill ที่ถูกต้อง อยู่ในเวลาที่ถูกต้อง และมี authority ชัดเจนพอจะทำงานได้. การใส่คนเพิ่มโดยไม่ดู skill และ coordination อาจทำให้งานช้าลง.

## ERP Scenario

**[Scenario]** ERP Transformation มี 80 key users ที่ต้องทำงานโครงการคู่กับงานประจำใน finance, sales, warehouse, production และ HR.

Resource decision:

- key users ต้องมี allocation ชัด เช่น 40% สำหรับ UAT/training ไม่ใช่ “ช่วยเมื่อว่าง”
- functional managers ต้องเห็น resource histogram และผลกระทบต่อ go-live หากไม่ปล่อยคน
- RACI ต้องมี A เพียงคนเดียวสำหรับ master data owner ต่อ domain
- ถ้า data cleansing delay เพราะ resource ไม่พอ PM ต้องเสนอ options: backfill, overtime, vendor support, reschedule หรือ scope trade-off

## Hotel Booking Scenario

**[Scenario]** Hotel Booking Platform ใช้ cross-functional team ที่มี UX, frontend, backend, QA, PO และ operations support.

Resource decision:

- ถ้า backend developer ติด payment integration งาน inventory API อาจกลายเป็น bottleneck
- เพิ่ม developer ใหม่ช่วงท้ายต้องคิด ramp-up และ code ownership risk
- QA capacity ต้องสัมพันธ์กับ release cadence และ regression testing
- PM/PO ต้องป้องกันทีมจากการรับ feature ใหม่จน focus แตกและ quality ลด

## Real Enterprise Example

**[Instructor Interpretation]** หลาย project plan ดูเหมือนมีคนพอเพราะ spreadsheet ใส่ชื่อครบ แต่ในชีวิตจริงคนเดียวกันอยู่ 5 โครงการ, มีงานประจำ, ไม่มี authority หรือไม่มี skill ตรงงาน. Lesson 11 ต้องทำให้ผู้เรียนถามว่า “available จริงไหม” ไม่ใช่ “มีชื่อใน resource plan ไหม”.

## Common Mistakes

1. ใส่ชื่อคนลงแผนโดยไม่เช็ก availability และ skill
2. มี Accountable หลายคนใน RACI เดียวกัน
3. แก้ delay ด้วยการเพิ่มคนโดยไม่คิด ramp-up
4. ปล่อย conflict ให้กลายเป็น relationship conflict
5. ลืม physical resources เช่น test environment, devices, licenses และ meeting rooms

## Common Misconceptions

| Misconception | Correction |
|---|---|
| Resource คือจำนวนคน | Resource รวม skill, capacity, authority, equipment และ environment |
| Senior 1 คนแทนด้วย junior 2 คนได้เสมอ | Skill, context และ ramp-up ทำให้ไม่เทียบตรงได้ |
| Conflict ต้องกำจัด | Task conflict ที่ดีช่วยตัดสินใจดีขึ้น |
| RACI เป็นเอกสาร HR | RACI คือ decision clarity ของ project |

## Interview Questions

### Definition

1. RACI คืออะไร และทำไม Accountable ควรมีหนึ่งคน
2. Resource histogram ใช้ช่วย PM อย่างไร

### Judgement

1. ถ้า key user ไม่พร้อมเพราะงานประจำ คุณจะเจรจากับ functional manager อย่างไร
2. ถ้าเพิ่มคนอาจทำให้งานช้าลง คุณจะอธิบาย sponsor อย่างไร

### Behavioral

1. เล่าครั้งหนึ่งที่คุณจัดการ resource conflict
2. คุณเคยพัฒนาทีมหรือแก้ morale problem อย่างไร

### Scenario

1. ใน ERP ถ้า finance key users ไม่ว่าง UAT คุณจะเสนอ resource options อย่างไร
2. ใน Hotel Booking ถ้า QA ไม่พอสำหรับ regression คุณจะปรับ release อย่างไร

## PM Dictionary

| Term | Meaning |
|---|---|
| Resource Management | การจัดหา พัฒนา บริหาร และควบคุมทรัพยากรโครงการ |
| RACI | ตารางบทบาท Responsible, Accountable, Consulted, Informed |
| Resource Calendar | ปฏิทิน availability ของคน/ทรัพยากร |
| Resource Histogram | ภาพแสดง workload หรือ resource demand ตามเวลา |
| Skill Matrix | ตารางความสามารถของสมาชิกทีม |
| Ramp-up Time | เวลาที่คนใหม่ต้องใช้เพื่อเข้าใจงานและทำงานได้เต็มที่ |
| Team Development | การพัฒนาทีม skill, trust และ performance |
| Conflict Management | การจัดการความขัดแย้งเพื่อให้เกิด decision/workflow ที่ดี |

## Workshop

### Scenario

ERP key users ถูกดึงไปทำ month-end close ทำให้ UAT ช้า. Hotel Booking backend และ QA ไม่พอเพราะ payment defect กินเวลาทีม.

### Task

ให้ผู้เรียนทำ resource recovery plan 1 หน้า:

1. role/resource gap
2. RACI impact
3. capacity evidence
4. options และ trade-offs
5. conflict resolution approach
6. decision owner และ escalation

### Debrief

คำตอบที่ดีต้องแก้ทั้ง capacity และ authority ไม่ใช่แค่บอกว่า “เพิ่มคน”.

## Assessment

ดูแบบประเมินหลักที่ [Lesson 11 Assessment](./Lesson-11_3-Assessment.md). แบบประเมินควรวัด judgement เรื่อง RACI, capacity, conflict และ resource trade-off.

## Executive Summary

Resource Management ทำให้แผนกลายเป็นงานจริงผ่านคน ทีม skill และทรัพยากรกายภาพ. PM ต้องรู้ว่าใครทำ ใครตัดสินใจ ใครมี capacity และ conflict ใดต้องจัดการ. ชื่อคนในแผนไม่พอ ต้องมี availability, authority และ capability.

## Lesson Connection

Lesson 10 ทำให้เห็นว่าคุณภาพต้องเกิดจากกระบวนการและคนที่พร้อม. Lesson 11 จัดการ resource ที่ทำให้คุณภาพและ delivery เกิดจริง. Lesson 12 จะต่อไปที่ Communications Management เพื่อให้บทบาท decision และข้อมูลไหลถึงคนที่ต้องใช้.

## AI Continuation Context

Future AI agents must tie Resource Management to real capacity and authority. Use ERP 80 key users and Hotel Booking cross-functional delivery team as recurring resource constraints.

---
lesson: 8
sequence: 8.2
title: Project Schedule Management
document_type: Lesson
level: Core
status: Draft
validation_status: Pending Final Repository Validation
version: 1.0
last_updated: 2026-07-22
prerequisite:
  - Lesson 07 — Project Scope Management and WBS
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 08_2 — Project Schedule Management

## Opening Professional Question — ทำไมโครงการส่วนใหญ่จึงล่าช้ากว่ากำหนด ทั้งที่มีการวาดแผนตารางเวลา (Gantt Chart) ไว้อย่างสวยงาม?

ลองพิจารณาปรากฏการณ์ที่พบได้บ่อยในองค์กร:

> ในวัน Kickoff โครงการ PM นำเสนอ Gantt Chart ความยาว 50 หน้าที่กำหนดวันเสร็จของทุกกิจกรรมไว้อย่างลงตัว แต่เมื่อเริ่มทำงานจริงได้เพียง 2 สัปดาห์ แผนงานกลับล่าช้าทันที และสุดท้ายวัน Go-live ก็ต้องเลื่อนออกไปหลายเดือน

เหตุใดตารางเวลาที่ดูสมบูรณ์แบบบนหน้ากระดาษ จึงพังทลายลงอย่างรวดเร็วในชีวิตจริง?

> **คำถามสำคัญคือ:** การบริหารตารางเวลา (Schedule Management) คือการ "ใส่วันที่ลงในปฏิทิน" เพียงอย่างเดียว หรือคือการวิเคราะห์ลำดับความเชื่อมโยงเชิงวิศวกรรม (Dependencies) และการบริหารสายงานวิกฤต (Critical Path)?

---

## Why This Matters — การวางตารางเวลาแบบไม่มีตรรกะเชื่อมโยง

ปัญหาหลักที่ทำให้การบริหารเวลาล้มเหลว ได้แก่:

1. **การกำหนดวันที่แบบย้อนกลับ (Backward Scheduling Without Logic):**
   * ล็อควันจบโครงการตามใจผู้บริหาร แล้วจับงานทั้งหมดมาอัดลงในเวลาที่มี โดยไม่วิเคราะห์ความเชื่อมโยงและความเป็นไปได้จริง
2. **ละเลยการหา Critical Path (สายงานวิกฤต):**
   * ไม่รู้ว่ากิจกรรมใดล่าช้าไม่ได้เลยแม้แต่สัมผัสเดียว (Zero Float) และกิจกรรมใดพอยืดหยุ่นได้ ทำให้ PM โฟกัสติดตามงานผิดจุด
3. **การประมาณเวลาแบบโลกสวย (Optimistic Estimation):**
   * ประเมินเวลาทำงานโดยสมมติว่าไม่มีอุปสรรคใด ๆ เกิดขึ้นเลย และลืมคิดเผื่อระยะเวลาในการรอคอย (Lag Time) หรือการส่งมอบข้ามทีม

---

## Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. อธิบาย schedule baseline และความสัมพันธ์กับ WBS
2. แยก activity, dependency, duration, milestone, float และ critical path
3. วิเคราะห์ว่าความล่าช้ากระทบวันจบโครงการหรือไม่
4. เลือก crashing หรือ fast tracking จาก trade-off ด้าน cost, risk และ quality
5. ใช้ ERP และ Hotel Booking scenarios เพื่อออกแบบ recovery decision ที่มีเหตุผล

## 3. เหตุผลและที่มา: เวลาคือทรัพยากรที่สูญแล้วสูญเลย

เหตุใด **Project Schedule Management** จึงเป็นมิติท้าทายที่สุดมิติหนึ่ง?

เพราะต่างจากงบประมาณหรือทรัพยากรมนุษย์ที่อาจหามาเพิ่มได้ตามสถานการณ์ **"เวลาเป็นทรัพยากรที่ไม่สามารถสร้างเพิ่มหรือซื้อคืนได้"**

> **Core Rationale:**  
> **Schedule Management ไม่ใช่แค่การสร้างตารางเวลาส่งเดช แต่คือการสร้างฐานอ้างอิงระยะเวลา (Schedule Baseline) ที่วัดผลได้จริง และเป็นเครื่องมือสื่อสารความก้าวหน้าแก่คนทั้งองค์กร**

---

## 4. Mental Model: สายงานวิกฤต (Critical Path Method — CPM)

เพื่อสร้างกรอบความคิดที่ถูกต้อง ให้มองตารางเวลาเป็น **"เครือข่ายความสัมพันธ์ของกิจกรรม" (Network Diagram)**:

```text
               ┌─── [ Activity B: Design (3 days) ] ───┐
               │                                       │
[ Activity A ] ─┤                                       ├─► [ Activity D: Testing (4 days) ]
 (Setup 2 days)│                                       │
               └─── [ Activity C: Build (7 days)  ] ───┘
```

- **Path 1 (A → B → D):** 2 + 3 + 4 = 9 วัน
- **Path 2 (A → C → D):** 2 + 7 + 4 = 13 วัน  *(Critical Path)*

### หลักการสำคัญของ Critical Path:
- **Critical Path** คือเส้นทางกิจกรรมที่ยาวที่สุดในโครงการ ซึ่งเป็นตัวกำหนด "ระยะเวลาที่สั้นที่สุดที่โครงการจะทำเสร็จได้"
- กิจกรรมบน Critical Path มี **Float (Slack) = 0** หมายความว่า หากกิจกรรม C ล่าช้าไป 1 วัน วันจบโครงการจะล่าช้าไป 1 วันทันที!

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [PMBOK Overview](../../references/PMBOK-Overview.md):

### 5.1 6 Sub-processes ของ Schedule Management
1. **Plan Schedule Management:** วางแผนแนวทางการสร้างและควบคุม Schedule
2. **Define Activities:** ดึงกิจกรรมย่อยมาจาก Work Packages ใน WBS
3. **Sequence Activities:** จัดลำดับความสัมพันธ์ก่อน-หลัง (FS, SS, FF, SF)
4. **Estimate Activity Durations:** ประเมินระยะเวลาทำงานของแต่ละกิจกรรม (เช่น ใช้ 3-Point Estimating: O, P, M)
5. **Develop Schedule:** นำข้อมูลทั้งหมดมาสร้าง **Schedule Baseline** และ Gantt Chart ด้วยวิธี CPM
6. **Control Schedule:** ติดตามความก้าวหน้าเปรียบเทียบกับ Baseline และใช้เทคนิคเร่งงาน (Crashing / Fast Tracking) เมื่อล่าช้า

### 5.2 เทคนิคการเร่งตารางเวลา (Schedule Compression Techniques)
- **Crashing (การอัดงบเร่งงาน):** เพิ่มทรัพยากรเข้าไปในกิจกรรมบน Critical Path (เช่น ทำ OT, เพิ่มคน) -> ค่าใช้จ่ายสูงขึ้น
- **Fast Tracking (การทำซ้อนขนาน):** ปรับกิจกรรมที่เคยทำต่อกัน ให้มาทำขนานกันไป -> เพิ่มความเสี่ยงและงานซ้ำซ้อน

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (Critical Path & Dependencies)

- **Activity Sequencing & Critical Path:**
  * กิจกรรม *Data Cleansing (3 สัปดาห์)* และ *Config ERP System (4 สัปดาห์)* ทำขนานกันได้
  * แต่กิจกรรม *Data Migration (2 สัปดาห์)* ต้องเกิด **หลัง** Data Cleansing และ Config เสร็จสมบูรณ์เท่านั้น (Finish-to-Start)
- **Schedule Control:**
  * หากพบว่า Data Cleansing ล่าช้า PM ใช้เทคนิค **Crashing** เพิ่มทีมคีย์ข้อมูลจากภายนอกเข้ามาร่วมทำทันทีเพื่อรักษา Critical Path ไว้

### 🏨 Core Scenario B: Hotel Booking Digital Platform (Agile Release Planning)

- **Release & Sprint Schedule:**
  * บริหารตารางเวลาด้วยกรอบ **Timeboxing** ผ่าน Sprint ละ 2 สัปดาห์
- **Milestone Tracking:**
  * กำหนด Milestone สำคัญ ได้แก่ *Payment Gateway Integration Sign-off*, *Internal Beta Release*, และ *Public Launch Date* เพื่อควบคุมทิศทางภาพรวม

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **"Gantt Chart คือแผนการบริหารตารางเวลาทั้งหมด":**
   * *ความจริง:* Gantt Chart เป็นเพียงเครื่องมือแสดงผล (Visualization) หัวใจที่แท้จริงคือตรรกะความเชื่อมโยง (Dependencies) และการคํานวณ Critical Path
2. **"เมื่อโครงการล่าช้า ให้ใส่คนเพิ่มเข้าไปในงานทันที (Adding Manpower)":**
   * *ความจริง:* กฎของ Brooks (Brooks' Law) ระบุว่า "การเพิ่มคนเข้าไปในโครงการซอฟต์แวร์ที่ล่าช้า จะยิ่งทำให้โครงการล่าช้ากว่าเดิม" เนื่องจากต้องเสียเวลาสื่อสารและสอนงานคนใหม่
3. **"การทำ Fast Tracking ไม่มีราคาที่ต้องจ่าย":**
   * *ความจริง:* การทำซ้อนขนานงานมักนำไปสู่การทำงานซ้ำ (Rework) และเพิ่มความเสี่ยงที่คุณภาพงานจะตกต่ำ

---

## 8. PM Thinking & Decision Making

เมื่อตารางเวลาเริ่มล่าช้ากว่า Baseline ให้ PM ใช้ **Schedule Recovery Decision Flow**:

```text
Step 1: Check Critical Path -> กิจกรรมที่ล่าช้าอยู่นี้ อยู่บน Critical Path หรือไม่?
        - ถ้าอยู่นอก Critical Path (มี Float เหลือ) -> บริหารทรัพยากรภายใน Float ยังไม่กระทบวันจบ
        - ถ้าอยู่บน Critical Path -> ไป Step 2

Step 2: Evaluate Fast Tracking -> สามารถทำกิจกรรมย่อยขนานกันได้หรือไม่?
        - ข้อดี: ไม่เพิ่มงบประมาณ
        - ข้อเสีย: เสี่ยงเกิด Rework

Step 3: Evaluate Crashing -> หาก Fast Tracking ไม่ได้ ต้องเพิ่มงบเร่งงานตรงจุดใดจึงคุ้มที่สุด?
        - ประเมินค่าใช้จ่ายต่อวันที่ประหยัดได้ (Cost per Day Saved)
```

---

## 9. Reflection & Assessment

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการของคุณ คุณทราบหรือไม่ว่ากิจกรรมใดบ้างที่จัดเป็น **Critical Path** ที่ห้ามล่าช้าเด็ดขาด?
2. คุณเคยใช้เทคนิค **Crashing** หรือ **Fast Tracking** ในการกู้คืนตารางเวลาหรือไม่ และได้ผลลัพธ์อย่างไร?

---

## 🌉 Bridge to Next Lesson: Lesson 09 — Project Cost Management and Earned Value

เมื่อเรามี **Schedule Baseline** ที่ระบุตารางเวลาของทุกกิจกรรมเรียบร้อยแล้ว ขั้นตอนถัดไปคือการคำนวณค่าใช้จ่ายและกำหนด **Cost Baseline** รวมไปถึงการวัดผลความก้าวหน้าด้วย **Earned Value Management (EVM)** ในบทถัดไป **Lesson 09** ครับ!

## PM Decision Thinking

**[PMBOK 6]** Schedule Management ครอบคลุม plan, define, sequence, estimate, develop และ control schedule. **[PMBOK 7]** delivery cadence และ uncertainty ทำให้ PM ต้องใช้ schedule เป็น decision model ไม่ใช่แค่ภาพ Gantt chart.

| Field | Lesson 08 Application |
|---|---|
| Decision | ความล่าช้านี้ต้อง recover, replan, accept หรือ escalate |
| Owner | PM วิเคราะห์ schedule impact; sponsor/change authority ตัดสินเมื่อกระทบ milestone หรือ baseline |
| Inputs | WBS, activity list, dependency, duration estimate, critical path, float, resource availability, risk |
| Options | resequence, use float, crashing, fast tracking, reduce scope, rebaseline |
| Trade-offs | cost vs time, risk vs speed, quality vs compression, team burnout vs deadline |
| Risk | ติดตามงานทุกชิ้นเท่ากันจนพลาดกิจกรรม critical path |
| Evidence | network diagram, critical path, variance, forecast finish date, recovery cost |
| Next Action | ทำ schedule recovery brief และ update baseline หาก decision อนุมัติ |

### PM Insight

Schedule ที่ดีไม่ได้เริ่มจากวันที่สวย แต่เริ่มจาก logic ที่จริง. PM ต้องรู้ว่างานใดล่าช้าได้ งานใดล่าช้าไม่ได้ และการเร่งงานหนึ่งจุดทำให้ risk/quality/cost เปลี่ยนอย่างไร.

## ERP Scenario

**[Scenario]** ERP มี go-live target ก่อน 1 ตุลาคม. Data cleansing ล่าช้าและ data migration ต้องรอ data cleansing กับ configuration เสร็จก่อน.

Schedule decision:

- ถ้า data cleansing อยู่บน critical path ความล่าช้าจะกระทบ go-live โดยตรง
- Crashing อาจเพิ่มทีม data cleansing หรือ overtime แต่กระทบ working budget 45 ล้านบาท
- Fast tracking อาจเริ่ม migration rehearsal ด้วย sample data แต่เพิ่ม rework/quality risk
- Sponsor ต้องเห็น forecast ใหม่และ trade-off ก่อนอนุมัติ recovery plan

## Hotel Booking Scenario

**[Scenario]** Hotel Booking timeline 8 เดือน มี milestones เช่น payment integration, beta, launch และ post-launch stabilization.

Schedule decision:

- ถ้า payment integration delay อยู่บน path ไป beta และ launch ต้อง recover ทันที
- Fast tracking UX polish กับ payment testing อาจเสี่ยง rework
- Crashing ด้วย vendor support เพิ่มอาจคุ้มถ้า payment failure กระทบ conversion outcome
- ถ้า launch ใกล้ high season PM อาจเสนอ split release เพื่อรักษา critical value flow

## Real Enterprise Example

**[Instructor Interpretation]** หลายโครงการมี Gantt chart แต่ไม่มี schedule logic. เมื่อผู้บริหารถามว่า “เลื่อนแค่งานนี้ ทำไมวันจบเลื่อน” PM ตอบไม่ได้ เพราะไม่มี dependency และ critical path. Lesson 08 ต้องทำให้ผู้เรียนใช้ schedule เพื่ออธิบายเหตุและผล ไม่ใช่ใช้เป็นภาพประกอบรายงาน.

## Common Mistakes

1. ตั้งวันจบก่อนแล้วบีบกิจกรรมให้พอดีโดยไม่ดู dependency
2. ไม่รู้ critical path และติดตามงานที่ไม่ critical มากเกินไป
3. ใช้ crashing กับงานที่ไม่อยู่บน critical path
4. fast tracking โดยไม่คำนวณ rework และ quality risk
5. ไม่ update forecast เมื่อ actual progress เปลี่ยน

## Common Misconceptions

| Misconception | Correction |
|---|---|
| Gantt chart คือ schedule management | Gantt เป็น visualization; logic อยู่ที่ activities, dependencies และ critical path |
| งานล่าช้าทุกงานกระทบวันจบ | เฉพาะงานบน critical path หรือเกิน float จึงกระทบวันจบ |
| ใส่คนเพิ่มแก้ schedule ได้เสมอ | Crashing มี cost และ coordination limit |
| Fast tracking ฟรี | Fast tracking เพิ่ม rework, risk และ quality pressure |

## Interview Questions

### Definition

1. Critical path คืออะไร
2. Float ต่างจาก buffer อย่างไรในมุมการควบคุม schedule

### Judgement

1. ถ้างานล่าช้า 5 วันแต่ไม่อยู่บน critical path คุณจะรายงานอย่างไร
2. คุณจะเลือก crashing หรือ fast tracking เมื่อใด

### Behavioral

1. เล่าครั้งหนึ่งที่คุณต้อง recover schedule
2. คุณเคยสื่อสาร schedule delay กับ sponsor อย่างไรให้เห็น options ไม่ใช่ panic

### Scenario

1. ใน ERP หาก data cleansing delay คุณจะวิเคราะห์ critical path อย่างไร
2. ใน Hotel Booking หาก payment integration ช้า คุณจะรักษา launch readiness อย่างไร

## PM Dictionary

| Term | Meaning |
|---|---|
| Activity | งานย่อยที่ได้จาก work package และใช้วาง schedule |
| Dependency | ความสัมพันธ์ก่อน-หลังระหว่าง activities |
| Milestone | จุดสำคัญใน schedule ที่ใช้ควบคุม progress |
| Duration | ระยะเวลาที่กิจกรรมใช้ |
| Critical Path | เส้นทางกิจกรรมที่ยาวที่สุดและกำหนดวันจบเร็วสุด |
| Float/Slack | เวลาที่ยืดได้ก่อนกระทบงานถัดไปหรือวันจบ |
| Schedule Baseline | ตารางเวลาที่อนุมัติแล้วเพื่อใช้วัด performance |
| Crashing | เพิ่มทรัพยากรเพื่อย่นเวลา โดยเพิ่ม cost |
| Fast Tracking | ทำงานบางส่วนขนานกัน โดยเพิ่ม risk/rework |

## Workshop

### Scenario

ERP data cleansing delay 2 สัปดาห์ก่อน migration rehearsal. Hotel Booking payment integration delay ก่อน beta.

### Task

ให้ผู้เรียนทำ schedule recovery decision brief 1 หน้า:

1. activities และ dependencies ที่เกี่ยวข้อง
2. critical path หรือ float impact
3. options: use float, crashing, fast tracking, split release, rebaseline
4. cost/risk/quality trade-off
5. recommendation และ approval needed

### Debrief

คำตอบที่ดีต้องเริ่มจาก critical path ไม่ใช่เริ่มจากการใส่คนเพิ่มหรือเลื่อนวันทันที.

## Assessment

ดูแบบประเมินหลักที่ [Lesson 08 Assessment](./Lesson-08_3-Assessment.md). แบบประเมินควรวัด judgement เรื่อง critical path, recovery option และ trade-off มากกว่าการอ่าน Gantt chart อย่างเดียว.

## Executive Summary

Schedule Management คือการสร้างและควบคุม logic ของเวลา. WBS บอกว่าต้องทำอะไร ส่วน schedule บอกว่างานเหล่านั้นเรียงอย่างไร ใช้เวลาเท่าไร และจุดใดกำหนดวันจบจริง. PM ต้องใช้ schedule เพื่อคาดการณ์และตัดสินใจ ไม่ใช่แค่รายงานว่างานช้า.

## Lesson Connection

Lesson 07 สร้าง scope baseline และ WBS. Lesson 08 ใช้ WBS เพื่อสร้าง activity network และ schedule baseline. Lesson 09 จะต่อไปที่ cost baseline และ Earned Value เพื่อวัดว่าเวลาและเงินกำลังสร้าง value ตามแผนหรือไม่.

## AI Continuation Context

Future AI agents must keep Schedule Management grounded in WBS, dependencies, critical path, and recovery trade-offs. Use ERP data migration and Hotel Booking payment integration as recurring schedule-risk examples.

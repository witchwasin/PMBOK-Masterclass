---
lesson: 8
sequence: 8.2
title: Project Schedule Management
document_type: Lesson
level: Core
status: Active
prerequisite:
  - Lesson 07 — Project Scope Management and WBS
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 08_2 — Project Schedule Management

## 1. คำถามเปิดบท: ทำไมโครงการส่วนใหญ่จึงล่าช้ากว่ากำหนด ทั้งที่มีการวาดแผนตารางเวลา (Gantt Chart) ไว้อย่างสวยงาม?

ลองพิจารณาปรากฏการณ์ที่พบได้บ่อยในองค์กร:

> ในวัน Kickoff โครงการ PM นำเสนอ Gantt Chart ความยาว 50 หน้าที่กำหนดวันเสร็จของทุกกิจกรรมไว้อย่างลงตัว แต่เมื่อเริ่มทำงานจริงได้เพียง 2 สัปดาห์ แผนงานกลับล่าช้าทันที และสุดท้ายวัน Go-live ก็ต้องเลื่อนออกไปหลายเดือน

เหตุใดตารางเวลาที่ดูสมบูรณ์แบบบนหน้ากระดาษ จึงพังทลายลงอย่างรวดเร็วในชีวิตจริง?

> **คำถามสำคัญคือ:** การบริหารตารางเวลา (Schedule Management) คือการ "ใส่วันที่ลงในปฏิทิน" เพียงอย่างเดียว หรือคือการวิเคราะห์ลำดับความเชื่อมโยงเชิงวิศวกรรม (Dependencies) และการบริหารสายงานวิกฤต (Critical Path)?

---

## 2. ปัญหาที่ต้องทำความเข้าใจ: การวางตารางเวลาแบบไม่มีตรรกะเชื่อมโยง

ปัญหาหลักที่ทำให้การบริหารเวลาล้มเหลว ได้แก่:

1. **การกำหนดวันที่แบบย้อนกลับ (Backward Scheduling Without Logic):**
   * ล็อควันจบโครงการตามใจผู้บริหาร แล้วจับงานทั้งหมดมาอัดลงในเวลาที่มี โดยไม่วิเคราะห์ความเชื่อมโยงและความเป็นไปได้จริง
2. **ละเลยการหา Critical Path (สายงานวิกฤต):**
   * ไม่รู้ว่ากิจกรรมใดล่าช้าไม่ได้เลยแม้แต่สัมผัสเดียว (Zero Float) และกิจกรรมใดพอยืดหยุ่นได้ ทำให้ PM โฟกัสติดตามงานผิดจุด
3. **การประมาณเวลาแบบโลกสวย (Optimistic Estimation):**
   * ประเมินเวลาทำงานโดยสมมติว่าไม่มีอุปสรรคใด ๆ เกิดขึ้นเลย และลืมคิดเผื่อระยะเวลาในการรอคอย (Lag Time) หรือการส่งมอบข้ามทีม

---

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

อ้างอิงจาก [references/PMBOK-Overview.md](file:///Users/arm/Documents/GitHub/PMBOK-Masterclass/references/PMBOK-Overview.md):

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

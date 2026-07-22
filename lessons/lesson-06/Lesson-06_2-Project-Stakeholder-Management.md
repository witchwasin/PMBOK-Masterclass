---
lesson: 6
sequence: 6.2
title: Project Stakeholder Management
document_type: Lesson
level: Core
status: Active
prerequisite:
  - Lesson 05 — Project Integration Management
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 06_2 — Project Stakeholder Management

## 1. คำถามเปิดบท: ถ้าส่งมอบระบบได้ตามสเปค แต่ผู้บริหารฝ่ายปฏิบัติการไม่ยอมให้พนักงานเข้าใช้อุปกรณ์ โครงการนี้ถือว่าสำเร็จหรือไม่?

ลองพิจารณาเหตุการณ์จริงที่มักเกิดขึ้นในหลายองค์กร:

> ทีมพัฒนาซอฟต์แวร์สามารถส่งมอบระบบบริหารคลังสินค้าใหม่ได้ตรงเวลา 100% แต่เมื่อถึงวัน Go-live ผู้จัดการฝ่ายคลังสินค้ากลับปฏิเสธไม่ให้พนักงานสแกนบาร์โค้ดผ่านระบบใหม่ โดยอ้างว่า "กระบวนการใหม่ทำให้งานช้าลง และไม่มีใครเคยเข้ามาถามความต้องการของคนหน้างานตั้งแต่แรก"

ในมิติเชิงเทคนิค ระบบทำงานได้ถูกต้องตามข้อกำหนด  
แต่ในมิติเชิงผู้คน โครงการนี้กำลังเผชิญหน้ากับ **"แรงต้านของผู้มีส่วนได้ส่วนเสีย" (Stakeholder Resistance)** ที่สามารถทำให้โครงการล้มเหลวลงทันที!

> **คำถามสำคัญคือ:** ผู้มีส่วนได้ส่วนเสีย (Stakeholders) คือใครบ้าง? และเหตุใดการบริหารคนกลุ่มนี้จึงไม่ใช่เรื่องของการ "เอาใจทุกคน" แต่เป็นการบริหารความคาดหวังและการมีส่วนร่วมอย่างมีกลยุทธ์?

---

## 2. ปัญหาที่ต้องทำความเข้าใจ: การบริหารคนแบบตั้งรับและการมองคนเพียงกลุ่มเดียว

ความผิดพลาดร้ายแรงเกี่ยวกับการบริหาร Stakeholder ในวิชาชีพ Project Management ได้แก่:

1. **มองว่า Stakeholder คือผู้บริหารระดับสูง (Sponsor) เท่านั้น:**
   * ละเลยกลุ่มผู้ใช้งานจริง (End Users), ฝ่ายปฏิบัติตามกฎระเบียบ (Compliance/Regulator), หรือคู่สัญญาภายนอก (Vendors) จนเกิดปัญหาในภายหลัง
2. **การบริหารแบบตั้งรับ (Reactive Management):**
   * รอให้เกิดความขัดแย้งหรือการต่อต้านก่อน แล้วค่อยเข้าไปแก้ไข แทนที่จะระบุและดึงเข้ามามีส่วนร่วมตั้งแต่ช่วงเริ่มต้น (Initiating Group)
3. **การพยายามทำให้ทุกคนพอใจ 100% (People-Pleasing Trait):**
   * ไม่เข้าใจว่า Stakeholders แต่ละกลุ่มมีเป้าหมายและอำนาจที่ขัดแย้งกัน การบริหารที่ถูกต้องคือการจัดระดับความสำคัญและการสื่อสารอย่างเหมาะสม

---

## 3. เหตุผลและที่มา: ผู้คนคือปัจจัยหลักที่กำหนดความล้มเหลวหรือสำเร็จ

เหตุใด **Project Stakeholder Management** จึงเป็นองค์ความรู้ที่สำคัญอย่างยิ่ง?

เพราะโครงการไม่ได้ดำเนินอยู่ในสุญญากาศ แต่ดำเนินอยู่ท่ามกลางมนุษย์ที่มีความคาดหวัง ผลประโยชน์ ความกลัว และอำนาจที่ต่างกัน

> **Core Rationale:**  
> **"โครงการเปลี่ยนกระบวนการ แต่ผู้คนเปลี่ยนผลลัพธ์"**  
> ไม่ว่าระบบหรือแผนงานจะสมบูรณ์แบบเพียงใด หากผู้มีส่วนได้ส่วนเสียไม่ยอมรับ ไม่ส่งมอบข้อมูล หรือปฏิเสธการนำไปใช้ โครงการก็ไม่สามารถสร้าง Business Value ได้จริง

---

## 4. Mental Model: ผัง Power-Interest Grid และกลยุทธ์การบริหาร 4 ทิศทาง

เพื่อสร้างกรอบความคิดที่คมชัด ให้ใช้ **Power-Interest Grid Matrix** ในการวิเคราะห์และจัดกลยุทธ์รับมือ Stakeholders:

```text
               High Power
                   │
                   │   [ Keep Satisfied ]    │   [ Manage Closely ]
                   │   (เอาใจใส่และดูแล)       │   (บริหารจัดการอย่างใกล้ชิด)
                   │                         │
  Power (อำนาจ)     │   - ผู้บริหารระดับสูงที่ไม่  │   - Project Sponsorหลัก
                   │     ได้คุมโครงการโดยตรง   │   - Head of Operations เจ้าของงาน
                   │                         │
   Low Power ──────┼─────────────────────────┼───────────────────────── High Power
                   │                         │
                   │   [ Monitor ]           │   [ Keep Informed ]
                   │   (เฝ้าติดตาม)            │   (แจ้งข่าวสารอย่างสม่ำเสมอ)
                   │                         │
                   │   - กลุ่มผู้ใช้ภายนอกทั่วไป  │   - End Users คนคีย์ข้อมูลหน้างาน
                   │   - สื่อมวลชน/สาธารณชน    │   - ทีมงาน Support เทคนิค
                   │                         │
                   └─────────────────────────┴─────────────────────────
                                          Interest (ความสนใจ)
```

---

## 5. คำศัพท์และ Framework (อ้างอิงจาก Canonical Source)

อ้างอิงจาก [references/PMBOK-Overview.md](file:///Users/arm/Documents/GitHub/PMBOK-Masterclass/references/PMBOK-Overview.md):

### 5.1 หมวดหมู่ของผู้มีส่วนได้ส่วนเสีย (Stakeholder Categories)
1. **Internal Stakeholders:** Project Sponsor, คณะกรรมการบริหารโครงการ (Steering Committee), คณะทำงานอำนวยการ, คณะทำงานโครงการ, PM
2. **External Stakeholders & Users:** คณะกรรมการตรวจรับพัสดุ, หน่วยงานผู้ใช้ระบบ, บริษัทคู่สัญญา/Vendor, กลุ่มผู้ใช้งานภายใน/ภายนอกองค์กร, ลูกค้า (Customer)
3. **Compliance / Regulator:** หน่วยงานกำกับดูแลตามกฎหมาย, ฝ่ายตรวจสอบภายใน (Audit), ฝ่ายกฎหมาย
4. **Business & System Owners:** เจ้าของระบบธุรกิจ (Business Owner), เจ้าของระบบ IT เดิม (System Owner)

### 5.2 4 Sub-processes ของ Stakeholder Management
1. **Identify Stakeholders:** ระบุรายชื่อผู้เกี่ยวข้องทั้งหมดทั้งภายในและภายนอก (ได้ *Stakeholder Register*)
2. **Plan Stakeholder Engagement:** วางแผนกลยุทธ์การดึงผู้มีส่วนได้ส่วนเสียเข้ามามีส่วนร่วมตามระดับอำนาจและความสนใจ
3. **Manage Stakeholder Engagement:** สื่อสาร ปรับความคาดหวัง และแก้ไขข้อขัดแย้งระหว่างดำเนินโครงการ
4. **Monitor Stakeholder Engagement:** ติดตามความสัมพันธ์และปรับกลยุทธ์เมื่อระดับอำนาจหรือความสนใจของผู้เกี่ยวข้องเปลี่ยนไป

---

## 6. ตัวอย่างสถานการณ์จริง (Core Scenarios)

### 🏢 Core Scenario A: ERP Transformation (บริหารแรงต้านการเปลี่ยนแปลง)

- **วิเคราะห์ Stakeholder:**
  * *CFO & Sponsor (High Power, High Interest):* ต้องการรายงานการเงินที่เร็วขึ้น -> **Manage Closely** (ต้องรายงานความก้าวหน้าและขออนุมัติในจุดสำคัญ)
  * *ฝ่ายบัญชีหน้างาน (Low Power, High Interest):* กังวลว่า ERP ใหม่จะทำให้คีย์งานยากขึ้น -> **Keep Informed & Engage** (ดึงมาร่วมทำ UAT และจัดอบรมอย่างเข้มข้น)
  * *ฝ่าย IT ระบบเดิม (High Power, Low Interest):* กังวลเรื่องการโดนลดบทบาท -> **Keep Satisfied** (ดึงมาเป็นคณะทำงานเปลี่ยนผ่านข้อมูล เพื่อสร้าง Ownership)

### 🏨 Core Scenario B: Hotel Booking Digital Platform (บริหารความคาดหวังคู่ค้า)

- **วิเคราะห์ Stakeholder:**
  * *โรงแรมคู่ค้า / Partner Hotels (High Power, High Interest):* กังวลเรื่องค่าคอมมิชชันและระบบตัดสต็อกห้องพัก -> **Manage Closely** (ต้องจัดประชุมร่วม และมีระบบ Back Office ที่ใช้งานง่าย)
  * *นักท่องเที่ยว / App Users (Low Power, High Interest):* ต้องการจองห้องพักชำระเงินได้รวดเร็ว -> **Keep Informed** (ทดสอบ UX/UI และแจ้งสื่อสารโปรโมชัน)

---

## 7. ความเข้าใจผิดที่พบบ่อย (Misconceptions to Correct)

1. **" Stakeholders หมายถึงเฉพาะเจ้านายหรือ Sponsor เท่านั้น":**
   * *ความจริง:* Stakeholder คือทุกคนที่ได้รับผลกระทบทั้งเชิงบวกและเชิงลบ รวมไปถึงผู้ใช้หน้างานและ Vendor
2. **"การบริหาร Stakeholders คือการปฏิบัติต่อทุกคนเท่ากันหมด":**
   * *ความจริง:* ทรัพยากรและเวลามีจำกัด PM ต้องใช้ Power-Interest Grid จัดสรรระดับการดูแลให้เหมาะสม
3. **"เมื่อทำ Stakeholder Register วันแรกเสร็จแล้ว ถือว่างานจบ":**
   * *ความจริง:* อำนาจและความสนใจของคนเปลี่ยนได้ตลอดเวลา (เช่น คนเคย Low Power อาจได้เลื่อนตำแหน่งเป็น High Power) PM ต้องทำ Monitor Engagement อย่างต่อเนื่อง

---

## 8. PM Thinking & Decision Making

เมื่อเกิดความขัดแย้งระหว่าง Stakeholders ให้ PM ใช้ **Stakeholder Alignment Steps**:

```text
Step 1: Map Positions -> ใครต้องการอะไร และทำไมเขาจึงต้องการเช่นนั้น? (Identify Underlying Need)
Step 2: Check Power/Interest -> เขามีผลกระทบต่อความสำเร็จของโครงการระดับใด? (Power Grid)
Step 3: Find Common Ground -> วัตถุประสงค์ใดใน Business Case ที่ทุกฝ่ายเห็นตรงกัน?
Step 4: Execute Engagement Plan -> สื่อสารผ่านช่องทางและรูปแบบที่เหมาะกับ Stakeholder กลุ่มนั้น
```

---

## 9. Reflection & Assessment

### 📝 คำถามทบทวนตัวเอง (Self-Reflection):
1. ในโครงการปัจจุบัน คุณได้จัดทำ **Stakeholder Register** และวิเคราะห์ Power-Interest Grid ไว้แล้วหรือยัง?
2. มี Stakeholder กลุ่มใดหรือไม่ที่คุณมองข้ามไปในวันแรก แล้วส่งผลกลับมารบกวนโครงการในวันนี้?

---

## 🌉 Bridge to Next Lesson: Lesson 07 — Project Scope Management and WBS

เมื่อเราบริหารความคาดหวังของผู้คน (**Stakeholders**) ได้แล้ว ขั้นตอนถัดไปคือการแปลงความคาดหวังเหล่านั้นให้กลายเป็น **"ขอบเขตงานที่ชัดเจน" (Project Scope & WBS)** ในบทถัดไป **Lesson 07** ครับ!

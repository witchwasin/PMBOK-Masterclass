---
lesson: 2
sequence: 2.2
title: Project Management Overview
document_type: Lesson
level: Foundation
status: Draft
prerequisite:
  - Lesson 01 — ทำไม Project Manager ต้องรู้ PMBOK
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 02_2 — Project Management Overview

## ก่อนเริ่ม: งานทุกอย่างที่มีวันเริ่มต้นและวันสิ้นสุด เป็น Project หรือไม่?

ลองพิจารณางานต่อไปนี้:

- ปิดบัญชีประจำเดือน
- ออกรายงานยอดขายทุกวัน
- ดูแล Booking ของโรงแรม
- แก้ Incident ที่ลูกค้าแจ้งเข้ามา
- พัฒนา Mobile App ใหม่
- เปลี่ยนระบบ ERP ทั้งองค์กร
- จัดงานสัมมนาหนึ่งครั้ง
- เปิดสาขาใหม่
- ปรับหน้า Landing Page เพื่อทดลองเพิ่ม Conversion

งานเหล่านี้บางงานเป็น Project บางงานเป็น Routine Work และบางงานอาจมีทั้งส่วนที่เป็น Project กับส่วนที่เป็น Operation อยู่พร้อมกัน

คำถามสำคัญจึงไม่ใช่เพียงว่า:

> “งานนี้มีวันเริ่มและวันจบหรือไม่?”

แต่ต้องถามว่า:

> “งานนี้ถูกตั้งขึ้นชั่วคราวเพื่อสร้างผลิตภัณฑ์ บริการ ผลลัพธ์ หรือการเปลี่ยนแปลงที่มีความเฉพาะตัวหรือไม่?”

นี่คือจุดเริ่มต้นของการเข้าใจ Project Management อย่างแท้จริง

---

# 1. Project คืออะไร

โดยแก่นสำคัญ Project มีคุณสมบัติหลักสองอย่าง:

1. **Temporary** — มีจุดเริ่มต้นและจุดสิ้นสุด
2. **Unique** — สร้างผลิตภัณฑ์ บริการ ผลลัพธ์ หรือการเปลี่ยนแปลงที่มีความเฉพาะตัว

คำว่า Temporary ไม่ได้หมายความว่าโครงการต้องสั้น

โครงการอาจใช้เวลา:

- 2 สัปดาห์
- 6 เดือน
- 3 ปี
- หรือมากกว่านั้น

ตราบใดที่มันมีเหตุผลให้เริ่ม และมีเงื่อนไขให้จบ มันก็ยังเป็น Temporary

คำว่า Unique ก็ไม่ได้หมายความว่าไม่เคยมีใครในโลกทำมาก่อน

องค์กรอาจติดตั้ง ERP ที่มีหลายบริษัทใช้แล้ว แต่สำหรับองค์กรนั้น การออกแบบ Process, Data, Integration, Governance และการเปลี่ยนแปลงผู้ใช้ยังมีความเฉพาะตัว

โรงแรมอาจสร้าง Mobile App จองห้องเหมือนคู่แข่ง แต่ Customer Journey, Brand, Pricing, Inventory, Payment, Operation และกลุ่มลูกค้ายังต่างกัน

ดังนั้น Unique หมายถึง:

> มีองค์ประกอบ บริบท หรือผลลัพธ์ที่ต้องออกแบบเฉพาะ ไม่ใช่งานที่ทำซ้ำแบบเดิมอย่างต่อเนื่อง

---

# 2. Project vs Routine Work

## 2.1 ความแตกต่างเชิงพื้นฐาน

| มิติ | Project | Routine Work / Operation |
|---|---|---|
| วัตถุประสงค์ | สร้างสิ่งใหม่หรือการเปลี่ยนแปลง | รักษาและดำเนินสิ่งที่มีอยู่ |
| ระยะเวลา | มีจุดเริ่มต้นและจุดสิ้นสุด | ดำเนินต่อเนื่อง |
| ผลลัพธ์ | มีความเฉพาะตัว | เกิดซ้ำตามรูปแบบ |
| ทีม | มักข้ามสายงาน | มักอยู่ในโครงสร้างประจำ |
| ความไม่แน่นอน | สูงกว่า | ต่ำกว่าและคาดการณ์ได้มากกว่า |
| การวัดผล | วัดตาม Objective, Deliverable, Outcome | วัดตาม SLA, Efficiency, Quality, Throughput |
| การสิ้นสุด | ปิดเมื่อเป้าหมายสำเร็จหรือถูกยกเลิก | ไม่มีจุดจบตราบใดที่ธุรกิจยังดำเนินอยู่ |

---

## 2.2 ตัวอย่าง ERP

### Operation

- เปิด Invoice ทุกวัน
- ปิดบัญชีทุกเดือน
- ดูแล User Access
- Backup ระบบ
- แก้ Incident
- จัดทำรายงานประจำ

### Project

- เปลี่ยนระบบบัญชีเดิมเป็น ERP
- ย้ายข้อมูลจาก Legacy System
- ปรับ Chart of Accounts
- เชื่อม ERP กับระบบคลัง
- ออกแบบ Process ใหม่
- Training ผู้ใช้ทั้งองค์กร
- Go-live และ Transition to Support

เมื่อ ERP เปิดใช้งานแล้ว งานของโครงการจะค่อย ๆ จบลง แต่การใช้งาน ดูแล และปรับปรุงระบบจะเข้าสู่ Operation

---

## 2.3 ตัวอย่าง Hotel Booking Platform

### Project

- ออกแบบ Mobile App
- พัฒนา Customer Web App
- สร้าง Landing Page
- สร้าง Back Office Web Application
- เชื่อม Payment Gateway
- เชื่อม Room Inventory
- ทดสอบ Booking Flow
- เปิดตัวระบบ

### Operation

- ดูแล Booking รายวัน
- ปรับราคาและ Promotion
- ตอบลูกค้า
- ตรวจ Payment
- แก้ Incident
- ดูแล Content โรงแรม
- Monitor Conversion
- Support Partner Hotel

แต่ในโลก Digital Product เส้นแบ่งอาจไม่คมชัด

หลังเปิดตัว องค์กรอาจตั้ง “โครงการ Phase 2” เพื่อเพิ่ม Loyalty Program หรือ Dynamic Pricing ขณะที่ทีม Product ยังคงดูแล Operation และ Improvement ต่อเนื่อง

นี่คือเหตุผลที่ PM ต้องเข้าใจทั้ง Project และ Product/Operation Boundary

---

# 3. งานเล็กก็เป็น Project ได้

คนจำนวนมากเข้าใจว่า Project ต้อง:

- งบสูง
- ทีมใหญ่
- มี Steering Committee
- มี Vendor
- ใช้เวลาหลายเดือน

แต่ความจริง งานเล็กก็เป็น Project ได้ ถ้ามันมี Temporary และ Unique

ตัวอย่าง:

- ย้าย Office ภายใน 2 สัปดาห์
- จัดงานเปิดตัวสินค้า
- ทำ Campaign พิเศษ
- ออกแบบ Landing Page สำหรับตลาดใหม่
- ทำ Pilot AI Chatbot
- ทำ Training Program ครั้งแรก

ในทางกลับกัน งานใหญ่ก็อาจไม่ใช่ Project หากมันเป็น Operation ต่อเนื่อง เช่น ศูนย์บริการลูกค้าขนาดใหญ่ที่รับสายทุกวัน

ดังนั้น:

> ขนาดไม่ใช่ตัวตัดสินว่าเป็น Project หรือไม่ ธรรมชาติของงานต่างหากที่เป็นตัวตัดสิน

---

# 4. Project Management คืออะไร

Project Management คือการประยุกต์ใช้:

- ความรู้
- ทักษะ
- เครื่องมือ
- เทคนิค
- การตัดสินใจ
- การประสานงาน
- การบริหารผู้คน

เพื่อให้กิจกรรมของโครงการบรรลุวัตถุประสงค์

แต่หากอธิบายเพียงเท่านี้ ผู้เรียนอาจยังเห็น PM เป็นคน “ทำให้โครงการเสร็จ”

จึงต้องขยายอีกขั้นว่า Project Management คือ:

> กลไกที่เชื่อม Business Need ไปสู่ Business Value ผ่านการสร้างและส่งมอบการเปลี่ยนแปลงอย่างมีระบบ

---

# 5. จาก Business Need ไปสู่ Business Value

ลองใช้เส้นทางนี้:

```text
Business Need
→ Business Case
→ Project
→ Work
→ Output
→ Outcome
→ Benefit
→ Business Value
→ Transition to Operation
```

## 5.1 Business Need

องค์กรมีปัญหาหรือโอกาสอะไร

ตัวอย่าง ERP:

- ข้อมูลไม่ตรงกัน
- ปิดบัญชีช้า
- งานซ้ำ
- ควบคุมต้นทุนยาก

ตัวอย่าง Hotel Booking:

- พึ่ง OTA มากเกินไป
- ค่าคอมมิชชันสูง
- ไม่มีข้อมูลลูกค้าโดยตรง
- ลูกค้าจองยาก
- Booking กระจายหลายช่องทาง

---

## 5.2 Business Case

เหตุใดองค์กรจึงควรลงทุน

Business Case ที่ดีควรช่วยตอบ:

- ปัญหาคืออะไร
- โอกาสคืออะไร
- ทางเลือกมีอะไร
- ลงทุนเท่าไร
- คาดหวัง Benefit อะไร
- ความเสี่ยงสำคัญคืออะไร
- หากไม่ทำจะเกิดอะไร

Business Case ไม่ใช่เพียงเอกสารเพื่อขออนุมัติ แต่คือเหตุผลเชิงธุรกิจของการมี Project

---

## 5.3 Project

เมื่อองค์กรตัดสินใจลงทุน Project จะถูกตั้งขึ้นเพื่อสร้างการเปลี่ยนแปลง

Project มี:

- Objective
- Scope
- Timeline
- Budget
- Team
- Stakeholder
- Deliverable
- Risk
- Governance

---

## 5.4 Work

ทีมดำเนินกิจกรรมต่าง ๆ เช่น:

- วิเคราะห์
- ออกแบบ
- พัฒนา
- ทดสอบ
- Training
- Migration
- Deployment
- Communication
- Change Management

---

## 5.5 Output

Output คือสิ่งที่โครงการสร้างหรือส่งมอบ

ตัวอย่าง:

- ระบบ ERP
- Mobile App
- Web App
- Landing Page
- Back Office
- รายงาน
- คู่มือ
- Process ใหม่
- Training Course

Output เป็นสิ่งที่จับต้อง ตรวจสอบ หรือรับมอบได้

แต่ Output ยังไม่ใช่ความสำเร็จขั้นสุดท้าย

---

## 5.6 Outcome

Outcome คือการเปลี่ยนแปลงที่เกิดขึ้นเมื่อ Output ถูกนำไปใช้

ตัวอย่าง ERP:

- พนักงานใช้ Process ใหม่
- ข้อมูลสอดคล้องกัน
- ปิดบัญชีเร็วขึ้น
- ลดงาน Manual

ตัวอย่าง Hotel Booking:

- ลูกค้าจองเองได้
- Conversion สูงขึ้น
- พนักงานจัดการ Booking เร็วขึ้น
- ลด Overbooking
- ลดงานผ่านโทรศัพท์

Outcome เป็นสิ่งที่เกิดกับ:

- พฤติกรรม
- Process
- Performance
- Customer Experience
- Operation

---

## 5.7 Benefit

Benefit คือผลประโยชน์ที่วัดได้

ตัวอย่าง:

- ลดเวลาปิดบัญชีจาก 10 วันเหลือ 4 วัน
- ลดงาน Manual 30%
- เพิ่ม Direct Booking 20%
- ลดค่าคอมมิชชัน OTA
- ลด Error Rate
- เพิ่ม Customer Satisfaction

Benefit ต้องเชื่อมกับ KPI หรือ Business Metric

---

## 5.8 Business Value

Business Value คือคุณค่าที่องค์กรได้รับในระดับกลยุทธ์ เช่น:

- เพิ่มรายได้
- ลดต้นทุน
- ลดความเสี่ยง
- เพิ่มความสามารถในการแข่งขัน
- เพิ่มความเร็วในการตัดสินใจ
- สร้างฐานข้อมูลลูกค้า
- รองรับการเติบโต

---

## 5.9 Transition to Operation

หลังโครงการส่งมอบ สิ่งที่สร้างขึ้นต้องมีเจ้าของต่อ

คำถามสำคัญ:

- ใครดูแลระบบ
- ใครรับ Incident
- ใครแก้ Bug
- ใครดูแล Data
- ใครวัด Outcome
- ใครบริหาร Benefit
- ใครจ่ายค่าใช้จ่ายประจำ
- ใครอนุมัติ Change หลัง Go-live

หาก Transition ไม่ดี Output อาจเสื่อมคุณค่าอย่างรวดเร็ว

---

# 6. Output ไม่เท่ากับ Outcome

นี่คือหนึ่งในแนวคิดสำคัญที่สุดของ Project Management

## 6.1 ERP

### Output

ระบบ ERP Go-live แล้ว

### Outcome ที่คาดหวัง

พนักงานใช้ Process ใหม่ ข้อมูลตรงกัน และลดงานซ้ำ

### สถานการณ์จริง

ระบบเปิดแล้ว แต่พนักงาน Export ข้อมูลกลับไปทำ Excel

คำถาม:

> Output สำเร็จหรือไม่?

ใช่

> Outcome สำเร็จหรือไม่?

ยังไม่สำเร็จ

---

## 6.2 Hotel Booking

### Output

Mobile App, Web App, Landing Page และ Back Office เปิดใช้งานแล้ว

### Outcome ที่คาดหวัง

ลูกค้าจองง่ายขึ้น และโรงแรมจัดการ Booking ได้เร็วขึ้น

### สถานการณ์จริง

- App Crash ตอน Payment
- Landing Page คนเข้าเยอะ แต่ไม่กดจอง
- Back Office ใช้ยาก
- Inventory ไม่ Sync
- Booking Confirmation ช้า

Output อาจครบ แต่ Outcome ไม่เกิด

---

## 6.3 ทำไม PM ต้องสนใจ Outcome

มีคนอาจบอกว่า Outcome เป็นหน้าที่ Business Owner ไม่ใช่ PM

ความจริงคือความรับผิดชอบอาจแบ่งกัน แต่ PM ต้องเข้าใจ Outcome เพราะมันมีผลต่อ:

- Scope
- Acceptance
- Quality
- Stakeholder
- Change
- Training
- Transition
- Measurement

PM ที่ไม่รู้ Outcome จะวางแผนได้เพียง Deliverable แต่ไม่รู้ว่า Deliverable นั้นมีไว้ทำอะไร

---

# 7. Outcome มีหลายช่วงเวลา

Outcome ไม่ได้เกิดทั้งหมดในวัน Go-live

## Short-Term Outcome

ช่วง 1–3 เดือน

- ผู้ใช้เริ่มใช้งานได้
- ระบบทำงานตาม Process
- ทีม Support รับช่วงได้
- Error ลดลง

## Medium-Term Outcome

ช่วง 3–6 เดือน

- Process มีประสิทธิภาพขึ้น
- ทีมแก้ปัญหาได้เอง
- KPI เริ่มดีขึ้น
- Adoption มีเสถียรภาพ

## Long-Term Outcome

มากกว่า 6 เดือน

- ธุรกิจสร้าง Benefit เต็มรูปแบบ
- ผู้ใช้ถ่ายทอดความรู้ได้
- ระบบรองรับการเติบโต
- องค์กรใช้ข้อมูลตัดสินใจดีขึ้น

Project อาจปิดก่อน Long-Term Outcome เกิด ดังนั้นต้องกำหนด Ownership ให้ชัด

---

# 8. Project Manager ทำอะไรจริง

หลายองค์กรนิยาม PM ว่า:

- นัด Meeting
- ทำ Timeline
- ตามงาน
- Update Status
- ส่ง Report

สิ่งเหล่านี้จำเป็น แต่ยังไม่ใช่ภาพทั้งหมด

Project Manager ต้องทำหน้าที่:

- ทำให้เป้าหมายชัด
- เชื่อม Business กับทีมปฏิบัติ
- จัดการข้อจำกัด
- สร้าง Alignment
- มองความเสี่ยงล่วงหน้า
- ทำให้การตัดสินใจเกิดขึ้น
- บริหาร Trade-off
- ควบคุม Change
- สื่อสารให้ถูกคน ถูกเวลา
- ทำให้ Deliverable เชื่อมกับ Outcome
- เตรียม Transition
- รักษาความน่าเชื่อถือของโครงการ

---

# 9. Basic PM vs Professional PM

## 9.1 Basic PM

PM ระดับพื้นฐานควรทำได้:

- กำหนด Scope
- ระบุกิจกรรม
- จัดลำดับงาน
- ประมาณเวลา
- ประมาณต้นทุน
- มอบหมายงาน
- ติดตามความคืบหน้า
- ตรวจสอบ Deliverable
- ส่งมอบและปิดงาน

นี่คือความสามารถสำคัญและขาดไม่ได้

---

## 9.2 Professional PM

PM ระดับมืออาชีพต้องเพิ่มความสามารถ:

- เข้าใจ Business Strategy
- เข้าใจ Outcome และ Benefit
- อ่าน Stakeholder Dynamics
- ประเมิน Risk เชิงระบบ
- บริหาร Change
- ตัดสินใจภายใต้ความไม่แน่นอน
- สร้าง Trust
- จัดการ Conflict
- พัฒนาทีม
- สื่อสารกับผู้บริหาร
- Tailor วิธีบริหารให้เหมาะกับบริบท
- เชื่อม Project กับ Operation

ความต่างสำคัญคือ:

> Basic PM ทำให้แผนเดินได้ ส่วน Professional PM ทำให้โครงการสร้างคุณค่าได้

---

# 10. Key Success Factors ของโครงการ

เอกสารอ้างอิงระบุปัจจัยความสำเร็จ 11 ข้อ เราจะไม่ท่องจำเป็นรายการ แต่จะจัดกลุ่มเพื่อให้เข้าใจง่ายขึ้น

## 10.1 Direction

### Clear Statement of Requirement

วัตถุประสงค์และความต้องการชัด

แต่ “ชัด” ไม่ได้หมายถึงเขียนเยอะ

ชัดหมายถึง:

- ทุกฝ่ายเข้าใจตรงกัน
- เชื่อมกับ Business Need
- ตรวจสอบได้
- มี Boundary
- มี Acceptance

### Clear Vision & Objective

ทีมรู้ว่ากำลังสร้างอะไรและเพื่ออะไร

---

## 10.2 Leadership and Support

### Executive Management Support

ผู้บริหารต้อง:

- ให้ Direction
- ตัดสินใจเมื่อมี Conflict
- ปลดข้อจำกัด
- จัดทรัพยากร
- สนับสนุนการเปลี่ยนแปลง

การมีชื่อผู้บริหารใน Steering Committee ไม่เท่ากับมี Executive Support

### Ownership

ผู้เกี่ยวข้องต้องรู้สึกว่าโครงการเป็นของตน ไม่ใช่ “โครงการของ IT” หรือ “โครงการของ Vendor”

---

## 10.3 People

### User Involvement

ผู้ใช้ต้องเข้ามามีส่วนใน:

- Requirement
- Validation
- Testing
- Training
- Feedback
- Adoption

การเชิญผู้ใช้มา Meeting โดยไม่มีอำนาจตัดสินใจ ไม่ใช่ User Involvement ที่แท้จริง

### Competent Staff

ทีมต้องมีความสามารถที่เหมาะสม

### Hard-Working, Focused Team

ทีมต้องมี Focus และ Commitment

### Conflict Management

ความขัดแย้งเป็นเรื่องปกติ PM ต้องทำให้ Conflict กลายเป็นการตัดสินใจ ไม่ใช่ความสัมพันธ์ที่พัง

---

## 10.4 Planning and Control

### Proper Planning

วางแผนตามระดับความไม่แน่นอน

### Realistic Expectations

เวลา งบ Scope และคุณภาพต้องสมเหตุสมผล

### Small Project Milestone

แบ่งการติดตามเป็นช่วงย่อย เพื่อเห็นปัญหาเร็ว

---

# 11. ปัจจัยความสำเร็จไม่ได้ทำงานแยกกัน

ตัวอย่าง ERP:

- Requirement ชัด แต่ผู้ใช้ไม่เข้าร่วม → เสี่ยง
- ผู้ใช้เข้าร่วม แต่ผู้บริหารไม่ตัดสินใจ → ติด
- มีทีมเก่ง แต่ไม่มี Ownership → Adoption ต่ำ
- มีแผนดี แต่ Expectation ไม่จริง → ล้ม

ตัวอย่าง Hotel Booking:

- UX ดี แต่ Inventory ไม่ Sync → Booking ผิด
- Payment ดี แต่ Support ไม่พร้อม → ลูกค้าเสียความเชื่อมั่น
- App เสร็จเร็ว แต่ Value Proposition ไม่ชัด → ไม่มีคนใช้
- ทีมทำงานหนัก แต่ Product Decision ช้า → เสีย Momentum

โครงการสำเร็จจากระบบของปัจจัย ไม่ใช่ปัจจัยใดปัจจัยหนึ่ง

---

# 12. Organization Structure มีผลต่อ PM อย่างไร

Project Manager ไม่ได้ทำงานในสุญญากาศ

อำนาจ การเข้าถึงทรัพยากร ความเร็วในการตัดสินใจ และ Budget Control ขึ้นอยู่กับโครงสร้างองค์กร

---

## 12.1 Functional Organization

ทีมถูกจัดตามสายงาน เช่น:

- Finance
- HR
- IT
- Marketing
- Operation

PM อาจมีอำนาจน้อย และต้องขอทรัพยากรจาก Functional Manager

### ข้อดี

- ความเชี่ยวชาญชัด
- Career Path ชัด
- Resource ใช้ร่วมกันได้

### ข้อจำกัด

- Project Priority อาจแพ้งานประจำ
- การตัดสินใจข้ามฝ่ายช้า
- PM ต้องใช้ Influence มากกว่า Authority

### ERP Example

Finance, Warehouse และ IT อาจให้คนมาช่วยโครงการแบบ Part-time ทำให้ Workshop และ Testing เลื่อนบ่อย

---

## 12.2 Weak Matrix

PM มีบทบาทประสานงาน แต่ Functional Manager ยังควบคุม Resource และ Budget เป็นหลัก

PM ต้องเก่ง:

- Influence
- Negotiation
- Escalation
- Relationship

---

## 12.3 Balanced Matrix

PM และ Functional Manager แบ่งอำนาจกัน

ข้อดีคือสมดุลระหว่าง Project กับสายงาน

ข้อท้าทายคือทีมอาจมี “หัวหน้าสองคน”

PM ต้องทำให้ Priority และ Accountability ชัด

---

## 12.4 Strong Matrix

PM มีอำนาจมากขึ้น

- Resource พร้อมกว่า
- Budget Control มากขึ้น
- ทีมอาจ Full-time
- การตัดสินใจเร็วขึ้น

แต่ PM ต้องรับผิดชอบสูงขึ้นด้วย

---

## 12.5 Projectized Organization

ทีมถูกจัดเพื่อ Project โดยตรง

PM มีอำนาจสูงและ Resource Dedicated

### ข้อดี

- Focus สูง
- Decision เร็ว
- Ownership ชัด

### ข้อจำกัด

- Resource ซ้ำซ้อน
- หลัง Project จบ ทีมอาจไม่มี Home
- ความรู้เฉพาะสายงานอาจแยกตัว

---

# 13. ไม่มีโครงสร้างใดดีที่สุดเสมอ

Projectized ไม่ได้ดีกว่า Functional ในทุกกรณี

โครงสร้างที่เหมาะขึ้นอยู่กับ:

- ขนาดองค์กร
- จำนวนโครงการ
- ความสำคัญของงานประจำ
- ความเชี่ยวชาญ
- Governance
- Culture
- Resource Availability

PM มืออาชีพต้องไม่ถามเพียงว่า:

> “ฉันมีอำนาจแค่ไหน?”

แต่ถามว่า:

> “ในโครงสร้างนี้ ฉันต้องใช้กลไกใดเพื่อทำให้การตัดสินใจและการทำงานเกิดขึ้น?”

---

# 14. กรณีศึกษาแบบเต็ม: ERP Transformation

## 14.1 Business Need

ข้อมูลไม่ตรงกัน ปิดบัญชีช้า และควบคุม Stock ยาก

## 14.2 Project

เปลี่ยน Legacy Systems เป็น ERP กลาง

## 14.3 Output

- ERP Configuration
- Data Migration
- Integration
- Training
- SOP
- Go-live

## 14.4 Outcome

- ใช้ Process กลาง
- ลดงานซ้ำ
- ลด Error
- ปิดบัญชีเร็วขึ้น
- รายงานน่าเชื่อถือขึ้น

## 14.5 Operation

- Support
- Master Data
- User Access
- Incident
- Enhancement
- Monthly Closing

## 14.6 Project vs Routine

| กิจกรรม | ประเภท |
|---|---|
| ออกแบบ Process ใหม่ | Project |
| Migration ข้อมูล | Project |
| Go-live | Project |
| ปิดบัญชีทุกเดือน | Operation |
| เพิ่ม User Access | Operation |
| Phase 2 เพิ่ม Module | Project |

## 14.7 Key Success Factors

- Sponsor ตัดสินใจเมื่อฝ่ายต่าง ๆ ขัดแย้ง
- User เข้าร่วม Workshop
- Data Owner ชัด
- Timeline สมจริง
- Training เพียงพอ
- Transition to Support ชัด

## 14.8 Organization Challenge

ถ้าเป็น Matrix:

- User ยังมีงานประจำ
- Functional Manager ไม่ยอมปล่อย Resource
- Testing ล่าช้า
- PM ต้อง Escalate และเจรจา Priority

นี่คือเหตุผลที่ PM ต้องเข้าใจ Organization Structure

---

# 15. กรณีศึกษาแบบเต็ม: Hotel Booking Digital Platform

## 15.1 Business Need

ต้องการเพิ่ม Direct Booking ลดค่าคอมมิชชัน และสร้าง Customer Data

## 15.2 Project

พัฒนา:

- Mobile App
- Customer Web App
- Landing Page
- Back Office
- Booking Engine
- Payment
- Inventory Integration

## 15.3 Output

ระบบและช่องทางทั้งหมดเปิดใช้งาน

## 15.4 Outcome

- ลูกค้าจองง่ายขึ้น
- Conversion ดีขึ้น
- Staff จัดการ Booking เร็วขึ้น
- Inventory ถูกต้อง
- ลด Manual Work

## 15.5 Operation

- ดูแล Booking
- จัด Promotion
- Support ลูกค้า
- Onboard โรงแรม
- Monitor Funnel
- แก้ Incident
- ปรับ Product ต่อเนื่อง

## 15.6 Project vs Routine

| กิจกรรม | ประเภท |
|---|---|
| พัฒนา MVP | Project |
| เปิดตัวระบบ | Project |
| ดูแล Booking รายวัน | Operation |
| ปรับราคาโรงแรม | Operation |
| ทำ Phase 2 Loyalty | Project |
| A/B Test Landing Page | อาจเป็น Product Experiment หรือ Mini Project |

## 15.7 Key Success Factors

- Product Vision ชัด
- Inventory Source เชื่อถือได้
- Payment Flow เสถียร
- User Feedback เร็ว
- Operation พร้อม
- Partner Hotel มีส่วนร่วม
- KPI ชัด เช่น Conversion และ Direct Booking

## 15.8 Organization Challenge

ทีมอาจประกอบด้วย:

- Product
- UX/UI
- Mobile
- Web
- Backend
- Marketing
- Hotel Operation
- Finance
- Customer Support

PM ต้องเชื่อมหลายสายงาน และไม่สามารถพึ่ง Authority อย่างเดียว

---

# 16. ERP กับ Hotel Booking ต่างกันอย่างไร

| มิติ | ERP Transformation | Hotel Booking Platform |
|---|---|---|
| จุดเน้น | Internal Transformation | External Digital Product |
| ผู้ใช้ | พนักงาน | ลูกค้าและพนักงาน |
| Outcome | Process Efficiency | Booking and Experience |
| Risk | Data, Change, Governance | Payment, Inventory, UX |
| Operation | Support และ Process | Booking และ Customer Service |
| Adoption | บังคับใช้ได้บางส่วน | ลูกค้าเลือกไม่ใช้ได้ทันที |
| Success Metric | Closing Time, Error, Efficiency | Conversion, Direct Booking, Revenue |

ทั้งสองโครงการใช้แนวคิด Project Management เดียวกัน แต่ต้อง Tailor ต่างกัน

---

# 17. ความเข้าใจผิดที่พบบ่อย

## “Project คือ งานใหญ่”

ผิด เพราะงานเล็กก็เป็น Project ได้

## “งานมี Deadline จึงเป็น Project”

ไม่เสมอไป รายงานประจำเดือนมี Deadline แต่เป็น Routine

## “PM คือคนทำ Timeline”

Timeline เป็นเพียงส่วนหนึ่ง

## “Deliverable ครบคือสำเร็จ”

ยังต้องดู Outcome และ Value

## “Go-live คือจบ”

Go-live มักเป็นจุดเริ่มของ Adoption และ Operation

## “Outcome ไม่ใช่หน้าที่ PM”

PM อาจไม่ได้เป็นเจ้าของ Benefit ระยะยาว แต่ต้องเข้าใจและออกแบบ Project ให้รองรับ Outcome

## “PM ต้องมี Authority สูง”

ในหลายองค์กร PM ใช้ Influence มากกว่า Authority

## “Projectized ดีที่สุด”

ขึ้นอยู่กับบริบท

---

# 18. PM Thinking

## 18.1 อย่าเริ่มจากถามว่า “ต้องทำอะไร”

ให้เริ่มจาก:

> “ทำไปเพื่ออะไร?”

จากนั้นค่อยถาม:

- Output คืออะไร
- Outcome คืออะไร
- Benefit คืออะไร
- Value คืออะไร

---

## 18.2 อย่าวัดความสำเร็จจากสิ่งที่ควบคุมง่ายเท่านั้น

เวลาและงบวัดง่าย แต่ Adoption, Customer Behavior และ Business Benefit วัดยากกว่า

สิ่งที่วัดยากไม่ได้แปลว่าไม่สำคัญ

---

## 18.3 Project Manager ต้องมองทั้ง Project และหลัง Project

PM ต้องถามตั้งแต่ต้นว่า:

- ใครรับช่วงต่อ
- ใครวัด Outcome
- ใครเป็น Owner
- Support Model คืออะไร
- Benefit Review เมื่อไร

---

## 18.4 อำนาจของ PM ไม่ได้มาจากตำแหน่งอย่างเดียว

อำนาจมาจาก:

- ความน่าเชื่อถือ
- ข้อมูล
- ความชัดเจน
- ความสัมพันธ์
- การสื่อสาร
- การตัดสินใจ
- การ Escalate อย่างเหมาะสม

---

# 19. สรุปบทเรียน

Project คือความพยายามชั่วคราวเพื่อสร้างผลลัพธ์ที่มีความเฉพาะตัว

Routine Work หรือ Operation คือการทำงานต่อเนื่องเพื่อรักษาและดำเนินสิ่งที่มีอยู่

Project Management มีหน้าที่เชื่อม:

```text
Business Need
→ Project
→ Output
→ Outcome
→ Benefit
→ Business Value
→ Operation
```

Project Manager จึงไม่ได้มีหน้าที่เพียงทำให้ Deliverable เสร็จ แต่ต้องทำให้:

- เป้าหมายชัด
- ทีมทำงานร่วมกัน
- Risk ถูกจัดการ
- Stakeholder Align
- Transition พร้อม
- Outcome มีโอกาสเกิด

ปัจจัยความสำเร็จของโครงการไม่ได้อยู่ที่แผนอย่างเดียว แต่รวม:

- Requirement
- Vision
- Executive Support
- User Involvement
- Planning
- Realistic Expectation
- Milestone
- Competent Staff
- Ownership
- Focused Team
- Conflict Management

และสิ่งที่ PM ทำได้จริงยังขึ้นกับ Organization Structure

ประโยคที่ควรจำจากบทนี้คือ:

> **Project ไม่ได้มีคุณค่าเพราะมันเสร็จ แต่มีคุณค่าเมื่อสิ่งที่ส่งมอบสร้าง Outcome และ Business Value ได้จริง**

---

# 20. Reflection

1. งานปัจจุบันของคุณมีส่วนใดเป็น Project และส่วนใดเป็น Operation?
2. อะไรคือ Temporary และ Unique ของงานนั้น?
3. Business Need คืออะไร?
4. Output คืออะไร?
5. Outcome คืออะไร?
6. Benefit วัดอย่างไร?
7. ใครเป็นเจ้าของ Outcome หลัง Project ปิด?
8. Organization Structure ของคุณเป็นแบบใด?
9. คุณมี Authority จริงระดับไหน?
10. ปัจจัยความสำเร็จข้อใดอ่อนที่สุด?
11. ถ้า Deliverable ครบแต่ User ไม่ใช้ คุณจะรายงานสถานะอย่างไร?
12. คุณต้องปรับวิธีบริหารอย่างไรตามโครงสร้างองค์กร?

---

# 21. เชื่อมไปยัง Lesson 03

เมื่อเราเข้าใจแล้วว่า Project คืออะไร และ Project Management ต้องเชื่อมอะไรบ้าง คำถามถัดไปคือ:

> โครงการเดินทางผ่านช่วงใดบ้าง ตั้งแต่เริ่มต้น วางแผน ดำเนินงาน ติดตาม ไปจนถึงปิดโครงการ?

Lesson 03 จะเข้าสู่ภาพรวมของ **5 Project Management Process Groups** และความสัมพันธ์ระหว่าง Initiating, Planning, Executing, Monitoring & Controlling และ Closing

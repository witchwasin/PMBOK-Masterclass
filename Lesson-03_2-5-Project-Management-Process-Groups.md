---
lesson: 3
sequence: 3.2
title: 5 Project Management Process Groups
document_type: Lesson
level: Foundation
status: Draft
prerequisite:
  - Lesson 01 — ทำไม Project Manager ต้องรู้ PMBOK
  - Lesson 02 — Project Management Overview
canonical_source:
  - ../../references/PMBOK-Overview.md
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---

# Lesson 03_2 — 5 Project Management Process Groups

## ก่อนเริ่ม: ถ้าเริ่มทำงานแล้ว แต่ Scope ยังไม่ชัด เราควรทำอย่างไร?

ลองนึกถึงโครงการ ERP ที่เริ่ม Development ไปแล้ว แต่ระหว่าง Workshop พบว่า Finance กับ Warehouse เข้าใจ Process ไม่ตรงกัน

หรือโครงการ Hotel Booking ที่เริ่มพัฒนา Mobile App แล้ว แต่ Beta User บอกว่า Booking Flow ซับซ้อนเกินไป

คำถามคือ:

- ต้องหยุดโครงการหรือไม่?
- ต้องย้อนกลับไป Planning หรือไม่?
- ถือว่า Planning ล้มเหลวหรือไม่?
- หรือเป็นเรื่องปกติของการบริหารโครงการ?

คำตอบคือ:

> การบริหารโครงการที่ดีไม่ใช่การวางแผนครั้งเดียวแล้วเดินตามเส้นตรง แต่เป็นการวางแผน ทำงาน ตรวจสอบ เรียนรู้ และปรับอย่างมีระบบ

นี่คือเหตุผลที่เราต้องเข้าใจ 5 Project Management Process Groups

---

# 1. Process Groups คืออะไร

5 Process Groups คือกลุ่มของกิจกรรมการบริหารโครงการที่มีวัตถุประสงค์ต่างกัน ได้แก่:

1. Initiating
2. Planning
3. Executing
4. Monitoring & Controlling
5. Closing

สิ่งสำคัญคือคำว่า “Group”

มันไม่ได้แปลว่าแต่ละกลุ่มต้องเกิดเพียงครั้งเดียว หรือเกิดแบบเส้นตรงตายตัว

แต่ละกลุ่มอาจเกิด:

- หลายครั้ง
- หลายระดับ
- ในแต่ละ Phase
- ในแต่ละ Release
- ในแต่ละ Workstream
- หรือในแต่ละช่วงของ Project

ดังนั้น Process Groups ควรถูกมองเป็น “หน้าที่การบริหาร” มากกว่า “ขั้นตอนแบบห้ามย้อนกลับ”

---

# 2. ภาพรวม 5 Process Groups

```text
Initiating
    ↓
Planning
    ↓
Executing
    ↔
Monitoring & Controlling
    ↓
Closing
```

แต่ภาพในโลกจริงใกล้เคียงแบบนี้มากกว่า:

```text
Initiating
    ↓
Planning
    ↓
Executing ↔ Monitoring & Controlling
      ↑              ↓
      └──── Replanning ┘
    ↓
Closing
```

ระหว่าง Executing เราอาจพบข้อมูลใหม่

ข้อมูลใหม่ทำให้เราต้อง:

- ปรับแผน
- วิเคราะห์ผลกระทบ
- เปลี่ยนลำดับงาน
- เพิ่มทรัพยากร
- ลด Scope
- แก้ Risk Response
- หรือทบทวนเป้าหมาย

นี่ไม่ใช่ความล้มเหลวของ Project Management

นี่คือ Project Management

---

# 3. Initiating — เริ่มต้นอย่างมีสิทธิ์และมีเหตุผล

Initiating คือการทำให้โครงการมีเหตุผล มีเจ้าของ และได้รับอำนาจให้เริ่มอย่างเป็นทางการ

## 3.1 คำถามสำคัญของ Initiating

- ทำไมต้องทำโครงการนี้?
- ปัญหาหรือโอกาสคืออะไร?
- เป้าหมายคืออะไร?
- ใครเป็น Sponsor?
- ใครได้รับผลกระทบ?
- ขอบเขตระดับสูงคืออะไร?
- งบและเวลาระดับสูงคือเท่าไร?
- ความเสี่ยงหลักคืออะไร?
- ใครมีอำนาจอนุมัติ?
- PM มี Authority ระดับใด?

---

## 3.2 Key Outputs

### Project Charter

Project Charter ทำหน้าที่:

- ให้สิทธิ์โครงการเริ่ม
- แต่งตั้งหรือรับรอง PM
- กำหนดเป้าหมายระดับสูง
- กำหนด Scope ระดับสูง
- ระบุ Sponsor
- ระบุ Budget และ Timeline ระดับสูง
- ระบุ Success Criteria
- ระบุความเสี่ยงหลัก
- สร้าง Alignment เบื้องต้น

Charter ไม่ใช่ Project Plan แบบละเอียด

มันคือเอกสารหรือหลักฐานที่ตอบว่า:

> “ทำไมโครงการนี้จึงมีอยู่ และใครอนุญาตให้เดินหน้า?”

### Stakeholder Information

Initiating ยังต้องระบุผู้มีส่วนได้ส่วนเสียเบื้องต้น เช่น:

- Sponsor
- Business Owner
- User
- Vendor
- Regulator
- Operation
- Support Team
- Customer
- Partner

หากเริ่ม Project โดยไม่รู้ว่าใครได้รับผลกระทบ เรากำลังเริ่มด้วย Blind Spot

---

# 4. Initiating ไม่ใช่แค่ Kickoff Meeting

Kickoff เป็นกิจกรรมหนึ่ง แต่ไม่ใช่แก่นของ Initiating

โครงการอาจจัด Kickoff สวยมาก มี Slide มีผู้บริหารเปิดงาน แต่ถ้ายังไม่ชัดว่า:

- Objective คืออะไร
- Scope อยู่ตรงไหน
- Sponsor ตัดสินใจเรื่องใด
- Success วัดอย่างไร
- ใครเป็น Owner

โครงการยังไม่ได้ Initiate อย่างมีคุณภาพ

คำถามที่ดีกว่าคือ:

> หลัง Kickoff ทุกคนมีความเข้าใจและอำนาจในการเดินหน้าอย่างชัดเจนหรือยัง?

---

# 5. Planning — เปลี่ยนเป้าหมายให้เป็นแผนที่ทำได้จริง

Planning คือการแปลงเป้าหมายระดับสูงให้เป็นแนวทางดำเนินงานที่ทีมเข้าใจและใช้ตัดสินใจได้

Planning ไม่ใช่เพียงทำ Timeline

มันต้องเชื่อม:

- Scope
- Requirement
- Deliverable
- Schedule
- Cost
- Resource
- Quality
- Communication
- Risk
- Procurement
- Stakeholder
- Change
- Acceptance
- Transition

---

## 5.1 คำถามสำคัญของ Planning

- ต้องส่งมอบอะไร?
- อะไรไม่อยู่ใน Scope?
- งานต้องแตกอย่างไร?
- ใครทำอะไร?
- งานใดต้องทำก่อน?
- ใช้เวลาเท่าไร?
- ใช้งบเท่าไร?
- ต้องมีคุณภาพระดับใด?
- ความเสี่ยงคืออะไร?
- ใครต้องรับข้อมูลอะไร?
- Vendor เกี่ยวข้องอย่างไร?
- Change จะควบคุมอย่างไร?
- Acceptance วัดอย่างไร?
- Transition ไป Operation อย่างไร?

---

## 5.2 Key Outputs

ตามภาพรวมจากแหล่งอ้างอิง Planning อาจสร้าง:

- Project Management Plan
- Scope
- WBS
- Activity List
- Requirement
- Quality Approach
- Resource Roles
- Communication Plan
- Risk Plan
- Deliverable Definition
- Schedule
- Cost Estimate
- Procurement Plan
- Transition Plan

แผนที่ดีไม่จำเป็นต้องยาว

แต่ต้องเพียงพอต่อ:

- การตัดสินใจ
- การทำงาน
- การควบคุม
- การสื่อสาร
- การตรวจสอบ

---

# 6. Planning ไม่ได้เกิดครั้งเดียว

หนึ่งในความเข้าใจผิดที่อันตรายที่สุดคือ:

> “Planning เสร็จแล้ว ต่อไปห้ามเปลี่ยน”

ความจริงคือแผนเป็นสมมติฐานเกี่ยวกับอนาคต

เมื่อเราได้ข้อมูลใหม่ เราต้องทบทวนสมมติฐาน

ตัวอย่าง:

- Requirement ใหม่
- Vendor ล่าช้า
- Budget ถูกลด
- Risk เกิดจริง
- Technology ใช้ไม่ได้
- User Feedback เปลี่ยน
- Regulation เปลี่ยน
- Resource ไม่พร้อม

การ Replanning ไม่ได้แปลว่าแผนเดิมไร้คุณภาพเสมอไป

บางครั้งมันแปลว่าโครงการเรียนรู้เร็วพอที่จะไม่เดินผิดทางต่อ

---

# 7. Progressive Elaboration

โครงการจำนวนมากไม่สามารถรู้รายละเอียดทั้งหมดตั้งแต่วันแรก

เราจึงวางแผนแบบ:

- High-level ก่อน
- Detail เมื่อข้อมูลพร้อม
- ทบทวนเมื่อเรียนรู้เพิ่ม

นี่เรียกว่า Progressive Elaboration

ตัวอย่าง ERP:

- ตอนเริ่มรู้ว่าต้อง Migration Data
- ต่อมารู้ Table และ Mapping
- ต่อมาพบ Data Quality Issue
- จากนั้นปรับ Cleansing Plan

ตัวอย่าง Hotel Booking:

- ตอนเริ่มรู้ว่าต้องมี Booking Flow
- ต่อมาทำ Prototype
- ทดสอบกับ User
- พบว่าขั้นตอนยาว
- ปรับ Flow และ Priority

Progressive Elaboration ไม่ใช่ข้ออ้างให้ไม่วางแผน

มันคือการวางแผนตามระดับข้อมูลที่มีอย่างมีวินัย

---

# 8. Executing — ทำให้แผนกลายเป็นผลลัพธ์

Executing คือการดำเนินงานเพื่อสร้าง Deliverable และผลลัพธ์ตามที่วางแผน

คนจำนวนมากคิดว่า Executing คือทีม Technical ทำงาน

แต่จริง ๆ แล้วรวมถึง:

- ทำงานตามแผน
- ประสานทีม
- บริหารผู้คน
- สื่อสาร
- จัดการ Vendor
- สร้าง Deliverable
- จัด Training
- ทำ Quality Assurance
- Implement Risk Response
- Engage Stakeholder
- บริหารความรู้
- แก้ Issue
- ทำ Change ที่อนุมัติแล้ว

---

## 8.1 คำถามสำคัญของ Executing

- ทีมกำลังทำงานที่ถูกต้องหรือไม่?
- ทุกคนเข้าใจ Priority หรือไม่?
- Decision ติดที่ไหน?
- Issue ใดต้อง Escalate?
- Stakeholder ได้รับข้อมูลหรือไม่?
- Vendor ส่งมอบตามที่ตกลงหรือไม่?
- Quality ถูกสร้างเข้าไปในงานหรือไม่?
- Risk Response ถูกนำไปใช้หรือไม่?
- ทีมมี Resource เพียงพอหรือไม่?

---

## 8.2 Deliverable ไม่ได้เกิดจากการ “ตามงาน” อย่างเดียว

PM ที่ทำเพียงถามว่า:

- เสร็จหรือยัง?
- กี่เปอร์เซ็นต์?
- เมื่อไรเสร็จ?

อาจได้ Status แต่ไม่ได้ช่วยให้ Execution ดีขึ้น

PM ต้องช่วย:

- ทำให้ Decision เกิด
- แก้ Dependency
- ลด Blocker
- ทำให้ Owner ชัด
- จัดการ Conflict
- ปกป้อง Focus
- ทำให้ข้อมูลไหล
- เชื่อมทีมกับ Objective

---

# 9. Monitoring & Controlling — รู้ว่าเกิดอะไร และตัดสินใจอย่างไร

Monitoring & Controlling คือการเปรียบเทียบสิ่งที่เกิดขึ้นกับสิ่งที่ควรเกิด แล้วตัดสินใจตอบสนอง

มันไม่ใช่แค่ Status Report

## 9.1 Monitoring

คือการสังเกตและวัด เช่น:

- Progress
- Schedule
- Cost
- Scope
- Quality
- Risk
- Issue
- Change
- Stakeholder Engagement
- Deliverable Status
- Benefit Indicator

## 9.2 Controlling

คือการตัดสินใจและดำเนินการ เช่น:

- Corrective Action
- Preventive Action
- Defect Repair
- Change Request
- Replanning
- Escalation
- Scope Adjustment
- Resource Reallocation
- Risk Response Adjustment

ดังนั้น:

> Monitoring ทำให้รู้ว่าเกิดอะไรขึ้น  
> Controlling ทำให้โครงการตอบสนองอย่างมีระบบ

---

# 10. Executing และ Monitoring & Controlling เกิดพร้อมกัน

สองกลุ่มนี้ทำงานคู่กัน

ระหว่างทีมทำงาน เราต้อง:

- ตรวจคุณภาพ
- ดู Progress
- ตรวจ Risk
- ติดตาม Issue
- ดู Cost
- รับ Feedback
- วิเคราะห์ Change

ถ้าเรารอให้ Executing เสร็จก่อนแล้วค่อย Monitor เราจะพบปัญหาช้าเกินไป

ตัวอย่าง ERP:

- ระหว่าง Migration ต้องตรวจ Data Quality
- ระหว่าง SIT ต้องตรวจ Defect
- ระหว่าง Training ต้องตรวจ Readiness

ตัวอย่าง Hotel Booking:

- ระหว่าง Beta ต้องดู Conversion
- ระหว่าง Payment Test ต้องดู Failure
- ระหว่าง Load Test ต้องดู Performance
- ระหว่าง Partner Onboarding ต้องดู Inventory Accuracy

---

# 11. Change Control

โครงการไม่มีทางป้องกัน Change ทั้งหมด

เป้าหมายคือไม่ปล่อยให้ Change เกิดแบบไร้การตัดสินใจ

Flow พื้นฐาน:

```text
Request for Change
→ Impact Analysis
→ Approve or Deny
→ Implement
→ Review and Report
```

Impact ต้องพิจารณา:

- Scope
- Schedule
- Cost
- Quality
- Risk
- Resource
- Contract
- Benefit
- Operation

Change ที่ดีอาจเพิ่มคุณค่า

Change ที่ไม่ผ่านการวิเคราะห์อาจทำลายโครงการ

---

# 12. Closing — ปิดให้ครบ ไม่ใช่แค่หยุดทำ

Closing คือการทำให้โครงการหรือ Phase จบอย่างเป็นทางการ

## 12.1 คำถามสำคัญ

- Deliverable ถูกยอมรับหรือยัง?
- Acceptance ครบหรือยัง?
- Contract ปิดหรือยัง?
- Handover ครบหรือยัง?
- Support พร้อมหรือยัง?
- Outstanding Issue ใครรับต่อ?
- Lessons Learned ถูกเก็บหรือยัง?
- Budget ปิดหรือยัง?
- Resource ถูก Release หรือยัง?
- Outcome Owner ชัดหรือยัง?
- PIR หรือ Benefit Review จะเกิดเมื่อไร?

---

## 12.2 Key Outputs

- Formal Acceptance
- Project Handover
- Supporting Flow
- Lessons Learned
- Post-Implementation Review Plan
- Closure Report
- Contract Closure
- Resource Release
- Archive
- Outstanding Issue Ownership

---

# 13. Closing ไม่ใช่แค่เซ็นรับงาน

ถ้าลูกค้าเซ็นรับ แต่:

- Support ไม่รู้ระบบ
- User ไม่มีคู่มือ
- Data Owner ไม่ชัด
- Warranty Process ไม่ชัด
- Incident Flow ไม่พร้อม
- Outstanding Defect ไม่มี Owner

โครงการยังปิดไม่สมบูรณ์

Closing ที่ดีต้องทำให้การเปลี่ยนผ่านไม่สร้างสุญญากาศ

---

# 14. Process Groups ไม่เท่ากับ Project Phases

นี่คือประเด็นสำคัญมาก

## Process Groups

คือกลุ่มหน้าที่การบริหาร:

- Initiating
- Planning
- Executing
- Monitoring & Controlling
- Closing

## Project Phases

คือช่วงของ Lifecycle เช่น:

ERP:

- Analysis
- Design
- Build
- Test
- Deploy

Hotel Booking:

- Discovery
- MVP
- Beta
- Launch
- Stabilization

ในแต่ละ Phase อาจมี Process Groups ของตนเอง

ตัวอย่าง Beta Phase:

- Initiate Beta
- Plan Beta
- Execute Beta
- Monitor Feedback
- Close Beta

ดังนั้นอย่าแปล 5 Process Groups ว่าเป็น 5 Phases แบบตายตัว

---

# 15. ERP Transformation — Process Group Flow

## 15.1 Initiating

- Business Case
- Sponsor Approval
- Charter
- PM Appointment
- High-level Scope
- Stakeholder Identification

## 15.2 Planning

- Process Design Plan
- Data Migration Plan
- Integration Plan
- Testing Plan
- Training Plan
- Cutover Plan
- Risk Plan
- Communication Plan
- Vendor Plan

## 15.3 Executing

- Workshop
- Configuration
- Development
- Migration
- SIT
- UAT
- Training
- Change Management
- Deployment

## 15.4 Monitoring & Controlling

- Progress Review
- Defect Tracking
- Risk Review
- Change Control
- Cost Tracking
- Readiness Assessment
- Go-live Decision

## 15.5 Closing

- Formal Acceptance
- Handover to Support
- Warranty Flow
- Lessons Learned
- Closure Report
- PIR Schedule

---

# 16. Hotel Booking Platform — Process Group Flow

## 16.1 Initiating

- Product Vision
- Business Objective
- MVP Authorization
- Sponsor/Product Owner
- High-level Scope
- Stakeholder Map

## 16.2 Planning

- Customer Journey
- MVP Scope
- Release Plan
- UX Plan
- Architecture Plan
- Payment Plan
- Inventory Plan
- Test Plan
- Launch Plan
- Support Plan

## 16.3 Executing

- UX Design
- Mobile Development
- Web Development
- Back Office Development
- API Integration
- Content Preparation
- Partner Onboarding
- Testing
- Launch Campaign

## 16.4 Monitoring & Controlling

- Sprint/Release Progress
- Defect
- Conversion
- Payment Failure
- Performance
- Security
- Inventory Accuracy
- Change Priority
- Launch Readiness

## 16.5 Closing

- MVP Acceptance
- Production Handover
- Support Ownership
- Known Issue List
- Lessons Learned
- Phase 2 Backlog
- Post-launch Review

---

# 17. Agile ก็มี 5 Process Groups ได้หรือไม่?

ได้

Agile ไม่ได้ตัดการเริ่มต้น การวางแผน การทำงาน การติดตาม หรือการปิดออกไป

สิ่งที่ต่างคือ:

- Planning ถี่ขึ้น
- Feedback เร็วขึ้น
- Scope ยืดหยุ่นขึ้น
- Delivery เป็นรอบ
- Monitoring ต่อเนื่อง
- Closing อาจเกิดระดับ Sprint, Release หรือ Product Increment

ดังนั้นอย่าถามว่า Agile มี Process Groups หรือไม่

ให้ถามว่า:

> หน้าที่ของแต่ละ Process Group ถูกทำในจังหวะและรูปแบบใด?

---

# 18. Common Misconceptions

## “Initiating คือ Kickoff”

ไม่ใช่ Initiating ต้องสร้างเหตุผล อำนาจ และ Alignment

## “Planning ทำครั้งเดียว”

ไม่ใช่ Planning ต้องปรับตามข้อมูลและ Change

## “Executing คือ Dev ทำงาน”

ไม่ใช่ รวม People, Communication, Vendor, Quality และ Stakeholder

## “Monitoring คือทำ Report”

ไม่ใช่ ต้องวัด วิเคราะห์ และตัดสินใจ

## “Controlling คือควบคุมคน”

ไม่ใช่ คือควบคุมผลกระทบและรักษาเป้าหมาย

## “Closing คือเซ็นรับ”

ไม่ใช่ ต้อง Handover, Archive, Learn และ Release

## “Agile ไม่มี Planning”

ไม่จริง Agile วางแผนถี่และเป็นหลายระดับ

## “Change คือความล้มเหลว”

ไม่เสมอ Change อาจเป็นการเรียนรู้

---

# 19. PM Thinking

## 19.1 ทุก Process Group ต้องตอบคำถามบางอย่าง

### Initiating

ทำไมต้องทำ และใครอนุญาต?

### Planning

จะทำอย่างไรให้เป็นไปได้?

### Executing

ทำอย่างไรให้ Deliverable เกิด?

### Monitoring & Controlling

รู้ได้อย่างไรว่าไปถูกทาง และต้องปรับอะไร?

### Closing

จบอย่างไรให้คุณค่าเดินต่อ?

---

## 19.2 อย่าทำ Process เพื่อให้มี Process

ตัวอย่าง:

- Charter ที่ไม่มีใครใช้
- Plan ที่ไม่ Update
- Status Report ที่ไม่มี Decision
- Change Form ที่ใช้ขัดขวางทุก Change
- Lessons Learned ที่ไม่ถูกอ่าน

ทั้งหมดนี้คือ Process Theater

Process มีคุณค่าเมื่อช่วย:

- ตัดสินใจ
- ลดความเสี่ยง
- สื่อสาร
- สร้าง Ownership
- รักษา Outcome

---

## 19.3 Project Manager ต้องบริหารวงจร Feedback

วงจรที่สำคัญคือ:

```text
Plan
→ Execute
→ Observe
→ Learn
→ Decide
→ Adjust
```

นี่คือหัวใจที่เชื่อม Planning, Executing และ Monitoring & Controlling

---

# 20. สรุปบทเรียน

5 Process Groups คือ:

1. Initiating
2. Planning
3. Executing
4. Monitoring & Controlling
5. Closing

แต่ไม่ควรถูกเข้าใจเป็นเส้นตรงตายตัว

ความจริงคือ:

- Planning เกิดซ้ำ
- Executing กับ Monitoring เกิดคู่กัน
- Change ทำให้ Replanning
- Closing ต้องเตรียม Transition
- แต่ละ Phase อาจมี Process Groups ของตนเอง
- Agile ก็ยังต้องทำหน้าที่เหล่านี้

ประโยคที่ควรจำจากบทนี้คือ:

> **Process Groups ไม่ใช่บันไดที่เดินขึ้นทีละขั้นแล้วห้ามย้อนกลับ แต่เป็นวงจรบริหารที่ทำงานร่วมกันตลอดโครงการ**

---

# 21. Reflection

1. โครงการของคุณ Initiate อย่างเป็นทางการหรือไม่?
2. Charter มีไว้ใช้จริงหรือเป็นพิธีกรรม?
3. Planning ใดต้องทบทวนบ่อยที่สุด?
4. Executing ติด Blocker ที่ไหน?
5. Monitoring ปัจจุบันวัดแต่ Progress หรือวัด Outcome ด้วย?
6. Controlling มี Decision จริงหรือแค่ Report?
7. Change ถูกวิเคราะห์อย่างไร?
8. Closing มี Handover ครบหรือไม่?
9. Lessons Learned ถูกนำกลับมาใช้หรือไม่?
10. โครงการของคุณกำลังสับสน Process Groups กับ Phases หรือไม่?

---

# 22. เชื่อมไปยัง Lesson 04

เมื่อเข้าใจแล้วว่าโครงการไหลผ่าน 5 Process Groups อย่างไร คำถามถัดไปคือ:

> ในแต่ละ Process Group Project Manager ต้องบริหาร “เรื่องอะไรบ้าง” ให้ครบ?

Lesson 04 จะเข้าสู่ภาพรวมของ **10 Project Management Knowledge Areas** และอธิบายว่าทำไม Integration Management จึงเป็นกระดูกสันหลังของโครงการ

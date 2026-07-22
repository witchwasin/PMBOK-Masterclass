# PMBOK Masterclass

หลักสูตร Project Management ภาษาไทยที่ออกแบบให้ผู้เรียน **เข้าใจเหตุผล คิดเชื่อมโยง และนำไปใช้กับงานจริง** ไม่ใช่เพียงท่องจำคำศัพท์หรือกระบวนการจาก PMBOK

## แนวทางการสอน

1. เริ่มจากคำถามว่า **ทำไมต้องรู้เรื่องนี้**
2. อธิบายที่มาและปัญหาที่แนวคิดนั้นพยายามแก้
3. ค่อยขยายจาก Mental Model ไปสู่ศัพท์และ Framework
4. ใช้สถานการณ์จริงช่วยให้เห็นผลของการตัดสินใจ
5. แก้ความเข้าใจผิดที่พบบ่อย
6. ปิดด้วย Reflection และการประยุกต์ใช้

## Governance & Reference

- **Canonical Reference:** [`references/PMBOK-Overview.md`](references/PMBOK-Overview.md) (ทุกบทเรียนอ้างอิงจากเอกสารนี้)
- **Course Roadmap:** [`governance/COURSE-ROADMAP.md`](governance/COURSE-ROADMAP.md)
- **Content Rules:** [`governance/CONTENT-RULES.md`](governance/CONTENT-RULES.md)
- **Validation & Audit Guideline:** [`governance/REPOSITORY-VALIDATION-AND-FULL-REBUILD.md`](governance/REPOSITORY-VALIDATION-AND-FULL-REBUILD.md)

## Core Teaching Scenarios

### ERP Transformation

ใช้สอนบริบท Enterprise ได้แก่ Cross-functional Process, Data Migration, Integration, Governance, Vendor, Change Management, User Adoption และ Transition to Operation

### Hotel Booking Digital Platform

ระบบตัวอย่างประกอบด้วย Mobile App, Customer Web App, Landing Page และ Back Office Web Application สำหรับค้นหาโรงแรม ตรวจสอบห้องว่าง จอง ชำระเงิน ยืนยันการจอง และบริหารข้อมูลโรงแรม

ใช้สอน Customer Journey, UX, Conversion, Transaction Flow, Product Adoption, Payment Integration และ Business Value

รายละเอียดของทั้งสองกรณีศึกษาเป็นข้อสมมติเพื่อการเรียนรู้ เว้นแต่จะมี Requirement จริงกำหนดไว้ชัดเจน

## Structure

```text
PMBOK-Masterclass/
├── README.md
├── references/
│   └── PMBOK-Overview.md
├── governance/
│   ├── CONTENT-RULES.md
│   ├── COURSE-ROADMAP.md
│   └── REPOSITORY-VALIDATION-AND-FULL-REBUILD.md
└── lessons/
    ├── lesson-01/
    │   ├── Lesson-01_1-Blueprint.md
    │   └── Lesson-01_2-Why-PM-Must-Know-PMBOK.md
    ├── lesson-02/
    │   ├── Lesson-02_1-Blueprint.md
    │   ├── Lesson-02_2-Project-Management-Overview.md
    │   ├── Lesson-02_3-Assessment.md
    │   └── Lesson-02_4-Source-Mapping.md
    ├── lesson-03/
    ├── lesson-04/
    ├── ...
    └── lesson-16/
```

## Current Status

- Repository foundation: Complete Structure
- Lessons 01–16: Structured in `lessons/`

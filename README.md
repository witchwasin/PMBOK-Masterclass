# PMBOK Masterclass

หลักสูตร Project Management ภาษาไทยที่ออกแบบให้ผู้เรียน **เข้าใจเหตุผล คิดเชื่อมโยง และนำไปใช้กับงานจริง** ไม่ใช่เพียงท่องจำคำศัพท์หรือกระบวนการจาก PMBOK

## แนวทางการสอน

1. เริ่มจากคำถามว่า **ทำไมต้องรู้เรื่องนี้**
2. อธิบายที่มาและปัญหาที่แนวคิดนั้นพยายามแก้
3. ค่อยขยายจาก Mental Model ไปสู่ศัพท์และ Framework
4. ใช้สถานการณ์จริงช่วยให้เห็นผลของการตัดสินใจ
5. แก้ความเข้าใจผิดที่พบบ่อย
6. ปิดด้วย Reflection และการประยุกต์ใช้

หลักสูตรใช้วงจรฝึกปฏิบัติ:

```text
Beginner Safety → Learn → Watch PM Think → Watch Completed Artifact
→ Do → Checkpoint → Review → Approve → Handoff
```

## Governance & Reference

- **Canonical Reference:** [`references/PMBOK-Overview.md`](references/PMBOK-Overview.md) (ทุกบทเรียนอ้างอิงจากเอกสารนี้)
- **Course Roadmap:** [`governance/COURSE-ROADMAP.md`](governance/COURSE-ROADMAP.md)
- **Content Rules:** [`governance/CONTENT-RULES.md`](governance/CONTENT-RULES.md)
- **Course Standard:** [`governance/COURSE_STANDARD.md`](governance/COURSE_STANDARD.md)
- **Execution Baseline:** [`governance/EXECUTION-BASELINE.md`](governance/EXECUTION-BASELINE.md)
- **Artifact Dependency Map:** [`governance/ARTIFACT_DEPENDENCY_MAP.md`](governance/ARTIFACT_DEPENDENCY_MAP.md)

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
│   └── COURSE_STANDARD.md
└── lessons/
    ├── lesson-01/
    │   ├── Lesson-01_1-Blueprint.md
    │   ├── Lesson-01_2-Why-PM-Must-Know-PMBOK.md
    │   ├── learner/
    │   └── instructor/
    ├── lesson-02/
    │   ├── Lesson-02_1-Blueprint.md
    │   ├── Lesson-02_2-Project-Management-Overview.md
    │   ├── Lesson-02_3-Assessment.md
    │   └── Lesson-02_4-Source-Mapping.md
    ├── lesson-03/
    ├── lesson-04/
    ├── ...
    └── lesson-16/
└── e-Book/
    ├── chapters/            # บทเรียน 01–16 (learner / instructor / answer-key)
    ├── integration-reviews/
    ├── capstone/
    ├── pdf/                 # เล่มรวม Learner + Instructor (PDF) + build script
    └── release/             # แพ็กเกจ release สำหรับผู้เรียน
```

## Current Status

- Repository release: Active / Validated through Lessons 01–16 and Capstone
- Lessons 01–05: Active / Validated (Batch 1)
- Lessons 06–10: Active / Validated (Batch 2)
- Lessons 11–16: Active / Validated (Batch 3)
- Capstone: Active / Validated
- Batch 1 Validation: [`repository/BATCH-1-VALIDATION-REPORT.md`](repository/BATCH-1-VALIDATION-REPORT.md)
- Batch 2 Validation: [`repository/BATCH-2-VALIDATION-REPORT.md`](repository/BATCH-2-VALIDATION-REPORT.md)
- Batch 3 Validation: [`repository/BATCH-3-VALIDATION-REPORT.md`](repository/BATCH-3-VALIDATION-REPORT.md)
- e-Book: Released — Lessons 01–16 + Capstone รวมเล่ม พร้อม PDF (Learner + Instructor) และแพ็กเกจ release ดู [`e-Book/README.md`](e-Book/README.md) และ [`e-Book/release/RELEASE-MANIFEST.md`](e-Book/release/RELEASE-MANIFEST.md)

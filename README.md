# PMBOK Masterclass

หลักสูตร Project Management ภาษาไทยที่ออกแบบให้ผู้เรียน **เข้าใจเหตุผล คิดเชื่อมโยง และนำไปใช้กับงานจริง** ไม่ใช่เพียงท่องจำคำศัพท์หรือกระบวนการจาก PMBOK

> ⚠️ เอกสารชุดนี้เป็นสื่อการสอนที่เรียบเรียงขึ้นเอง (PMBOK-aligned) **ไม่ใช่เอกสารทางการของ PMI** และไม่ได้อ้างว่าครอบคลุมเนื้อหาสอบ PMP ครบถ้วน — PMBOK® และ PMP® เป็นเครื่องหมายการค้าของ Project Management Institute, Inc.

## เริ่มอ่านตรงไหน

| ถ้าคุณคือ | เริ่มที่ |
|---|---|
| อยากอ่านรวดเดียวจบ แบบ PDF | [PM Delivery Guide — Learner Edition](field-guide/pdf/PM-Delivery-Guide-Learner-Edition.pdf) (เล่มใหม่, PMBOK 8) |
| ผู้สอน / ต้องการเฉลย + rubric ด้วย | [PM Delivery Guide — Complete Edition](field-guide/pdf/PM-Delivery-Guide-Complete-Edition.pdf) |
| อยากได้เนื้อหาตาม 10 Knowledge Areas | [PMBOK Masterclass — Complete Edition](e-Book/pdf/PMBOK-Masterclass-Complete-Edition.pdf) (เล่มเดิม, PMBOK 6+7) |
| อยากอ่านเป็น Markdown ทีละบท | [`field-guide/chapters/`](field-guide/chapters) หรือ [`lessons/`](lessons) |
| อยากรู้ศัพท์ PM ก่อน | [PM Glossary](docs/PM_GLOSSARY.md) |

## เนื้อหาสองชุดในนี้ต่างกันอย่างไร

| | `field-guide/` — PM Delivery Guide | `e-Book/` + `lessons/` — PMBOK Masterclass |
|---|---|---|
| อิง PMBOK | 8th Edition | 6th + 7th Edition |
| จัดเรียงตาม | ลำดับงานจริง A→H (Pre-sales → Closure) | 10 Knowledge Areas |
| จำนวน | 11 บท (Ch.0–10) + ภาคผนวก A–F | 16 บทเรียน + Capstone |
| เหมาะกับ | คนที่อยากเดินตามโครงการจริงตั้งแต่ต้นจนจบ | คนที่อยากไล่ตามโครงสร้าง PMBOK แบบคลาสสิก |

ทั้งสองชุดใช้ scenario เดียวกันและ glossary เดียวกัน อ่านชุดไหนก่อนก็ได้ — ดูตาราง mapping ระหว่างสองเล่มที่ [Content Coverage Matrix §7](docs/CONTENT_COVERAGE_MATRIX.md)

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

## กรณีศึกษาหลัก

ทุกบทเรียนผูกกับสองกรณีศึกษานี้ตลอดเล่ม เพื่อให้เห็นผลของการตัดสินใจสะสมข้ามบท

**ERP Transformation** — ใช้สอนบริบท Enterprise: Cross-functional Process, Data Migration, Integration, Governance, Vendor, Change Management, User Adoption และ Transition to Operation

**Hotel Booking Digital Platform** — ระบบตัวอย่างประกอบด้วย Mobile App, Customer Web App, Landing Page และ Back Office สำหรับค้นหาโรงแรม ตรวจสอบห้องว่าง จอง ชำระเงิน ยืนยันการจอง และบริหารข้อมูลโรงแรม ใช้สอน Customer Journey, UX, Conversion, Transaction Flow, Product Adoption, Payment Integration และ Business Value

รายละเอียดของทั้งสองกรณีศึกษาเป็น**ข้อสมมติเพื่อการเรียนรู้** ไม่ใช่ข้อมูลขององค์กรจริง — ดูไฟล์ต้นฉบับที่ [`scenarios/`](scenarios)

## โครงสร้าง repository

```text
PMBOK-Masterclass/
├── field-guide/        # PM Delivery Guide (PMBOK 8) — 11 บท เรียงตาม workflow A→H
│   ├── chapters/       #   ch-00 … ch-10 (learner / instructor / answer-key)
│   ├── appendices/     #   ภาคผนวก A–F (Artifact Catalogue, Golden Rules, Glossary ฯลฯ)
│   └── pdf/            #   เล่ม PDF + build script
├── e-Book/             # PMBOK Masterclass (PMBOK 6+7) — 16 บท ตาม Knowledge Areas
│   ├── chapters/       #   lesson-01 … lesson-16
│   ├── integration-reviews/
│   ├── capstone/
│   ├── pdf/
│   └── release/        #   ไฟล์สำหรับอ่าน/แจก
├── lessons/            # ต้นฉบับบทเรียน 01–16 (Blueprint / เนื้อหา / Assessment / Source Mapping)
├── capstone/           # โจทย์ Capstone + เกณฑ์ประเมิน
├── scenarios/          # Scenario Master — ERP และ Hotel Booking (แหล่งอ้างอิงข้อเท็จจริงเดียว)
├── references/         # PMBOK Overview (canonical source) + Delivery Playbook
└── docs/               # มาตรฐานและเอกสารอ้างอิงสำหรับคนที่จะเขียนต่อ
```

## เอกสารมาตรฐาน (สำหรับคนที่จะเขียนเนื้อหาต่อ)

| เอกสาร | ใช้ทำอะไร |
|---|---|
| [Content Rules](docs/CONTENT-RULES.md) | กฎการเขียนเนื้อหาทุกไฟล์ — source hierarchy, label, Definition of Done |
| [Course Standard](docs/COURSE_STANDARD.md) | เกณฑ์ release gate ของบทเรียน |
| [Style Guide](docs/STYLE_GUIDE.md) | แนวการเขียน ภาษา และการทำ link |
| [Lesson Template](docs/LESSON_TEMPLATE.md) | โครงบทเรียนมาตรฐาน |
| [Course Roadmap](docs/COURSE-ROADMAP.md) · [Lesson Index](docs/LESSON_INDEX.md) | ลำดับบทและสารบัญรวม |
| [Artifact Dependency Map](docs/ARTIFACT_DEPENDENCY_MAP.md) | Artifact ของบทไหนถูกใช้ต่อในบทใด |
| [PMBOK Edition Position](docs/PMBOK-EDITION-POSITION.md) | จุดยืนเรื่อง edition ของ repo นี้ |
| [`validate-repository.sh`](docs/validate-repository.sh) | ตรวจ metadata / link / absolute path ก่อน commit |

## สัญญาอนุญาต

เนื้อหาในหลักสูตรนี้เผยแพร่ภายใต้ **[CC BY-NC 4.0](LICENSE)** (Attribution-NonCommercial 4.0 International)

© 2026 Witchwasin K.

**ทำได้** — อ่าน ดาวน์โหลด แจกจ่ายต่อ ดัดแปลงต่อยอด และใช้สอนในองค์กร ชมรม หรือกลุ่มศึกษาที่ไม่เก็บค่าใช้จ่าย

**เงื่อนไข**

- **BY — ให้เครดิต:** ระบุชื่อผู้เรียบเรียง link กลับมาที่ repo นี้ และแจ้งว่าดัดแปลงหรือไม่
- **NC — ห้ามใช้เชิงพาณิชย์:** ห้ามนำไปเปิดคอร์สเก็บเงิน ขายเป็นหนังสือ หรือใช้เพื่อประโยชน์ทางการค้า เว้นแต่ได้รับอนุญาตเป็นลายลักษณ์อักษรจากผู้เรียบเรียง

ตัวอย่างการให้เครดิต:

```text
"PMBOK Masterclass" โดย Witchwasin K.
https://github.com/witchwasin/PMBOK-Masterclass — CC BY-NC 4.0
```

**ข้อยกเว้น** — ไฟล์ `references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook.md` และ `-V2.md` เป็นเอกสารต้นฉบับจากภายนอก เก็บไว้เป็น external reference ไม่ได้เรียบเรียงขึ้นในโครงการนี้ และไม่อยู่ภายใต้สัญญาอนุญาตข้างต้น

**เครื่องหมายการค้า** — PMBOK®, PMP® และ PMI® เป็นเครื่องหมายการค้าจดทะเบียนของ Project Management Institute, Inc. สัญญาอนุญาตนี้ครอบคลุมเฉพาะเนื้อหาที่เรียบเรียงขึ้นเองใน repo นี้ ไม่ครอบคลุมมาตรฐาน PMBOK ต้นฉบับซึ่งเป็นลิขสิทธิ์ของ PMI

## ผู้เรียบเรียง

Witchwasin K.

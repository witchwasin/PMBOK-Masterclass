---
title: Course Standard
document_type: Course Standard
version: 1.0
status: Active
---

# PMBOK Masterclass — Course Standard

> มาตรฐานคุณภาพที่ทุกบทเรียนต้องปฏิบัติตาม

---

## 1. Mandatory Lesson Sections (21 sections)

ทุกบทเรียนฉบับเต็ม (`_2-<Title>.md`) ต้องมีครบ:

| # | Section | หน้าที่ |
|---|---|---|
| 1 | **Lesson Metadata** | Lesson number, Title, Difficulty, Study time, Prerequisites, Related lessons, Canonical sources, Scenario versions, Status, Last reviewed, Intended learner level |
| 2 | **Opening Professional Question** | คำถาม/สถานการณ์ที่สร้างความอยากรู้ |
| 3 | **Why This Matters** | ปัญหาก่อนมีแนวคิดนี้, สิ่งที่ผิดพลาดเมื่อไม่มี, เชื่อมกับ Business Outcome |
| 4 | **Learning Objectives** | Observable + Measurable (ห้ามใช้ "เข้าใจ..." เปล่าๆ) |
| 5 | **Mental Model** | แผนผังความคิดที่ช่วยให้ผู้เรียนจำและเชื่อมโยงได้ |
| 6 | **Main Lesson** | เนื้อหาหลัก — progressive, ไม่ dump ข้อมูล |
| 7 | **PM Thinking** | สิ่งที่ PM ควรสังเกต ตั้งคำถาม คาดการณ์ |
| 8 | **PM Decision Thinking** | Structured Decision format (Decision, Owner, Inputs, Options, Trade-offs, Risk, Evidence, Next Action) |
| 9 | **PM Insight** | ข้อคิดเชิงวิชาชีพที่ลึกกว่า procedure |
| 10 | **ERP Scenario** | ใช้ข้อมูลจาก `scenarios/ERP-TRANSFORMATION-CASE.md` |
| 11 | **Hotel Booking Scenario** | ใช้ข้อมูลจาก `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` |
| 12 | **Real Enterprise Example** | ตัวอย่างนอกเหนือ 2 scenarios หลัก (เฉพาะเมื่อเพิ่มคุณค่า) |
| 13 | **Common Mistakes** | ข้อผิดพลาดที่เกิดจริงขณะทำงาน |
| 14 | **Common Misconceptions** | ความเชื่อผิดที่นำไปสู่การตัดสินใจผิด |
| 15 | **Interview Questions** | Foundational, Scenario, Senior PM, Executive + Answer direction + Warning signs |
| 16 | **PM Dictionary** | ศัพท์ที่ใช้ในบท (EN, Thai explanation, Practical meaning, Common misuse, Related term) — sync กับ PM_GLOSSARY.md |
| 17 | **Workshop** | ฝึกตัดสินใจ ไม่ใช่ท่องจำ (Scenario, Role, Info, Missing info, Decision, Constraints, Expected output, Debrief, Evaluation) |
| 18 | **Assessment** | ≥50% ต้องเป็น application/judgement (Decision Case, Trade-off, Artifact Review, Cross-Knowledge Analysis) |
| 19 | **Executive Summary** | สรุปสำหรับผู้บริหาร: Why, Decision improved, Failure prevented, What to monitor |
| 20 | **Lesson Connection** | สิ่งที่ทำได้แล้ว, สิ่งที่ยังไม่ครบ, เหตุผลที่บทถัดไปตามมา |
| 21 | **AI Continuation Context** | Concepts introduced, Terms standardized, Scenario state, Decisions made, Assumptions, Open questions, Dependencies, Prohibited contradictions, Next lesson handoff |

---

## 2. Source Classification Labels

ทุกส่วนเนื้อหาต้องระบุ label:

| Label | ใช้เมื่อ |
|---|---|
| `[PMBOK]` | แนวคิดจาก PMBOK (ไม่ระบุ edition = ใช้ได้ทั้ง 6 และ 7) |
| `[PMBOK 6]` | เฉพาะเจาะจง PMBOK 6th Edition |
| `[PMBOK 7]` | เฉพาะเจาะจง PMBOK 7th Edition |
| `[Best Practice]` | แนวปฏิบัติที่ดีทั่วไป |
| `[Enterprise Practice]` | Pattern ในองค์กรจริง |
| `[Teaching Scenario]` | สร้างขึ้นเพื่อการสอน |
| `[Professional Opinion]` | ความเห็นเชิงวิชาชีพ |

---

## 3. Metadata Standard

```yaml
---
lesson: <number>
sequence: <lesson.file_number>  # e.g., 5.2
title: <title>
document_type: <Lesson | Blueprint | Assessment | Source Mapping>
difficulty: <Foundation | Core | Advanced>
estimated_study_time: <minutes>
status: Draft | Review | Active
validation_status: Not Validated | Validated
last_reviewed: <YYYY-MM-DD>
intended_learner_level: <Beginner PM | Experienced PM | Senior PM>
prerequisite:
  - <Lesson reference>
related_lessons:
  - <Lesson reference>
canonical_source:
  - ../../references/PMBOK-Overview.md
scenario_version:
  erp: "1.0"
  hotel_booking: "1.0"
core_scenarios:
  - ERP Transformation
  - Hotel Booking Digital Platform
---
```

---

## 4. Release Gate

บทเรียนผ่าน Release Gate เมื่อ:

| Criterion | Threshold |
|---|---|
| ทุก 15 มิติใน Quality Scorecard | ไม่ต่ำกว่า 3/5 |
| เฉลี่ย Quality Score | ≥ 4/5 |
| Source Transparency | 5/5 |
| Terminology Consistency | 5/5 |
| PM Decision Thinking | ≥ 4/5 |
| Assessment Quality | ≥ 4/5 |
| มีครบ 21 mandatory sections | ✅ |
| Source Classification labels | ✅ |
| Scenario ใช้ข้อมูลจาก Scenario Master | ✅ |
| Internal links เป็น relative path | ✅ |

---

## 5. Definition of Done — Per Lesson

- [ ] Blueprint ผ่าน review
- [ ] Lesson content มีครบ 21 sections
- [ ] Source Classification labels ครบ
- [ ] Scenario ข้อมูลตรงกับ Scenario Master
- [ ] Assessment ≥50% application/judgement
- [ ] Source Mapping specific (ไม่ generic)
- [ ] Terminology ตรงกับ PM_GLOSSARY.md
- [ ] Internal links เป็น relative path
- [ ] Quality Score ผ่าน Release Gate
- [ ] Cross-lesson references ถูกต้อง

---

## 6. Assessment Types Required

ทุกบทต้องมี assessment ผสมจากประเภทเหล่านี้:

| Type | คำอธิบาย | % ขั้นต่ำ |
|---|---|---|
| **Decision Case** | ให้ข้อมูลไม่ครบ ให้ถามกลับว่าขาดอะไร | — |
| **Trade-off Case** | เลือก 3 ทางเลือก อธิบายผลกระทบ | — |
| **Artifact Review** | ให้ Artifact ที่มีข้อผิดพลาด ให้ Review | — |
| **Executive Communication** | ร่างสรุปถึง Sponsor | — |
| **Cross-Knowledge Analysis** | เปลี่ยนแปลง 1 อย่าง วิเคราะห์ผลข้ามด้าน | — |
| **Ambiguous Scenario** | ไม่มีคำตอบเดียว ต้องมี Reasoning | — |
| **Application/Judgement (รวม)** | — | **≥ 50%** |
| Concept Check (MC/T-F) | — | ≤ 30% |
| Reflection | — | ≤ 20% |

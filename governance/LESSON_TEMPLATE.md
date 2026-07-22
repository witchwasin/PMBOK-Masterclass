---
title: Lesson Template
document_type: Template
version: 1.0
usage: ใช้เป็น skeleton สำหรับสร้างบทเรียนใหม่ — เติมเนื้อหาจริงแทน placeholder
---

# Lesson Template — 21 Mandatory Sections

> คัดลอกไฟล์นี้แล้วเปลี่ยน placeholder เป็นเนื้อหาจริง

---

```yaml
---
lesson: XX
sequence: XX.2
title: <Lesson Title>
document_type: Lesson
difficulty: <Foundation | Core | Advanced>
estimated_study_time: <minutes>
status: Draft
validation_status: Not Validated
last_reviewed: YYYY-MM-DD
intended_learner_level: <Beginner PM | Experienced PM | Senior PM>
prerequisite:
  - Lesson XX — <Title>
related_lessons:
  - Lesson XX — <Title>
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

# Lesson XX — <Lesson Title>

## 1. Opening Professional Question

> <คำถาม/สถานการณ์ที่ทำให้ผู้เรียนอยากเข้าใจ concept ของบทนี้>

## 2. Why This Matters

<อธิบาย: ปัญหาก่อนมีแนวคิดนี้, สิ่งที่ผิดพลาดเมื่อไม่มี, เชื่อมกับ Business Outcome>

## 3. Learning Objectives

เมื่อเรียนจบบทนี้ ผู้เรียนควรสามารถ:

1. <Observable action verb> + <specific skill>
2. ...

## 4. Mental Model

```text
<Simple visual model that helps reasoning, not memorization>
```

## 5. Main Lesson

### 5.1 <Sub-topic>

**[Source Classification]** <Content>

### 5.2 <Sub-topic>

...

## 6. PM Thinking

<สิ่งที่ PM ควรสังเกต ตั้งคำถาม คาดการณ์>

## 7. PM Decision Thinking

```text
Decision: <What must be decided?>
Owner: <Who decides?>
Inputs: <What information is needed?>
Options:
  A: <Option and consequence>
  B: <Option and consequence>
  C: <Option and consequence>
Trade-offs: <What is gained and lost?>
Risk of Delay: <What happens if decision is delayed?>
Evidence: <How to document the decision?>
Next Action: <What follows the decision?>
```

## 8. PM Insight

> <Professional insight that goes beyond procedure>

## 9. ERP Scenario: <Scenario Title>

**[Teaching Scenario]** อ้างอิง [ERP Transformation Case](../../scenarios/ERP-TRANSFORMATION-CASE.md) v1.0

<Apply lesson concept to ERP scenario using locked facts>

## 10. Hotel Booking Scenario: <Scenario Title>

**[Teaching Scenario]** อ้างอิง [Hotel Booking Platform Case](../../scenarios/HOTEL-BOOKING-PLATFORM-CASE.md) v1.0

<Apply lesson concept to Hotel Booking scenario using locked facts>

## 11. Real Enterprise Example

**[Enterprise Practice]** <ตัวอย่างนอกเหนือ 2 scenarios หลัก — เฉพาะเมื่อเพิ่มคุณค่า>

## 12. Common Mistakes

1. <ข้อผิดพลาดที่เกิดจริงขณะทำงาน + ผลที่ตามมา>

## 13. Common Misconceptions

| ความเข้าใจผิด | ความจริง |
|---|---|
| <Misconception> | <Correction> |

## 14. Interview Questions

### Foundational
- **Q:** <คำถาม>
- **Answer Direction:** <แนวทางตอบ>
- **Warning Signs:** <สัญญาณคำตอบอ่อน>

### Scenario
- **Q:** <คำถาม>

### Senior PM
- **Q:** <คำถาม>

### Executive
- **Q:** <คำถาม>

## 15. PM Dictionary

| Term (EN) | คำอธิบาย (TH) | ความหมายเชิงปฏิบัติ | การใช้ผิดที่พบบ่อย | Term ที่เกี่ยวข้อง |
|---|---|---|---|---|

## 16. Workshop

### Scenario
<สถานการณ์>

### Your Role
<บทบาทของผู้เรียน>

### Available Information
<ข้อมูลที่มี>

### Missing Information
<ข้อมูลที่ขาด — ผู้เรียนต้องระบุ>

### Decision Required
<การตัดสินใจที่ต้องทำ>

### Constraints
<ข้อจำกัด>

### Expected Output
<ผลลัพธ์ที่คาดหวัง>

### Debrief Questions
1. <คำถามทบทวน>

### Evaluation Criteria
- <เกณฑ์ประเมิน>

## 17. Assessment

> ดูไฟล์ `Lesson-XX_3-Assessment.md`

## 18. Executive Summary

| มิติ | สรุป |
|---|---|
| **Why** | <ทำไมเรื่องนี้สำคัญ> |
| **Decision Improved** | <การตัดสินใจใดดีขึ้น> |
| **Failure Prevented** | <ความล้มเหลวใดป้องกันได้> |
| **What to Monitor** | <ผู้บริหารควรดูอะไร> |

## 19. Lesson Connection

- **สิ่งที่ทำได้แล้ว:** <capabilities gained>
- **สิ่งที่ยังไม่ครบ:** <what remains>
- **บทถัดไป:** <Lesson XX+1 — Title> เพราะ <reason>

## 20. AI Continuation Context

```yaml
concepts_introduced:
  - <concept>
terms_standardized:
  - <term>
scenario_state:
  erp: <what happened in this lesson>
  hotel_booking: <what happened in this lesson>
decisions_made:
  - <decision>
assumptions:
  - <assumption>
open_questions:
  - <question>
dependencies:
  - <dependency>
prohibited_contradictions:
  - <do not contradict this in later lessons>
next_lesson_handoff: <what the next lesson should pick up>
```

---
title: PMBOK Masterclass Execution Baseline
document_type: Execution Baseline
version: 3.0
status: Frozen
frozen_on: 2026-07-22
---

# Execution Baseline v3

เอกสารนี้เป็นขอบเขตบังคับสำหรับการยกระดับหลักสูตรจากเอกสารอธิบายแนวคิดไปสู่หลักสูตรที่ผู้เรียนประสบการณ์ศูนย์สามารถสร้าง ส่งตรวจ และเชื่อม Artifact จนถึง Handover ได้

## 1. Learning Sequence

ทุกบทต้องเดินตามลำดับ:

```text
Beginner Safety
→ Learn
→ Watch PM Think
→ Watch Completed Artifact
→ Do
→ Beginner Checkpoint
→ Review
→ Approve
→ ส่งต่อ Artifact
```

ห้ามวาง Learning Objectives, Mental Model, Workshop หรือ Lesson Connection ต่อท้าย Reflection/Bridge ของบทเดิมโดยไม่จัด Narrative ใหม่

## 2. Artifact Contract

Blueprint ทุกบทต้องประกาศ:

```yaml
artifact_inputs:
  - <artifact จากบทก่อน>
artifact_outputs:
  - name: <ชื่อ artifact>
    creator: <ผู้จัดทำ>
    artifact_owner: <ผู้รับผิดชอบความถูกต้องและการใช้งาน>
    reviewer: <ผู้ตรวจสอบ>
    approval_authority: <ผู้มีอำนาจอนุมัติ>
    approval_evidence: <หลักฐานอนุมัติ>
next_lesson_usage:
  - <วิธีใช้ artifact ในบทถัดไป>
acceptance_level:
  incomplete: <สิ่งสำคัญยังขาด>
  usable: <เพียงพอสำหรับใช้ต่อ>
  professional: <พร้อมใช้ใน governance และการตัดสินใจจริง>
```

Artifact ทุกชิ้นต้องมี Template, Thinking Walkthrough, Completed Example, Model Answer, Review Checklist และ Scoring Rubric

## 3. Scenario Strategy

- Lessons 01–04: ใช้ ERP และ Hotel Booking เพื่อเปรียบเทียบบริบท
- Lessons 05–14: ERP เป็น Primary Worked Example; Hotel Booking เป็น Contrast Example
- Lessons 15–16: Hotel Booking เป็น Primary Worked Example; ERP เป็น Contrast Example
- ตัวเลข ขอบเขต Owner และ Timeline ต้องตรง Scenario Master

## 4. Batch Boundaries

- Batch 1: Lessons 01–05
- Batch 2: Lessons 06–10
- Batch 3: Lessons 11–16 และ Capstone

Lesson 01 ใช้ Controlled Restructuring และรักษา Narrative หลัก ส่วน Lessons 02–05 ใช้ Full Narrative Rebuild

## 5. Batch Exit Criteria

Batch ปิดได้ต่อเมื่อ:

- ทุกบทใน Batch ผ่าน Release Gate
- Integration Review ผ่าน
- Scenario, Terminology และ Source Label ไม่มี Critical Issue
- Artifact มี Creator, Owner, Reviewer, Approval Authority และ Approval Evidence
- Artifact Output เชื่อมเป็น Input ของบทถัดไปได้จริง
- Beginner Comprehension และ Artifact Traceability Validation ผ่าน
- Structural validation และ Markdown checks ผ่าน
- Scorecard, Lesson Index และ Validation Report แสดงสถานะตรงกัน

## 6. Approval Workflow

เมื่อ Batch ผ่านเกณฑ์ ให้ส่ง diff, scorecard, integration report และประเด็นคงเหลือให้ผู้ดูแล Repository ตรวจ ก่อน commit และ push แยกหนึ่ง commit ต่อ Batch

---
chapter: lesson-07
title: Project Scope Management and WBS
edition: Instructor
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-07/
learner_chapter: ./lesson-07-learner.md
---

# Instructor Guide - Chapter 07

ลิงก์ไป Learner Chapter: [lesson-07-learner.md](./lesson-07-learner.md)

## Teaching Notes

สอน scope เป็น control boundary ไม่ใช่รายการความต้องการทั้งหมด. ให้ผู้เรียนเริ่มจาก stakeholder need แล้วบังคับแปลงเป็น requirement ที่ตรวจรับได้ ก่อนแตก WBS

## Learning Intent

ผู้เรียนต้องสร้าง scope artifact pack ที่ส่งต่อให้ schedule ได้จริง โดย work packages มี owner และ acceptance criteria

## Suggested Timing

| Segment | Time |
|---|---:|
| Lesson 06 handoff | 10 |
| Scope baseline concepts | 25 |
| WBS and dictionary | 25 |
| ERP/Hotel cases | 25 |
| Artifact workshop | 35 |

## Thinking Walkthrough

1. Ask what business decision or value the requirement supports
2. Convert vague request to slices with acceptance criteria
3. Separate in scope, out of scope, assumptions and exclusions
4. Build deliverable-oriented WBS
5. Add owner and acceptance in WBS dictionary
6. Route baseline impact through governance

## Completed Example

ERP reporting scope:

- Requirement: CFO monthly margin dashboard for approved module data only
- Boundary: excludes CRM/BI analytics and non-cleansed legacy data
- WBS fragment: reporting deliverable, data mapping, report design, reconciliation, UAT, sign-off
- Dictionary: owner, source data, acceptance criteria, dependency and approval route

## Model Answer

คำตอบ Professional ไม่รับคำว่า "รายงานบริหารทั้งหมด" เป็น scope โดยตรง ต้องแตก question set, decision need, source data, acceptance criteria และ WBS fragment

WBS ต้องเป็น deliverable-oriented และครอบคลุม 100% ของ approved scope ไม่ใช่ทุกคำขอ

## Review Checklist

- [ ] Requirements ตรวจรับได้
- [ ] Scope statement มี in/out/assumption/exclusion
- [ ] WBS ไม่แตกตาม department อย่างเดียว
- [ ] WBS dictionary มี owner และ acceptance
- [ ] Change route ระบุ authority และ evidence
- [ ] Handoff ไป Lesson 08 ชัดเจน

## Scoring Rubric

| Dimension | Incomplete | Usable | Professional |
|---|---|---|---|
| Requirements | กว้างและวัดไม่ได้ | มี slices และ criteria | trace stakeholder/value/acceptance |
| Scope boundary | ไม่มี out of scope | มี boundary พอควบคุม | มี assumption/exclusion/change trigger |
| WBS logic | แตกตามทีม/activity | deliverable-oriented | 100% rule และ owner ชัด |
| Governance | ไม่มี approval | มี Sponsor/CCB route | evidence/version baseline ครบ |

## Debrief Questions

- คำขอนี้อยู่ใน baseline หรือเป็น change
- Deliverable ใดตรวจรับได้จริง
- Work package ใดส่งต่อให้ Lesson 08 แตก activity ได้
- ถ้า include now จะต้อง replace หรือเพิ่มอะไร

## Artifact Approval Guidance

ผ่าน `Usable` เมื่อ scope pack ใช้ควบคุม baseline และส่งต่อ schedule ได้ ผ่าน `Professional` เมื่อ trace จาก stakeholder need ถึง requirement, WBS, acceptance และ change route ครบ


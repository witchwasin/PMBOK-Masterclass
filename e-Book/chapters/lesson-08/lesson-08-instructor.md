---
chapter: lesson-08
title: Project Schedule Management
edition: Instructor
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-08/
learner_chapter: ./lesson-08-learner.md
---

# Instructor Guide - Chapter 08

ลิงก์ไป Learner Chapter: [lesson-08-learner.md](./lesson-08-learner.md)

## Teaching Notes

สอน schedule เป็น logic for recovery. ผู้เรียนควรเลิกตอบจากวันที่บน Gantt และเริ่มถามเรื่อง dependency, float, critical path และ baseline authority

## Learning Intent

ผู้เรียนต้องสร้าง schedule artifact pack ที่ระบุ activity, dependency, owner, estimate basis, critical path และ recovery options

## Suggested Timing

| Segment | Time |
|---|---:|
| Lesson 07 handoff | 10 |
| Activity/dependency concepts | 25 |
| Critical path and float | 25 |
| Recovery options | 30 |
| Artifact workshop | 30 |

## Thinking Walkthrough

1. Start from WBS work packages
2. Convert deliverables into activities
3. Add dependencies and estimates
4. Identify critical path and float
5. Test delay against downstream gates
6. Compare recovery options against cost, quality and risk
7. Escalate baseline change only with evidence

## Completed Example

ERP test/migration network:

- Data cleansing and ERP configuration may run partly in parallel
- Migration rehearsal depends on cleansed data and configuration
- UAT depends on SIT exit criteria and usable migration data
- Cutover depends on final migration, UAT sign-off and readiness

## Model Answer

Professional answer must show schedule benefit and trade-off. "เร่งทีม" is not enough unless it states mechanism, cost, quality risk, owner and evidence

## Review Checklist

- [ ] Activities trace to WBS
- [ ] Dependencies shown
- [ ] Critical path/float considered
- [ ] Recovery options include trade-offs
- [ ] Baseline authority identified
- [ ] Output can feed time-phased cost in Lesson 09

## Scoring Rubric

| Dimension | Incomplete | Usable | Professional |
|---|---|---|---|
| Activity logic | มีวันที่อย่างเดียว | activities/dependencies ครบ | estimate basis and constraints clear |
| Critical path | ไม่วิเคราะห์ | identifies likely path/float | tests uncertainty and missing evidence |
| Recovery | generic speed-up | options with trade-offs | recommendation and governance clear |
| Governance | ไม่มี baseline | approved schedule route | change evidence/version control ครบ |

## Artifact Approval Guidance

ผ่าน `Usable` เมื่อ schedule สามารถใช้ forecast และ recovery ได้ ผ่าน `Professional` เมื่อแสดง logic, uncertainty, trade-off และ governance evidence ครบ


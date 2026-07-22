---
chapter: lesson-04
title: 10 Project Management Knowledge Areas Overview
edition: Instructor
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-04/
learner_chapter: ./lesson-04-learner.md
---

# Instructor Guide — Chapter 04

## Teaching Notes

ลิงก์ไป Learner Chapter: [lesson-04-learner.md](./lesson-04-learner.md)

บทนี้ต้องทำให้ผู้เรียนหยุดมอง Knowledge Areas เป็น list จำชื่อ และเริ่มใช้เป็น impact lens สำหรับ decision จริง

## Learning Intent

ผู้เรียนต้องแยกได้ว่า Process Groups คือ “ช่วง/โหมดการบริหาร” ส่วน Knowledge Areas คือ “เรื่องที่ต้องบริหาร” และ Integration คือจุดที่รวมผลกระทบเป็น decision

## Suggested Timing

| Segment | Time |
|---|---:|
| Lesson 03 handoff | 5 |
| Process Groups vs Knowledge Areas | 15 |
| 10 Knowledge Areas overview | 25 |
| Cross-impact examples | 25 |
| Workshop/debrief | 30 |

## Thinking Walkthrough

1. เริ่มจาก lifecycle/gate ของ Lesson 03
2. ระบุ primary Knowledge Area ที่เกิด change
3. ไล่ downstream impact ข้าม baseline, people, vendor, quality และ risk
4. แยก evidence available ออกจาก missing evidence
5. ระบุ impact owner แต่ละด้าน
6. เสนอ options และ approval threshold

## Completed Example

Hotel Booking ขอเพิ่ม Corporate Booking ก่อน high season:

| Area | Example impact |
|---|---|
| Scope | เพิ่ม feature ใหม่และ acceptance criteria |
| Schedule | กระทบ launch ก่อน high season |
| Cost | เพิ่ม development/QA/support cost |
| Quality | ต้อง test checkout, payment, inventory |
| Resource | แย่งทีมจาก payment stabilization |
| Stakeholder | Marketing ได้ value แต่ Operations เสี่ยง readiness |
| Procurement | อาจต้อง vendor/cloud/payment support เพิ่ม |
| Risk | conversion upside vs launch instability |
| Communications | ต้องแจ้ง sponsor, hotels, support, marketing |
| Integration | รวม options: include, defer, replace scope |

## Model Answer

คำตอบระดับ Professional ต้องไม่เติมผลกระทบให้ครบช่องแบบ generic แต่ต้องแสดง dependency เฉพาะเจาะจง มีอย่างน้อย 3 options และแยก impact owner/reviewer/approver ชัดเจน

Product Owner และ functional leads เป็น impact owners บางด้าน ส่วน Sponsor หรือ Change Authority เป็นผู้อนุมัติตาม threshold PM เป็นเจ้าของ integrated analysis ไม่ได้อนุมัติทุกเรื่องเอง

## Review Checklist

- [ ] ระบุ primary Knowledge Area
- [ ] Impact ไม่ generic
- [ ] มี missing evidence
- [ ] มี impact owner
- [ ] มีอย่างน้อย 3 options
- [ ] ระบุ approval threshold
- [ ] ส่งต่อใช้ทำ governance/change record ใน Lesson 05 ได้

## Scoring Rubric

| Dimension | Incomplete | Usable | Professional |
|---|---|---|---|
| Coverage | ลิสต์ชื่อด้าน | ระบุ impacts สำคัญ | แสดง dependency ข้ามด้าน |
| Evidence | assumption ปน fact | แยก gap | ระบุ owner, source และ deadline |
| Options | ทางเดียว | อย่างน้อย 3 options | trade-off เชื่อม value/baseline |
| Governance | PM อนุมัติทุกอย่าง | authority ตาม threshold | แยก impact owner/reviewer/approver |
| Handoff | ไม่รู้ปรับอะไร | ระบุ evidence update | พร้อมสร้าง governance/change record |

## Debrief Questions

- Impact ใดเป็น fact และ impact ใดยังเป็น assumption
- ใครเป็น impact owner ของ quality, resource และ stakeholder
- Option ใดปกป้อง value มากสุด
- Decision นี้ควรไปถึง Sponsor หรือไม่ เพราะอะไร

## Common Learner Errors

- เขียน “กระทบทุกด้านเล็กน้อย”
- ไม่มี owner
- ใช้ schedule/cost เป็นเกณฑ์เดียว
- ให้ PM approve change ที่เกิน threshold
- ลงลึกเทคนิคของบทหลังมากเกินไป

## Remediation Guidance

ถ้าคำตอบ generic ให้บังคับผู้เรียนเขียน evidence หนึ่งชิ้นต่อ impact หนึ่งด้าน ถ้าไม่มี evidence ให้เขียนว่า missing และตั้ง owner

## Facilitation Notes

อย่าขยายเข้า Lesson 05 ลึกเกินไป ใช้ Integration เป็นสะพาน ไม่ใช่สอน integrated change control เต็มบท

## Artifact Approval Guidance

ผ่าน `Usable` เมื่อมี impacts สำคัญ, missing evidence, owners, options และ approval route ครบ ผ่าน `Professional` เมื่อ trace กลับ baseline/gate และพร้อมทำ Change Decision Record


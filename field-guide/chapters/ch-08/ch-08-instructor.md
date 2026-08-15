---
chapter: ch-08
title: "Verification, UAT และ Release Readiness (Playbook F)"
book: "PM Delivery Guide"
edition: Instructor
status: Released
validation_status: Reviewed
last_reviewed: 2026-08-13
learner_chapter: ./ch-08-learner.md
---

# Instructor Guide — Chapter 08 (Verification/UAT)

ลิงก์ไป Learner Chapter: [ch-08-learner.md](./ch-08-learner.md)

## Teaching Notes

บทนี้คือ Quality ฝั่ง Control Quality/Validate (lesson-10 บางส่วน) + Playbook Phase F — **Cross-reference Quality ครบ 3 จุดต้องชัด: แผน Test = Ch.5, QA ฝั่งกระบวนการ = Ch.6, ผลจริง/QC/UAT = บทนี้** — นี่คือจุดที่ผู้ใช้เคยจับผิดใน Appendix E มาก่อน อย่าพลาด

## Learning Intent

ผู้เรียนต้องสร้าง: Release Readiness Report, Go/No-Go recommendation (พร้อม options/trade-off/authority), gap log และเห็นว่า RTM + severity + retest คือหลักฐาน ไม่ใช่สี dashboard

## Suggested Timing

| Segment | Time (นาที) |
|---|---:|
| Opening + Why | 10 |
| Test levels + QA vs UAT | 15 |
| UAT Planning + RTM + Defect | 25 |
| Release Readiness + Go/No-Go | 20 |
| Workshop | 25 |

## Thinking Walkthrough

1. UAT ไม่แทน system test
2. RTM = หลักฐาน coverage; ถ้าไม่ครบ = มี requirement ที่ไม่ถูกทดสอบ
3. Severity (QA) ≠ Priority (PO)
4. Readiness ครบ F.7 ก่อน Go/No-Go
5. Go/No-Go = Sponsor; conditional ต้องมีเงื่อนไข + owner + due date
6. residual risk ต้องถูกบันทึกเสมอ

## Scenario Note

ตัวเลขตาม Scenario Master: Sprint 11 (UAT/Performance/Security), Sprint 12 (Bug Fix + Soft Launch 3 โรงแรม), payment failure risk (Low Conversion), PCI-DSS/3s/5s/99.5% constraints

## Assessment หมายเหตุ

Decision/artifact ครอบงำ; ข้อ 7 recall

## Checklist ผู้สอน

- [ ] ครบ 15 หัวข้อ
- [ ] Cross-ref Quality ครบ 3 จุด (Ch.5/Ch.6/Ch.8)
- [ ] Scenario ตรง Scenario Master
- [ ] Source labels ถูกต้อง

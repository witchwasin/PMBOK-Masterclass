---
chapter: ch-09
title: "Go-Live และ Hypercare (Playbook G)"
book: "PM Delivery Guide (Ver.2)"
edition: Instructor
status: Draft
validation_status: Not Validated
last_reviewed: 2026-08-13
learner_chapter: ./ch-09-learner.md
---

# Instructor Guide — Chapter 09 (Go-Live & Hypercare)

ลิงก์ไป Learner Chapter: [ch-09-learner.md](./ch-09-learner.md)

## Teaching Notes

**บทนี้เป็นเนื้อหาใหม่ทั้งหมด — e-Book เดิมไม่มีบท deployment/hypercare เฉพาะ (ตาม master_plan §3)** — เขียนจาก Playbook Phase G โดยตรง + ผูก Scenario Master (soft launch 3 โรงแรม = Sprint 12, full launch 12 โรงแรม, post-launch support 3 เดือน) — เน้นว่าผู้ใช้เคยจับว่า "Go-live ≠ Closure" มาก่อน (lesson-01) ต้องชี้ชัดว่าบทนี้คือ Go-live, Closure คือ Ch.10

## Learning Intent

ผู้เรียนต้องสร้าง: cutover/rollback plan ที่มี trigger + owner + เวลาจำกัด, hypercare plan ที่มี exit criteria, และ Go/Defer decision record

## Suggested Timing

| Segment | Time (นาที) |
|---|---:|
| Opening + Why | 10 |
| Cutover + Deployment (G.3–G.4) | 20 |
| Rollback (G.5) | 15 |
| Hypercare + Stabilization (G.6–G.8) | 20 |
| Workshop | 25 |

## Thinking Walkthrough

1. Entry criteria ครบก่อนเริ่ม cutover
2. Cutover = sequence + owner + validation + decision point ต่อขั้น
3. Rollback ต้องทดสอบจริง + trigger + เวลาจำกัด + owner
4. Hypercare มี command center + metrics + exit criteria
5. Stabilization criteria กำหนดล่วงหน้า
6. Go-live ≠ Closure (Ch.10)

## Scenario Note

ตัวเลขตาม Scenario Master: Soft Launch pilot 3 โรงแรม (Sprint 12), Full Launch 12 โรงแรม, Post-Launch Support 3 เดือน, launch ก่อน High Season 1 พ.ย.

## Assessment หมายเหตุ

Decision-based ครอบงำ; ข้อ 7 recall

## Checklist ผู้สอน

- [ ] ครบ 15 หัวข้อ
- [ ] เนื้อหาใหม่ทั้งหมดตาม Playbook G (ไม่ใช่ของเดิม)
- [ ] ระบุชัด Go-live ≠ Closure
- [ ] Scenario ตรง Scenario Master

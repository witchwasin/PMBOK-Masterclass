---
title: AI Continuation Guide
document_type: AI Guide
version: 1.0
---

# PMBOK Masterclass — AI Continuation Guide

> คำแนะนำสำหรับ AI ที่จะทำงานต่อในอนาคต

---

## 1. ก่อนทำอะไร ให้อ่านไฟล์เหล่านี้ก่อน (ตามลำดับ)

1. `governance/REPOSITORY-VALIDATION-AND-FULL-REBUILD.md` — คำสั่งหลัก
2. `governance/COURSE_STANDARD.md` — มาตรฐาน 21 mandatory sections
3. `governance/STYLE_GUIDE.md` — กฎการเขียน
4. `governance/CONTENT-RULES.md` — กฎเนื้อหา
5. `repository/PMBOK-EDITION-POSITION.md` — จุดยืน PMBOK Edition
6. `scenarios/ERP-TRANSFORMATION-CASE.md` — Scenario Master ERP
7. `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` — Scenario Master Hotel Booking
8. `repository/LESSON_QUALITY_SCORECARD.md` — สถานะคุณภาพปัจจุบัน
9. `governance/LESSON_INDEX.md` — สถานะทุกบท
10. `repository/REPOSITORY_DECISION_LOG.md` — การตัดสินใจที่เคยทำ

## 2. กฎหลัก

1. **ห้าม Rewrite ก่อน Audit** — ถ้ายังไม่มี Audit Report ให้ทำก่อน
2. **ห้ามสร้างตัวเลข Scenario ใหม่** — ใช้จาก Scenario Master เท่านั้น ถ้าต้องเพิ่มให้ update Scenario Master ก่อน
3. **ห้ามข้ามขั้นตอน** — Pass 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7
4. **ทุก Lesson ต้องมีครบ 21 sections** — ตาม COURSE_STANDARD.md
5. **ทุกส่วนเนื้อหาต้องมี Source Classification label**
6. **Lesson 01 คือ quality baseline** — ห้ามลดคุณภาพ narrative ของ L01 เพื่อให้เท่ากับบทอื่น
7. **Assessment ต้อง ≥50% application/judgement** — ไม่ใช่แค่ MC/T-F
8. **Internal links ต้องเป็น relative path เสมอ**
9. **Terminology ต้อง sync กับ PM_GLOSSARY.md**
10. **อย่าอ้างว่า "เสร็จ" ถ้ายังไม่ผ่าน Release Gate**

## 3. Scenario Continuity

- ERP: ใช้ข้อมูลจาก `scenarios/ERP-TRANSFORMATION-CASE.md` — Sponsor คือคุณสมชาย (CEO), PM คือคุณเอก, SI คือ TechConsult, Working Budget 45 ล้านบาท / Total Funding Envelope 60 ล้านบาท, Timeline 12 เดือน
- Hotel Booking: ใช้ข้อมูลจาก `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` — Sponsor คือคุณจิรา (CEO), PO คือคุณนภา, PM คือคุณสุทธิ, Budget 12 ล้านบาท, Timeline 8 เดือน

## 4. เมื่อ Output ใกล้ Response Limit

หยุดที่ logical boundary แล้วรอคำสั่ง: `Continue Repository Rebuild`

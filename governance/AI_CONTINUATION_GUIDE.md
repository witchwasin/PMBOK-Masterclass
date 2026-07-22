---
title: AI Continuation Guide
document_type: AI Guide
version: 2.0
---

# PMBOK Masterclass — AI Continuation Guide

> คำแนะนำสำหรับ AI ที่จะทำงานต่อในอนาคต

---

## 1. ก่อนทำอะไร ให้อ่านไฟล์เหล่านี้ก่อน (ตามลำดับ)

1. `governance/COURSE_STANDARD.md` — มาตรฐานและ release gate
2. `governance/CONTENT-RULES.md` — กฎเนื้อหาและ source boundaries
3. `governance/EXECUTION_BASELINE.md` — learning sequence และ artifact contract
4. `governance/ARTIFACT_DEPENDENCY_MAP.md` — end-to-end handoff
5. `governance/STYLE_GUIDE.md` — กฎการเขียน
6. `repository/PMBOK-EDITION-POSITION.md` — จุดยืน PMBOK Edition
7. `scenarios/ERP-TRANSFORMATION-CASE.md` — Scenario Master ERP
8. `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` — Scenario Master Hotel Booking
9. `repository/LESSON_QUALITY_SCORECARD.md` และ `governance/LESSON_INDEX.md` — สถานะ release ปัจจุบัน
10. `repository/REPOSITORY_DECISION_LOG.md` — การตัดสินใจที่เคยทำ

## 2. กฎหลัก

1. **เริ่มจาก source of truth ปัจจุบัน** — ใช้ Course Standard, Execution Baseline และ Scenario Master; อ่าน archive เฉพาะเมื่อจำเป็นต้องเข้าใจประวัติ
2. **ห้ามสร้างตัวเลข Scenario ใหม่** — ใช้จาก Scenario Master เท่านั้น ถ้าต้องเพิ่มให้ update Scenario Master ก่อน
3. **ห้ามข้าม release gate** — ตรวจ metadata, artifact, scenario consistency, integration และ evidence ตามงานที่เปลี่ยน
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

หยุดที่ logical boundary แล้วสรุป validation และ artifact handoff ที่ยังเหลือ

---
title: Repository Decision Log
document_type: Decision Log
version: 1.0
---

# PMBOK Masterclass — Repository Decision Log

| # | Date | Decision | Rationale | Decided By | Impact |
|---|---|---|---|---|---|
| 1 | 2026-07-22 | PMBOK Edition: ใช้ Canonical Source (ผสม PMBOK 6+7) + label ให้ชัด | Canonical Source เป็นฐาน PMBOK 6 process structure ผสม Agile/Hybrid จาก PMBOK 7 — label ชัดแทนที่จะเลือกข้างเดียว | User (Owner) | ทุก Lesson ต้องมี Source Classification labels |
| 2 | 2026-07-22 | ERP Scenario: Generic ERP ไม่ระบุ vendor เฉพาะ | ใช้ได้กับทุกอุตสาหกรรม ไม่ผูกกับ SAP/Oracle | User (Owner) | สร้าง ERP-TRANSFORMATION-CASE.md เป็น FMCG company |
| 3 | 2026-07-22 | Hotel Booking: Hotel Chain สร้างระบบจองของตัวเอง (Direct Booking Platform) | สอน Digital Product ในมุม Hotel Chain ที่ต้องการลด OTA dependency | User (Owner) | สร้าง HOTEL-BOOKING-PLATFORM-CASE.md เป็น Hotel Chain |
| 4 | 2026-07-22 | Commit Strategy: ทำทั้งหมดแล้ว push ทีเดียว | ลดจำนวน commits ให้ clean | User (Owner) | Push ครั้งเดียวหลัง rebuild เสร็จ |
| 5 | 2026-07-22 | ทุก Lesson status เปลี่ยนจาก Active → Draft | ไม่มี Lesson ใดผ่าน Release Gate | Audit Report | ต้อง rebuild ก่อนเปลี่ยนกลับเป็น Active |
| 6 | 2026-07-22 | Course เป็น Practice-Oriented ไม่ใช่ Exam-Oriented | สอน PM Thinking & Decision Making ไม่ใช่ exam prep | Edition Position + User | Assessment เน้น Decision Case ไม่ใช่ MC recall |
| 7 | 2026-07-22 | Lock ERP budget terminology: Working Budget 45 ล้านบาท; Total Funding Envelope 60 ล้านบาท | หลีกเลี่ยงการใช้ตัวเลข 45 และ 60 แทนกันโดยไม่บอกขอบเขต | Rebuild execution | ทุก lesson และ assessment ต้องระบุ baseline ที่ใช้อ้างอิง |

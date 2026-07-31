---
title: PM Delivery Field Guide — Book Blueprint
document_type: Book Blueprint
version: 0.1
status: Draft — Outline Only, No Chapters Written
last_updated: 2026-07-31
related_decision_log: repository/REPOSITORY_DECISION_LOG.md (#8, #9)
related_reference: repository/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md (preferred source; V1 also available)
---

# แผนโครงเล่มใหม่: PM Delivery Field Guide (ชื่อชั่วคราว)

> สถานะ: **ร่างโครง (Draft Outline)** สำหรับให้ปรับในอนาคต — ยังไม่เริ่มเขียนเนื้อหาจริง ไม่มีบทใดถูกเขียนขึ้นเลย

## Context — ทำไมต้องมีเล่มนี้

ผู้ใช้ต้องการหนังสือเล่มใหม่ที่:

1. สอนคนทั่วไปให้เข้าใจ PM ด้วยภาษาง่าย มีตัวอย่างที่จับต้องได้ มีแบบทดสอบ อ่านจบแล้วเป็น PM ได้จริง
2. **ใช้เป็น field manual** — เวลามีปัญหาหน้างาน เปิดเล่มนี้อ่านแล้วแก้ปัญหาได้เลย

ต้นทางคือ [repository/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md](../repository/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md) ที่เก็บไว้เป็น Pending External Reference (อ้างอิง PMBOK 8th Edition, ดู [Decision Log #8](../repository/REPOSITORY_DECISION_LOG.md) และ [#9](../repository/REPOSITORY_DECISION_LOG.md)) — เป็น operational playbook สาย A–H (Pre-sales → Closure) เขียนแบบ dense/checklist ยังไม่มีชั้นการสอน V2 เพิ่มชั้น Execution Ownership (RACI ต่อกิจกรรม, Action Flow table ทุกช่วง, Quick Role-to-Action Reference) เหนือกว่า V1 — ใช้ V2 เป็นแหล่งอ้างอิงหลัก V1 ([repository/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook.md](../repository/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook.md)) เก็บไว้เป็น fallback/cross-check

Repo มี [e-Book/](../e-Book) อยู่แล้ว (16 บทตาม PMBOK 6+7 Knowledge Areas, pedagogy-first) — ผู้ใช้ยืนยันแล้วว่า **เล่มใหม่นี้แยกต่างหากจาก e-Book เดิม ไม่ใช่ replacement** จึงมี identity, โครงสร้าง, และ edition label ของตัวเอง (PMBOK 8) โดยไม่แตะของเดิม

สิ่งที่ยืนยันแล้วว่าทำได้จริงในโปรเจกต์นี้: e-Book เดิมพิสูจน์ว่า pipeline "lesson → learner/instructor/answer-key → compile → PDF" ใช้งานได้จริง ([e-Book/pdf/build_pdf.py](../e-Book/pdf/build_pdf.py)) เล่มใหม่ควรทำซ้ำแนวทางเดียวกัน ปรับ template ให้เบาลงและ workflow-first แทน KA-first

---

## โครงเล่ม (Proposed Table of Contents)

### ชื่อเล่ม (เสนอ 3 ตัวเลือก — เลือก/ปรับได้)

- A. **"PM Delivery Field Guide"** — ตรงไปตรงมา บอกว่าใช้ทำงานจริง
- B. **"จากรับโจทย์ลูกค้าสู่ Go-Live: คู่มือ PM ภาคปฏิบัติ (PMBOK 8)"**
- C. **"The PM Playbook: Pre-sales to Closure"**

### Front Matter

- **วิธีใช้เล่มนี้** — อธิบาย 2 โหมดการอ่าน: (1) **Study Mode** อ่านเรียงบทเพื่อเรียนจบเป็น PM (2) **Field Mode** ใช้ตาราง "มีปัญหาอะไร → ไปบทไหน" เพื่อ lookup ตอนติดปัญหาหน้างาน
- **หมายเหตุ Edition** — เล่มนี้อิง PMBOK 8th Edition ต่างจาก e-Book เดิม (PMBOK 6+7) พร้อมลิงก์อธิบายความสัมพันธ์
- **Scenario ที่ใช้ตลอดเล่ม** — ดูหัวข้อ "จุดตัดสินใจเรื่อง Scenario" ด้านล่าง

### Part 0 — ปฐมบท (1 บท)

- Ch.0: PMBOK คืออะไร (ฉบับย่อ) + ภาพรวม 6 Principles / 7 Performance Domains / 5 Focus Areas ของ PMBOK 8 + ทำไมหนังสือเล่มนี้เดินตามลำดับ A→H แทนที่จะเดินตาม Domain

### Part I — ก่อนเริ่มโครงการ

- **Ch.1 (จาก Playbook ส่วน A):** Pre-sales — ตั้งแต่ได้โจทย์ลูกค้าจนถึง Proposal/Contract
- **Ch.2 (จาก Playbook ส่วน B):** เริ่มต้นโครงการอย่างเป็นทางการ (Charter, Stakeholder, Governance, Kickoff)

### Part II — วางแผน (แตกจาก Playbook ส่วน C ซึ่งยาวที่สุด C1–C19 → แบ่งเป็น 3 บทย่อยเพื่อไม่ให้บทเดียวหนักเกินไป)

- **Ch.3:** วางแผน Requirement, Scope และ WBS (C1–C7)
- **Ch.4:** วางแผน Schedule (CPM) และ Cost/Resource (C8–C13)
- **Ch.5:** วางแผน Risk, Procurement, Environment และรวมเป็นแผนเดียว + Planning Gate (C14–C19)

### Part III — ลงมือทำและควบคุม

- **Ch.6 (จาก Playbook ส่วน D):** Execution / ส่งมอบ Solution
- **Ch.7 (จาก Playbook ส่วน E):** Monitoring, Controlling และ Change Control

### Part IV — ปิดจ๊อบ

- **Ch.8 (จาก Playbook ส่วน F):** Verification, UAT, Release Readiness
- **Ch.9 (จาก Playbook ส่วน G):** Go-Live และ Hypercare
- **Ch.10 (จาก Playbook ส่วน H):** Transition, Closure, Benefit Handover

### Back Matter (ส่วนที่ตอบโจทย์ "field manual")

- **Appendix A:** Artifact Catalogue ฉบับเต็ม (รวมจาก Playbook §4–5 ทำเป็นตาราง lookup)
- **Appendix B:** Golden Rules Poster (20 ข้อจาก Playbook §9 พิมพ์เป็น 1 หน้า)
- **Appendix C:** PM Glossary เพิ่มเติม — เทียบกับ [governance/PM_GLOSSARY.md](../governance/PM_GLOSSARY.md) แล้วพบว่ายังไม่มีคำว่า ROM, SOW, Cutover, Hypercare, Rollback, Go/No-Go ฯลฯ ต้องเพิ่มใหม่ ไม่ใช่ใช้ glossary เดิมตรงๆ
- **Appendix D:** Master Answer Key รวมทุกบท
- **Appendix E ("เปิดเมื่อมีปัญหา"):** ตาราง Problem → Chapter index เช่น "ลูกค้าขอเพิ่ม Scope กะทันหัน → บทที่ 7", "พรุ่งนี้จะขึ้น Production → บทที่ 9 + Checklist ท้ายบท"

**รวม: 11 บทเนื้อหา (Ch.0–10) + Front matter + 5 Appendix** — ใหญ่กว่า Playbook ต้นทาง (8 ส่วน) เพราะแตก Part C ออกเป็น 3 บทเพื่อย่อยง่ายขึ้น

---

## Template ต่อ 1 บท (เบากว่า LESSON_TEMPLATE 21 หัวข้อเดิม เพราะเล่มนี้เน้น field-use)

อ้างอิงโทน/สไตล์จาก [e-Book/chapters/lesson-01/lesson-01-learner.md](../e-Book/chapters/lesson-01/lesson-01-learner.md) (เปิดด้วยเรื่องเล่า ภาษาสนทนา ไม่ใช่ bullet ทันที) แต่ลดจำนวนหัวข้อจาก 21 เหลือ 10 ให้เหมาะกับหนังสือ 11 บท:

1. **เปิดด้วยสถานการณ์จริงจาก Case** (Opening Scenario Hook)
2. **ทำไมต้องรู้เรื่องนี้** (Why It Matters)
3. **Mental Model / ภาพรวม** (ดึงจาก Goal + Flow diagram ของ Playbook ส่วนนั้น)
4. **เนื้อหาหลัก** — แปลง Step-by-Step ของ Playbook จาก list เป็น narrative สอนเหตุผล
5. **ตัวอย่างจริงจาก Case ต่อเนื่อง** — ผูกกับ Scenario เดียวกันทั้งเล่ม
6. **จุดตัดสินใจและกับดักที่พบบ่อย** — แปลง Common Mistakes ของ Playbook เป็นเคสสั้นๆ แบบ "ถ้าคุณเจอแบบนี้..."
7. **Checklist ใช้งานจริง** — ดึงจาก Practical Checklist / Artifact table ของ Playbook ตรงๆ (นี่คือส่วนที่ตอบโจทย์ "กางอ่านตอนมีปัญหา")
8. **แบบทดสอบความเข้าใจ** (5–8 ข้อ ผสม recall + scenario-based decision case)
9. **เชื่อมไปบทถัดไป** (Bridge / artifact ที่ส่งต่อ)
10. **Quick Reference Card ท้ายบท** — สรุป 1 หน้า สำหรับพลิกดูเร็วๆ

---

## จุดตัดสินใจเรื่อง Scenario (ต้อง lock ก่อนเริ่มเขียนจริง)

Playbook ต้นฉบับ Section A (Pre-sales) สมมติว่า **มีความสัมพันธ์แบบ Vendor–Client** (Proposal, SOW, Contract negotiation) แต่ Scenario ที่ล็อกไว้ใน repo ([scenarios/HOTEL-BOOKING-PLATFORM-CASE.md](../scenarios/HOTEL-BOOKING-PLATFORM-CASE.md)) คือ Siri Hospitality Group (SHG) **สร้างระบบเอง** ด้วยทีม PO/PM ภายใน — ไม่มีความสัมพันธ์ Vendor–Client ให้ Ch.1 ใช้ตรงๆ

ทางเลือกที่ต้องตัดสินใจก่อนลงมือเขียน (เสนอ default ไว้ ปรับได้):

- **(แนะนำ) เพิ่มชั้นสมมติสั้นๆ เฉพาะ Ch.1–2:** สมมติว่า SHG จ้างบริษัท Digital Vendor ภายนอกมาพัฒนา (ตั้งชื่อใหม่ เช่น "บริษัท Booking Tech Solutions") ให้ Ch.1–2 เดินเรื่องจากมุมเวนเดอร์ แล้ว Ch.3 เป็นต้นไปกลับมาใช้ทีม SHG ตามที่ล็อกไว้เดิม (ล็อกด้วย label `[Teaching Scenario Extension]` ไม่กระทบตัวเลข/roles เดิมที่ล็อกไว้แล้ว)
- ใช้ Scenario เดิมแบบไม่ฝืน — เขียน Ch.1 เป็น "Internal Business Case Approval" แทน "Pre-sales ขายลูกค้า" (ตัด vendor framing ออก ปรับความหมายให้เข้ากับโครงการ internal product)
- สร้าง Scenario คู่ขนานใหม่ทั้งเล่ม (ไม่ผูกกับ Hotel Booking เดิม) — ใหญ่สุด เสี่ยงสุด ไม่แนะนำ

---

## Governance ที่ต้องแตะ (เมื่อเริ่มเขียนจริง)

- เพิ่ม label `[PMBOK 8]` ในระบบ label ของหนังสือเล่มนี้เท่านั้น (ไม่แก้ label เดิมของ e-Book/lessons)
- อัปเดต [repository/REPOSITORY_DECISION_LOG.md](../repository/REPOSITORY_DECISION_LOG.md) เพิ่มรายการเมื่อ "เริ่มเขียนจริง" (ตอนนี้ยังเป็นแค่ draft โครงเล่ม ไม่ถือว่าเริ่ม migrate)
- ไฟล์เล่มใหม่ควรอยู่ในโฟลเดอร์แยก คือ `field-guide/` (โฟลเดอร์นี้ ระดับเดียวกับ `e-Book/`) เพื่อไม่ปนกับ e-Book เดิม

---

## Production Pipeline ที่เสนอ (ทำซ้ำแนวทาง e-Book เดิม)

1. **Phase 0 (ตอนนี้):** ล็อกโครงเล่ม + ชื่อเล่ม + ตัดสินใจเรื่อง Scenario ข้างต้น
2. **Phase 1 — Pilot:** เขียน Ch.1 เต็มรูปแบบ 1 บท ตรวจสอบ tone/ความยาว/คุณภาพก่อนขยายบทอื่น
3. **Phase 2 — Batch Production:** เขียนบทที่เหลือเป็นชุด (เช่น 3 บทต่อรอบ) พร้อม integration review ทุกจบชุด (รูปแบบเดียวกับ `repository/BATCH-N-INTEGRATION-REVIEW.md` เดิม)
4. **Phase 3:** ทำ Appendix ทั้ง 5 ส่วน
5. **Phase 4:** รวมเล่ม ตรวจ cross-reference ทั้งเล่ม
6. **Phase 5:** Export PDF (ต่อยอด `e-Book/pdf/build_pdf.py` หรือสร้าง script ใหม่คล้ายกัน)

---

## Verification (สำหรับตอน "อนาคต" ที่จะปรับ/อนุมัติแผนนี้)

- ผู้ใช้ทวนโครงเล่ม/ชื่อเล่ม/จุดตัดสินใจเรื่อง Scenario แล้วปรับตามต้องการ
- เมื่อ lock แล้ว ค่อยขออนุมัติเริ่ม Phase 1 (เขียน Ch.1 นำร่อง) แยกต่างหาก — ไม่ auto-start เขียนเนื้อหาเต็มเล่มจากแผนนี้ทันที

---

## สถานะปัจจุบัน

**ไฟล์นี้คือ Blueprint เท่านั้น** ยังไม่มีบทใดถูกเขียน ไม่มีการแก้ policy ใดๆ ใน `governance/` หรือ `repository/` ยัง ไม่ commit/push จนกว่าจะได้รับคำสั่ง

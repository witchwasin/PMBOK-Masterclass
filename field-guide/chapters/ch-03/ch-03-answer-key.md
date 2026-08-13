---
chapter: ch-03
title: "Requirements, Scope และ WBS (Playbook C1–C6)"
book: "PM Delivery Guide (Ver.2)"
edition: Answer Key
status: Draft
validation_status: Not Validated
last_reviewed: 2026-08-13
learner_chapter: ./ch-03-learner.md
---

# Answer Key — Chapter 03 (Requirements, Scope และ WBS)

Instructor-facing only.

## Assessment Composition

| Section | Share | Type |
|---|---:|---|
| Decision Case | ~30% | Application |
| Artifact Review | ~20% | Artifact review |
| Trade-off Case | ~15% | Application |
| Artifact Construction | ~20% | Artifact |
| Cross-Knowledge Analysis | ~10% | Application |
| Recall | ~5% | Retrieval |

## Model Answers

### 1. [Decision Case] เพิ่ม loyalty program ใน MVP

**แนวตอบ:** อ้าง Scenario Master §4 — Loyalty อยู่ใน Out of Scope (Phase 2+) อย่างชัดเจน → เสนอ:
- A. Include: ขัดกับ baseline ที่ล็อก, เพิ่มความเสี่ยง payment/launch readiness, งบ 12M/8 เดือนไม่พอ → ไม่แนะนำ
- B. Defer ไป Phase 2 (แนะนำ): เก็บเป็น backlog, บันทึก decision record, คุณนภา (PO) จัด priority
- C. Replace: ต้องชี้ชัดว่า replace ฟีเจอร์ไหน value ต่ำกว่า และต้องผ่าน CCB
- Evidence: decision record + updated backlog + ไม่แก้ Scenario Master เงียบ ๆ (ต้อง proposal versioned update ถ้าจะเปลี่ยน)

**เกณฑ์ผ่าน:** อ้าง Out of Scope ใน Scenario Master, เสนอ defer อย่างมีหลักฐาน, ไม่รับคำขอโดยไม่มี impact

### 2. [Decision Case] "รายงานทุกอย่าง"

**แนวตอบ:** คำถาม 5 ข้อ เช่น: (1) รายงานนี้ใช้ตัดสินใจอะไร (2) ใครเป็นผู้ใช้/ผู้รับ (3) ข้อมูลมาจากระบบใด (4) ความแม่นยำ/ความถี่ที่ต้องการคืออะไร (5) ใครตรวจรับ (sign-off) — จากนั้นแปลงเป็น requirement slices ที่ testable + traceable

**เกณฑ์ผ่าน:** คำถามแยก decision need, user, data source, quality, acceptance

### 3. [Artifact Review] WBS แตกตามแผนก

**แนวตอบ:** WBS ตาม department ไม่แสดง deliverable → ตรวจ 100% Rule ไม่ได้, กำหนด acceptance ต่อ deliverable ไม่ได้, และงานข้ามแผนก (เช่น PMS sync) หลุดจากโครงสร้าง แก้: แตกเป็น "PMS Sync Adapter", "Payment Integration", "Customer Web App" ฯลฯ (deliverable-oriented) แล้วค่อย assign owner

**เกณฑ์ผ่าน:** อธิบายผลเสีย ≥ 2 ข้อ + วิธีแก้

### 4. [Trade-off Case] SRS/FSD เต็ม vs User Story + AC

**แนวตอบ:** สำหรับงาน compliance สูง (payment/PCI-DSS) ต้องมี SRS/FSD หรือสิ่งทดแทนที่มี coverage ครบ (API spec, data dictionary, business rules, error handling) เพราะ audit + ผูก payment + หลายทีม — User Story อย่างเดียวอาจไม่พอถ้าไม่มี acceptance criteria และ traceability; ในงานที่ compliance ต่ำ User Story + DoD + RTM อาจพอ
**เกณฑ์ผ่าน:** ตัดสินตาม coverage/compliance ไม่ใช่ตามกระแส Agile

### 5. [Artifact Construction] WBS "Payment Integration"

**แนวตอบ (ตัวอย่าง):** 1. Payment Gateway Contract & Setup, 2. Payment Flow Design, 3. Payment API Implementation, 4. Callback & Reconciliation, 5. PCI-DSS Security Review, 6. Payment Testing (SIT/UAT prep) — แต่ละ item ระบุ owner (คุณวีระ/DevOps/QA) + acceptance criteria (เช่น "refund flow ผ่าน test case TC-PAY-07")

**เกณฑ์ผ่าน:** deliverable-oriented, มี owner + acceptance criteria ต่อ work package

### 6. [Cross-Knowledge Analysis] PMS API ไม่รองรับ real-time sync (3 โรงแรม)

**แนวตอบ:**
- Scope (Ch.3): ต้อง define boundary — เช่น adapter แบบ batch sync ชั่วคราว หรือจำกัด real-time เฉพาะโรงแรมที่รองรับ
- Schedule (Ch.4): adapter/งาน sync เพิ่ม → กระทบ Sprint 7–8 (Back Office + Inventory Sync) หรือต้องเร่ง PoC ก่อน Sprint 1
- Test (Ch.8): ต้องเพิ่ม test scenario สำหรับ sync failure/reconciliation → กระทบ UAT scope
- ต้องผ่าน change/decision process ถ้า baseline เปลี่ยน

**เกณฑ์ผ่าน:** เห็นผลข้าม scope/schedule/test + decision path

### 7. [Recall] 100% Rule

**แนวตอบ:** WBS ต้องครอบคลุม approved scope ทั้งหมด (ผลรวม child = parent) และไม่รวมงานนอก scope — ต่างจาก "รวมทุกคำขอ" เพราะรวมเฉพาะที่ผ่าน approval

**เกณฑ์ผ่าน:** ถูกต้องครบสองด้าน (ครอบคลุม + ไม่เกิน)

## Rubric สรุป

| ระดับ | เกณฑ์ |
|---|---|
| Professional | อ้าง baseline/Scenario Master, มี options + evidence + owner, acceptance criteria ชัด |
| Usable | ตอบถูกประเด็นหลัก มี options แต่ไม่ระบุ owner/evidence |
| Incomplete | ความเห็นลอย ๆ ไม่ผูกกับ baseline |

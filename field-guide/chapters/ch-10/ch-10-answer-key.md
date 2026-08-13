---
chapter: ch-10
title: "Transition, Closure และ Benefit Handover (Playbook H)"
book: "PM Delivery Guide (Ver.2)"
edition: Answer Key
status: Draft
validation_status: Not Validated
last_reviewed: 2026-08-13
learner_chapter: ./ch-10-learner.md
---

# Answer Key — Chapter 10 (Transition & Closure)

Instructor-facing only.

## Assessment Composition

| Section | Share | Type |
|---|---:|---|
| Decision Case | ~30% | Application |
| Artifact Review | ~15% | Artifact review |
| Scenario Case | ~10% | Application |
| Trade-off Case | ~15% | Application |
| Cross-Knowledge Analysis | ~10% | Application |
| Recall | ~10% | Retrieval |

## Model Answers

### 1. [Decision Case] PMS known issue ยังค้างก่อน closure

**แนวตอบ:** ปิดแบบมีเงื่อนไข (ไม่เลื่อนทั้งหมด): known issue ฝากเป็น open item ใน handover — owner = Ops/DevOps (หลังลดทีม), SLA + due date ชัด, บันทึกใน closure report + residual risk + เชื่อม benefit plan (Inventory Sync ≥ 98% — Scenario Master §15) — ถ้า issue กระทบ critical (เช่น double booking) ต้องแก้ก่อนปิด

**เกณฑ์ผ่าน:** มีเงื่อนไข + owner + due date + เชื่อม benefit; แยก critical/non-critical

### 2. [Decision Case] คุณภัทรยังไม่ยืนยัน benefit owner

**แนวตอบ:** ไม่ปิดโดยไม่มี benefit owner — จัดประชุมกับคุณภัทร + คุณจิรา (Sponsor): ยืนยันบทบาท, measure (10% → 35% ใน 18 เดือน), baseline, data source, review cadence (รายเดือน) — ถ้ายังไม่ยืนยัน ระบุเป็น open item ที่ต้องปิดก่อน Sponsor อนุมัติ closure (exit criteria ข้อ benefit owner assigned)

**เกณฑ์ผ่าน:** ยึด exit criteria + มี escalation ผ่าน Sponsor + benefit plan ครบ

### 3. [Artifact Review] Closure Report ไม่มี handover/lessons/benefit

**แนวตอบ:** ขาด: operational handover (owner/SLA/runbook), lessons (action owner), benefit handover (owner/measure/cadence), open items, evidence — ผล: ระบบไร้เจ้าภาพหลัง 3 เดือน, 35% ไม่มีใครวัด, องค์กรไม่เรียนรู้ — แก้: ครบ H.8 elements + exit criteria (H.9)

**เกณฑ์ผ่าน:** ระบุสิ่งที่ขาด + ผล + วิธีแก้

### 4. [Scenario Case] 2C2P final invoice ไม่ตรง

**แนวตอบ:** ตาม H.5 — ตรวจกับ contract/SLA (transaction fee 2.5% + 7 บาท/txn), ขอ breakdown + reconciliation กับ settlement data, ถ้าต่างจริงเจรจา/ปรับตามสัญญา, บันทึกเป็น commercial closure record — ไม่จ่ายก่อน reconcile; ถ้าจำเป็น escalate ผ่าน Sponsor/Finance

**เกณฑ์ผ่าน:** อ้างสัญญา + evidence + ไม่จ่ายก่อนตรวจสอบ

### 5. [Trade-off Case] ปิดเร็ว (ปล่อยทีม) vs ปิดช้า

**แนวตอบ:** ปิดเร็ว: ปล่อย resource, ประหยัด — แต่ open items ค้าง → หลัง 3 เดือนไม่มีใครแก้, benefit ไม่มี owner; ปิดช้า: เก็บทีมจนทุกอย่างลงตัว — แต่ต้นทุนสูง, ทีมถูกดึงไปงานอื่นระหว่างรอ — แนะนำ: ปิดแบบมีเงื่อนไขที่ open items มี owner + due date ชัด (ส่วนใหญ่) และปิดเต็มเมื่อ exit criteria ครบ

**เกณฑ์ผ่าน:** เห็น trade-off + แนะนำตาม evidence

### 6. [Cross-Knowledge Analysis] 6 เดือนหลัง launch direct booking = 20% (ไม่ถึง 35%)

**แนวตอบ:** ตาม Scenario Master §14: 6 เดือน = 10→20% (อยู่บนเส้นทาง), 18 เดือน = 35% — สิ่งที่ต้องทำ: Benefit Owner (คุณภัทร) ทบทวน trend รายเดือน, วิเคราะห์ cause (conversion, payment, marketing, inventory), ปรับ product roadmap (PO คุณนภา ยังดูแล backlog ตาม Operating Model §16), PM ที่ปิดไปแล้วไม่ใช่เจ้าของ — แต่ lessons/PIR ควรถูกใช้ — ถ้า trend ออกนอกเส้นทาง ต้อง plan correction ผ่าน business ไม่ใช่ "เปิดโครงการใหม่" ทันที

**เกณฑ์ผ่าน:** อ่าน target ถูกต้อง (18 เดือน ไม่ใช่ 6), owner ถูก, มี action path

### 7. [Recall] Exit Criteria (H.9)

**แนวตอบ:** Deliverables Accepted, Operations Handover Complete, Support Ready, Financial Closure, Contract Closure, Lessons Captured, Resources Released, Benefit Owner Assigned, Sponsor Approves Closure

**เกณฑ์ผ่าน:** ระบุได้ ≥ 6 ข้อ

## Rubric สรุป

| ระดับ | เกณฑ์ |
|---|---|
| Professional | open items มี owner/due date, benefit owner ชัด, lessons มี action, อ้าง Scenario Master |
| Usable | ตอบถูกประเด็น แต่ ownership/evidence ยังไม่ครบ |
| Incomplete | ตอบ "ปิดเลย" หรือ "เลื่อน" โดยไม่มีเหตุผล/owner |

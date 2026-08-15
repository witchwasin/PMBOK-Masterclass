---
chapter: ch-09
title: "Go-Live และ Hypercare (Playbook G)"
book: "PM Delivery Guide"
edition: Answer Key
status: Released
validation_status: Reviewed
last_reviewed: 2026-08-13
learner_chapter: ./ch-09-learner.md
---

# Answer Key — Chapter 09 (Go-Live & Hypercare)

Instructor-facing only.

## Assessment Composition

| Section | Share | Type |
|---|---:|---|
| Decision Case | ~35% | Application |
| Artifact Review | ~15% | Artifact review |
| Scenario Case | ~10% | Application |
| Trade-off Case | ~15% | Application |
| Cross-Knowledge Analysis | ~10% | Application |
| Recall | ~10% | Retrieval |

## Model Answers

### 1. [Decision Case] payment failure 6% (threshold 4%)

**แนวตอบ:** เปิด rollback trigger → นำเสนอ options ภายในเวลาจำกัด (เช่น 30 นาที):
- A. Rollback: restore ระบบเดิม — ปลอดภัยสุด แต่ลูกค้า/โรงแรมเสีย trust, campaign กระทบ
- B. Fix-in-place: hotfix + monitor เข้ม — เร็ว แต่ต้องมั่นใจ root cause (gateway? flow? data?)
- C. Mitigation: จำกัดฟีเจอร์/workaround + monitor — กลาง ๆ
- ตัดสินใจตาม evidence: ถ้า root cause ชัดและ fix เร็ว → fix-in-place; ถ้าไม่ชัด/กระทบวงกว้าง → rollback — decision owner = Go-Live Authority (Sponsor) ภายในเวลาจำกัด, บันทึก decision + communication

**เกณฑ์ผ่าน:** มี trigger + เวลาจำกัด + options + authority + evidence

### 2. [Decision Case] คืนก่อน cutover พบ rollback ยังไม่ทดสอบ

**แนวตอบ:** ไม่เดินหน้าโดยไม่ทดสอบ rollback (กฎข้อ 1 ของบท) — options: (A) เลื่อน 48 ชม. เพื่อทำ rehearsal (แนะนำ ถ้า gap ปิดได้เร็ว), (B) ขึ้น 2 โรงแรมก่อน (แบ่งเฟส) แล้วโรงแรมที่ 3 ตามหลัง เมื่อ rollback ทดสอบ, (C) เดินหน้าแบบเสี่ยง — ไม่แนะนำ — ต้องสื่อสาร Sponsor + ยอมรับผลต่อ timeline/campaign

**เกณฑ์ผ่าน:** ไม่ขึ้นโดยไม่ทดสอบ rollback + มีทางเลือก + owner/due date

### 3. [Artifact Review] cutover plan ที่ไม่มี owner/sequence/validation/trigger

**แนวตอบ:** ความเสี่ยง: ไม่รู้ว่าใครทำอะไรต่อขั้น → วุ่นวายตอนกลางคืน, ไม่มี validation → พลาดจุดพัง, ไม่มี rollback trigger → ตัดสินใจช้า/มั่ว — แก้: เติม sequence + owner + validation + decision point + rollback trigger ต่อขั้น + evidence

**เกณฑ์ผ่าน:** ระบุความเสี่ยง + วิธีแก้

### 4. [Scenario Case] โรงแรมที่ 3 ไม่พร้อม

**แนวตอบ:** options: (A) เลื่อนโรงแรมที่ 3 ออกไป (ขึ้น 2 โรงแรมก่อน) — ลด blast radius, (B) เร่ง training คืนเดียว — เสี่ยงคุณภาพ, (C) ขึ้นทั้ง 3 พร้อม support เข้มที่โรงแรมนั้น — เสี่ยง overload — แนะนำ A พร้อมกำหนดวันที่ใหม่ + สื่อสาร GM — decision ผ่าน PM + Sponsor

**เกณฑ์ผ่าน:** มี options + trade-off + แนะนำตาม evidence

### 5. [Trade-off Case] Rollback vs Fix-in-place

**แนวตอบ:** Rollback: ปลอดภัย คืนสู่สภาพเดิม แต่เสีย trust + campaign + การย้อน data มีต้นทุน; Fix-in-place: เร็ว ไม่หยุดบริการ แต่ถ้า root cause ยังไม่ชัด อาจล้มซ้ำ/กระทบวงกว้าง — แนะนำ: root cause ชัด + fix เล็ก → fix-in-place; root cause ไม่ชัด/กระทบ critical → rollback — ตัดสินใจภายในเวลาจำกัด + decision record

**เกณฑ์ผ่าน:** เห็น trade-off ทั้งสองฝั่ง + เกณฑ์เลือก + เวลาจำกัด

### 6. [Cross-Knowledge Analysis] PMS sync error 5% หลัง hypercare

**แนวตอบ:** กระทบ booking accuracy (Ch.9) — ห้องว่าง/ราคาผิด → ลูกค้า double booking/overbooking → trust + support load — กระทบ benefit (Ch.10): direct booking 35% ใน 18 เดือนจะไม่เกิดถ้า inventory ไม่น่าเชื่อถือ (Scenario Master: Inventory Sync Accuracy ≥ 98%) — ทางเลือก: เพิ่ม hypercare/reconciliation, SLA กับโรงแรม, แก้ adapter — ต้องส่งต่อเป็น known issue/action ใน handover (Ch.10)

**เกณฑ์ผ่าน:** เห็นผลต่อ Ch.9 + benefit Ch.10 + ทางเลือก + handover

### 7. [Recall] Stabilization criteria (G.8)

**แนวตอบ:** ไม่มี Critical Incident ค้าง, Error Rate ใน threshold, Performance Stable, Business Transaction Correct, Support รับช่วงได้, Known Issues มี Plan, Operations Accepts Handover

**เกณฑ์ผ่าน:** ระบุได้ ≥ 5 ข้อ

## Rubric สรุป

| ระดับ | เกณฑ์ |
|---|---|
| Professional | trigger/เวลาจำกัด/owner ชัด, options + trade-off ครบ, decision record, อ้าง Scenario Master |
| Usable | ตอบถูกประเด็น แต่ trigger/เวลาจำกัด/evidence ยังไม่ครบ |
| Incomplete | ตอบลอย ๆ "กู้ backup" หรือ "เดี๋ยวดูทีหลัง" |

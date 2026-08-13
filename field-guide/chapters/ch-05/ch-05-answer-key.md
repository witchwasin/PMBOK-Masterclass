---
chapter: ch-05
title: "Risk, Procurement, Communications, Environment และ Integrated Plan (Playbook C7 + C14–C19)"
book: "PM Delivery Guide (Ver.2)"
edition: Answer Key
status: Draft
validation_status: Not Validated
last_reviewed: 2026-08-13
learner_chapter: ./ch-05-learner.md
---

# Answer Key — Chapter 05 (Risk/Procurement/Comms/Quality/Env + Gate)

Instructor-facing only.

## Assessment Composition

| Section | Share | Type |
|---|---:|---|
| Decision Case | ~30% | Application |
| Trade-off Case | ~15% | Application |
| Artifact Review | ~15% | Artifact review |
| Executive Communication | ~10% | Application |
| Cross-Knowledge Analysis | ~15% | Application |
| Recall | ~10% | Retrieval |
| (Decision-based รวม) | ≥ 85% | — |

## Model Answers

### 1. [Decision Case] Risk "key users ไม่ว่าง UAT"

**แนวตอบ:**
- Risk statement: "หาก finance/warehouse key users ยืนยัน availability ต่ำกว่า 60% ภายในวันที่ X UAT wave จะเลื่อน ทำให้ defect ไม่ถูกพบก่อน launch และเพิ่ม go-live risk"
- Trigger: availability < 60% ณ วันที่กำหนด / month-end overlap
- Owner: คุณสุทธิ (PM) ประสาน + Functional Managers (commit capacity)
- Response (Mitigate): phased UAT ตาม module, backfill, vendor support
- Residual: บาง user group อาจทดสอบช้า → เปิด contingency trigger
- Escalation: ถ้า capacity ไม่พอ → Steering Committee

**เกณฑ์ผ่าน:** มี trigger/owner/response/residual/escalation ครบ ไม่ใช่ "จะระวัง"

### 2. [Decision Case] 2C2P fee ต่ำแต่ SLA อ่อน

**แนวตอบ:** ไม่เลือกจาก fee อย่างเดียว — ดู Total Cost of Ownership: fee ต่ำแต่ถ้า incident กลาง campaign ทำ revenue/trust เสียหาย ค่าเสียหายแฝงสูงกว่า — ทางเลือก: negotiate SLA (incident response time, uptime), ขอ pricing adjustment แลก SLA ที่ดีขึ้น, หรือเลือก provider ที่ trade-off ดีกว่า — บันทึก commercial decision record + risk ลง register

**เกณฑ์ผ่าน:** เห็น cost/risk ทั้งระบบ ไม่ใช่ fee เฉย ๆ + มี decision record

### 3. [Trade-off Case] Conditional gate vs เลื่อน 2 สัปดาห์

**แนวตอบ:**
- Conditional: ได้ momentum, แต่ต้องมี gap log + owner + due date และยอมรับ residual risk ระหว่างทาง
- เลื่อน 2 สัปดาห์: ปิด gap ให้จบ แต่กินเวลาใกล้ launch 1 พ.ย. — ถ้า gap ไม่ใช่ blocker (เช่น test data เตรียมคู่ขนานได้) conditional เหมาะกว่า; ถ้า gap คือ baseline อ่อน (schedule ไม่จริง) ควรเลื่อน
- แนะนำ: conditional สำหรับ gap ที่ไม่บล็อก Execution + gate re-check ตาม due date

**เกณฑ์ผ่าน:** ตัดสินตามธรรมชาติของ gap + มี mechanism (gap log/re-check)

### 4. [Artifact Review] Risk register "ทีมไม่พร้อม"

**แนวตอบ:** แก้เป็น: risk ที่มี event ("key users เข้าร่วม UAT < 60%"), trigger (availability < 60% วันที่ X), owner (Functional Manager), response (phased UAT/backfill), probability/impact, residual, review cadence — "ทีมไม่พร้อม" monitor ไม่ได้เพราะไม่รู้ว่าจะดูอะไร

**เกณฑ์ผ่าน:** แปลงคำกว้างเป็น actionable risk ครบองค์ประกอบ

### 5. [Executive Communication] ทำไม Test Strategy ต้องล็อกก่อน build

**แนวตอบ:** Test Strategy กำหนดว่า "อะไรคือพอ" (test levels, env, data, entry/exit, acceptance authority) — ถ้าไม่ล็อกก่อน build ทีมจะ build โดยไม่มีเกณฑ์ตรวจรับ และ Ch.8 (UAT) จะเถียงว่าแบบไหนถึงจะผ่าน; การล็อกตั้งแต่ต้นลด rework, ทำให้ resource/งบการทดสอบถูกวางแผนถูกต้อง และทำให้ acceptance มีหลักฐาน — ผลทดสอบจริงจะถูกตรวจใน Ch.8

**เกณฑ์ผ่าน:** เชื่อมกับ value/risk + กระชับ

### 6. [Cross-Knowledge Analysis] settlement 2 วันทำการ

**แนวตอบ:**
- Requirement (Ch.3): ข้อกำหนด "booking confirmation ≤ 5 วินาที" อาจไม่กระทบ แต่ business rule เรื่อง refund/สถานะ payment ต้องปรับ + communication กับลูกค้าเรื่องเวลาสะท้อนเงิน
- Test (Ch.5/Ch.8): เพิ่ม test case สำหรับ pending settlement state, reconciliation scenario
- Operating model (Ch.9): support script + คำถามลูกค้าเรื่อง "จ่ายแล้วแต่ยังไม่ยืนยัน" + SLA กับ 2C2P ต้องชัดเจน
- ต้องผ่าน change/decision process ถ้า baseline กระทบ

**เกณฑ์ผ่าน:** เห็นผลข้าม Ch.3/Ch.5/Ch.8/Ch.9 + decision path

### 7. [Recall] Verification vs Validation

**แนวตอบ:** Verification = สร้างถูกตาม spec (เช่น booking flow ทำงานตามที่เขียนใน SRS); Validation = สร้างสิ่งที่ตอบ need (เช่น ลูกค้าจองจบและจ่ายเงินสำเร็จจริง, direct booking เพิ่มขึ้น) — จาก SHG: verify ว่า "ฟีเจอร์ทำงานตาม spec" กับ validate ว่า "ผู้ใช้จองสำเร็จและ conversion ดีขึ้น"

**เกณฑ์ผ่าน:** แยก concept + ยกตัวอย่างจาก scenario

## Rubric สรุป

| ระดับ | เกณฑ์ |
|---|---|
| Professional | Risk มี trigger/owner/residual, contract decision เห็น TCO, gate มี gap log + due date |
| Usable | ตอบถูกประเด็นหลัก แต่องค์ประกอบยังไม่ครบ (เช่น ขาด residual/owner) |
| Incomplete | ความเห็นลอย ๆ ไม่มี trigger/owner/evidence |

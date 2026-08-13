---
chapter: ch-04
title: "Schedule, Cost และ Resource (Playbook C8–C13)"
book: "PM Delivery Guide (Ver.2)"
edition: Answer Key
status: Draft
validation_status: Not Validated
last_reviewed: 2026-08-13
learner_chapter: ./ch-04-learner.md
---

# Answer Key — Chapter 04 (Schedule, Cost และ Resource)

Instructor-facing only.

## Assessment Composition

| Section | Share | Type |
|---|---:|---|
| Decision Case | ~30% | Application |
| EVM Case | ~20% | Application/judgement |
| Trade-off Case | ~10% | Application |
| Artifact Review | ~15% | Artifact review |
| Artifact Construction | ~15% | Artifact |
| Recall | ~10% | Retrieval |

## Model Answers

### 1. [Decision Case] Payment Integration ช้า 1 สัปดาห์

**แนวตอบ:** ข้อมูลที่ต้องรู้ก่อนตัดสินใจ: (1) delay อยู่บน critical path หรือไม่ (2) float ที่เหลือของกิจกรรมนี้ (3) downstream dependency (Mobile App Sprint 5–6, Back Office Sprint 7–8) (4) recovery mechanism ที่เป็นไปได้ (5) กระทบ cost/resource/quality อย่างไร

**3 options + trade-off:**
- A. Use float + resequence — ถูกสุด แต่ใช้ได้ถ้า float จริง
- B. Crashing (เพิ่ม payment specialist / OT) — ย่นเวลาแต่เพิ่ม cost และ coordination risk
- C. Fast Tracking (เริ่ม mobile integration ก่อน payment ปิดครบ) — เร็ว แต่เพิ่ม rework + quality risk
- ถ้าล่าช้าเกิน tolerance → Split Release หรือ Rebaseline ต้อง Sponsor อนุมัติ

**เกณฑ์ผ่าน:** ไม่สรุป "เร่งทีม" โดยไม่มี mechanism, เห็น trade-off ข้าม cost/resource/quality

### 2. [Decision Case] 80 key users ไม่ว่าง UAT

**แนวตอบ:** options: phased UAT ตาม module (เลี่ยง month-end), backfill งานประจำช่วง UAT, vendor support สำหรับ test preparation, ขอ key users บางกลุ่ม dedicated 50% ใน 4 สัปดาห์, เลื่อน wave ที่ชน month-end — capacity commitment ต้องมาจาก functional managers; exception/priority conflict ขึ้น Steering

**เกณฑ์ผ่าน:** มี options + ระบุ owner/authority ถูกต้อง (PM ไม่ approve capacity แผนกเอง)

### 3. [EVM Case] PV = 6M, EV = 5M, AC = 6.5M

**แนวตอบ:**
- SV = 5 - 6 = -1M; CV = 5 - 6.5 = -1.5M
- SPI = 5/6 = 0.83; CPI = 5/6.5 = 0.77
- EAC = BAC/CPI = 12/0.77 ≈ 15.6M; VAC = 12 - 15.6 = -3.6M
- คำถามต่อ: EV วัดจาก deliverable ที่มี evidence หรือไม่, สาเหตุ (PMS delay, defect, scope ambiguity?), เป็น trend หรือ one-time, reserve ใดใช้ได้ ใครอนุมัติ

**เกณฑ์ผ่าน:** คำนวณถูก + ถาม cause/evidence ไม่ใช่จบที่ตัวเลข

### 4. [Trade-off Case] Crashing vs Fast Tracking

**แนวตอบ:** Crashing = เพิ่มทรัพยากร → เร็วแต่ต้นทุน + coordination เพิ่ม; Fast Tracking = ทำงานขนาน → เร็วโดยไม่เพิ่มคน แต่ rework/quality risk สูง (เช่น UAT บางส่วนก่อน SIT ปิด) — สำหรับ PMS delay ถ้า issue คือรอข้อมูลภายนอก (vendor API) fast tracking ฝั่งที่รอได้อาจดีกว่า crashing ที่เพิ่มคนแต่ยังรอข้อมูลอยู่

**เกณฑ์ผ่าน:** เข้าใจกลไกต่างกัน + เลือกตามสาเหตุของ delay

### 5. [Artifact Review] Gantt ที่ไม่มี dependency/owner/basis

**แนวตอบ:** decision risk: ตอบไม่ได้ว่า delay กระทบ milestone หรือไม่ (ไม่มี dependency/float), ไม่รู้ว่าใครรับผิดชอบ (ไม่มี owner), estimate ไม่มี basis → recovery คุยกันด้วยความเห็น — แก้: เพิ่ม dependency network, float, owner, estimate basis + baseline

**เกณฑ์ผ่าน:** ระบุ decision risk ≥ 3 + วิธีแก้

### 6. [Artifact Construction] Resource Plan + RACI สำหรับ UAT

**แนวตอบ (ตัวอย่าง):** UAT wave แยก module (Booking, Payment, Back Office) — RACI: คุณนภา (PO) = Accountable การยอมรับ business, QA Lead = Responsible test prep, คุณสุทธิ (PM) = Responsible จัดตาราง/ประสาน, Hotel Coordinator = Consulted (ความพร้อม 12 โรงแรม), คุณกาญจนา = Consulted (rate/pricing scenario) — capacity: key users 80 คนมี BAU → wave plan + backfill ระบุ owner และ sign-off จาก functional managers

**เกณฑ์ผ่าน:** มี RACI ถูกต้อง (A หนึ่งคน), capacity + sign-off + wave plan

### 7. [Recall] Effort vs Duration

**แนวตอบ:** Effort = ปริมาณแรงงาน (person-days); Duration = เวลาปฏิทิน — 8 person-days อาจทำ 2 คนใน 4 วัน หรือ 1 คนใน 8 วัน (ขึ้นกับ parallelism, dependencies, availability) — สับสนสองอย่างนี้ทำให้ schedule ผิดพลาด

**เกณฑ์ผ่าน:** แยก concept + ยกตัวอย่าง

## Rubric สรุป

| ระดับ | เกณฑ์ |
|---|---|
| Professional | คำนวณ EVM ถูก, options มี mechanism + trade-off, owner/authority ชัด, อ้าง Scenario Master |
| Usable | ตอบถูกประเด็น มี options แต่ mechanism/ตัวเลขยังหลวม |
| Incomplete | ตอบลอย ๆ "เร่งทีม/เพิ่มคน" ไม่มี mechanism |

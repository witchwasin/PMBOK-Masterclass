---
chapter: ch-06
title: "Execution — ส่งมอบ Solution, บริหารทีม และ Manage Quality (Playbook D)"
book: "PM Delivery Guide (Ver.2)"
edition: Answer Key
status: Draft
validation_status: Not Validated
last_reviewed: 2026-08-13
learner_chapter: ./ch-06-learner.md
---

# Answer Key — Chapter 06 (Execution)

Instructor-facing only.

## Assessment Composition

| Section | Share | Type |
|---|---:|---|
| Decision Case | ~30% | Application |
| Artifact Review | ~15% | Artifact review |
| Trade-off Case | ~15% | Application |
| Scenario Case | ~15% | Application |
| Cross-Knowledge Analysis | ~15% | Application |
| Recall | ~10% | Retrieval |

## Model Answers

### 1. [Decision Case] story code เสร็จแต่ไม่มี unit test + security check

**แนวตอบ:** ไม่นับเป็น Done — กลับไปทำ unit test + security check ให้ครบ DoD (อาจช่วย pair/fast-track) — อธิบายว่าการปล่อยผ่านตอนนี้แค่ย้าย defect ไป Ch.8/Ch.9 ซึ่งแพงกว่า; บันทึกเป็น process improvement (ทำไม dev ข้ามขั้นตอน? overload? ไม่รู้ DoD?) และแก้ที่ต้นตอ

**เกณฑ์ผ่าน:** ยึด DoD + แก้ต้นตอ ไม่ใช่แค่สั่งให้ทำใหม่

### 2. [Decision Case] flash sale กลาง sprint

**แนวตอบ:** ไม่รับเข้าสู่ sprint โดยตรง — เข้า Product Backlog, PO (คุณนภา) จัด priority; ถ้า Marketing อ้างว่า urgent ต้องผ่าน change process (Ch.7) และยอมรับผลต่อ Sprint Goal (Mobile App core booking) — ปกป้อง Sprint Goal ตามหลัก Agile

**เกณฑ์ผ่าน:** มีกระบวนการ (backlog/change) + ปกป้อง Sprint Goal + ไม่ขัด Scenario Master

### 3. [Artifact Review] sprint board ที่ทุกชิ้น Done แต่ไม่มี evidence

**แนวตอบ:** Board หลอกเพราะ "Done" ไม่ได้หมายถึง DoD — ไม่มี test result/review/security evidence → ไม่รู้ว่าจริง ๆ เสร็จแค่ไหน; แก้: ให้ Done ต้องมี evidence link (test case ID, review record, deploy status), ใช้ Definition of Done checklist ต่อ story, QA gate ก่อนย้าย column

**เกณฑ์ผ่าน:** เห็นว่ามันคือ status illusion + วิธีแก้เชิง process

### 4. [Trade-off Case] บังคับ DoD (ช้า 2 วัน) vs ปล่อยผ่านแล้วแก้ Ch.8

**แนวตอบ:** บังคับ DoD — defect ที่พบใน sprint แก้ภายในชั่วโมง/วัน; ที่พบใน UAT (Ch.8) แก้เป็นวัน/สัปดาห์ + กระทบ schedule/trust + rework ของ QA/PO — Cost of Quality: prevention ถูกกว่า failure; ช้า 2 วันวันนี้ถูกกว่าเสีย 2 สัปดาห์หน้า

**เกณฑ์ผ่าน:** อธิบายด้วย cost of quality + เห็นผลต่อ Ch.8/Ch.9

### 5. [Scenario Case] QA กับ dev ขัดแย้งเรื่อง test data

**แนวตอบ:** ใช้ Collaborate/Problem Solve ก่อน — หาต้นตอ (test data ไม่พร้อมจาก 2C2P? ไม่มี policy การเตรียม data?) — ถ้าต้องตัดสินใจเร่งด่วนใช้ Compromise หรือ escalate ตาม governance; บันทึกเป็น process improvement (test data readiness เข้า DoR) — ไม่เลือกข้าง ไม่หลีกเลี่ยง

**เกณฑ์ผ่าน:** เลือกเทคนิคตามสถานการณ์ + แก้ที่ระบบ ไม่ใช่โทษบุคคล

### 6. [Cross-Knowledge Analysis] 2C2P sandbox ช้า 1 สัปดาห์

**แนวตอบ:**
- Ch.6: Sprint 3–4 (Payment) ทำต่อไม่ได้เต็มที่ → ทำงานคู่ขนาน (design/unit test), blocker escalate
- Ch.7: variance ปรากฏใน status — ดูว่า critical path กระทบไหม, forecast เปลี่ยน, อาจเป็น change/risk trigger
- Ch.8: UAT payment scenario ช้า → กระทบ UAT scope/data — ต้องมี fallback (sandbox สำรอง, ม็อก)
- ต้องติดตาม trigger (R-02 dependency 2C2P) + update RAID

**เกณฑ์ผ่าน:** เห็นผลต่อเนื่องข้าม 3 บท + escalation/fallback

### 7. [Recall] QA vs QC

**แนวตอบ:** QA (Manage Quality) = ดูกระบวนการป้องกัน defect (design review, test readiness gate, checklist); QC (Control Quality) = ตรวจผลลัพธ์จริง (test execution, defect log, evidence) — จาก SHG: QA = test readiness gate ก่อนรับ story, QC = ผล UAT/SIT ใน Ch.8

**เกณฑ์ผ่าน:** แยกบทบาท + ยกตัวอย่าง scenario

## Rubric สรุป

| ระดับ | เกณฑ์ |
|---|---|
| Professional | ยึด DoD + แก้ต้นตอ, escalation มี evidence/owner, เห็น cost of quality |
| Usable | ตอบถูกประเด็น แต่ mechanism/evidence ยังหลวม |
| Incomplete | ปล่อยผ่าน/สั่งงานลอย ๆ ไม่มี process |

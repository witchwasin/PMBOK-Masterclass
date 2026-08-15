---
chapter: ch-08
title: "Verification, UAT และ Release Readiness (Playbook F)"
book: "PM Delivery Guide"
edition: Answer Key
status: Released
validation_status: Reviewed
last_reviewed: 2026-08-13
learner_chapter: ./ch-08-learner.md
---

# Answer Key — Chapter 08 (Verification/UAT)

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

### 1. [Decision Case] payment defect 8% + 3 โรงแรมยังไม่ทดสอบ

**แนวตอบ:** ไม่ Go เต็ม — เสนอ **Conditional Go (Soft Launch 3 โรงแรม)** ตาม Sprint 12 ของ Scenario Master: เงื่อนไข = fix defect critical + regression retest ผ่านภายใน due date, เพิ่ม UAT wave สำหรับ 3 โรงแรม (cancellation scenario), monitor payment failure < threshold ระหว่าง pilot, support/hypercare พร้อม — ถ้า rollback ยังไม่พร้อม ต้อง No-Go จนกว่าทดสอบ rollback — Authority: Sponsor (คุณจิรา) ตัดสิน

**เกณฑ์ผ่าน:** มี evidence (severity/retest/rollback), conditional มีเงื่อนไข + owner + due date, ไม่ขึ้น production โดยไม่มี rollback

### 2. [Decision Case] PO อยากเซ็น UAT ทั้งที่ coverage 85%

**แนวตอบ:** ไม่ปล่อยให้เซ็นแบบพิธี — options: (A) ขยาย UAT wave ให้ครบ 100% (ใช้เวลา), (B) Waiver + conditional sign-off ระบุ scenario ที่เลื่อน + due date + residual risk (ยอมรับอย่างเป็นทางการ), (C) ลด scope ของ sign-off ให้ตรงกับที่ทดสอบแล้ว — บันทึก residual risk + owner; อธิบายว่า coverage gap = requirement ที่ไม่ถูกพิสูจน์ → ย้ายความเสี่ยงไป Ch.9

**เกณฑ์ผ่าน:** มี options + residual risk decision + ไม่ปล่อยแบบเงียบ ๆ

### 3. [Artifact Review] dashboard สีเขียวที่ไม่มี evidence

**แนวตอบ:** ขาด: RTM coverage, defect severity/ageing, retest/regression result, data reconciliation, key-user participation, signed acceptance — ผล: สีเขียวคือความเห็น ไม่ใช่หลักฐาน; ตัดสินใจ Go จากข้อมูลไม่ครบ → defect แฝงไประเบิด Ch.9 — แก้: dashboard ต้องเชื่อม requirement → test → result → acceptance

**เกณฑ์ผ่าน:** ระบุสิ่งที่ขาด + ผล + วิธีแก้

### 4. [Scenario Case] cosmetic 20 ตัว vs payment critical 1 ตัว

**แนวตอบ:** Severity (QA): payment = Critical (กระทบการทำงานหลัก), cosmetic = Minor — Priority (PO): payment = Immediate, cosmetic = Low — ตัดสินใจ: fix critical ก่อน, cosmetic defer/waive — จำนวนรวมไม่ใช่ตัวชี้ขาด

**เกณฑ์ผ่าน:** แยก severity/priority ถูก + ตัดสินตาม impact

### 5. [Trade-off Case] Soft Launch 3 โรงแรม vs Full Launch

**แนวตอบ:**
- Soft launch (3 โรงแรม): ลด blast radius, เรียนรู้จากจริง, monitor ก่อนขยาย — แต่ campaign/benefit ช้า, สองกลุ่มประสบการณ์ไม่เท่ากัน
- Full launch: เร็ว ครบ 12 โรงแรม — แต่ถ้า payment ยังไม่เสถียร risk กระจายทั้งเครือ + support overload
- แนะนำ soft launch ตาม Scenario Master (Sprint 12) + criteria การขยายเต็ม

**เกณฑ์ผ่าน:** เห็น trade-off ครบ + เลือกตาม evidence/Scenario Master

### 6. [Cross-Knowledge Analysis] RTM coverage gap 15%

**แนวตอบ:** UAT schedule (Ch.8) ต้องขยายหรือเพิ่ม wave → กระทบ sprint 12 + soft launch วันที่ — Go-live (Ch.9) เสี่ยง: requirement ที่ไม่ถูกทดสอบอาจพังตอน production → เพิ่ม hypercare load, rollback trigger — ทางเลือก: เพิ่ม wave (ช้า), waiver + residual risk (ยอมรับ), หรือลด scope release — ต้องผ่าน governance (Ch.7)

**เกณฑ์ผ่าน:** เห็นผลต่อ Ch.8/Ch.9 + ทางเลือก + decision path

### 7. [Recall] Release Readiness องค์ประกอบ (F.7)

**แนวตอบ:** Scope Complete, Tests Pass, Critical Defects Closed, Security Accepted, Performance Accepted, Data Migration Tested, Monitoring Ready, Backup Ready, Rollback Ready, Training Complete, Support Ready, Communication Ready, Approval Ready

**เกณฑ์ผ่าน:** ระบุได้ ≥ 7 ข้อ

## Rubric สรุป

| ระดับ | เกณฑ์ |
|---|---|
| Professional | Evidence-based (RTM/severity/retest/rollback), conditional มีเงื่อนไข + owner + due date, authority ถูก |
| Usable | ตอบถูกประเด็น แต่ evidence/เงื่อนไขยังไม่ครบ |
| Incomplete | ตัดสินจากความรู้สึก/แรงกดดัน ไม่มี evidence |

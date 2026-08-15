---
chapter: ch-07
title: "Monitoring, Controlling และ Change Control (Playbook E)"
book: "PM Delivery Guide"
edition: Answer Key
status: Released
validation_status: Reviewed
last_reviewed: 2026-08-13
learner_chapter: ./ch-07-learner.md
---

# Answer Key — Chapter 07 (Monitoring & Change)

Instructor-facing only.

## Assessment Composition

| Section | Share | Type |
|---|---:|---|
| EVM Case | ~20% | Application |
| Decision Case | ~35% | Application |
| Artifact Review | ~15% | Artifact review |
| Scenario Case | ~10% | Application |
| Cross-Knowledge Analysis | ~10% | Application |
| Recall | ~10% | Retrieval |

## Model Answers

### 1. [EVM Case] PV = 7.5M, EV = 6.75M, AC = 7.5M

**แนวตอบ:**
- SV = 6.75 - 7.5 = -0.75M; CV = 6.75 - 7.5 = -0.75M
- SPI = 0.90; CPI = 0.90
- EAC = 12/0.90 ≈ 13.3M; VAC = 12 - 13.3 ≈ -1.3M
- Reserve: Contingency 1.5M — PM ใช้ได้ตาม governance (ต้องมี evidence + decision record); Management Reserve 1.5M — ต้อง Sponsor อนุมัติเท่านั้น
- ไม่ควรสรุปทันที — ถาม cause + evidence + trend

**เกณฑ์ผ่าน:** คำนวณถูก + แยก reserve + ถาม cause

### 2. [Decision Case] flash sale ก่อน launch

**แนวตอบ:** Impact ครบทุกด้าน: Scope (ฟีเจอร์ใหม่ใน sprint 9–10), Schedule (กระทบ critical path + load test), Cost (dev/QA/cloud), Quality (payment load test ต้องเพิ่ม), Resource (ทีมถูกดึง), Risk (payment stability กลาง campaign), Contract (ถ้า campaign ผูก vendor), Operation (support/partners), Benefits (conversion เทียบกับ stability) — แนะนำ defer ไปหลัง stabilization (Phase 2 ตาม Scenario Master §4) หรือ pilot เล็ก; Authority = CCB/Sponsor (กระทบ baseline); ถ้าอนุมัติ ต้อง baseline update + communication

**เกณฑ์ผ่าน:** impact ครบทุกด้าน + แนะนำตามหลักฐาน + authority ถูก

### 3. [Decision Case] PMS vendor ขอ T&M เพิ่ม 300K

**แนวตอบ:** options: (A) ใช้ Contingency 1.5M ตาม governance — เร็วแต่ต้อง evidence + record; (B) เจรจาให้ vendor รับส่วนหนึ่ง/แบ่ง milestone — ลดต้นทุนแต่ใช้เวลา; (C) ปฏิเสธและร้องขอ SOW/scope clarification — ถ้างานอยู่นอก SOW จริงต้องมี change; (D) ขอ Sponsor ใช้ Management Reserve ถ้าเกิน contingency — ต้อง approval — decision path: PM วิเคราะห์ → Commercial/Procurement ดู contract → CCB/Sponsor อนุมัติตาม threshold

**เกณฑ์ผ่าน:** มี options + trade-off + authority/evidence ครบ

### 4. [Artifact Review] Change Log ที่ไม่มี impact/baseline/approval

**แนวตอบ:** ขาด: impact analysis (ผลต่อ scope/schedule/cost/quality/risk), baseline update (อะไรเปลี่ยน), approval evidence (ใครอนุมัติ ตาม threshold ใด), communication — ผล: ไม่มีใครรู้ว่าตกลงอะไร, baseline ใช้ควบคุมไม่ได้, ตอนปิดโครงการ (Ch.10) เกิด dispute — แก้: change ต้องครบ flow (intake → impact → authority → baseline → communicate)

**เกณฑ์ผ่าน:** ระบุสิ่งที่ขาด + ผลที่เกิด + วิธีแก้

### 5. [Scenario Case] Sponsor อนุมัติด้วยวาจา

**แนวตอบ:** ขอบคุณ + ยืนยันผ่านระบบ: เขียน change request + impact pack ทันที, ส่ง email/decision record ให้ Sponsor ยืนยัน (formalize), รอ confirm ก่อน update baseline — อธิบายเหตุผลว่า baseline ที่ไม่มี evidence defend ไม่ได้ และป้องกันความเข้าใจผิดภายหลัง

**เกณฑ์ผ่าน:** ทำเป็นทางการโดยไม่ทะเลาะ + มีเหตุผล

### 6. [Cross-Knowledge Analysis] fast-track ทำให้ defect เพิ่ม

**แนวตอบ:**
- Ch.8 (UAT): defect มากขึ้น → UAT ล่าช้า, UAT sign-off เสี่ยง, ต้อง triage severity ดีๆ
- Ch.9 (Go-live): ถ้า defect สำคัญตกค้าง → go-live risk สูง, hypercare หนัก, rollback trigger อาจถูกใช้
- Monitor: defect trend, severity ageing, retest rate, UAT exit criteria — ถ้าจำเป็นต้องเลื่อน/แบ่ง release ต้องผ่าน governance (Ch.7)

**เกณฑ์ผ่าน:** เห็นผลต่อเนื่อง Ch.8/Ch.9 + สิ่งที่ต้อง monitor

### 7. [Recall] เงื่อนไข escalation (E.10)

**แนวตอบ:** เกินอำนาจ PM, กระทบ baseline, ต้องการ Sponsor decision, cross-project conflict, contract risk, security/legal, critical milestone, benefit at risk

**เกณฑ์ผ่าน:** ระบุได้ ≥ 5 ข้อ

## Rubric สรุป

| ระดับ | เกณฑ์ |
|---|---|
| Professional | EVM ถูก, impact ครบทุกด้าน, authority/reserve/evidence ถูกต้อง, มี decision record |
| Usable | ตอบถูกประเด็น แต่ impact/authority ยังไม่ครบ |
| Incomplete | ตอบลอย ๆ ไม่มีตัวเลข/evidence/authority |

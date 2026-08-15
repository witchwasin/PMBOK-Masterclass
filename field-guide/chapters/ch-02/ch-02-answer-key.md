---
chapter: ch-02
title: "Initiation — Charter, Stakeholder, Governance และ Kickoff (Playbook B)"
book: "PM Delivery Guide"
edition: Answer Key
status: Released
validation_status: Reviewed
last_reviewed: 2026-08-13
learner_chapter: ./ch-02-learner.md
---

# Answer Key — Chapter 02 (Initiation)

Instructor-facing only.

## Assessment Composition

| Section | Share | Type |
|---|---:|---|
| Decision Case | ~40% | Application |
| Trade-off Case | ~15% | Application |
| Artifact Review | ~15% | Artifact review |
| Executive Communication | ~10% | Application |
| Cross-Knowledge Analysis | ~15% | Application |
| Recall | ~5% | Retrieval |

## Model Answers

### 1. [Decision Case] Sponsor อยากให้ PM "จัดการทุกอย่างเอง" ไม่มี threshold

**แนวตอบ:** แนะนำให้กำหนด threshold แม้จะกว้าง:
- PM authority ควรเขียนเป็นตัวเลข + ขอบเขต (เช่น อนุมัติ minor change ≤ 500K, ใช้ contingency ตาม governance) แต่ baseline change (scope/เวลา/งบหลัก) ต้องผ่าน CCB
- Risk ถ้า PM มีอำนาจไม่จำกัด: ตัดสินใจผิดโดยไม่มี check, ไม่มี accountability trail, sponsor สูญเสียการกำกับ, และเมื่อพลาดจะกลายเป็น "PM คนเดียวผิด"
- เสนอ: เขียน Decision Rights Matrix แนบใน Charter

**เกณฑ์ผ่าน:** เสนอ threshold เป็นรูปธรรม + อธิบาย risk ของอำนาจไร้ขอบเขต

### 2. [Decision Case] Stakeholder Register มีแค่ 4 คน

**แนวตอบ:** กลุ่มที่ขาดตาม Scenario Master: คุณภัทร (VP Marketing/Business Owner — เจ้าของ KPI direct booking), คุณสมศรี (VP Ops — adoption/ops), คุณกาญจนา (Revenue Mgr — pricing), GM 12 โรงแรม (partner adoption), Front Desk (end users), 2C2P + PMS vendors (dependency), Marketing Agency, คุณธีร์ (UX Lead) — เหตุผล: แต่ละกลุ่มมีผลต่อ requirement, acceptance หรือ adoption; ถ้าข้ามจะพลาด requirement และเจอ resistance ตอน UAT/Go-live

**เกณฑ์ผ่าน:** ระบุกลุ่ม ≥ 4 ที่ขาด + เหตุผลเชื่อมกับ Ch.3 requirement หรือ Ch.8 UAT

### 3. [Trade-off Case] PM authority กว้าง vs แคบ

**แนวตอบ:**
- กว้าง: decision เร็ว, PM รู้สึก empowered — แต่ risk governance หลุด, sponsor ไม่เห็นภาพ
- แคบ: control แน่น, accountability ชัด — แต่ escalation ท่วม, PM กลายเป็นคนเดินเอกสาร, decision latency สูง
- ข้อเสนอสำหรับ 12M: PM อนุมัติ minor ≤ 500K และ operational decisions; CCB อนุมัติ baseline change; Sponsor อนุมัติ budget change เกิน contingency

**เกณฑ์ผ่าน:** อธิบายทั้งสองฝั่ง + เสนอ threshold ที่สอดคล้องขนาดโครงการ

### 4. [Artifact Review] Charter ที่ PM เขียนเอง Sponsor แค่เซ็น ไม่มี exit criteria

**แนวตอบ:**
- PM เขียนเอง = Sponsor ไม่ได้ ownership → เมื่อเกิด conflict Sponsor จะไม่ defend ทิศทางโครงการ
- ไม่มี exit criteria = ไม่รู้ว่า "เสร็จเมื่อไร" → closure (Ch.10) จะเถียงกัน
- ไม่มี PM authority = escalation ไม่มีเจ้าภาพ
- แก้: Sponsor ต้อง review + แก้ draft เองบางส่วน, เพิ่ม success criteria + exit criteria + PM authority

**เกณฑ์ผ่าน:** ระบุจุดพัง ≥ 3 + วิธีแก้

### 5. [Executive Communication] ทำไมต้องมี Steering Committee + PM threshold

**แนวตอบ:** Steering Committee ทำให้ decision ใหญ่มีผู้มีอำนาจตัดสินใจร่วมกันตามข้อมูล ไม่ใช่คนเดียว/เสียงดัง และ PM threshold ทำให้งานเล็กตัดสินใจได้เร็วโดยไม่รบกวนผู้บริหาร — สมดุลระหว่าง speed กับ control ลด decision latency ที่เป็นต้นทุนแฝงของโครงการ

**เกณฑ์ผ่าน:** กระชับ, โยงกับ value/risk, อ่านจบแล้ว CEO เห็นว่า "ทำไมต้องทำ"

### 6. [Cross-Knowledge Analysis] CFO อยากตัดสินใจเรื่องงบทุกครั้ง

**แนวตอบ:**
- ผลต่อ Ch.4 (Cost): ทุก cost decision ต้องรอ CFO → baseline อนุมัติช้า, ช่องว่างระหว่างราคาที่คาดกับอนุมัติ
- ผลต่อ Ch.7 (Change): ทุก change ที่มีผลเงิน (แม้ minor) ผ่าน CFO → CCB อืด, change queue ค้าง, ทีม workaround นอกระบบ
- การปรับ: ให้ CFO มี decision right เฉพาะงบที่เกิน threshold (เช่น > 500K) หรือเป็น Steering member ไม่ใช่ single approver ทุกรายการ; กำหนด decision SLA

**เกณฑ์ผ่าน:** เห็นผลข้าม Ch.4/Ch.7 + เสนอ governance adjustment ที่รักษา balance

### 7. [Recall] Stakeholder Register vs Power-Interest Grid

**แนวตอบ:** Register คือบันทึกข้อมูล stakeholder (role, interest, influence, needs, strategy) ส่วน Grid คือเครื่องมือวิเคราะห์เพื่อเลือก engagement approach — Register มีข้อมูล, Grid ช่วยตัดสินใจ

**เกณฑ์ผ่าน:** แยกบทบาทของสองสิ่งนี้ได้

## Rubric สรุป

| ระดับ | เกณฑ์ |
|---|---|
| Professional | เสนอ threshold/governance เป็นรูปธรรม, อ้าง Scenario Master, มี owner + evidence |
| Usable | ตอบถูกประเด็น มีทางเลือก แต่ยังไม่ระบุ threshold/owner |
| Incomplete | ความเห็นลอย ๆ ไม่มีตัวเลข/mechanism |

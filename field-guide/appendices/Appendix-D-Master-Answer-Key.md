---
title: "Appendix D — Master Answer Key (รวมทุกบท)"
book: "PM Delivery Guide (Ver.2)"
document_type: Appendix
version: 1.0
status: Draft
last_reviewed: 2026-08-13
related_reference: ../../governance/COURSE_STANDARD.md
---

# Appendix D — Master Answer Key (รวมทุกบท)

> Instructor-facing only. ไฟล์นี้คือดัชนีรวมคำตอบ Assessment ของทุกบท — คำตอบเต็มอยู่ใน answer-key ของแต่ละบท (ลิงก์ในตาราง) หลักการประเมินร่วมทุกบท: **decision-based ≥ 90% ของน้ำหนัก, ใช้ rubric เกณฑ์ผ่าน ไม่ใช่คำตอบเดียวที่ถูก** (ตาม `COURSE_STANDARD.md`)

## ภาพรวม Assessment ต่อบท

| บท | จำนวนข้อ | ลักษณะเด่น | Answer Key เต็ม |
|---|---|---|---|
| Ch.0 | — | ไม่มี Assessment (บทปฐมบท) — มี Discussion Prompts | [ch-00-answer-key.md](../chapters/ch-00/ch-00-answer-key.md) |
| Ch.1 | 7 | Pre-sales: Decision + Trade-off (Fixed vs T&M) | [ch-01-answer-key.md](../chapters/ch-01/ch-01-answer-key.md) |
| Ch.2 | 7 | Initiation: Charter, Authority, Stakeholder | [ch-02-answer-key.md](../chapters/ch-02/ch-02-answer-key.md) |
| Ch.3 | 7 | Scope/WBS: MVP, WBS, 100% Rule | [ch-03-answer-key.md](../chapters/ch-03/ch-03-answer-key.md) |
| Ch.4 | 7 | Schedule/Cost/Resource + EVM Case | [ch-04-answer-key.md](../chapters/ch-04/ch-04-answer-key.md) |
| Ch.5 | 7 | Risk/Procurement/Comms/Quality-Plan | [ch-05-answer-key.md](../chapters/ch-05/ch-05-answer-key.md) |
| Ch.6 | 7 | Execution: DoD, QA/QC, Sprint กลางทาง | [ch-06-answer-key.md](../chapters/ch-06/ch-06-answer-key.md) |
| Ch.7 | 7 | Monitoring: EVM, Change Control, Escalation | [ch-07-answer-key.md](../chapters/ch-07/ch-07-answer-key.md) |
| Ch.8 | 7 | Verification/UAT: Release Readiness, UAT gate | [ch-08-answer-key.md](../chapters/ch-08/ch-08-answer-key.md) |
| Ch.9 | 7 | Go-Live/Hypercare: Cutover, Rollback, Stabilization | [ch-09-answer-key.md](../chapters/ch-09/ch-09-answer-key.md) |
| Ch.10 | 7 | Closure: Handover, Benefit Owner, Exit Criteria | [ch-10-answer-key.md](../chapters/ch-10/ch-10-answer-key.md) |

## เกณฑ์ผ่านร่วมทุกบท (rubric กลาง)

1. **Decision Case** — ผ่านเมื่อ: ระบุ missing information ได้, เสนอ options ≥ 3 พร้อมเกณฑ์เลือก, ไม่ตอบ "รับเลย/ทำเลย" โดยไม่มี evidence
2. **Trade-off Case** — ผ่านเมื่อ: ชี้ trade-off ทั้ง 2 ด้าน + แนะนำทางเลือกพร้อมเหตุผลที่ผูกกับ business objective ของ SHG (12M budget, 35% direct booking, launch ก่อน 1 พ.ย.)
3. **Artifact Review** — ผ่านเมื่อ: เจอจุดบกพร่องของ artifact ครบตามเกณฑ์ของบท (ไม่ใช่แค่ "ชื่อเอกสารมี")
4. **Executive Communication** — ผ่านเมื่อ: พูดกับผู้บริหารด้วย risk + option + recommendation ไม่ใช่ technical detail
5. **Cross-Knowledge Analysis** — ผ่านเมื่อ: เชื่อมผลกระทบข้ามบท (เช่น fast-track → defect → UAT scope) ครบสายเหตุผล
6. **Recall** — ตรวจว่าแม่นยำตรงกับ Playbook section ที่ระบุ (เช่น G.8, H.9, E.10)

## สรุปคำตอบสำคัญรายบท (แนวตอบย่อ — ดูไฟล์เต็มเพื่อ rubric รายข้อ)

### Ch.1 — Pre-sales
1. ลูกค้าขอเพิ่ม Mobile App → ไม่ตอบรับทันที, ขอ evidence + Impact Analysis, เสนอ Base/Option หรือ Phase 2
2. Sales เสนอ 9M แต่ ROM 9.5–12M → อย่าต่ำกว่า ROM โดยไม่มีเหตุผล; ลด scope / เพิ่ม budget / No-Bid
3. Fixed vs T&M เมื่อ PMS API ไม่ชัด → Hybrid: fixed core + T&M มี cap สำหรับ adapter
4. Proposal ไม่มี Out of Scope/Assumptions → ปฏิเสธส่ง; อ้างว่าผูก contract ภายหลัง
5. Paid Discovery Phase → อธิบาย CEO ด้วย value: ลด delivery risk > ค่าใช้จ่าย
6. launch ก่อน High Season แต่ PMS ใช้ 6 เดือน → ตั้งคำถาม feasibility ตั้งแต่ต้น, option รวม cutover windows
7. ROM ≠ ราคาผูกพัน → ROM คือช่วง estimate มี basis; ราคาผูกพันหลัง SOW

### Ch.2 — Initiation
1. Sponsor อยากให้ PM จัดการเอง ไม่มี threshold → ต้องล็อก PM authority + escalation threshold ใน Charter
2. Stakeholder Register 4 คน → ขาดทีม 2C2P/PMS/โรงแรม; ใช้ RACI + power-interest สแกนต่อ
3. PM authority กว้าง vs แคบ → กว้าง = คล่องตัว, แคบ = ควบคุม; เลือกตามความเสี่ยงโครงการ
4. Charter PM เขียนเอง Sponsor เซ็น ไม่มี exit criteria → Charter ต้องมี goal/budget/threshold/exit criteria
5. Steering Committee + threshold → สร้าง escalation path ชัด, กัน PM รับความเสี่ยงคนเดียว
6. CFO ตัดสินใจงบทุกครั้ง → จัด role: CFO = sponsor finance, PM = day-to-day; threshold กำหนดไว้
7. Stakeholder Register vs Power-Interest Grid → Register = ข้อมูล, Grid = เครื่องมือจัดลำดับ engagement

### Ch.3 — Scope/WBS
1. เพิ่ม loyalty program ใน MVP → ทดสอบกับ objective: ไม่ช่วย 35% direct booking ใน 18 เดือน → ไม่เข้า MVP
2. "รายงานทุกอย่าง" → ขอ criteria: ใครใช้, ตัดสินใจอะไร, ความถี่; ตัดให้เหลือที่ใช้งานจริง
3. WBS แตกตามแผนก → ผิด: ต้องแตกตาม deliverable (100% Rule)
4. SRS/FSD เต็ม vs User Story + AC → เลือกตามความเสี่ยง: fixed-price ใช้ SRS, ภายในใช้ story + AC
5. WBS "Payment Integration" → แตกถึง work package + criteria เสร็จ
6. PMS API ไม่รองรับ real-time → ตรวจ constraint ตั้งแต่ requirement, มี fallback design
7. 100% Rule → ลูกหลานรวมกัน = พ่อแม่พอดี ไม่เกินไม่ขาด

### Ch.4 — Schedule/Cost/Resource
1. Payment Integration ช้า 1 สัปดาห์ → ดูก่อนว่าอยู่ critical path หรือไม่ → แล้วเลือก crashing/fast-track/re-baseline
2. 80 key users ไม่ว่าง UAT → มี mitigation ตั้งแต่วางแผน resource (ช่วงเวลา, สำรองผู้ใช้)
3. EVM: PV=6M, EV=5M, AC=6.5M → SPI 0.83, CPI 0.77 → behind + over budget → corrective action
4. Crashing vs Fast Tracking → crashing เพิ่ม cost ลด duration; fast-track ทำงานคู่ขนาน เพิ่ม rework risk
5. Gantt ไม่มี dependency/owner/basis → ปฏิเสธ; CPM ต้องพึ่ง dependency + duration ที่มี basis
6. Resource Plan + RACI สำหรับ UAT → ระบุใครทำอะไร + conflict (UAT users ทำงานประจำ) มีสำรอง
7. Effort ≠ Duration → effort คือคน-ชั่วโมง, duration คือเวลาจริง (คนเพิ่ม ≠ duration ลดเสมอ)

### Ch.5 — Risk/Procurement/Comms/Quality-Plan
1. Risk "key users ไม่ว่าง UAT" → มี owner, มี trigger, มี response (สำรอง, ช่วงเวลา, incentive)
2. 2C2P fee ต่ำแต่ SLA อ่อน → ประเมิน cost of poor SLA (settlement delay) มากกว่า fee
3. Conditional gate vs เลื่อน 2 สัปดาห์ → gate แบบมีเงื่อนไข (risk-based) เมื่อ evidence พอ; เลื่อนเมื่อไม่
4. Risk register "ทีมไม่พร้อม" → ต้องมี: owner, likelihood/impact, response, trigger, วันที่ทบทวน
5. Test Strategy ล็อกก่อน build → กำหนด QA scope/เกณฑ์ผ่าน/รอบ ก่อนงานเริ่ม; เปลี่ยนทีหลังแพง
6. settlement 2 วันทำการ → กระทบ booking flow + hypercare; ต้องแจ้ง stakeholders ตั้งแต่ plan
7. Verification vs Validation → Verification = ตรง spec ไหม, Validation = ตรง need ไหม

### Ch.6 — Execution
1. story เสร็จแต่ไม่มี unit test/security check → ยังไม่ Done; DoD เป็นสัญญาทีม ไม่ยืดหยุ่นตามแรงกด
2. flash sale กลาง sprint → เข้า change management: impact + decision โดยไม่ทำลาย sprint goal
3. sprint board ทุกชิ้น Done แต่ไม่มี evidence → Done ≠ done; ตรวจ artifact/definition
4. บังคับ DoD (ช้า 2 วัน) vs ปล่อยแล้วแก้ Ch.8 → บังคับ DoD; defect ช้าแพงกว่า
5. QA กับ dev ขัดแย้ง test data → PM แก้ root cause (test data plan) ไม่ใช่จับคนกลาง
6. 2C2P sandbox ช้า 1 สัปดาห์ → vendor dependency: escalate + fallback + กันผลกระทบต่อ sprint
7. QA vs QC → QA = กระบวนการ (ป้องกัน), QC = ตรวจผล (ตรวจจับ)

### Ch.7 — Monitoring & Change
1. EVM: PV=7.5M, EV=6.75M, AC=7.5M → SPI 0.9, CPI 0.9 → behind + over → วิเคราะห์ variance ก่อน action
2. flash sale ก่อน launch → เข้า PICC: impact ต่อ scope/schedule/cost/risk → decision โดย CCB/sponsor
3. PMS vendor ขอ T&M เพิ่ม 300K → ตรวจ contract + change control; ไม่จ่ายนอก process
4. Change Log ไม่มี impact/baseline/approval → ปฏิเสธ; ทุก change ต้องมี 3 อย่างนี้
5. Sponsor อนุมัติด้วยวาจา → ขอ confirmation เป็นลายลักษณ์อักษร; oral ≠ change
6. fast-track ทำให้ defect เพิ่ม → ยอมรับ trade-off หรือชะลอ; ติดตาม quality metric ควบคู่
7. escalation (E.10) → เงื่อนไขชัด: budget/time threshold, sponsor unavailable, vendor breach

### Ch.8 — Verification/UAT
1. payment defect 8% (threshold 4%) + 3 โรงแรมยังไม่ทดสอบ → ยังไม่ release-ready; เกณฑ์ผ่านไม่ยืดหยุ่น
2. PO อยากเซ็น UAT ที่ coverage 85% → ไม่; ขอ evidence + แผนปิด gap หรือ conditional sign-off ระบุความเสี่ยง
3. dashboard สีเขียวไม่มี evidence → ตรวจ evidence (log, จำนวนเคส, บันทึก) ไม่ใช่สี
4. cosmetic 20 ตัว vs payment critical 1 ตัว → priority ตาม impact; critical ก่อน, cosmetic เข้า backlog
5. Soft Launch 3 โรงแรม vs Full Launch → soft launch ลด risk, เก็บ learning; เหมาะเมื่อ readiness ไม่เต็ม
6. RTM coverage gap 15% → ไม่ผ่าน gate; ระบุ gap + แผนปิด ก่อน UAT สรุปผล
7. Release Readiness (F.7) → องค์ประกอบ: ผล QA/UAT, RTM ครบ, เกณฑ์ผ่าน, rollback, owner, sign-off

### Ch.9 — Go-Live/Hypercare
1. payment failure 6% (threshold 4%) → อยู่เหนือเกณฑ์ → escalate; ระงับ/ชะลอ cutover ตามแผน
2. คืนก่อน cutover พบ rollback ยังไม่ทดสอบ → หยุด; rollback ไม่ทดสอบ = ยังไม่ go/no-go ได้
3. cutover plan ไม่มี owner/sequence/validation/trigger → ปฏิเสธ; 4 องค์ประกอบนี้ขาดไม่ได้
4. โรงแรมที่ 3 ไม่พร้อม → ลดขอบเขต cutover (เลื่อนโรงแรมที่ 3) หรือเลื่อนทั้ง cutover — ตาม impact
5. Rollback vs Fix-in-place → rollback เมื่อ risk สูง/ไม่รู้ root cause; fix-in-place เมื่อเล็กและรู้สาเหตุ
6. PMS sync error 5% หลัง hypercare → ตัดสินใจ: rollback บางส่วน / fix-in-place / ขยาย hypercare ตาม SLA
7. Stabilization criteria (G.8) → เกณฑ์ที่ทำให้ hypercare จบได้: metrics อยู่ในเกณฑ์ x วันติด

### Ch.10 — Closure
1. PMS known issue ค้างก่อน closure → ไม่ออกจาก hypercare ยัง; ย้ายเป็น operational backlog + owner
2. คุณภัทรไม่ยืนยัน benefit owner → closure ไม่จบ; ต้องมี operational + benefit owner ระบุ
3. Closure Report ไม่มี handover/lessons/benefit → ไม่ผ่าน; 3 ส่วนนี้บังคับ
4. 2C2P final invoice ไม่ตรง → ตรวจ contract + deliverable + sign-off ก่อนจ่าย; dispute ผ่าน process
5. ปิดเร็ว (ปล่อยทีม) vs ปิดช้า → ปิดเร็วเสี่ยง knowledge loss; ปิดช้าเสีย cost — ชั่งกับ readiness จริง
6. 6 เดือนหลัง launch direct booking 20% (ไม่ถึง 35%) → ติดตาม benefit; วิเคราะห์ gap + แผนปรับ (ไม่ใช่ปิดแล้วลืม)
7. Exit Criteria (H.9) → ครบ: scope ส่งมอบ, acceptance, handover, lessons, benefit baseline, financial close

## วิธีใช้

- **Instructor:** ใช้ rubric รายข้อในไฟล์ answer-key เต็มของแต่ละบท (ลิงก์ตารางบน) — ไฟล์นี้เป็น index สำหรับรวมผลสอบหลายบท
- **การให้คะแนนรวม:** ใช้ Assessment Composition ต่อบท (ใน answer-key เต็ม) — application/judgement ≥ 90% ของน้ำหนักตาม `COURSE_STANDARD.md`

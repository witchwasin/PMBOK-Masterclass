---
chapter: ch-07
title: "Monitoring, Controlling และ Change Control (Playbook E)"
book: "PM Delivery Guide: From Pre-sales to Closure — คู่มือปฏิบัติการบริหารโครงการซอฟต์แวร์ (PMBOK 8th Edition)"
edition: Learner
status: Released
validation_status: Reviewed
last_reviewed: 2026-08-15
intended_learner_level: Experienced PM
difficulty: Core
estimated_study_time: 100
prerequisite:
  - "Ch.6 — Execution (Work Performance Data)"
  - "Ch.4 — Schedule/Cost/Resource (EVM)"
related_chapters:
  - "Ch.2 — Initiation (Integration ท่อนที่ 1: Charter)"
  - "Ch.10 — Transition & Closure (Integration ท่อนที่ 3: Close)"
canonical_source:
  - ../../references/PMBOK-Overview.md (PMBOK framework)
  - ../../e-Book/chapters/lesson-05/lesson-05-learner.md (Perform Integrated Change Control)
  - ../../e-Book/chapters/lesson-09/lesson-09-learner.md (Cost Control / EVM ฝั่ง Control)
  - ../../e-Book/chapters/lesson-08/lesson-08-learner.md (Control Schedule)
scenario_version:
  hotel_booking: "1.0"
artifact_outputs:
  - name: Status Report + Variance/Forecast
    creator: PM
    artifact_owner: PM
    reviewer: Sponsor, Stakeholders
    approval_authority: PM (report) / Steering (decision)
    approval_evidence: Report cadence + decision records
  - name: Change Log + Impact Pack + Decision Record
    creator: PM + Impact Owners
    artifact_owner: PM
    reviewer: CCB/Impact Owners
    approval_authority: PM (minor ตาม threshold) / CCB-Sponsor (baseline)
    approval_evidence: Approved change log + updated baselines
  - name: Updated RAID + Issue Log
    creator: PM + Owners
    artifact_owner: PM
    reviewer: Sponsor
    approval_authority: ตาม Governance
    approval_evidence: RAID review record
---

# Chapter 07 — Monitoring, Controlling และ Change: วัดจริง ควบคุม และอนุมัติการเปลี่ยนแปลง

## 1. Opening Scenario Hook

**[Teaching Scenario]** เดือนที่ 5 ของ SHG: Sprint 9–10 กำลังจะจบ แต่รายงานพบว่า CPI = 0.90 และ Sprint 7–8 (Back Office + Inventory Sync) ล่าช้า 1 สัปดาห์ พร้อมกันนี้คุณภัทร (VP Marketing) ขอเพิ่ม "flash sale campaign" และคุณวีระ (CTO) แจ้งว่า PMS vendor ขอค่าใช้จ่ายเพิ่มสำหรับ adapter พิเศษ

**[PMBOK 8]** ผู้บริหารหลายคนจะถาม "แล้วจะทัน launch ไหม" ทีมอาจตอบ "เดี๋ยวเร่งให้" แต่ PM ต้องทำมากกว่านั้น: วัด variance เทียบ baseline, forecast ผลลัพธ์, หาสาเหตุ และพาทุกคำขอเปลี่ยนแปลงเข้าสู่ **Perform Integrated Change Control** — เพราะ Integration ทำงานตลอดโครงการ (ท่อนที่ 2 ของ 3 ท่อน: Charter = Ch.2, Change = บทนี้, Closure = Ch.10)

## 2. Why It Matters

**[PMBOK 6]** Monitoring & Controlling ไม่ได้เริ่มหลัง Execution เสร็จ — เกิดควบคู่กัน: Collect Actuals → Compare with Baseline → Analyze Variance → Forecast → Identify Cause → Develop Options → Decide → Implement → Verify

**[Best Practice]** ถ้าไม่มีระบบนี้: สีเขียวบนรายงานคือความเห็น, change ถูกอนุมัติด้วยวาจา, baseline ค่อย ๆ เลื่อนโดยไม่มีใครสังเกต และ sponsor ตัดสินใจจากข้อมูลที่คลาดเคลื่อน — ระบบ monitoring + change control คือสิ่งที่ทำให้ "การบริหาร" ต่างจาก "การตามงาน"

## 3. Mental Model

```text
Work Performance Data (Ch.6)
  -> Collect Actuals (daily/weekly)
  -> Compare with Baseline (schedule/cost/scope)
  -> Variance + Forecast (SPI/CPI/EAC, critical path)
  -> Identify Cause (ทำไม — ไม่ใช่แค่เท่าไร)
  -> Develop Options + Decide (มี governance)
  -> Implement + Verify
ควบคู่กัน:
  Change Intake -> Impact Analysis -> CCB Decision -> Baseline Update
  RAID Review (ต่อเนื่อง) + Escalation (เมื่อเกินอำนาจ)
  -> สถานะพร้อมส่ง Ch.8 (Verification/UAT)
```

## 4. Main Lesson

### 4.1 Monitoring Cycle (E.3) + Status Reporting (E.4)

**[Best Practice]** รายงานต้องตอบ: ตอนนี้อยู่ที่ไหน / เทียบแผนเป็นอย่างไร / อะไรเปลี่ยน / ทำไม / กระทบอะไร / ต้องตัดสินใจอะไร / ใครต้องทำอะไร / ภายในเมื่อไร

**[Teaching Scenario]** Status รายสัปดาห์ของ SHG: CPI/SPI, critical path health, defect trend, RAID update, decision ask (พร้อม deadline)

### 4.2 Schedule Control (E.6)

**[PMBOK 6]** ดู: Actual Start/Finish, Remaining Duration, Critical Path, Float, Milestone Variance, Forecast Finish, Recovery Plan — delay ต้องถูกเทียบกับ critical path (บทเรียน Ch.4) ก่อนสรุป

### 4.3 Cost Control และ EVM (E.7) — จาก lesson-09

**[PMBOK 6]** ใช้เมื่อข้อมูลและ governance เหมาะสม:
```text
SV = EV - PV | CV = EV - AC | SPI = EV/PV | CPI = EV/AC
EAC = BAC/CPI (trend เดิม) | VAC = BAC - EAC
```

**[Best Practice]** ตัวเลข < 1 เป็นประตูคำถาม ไม่ใช่คำตอบ — ถาม: variance มาจาก cost/schedule/completion? EV มี evidence จริง? one-time หรือ trend? reserve ใดใช้ได้ ใครอนุมัติ?

**[Best Practice]** ความหมายเชิงบริหารของ CPI < 1: ด้วยงานที่ทำได้จริง (EV) เราใช้เงินมากกว่าแผน (AC) — คำถามที่ต้องตอบไม่ใช่ "เกินเท่าไร" แต่คือ **"จะจบด้วยงบเท่าไร (EAC) และต้องตัดสินใจอะไร"**: ลดงาน (scope cut), หางบเพิ่ม (reserve/sponsor), หรือเพิ่ม efficiency (re-plan) — เช่นเดียวกับ SPI < 1 ต้องตอบว่า "จะจบเมื่อไร และจะเร่งอะไรโดยไม่เสีย quality" — ตัวเลขคือจุดเริ่มต้นของการตัดสินใจ ไม่ใช่จุดจบของการรายงาน

**[Teaching Scenario]** SHG ณ เดือนที่ 5: ถ้า PV = 7.5M, EV = 6.75M, AC = 7.5M → SPI = 0.90, CPI = 0.90, EAC ≈ 12/0.90 = 13.3M, VAC ≈ -1.3M → ยังพอรับได้ใน Contingency 1.5M แต่ต้องถามสาเหตุและตั้ง forecast ใหม่ — ห้ามเอา Management Reserve 1.5M มาใช้โดยไม่ผ่าน Sponsor

### 4.4 Validate Scope vs Control Scope (E.8)

**[PMBOK 6]**
- **Validate Scope:** ลูกค้า/Sponsor ตรวจรับ deliverable (acceptance evidence) — กระบวนการตรวจรับจริงเต็มรูปแบบอยู่ Ch.8
- **Control Scope:** ควบคุมการเปลี่ยน Scope Baseline — ทุก change ผ่านกระบวนการ

### 4.5 Perform Integrated Change Control (E.5) — หัวใจของบท

**[PMBOK 6]** Change Flow:
```text
Submit Request -> Log -> Check Baseline -> Clarify -> Impact Analysis
-> Develop Options -> Recommend -> Change Authority Decision
-> Update Plan/Baseline -> Communicate -> Implement -> Verify -> Close
```

**[Teaching Scenario]** ตัวอย่าง change flow จริง: ลูกค้าขอเพิ่ม "ชำระด้วย TrueMoney" — **Submit** (PO เขียน change request + เหตุผล business) → **Log** → **Impact Analysis**: Scope (เพิ่ม payment gateway 1 ตัว), Schedule (Sprint 10 +2 วัน — อยู่บน critical path → เสี่ยง launch), Cost (+150K integration + T&M vendor), Quality (ต้องเพิ่ม load test + regression), Risk (ลด conversion risk — ตรงกับ Scenario Master §4), Contract (ต้องคุยกับ 2C2P) → **CCB ตัดสินใจ**: อนุมัติแบบมีเงื่อนไข (เลื่อนไป sprint หลัง launch เพื่อไม่กระทบ high season) → **Baseline Update + สื่อสาร** → **Implement → Verify** — ทุกขั้นมีบันทึก ไม่มีอะไร "ผ่านด้วยวาจา"

**Impact Areas ต้องดูครบ** — change หนึ่งตัวกระทบอะไรบ้าง:

| ด้าน | คำถามที่ต้องตอบ |
|---|---|
| Scope | งานเพิ่ม/ลดอะไร? deliverable เปลี่ยนไหม? |
| Schedule | กระทบ critical path ไหม? ล่าช้ากี่วัน? |
| Cost | งบเพิ่มเท่าไร? reserve ตัวไหนใช้ได้ ใครอนุมัติ? |
| Quality | acceptance criteria เปลี่ยนไหม? ต้อง test อะไรเพิ่ม? |
| Resource | ต้องคนเพิ่ม/ทักษะใหม่ไหม? มี capacity ไหม? |
| Risk | สร้าง risk ใหม่ หรือลด risk เดิม? |
| Contract | vendor scope/SOW เปลี่ยนไหม? ราคา/เงื่อนไข? |
| Operation | กระทบกระบวนการใช้งาน/การดูแลหลัง go-live? |
| Benefits | กระทบตัวเลข outcome (35% direct booking) หรือไม่? |

**Change Authority:** PM อนุมัติ minor ตาม threshold; PO จัด priority; Sponsor/CCB อนุมัติ baseline change; Commercial/Legal อนุมัติ contract change

**[Best Practice]** Integrated Change Control ไม่ได้มีไว้เพื่อปฏิเสธ change — มีไว้เพื่อให้ change ที่ควรทำถูกอนุมัติด้วยความเข้าใจผลกระทบ และ change ที่ยังไม่ควรทำถูกเลื่อน/แบ่งเฟสอย่างมีเหตุผล — แยก Issue (เกิดแล้ว) ออกจาก Change Request (ขอปรับ baseline)

### 4.6 RAID Review และ Escalation (E.9–E.10)

**[Best Practice]** Risk/Assumption/Issue/Dependency ต้อง review ต่อเนื่อง — Escalate เมื่อ: เกินอำนาจ PM, กระทบ baseline, ต้องการ Sponsor decision, cross-project conflict, contract risk, security/legal, critical milestone, benefit at risk

## 5. PM Decision Thinking

```text
Decision: flash sale campaign ของคุณภัทร + ค่าใช้จ่าย PMS adapter เพิ่ม — approve/reject/defer/split อย่างไร
Owner: PM ทำ impact analysis; CCB/Sponsor ตัดสินตาม governance; Commercial/Legal สำหรับ contract impact
Inputs: charter, baselines, status reports, change request, risk register, quality evidence, contract
Options:
  A: Approve ทั้งคู่ — ต้องมีงบ/เวลา/scope ใหม่ + baseline update
  B: Approve แบบมีเงื่อนไข (flash sale defer ไปหลัง stabilization; adapter ใช้ contingency ตาม governance)
  C: Reject/split — flash sale ไป Phase 2 (Scenario Master: feature ใหม่ = Phase 2+), adapter เจรจา contract
Trade-offs: business value vs delivery risk, speed vs stability, local request vs enterprise outcome
Risk: อนุมัติโดยไม่เห็นผลกระทบ -> baseline ใช้ควบคุมไม่ได้
Evidence: integrated impact pack, decision record, updated baselines, communication
Next Action: ตัดสินใจ -> update plan/baseline/log -> สื่อสาร -> verify หลัง implement
```

## 6. ตัวอย่างจริงจาก Case ต่อเนื่อง (SHG)

**[Teaching Scenario] Watch PM Think — เดือนที่ 5 ก่อน CCB รอบเดือน**

รายงานรายสัปดาห์เพิ่งออก: SPI = 0.90, CPI = 0.90 — คุณสุทธิ (PM) ไม่สรุปทันทีว่า "แย่" แต่ถามคำถามต่อ: "variance มาจากไหน — cost, schedule หรือ completion? Sprint 7–8 ที่ล่าช้า 1 สัปดาห์อยู่บน critical path หรือไม่?" — เขารู้จาก Ch.4 ว่าต้องเทียบกับ critical path ก่อนสรุป: ใช่ มันอยู่บนเส้นวิกฤติ กระทบ launch — เขาเสนอ recovery: fast-track บางส่วนของ Back Office + เพิ่ม QA คู่ขนาน แล้ว monitor ใหม่ทุกสัปดาห์

พร้อมกันนั้นมี 2 change เข้ามา: flash sale ของคุณภัทร และ PMS adapter ที่ vendor ขอ T&M เพิ่ม 300K เกิน cap — เขาไม่ตอบตกลงทันที แต่ทำ impact analysis ทีละตัว: flash sale → กระทบ scope + sprint 9–10 + payment load test → เสนอ defer ไป Phase 2 (ตาม Scenario Master §4) หรือทำ pilot เล็กหลัง stabilization → CCB อนุมัติ defer; adapter → กระทบ cost baseline → เสนอใช้ Contingency 1.5M ตาม governance + ขอ vendor แบ่ง milestone → Sponsor อนุมัติแบบมีเงื่อนไข

RAID: R-01 (PMS API) ใกล้ trigger — เขาเพิ่ม daily data review + บังคับ vendor SLA — "risk ที่ไม่ monitor คือ issue ที่กำลังก่อตัว"

**[PMBOK 8]** สังเกต: ทุกการตัดสินใจมี decision record, baseline update และ communication — ไม่มีอะไรผ่าน "ด้วยวาจา"

## 7. จุดตัดสินใจและกับดักที่พบบ่อย

**Common Mistakes:**

1. ปล่อย change ผ่านคำพูด — ผล: ไม่มีใครจำได้ว่าตกลงอะไร baseline ไหนเปลี่ยน
2. Issue กับ Change Request ปนกัน — ผล: แก้ issue โดยไม่รู้ว่า baseline เปลี่ยน
3. ดูแค่ % complete โดยไม่ดู EV/evidence — ผล: รายงานเขียวแต่ของจริงไม่เสร็จ
4. ใช้ Funding Envelope (12M) เป็นข้ออ้างเลี่ยง governance — ผล: reserve หมดโดยไม่มีเหตุผล
5. รอ "ถึงเวลาจริง" ค่อย monitor — ผล: ปัญหาสะสมจน recovery แพง
6. Escalate ทุกอย่าง (หรือไม่ escalate เลย) — ผล: เสียงดังกลบ decision หรือ decision ช้าเกินไป
7. Baseline เปลี่ยนแต่ไม่ update ทุกฝ่าย — ผล: ทีมวางแผนจากแผนเก่า

**Common Misconceptions:**

| ความเข้าใจผิด | ความจริง |
|---|---|
| Monitoring คือการทำรายงาน | คือการวัด + วิเคราะห์ + ตัดสินใจ + verify |
| Change Control ทำให้ช้าเสมอ | ลด rework และทำให้ trade-off โปร่งใส |
| PM อนุมัติทุก change | Authority ตาม Governance (minor = PM, baseline = CCB/Sponsor) |
| CPI/SPI ตอบทุกอย่าง | ต้องดู cause, forecast, quality, risk |
| ใช้เงินน้อย = ดี | ต้องเทียบกับ EV และ schedule |
| Escalation = แพ้ | Escalate ที่ถูกเวลา = ใช้ governance ให้เกิดประโยชน์ |

## 8. Interview Questions

### Foundational
- **Q:** Issue ต่างจาก Change Request อย่างไร?
- **Answer Direction:** Issue = ปัญหาที่เกิดแล้ว (ต้องแก้/escalate); Change Request = คำขอปรับ baseline อย่างเป็นทางการ (ต้อง impact analysis + approval)
- **Warning Signs:** ใช้สลับกัน หรือเรียกทุกอย่างว่า change

### Scenario
- **Q:** CPI = 0.90 และ Sprint 7–8 ล่าช้าบน critical path — คุณจะรายงานและตัดสินใจอย่างไร?
- **Answer Direction:** แยก variance ออกจาก cause; คำนวณ EAC/VAC; ดู critical path/float; เสนอ recovery options พร้อม trade-off; ระบุ authority ถ้าต้อง rebaseline; สื่อสารเป็น decision brief (ไม่ใช่แค่ตัวเลข)
- **Warning Signs:** ตอบ "เร่งทีม" หรือรายงานแค่ "CPI ต่ำ"

### Senior PM
- **Q:** Sponsor อนุมัติ change ด้วยวาจาในที่ประชุม แล้วบอกว่า "จดไว้ก็แล้วกัน" — คุณจะทำอย่างไร?
- **Answer Direction:** ยืนยันผ่านระบบ: บันทึกเป็น change request + impact pack, ขอ decision record/email confirm ก่อน update baseline — อธิบายว่า baseline ที่ไม่มี evidence ใช้ defend ไม่ได้ตอนปิดโครงการ
- **Warning Signs:** เงียบแล้วทำตาม หรือทะเลาะโดยไม่มีทางเลือกที่สะดวกทั้งสองฝ่าย

### Executive
- **Q:** ทำไม change ต้องผ่าน CCB ทั้งที่ Sponsor เห็นด้วยแล้ว?
- **Answer Direction:** CCB ทำให้เห็นผลกระทบครบทุกด้าน (scope/schedule/cost/quality/risk/contract) ก่อนตัดสินใจ และสร้าง audit trail — ลดความเสี่ยงที่ decision รีบร้อนจะพังทีหลัง; decision ใหญ่ยังจบที่ Sponsor/CCB เหมือนเดิม แค่มีข้อมูลครบ
- **Warning Signs:** ตอบว่า "เป็นขั้นตอนราชการ"

## 9. PM Dictionary ประจำบท

| Term (EN) | คำอธิบาย (TH) | ความหมายเชิงปฏิบัติ | การใช้ผิดที่พบบ่อย | Term ที่เกี่ยวข้อง |
|---|---|---|---|---|
| Monitoring | การติดตาม | วัดจริงเทียบ baseline ต่อเนื่อง | คิดว่า = รายงานตามรอบ | Controlling |
| Controlling | การควบคุม | วิเคราะห์ variance + แก้ + verify | สับสนกับ Monitoring | Monitoring |
| Variance | ส่วนเบี่ยงเบน | SV/CV — ต่างจากแผนเท่าไร | ดูแค่ตัวเลขไม่ดู cause | Forecast |
| Forecast | การคาดการณ์ | EAC/VAC — จบงานจะจบแบบไหน | คิดว่าเท่ากับ BAC เสมอ | EAC, VAC |
| Change Request | คำขอเปลี่ยนแปลง | ขอปรับ baseline อย่างเป็นทางการ | สับสนกับ Issue | Issue, Impact Analysis |
| Impact Analysis | วิเคราะห์ผลกระทบ | ดูครบ scope/schedule/cost/quality/risk/contract | ทำผิวเผินเป็น opinion | CCB |
| CCB | Change Control Board | อนุมัติ change ที่กระทบ baseline | คิดว่า PM อนุมัติเองได้ทุกเรื่อง | Governance |
| Baseline Update | ปรับฐานควบคุม | update หลังอนุมัติ change | สับสนกับ Status Update | Change Request |
| Issue | ปัญหาที่เกิดแล้ว | ต้องมี owner, action, escalation | สับสนกับ Risk/Change | Risk, Change Request |
| Escalation | การยกระดับ | ส่งเรื่องให้ authority ตัดสินใจ | ไม่ escalate / escalate ทุกอย่าง | Governance |
| Decision Brief | บันทึกขอตัดสินใจ | decision ask + evidence + deadline | สับสนกับ Status Report | Status Report |
| Validate Scope | ตรวจรับขอบเขต | ยืนยัน deliverable กับผู้มี authority (Ch.8) | สับสนกับ Control Scope | Control Scope |
| Control Scope | ควบคุมขอบเขต | จัดการ change ต่อ scope baseline | สับสนกับ Validate Scope | Change Request |

## 10. Workshop

### Scenario
**[Teaching Scenario]** เดือนที่ 5 ของ SHG: CPI/SPI = 0.90, Sprint 7–8 ล่าช้า 1 สัปดาห์ (critical path), คุณภัทรขอ flash sale ก่อน launch, PMS vendor ขอ T&M เพิ่ม 300K — คุณต้องจัดทำ decision pack สำหรับ CCB รอบถัดไป

### Your Role
PM (คุณสุทธิ) ที่ต้องสร้าง integrated impact pack + recommendation

### Available Information
- Baselines (12M, Sprint 0–12), EVM ตัวเลข, Risk Register (R-01 PMS), Scenario Master (feature ใหม่ = Phase 2+)

### Missing Information
- รายละเอียด flash sale (scope/ระยะเวลา/impact ต่อ payment load), เหตุผล vendor ขอเพิ่ม (work เกิน SOW จริงหรือ?), ความเห็น QA ต่อ fast-track Back Office, การอนุมัติ contingency ของ Sponsor

### Decision Required
- flash sale: approve/defer/reject? PMS adapter: approve ใช้ contingency / เจรจา / ปฏิเสธ? recovery สำหรับ critical path delay: option ใด?

### Constraints
- Launch ก่อน 1 พ.ย., งบ 12M + reserve ต้องใช้ตาม governance, feature ใหม่ตาม Scenario Master ต้องไป Phase 2+, ทุก decision ต้องมี decision record + baseline update

### Expected Output
- Impact Pack (impact analysis ครบทุกด้าน ต่อ 2 change), CCB recommendation (options + trade-off + authority), recovery brief สำหรับ schedule delay, updated RAID

### Debrief Questions
1. ทำไม impact analysis ต้องดู "benefits" ด้วย ไม่ใช่แค่ scope/cost
2. การใช้ Contingency Reserve ต่างจาก Management Reserve อย่างไร
3. ถ้า CCB อนุมัติต่างจากคำแนะนำ คุณจะทำอะไร

### Evaluation Criteria
- Impact ครบทุกด้าน, options + trade-off ชัด, authority/evidence ถูกต้อง, ไม่ขัด Scenario Master, baseline update ระบุครบ

## 11. Checklist ใช้งานจริง (Monitoring & Change / Phase E)

- [ ] Actuals ถูกเก็บตาม cadence (daily/weekly) พร้อม evidence
- [ ] Variance + forecast คำนวณ (SV/CV/SPI/CPI/EAC/VAC เมื่อเหมาะสม)
- [ ] Critical path health ถูกติดตามทุกสัปดาห์
- [ ] Status report ตอบ 8 คำถาม (อยู่ไหน/เทียบแผน/เปลี่ยนอะไร/ทำไม/กระทบ/decision/ใคร/เมื่อไร)
- [ ] Change intake: ทุกคำขอถูกล็อก (Change Log)
- [ ] Impact analysis ครบทุกด้าน (scope/schedule/cost/quality/resource/risk/contract/operation/benefits)
- [ ] Decision ผ่าน authority ที่ถูกต้อง (PM minor / CCB baseline / Sponsor reserve)
- [ ] Baseline ถูก update หลังอนุมัติ + สื่อสารทุกฝ่าย
- [ ] RAID review ต่อเนื่อง — risk trigger ถูก monitor
- [ ] Escalation ใช้เมื่อเข้าเงื่อนไข (E.10)
- [ ] Decision record + communication ครบ
- [ ] ส่งต่อ Ch.8: deliverables + evidence พร้อมตรวจรับ

## 12. Assessment

1. **[EVM Case]** เดือนที่ 5: PV = 7.5M, EV = 6.75M, AC = 7.5M — คำนวณ SPI/CPI/EAC/VAC และอธิบายว่า reserve ตัวไหนใช้ได้ ใครอนุมัติ
2. **[Decision Case]** flash sale ก่อน launch — ทำ impact analysis (ครบทุกด้าน) + แนะนำ approve/defer/reject พร้อม authority
3. **[Decision Case]** PMS vendor ขอ T&M เพิ่ม 300K เกิน cap — เสนอทางเลือก (ใช้ contingency/เจรจา/ปฏิเสธ) พร้อม evidence และ decision path
4. **[Artifact Review]** ตรวจ Change Log ที่มี "เพิ่มฟีเจอร์" โดยไม่มี impact analysis/baseline update/approval — ระบุสิ่งที่ขาดและผลที่จะเกิด
5. **[Scenario Case]** Sponsor อนุมัติ change ด้วยวาจา — อธิบายขั้นตอนที่คุณจะทำให้เป็นทางการ
6. **[Cross-Knowledge Analysis]** ถ้า fast-track Back Office ทำให้ defect เพิ่ม — กระทบ Ch.8 (UAT) และ Ch.9 (Go-live) อย่างไร และคุณจะ monitor อะไร
7. **[Recall]** เงื่อนไขที่ควร escalate (จาก E.10) มีอะไรบ้าง

## 13. Executive Summary

| มิติ | สรุป |
|---|---|
| **Why** | Monitoring + Change Control คือระบบที่ทำให้การบริหารต่างจากการตามงาน |
| **Decision Improved** | ทุก change ผ่าน impact analysis + authority + evidence |
| **Failure Prevented** | ป้องกัน baseline เลื่อนเงียบ ๆ, change ด้วยวาจา, และรายงานที่หลอก |
| **What to Monitor** | SPI/CPI trend, critical path, reserve usage, change queue, escalation ageing |

## 14. เชื่อมไปบทถัดไป + Artifact Handoff

**Bridge:** งานหลักเสร็จ + ถูกควบคุมแล้ว — Ch.8 (Verification/UAT) จะพิสูจน์ว่า solution ตรง requirement และพร้อมขึ้น Production (Quality ฝั่ง QC — cross-ref กับ Test Strategy ที่วางใน Ch.5)

| Field | Handoff |
|---|---|
| Input | Work Performance Data (Ch.6), Baselines (Ch.4/Ch.5), Change Log |
| Output | Status Reports, Variance/Forecast, Approved Change Log + Updated Baselines, Updated RAID |
| Creator | PM + Impact Owners |
| Artifact owner | PM |
| Reviewer | CCB/Sponsor (decision), Stakeholders (report) |
| Approval authority | PM (minor) / CCB-Sponsor (baseline) / Commercial-Legal (contract) |
| Minimum acceptance | Usable (decision record + baseline update ครบ) |
| Next chapter use | Ch.8 ใช้ deliverables + evidence + acceptance criteria เพื่อ Verification/UAT/Release Readiness |

## 15. Quick Reference Card

```text
MONITORING & CHANGE (E)
------------------------------------------------------------
Cycle: Collect -> Compare baseline -> Variance/Forecast -> Cause
       -> Options -> Decide -> Implement -> Verify
EVM:   SV/SPI/CV/CPI -> EAC = BAC/CPI -> VAC = BAC - EAC
Change: Intake -> Log -> Impact (ทุกด้าน) -> Options -> CCB/Authority
        -> Baseline Update -> Communicate -> Implement -> Verify
RAID:  Review ต่อเนื่อง + Escalate เมื่อเข้าเงื่อนไข (E.10)

กฎ 3 ข้อห้าม:
- ห้าม change ผ่านวาจา
- ห้ามแยก Issue กับ Change Request ปนกัน
- ห้ามรายงาน % โดยไม่มี EV/evidence

Integration note: Charter = Ch.2 | Change Control = บทนี้ | Closure = Ch.10
```

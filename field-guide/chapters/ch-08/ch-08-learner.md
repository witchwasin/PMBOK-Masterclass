---
chapter: ch-08
title: "Verification, UAT และ Release Readiness (Playbook F)"
book: "PM Delivery Guide: From Pre-sales to Closure — คู่มือปฏิบัติการบริหารโครงการซอฟต์แวร์ (PMBOK 8th Edition)"
edition: Learner
status: Released
validation_status: Reviewed
last_reviewed: 2026-08-15
intended_learner_level: Experienced PM
difficulty: Core
estimated_study_time: 100
prerequisite:
  - "Ch.5 — Test Strategy/Quality Plan (วางแผน)"
  - "Ch.7 — Monitoring & Change"
related_chapters:
  - "Ch.5 — วางแผน Test/Quality (cross-reference)"
  - "Ch.9 — Go-Live & Hypercare (ต่อจาก Go/No-Go)"
canonical_source:
  - ../../references/PMBOK-Overview.md (PMBOK framework)
  - ../../e-Book/chapters/lesson-10/lesson-10-learner.md (Quality — ฝั่ง Control Quality/Validate)
scenario_version:
  hotel_booking: "1.0"
artifact_outputs:
  - name: Test Results + Defect Log
    creator: QA + Testers
    artifact_owner: QA Lead
    reviewer: Tech Lead, PM
    approval_authority: QA Lead (test readiness) / PO (business acceptance)
    approval_evidence: Test evidence, defect triage record
  - name: UAT Evidence + UAT Sign-off
    creator: Business Users + BA
    artifact_owner: Acceptance Authority (PO/คุณภัทร)
    reviewer: PM, QA Lead
    approval_authority: PO / VP Marketing (ตาม Governance)
    approval_evidence: Signed UAT sign-off + acceptance evidence
  - name: Release Readiness Report + Go/No-Go Decision
    creator: PM + Release Manager
    artifact_owner: PM
    reviewer: Sponsor, Security, Ops
    approval_authority: Sponsor / Business Owner (Go/No-Go)
    approval_evidence: Readiness checklist + Go/No-Go record
---

# Chapter 08 — Verification, UAT และ Release Readiness: พิสูจน์ว่า "พร้อมขึ้น Production"

## 1. Opening Scenario Hook

**[Teaching Scenario]** Sprint 11 ของ SHG เริ่มแล้ว UAT dashboard เป็นสีเขียว แต่เมื่อคุณสุทธิ (PM) ถามลึกลงไป กลับพบว่า: ไม่มี requirement coverage, ไม่มี defect severity, ไม่มี retest result, key users จาก 3 โรงแรมยังไม่ได้ทดสอบ payment scenario จริง และ UAT sign-off ยังไม่เซ็น

**[PMBOK 8]** สีเขียวบน dashboard ไม่ใช่หลักฐาน — หลักฐานคือ connection ระหว่าง requirement → test case → test result → acceptance (RTM) ที่มี evidence ครบ — บทนี้คือจุดที่ **Test Strategy จาก Ch.5** กลายเป็น **ผลการทดสอบจริง** และเป็นจุดตัดสินใจ Go/No-Go ก่อนส่งต่อ Ch.9

## 2. Why It Matters

**[PMBOK 6]** Verification (สร้างถูกตาม spec) + Validation (สร้างสิ่งที่ตอบ need) + Release Readiness คือการพิสูจน์ว่า solution ทำงานตาม requirement, มีคุณภาพ, ปลอดภัย, ลูกค้ายอมรับ และ operations พร้อมรับช่วง — ถ้าข้ามหรือทำเป็นพิธี ต้นทุนจะย้ายไป Ch.9 (Go-live ผิดพลาด) และ Ch.10 (closure dispute)

**[Best Practice]** UAT ไม่ควรใช้แทน System Test — QA/SIT พิสูจน์ technical/functional correctness ส่วน UAT พิสูจน์ว่า business user ยอมรับว่า solution รองรับ business process จริง

## 3. Mental Model

```text
Test Strategy (Ch.5) + Deliverables (Ch.6) + Baselines
  -> Test Planning (env, data, entry/exit)
  -> SIT / System Test (technical correctness)
  -> UAT Prepare (pack: scope, participants, scenarios)
  -> UAT Execute (business users + evidence)
  -> Defect Triage (severity ≠ priority; fix/defer/waive)
  -> RTM check (requirement -> test -> result -> acceptance)
  -> Release Readiness Review (F.7 checklist)
  -> Go / No-Go Decision (Sponsor/Business Owner)
  -> Ch.9 (Go-Live & Hypercare)
```

> **Cross-reference (Quality):** แผน Test/Test Strategy = Ch.5 | QA ฝั่งกระบวนการ = Ch.6 | **ผลการทดสอบจริง/QC/UAT = บทนี้**

## 4. Main Lesson

### 4.1 Test Levels (F.2)

**[Best Practice]** แต่ละ level มี purpose + owner + exit criteria ที่ต่างกัน — หลักสำคัญ: **ทดสอบเร็วพบเร็ว ราคาถูก; ทดสอบช้าพบช้า ราคาแพง** (bug ที่ QA พบใน 1 ชั่วโมง ต่างจากที่ลูกค้าเจอหลัง go-live หลายเท่า):

| ระดับ | ทดสอบอะไร | ใครทำ | พบ defect แบบไหน |
|---|---|---|---|
| Unit / Component | ฟังก์ชันย่อย (เช่น คำนวณราคาห้อง) | Developer | logic ผิดในฟังก์ชันเดียว |
| Integration / SIT | การเชื่อมต่อระหว่างระบบ (ระบบ ↔ PMS, ↔ payment gateway) | QA / DevOps | interface mismatch, data format, timing |
| System Test | ทั้งระบบตาม spec ครบ | QA | ฟีเจอร์ไม่ตรง spec, workflow ผิด |
| Performance / Security | โหลด, response time, PCI-DSS | QA + Security | ช้าภายใต้โหลด, ช่องโหว่ |
| Regression | ฟีเจอร์เดิมยังทำงานหลังแก้ | QA (automation) | fix ใหม่พังของเดิม |
| UAT | Business process ตาม acceptance criteria | Business Users | งานไม่รองรับกระบวนการจริงของ user |
| Production Verification | ระบบทำงานจริงหลัง deploy | PM / Support | หลัง up: monitor + smoke |

### 4.2 QA vs UAT (F.3)

**[PMBOK 6]** QA/SIT พิสูจน์ technical correctness; UAT พิสูจน์ business acceptance — UAT ไม่ใช้แทน system test; ถ้า SIT ยังไม่ผ่าน UAT จะกลายเป็นการทดสอบซ้ำที่แพงและไร้ความหมาย

**[Best Practice]** จับคู่กับ Verification/Validation ที่บทนี้เปิดเรื่อง: **QA = Verification (สร้างถูกตาม spec — "Ver" ใน Ch.5), UAT = Validation (สร้างสิ่งที่ตอบ need — "Val")** — จำง่าย ๆ: QA ตอบคำถาม "ตรง spec ไหม" ส่วน UAT ตอบคำถาม "คนใช้ทำงานได้จริงไหม" — ต่างกันที่คำถาม ไม่ใช่แค่ "ใครเป็นคนกด"

### 4.3 UAT Planning (F.4)

**[Best Practice]** ต้องมี: UAT Scope, Participants, Environment, Data, Scenarios, Expected Result, Entry Criteria, Exit Criteria, Defect Handling, Sign-off Authority, Schedule, Evidence

**[Teaching Scenario]** SHG UAT: scope = booking flow + payment + back office + PMS sync, participants = key users 80 คน (จาก 12 โรงแรม), environment = UAT env กับ test data (ต้องไม่ใช้ production data), scenarios = ตาม acceptance criteria จาก Ch.3, sign-off = คุณนภา (PO) + คุณภัทร (VP Marketing) ตาม Governance

### 4.4 Requirements Traceability (F.5)

**[Best Practice]** RTM เชื่อม: Business Need → Requirement → Design → Build → Test Case → Test Result → Acceptance — ถ้า RTM ไม่ครบ แปลว่ามี requirement ที่ไม่ถูกทดสอบ (coverage gap)

**[Teaching Scenario]** ตัวอย่างแถว RTM ของ SHG: **REQ-042** (ลูกค้าจองห้องแล้วได้รับ confirmation อีเมล) → Design (booking service + email queue) → Build (ฟีเจอร์ใน Sprint 6) → Test Case TC-118 (จอง + ตรวจอีเมล) → Result (ผ่าน + evidence) → Acceptance (UAT wave 1 เซ็น) — ถ้าแถวไหนช่อง Test Result ว่าง แปลว่า requirement นั้นยังไม่ถูกพิสูจน์ — นั่นคือ coverage gap ที่ต้องปิดก่อน Go/No-Go

### 4.5 Defect Management (F.6)

**[Best Practice]** Defect ต้องมี: ID, Description, Environment, Steps, Expected, Actual, Severity, Priority, Owner, Fix Version, Retest, Status

**[PMBOK 6]** **Severity ≠ Priority:** Tester/QA กำหนด Severity (ผลกระทบ: Critical/Major/Minor/Low); PO กำหนด Priority (ความเร่งด่วน: Immediate/High/Medium/Low) — defect 20 รายการที่เป็น cosmetic อาจน่ากังวลน้อยกว่า defect เดียวที่ทำให้ payment fail

**[Best Practice]** ทำไมต้อง**แยกคนตั้ง** Severity และ Priority: เพราะเป็นคำถามคนละอย่าง — Severity = "ร้ายแรงแค่ไหน" (QA ตอบจากผลกระทบทางเทคนิค: ข้อมูลเสียหายไหม, payment พังไหม) ส่วน Priority = "ต้องแก้เมื่อไร" (PO ตอบจากผลต่อ business: campaign เปิดพรุ่งนี้ไหม) — defect ที่ critical แต่อยู่ในฟีเจอร์ที่ยังไม่ launch อาจ priority กลาง; defect ที่เล็กน้อยแต่ขวาง key user ทำงานอาจ priority สูง — ถ้าให้คนเดียวตั้งทั้งคู่ มักจบด้วยการโหวต "รู้สึก" แทนการตัดสินจากหลักฐาน

### 4.6 Release Readiness (F.7) + Go/No-Go (F.8)

**[Best Practice]** ตรวจ: Scope Complete, Tests Pass, Critical Defects Closed, Security Accepted, Performance Accepted, Data Migration Tested, Monitoring Ready, Backup Ready, Rollback Ready, Training Complete, Support Ready, Communication Ready, Approval Ready

**Go/No-Go inputs:** Business Readiness, Technical Readiness, Operational Readiness, Security, Data, Defects, Rollback, Support, Risk, Stakeholder Approval

**[Best Practice]** Go/No-Go ไม่ใช่การเชียร์ให้ผ่าน — ถ้า defect critical ค้าง หรือ rollback ยังไม่ทดสอบ คำตอบที่ถูกอาจเป็น No-Go หรือ Go แบบมีเงื่อนไข (conditional) — Sponsor/Business Owner เป็น authority

## 5. PM Decision Thinking

```text
Decision: UAT พบ payment defect 8% failure rate + key users 3 โรงแรมยังไม่ทดสอบ — Go, No-Go หรือ Conditional?
Owner: PM + QA Lead วิเคราะห์; PO/คุณภัทร (business acceptance); Sponsor (go-live authority)
Inputs: RTM coverage, test results, severity, retest, regression, data readiness, rollback, support, Scenario Master
Options:
  A: Go — ทุก exit criteria ผ่าน
  B: Conditional Go — เปิดใช้งานบางส่วน (pilot 3 โรงแรม) + ปิด defect ตาม due date (ตรงกับ Sprint 12 soft launch)
  C: No-Go — defect critical ค้าง / rollback ยังไม่พร้อม -> เลื่อน launch (กระทบ high season)
Trade-offs: launch timing vs failure cost, momentum vs trust, pilot vs full launch
Risk: Go ทั้งที่ payment ไม่เสถียร -> campaign กลาง launch ล่ม -> revenue + trust เสียหาย
Evidence: release readiness report, defect triage, retest results, rollback test, support plan, signed acceptance
Next Action: ตัดสินใจ -> ดำเนินการ (launch/cutover = Ch.9) หรือปิด gap -> review ใหม่
```

## 6. ตัวอย่างจริงจาก Case ต่อเนื่อง (SHG)

**[Teaching Scenario] Watch PM Think — สัปดาห์ Go/No-Go**

คุณสุทธิ (PM) เปิด UAT dashboard — สีเขียว แต่เขารู้จากบทเรียนว่า **สีเขียวไม่ใช่หลักฐาน** เขาไล่ถาม QA lead 3 คำถาม: "RTM ครอบคลุมครบไหม?", "defect ที่ค้างมี severity อะไร?", "retest หลัง fix มี evidence ไหม?" — คำตอบแรกคือ coverage 85% และ 3 โรงแรมยังไม่ได้ทดสอบ cancellation scenario

Payment defect 8% failure ใน UAT — เขาไม่สรุปทันที: triage แยก **severity (payment = Critical)** ออกจาก **priority (PO ตั้ง Immediate เพราะ campaign ใกล้)** — "defect 20 ตัวที่เป็น cosmetic อาจน่ากังวลน้อยกว่า defect เดียวที่ทำให้ payment ล่ม"

SIT ผ่าน (booking + PMS sync) แต่ payment sandbox พบ 2 defect (callback timeout, duplicate confirmation) — เขาตัดสินใจ: fix critical ก่อน, defer cosmetic, แล้ว **regression retest หลัง fix** — "fix โดยไม่ retest = แก้ปัญหาเดิมแต่สร้างปัญหาใหม่"

Release readiness: security (PCI-DSS) ผ่าน, performance ผ่าน (3s/5s/99.5%), **rollback plan ทดสอบแล้ว** (บทเรียนจาก Ch.9: rollback ที่ไม่ทดสอบ = ไม่มี rollback), support team พร้อม

ข้อเสนอของเขา: **Conditional Go — Soft Launch 3 โรงแรม** (ตรง Sprint 12 ของ Scenario Master) + ปิด defect critical ภายใน 1 สัปดาห์ + monitor payment failure rate < threshold — Sponsor (คุณจิรา) อนุมัติ — "ไม่ใช่ 'ผ่านไปก่อน' แต่เป็นเงื่อนไขที่ชัดเจน มี owner และ due date"

**[PMBOK 8]** สังเกตว่า decision มี evidence และเป็น conditional ที่มีเงื่อนไขชัด ไม่ใช่ "ผ่านไปก่อน"

## 7. จุดตัดสินใจและกับดักที่พบบ่อย

**Common Mistakes:**

1. ใช้ UAT แทน System Test — ผล: ทดสอบซ้ำแพง หรือ business เจอ bug ที่ QA ควรเจอ
2. นับ defect ทั้งหมดเป็น "เยอะ" โดยไม่ดู severity — ผล: ตัดสินใจผิด (cosmetic 20 ตัว vs critical 1 ตัว)
3. UAT sign-off เป็นพิธี — ผล: ผู้ใช้ไม่ได้ทดสอบจริง แต่เซ็นเพราะเกรงใจ
4. ไม่มี RTM — ผล: ไม่รู้ว่า requirement ไหนยังไม่ถูกทดสอบ
5. Go/No-Go ตัดสินจากแรงกดดัน campaign — ผล: ขึ้น production ทั้งที่ rollback ยังไม่พร้อม
6. Test data ไม่ตรงของจริง — ผล: ผล test ไม่สะท้อน production
7. ไม่มี release readiness checklist — ผล: ลืม training/support/communication ตอนท้าย

**Common Misconceptions:**

| ความเข้าใจผิด | ความจริง |
|---|---|
| จำนวน defect น้อย = พร้อม | ต้องดู severity, coverage, retest, data readiness |
| สีเขียวบน dashboard = ผ่าน | ต้องมี evidence เชื่อม requirement → test → acceptance |
| UAT = การทดสอบรอบสุดท้ายทั่วไป | UAT = business acceptance โดยเฉพาะ ไม่แทน system test |
| Severity = Priority | Tester ตั้ง severity; PO ตั้ง priority |
| Go/No-Go ตัดสินโดย PM | Authority = Sponsor/Business Owner |
| Sign-off = จบ | ต้องมี acceptance evidence + residual risk decision |

## 8. Interview Questions

### Foundational
- **Q:** Verification ต่างจาก Validation อย่างไร?
- **Answer Direction:** Verification = สร้างถูกตาม spec (build the product right); Validation = สร้างสิ่งที่ตอบ need (build the right product) — SHG: verify ว่า booking flow ทำงานตาม SRS; validate ว่าผู้ใช้จองสำเร็จและ conversion ดี
- **Warning Signs:** สลับกันหรือตอบว่าเหมือนกัน

### Scenario
- **Q:** UAT พบ payment failure 8% ก่อน launch campaign — คุณจะทำอย่างไร?
- **Answer Direction:** ไม่สรุปทันที — triage severity (critical?), หาสาเหตุ, fix + regression retest, ประเมิน rollback/support readiness, นำเสนอ Go/No-Go แบบมี evidence ต่อ Sponsor (อาจ conditional: pilot ก่อน)
- **Warning Signs:** ตอบ "เลื่อน launch" ทันที หรือ "go เลย campaign รอไม่ได้" โดยไม่มี evidence

### Senior PM
- **Q:** PO อยากเซ็น UAT sign-off ทั้งที่ key users ยังทดสอบไม่ครบทุก scenario — คุณจะจัดการอย่างไร?
- **Answer Direction:** อธิบายความเสี่ยงของการ accept โดยไม่ครบ coverage; เสนอทางเลือก: ขยาย UAT wave, ลด scope ของ sign-off (waiver ระบุ scenario ที่เลื่อน), หรือ conditional sign-off พร้อม due date — บันทึก residual risk อย่างเป็นทางการ
- **Warning Signs:** ปล่อยให้เซ็นเพื่อความสะดวก หรือยึดตายตัวโดยไม่มีทางเลือก

### Executive
- **Q:** ทำไมต้องมี Release Readiness Report ก่อน Go/No-Go?
- **Answer Direction:** รายงานรวม evidence จากทุกมุม (scope, test, security, performance, data, rollback, training, support, approval) ให้ decision maker เห็นภาพเดียว — ลดความเสี่ยงที่ Sponsor ตัดสินใจจากข้อมูลไม่ครบ และสร้าง audit trail สำหรับ go-live
- **Warning Signs:** ตอบว่า "เป็นกระบวนการ QA"

## 9. PM Dictionary ประจำบท

| Term (EN) | คำอธิบาย (TH) | ความหมายเชิงปฏิบัติ | การใช้ผิดที่พบบ่อย | Term ที่เกี่ยวข้อง |
|---|---|---|---|---|
| Verification | ตรวจตาม spec | build the product right | สับสนกับ Validation | Validation |
| Validation | ตรวจว่าตอบ need | build the right product | สับสนกับ Verification | Verification |
| SIT | System Integration Test | ทดสอบรวมระบบ/การเชื่อมต่อ | ใช้แทน UAT | UAT |
| UAT | User Acceptance Test | ผู้ใช้ธุรกิจตรวจรับ business process | ใช้แทน system test | SIT, Acceptance |
| RTM | Requirements Traceability Matrix | requirement → test → result → acceptance | ทำเพื่อให้ครบ template | Coverage |
| Defect Severity | ความรุนแรง | ผลกระทบต่อ value/user/risk | สับสนกับ Priority | Defect Priority |
| Defect Priority | ความเร่งด่วน | ต้องแก้เมื่อไร (PO ตั้ง) | สับสนกับ Severity | Defect Severity |
| Release Readiness | ความพร้อมขึ้น Production | scope/test/security/data/rollback/support/approval | เช็คเฉพาะ test ผ่าน | Go/No-Go |
| Go/No-Go | การตัดสินใจขึ้น Production | ตัดสินจาก readiness + risk + rollback + support | ตัดสินจากแรงกดดัน | Release Readiness |
| Residual Risk | ความเสี่ยงคงเหลือ | risk หลัง mitigation — ต้องมี owner | ลืมว่ายังเหลืออยู่ | Risk |
| Acceptance Evidence | หลักฐานตรวจรับ | พิสูจน์ว่า deliverable ผ่าน criteria | คิดว่า sign-off พอ | UAT Sign-off |
| Test Strategy | แนวทางการทดสอบ | วางแผนไว้ Ch.5; ผลจริง = บทนี้ | คิดว่าเท่ากับ Test Plan | Test Plan |

## 10. Workshop

### Scenario
**[Teaching Scenario]** ก่อน Planning Go/No-Go ของ SHG: UAT พบ payment defect (8% failure), 3 โรงแรมยังไม่ได้ทดสอบ cancellation scenario, RTM แสดง coverage 85%, rollback plan ยังไม่เคยทดสอบจริง, support team ยังไม่ได้ฝึก hypercare runbook

### Your Role
PM (คุณสุทธิ) ที่ต้องเสนอ Go/No-Go recommendation พร้อม evidence

### Available Information
- Test results, defect log (severity/priority), RTM, release readiness checklist (F.7), Scenario Master (Sprint 12 = soft launch 3 โรงแรม)

### Missing Information
- สาเหตุ payment defect (gateway? flow? data?), ผล retest หลัง fix, ความพร้อม rollback test, training status ของ support team, ความเห็น Sponsor ต่อ conditional approach

### Decision Required
- Go / No-Go / Conditional Go? ถ้า conditional: เงื่อนไขอะไร owner ใคร due date เท่าไร?

### Constraints
- Launch ก่อน High Season (1 พ.ย.), ต้องไม่ขึ้น production โดยไม่มี rollback, Go/No-Go authority = Sponsor

### Expected Output
- Release Readiness Report (ตาม F.7 checklist), Go/No-Go recommendation + options + trade-off, gap log (owner + due date), residual risk statement

### Debrief Questions
1. ทำไม "defect น้อย" ยังไม่พอต่อการตัดสินใจ Go
2. Conditional Go ต่างจาก Go เต็มอย่างไร และเมื่อไรถึงสมเหตุสมผล
3. ถ้า Sponsor เร่งให้ Go ทั้งที่ rollback ยังไม่พร้อม คุณจะ defend อย่างไร

### Evaluation Criteria
- Decision มี evidence (RTM, severity, retest, rollback, support), conditional มีเงื่อนไข + owner + due date, authority ถูกต้อง, ไม่ขัด Scenario Master

## 11. Checklist ใช้งานจริง (Verification/UAT / Phase F)

- [ ] Test Plan ตาม Test Strategy (Ch.5): scope, env, data, entry/exit
- [ ] SIT/System Test เสร็จก่อน UAT (ไม่ใช้ UAT แทน)
- [ ] UAT pack พร้อม: participants, scenarios, expected results, sign-off authority
- [ ] RTM ครอบคลุม 100% (requirement → test → result → acceptance)
- [ ] Defect log ครบ: severity (QA) + priority (PO) + owner + retest
- [ ] Retest + regression หลัง fix มี evidence
- [ ] Security/Performance accepted (PCI-DSS, 3s/5s/99.5%)
- [ ] Data migration tested; monitoring/backup/rollback ready
- [ ] Training + support พร้อม (Ch.9 hypercare)
- [ ] UAT sign-off เซ็นโดย acceptance authority (PO/คุณภัทร) พร้อม evidence
- [ ] Release Readiness Report (F.7) สมบูรณ์
- [ ] Go/No-Go decision บันทึกโดย Sponsor + residual risk statement
- [ ] Cross-ref: แผน Test = Ch.5, QA = Ch.6, ผลจริง = บทนี้

## 12. Assessment

1. **[Decision Case]** payment defect 8% + 3 โรงแรมยังไม่ทดสอบ — เสนอ Go/No-Go/Conditional พร้อม evidence + trade-off + authority
2. **[Decision Case]** PO อยากเซ็น UAT ทั้งที่ coverage 85% — คุณจะทำอย่างไร (options + risk + residual decision)
3. **[Artifact Review]** ตรวจ UAT dashboard สีเขียวที่ไม่มี coverage/severity/retest/acceptance — ระบุสิ่งที่ขาดและผล
4. **[Scenario Case]** defect 20 รายการ cosmetic กับ 1 รายการ payment critical — อธิบาย severity vs priority และการตัดสินใจ
5. **[Trade-off Case]** Soft Launch 3 โรงแรม (conditional) vs Full Launch ทั้ง 12 โรงแรม — trade-off ต่อ campaign, support และ trust
6. **[Cross-Knowledge Analysis]** ถ้า RTM พบ coverage gap 15% — กระทบ UAT schedule (Ch.8) และ Go-live (Ch.9) อย่างไร และทางเลือกคืออะไร
7. **[Recall]** องค์ประกอบของ Release Readiness (F.7) มีอะไรบ้าง (ระบุ ≥ 7)

## 13. Executive Summary

| มิติ | สรุป |
|---|---|
| **Why** | Verification/UAT คือหลักฐานว่า "พร้อมขึ้น Production" — ไม่ใช่แค่สีเขียวบน dashboard |
| **Decision Improved** | Go/No-Go ตัดสินจาก evidence + risk + rollback + support |
| **Failure Prevented** | ป้องกัน UAT พิธี, defect แฝง, coverage gap และ go-live ที่ไม่มีหลักประกัน |
| **What to Monitor** | RTM coverage, defect severity ageing, retest rate, readiness checklist status |

## 14. เชื่อมไปบทถัดไป + Artifact Handoff

**Bridge:** Go/No-Go ผ่าน (conditional: soft launch) — Ch.9 (Go-Live & Hypercare) จะบริหาร Cutover, Rollback, Monitoring และ Stabilization ตามแผนที่วางใน Ch.5 (C17)

| Field | Handoff |
|---|---|
| Input | Deliverables + evidence (Ch.6), Test Strategy (Ch.5), Change Log (Ch.7) |
| Output | Test Results, UAT Sign-off, Release Readiness Report, Go/No-Go Decision |
| Creator | QA Lead (test), Business Users (UAT), PM + Release Mgr (readiness) |
| Artifact owner | QA Lead / Acceptance Authority / PM |
| Reviewer | Tech Lead, PO, Security, Ops |
| Approval authority | Sponsor / Business Owner (Go/No-Go) |
| Minimum acceptance | Usable (ต้องมี RTM + severity + readiness + sign-off) |
| Next chapter use | Ch.9 ใช้ Go decision + cutover/rollback plan + support readiness เพื่อ Go-Live & Hypercare |

## 15. Quick Reference Card

```text
VERIFICATION/UAT (F) — เป้าหมาย: พิสูจน์พร้อม Production
------------------------------------------------------------
Test levels: Unit -> SIT -> Performance -> Security -> Regression -> UAT
UAT: scope/participants/env/data/scenarios/entry-exit/sign-off authority
RTM: requirement -> design -> build -> test -> result -> acceptance
Defect: Severity (QA) ≠ Priority (PO); retest + regression มี evidence
Readiness (F.7): scope/test/security/perf/data/backup/rollback/training/support/approval
Go/No-Go: Sponsor ตัดสินจาก evidence + risk; conditional ต้องมีเงื่อนไข + owner + due date

กฎ 3 ข้อห้าม:
- ห้ามใช้ UAT แทน system test
- ห้าม Go โดยไม่มี rollback ที่ทดสอบแล้ว
- ห้าม sign-off แบบพิธี โดยไม่มี coverage/evidence

Cross-ref: แผน Test = Ch.5 | QA = Ch.6 | ผลจริง = บทนี้
```

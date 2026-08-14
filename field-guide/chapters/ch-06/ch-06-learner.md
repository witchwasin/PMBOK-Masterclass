---
chapter: ch-06
title: "Execution — ส่งมอบ Solution, บริหารทีม และ Manage Quality (Playbook D)"
book: "PM Delivery Guide: From Pre-sales to Closure — คู่มือปฏิบัติการบริหารโครงการซอฟต์แวร์ (PMBOK 8th Edition)"
edition: Learner
status: Draft
validation_status: Not Validated
last_reviewed: 2026-08-15
intended_learner_level: Experienced PM
difficulty: Core
estimated_study_time: 100
prerequisite:
  - "Ch.5 — Risk, Procurement, Communications, Environment และ Planning Gate"
related_chapters:
  - "Ch.7 — Monitoring & Change (ควบคู่กับ Execution)"
  - "Ch.8 — Verification/UAT (QC ผลจริง)"
canonical_source:
  - ../../references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md (Phase D)
  - ../../e-Book/chapters/lesson-10/lesson-10-learner.md (Quality — ฝั่ง Manage Quality)
  - ../../e-Book/chapters/lesson-11/lesson-11-learner.md (Resource — ฝั่ง Develop/Manage Team)
  - ../../e-Book/chapters/lesson-15/lesson-15-learner.md + lesson-16 (Agile inserts)
scenario_version:
  hotel_booking: "1.0"
artifact_outputs:
  - name: Work Performance Data + Deliverables
    creator: Delivery Team + Leads
    artifact_owner: Workstream Leads
    reviewer: PM, QA
    approval_authority: ตาม Governance (acceptance = Ch.8)
    approval_evidence: Test evidence, review records, DoD check
  - name: Quality/QA Evidence (Manage Quality)
    creator: QA Lead + Team
    artifact_owner: QA Lead
    reviewer: PM
    approval_authority: QA Lead (test readiness) / PO (business acceptance = Ch.8)
    approval_evidence: Design review, test readiness gate, process improvement log
  - name: Team Management Records
    creator: PM + Team Leads
    artifact_owner: PM
    reviewer: Functional Managers
    approval_authority: PM (ภายใน delegated authority)
    approval_evidence: Conflict resolution log, performance feedback, blocker log
---

# Chapter 06 — Execution: ลงมือสร้าง พร้อมรักษาคุณภาพและทีม

## 1. Opening Scenario Hook

**[Teaching Scenario]** Planning Gate ผ่านแล้ว ทีม SHG เริ่ม Sprint 1 — คุณสุทธิ (PM) เห็น board เต็มไปด้วยงาน แต่เมื่อคุณถาม QA ว่า "payment flow จะเริ่ม test เมื่อไร" QA ตอบว่า "เดี๋ยวค่อยดูตอนใกล้เสร็จ" และเมื่อคุณถาม Developer คนหนึ่งว่า "ทำไม story นี้ยังไม่ Done" เขาตอบว่า "code เขียนเสร็จแล้วไง"

**[PMBOK 8]** นี่คือสองกับดักของ Execution: (1) คุณภาพที่คิดว่า "มาทำตอนท้าย" แทนที่จะฝังไว้ในกระบวนการ (Manage Quality / QA) และ (2) นิยาม "เสร็จ" ที่ไม่ตรงกันระหว่างคนเขียน คนทดสอบ และคนรับงาน (Definition of Done) — Execution ไม่ใช่แค่ "เขียน code ให้เสร็จ" แต่คือการสร้าง deliverables พร้อม evidence ผ่านกระบวนการที่ป้องกัน defect

## 2. Why It Matters

**[PMBOK 6]** Executing คือที่ที่แผนกลายเป็นของจริง — Direct and Manage Project Work, Manage Quality, Develop/Manage Team, Manage Communications, Implement Risk Responses, Conduct Procurements, Manage Stakeholder Engagement

**[Best Practice]** ถ้า Execution ไม่มีวินัย (ไม่มี DoR/DoD, QA มาทีหลัง, blocker ไม่ถูก escalate) ปัญหาจะสะสมไประเบิดที่ Ch.8 (UAT) และ Ch.9 (Go-live) — ต้นทุนการแก้ตอนนั้นแพงกว่าการป้องกันตอนนี้หลายเท่า

## 3. Mental Model

```text
Integrated Plan (Ch.5) + Baselines (Ch.4)
  -> Confirm Ready Work (DoR) — งานพร้อมเริ่มหรือยัง
  -> Build/Configure/Integrate
  -> Peer Review -> Test (ระหว่างทาง)
  -> Definition of Done — ครบทุกเกณฑ์ ไม่ใช่ "code เสร็จ"
  -> Work Performance Data -> Ch.7 (Monitoring)
  -> Deliverable -> Ch.8 (Verification/UAT)
ควบคู่กัน:
  Manage Quality (QA) — กระบวนการป้องกัน defect
  Develop/Manage Team — Tuckman, conflict, motivation
  Manage Comms/Risk/Stakeholder — ตามแผน Ch.5
```

> **Cross-reference (Quality):** แผนคุณภาพ/Test Strategy = Ch.5, **Manage Quality (QA ฝั่งกระบวนการ) = บทนี้**, **ผลการทดสอบจริง/QC = Ch.8**

## 4. Main Lesson

### 4.1 Execution Flow (D.4)

**[Best Practice]**
- **Predictive:** Analyze → Design → Build → Test → UAT → Deploy
- **Agile:** Refine → Plan Sprint → Build/Test → Review → Retro → Release
- **Hybrid:** Fixed Milestones + Iterative Development + Formal Gates (ตรงกับ SHG)

**[Best Practice]** ทั้ง 3 แบบต่างกันที่ **จังหวะตรวจ/ปรับ (feedback cadence)** ไม่ใช่แค่ชื่อขั้นตอน: Predictive ตรวจ/ปรับน้อยครั้ง — plan ครั้งเดียว แล้วไป test/UAT ปลายทาง (ผิดพลาดพบช้า แก้แพง); Agile ตรวจทุก sprint — review + retro ทุก 2 สัปดาห์ (ผิดพลาดพบเร็ว ปรับทันที); Hybrid ตรวจสองจังหวะ: มี gate ตาม milestone (เหมือน predictive — ควบคุม deadline) แต่ภายในยังเป็น sprint รอบสั้น (เหมือน agile — ได้ feedback จาก user เร็ว) — SHG เลือก Hybrid เพราะต้องล็อก launch ก่อน 1 พ.ย. แต่ยังอยากเห็นหน้าจอจริงจาก user ทุก sprint

### 4.2 Definition of Ready (DoR) และ Definition of Done (DoD) (D.6–D.7)

**[Best Practice]**
- **DoR (พร้อมเริ่ม):** Purpose, Scope, Requirement, Acceptance Criteria, Dependencies, Design/Decision, Test Data, Owner, Estimate, Priority
- **DoD (เสร็จจริง):** Build Complete, Code Review, Unit Test, Integration Test, Security Check, Documentation, Acceptance Criteria Pass, Defect Threshold Met, Deployed to Required Environment, Evidence Captured

**[Best Practice]** จำง่าย ๆ: **DoR ตอบ "พร้อมเริ่มไหม" — DoD ตอบ "เสร็จจริงไหม"**:

| | Definition of Ready (DoR) | Definition of Done (DoD) |
|---|---|---|
| ใช้ตอน | ก่อนรับงานเข้าสู่ sprint | ก่อนนับว่างานสำเร็จ |
| ตอบคำถาม | งานนี้เริ่มได้หรือยัง | งานนี้เสร็จจริงหรือยัง |
| ตัวอย่าง | scope ชัด, acceptance criteria มี, test data พร้อม, owner/estimate มี | build + review + unit test + integration + security + deploy + evidence ครบ |
| ถ้าไม่ผ่าน | ยังไม่เข้า sprint (หรือเข้าแบบมีเงื่อนไข) | ยังไม่นับ Done — กลับไปทำให้ครบ |

**[Teaching Scenario]** ตัวอย่าง DoD จริงของ SHG สำหรับ story "ชำระเงินด้วยบัตร (Payment Flow)": ( ) build เสร็จ ( ) peer review ผ่าน ( ) unit test ผ่าน ( ) integration test กับ 2C2P sandbox ผ่าน ( ) PCI-DSS checklist ผ่าน ( ) deploy ไป test environment ( ) evidence บันทึก (screenshot / test result) — ถ้าขาดข้อไหน ยังไม่ Done — อย่างกรณีใน opening scenario ที่ dev ตอบว่า "code เขียนเสร็จแล้วไง"

### 4.3 Manage Quality / QA — ฝั่งกระบวนการ (จาก lesson-10)

**[PMBOK 6]** Manage Quality (QA) = ดูว่ากระบวนการช่วยป้องกันปัญหาหรือไม่: design review, data migration checklist, test readiness gate, root-cause review, process improvement — **ไม่ใช่** การตรวจผลลัพธ์ (นั่นคือ Control Quality → Ch.8)

**[Best Practice]** Cost of Quality: Prevention/Appraisal (จ่ายเพื่อทำให้ถูก) ถูกกว่า Failure (rework, incident, lost trust) เสมอ — QA คือการลงทุนฝั่ง prevention

**[Teaching Scenario]** SHG QA activities ระหว่าง Sprint: test readiness gate ก่อนรับ story เข้า sprint, design review สำหรับ payment flow, data migration checklist ก่อน Sprint 7–8, regression policy ก่อน release

### 4.4 Develop Team และ Manage Team (จาก lesson-11)

**[PMBOK 6]**
- **Develop Team:** Tuckman (Forming → Storming → Norming → Performing), สร้าง trust, skill development, ให้อำนาจ (empowerment)
- **Manage Team:** จัดการ conflict ด้วย 5 เทคนิค — Collaborate/Problem Solve, Compromise, Withdraw/Avoid, Smooth/Accommodate, Force/Direct — ต้องเลือกตามสถานการณ์ ไม่ใช่ใช้วิธีเดียวทุกครั้ง
- **Manage Team inputs:** team performance, issue log, work performance data

**[Best Practice]** PM ไม่ใช่ "คนตามงาน" แต่เป็นผู้ที่ทำให้ทีมมีเป้าหมายร่วม, ขจัด blocker และสร้าง environment ที่ทีมทำงานได้ — ถ้าเห็น Storming (ขัดแย้ง) อย่าหนี ต้องจัดการเป็น process

### 4.5 Manage Communications / Risk / Stakeholder / Procurement ระหว่าง Execution (D.2)

**[Best Practice]** ตามแผนจาก Ch.5: Manage Communications (ส่งสารตาม cadence, จับ feedback), Implement Risk Responses (ทำตาม response plan, monitor trigger), Manage Stakeholder Engagement (ติดตาม engagement จริง vs แผน), Conduct Procurements (vendor ตาม contract, เก็บ evidence)

### 4.6 กล่อง Agile: Sprint Execution (จาก lesson-15/16)

**[PMBOK 8]** ถ้าใช้ Scrum (SHG ใช้สำหรับ UX/Booking Journey):
- **Sprint Planning:** เลือก backlog ตาม Sprint Goal — ปกป้อง Sprint Goal จากงานใหม่ที่แทรก
- **Daily Scrum (15 นาที):** เมื่อวานทำอะไร / วันนี้จะทำอะไร / มี blocker อะไร
- **Sprint Review:** โชว์ increment ให้ stakeholder ตรวจ — feedback เปลี่ยน backlog
- **Retrospective:** START / CONTINUE / STOP — ปรับปรุงกระบวนการ
- **Kanban** สำหรับ flow/support/incident: จำกัด WIP, เห็น bottleneck

**[Best Practice]** Agile ไม่ใช่การไม่มีวินัย — Ceremony ที่ไม่มี feedback ที่เปลี่ยน decision คือ Agile theater

## 5. PM Decision Thinking

```text
Decision: story "Payment Flow" ที่ code เสร็จแต่ test/security ยังไม่ครบ — ควรนับเป็น Done หรือไม่
Owner: Team + QA Lead (DoD check); PM ดูแล process; PO กำหนด business acceptance (Ch.8)
Inputs: DoD, test evidence, review records, security check, deployment status, sprint goal
Options:
  A: นับเป็น Done — เร็ว แต่ส่งของไม่ครบ DoD -> defect ไปตก Ch.8/Ch.9
  B: ไม่นับเป็น Done จนกว่าครบ DoD (แนะนำ) — ช้าชั่วคราว แต่คุณภาพอยู่ในกระบวนการ
  C: ปรับ DoD ให้เบาลง — ต้องผ่านทีม/PO และมีเหตุผล (เช่น ย้าย security check ไปขั้น release)
Trade-offs: velocity ระยะสั้น vs quality/trust ระยะยาว, sprint commitment vs reality
Risk: DoD ที่ยืดหยุ่นเกิน -> "เสร็จ" กลายเป็นคำไร้ความหมาย
Evidence: DoD checklist, sprint review minutes, quality metrics, blocker log
Next Action: นับตาม DoD -> update progress data -> Ch.7 (monitoring) / Ch.8 (verification)
```

## 6. ตัวอย่างจริงจาก Case ต่อเนื่อง (SHG)

**[Teaching Scenario] Watch PM Think — ระหว่าง Sprint 3 (Payment Flow)**

QA วาง test cases ตั้งแต่ช่วง design ไม่ใช่รอใกล้เสร็จ — คุณสุทธิ (PM) ยืนยันกับ QA lead: "payment ต้องเข้า DoR แบบมี test data ครบ: card test จาก 2C2P sandbox + design decision — ก่อนรับเข้าสู่ sprint" — เขารู้ว่าถ้า sandbox ไม่พร้อมตอนเริ่ม sprint จะกลายเป็น blocker กลางคัน

Developer บอก "code เสร็จแล้ว" — เขาเปิด DoD checklist: "build เสร็จ แล้ว unit test? security check? deploy ไป test env? evidence?" — คำตอบขาด 3 ข้อ → ยังไม่นับ Done — "เสร็จ" ต้องหมายถึงสิ่งเดียวกันทั้งทีม ไม่ใช่คนละคำพูด

Sprint 5–6: ทีม mobile กับ backend ใช้ API contract review ก่อน integration — เพราะ defect ที่พบตอน merge ระหว่างทีมแก้แพงกว่าที่พบตอน design

Retro ทุก sprint จบด้วย action (ปรับ WIP, แก้ bottleneck, ปรับปรุง test data readiness) — ไม่ใช่แค่คุยกันเพลิน ๆ

Blocker: PMS API doc ล่าช้า — เขา escalate ตาม RAID (R-01, owner คุณวีระ) ทันที ไม่รอให้ทีมติดค้างหลายวัน → vendor support เพิ่ม

**[PMBOK 8]** สังเกตว่าการทดสอบไม่ได้ "รอตอนท้าย" — มันถูกฝังในทุก sprint ผ่าน DoD และ test readiness gate ส่วนการตรวจรับอย่างเป็นทางการยังเป็นหน้าที่ของ Ch.8

## 7. จุดตัดสินใจและกับดักที่พบบ่อย

**Common Mistakes:**

1. ไม่มี DoR/DoD — ผล: รับงานไม่พร้อมเข้าสู่ sprint แล้ว "เสร็จ" ไม่ตรงกัน
2. QA มาทีหลัง (test หลัง build เสร็จหมด) — ผล: defect กองและแก้ช้า
3. Sprint Goal ถูกแทรกงานตลอด (marketing ขอ feature กลาง sprint) — ผล: สิ่งสำคัญไม่เสร็จ
4. Blocker ไม่ถูก escalate — ผล: ทีมติดค้างหลายวันโดยไม่มีใครรู้
5. Conflict ถูกหลีกเลี่ยงแทนจัดการ — ผล: พิษสะสม กระทบทีม
6. Manage Quality ถูกเข้าใจว่าเป็น QC — ผล: ไม่มีใครดูกระบวนการ มีแต่ตรวจผลปลายทาง
7. Retro ไม่มี action — ผล: วนทำผิดซ้ำเดิม

**Common Misconceptions:**

| ความเข้าใจผิด | ความจริง |
|---|---|
| Execution = เขียน code | คือสร้าง deliverables + evidence ผ่านกระบวนการ |
| QA คือตรวจผลตอนท้าย | QA = ดูกระบวนการ (prevention); QC = ตรวจผล (Ch.8) |
| "เสร็จ" = code เสร็จ | ต้องครบ DoD (test, review, security, deploy, evidence) |
| Agile ไม่ต้องมีวินัย | Agile มีวินัยที่สั้น เร็ว และเรียนรู้จาก evidence |
| PM ต้องสั่งงานทีมทุกอย่าง | PM สร้าง environment + ขจัด blocker; ทีม self-organize (Agile) |
| Retro เป็นแค่การประชุม | Retro ต้องจบด้วย action ที่มี owner |

## 8. Interview Questions

### Foundational
- **Q:** Definition of Done ต่างจาก Definition of Ready อย่างไร?
- **Answer Direction:** DoR = เกณฑ์ก่อนเริ่มงาน (scope, AC, test data, owner); DoD = เกณฑ์ว่าเสร็จจริง (build, review, test, security, deploy, evidence)
- **Warning Signs:** ตอบว่าเหมือนกัน หรือสลับกัน

### Scenario
- **Q:** Marketing ขอเพิ่ม feature กลาง Sprint 5 (Mobile App) — คุณจะจัดการอย่างไร?
- **Answer Direction:** ไม่รับเข้าสู่ sprint โดยตรง — ปกป้อง Sprint Goal; เอา feature เข้า backlog, ให้ PO (คุณนภา) จัด priority, ถ้าจำเป็นจริงต้องผ่าน change process (Ch.7) และยอมรับผลต่อ sprint commitment
- **Warning Signs:** รับทุกงานเข้า sprint เพราะ "Agile เปลี่ยนได้" หรือปฏิเสธโดยไม่มีทางเลือก

### Senior PM
- **Q:** ทีมมี conflict ระหว่าง dev กับ QA เรื่อง test data — คุณจะจัดการอย่างไร?
- **Answer Direction:** ใช้ conflict resolution ตามสถานการณ์: เริ่มจาก collaborate (หาต้นตอ — test data ไม่พร้อม?), ถ้าจำเป็น compromise/escortate ตาม governance — บันทึกเป็น process improvement ไม่ใช่โทษบุคคล
- **Warning Signs:** เลือกข้าง หรือหลีกเลี่ยงจนปัญหาโต

### Executive
- **Q:** ทำไมต้องลงทุนกับ QA ระหว่าง sprint ทั้งที่ "test จริงอยู่ Ch.8"?
- **Answer Direction:** QA (prevention) ถูกกว่า failure cost หลายเท่า — defect ที่พบใน sprint แก้ภายใน 2 ชั่วโมง; ที่พบใน UAT/Production แก้เป็นวัน/สัปดาห์ และกระทบ trust — QA ระหว่างทางลดงานและความเสี่ยงของ Ch.8/Ch.9
- **Warning Signs:** ตอบว่า "QA คือค่าใช้จ่าย" โดยไม่เห็น cost of quality

## 9. PM Dictionary ประจำบท

| Term (EN) | คำอธิบาย (TH) | ความหมายเชิงปฏิบัติ | การใช้ผิดที่พบบ่อย | Term ที่เกี่ยวข้อง |
|---|---|---|---|---|
| Definition of Ready | เกณฑ์พร้อมเริ่ม | scope, AC, test data, owner, estimate ชัด | สับสนกับ DoD | Definition of Done |
| Definition of Done | เกณฑ์เสร็จจริง | build + review + test + security + deploy + evidence | คิดว่า "code เสร็จ" = Done | Definition of Ready |
| Manage Quality (QA) | การประกันคุณภาพ | ดูกระบวนการป้องกัน defect | สับสนกับ QC | Control Quality |
| Control Quality (QC) | การควบคุมคุณภาพ | ตรวจผลลัพธ์จริง (Ch.8) | สับสนกับ QA | Manage Quality |
| Cost of Quality | ต้นทุนคุณภาพ | Prevention + Appraisal vs Failure | คิดว่า Quality = ค่าใช้จ่ายเพิ่ม | QA, QC |
| Sprint Goal | เป้าหมาย sprint | focus ของรอบส่งมอบ | ให้งานแทรกตลอด | Sprint |
| Daily Scrum | ประชุมประจำวัน | เมื่อวาน/วันนี้/blocker (15 นาที) | เป็น status meeting ยาว | Sprint |
| Retrospective | ทบทวนรอบ | START/CONTINUE/STOP + action | ไม่มี action ออกมา | Sprint Review |
| WIP Limit | จำกัดงานค้าง | ป้องกันรับงานเกิน capacity | ยิ่งทำหลายงานยิ่งเร็ว | Kanban |
| Tuckman | ขั้นพัฒนาทีม | Forming→Storming→Norming→Performing | คิดว่าทีมข้ามขั้นได้โดยไม่มี cost | Develop Team |
| Conflict Resolution | แก้ความขัดแย้ง | collaborate/compromise/withdraw/smooth/force | ใช้วิธีเดียวทุกครั้ง | Manage Team |
| Blocker | อุปสรรค | สิ่งที่ขัดงาน — ต้อง escalate | ปล่อยค้างไม่รายงาน | RAID, Escalation |

## 10. Workshop

### Scenario
**[Teaching Scenario]** กลาง Sprint 5 (Mobile App) QA พบว่า: (1) test data ของ payment sandbox ยังไม่พร้อม (2C2P ช้า), (2) Developer หนึ่งคนนับ story เป็น Done โดยไม่มี unit test, (3) Marketing ขอเพิ่ม "flash sale" หน้าจอหลัก — ทีมเริ่มมีเสียงบ่นกัน

### Your Role
PM (คุณสุทธิ) ที่ต้องรักษา Sprint Goal + quality process

### Available Information
- DoR/DoD ที่ทีมตกลงกัน, Sprint plan, RAID (R-01 PMS, 2C2P dependency), Scenario Master

### Missing Information
- 2C2P จะให้ sandbox เมื่อไร, QA เห็น defect trend อย่างไร, Marketing ต้องการ flash sale ในรอบนี้จริงหรือไม่ (impact ต่อ sprint commitment)

### Decision Required
- story ที่ไม่มี unit test จะจัดการอย่างไร, จะ escalate 2C2P อย่างไร, flash sale ควรเข้าสู่ sprint หรือ backlog

### Constraints
- DoD ต้องไม่ถูกลดโดยไม่มีเหตุผล, Sprint Goal (Mobile App core booking) ต้องไม่หลุด, ต้องไม่ขัดกับ Scenario Master (loyalty/feature ใหม่ = Phase 2+)

### Expected Output
- Decision record 3 ข้อ (DoD enforcement, 2C2P escalation, flash sale placement), blocker log update, sprint review agenda ที่รวม quality metrics

### Debrief Questions
1. ทำไมการบังคับ DoD ใน sprint ถึงช่วย Ch.8
2. การ escalate 2C2P ที่ดีต้องมีข้อมูลอะไร
3. Retro ที่ดีควรจบด้วยอะไร

### Evaluation Criteria
- DoD ไม่ถูกลดเงียบ ๆ, escalation มี evidence + owner, feature ใหม่เข้าผ่าน priority/change process, บันทึก decision ครบ

## 11. Checklist ใช้งานจริง (Execution / Phase D)

- [ ] DoR ใช้ก่อนรับงานเข้าสู่ sprint/work package
- [ ] DoD รวม test/review/security/deploy/evidence และถูกใช้จริง
- [ ] QA ทำงานคู่ขนาน (test cases ตั้งแต่ design; test readiness gate)
- [ ] Design/data review ก่อน merge (โดยเฉพาะ payment/PMS sync)
- [ ] Daily blocker management — blocker มี owner + escalate path
- [ ] Risk responses ถูก implement ตามแผน (Ch.5) + trigger monitor
- [ ] Stakeholder engagement ตามแผน (Ch.2) — ติดตามจริง vs desired
- [ ] Communication ตาม cadence (Ch.5) — มี feedback loop
- [ ] Team management: conflict จัดการเป็น process, performance feedback
- [ ] Work Performance Data ถูกเก็บ (ส่งให้ Ch.7)
- [ ] Retro (ถ้า Agile) จบด้วย action + owner
- [ ] Cross-ref: QC ผลจริง = Ch.8, monitoring/change = Ch.7

## 12. Assessment

1. **[Decision Case]** story code เสร็จแต่ไม่มี unit test + security check — จะจัดการอย่างไรโดยไม่ทำลาย velocity ระยะยาว?
2. **[Decision Case]** Marketing ขอ flash sale กลาง sprint — ตัดสินใจอย่างไร (เข้า sprint/backlog/change) พร้อมเหตุผล + กระบวนการ
3. **[Artifact Review]** ตรวจ sprint board ที่งานทุกชิ้น "Done" แต่ไม่มี evidence/test result — อธิบายว่าทำไม board นี้หลอก และแก้อย่างไร
4. **[Trade-off Case]** ระหว่างบังคับ DoD (ช้า 2 วัน) กับปล่อยผ่านแล้วแก้ใน Ch.8 — อธิบาย trade-off ด้าน cost of quality
5. **[Scenario Case]** QA กับ dev ขัดแย้งเรื่อง test data — เลือก conflict resolution technique พร้อมเหตุผลและขั้นตอน
6. **[Cross-Knowledge Analysis]** ถ้า 2C2P sandbox ช้า 1 สัปดาห์ — กระทบ sprint 3–4 (Ch.6), monitoring (Ch.7) และ UAT (Ch.8) อย่างไร
7. **[Recall]** ความต่างระหว่าง Manage Quality (QA) กับ Control Quality (QC) พร้อมตัวอย่างจาก SHG

## 13. Executive Summary

| มิติ | สรุป |
|---|---|
| **Why** | Execution คือจุดที่แผนกลายเป็น deliverables — วินัยตรงนี้กำหนดคุณภาพของ Ch.8/Ch.9 |
| **Decision Improved** | "เสร็จ" ถูกตัดสินด้วย DoD + evidence ไม่ใช่ความรู้สึก |
| **Failure Prevented** | ป้องกัน defect สะสม, sprint goal หลุด, conflict เน่า และ QA ที่มาทีหลัง |
| **What to Monitor** | DoD compliance, defect trend, blocker ageing, sprint velocity vs commitment |

## 14. เชื่อมไปบทถัดไป + Artifact Handoff

**Bridge:** Execution กำลังสร้าง deliverables พร้อม Work Performance Data — Ch.7 (Monitoring & Change) จะวัดผลจริงเทียบ baseline จัดการ variance และทำ Perform Integrated Change Control (Integration ท่อนที่ 2)

| Field | Handoff |
|---|---|
| Input | Integrated Plan, Baselines (Ch.4/Ch.5), Sprint/Work plan |
| Output | Deliverables, Work Performance Data, Quality/QA Evidence, Team/Blocker Records |
| Creator | Delivery Team + Leads; QA Lead (QA evidence); PM (team/process) |
| Artifact owner | Workstream Leads / QA Lead / PM |
| Reviewer | PM, QA, PO (business) |
| Approval authority | ตาม Governance; acceptance อย่างเป็นทางการ = Ch.8 |
| Minimum acceptance | Usable (evidence ต่อ deliverable + DoD check) |
| Next chapter use | Ch.7 ใช้ Work Performance Data + baselines ไปวัด variance, forecast และ change control |

## 15. Quick Reference Card

```text
EXECUTION (D) — เป้าหมาย: สร้าง deliverables + evidence ด้วยกระบวนการที่มีวินัย
------------------------------------------------------------
1. DoR ก่อนเริ่ม   -> scope, AC, test data, owner, estimate
2. Build/Integrate -> ตาม sprint/work package
3. Peer Review     -> ก่อน QA
4. Test ระหว่างทาง -> QA คู่ขนาน (ไม่ใช่รอท้าย)
5. DoD            -> build + review + test + security + deploy + evidence
6. Manage Quality  -> QA ดูกระบวนการ (prevention) | QC ตรวจผล = Ch.8
7. Team           -> Tuckman + conflict resolution + blocker escalation
8. Comms/Risk/Stakeholder -> ตามแผน Ch.5
9. Work Performance Data -> ส่ง Ch.7

Agile insert:
  Sprint Planning -> Daily Scrum -> Review -> Retro (START/CONTINUE/STOP)
  ปกป้อง Sprint Goal | Kanban: WIP limit + bottleneck

กฎ 3 ข้อห้าม:
- ห้าม "เสร็จ" โดยไม่ครบ DoD
- ห้าม QA มาทีหลัง
- ห้าม Retro ไม่มี action
```

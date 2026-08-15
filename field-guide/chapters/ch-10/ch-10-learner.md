---
chapter: ch-10
title: "Transition, Closure และ Benefit Handover (Playbook H)"
book: "PM Delivery Guide: From Pre-sales to Closure — คู่มือปฏิบัติการบริหารโครงการซอฟต์แวร์ (PMBOK 8th Edition)"
edition: Learner
status: Released
validation_status: Reviewed
last_reviewed: 2026-08-15
intended_learner_level: Experienced PM
difficulty: Core
estimated_study_time: 90
prerequisite:
  - "Ch.9 — Go-Live & Hypercare (Stabilization)"
related_chapters:
  - "Ch.2 — Initiation (Integration ท่อนที่ 1: Charter)"
  - "Ch.7 — Monitoring & Change (Integration ท่อนที่ 2: Change Control)"
canonical_source:
  - ../../references/PMBOK-Overview.md (PMBOK framework)
  - ../../e-Book/chapters/lesson-05/lesson-05-learner.md (Close Project or Phase)
scenario_version:
  hotel_booking: "1.0"
artifact_outputs:
  - name: Handover Pack (Operational)
    creator: Leads + Support
    artifact_owner: Operations Owner
    reviewer: PM, Support Lead
    approval_authority: Operations Owner
    approval_evidence: Accepted handover pack
  - name: Final Acceptance + Closure Report
    creator: PM
    artifact_owner: PM
    reviewer: Sponsor, Finance, Legal
    approval_authority: Sponsor / Acceptance Authority
    approval_evidence: Signed final acceptance + closure approval
  - name: Lessons Learned + Benefit Handover Plan
    creator: PM + Team / PM + Business Owner
    artifact_owner: PM / Benefit Owner (Business)
    reviewer: Sponsor
    approval_authority: Sponsor (benefit plan)
    approval_evidence: Lessons register + approved benefit plan
---

# Chapter 10 — Transition, Closure และ Benefit Handover: ปิดโครงการอย่างมืออาชีพ

## 1. Opening Scenario Hook

**[Teaching Scenario]** SHG ผ่าน stabilization 2 เดือนหลัง soft launch — ทีมลดเหลือ 6 คนตาม Operating Model (Scenario Master §16) และคุณสุทธิ (PM) เตรียม "ปิดโครงการ" แต่ยังมีคำถาม: ใครเป็น owner ของระบบหลังส่งมอบ, contract กับ 2C2P/PMS vendors ปิดยังไง, lessons learned เก็บไว้ที่ไหน, และที่สำคัญ — **ใครรับผิดชอบว่า direct booking จะถึง 35% ใน 18 เดือน**

**[PMBOK 8]** บทสุดท้ายของ workflow A→H: **Close Project or Phase** (Integration ท่อนที่ 3 ของ 3) — ปิดภาระผูกพันทั้งหมด, ส่งมอบให้ Operations, ปิด contract/การเงิน, เก็บบทเรียน และกำหนด Benefit Owner — **Go-live ไม่ใช่จุดจบ; Closure คือจุดที่ Output ถูกส่งต่อให้กลายเป็น Outcome และ Benefit**

## 2. Why It Matters

**[Best Practice]** โครงการที่ปิดไม่ดี: ระบบถูกส่งต่อแบบไม่มี owner → หลัง 3 เดือนไม่มีใครดูแล, benefit ไม่มีคนวัด → 35% direct booking ไม่รู้ว่าเกิดหรือไม่, lessons ไม่ถูกเก็บ → องค์กรวนทำผิดซ้ำ, และ contract ยังค้าง → ภาระผูกพันทางการเงิน/กฎหมาย

**[PMBOK 6]** Closing ไม่ใช่แค่ "ส่ง deliverable" — ครอบคลุม acceptance, knowledge transfer, contract/admin closure, open-item ownership และ transition to operation — นี่คือจุดที่บทเรียน lesson-01 กลับมา: Output ต่างจาก Outcome และ Benefit ต้องมี owner หลัง handover

## 3. Mental Model

```text
Stabilization Acceptance (Ch.9)
  -> Operational Handover (H.3) — owner, support model, SLA, runbook
  -> Final Acceptance (H.4) — deliverables ครบ + sign-off
  -> Contract/Financial Closure (H.5) — invoice, payment, vendor, PO
  -> Lessons Learned (H.6) — what worked/didn't + action owner
  -> Benefit Handover (H.7) — benefit owner, measure, baseline, review date
  -> Closure Report (H.8) + Sponsor Approval (H.9 exit criteria)
```

## 4. Main Lesson

### 4.1 Operational Handover (H.3)

**[Best Practice]** ต้องมี: System Ownership, Support Model, SLA, Runbook, Monitoring, Incident Process, Backup, DR, Access, Vendor Contact, Known Issues, Maintenance

**[Best Practice]** ทำไม handover ถึงไม่ใช่ "ส่งเอกสาร": เอกสารที่ไม่มีใครอ่านคือข้อมูล ไม่ใช่ความสามารถ — เป้าหมายคือทำให้ Ops **รับช่วงได้จริง** นั่นคือ: มีเจ้าของระบบชัดเจน (System Ownership), มี runbook ที่ใช้ได้กับระบบจริง (ไม่ใช่เขียนจากจินตนาการ), ทีม support ผ่าน training และลองทำจริง, และมี SLA ว่าใครตอบ incident ภายในกี่นาที — **ทดสอบว่า Ops ใช้ runbook แก้ incident จำลองได้ไหม** ก่อนประกาศ handover สำเร็จ เช่นเดียวกับที่ Ch.9 บอกว่า rollback ต้องทดสอบ ไม่ใช่แค่มีแผน

**[Teaching Scenario]** SHG: ทีมเหลือ 6 คน (2 Frontend, 2 Backend, 1 QA, 1 DevOps) — PM ส่งมอบ runbook + monitoring + incident process ให้ Operations; hypercare (Ch.9) เปลี่ยนเป็น support ตาม SLA; known issues (เช่น PMS sync error 5%) มี plan + owner

### 4.2 Final Acceptance (H.4)

**[Best Practice]** ตรวจ: Contract Deliverables, Acceptance Evidence, Outstanding Items, Waiver, Warranty, Payment, Sign-off — acceptance ต้องอ้าง evidence จาก Ch.8 (UAT sign-off) ไม่ใช่แค่ "ดูแล้วโอเค"

### 4.3 Contract และ Financial Closure (H.5)

**[Best Practice]** Final Invoice, Payment, Vendor Closure, Asset Transfer, License, PO Closure, Budget Reconciliation — ปิดกับ 2C2P, PMS vendors, AWS, Design Agency ตามสัญญา (Ch.1–2 ตั้งต้น vendor relationship, Ch.5 วาง procurement)

**[Best Practice]** จุดที่คนมักลืมสองอย่าง: (1) **warranty เริ่มนับจากวันไหน** — ปกตินับจาก final acceptance ไม่ใช่จาก go-live เพราะช่วง hypercare (Ch.9) ยังเป็นความรับผิดชอบของทีม implement; (2) **resource release ต้องเป็นทางการ** — ทีมถูกปล่อย/ย้ายงานอย่างเป็นทางการพร้อมบันทึก ไม่ใช่ "ค่อย ๆ หายไป" — และ budget reconciliation ต้องปิดยอดจริง: งบ 12M ใช้ไปเท่าไหร่ เหลือเท่าไหร่ ใคร approve — เพื่อไม่ให้ใบแจ้งหนี้ vendor ตามมาทีหลังโดยไม่มีงบรองรับ

### 4.4 Lessons Learned (H.6)

**[Best Practice]** เก็บ: What Worked, What Did Not, Root Causes, Decisions, Risk Outcomes, Estimate Accuracy, Stakeholder Lessons, Technical Lessons, Recommended Actions, Owner for Improvement — lessons ที่ไม่มี action owner = แค่บันทึก

**[Best Practice]** ทำไม lessons ต้องเก็บ**ระหว่าง**โครงการ ไม่ใช่รอจบ: ความจำของทีมสั้น และทีมเริ่มแยกย้ายทันทีที่งานหลักจบ — เดือนที่ 8 ไม่มีใครจำได้แล้วว่า Sprint 3 ตัดสินใจอะไรและทำไม — เทคนิคที่ใช้จริง: ทำ **retrospective สั้น ๆ** หลัง milestone/sprint สำคัญ (What worked / What didn't / Root cause / Action + owner) เก็บเข้า register ทันที — ตอนปิดโครงการเหลือแค่รวบรวม + ทวน + ปิด action ในประชุมครั้งเดียว ไม่ใช่พยายามนึกย้อน 11 เดือน

**[Teaching Scenario]** SHG lessons: PMS PoC ก่อน Sprint 1 ช่วยลด risk จริง, fast-track Back Office เพิ่ม defect (ควรประเมิน quality impact ให้ดี), test data readiness ต้องเข้า DoR ตั้งแต่แรก

### 4.5 Benefit Handover (H.7) — Output ≠ Benefit

**[PMBOK 6]** ต้องระบุ: Benefit Owner, Benefit Measure, Baseline, Target, Measurement Date, Data Source, Review Cadence

**[Best Practice]** ตรงนี้คือจุดที่ **Output กลายเป็น Outcome และ Benefit**: ระบบจองที่ส่งมอบ (Output) → คนใช้จริง (Outcome) → ตัวเลขธุรกิจที่เปลี่ยน (Benefit) — PM ปิดโครงการแล้วออกไป แต่ตัวเลข 35% ยังต้องถูกวัดต่อ: ต้องระบุ **ใครวัด (Benefit Owner = business), วัดจากข้อมูลอะไร (data source), เทียบกับอะไร (baseline 10%), และเมื่อไหร่ (measurement date + review cadence)** ก่อน Sponsor อนุมัติปิด — ถ้าไม่ล็อกตอนนี้ หลัง 6 เดือนจะไม่มีใครรู้ว่า "ควรจะถึงเท่าไหร่แล้ว และใครเป็นคนดู"

**[Teaching Scenario]** SHG: Benefit = Direct Booking 10% → 35% ภายใน 18 เดือน — Owner = คุณภัทร (VP Marketing) + คุณนภา (PO) ตาม Operating Model — Measure = % direct booking จากระบบ — Baseline = 10% — Review = รายเดือน post-launch (ตรง Scenario Master §14–15) — **PM ไม่ใช่ benefit owner หลังปิดโครงการ**

### 4.6 Closure Report (H.8) + Exit Criteria (H.9)

**[Best Practice]** Closure Report: Objectives, Scope Delivered, Acceptance, Schedule, Cost, Quality, Risks, Changes, Benefits, Outstanding, Lessons, Handover, Final Approval

**[Best Practice]** Closure Report คือ**หลักฐานการปิดโครงการ** — ถ้าเกิดคำถามทีหลัง (ทำไมจบแบบนี้, ใครอนุมัติ, มีอะไรค้าง) ทุกคนเปิดรายงานนี้แล้วได้คำตอบเดียวกัน — หัวใจคือการ**เทียบ plan vs actual** (schedule, cost, scope ที่ promised ไว้ใน Charter/Ch.1–2 เทียบสิ่งที่เกิดขึ้นจริง) และบันทึก open items อย่างเป็นทางการ — ไม่ใช่แค่สรุปว่าสำเร็จ

**Exit Criteria:** Deliverables Accepted, Operations Handover Complete, Support Ready, Financial Closure, Contract Closure, Lessons Captured, Resources Released, Benefit Owner Assigned, Sponsor Approves Closure

## 5. PM Decision Thinking

```text
Decision: โครงการ SHG พร้อมปิดหรือยัง — หรือต้องปิด open items ใดก่อน (เช่น PMS known issue, contract 2C2P)
Owner: PM เสนอ closure; Sponsor อนุมัติ; Operations Owner รับ handover; Benefit Owner (คุณภัทร) รับ benefit
Inputs: closure report draft, handover pack, acceptance evidence, contract status, lessons, benefit plan
Options:
  A: ปิดเลย — ทุก exit criteria ผ่าน
  B: ปิดแบบมีเงื่อนไข (open items มี owner + due date) — เช่น known issue ฝาก Operations ตาม SLA
  C: ยังไม่ปิด — ขาด acceptance/contract/benefit owner ที่จำเป็น
Trade-offs: release resources early vs completeness, momentum vs governance
Risk: ปิดเร็ว -> ภาระผูกพันค้าง; ปิดช้า -> ทรัพยากรผูกเปล่า
Evidence: signed acceptance, handover acceptance, closure report, sponsor approval
Next Action: หลังปิด -> PIR/benefit review ตาม cadence (คุณภัทร) + lessons นำไปใช้
```

## 6. ตัวอย่างจริงจาก Case ต่อเนื่อง (SHG)

**[Teaching Scenario] Watch PM Think — สัปดาห์สุดท้ายก่อนปิดโครงการ**

คุณสุทธิ (PM) ไล่ทวนรายการปิดโครงการในใจ: "Handover ต้องไม่ใช่แค่ส่งไฟล์ — ให้ Ops ซ้อม runbook แก้ incident จำลองแล้วหรือยัง, known issue PMS sync 5% มี owner และ SLA ใน handover หรือยัง" — เขารู้ว่าตรงนี้คือจุดที่ "ส่งต่อได้จริง" ต่างจาก "ส่งเอกสาร"

Final acceptance: เขาดึง UAT evidence จาก Ch.8 มาประกอบ ไม่ใช่ "คุณภัทรดูแล้วโอเค" — มี waiver อย่างเป็นทางการสำหรับ cosmetic defect ที่ยอมรับแบบเลื่อน — "ถ้าไม่มี evidence ตอนนี้ จะเถียงกันตอนจ่ายเงิน"

Financial/contract: ปิด 2C2P (settlement reconciliation), PMS vendors (final T&M ตาม cap), AWS (โอน ownership ของ account), Design Agency (final payment ตาม milestone) — เขาเช็คว่า warranty นับจาก final acceptance และทีมถูก release อย่างเป็นทางการ

Lessons: 3 บทเรียนหลักที่เก็บระหว่างทาง (PMS PoC ช่วยจริง, fast-track เพิ่ม defect, test data ต้องเข้า DoR) — แต่ละข้อมี action owner ไม่ใช่แค่ "เล่ากันฟัง"

สุดท้าย — สิ่งที่เขาเน้นที่สุด: **Benefit Handover** — Owner = คุณภัทร, Target = 35% ภายใน 18 เดือน, Baseline = 10%, Review = รายเดือน, Data source = booking analytics — "PM ปิดแล้วออกไป แต่ตัวเลข 35% ต้องมีคนวัด — ถ้าไม่ล็อกตรงนี้ตอนนี้ หลัง 6 เดือนจะไม่มีใครรู้ว่าใครดูตัวเลขนี้"

Sponsor (คุณจิรา) อนุมัติ closure — PIR หลัง 6 เดือนตรวจ benefit

**[PMBOK 8]** สังเกตว่า "ความสำเร็จของโครงการ" ณ จุดนี้คือ "ส่งต่อได้อย่างเป็นระเบียบ" — benefit จริง (35%) จะวัดกันทีหลัง โดยคนที่รับผิดชอบคือ business ไม่ใช่ทีม project

## 7. จุดตัดสินใจและกับดักที่พบบ่อย

**Common Mistakes:**

1. คิดว่า Go-live (Ch.9) = ปิดโครงการ — ผล: ไม่มี handover/benefit owner
2. ส่งระบบให้ Ops โดยไม่มี runbook/SLA/known-issue plan — ผล: support งง หลัง 3 เดือนพัง
3. Acceptance จากการ "ดูแล้วโอเค" ไม่มี evidence — ผล: dispute ตอนจ่ายเงิน/ปิด
4. ไม่ปิด contract/finance — ผล: ภาระค้าง ใบแจ้งหนี้เกิน
5. Lessons learned เป็นพิธี ไม่มี action owner — ผล: องค์กรวนทำผิดซ้ำ
6. Benefit ไม่มี owner หลังปิด — ผล: 35% ไม่มีใครวัด (lesson-01 บทเรียนเดิม)
7. ปล่อย resource โดยไม่ release อย่างเป็นทางการ — ผล: ทีมถูกดึงไปงานอื่นยังไม่ปิด

**Common Misconceptions:**

| ความเข้าใจผิด | ความจริง |
|---|---|
| Project จบเมื่อ system ส่งมอบ | จบเมื่อ exit criteria ครบ (H.9) |
| PM เป็น benefit owner หลังปิด | Benefit Owner ต้องเป็น business (คุณภัทร) |
| Lessons learned = ประชุมเล่ากันฟัง | ต้องมี register + action owner |
| Acceptance = เซ็นรับของ | ต้องอ้าง evidence (Ch.8 UAT sign-off) |
| Closure = เอกสารเยอะ | Closure = ปิดภาระผูกพัน + เก็บบทเรียน + ตั้ง benefit |
| Handover = ส่งไฟล์ | Handover = owner + support model + SLA + known issues |

## 8. Interview Questions

### Foundational
- **Q:** องค์ประกอบของ Operational Handover (H.3) มีอะไรบ้าง?
- **Answer Direction:** System Ownership, Support Model, SLA, Runbook, Monitoring, Incident Process, Backup, DR, Access, Vendor Contact, Known Issues, Maintenance
- **Warning Signs:** ตอบ "ส่งเอกสารให้ Ops"

### Scenario
- **Q:** หลัง stabilization คุณพบว่า PMS known issue ยังค้าง (sync 5% error) — คุณจะปิดโครงการอย่างไร?
- **Answer Direction:** ไม่ปิดแบบไร้เงื่อนไข — ฝากเป็น known issue ใน handover (มี owner + SLA + due date), บันทึกใน closure report + residual risk, และเชื่อมกับ benefit plan (Inventory Sync Accuracy ≥ 98%) — closure แบบมีเงื่อนไขที่ชัดเจน
- **Warning Signs:** ปิดเลยโดยไม่พูดถึง known issue หรือเลื่อนปิดโดยไม่มีเหตุผล

### Senior PM
- **Q:** Benefit (35% direct booking) จะถูกวัดหลังปิดโครงการ — คุณจะมั่นใจได้อย่างไรว่ามันจะเกิด?
- **Answer Direction:** ตั้ง Benefit Owner (คุณภัทร) + measure + baseline + target + review cadence + data source ก่อนปิด; ทำ benefit handover เป็นส่วนหนึ่งของ closure; จัด PIR ตามรอบ — PM ไม่ต้องเป็น owner แต่ต้องทำให้ ownership ชัดเจนก่อนจาก
- **Warning Signs:** ตอบว่า "ไม่ใช่เรื่องเราหลังปิด" โดยไม่จัด ownership

### Executive
- **Q:** ทำไมต้องเสียเวลากับ Lessons Learned ในเมื่องานเสร็จแล้ว?
- **Answer Direction:** lessons ที่มี action owner ช่วยให้องค์กรไม่จ่ายค่า tuition ซ้ำ (estimate, vendor, test readiness) — ต้นทุนเล็กน้อย vs วนทำผิดซ้ำในโครงการถัดไป; เป็นส่วนหนึ่งของ organizational learning
- **Warning Signs:** ตอบว่า "ไม่มีเวลา" หรือทำเป็นพิธี

## 9. PM Dictionary ประจำบท

| Term (EN) | คำอธิบาย (TH) | ความหมายเชิงปฏิบัติ | การใช้ผิดที่พบบ่อย | Term ที่เกี่ยวข้อง |
|---|---|---|---|---|
| Handover | การส่งมอบผลงาน | owner + support model + SLA + runbook + known issues | คิดว่า Go-live = handover สำเร็จ | Transition to Operation |
| Transition to Operation | ส่งต่อให้ฝ่ายปฏิบัติการ | วางแผนตั้งแต่ Planning (Ch.5 C17) | คิดว่า Go-live = ส่งมอบเสร็จ | Handover |
| Final Acceptance | ตรวจรับสุดท้าย | deliverables ครบ + evidence + sign-off | เซ็นแบบพิธี | Acceptance |
| Contract Closure | ปิดสัญญา | invoice, payment, vendor, PO, license | ค้างไว้ไม่มีใครปิด | Financial Closure |
| Lessons Learned | บทเรียน | what worked/didn't + action owner | ประชุมเล่ากันฟัง | PIR |
| Benefit Owner | เจ้าของ benefit | business คนที่วัดผล หลังปิดโครงการ | PM เป็น owner | Benefit |
| Benefit Measure | ตัววัด benefit | % direct booking, commission saved | ตั้งโดยไม่ผูก baseline | Baseline, Target |
| Closure Report | รายงานปิดโครงการ | objectives, scope, acceptance, cost, lessons, handover | เขียนสั้น ๆ ไม่มีหลักฐาน | Exit Criteria |
| PIR | Post-Implementation Review | ทบทวนหลัง implement เทียบ target | ทำช้าเกินไปจนไม่มีใครจำ | Lessons Learned |
| Exit Criteria | เกณฑ์ปิด | H.9 — ครบแล้ว Sponsor อนุมัติปิด | เปิดใช้เฉพาะตอนปิด | Closure Report |
| Open Items | รายการค้าง | ต้องมี owner + due date ก่อนปิด | ปิดโดยไม่พูดถึง | Waiver |
| Waiver | การสละสิทธิ์/เลื่อน | ยอมรับ item ที่เลื่อน อย่างเป็นทางการ | ใช้ปิดบังปัญหา | Open Items |

## 10. Workshop

### Scenario
**[Teaching Scenario]** SHG ใกล้ปิดโครงการ: ทีมลดเหลือ 6 คน, hypercare จบ, แต่ (1) PMS known issue (sync 5%) ยังค้าง, (2) 2C2P ยังมี final invoice ไม่ชัดเจน, (3) lessons learned ยังไม่ถูกเก็บ, (4) คุณภัทร ยังไม่ได้ยืนยันว่าเป็น benefit owner

### Your Role
PM (คุณสุทธิ) ที่ต้องทำให้ Closure สมบูรณ์

### Available Information
- Stabilization acceptance (Ch.9), UAT evidence (Ch.8), contract list (2C2P, PMS vendors, AWS, Design Agency), Scenario Master §14–16 (outcomes, benefits, operating model)

### Missing Information
- ความชัดเจน final invoice 2C2P, SLA/owner ของ PMS known issue ที่ Ops ยอมรับ, กำหนดการ lessons workshop, confirmation ของคุณภัทรเรื่อง benefit review cadence

### Decision Required
- ปิดเลย / ปิดแบบมีเงื่อนไข (open items + owner + due date) / เลื่อนปิด — และใครเป็น owner ของแต่ละ item

### Constraints
- Exit criteria (H.9) ต้องครบก่อน Sponsor อนุมัติ, benefit owner ต้องเป็น business ไม่ใช่ PM, ห้ามปิดโดยไม่มี handover

### Expected Output
- Closure recommendation + open-items log (owner + due date), handover pack checklist, lessons register (3 items + action owners), benefit handover plan (owner, measure, baseline, target, cadence)

### Debrief Questions
1. Open items แบบไหนที่ "ปิดแบบมีเงื่อนไขได้" และแบบไหนที่ต้องปิดก่อน
2. ทำไม benefit owner ต้องชัดเจนก่อน Sponsor อนุมัติ closure
3. Lessons ที่ดีควรจบด้วยอะไร

### Evaluation Criteria
- Exit criteria ถูกใช้จริง, open items มี owner + due date, benefit plan ครบ (owner/measure/baseline/target/cadence), lessons มี action owner, ไม่ขัด Scenario Master

## 11. Checklist ใช้งานจริง (Transition & Closure / Phase H)

- [ ] Operational Handover ครบ: owner, support model, SLA, runbook, monitoring, incident, backup/DR, access, vendor contact, known issues
- [ ] Final Acceptance อ้าง evidence (Ch.8) + waiver อย่างเป็นทางการ
- [ ] Contract/Financial Closure: invoice, payment, vendor, PO, license, budget reconciliation
- [ ] Lessons Learned register + action owners
- [ ] Benefit Handover: owner (คุณภัทร), measure, baseline (10%), target (35%/18 เดือน), data source, review cadence
- [ ] Closure Report ครบ (H.8)
- [ ] Exit criteria (H.9) ตรวจแล้ว: deliverables accepted, handover complete, support ready, finance/contract closed, lessons captured, resources released, benefit owner assigned
- [ ] Sponsor อนุมัติ closure
- [ ] PIR/benefit review กำหนดไว้ (เช่น 6 เดือน)
- [ ] ส่งต่อ: benefit measurement เป็นของ business; lessons กลับสู่องค์กร

## 12. Assessment

1. **[Decision Case]** PMS known issue ยังค้างก่อน closure — ปิดเลย/ปิดมีเงื่อนไข/เลื่อน พร้อมเหตุผล + owner + due date
2. **[Decision Case]** คุณภัทรยังไม่ยืนยันบทบาท benefit owner — คุณจะทำอย่างไรก่อน Sponsor อนุมัติ closure
3. **[Artifact Review]** ตรวจ Closure Report ที่ไม่มี handover/lessons/benefit owner — ระบุสิ่งที่ขาดและผล
4. **[Scenario Case]** 2C2P final invoice ไม่ตรงกับที่ตกลง — ขั้นตอนการจัดการ (H.5) พร้อม evidence
5. **[Trade-off Case]** ปิดเร็ว (ปล่อยทีม) vs ปิดช้า (เก็บทีมไว้) — trade-off ต่อ open items และต้นทุน
6. **[Cross-Knowledge Analysis]** ถ้า 6 เดือนหลัง launch direct booking ได้ 20% (ไม่ถึง 35%) — ใครทำอะไร (benefit owner, PM? PIR) และระบบที่ปิดไปแล้วจะจัดการอย่างไร
7. **[Recall]** Exit Criteria (H.9) มีอะไรบ้าง (ระบุ ≥ 6)

## 13. Executive Summary

| มิติ | สรุป |
|---|---|
| **Why** | Closure คือจุดที่โครงการส่งต่อ output ให้ business สร้าง outcome/benefit ต่อ |
| **Decision Improved** | ปิดด้วย exit criteria + open-items owner แทน "ดูว่าเสร็จแล้ว" |
| **Failure Prevented** | ป้องกัน handover ไร้เจ้าภาพ, contract ค้าง, lessons ที่ไม่ถูกใช้ และ benefit ไร้ owner |
| **What to Monitor** | Benefit trend (35% ใน 18 เดือน), known issues, PIR schedule |

## 14. จบเล่ม + Artifact Handoff

**จบ workflow A→H:** จาก Opportunity (Ch.1) ถึง Closure (บทนี้) — ผู้อ่านที่ทำครบทั้ง 11 บทจะเห็นวงจรครบ: Value (Ch.1) → Authorization (Ch.2) → Scope (Ch.3) → Plan (Ch.4–5) → Execute (Ch.6) → Control (Ch.7) → Verify (Ch.8) → Go-Live (Ch.9) → Close (Ch.10) — Appendix A–F เป็นเครื่องมือ lookup สำหรับ field use

| Field | Handoff |
|---|---|
| Input | Stabilization acceptance (Ch.9), UAT evidence (Ch.8), contract list (Ch.1/Ch.5) |
| Output | Handover Pack, Final Acceptance, Contract/Financial Closure, Lessons Learned, Benefit Handover Plan, Closure Report |
| Creator | PM + Leads (handover), PM (closure report), PM + Business Owner (benefit) |
| Artifact owner | Operations Owner (handover), Business Owner (benefit), PM (closure) |
| Reviewer | Sponsor, Finance, Legal, Operations |
| Approval authority | Sponsor / Acceptance Authority |
| Minimum acceptance | Usable (exit criteria ครบ + open items มี owner) |
| Next use | Benefit review/PIR หลังปิด (business); lessons ใช้ในโครงการถัดไป |

## 15. Quick Reference Card

```text
TRANSITION & CLOSURE (H) — เป้าหมาย: ปิดภาระผูกพัน + ตั้ง benefit owner
------------------------------------------------------------
1. Handover   -> owner, support model, SLA, runbook, known issues
2. Acceptance -> deliverables + evidence + sign-off (อ้าง Ch.8)
3. Contract   -> invoice, payment, vendor, PO, license, reconciliation
4. Lessons    -> what worked/didn't + action owner
5. Benefit    -> owner (business), measure, baseline, target, cadence
6. Report     -> objectives, scope, acceptance, cost, lessons, handover
7. Exit       -> H.9 ครบ -> Sponsor อนุมัติ -> PIR ตามรอบ

กฎ 3 ข้อห้าม:
- ห้ามคิดว่า Go-live = จบ (จบจริงที่นี่)
- ห้ามปิดโดยไม่มี benefit owner
- ห้าม lessons ไม่มี action owner

Integration note: Charter = Ch.2 | Change = Ch.7 | Closure = บทนี้ — ครบ 3 ท่อน
```

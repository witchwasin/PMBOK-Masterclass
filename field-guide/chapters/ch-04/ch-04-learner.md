---
chapter: ch-04
title: "Schedule, Cost และ Resource (Playbook C8–C13)"
book: "PM Delivery Guide: From Pre-sales to Closure — คู่มือปฏิบัติการบริหารโครงการซอฟต์แวร์ (PMBOK 8th Edition)"
edition: Learner
status: Draft
validation_status: Not Validated
last_reviewed: 2026-08-15
intended_learner_level: Experienced PM
difficulty: Advanced
estimated_study_time: 120
prerequisite:
  - "Ch.3 — Requirements, Scope และ WBS"
related_chapters:
  - "Ch.7 — Monitoring & Change (EVM ฝั่ง Control)"
  - "Ch.6 — Execution (Develop/Manage Team)"
canonical_source:
  - ../../references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md (Phase C8–C13)
  - ../../e-Book/chapters/lesson-08/lesson-08-learner.md (Schedule เต็มบท)
  - ../../e-Book/chapters/lesson-09/lesson-09-learner.md (Cost/EVM เต็มบท)
  - ../../e-Book/chapters/lesson-11/lesson-11-learner.md (Resource เต็มบท)
  - ../../e-Book/chapters/lesson-15/lesson-15-learner.md + lesson-16 (Agile inserts)
scenario_version:
  hotel_booking: "1.0"
artifact_outputs:
  - name: Activity List + Dependency Network + Schedule Baseline
    creator: PM + Planner
    artifact_owner: PM
    reviewer: Functional Leads
    approval_authority: Sponsor / Steering Committee
    approval_evidence: Approved schedule baseline
  - name: Cost Estimate + Cost Baseline
    creator: PM + Finance
    artifact_owner: PM + Finance
    reviewer: Commercial
    approval_authority: Sponsor / Finance
    approval_evidence: Approved cost baseline
  - name: Consolidated Resource Plan + RACI
    creator: PM + Functional Leads
    artifact_owner: PM
    reviewer: Functional Managers
    approval_authority: Functional Managers (capacity) / Steering (exceptions)
    approval_evidence: Capacity sign-off + RACI approval
---

# Chapter 04 — Schedule, Cost และ Resource: แปลง Scope เป็นแผนที่วัดได้

## 1. Opening Scenario Hook

**[Teaching Scenario]** คุณสุทธิ (PM SHG) นั่งดู Gantt chart ที่ทีมวาดให้: มีแถบสีสวยงาม 12 Sprint ตาม Scenario Master แต่เมื่อคุณถามว่า "ถ้า Payment Integration ช้า 1 สัปดาห์ กระทบ launch วันที่ 1 พ.ย. หรือไม่" ไม่มีใครตอบได้ เพราะไม่มี dependency network, ไม่มี float, ไม่มี critical path

คุณวีระ (CTO) บอกว่า "ใช้เงิน 12 ล้านก็จบ" แต่คุณกาญจนา (Revenue Manager) ถามว่า "เงิน 12 ล้านนี่ใช้ตอนไหน และถ้าเร่งงานต้องเพิ่มงบเท่าไร" และคุณสมศรี (VP Ops) กังวลว่า "key users 80 คนมีงานประจำ จะมาทดสอบ UAT ได้จริงหรือ"

**[PMBOK 8]** บทนี้รวม 3 Knowledge Areas ที่ทำงานคู่กัน: Schedule (งานจะเสร็จเมื่อไร), Cost (ต้องใช้เงินเท่าไร ตอนไหน) และ Resource (ใครทำ มีเวลาจริงหรือไม่) — แยกดูทีละตัวก็เห็น แต่จะเห็นภาพจริงก็ต่อเมื่ออ่านพร้อมกัน

## 2. Why It Matters

**[PMBOK 6]** Schedule ที่ดีต้องตอบได้ว่า: ถ้างานหนึ่งช้า งานใดช้าตาม งานใดมีเวลาสำรอง และ recovery option ใดคุ้มค่า — Cost ที่ดีต้องอ่านเงินคู่กับงาน (Earned Value) ไม่ใช่ดูว่า "ใช้ไปเท่าไร" — Resource ที่ดีต้องแยก "มีชื่อในแผน" ออกจาก "มี capacity จริง"

**[Best Practice]** โครงการส่วนใหญ่พังไม่ใช่เพราะขาดแผน แต่เพราะแผนเป็นแค่ภาพ ไม่ใช่ระบบที่ตอบคำถาม "ถ้า...แล้ว...": ถ้า Payment ช้า แล้ว launch ล่าช้าไหม ถ้า key users ไม่ว่าง แล้ว UAT เลื่อนไหม ถ้าใช้เงินเกิน แล้ว baseline ไหนต้องเปลี่ยน

## 3. Mental Model

```text
WBS Work Packages (Ch.3)
  -> Activity List (C8) — งานย่อยที่ลงมือทำได้
  -> Dependency Network (C9) — อะไรมาก่อน/หลัง
  -> Duration Estimate (C10) — effort vs duration ต้องแยก
  -> CPM + Float (C11) — critical path คือเส้นที่กำหนดโครงการ
  -> Schedule Baseline (C11) — ฐานวัด variance
  -> Cost Estimate + Time-phased Baseline (C12) — เงินตามเวลา
  -> EVM: PV / EV / AC (C12) — วัด performance ระหว่างทาง
  -> Resource Plan + RACI (C13) — ใครทำ มี capacity จริงหรือไม่
  -> Ch.5 (Risk/Procurement/Comms) + Ch.6 (Execution)
```

## 4. Main Lesson

### 4.1 Schedule — จาก Work Package เป็นกิจกรรม (C8–C11)

**[PMBOK 6]** เปลี่ยน Work Package (Ch.3) เป็น Activity List + Activity Attributes + Milestone List — WBS ไม่ใช่ Activity List

**Dependency 4 แบบ (C9):** Finish-to-Start (ทั่วไป), Finish-to-Finish, Start-to-Start, Start-to-Finish — แหล่งที่มา: Mandatory, Discretionary, External, Internal — อย่าลืม Lead (เริ่มก่อนจบ) และ Lag (เวลารอ)

**CPM (C11):**
```text
Forward Pass: EF = ES + Duration
Backward Pass: LS = LF - Duration
Total Float: TF = LS - ES (หรือ LF - EF)
Critical Path = เส้นทางที่กำหนด Project Duration (โดยทั่วไป TF ต่ำสุด/เป็นศูนย์)
```

**[PMBOK 6]** Three-point Estimate (PERT): **E = (O + 4M + P) / 6** — O = optimistic, M = most likely, P = pessimistic — ทำไมต้องถ่วง M 4 เท่า: เพื่อ**ลดผลของ outlier** ปลายทั้งสองด้าน (worst case ที่หายากไม่ควรฉุดค่าเฉลี่ยมากเกินไป) — ตัวอย่าง: Payment Flow O = 4 วัน, M = 6 วัน, P = 14 วัน → E = (4 + 24 + 14)/6 = **7 วัน** (ไม่ใช่ (4+6+14)/3 = 8 วัน) — และจด range + assumption ไว้ด้วย (ป้อนให้ risk register ใน Ch.5)

**[Teaching Scenario]** ตัวอย่างคำนวณ CPM จริง (ดัดแปลงจาก Playbook C11.5) — 4 กิจกรรมย่อยของ Payment Integration:

| Activity | Duration (วัน) | Predecessor |
|---|---:|---|
| A API Design | 3 | - |
| B Payment Flow Build | 5 | A |
| C Gateway Contract | 4 | A |
| D Integration Test | 4 | B, C |

Forward Pass: A: ES=0, EF=3 → B: ES=3, EF=8 · C: ES=3, EF=7 → D: ES = max(8,7) = 8, EF=12 — Backward Pass: D: LF=12, LS=8 → B: LF=8, LS=3 · C: LF=8, LS=4 → A: LF = min(3,4) = 3, LS=0 — **Float: A=0, B=0, C=1, D=0** → **Critical Path = A→B→D (12 วัน)** — สรุปเชิงบริหาร: Gateway Contract (C) มี float 1 วัน — ช้าไม่เกิน 1 วันยังไม่กระทบ; แต่ A หรือ B ช้า 1 วัน = launch ล่าช้า 1 วันทันที — นี่คือสิ่งที่ Ch.7 จะใช้ตอน delay เกิดจริง

**[Teaching Scenario]** SHG timeline 8 เดือน (Sprint 0–12): ถ้า Payment Integration (Sprint 3–4) ช้า กระทบ Mobile App (Sprint 5–6) และ Back Office (Sprint 7–8) ตาม dependency — แต่ถ้าล่าช้าอยู่บนเส้นที่มี float ก็อาจไม่กระทบ launch

**Schedule Compression (C11):**
- **Crashing** = เพิ่มทรัพยากรเพื่อย่นเวลา → เพิ่มต้นทุน + coordination risk
- **Fast Tracking** = ทำงานขนาน → เพิ่ม rework + quality risk
- **Split Release / Phased** = แบ่งส่งมอบเป็น wave
- **Rebaseline** = ขออนุมัติเปลี่ยน baseline เมื่อ delay เกิน tolerance

### 4.2 Cost — Estimate, Baseline และ EVM (C12)

**[PMBOK 6]** แยกให้ชัด: Estimate (ประมาณการ) → Budget (วงเงินอนุมัติ) → Cost Baseline (budget แบ่งตามเวลาเพื่อควบคุม) → Contingency Reserve (known-unknowns) → Management Reserve (unknown-unknowns, ต้องขอ Sponsor ก่อนใช้)

**EVM:**
```text
PV = Planned Value (งานที่ควรเสร็จตามแผน)
EV = Earned Value (งานที่เสร็จจริง ตาม evidence)
AC = Actual Cost (เงินที่ใช้จริง)
SV = EV - PV | CV = EV - AC
SPI = EV / PV | CPI = EV / AC
EAC = BAC / CPI (ถ้า trend เดิมต่อ) | VAC = BAC - EAC
```

**[Best Practice]** ตัวเลขต่ำกว่า 1 ไม่ใช่คำตอบสุดท้าย แต่เป็นประตูเข้าสู่คำถาม: variance มาจาก cost/schedule/completion? EV มี acceptance evidence จริงหรือ? เป็น one-time หรือ trend?

**[Best Practice]** อ่านผลเชิงบริหาร: **CPI < 1** = "ด้วยงานที่ทำได้จริง (EV) เราใช้เงินมากกว่าแผน (AC)" → ต้องตอบว่า EAC จะจบที่เท่าไร และต้องตัดสินใจอะไร (ลดงาน / หางบเพิ่ม / เพิ่ม efficiency) — **SPI < 1** = "งานเดินช้ากว่าแผน" → ต้องดู critical path ว่าจุดไหนรับได้ (มี float) จุดไหนรับไม่ได้ — ตัวเลขคือจุดเริ่มต้นของการตัดสินใจ ไม่ใช่จุดจบของการรายงาน

### 4.3 Resource — คน ทักษะ capacity และอำนาจ (C13)

**[PMBOK 6]** แยก Role (บทบาท) / Person (คนจริง) / Assignment (การมอบหมาย) / Capacity (เวลาจริง) — RACI: Responsible (ลงมือ), Accountable (รับผิดชอบผลสุดท้าย — ต้อง 1 คน), Consulted (ให้ input), Informed (รับรู้)

**[Best Practice]** Resource Calendar แสดง availability; Resource Histogram แสดง demand vs capacity — เมื่อเห็น peak/overload เริ่มคุย backfill, vendor support, resequence หรือ scope trade-off ด้วยหลักฐาน

**[Teaching Scenario]** SHG ต้องการ 80 key users (จาก 12 โรงแรม) สำหรับ UAT แต่ finance month-end close ซ้อนกับ UAT wave → ต้อง phased UAT + backfill หรือเลื่อน wave

### 4.4 กล่อง Agile: ถ้าโครงการเป็น Agile (แทรกจาก lesson-15/16)

**[PMBOK 8]** ถ้า delivery เป็น Agile (เช่น ส่วน UX/Booking Journey ของ SHG):
- **Scrum** สำหรับ product increment: Product Backlog (PO จัด priority), Sprint 2–4 สัปดาห์, Sprint Planning, Daily Scrum, Sprint Review, Retrospective — Sprint Goal ปกป้อง focus
- **Kanban** สำหรับ flow/support/incident: Flow Board (To Do/In Progress/Review/Done), WIP Limit, explicit policy — ใช้กับ defect triage, payment incident, support
- **Predictive vs Agile vs Hybrid:** ดู Requirement Stability, Change Cost, Compliance, Feedback Need — **Hybrid** = budget/milestones คุมแบบ predictive แต่ build เป็น sprint (ตรงกับ SHG: 12M + launch 1 พ.ย. คุมแน่น, development เป็น sprint)
- **Agile ไม่ได้แปลว่าไม่มีแผน** — เปลี่ยนจังหวะ planning ให้สั้นลง และต้องมี Definition of Done ที่รวม quality/security/acceptance

**[Best Practice]** Schedule บน Agile ต่างจาก CPM ตรงไหน: CPM วางเส้นทางเดียวล่วงหน้าหมด (เหมาะกับงานที่ dependency ชัดและไม่เปลี่ยนบ่อย เช่น integration ระหว่างระบบ); Scrum/Kanban วางแค่ sprint ถัดไป (plan ระยะสั้น) แล้วปรับจาก velocity/feedback — **เมื่อไรใช้แบบไหน**: ถ้าต้องตอบคำถาม "ขึ้น production วันที่เท่าไร" (deadline แน่นอน) ยังต้องมี milestone + critical path ระดับสูงแม้ใช้ Agile ภายใน — SHG เลยเป็น Hybrid: ล็อก launch ก่อน 1 พ.ย. ด้วย critical path ระดับ high-level แต่ภายใน sprint วางด้วย velocity

> **หมายเหตุ:** Tailoring ลึก ๆ กลับมาอีกครั้งใน Ch.6 (กล่อง Agile) — บทนี้แนะนำหลักการให้เห็นภาพการวางแผน

## 5. PM Decision Thinking

```text
Decision: Schedule delay ควร recover within baseline, เปลี่ยน baseline หรือปรับ scope/release
Owner: PM วิเคราะห์; Sponsor/Steering ตัดสินเมื่อกระทบ milestone หรือ baseline
Inputs: WBS, activity list, dependency, duration, critical path, float, resource availability, cost baseline, risk
Options:
  A: Use float + resequence — ราคาถูกสุด แต่ใช้ได้เมื่อ float จริง
  B: Crashing (เพิ่มคน/โอที) — ย่นเวลาแต่เพิ่ม cost + coordination risk
  C: Fast Tracking (ทำงานขนาน) — เร็วแต่เพิ่ม rework/quality risk
  D: Split Release (wave) — ลด waiting แต่เปลี่ยน user experience
  E: Rebaseline — ยอมรับ delay อย่างเป็นทางการ ต้อง Sponsor อนุมัติ
Trade-offs: speed vs cost, speed vs quality, milestone pressure vs readiness
Risk: recovery ที่ย่นวันแต่เพิ่ม defect -> go-live ยังไม่พร้อมอยู่ดี
Evidence: updated network, recovery brief, approved baseline change (ถ้า rebaseline)
Next Action: เลือก option -> ประเมินผลต่อ cost baseline + resource -> สื่อสาร decision -> Ch.5 (risk/procurement)
```

## 6. ตัวอย่างจริงจาก Case ต่อเนื่อง (SHG)

**[Teaching Scenario] Watch PM Think — สัปดาห์วางแผน baseline**

คุณสุทธิ (PM) ไล่ตรวจ Gantt ที่ทีมวาด: มีแถบสีครบ 12 sprint ตาม Scenario Master แต่เขาถามคำถามเดียวที่ทำให้ทีมเงียบ: "ถ้า Payment Integration ช้า 1 สัปดาห์ กระทบ launch 1 พ.ย. หรือไม่" — ไม่มีใครตอบได้ เพราะไม่มี dependency network และ critical path — เขาสร้าง network ขึ้นมา: critical path ต้องผ่าน Payment Integration → Mobile App → Back Office → UAT → Launch — "Gantt ที่ไม่มี logic คือภาพสวยที่ตอบคำถาม 'ถ้า...แล้ว...' ไม่ได้"

Cost: เขาแยก 12M ออกเป็น Dev 6.0 / Cloud 1.0 / Design 0.8 / PMS Integration 0.5 / Payment Setup 0.2 / QA-Security 0.5 / Contingency 1.5 / Management Reserve 1.5 — "Contingency ใช้ได้ตาม governance แต่ Management Reserve ต้อง Sponsor เท่านั้น" — เพราะสำรองคือกันชน ไม่ใช่เงินที่ใช้ก่อน

Resource: 80 key users สำหรับ UAT — เขาไม่นับว่ามี capacity จนกว่า functional manager เซ็น commitment — "ชื่อในแผน ≠ เวลาจริง — ถ้า month-end ซ้อนกับ UAT wave ต้อง phased หรือ backfill"

**[PMBOK 8]** ตัวอย่าง EVM ระหว่างทาง: ถ้า ณ เดือนที่ 4 PV = 6M, EV = 5M, AC = 6.5M → SPI = 0.83, CPI = 0.77 → ต้องถามต่อ: งานที่ "เสร็จ" มี evidence หรือไม่ สาเหตุคืออะไร และ EAC จะเป็นเท่าไร (รายละเอียดการควบคุมอยู่ Ch.7)

## 7. จุดตัดสินใจและกับดักที่พบบ่อย

**Common Mistakes:**

1. Gantt chart ที่ไม่มี dependency/float/owner — ผล: ดูมั่นใจแต่ตอบคำถาม "ถ้า...แล้ว..." ไม่ได้
2. Effort กับ Duration ปนกัน (8 person-days ≠ 8 วัน) — ผล: schedule ผิดพลาด
3. Estimate โดย PM คนเดียว — ผล: ไม่เห็น skill/capacity gap
4. ใช้ Funding Envelope เป็น Cost Baseline — ผล: ควบคุมเงินผิด (ERP 45M vs 60M บทเรียนเดิม)
5. Resource plan มีชื่อคนครบ แต่ไม่มี capacity sign-off — ผล: UAT ว่างจริงแค่บางช่วง
6. RACI มี Accountable หลายคน — ผล: ไม่มีใครรับผิดชอบจริง
7. ใช้ Contingency/Management Reserve โดยไม่ผ่าน governance — ผล: สำรองหมดก่อนเจอของจริง

**Common Misconceptions:**

| ความเข้าใจผิด | ความจริง |
|---|---|
| ใช้เงินน้อย = ดี | ต้องเทียบกับ EV และ schedule (อาจแค่ทำงานช้า) |
| เพิ่มคนแก้ delay ได้เสมอ | เพิ่ม ramp-up + coordination cost |
| Fast tracking ฟรี | เพิ่ม rework + quality risk |
| ใส่ชื่อคนครบ = มี resource | ต้องมี capacity, skill และ authority |
| Agile ไม่ต้องวางแผน | Agile วางแผนบ่อยและปรับจาก feedback |

## 8. Interview Questions

### Foundational
- **Q:** Critical Path คืออะไร และต่างจาก Milestone อย่างไร?
- **Answer Direction:** CP คือเส้นทางกิจกรรมที่กำหนดระยะเวลาโครงการ (float ต่ำสุด) ส่วน Milestone คือจุดสำคัญที่ไม่มี duration — งานบน CP ช้า = โครงการช้า
- **Warning Signs:** ตอบว่า "เส้นทางที่ยาวที่สุดในตาราง" โดยไม่อธิบาย float/dependency

### Scenario
- **Q:** Payment Integration ช้า 1 สัปดาห์ ก่อน launch 1 พ.ย. คุณจะทำอะไร?
- **Answer Direction:** ไม่สรุปทันที — ดูว่า delay อยู่บน critical path หรือไม่, float ที่เหลือ, downstream dependency (Mobile App, Back Office), แล้วเสนอ options (float, crashing, fast track, split release) พร้อม trade-off ต่อ cost/resource/quality
- **Warning Signs:** ตอบ "เร่งทีม" โดยไม่มี mechanism หรือเลื่อน launch ทันทีโดยไม่วิเคราะห์

### Senior PM
- **Q:** 80 key users ไม่ว่าง UAT เพราะงานประจำ คุณจะจัดการ capacity อย่างไร?
- **Answer Direction:** ดู resource histogram → เสนอ phased UAT ตาม module, backfill, vendor support สำหรับ test prep, หรือเลื่อน wave ที่ชน month-end — capacity commitment ต้องมาจาก functional managers ไม่ใช่ PM สั่งเอง
- **Warning Signs:** ตอบว่า "บังคับให้มา" หรือขอ Steering โดยไม่มีข้อมูล workload

### Executive
- **Q:** CPI = 0.77 หมายความว่าอะไร และคุณจะรายงาน Sponsor อย่างไร?
- **Answer Direction:** อธิบายว่าใช้เงินไปแล้วได้งานกลับมาน้อยกว่าแผน (EV < AC) — ไม่ใช่แค่ "เงินหมด" แต่เป็น performance issue; เสนอ cause analysis + EAC forecast + options; รายงานแยก funding (12M) ออกจาก baseline/reserve
- **Warning Signs:** ปกป้องตัวเลข หรือพูดเฉพาะ AC โดยไม่เชื่อม EV

## 9. PM Dictionary ประจำบท

| Term (EN) | คำอธิบาย (TH) | ความหมายเชิงปฏิบัติ | การใช้ผิดที่พบบ่อย | Term ที่เกี่ยวข้อง |
|---|---|---|---|---|
| Activity List | รายการกิจกรรม | งานจาก work packages ที่ใช้จัดตาราง | สับสนกับ WBS | WBS, Work Package |
| Dependency | ความสัมพันธ์ก่อนหลัง | FS/FF/SS/SF + lead/lag | มองข้าม external dependency | Network Diagram |
| Critical Path | สายงานวิกฤต | เส้นที่กำหนดระยะเวลา project | คิดว่าทุกงานช้า = ล่าช้าเท่ากัน | Float |
| Float / Slack | เวลาสำรอง | เลื่อนได้โดยไม่กระทบ milestone | สับสนกับ Buffer | Critical Path |
| Schedule Baseline | ฐานควบคุมเวลา | ตารางอนุมัติไว้ใช้วัด variance | สับสนกับ Gantt | Control Schedule |
| Crashing | เร่งด้วยทรัพยากร | เพิ่มคน/เงินเพื่อลดเวลา | คิดว่าฟรี | Fast Tracking |
| Fast Tracking | ทำงานขนาน | ซ้อนงาน เพิ่ม rework risk | คิดว่าฟรี | Crashing |
| Cost Baseline | ฐานควบคุมต้นทุน | งบแบ่งตามเวลาเพื่อควบคุม | สับสนกับ Funding | BAC, Budget |
| Contingency Reserve | สำรอง risk ที่รู้ | PM ใช้ตาม governance | สับสนกับ Management Reserve | Management Reserve |
| EVM | Earned Value Management | วัดงานที่เสร็จจริงเป็นเงิน | อ่านแค่ AC | PV, EV, AC, CPI, SPI |
| EAC | Estimate at Completion | forecast ต้นทุนจบงาน = BAC/CPI | คิดว่าเท่ากับ BAC เสมอ | VAC |
| RACI | ตารางบทบาท | Responsible/Accountable/Consulted/Informed | ใส่ A หลายคน | Decision Rights |
| Capacity | กำลังทำงานจริง | เวลาที่ใช้ได้จริง ไม่ใช่ชื่อในแผน | มีชื่อ = มี capacity | Resource Calendar |
| Sprint | รอบส่งมอบ Agile | 2–4 สัปดาห์ มี Sprint Goal | คิดว่า Sprint = deadline ตามใจ | Product Backlog |
| WIP Limit | จำกัดงานค้าง | ป้องกันรับงานเกิน capacity | ยิ่งทำหลายงานยิ่งเร็ว | Kanban |

## 10. Workshop

### Scenario
**[Teaching Scenario]** ทีม SHG เจอว่า PMS Integration (Sprint 7–8) มีความเสี่ยงล่าช้า เพราะ PMS vendor หนึ่งในสามยี่ห้อตอบ API spec ช้า และ finance key users แจ้งว่าไม่ว่าง UAT ช่วงปลายเดือน — พร้อมกันนี้คุณกาญจนา (Revenue) ขอ dashboard เพิ่ม 2 ฟีเจอร์

### Your Role
PM (คุณสุทธิ) ต้องสร้าง recovery + resource decision

### Available Information
- Schedule baseline (Sprint 0–12), งบ 12M (Contingency 1.5M), Resource plan (ทีม 12 + business), Scenario Master risks

### Missing Information
- API spec ของ PMS vendor ยี่ห้อที่ 3 จะมาถึงเมื่อไร, ความเห็นของ QA ว่า fast-track กระทบ test มากแค่ไหน, capacity sign-off จาก functional managers, ราคา/เวลาที่แน่นอนของ dashboard 2 ฟีเจอร์

### Decision Required
- recovery option สำหรับ PMS delay, การจัดการ UAT capacity (phased/backfill), และ dashboard ควรไปไหน (ใน/นอก scope)

### Constraints
- Launch ก่อน 1 พ.ย., งบ 12M (ใช้ contingency ต้องมี evidence + governance), key users มี BAU duties

### Expected Output
- Schedule recovery brief (dependency + critical path + 3 options + trade-off), resource decision (UAT wave plan + owner + authority), decision record สำหรับ dashboard

### Debrief Questions
1. ทำไมต้องรู้ว่า delay อยู่บน critical path ก่อนตัดสินใจ
2. Contingency reserve ใช้ตอนไหน และใครอนุมัติ
3. Resource decision ที่ดีต้องมี evidence อะไรบ้าง

### Evaluation Criteria
- มี mechanism ต่อ recovery (ไม่ใช่ "เร่งทีม"), แยก EVM ถูกต้อง, RACI/capacity มี owner + authority, ตัวเลขไม่ขัด Scenario Master

## 11. Checklist ใช้งานจริง (Planning — Schedule/Cost/Resource / Phase C8–C13)

- [ ] Activity List สร้างจาก Work Packages (ไม่ใช่ WBS ซ้ำ)
- [ ] Dependency Network มี FS/FF/SS/SF + external dependencies
- [ ] Duration estimate แยก effort vs duration และมี basis
- [ ] CPM + Float วิเคราะห์แล้ว — critical path ชัดเจน
- [ ] Schedule Baseline ผ่าน approval
- [ ] Cost Estimate มี basis; Cost Baseline time-phased; reserve แยกชัด
- [ ] EVM setup (PV/EV/AC measurement rules + evidence definition) พร้อม
- [ ] Resource Plan มี capacity sign-off จาก functional managers
- [ ] RACI มี Accountable หนึ่งคนต่อ decision สำคัญ
- [ ] Resource histogram ไม่มี overload ที่ไม่มีการจัดการ
- [ ] Agile inserts: ถ้าใช้ Scrum/Kanban มี backlog owner + DoD + WIP policy
- [ ] ส่งต่อ Ch.5: risks, procurement constraints, communication plan

## 12. Assessment

1. **[Decision Case]** Payment Integration ช้า 1 สัปดาห์ — ให้ข้อมูลที่ต้องรู้ก่อนตัดสินใจ + 3 recovery options พร้อม trade-off ต่อ cost/resource/quality
2. **[Decision Case]** 80 key users ไม่ว่าง UAT ช่วงปลายเดือน — เสนอ resource options และ authority ที่ถูกต้อง
3. **[EVM Case]** ณ เดือนที่ 4: PV = 6M, EV = 5M, AC = 6.5M — คำนวณ SPI/CPI/EAC/VAC และระบุคำถามที่ต้องถามต่อ
4. **[Trade-off Case]** Crashing vs Fast Tracking สำหรับ PMS delay — อธิบาย trade-off และเลือกพร้อมเหตุผล
5. **[Artifact Review]** ตรวจ Gantt chart ที่ไม่มี dependency/owner/estimate basis — ระบุ decision risk
6. **[Artifact Construction]** สร้าง Resource Plan + RACI fragment สำหรับ UAT (SHG) — ระบุ capacity, skill, authority
7. **[Recall]** Effort กับ Duration ต่างกันอย่างไร และทำไม 8 person-days ไม่เท่ากับ 8 วัน

## 13. Executive Summary

| มิติ | สรุป |
|---|---|
| **Why** | Schedule/Cost/Resource คือสามเหลี่ยมที่ทำให้ scope กลายเป็นแผนที่วัดและควบคุมได้ |
| **Decision Improved** | Recovery, cost และ capacity ตัดสินด้วย critical path/EVM/data แทนความรู้สึก |
| **Failure Prevented** | ป้องกัน Gantt หลอก, เงินเกินโดยไม่รู้, และ resource ที่มีชื่อแต่ไม่มี capacity |
| **What to Monitor** | SPI/CPI trend, critical path health, resource histogram, reserve usage |

## 14. เชื่อมไปบทถัดไป + Artifact Handoff

**Bridge:** แผนเวลา/เงิน/คนผ่าน baseline แล้ว — Ch.5 จะเพิ่ม Risk, Procurement, Communications, Environment และรวมเป็น Integrated Plan ก่อน Planning Gate (C14–C19)

| Field | Handoff |
|---|---|
| Input | WBS, Scope Baseline, Acceptance Criteria (Ch.3) |
| Output | Activity List, Dependency Network, Schedule Baseline, Cost Baseline, Resource Plan + RACI |
| Creator | PM + Planner / PM + Finance / PM + Functional Leads |
| Artifact owner | PM (schedule), PM + Finance (cost), PM (resource plan) |
| Reviewer | Functional Leads, Commercial, QA |
| Approval authority | Sponsor / Steering (baseline), Functional Managers (capacity) |
| Minimum acceptance | Usable (ต้องมี baseline + capacity sign-off + EVM rules) |
| Next chapter use | Ch.5 ใช้ baselines + resource ไปวาง Risk, Procurement, Communications และ Environment |

## 15. Quick Reference Card

```text
SCHEDULE/COST/RESOURCE (C8–C13)
------------------------------------------------------------
Schedule:
  WP -> Activity List -> Dependency -> Duration -> CPM/Float -> Baseline
  Delay? ดู critical path + float ก่อน -> use float / crash / fast-track / split / rebaseline
Cost:
  Estimate -> Budget -> Time-phased Baseline -> Contingency/Management Reserve
  EVM: PV/EV/AC -> SV/CV/SPI/CPI -> EAC = BAC/CPI -> VAC = BAC-EAC
Resource:
  Role vs Person vs Assignment vs Capacity
  RACI: A หนึ่งคนต่อ decision | Histogram เจอ overload -> backfill/vendor/resequence
Agile insert:
  Scrum = increment (Sprint Goal + DoD) | Kanban = flow (WIP limit + policy)
  Hybrid = predictive control + sprint build (ตรงกับ SHG)

กฎ 3 ข้อห้าม:
- ห้าม Gantt ที่ไม่มี logic
- ห้ามอ่านเงินโดยไม่ดู EV
- ห้ามมีชื่อคนโดยไม่มี capacity sign-off
```

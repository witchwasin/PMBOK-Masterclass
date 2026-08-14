---
chapter: ch-05
title: "Risk, Procurement, Communications, Environment และ Integrated Plan (Playbook C7 + C14–C19)"
book: "PM Delivery Guide: From Pre-sales to Closure — คู่มือปฏิบัติการบริหารโครงการซอฟต์แวร์ (PMBOK 8th Edition)"
edition: Learner
status: Draft
validation_status: Not Validated
last_reviewed: 2026-08-13
intended_learner_level: Experienced PM
difficulty: Advanced
estimated_study_time: 110
prerequisite:
  - "Ch.4 — Schedule, Cost และ Resource"
related_chapters:
  - "Ch.7 — Monitoring & Change (EVM ฝั่ง Control, Risk Monitor)"
  - "Ch.8 — Verification/UAT (ผลการทดสอบจริง — cross-ref กับ Test Strategy ในบทนี้)"
canonical_source:
  - ../../references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md (Phase C7, C14–C19)
  - ../../e-Book/chapters/lesson-13/lesson-13-learner.md (Risk เต็มบท)
  - ../../e-Book/chapters/lesson-14/lesson-14-learner.md (Procurement เต็มบท)
  - ../../e-Book/chapters/lesson-12/lesson-12-learner.md (Communications เต็มบท)
  - ../../e-Book/chapters/lesson-10/lesson-10-learner.md (Quality — ฝั่ง Plan/Test Strategy)
scenario_version:
  hotel_booking: "1.0"
artifact_outputs:
  - name: Risk Register + Response Plan
    creator: PM + Risk Owners
    artifact_owner: Risk Owners (แต่ละรายการ) / PM (register)
    reviewer: Sponsor, Leads
    approval_authority: Sponsor / Steering (เมื่อเกิน threshold)
    approval_evidence: Approved register + response approval
  - name: Procurement Plan + Vendor Evaluation
    creator: Procurement Manager + PM
    artifact_owner: Procurement Manager
    reviewer: Legal, Finance
    approval_authority: Procurement Authority / Sponsor
    approval_evidence: Approved procurement strategy + contract
  - name: Communication Plan
    creator: PM
    artifact_owner: PM
    reviewer: Sponsor, Stakeholder owners
    approval_authority: Sponsor (plan/cadence)
    approval_evidence: Approved communication matrix
  - name: Quality Plan + Test Strategy (วางแผน)
    creator: QA Lead + BA + PM
    artifact_owner: QA Lead
    reviewer: PO, Business Owner
    approval_authority: Acceptance Authority
    approval_evidence: Approved test strategy
  - name: Integrated PM Plan + Baseline Approval
    creator: PM
    artifact_owner: PM
    reviewer: All plan owners
    approval_authority: Sponsor / CCB (Planning Gate C19)
    approval_evidence: Approved baselines + gate record
---

# Chapter 05 — Risk, Procurement, Communications, Environment และ Planning Gate

## 1. Opening Scenario Hook

**[Teaching Scenario]** ใกล้จบช่วงวางแผน คุณสุทธิ (PM SHG) นั่งรวมแผนย่อยเข้าด้วยกัน: Schedule + Cost + Resource ผ่านแล้ว แต่ยังมีคำถามค้าง: PMS integration มีความเสี่ยงสูง (Scenario Master Risk #1) จะจัดการอย่างไร 2C2P contract เงื่อนไขอะไร ใครต้องรู้เรื่องไหนเป็นรายสัปดาห์ และที่สำคัญ — **Test Strategy ยังไม่ถูกล็อก** ทั้งที่ Ch.8 จะต้องใช้ตรวจรับผลงาน

คุณวีระ (CTO) ถามว่า "เราเตรียม Test Plan ไว้หรือยัง" คุณกาญจนา (Revenue) ถามว่า "รายงานสถานะใครเห็นบ้าง" และคุณสมศรี (VP Ops) ถามว่า "ถ้าระบบล่ม ใครรับผิดชอบ"

**[PMBOK 8]** บทนี้คือ "ปิดจบการวางแผน": วาง Risk, Procurement, Communications, Environment และ Quality/Test Strategy แล้วรวมเป็น Integrated Plan ผ่าน **Planning Gate (C19)** — ผ่านตรงนี้แล้วทีมถึงจะเริ่ม Execution (Ch.6)

## 2. Why It Matters

**[PMBOK 6]** Risk ที่ไม่วางแผน = เจอ issue ตอนช้าเกินไป Procurement ที่ไม่วางแผน = สัญญาที่ไม่รองรับการส่งมอบจริง Communications ที่ไม่วางแผน = ข้อมูลไปผิดคน/ผิดเวลา และ Test Strategy ที่ไม่วางแผน = UAT (Ch.8) เถียงกันว่า "แบบไหนถึงจะผ่าน"

**[Best Practice]** แผนย่อยแต่ละอันดูดีได้คนเดียว แต่ Integrated Plan คือการทำให้เห็นว่า Risk กระทบ Schedule อย่างไร Procurement กระทบ Cost อย่างไร Test Strategy กระทบ Resource อย่างไร — นี่คือหัวใจของ Integration ที่ PM ต้องถือภาพรวม (ต่อจาก Ch.2, กลับมาอีกครั้งใน Ch.7 และจบที่ Ch.10)

## 3. Mental Model

```text
Ch.4 Baselines (schedule/cost/resource)
  -> Risk Planning (C15) — register, response, owner, trigger
  -> Procurement Planning (C16) — make-or-buy, contract type, vendor
  -> Communications Planning (C14) — ใครรู้อะไร เมื่อไร ผ่านช่องทางใด
  -> Quality/Test Strategy (C7) — วางแผนไว้ตรงนี้ ผลจริงอยู่ Ch.8
  -> Environment/Security/Release/Transition (C17) — env, security, cutover เบื้องต้น
  -> Integrated PM Plan (C18) — รวมทุกแผนเป็นหนึ่งเดียว
  -> Planning Gate (C19) — Sponsor/CCB อนุมัติ -> Ch.6 Execution
```

> **Cross-reference (Quality):** **Test Strategy / Quality Plan วางแผนที่นี่ (Ch.5)** — **ผลการทดสอบจริง/UAT Evidence อยู่ Ch.8** อย่าสับสนสองจุดนี้

## 4. Main Lesson

### 4.1 Risk Planning (C15) — จาก lesson-13

**[PMBOK 6]** กระบวนการ Risk: Plan → Identify → Qualitative Analysis → Quantitative (เมื่อจำเป็น) → Plan Responses → Implement → Monitor

**Risk statement ต้องมี Cause + Event + Impact:**
```text
"หาก data cleansing ของ legacy systems ไม่ผ่าน threshold ก่อน migration rehearsal
UAT จะใช้ข้อมูลที่ไม่น่าเชื่อถือ ทำให้ defect เพิ่มและ go-live เสี่ยง"
```

**Risk fields:** ID, Cause, Risk Event, Impact, Probability, Impact Rating, Exposure, Trigger, Owner, Response, Contingency, Residual Risk, Status

**Response strategies:**
- Threat: Avoid > Mitigate > Transfer > Accept (+ Escalate)
- Opportunity: Exploit, Enhance, Share, Accept (+ Escalate)

**[Best Practice]** Accept ≠ ไม่ทำอะไร — Active acceptance มี contingency reserve, trigger และ fallback plan — Risk Owner ควรเป็นคนที่รู้/มีอำนาจต่อ risk นั้น ไม่ใช่ PM เสมอไป

### 4.2 Procurement and Vendor Planning (C16) — จาก lesson-14

**[Best Practice]** เริ่มจาก Need และ Risk ไม่ใช่จาก contract type — Make-or-Buy ต้องมี rationale

| Contract Type | เหมาะกับ | ต้องมี control |
|---|---|---|
| Fixed Price | Scope ชัด, vendor รับ cost risk | Scope ที่ชัดพอ + change control |
| Time and Material | Scope ไม่ชัด, ต้องเรียนรู้ | Rate, Cap, Approval Cadence, Acceptance |
| Hybrid | บางส่วนชัด บางส่วนไม่ชัด | Fixed core + T&M cap สำหรับส่วน discovery |

**[Teaching Scenario]** SHG: 2C2P (transaction fee 2.5% + 7 บาท/txn) — ต้องดูไม่แค่ fee แต่ SLA, security obligation, settlement, incident response, refund process และ integration support; PMS Vendors (T&M ~500K รวม) — ต้องมี cap + acceptance; AWS (pay-as-you-go ~120K/เดือน) — ต้องมี cost forecast + monitoring

### 4.3 Communications Planning (C14) — จาก lesson-12

**[PMBOK 6]** Communication Plan (5W1H): Audience, Information, Purpose, Format, Frequency, Owner, Channel, Escalation, Confidentiality

**3 รูปแบบ:** Push (email/report), Pull (dashboard/wiki), Interactive (meeting/workshop)

**[Best Practice]** แยก **Status Report** (บอกสถานะตามรอบ) ออกจาก **Decision Brief** (ขอ decision พร้อม evidence + deadline) — Dashboard สีแดงไม่ใช่ escalation ถ้าไม่มี decision ask

**[Teaching Scenario]** SHG cadence: Daily Team Sync (dev), Weekly Status (Steering + Stakeholders), Sprint Review (PO/คุณนภา + business), Risk Review (รายสัปดาห์), UAT Defect Review (ช่วง Ch.8), Go-live Command Center (Ch.9)

### 4.4 Quality / Test Strategy Planning (C7) — วางแผนไว้ที่นี่

**[PMBOK 6]** Plan Quality Management: กำหนด Quality Standard, Acceptance Criteria, Test Strategy, Review Approach, Verification vs Validation, Defect Process, Acceptance Authority, Evidence

- **Verification** = สร้างถูกตาม spec (build the product right)
- **Validation** = สร้างสิ่งที่ตอบ need (build the right product)
- **Cost of Quality** = Prevention + Appraisal (ต้นทุนทำให้ถูก) vs Failure (rework, incident, lost trust)
- **Test levels (F.2):** Unit → Component → Integration → System/SIT → Performance → Security → Regression → UAT → Production Verification

**[Teaching Scenario]** SHG Test Strategy ควรระบุ: SIT สำหรับ booking flow + PMS sync, Performance Test (3 วินาที load, 5 วินาที confirmation, uptime 99.5%), Security/Penetration Test (PCI-DSS, PDPA), UAT ด้วย key users 80 คน, Regression ก่อน release — **ผลจริงของทั้งหมดนี้ถูกตรวจและรายงานใน Ch.8**

### 4.5 Environment, Security, Release, Transition Planning (C17)

**[Best Practice]** Environment Plan: Dev/Test/SIT/UAT/Staging/Production/DR — Security: access, auth, encryption, logging, vulnerability, privacy, backup, incident — Transition: data migration, training, cutover, support, rollback (แผนเต็มของ rollout อยู่ Ch.9)

### 4.6 Integrated PM Plan (C18) + Planning Gate (C19)

**[PMBOK 6]** Integrated Plan แสดง Scope/Release, Timeline, Cost, Resource, Quality, Risk, Communication, Procurement, Change, Transition, Governance — ไม่ใช่มองเป็นแผนแยก

**[Best Practice]** **Gate C (Ready for Execution)** ตรวจ: Requirements คุณภาพ, Scope/Release boundary, WBS/Backlog, Acceptance Criteria, Schedule, Resource Commit, Cost Baseline, Risks มี Owner, Client Dependencies, Environment, Change Process, Governance, ทีมเห็นแผนเดียวกัน — ผ่านแล้วถึงเริ่ม Execution

## 5. PM Decision Thinking

```text
Decision: ผ่าน Planning Gate (C19) หรือต้องปิด gap ใดก่อนเริ่ม Execution
Owner: PM นำเสนอ; Sponsor/CCB อนุมัติ baselines + gate
Inputs: integrated plan (ทุก subsidiary plan), risk register, procurement, test strategy, readiness checklist (Playbook §7)
Options:
  A: ผ่าน gate ทันที — ทุกอย่างครบ
  B: ผ่านแบบมีเงื่อนไข (conditional) — ระบุ gap + owner + due date เช่น Test Strategy ยังต้องล็อก UAT data
  C: ไม่ผ่าน กลับไปแก้ — เหมาะเมื่อ baseline อ่อนจน Execution จะสร้างของเสีย
Trade-offs: momentum vs readiness, schedule pressure vs rework cost
Risk: ผ่าน gate ทั้งที่ baseline ไม่พร้อม -> Ch.6–8 เจอ defect/dispute มาก
Evidence: gate review record, approved baselines, open-gap log
Next Action: ถ้าผ่าน -> Kickoff Execution (Ch.6); ถ้าไม่ -> ปิด gap ตาม due date แล้ว review ใหม่
```

## 6. ตัวอย่างจริงจาก Case ต่อเนื่อง (SHG)

**[Teaching Scenario]**

- **Risk Register (ตัวอย่าง 2 รายการ):**
  - R-01: PMS API ไม่พร้อม (High/High) — Mitigate: PoC integration ก่อน Sprint 1, daily data review, wave migration rehearsal — Owner: คุณวีระ (CTO)
  - R-02: Payment Security Breach (Low/Critical) — Avoid: PCI-DSS audit ก่อน launch — Owner: คุณวีระ
- **Procurement:** 2C2P (transaction fee + SLA + incident response), PMS Vendors (T&M cap 500K), AWS (pay-as-you-go + forecast), Design Agency (Fixed 800K)
- **Communications:** Weekly Status ถึง Steering (คุณจิรา, คุณภัทร, คุณวีระ, PM), Sprint Review กับ PO + business, Daily Team Sync ภายในทีม, Risk Review รายสัปดาห์
- **Test Strategy:** SIT + Performance (3s/5s/99.5%) + Security (PCI-DSS/PDPA) + UAT (key users 80) + Regression — ผลจริง → Ch.8
- **Planning Gate:** Sponsor อนุมัติ baselines + เปิดรายการ gap (เช่น test data ยังไม่ครบ) พร้อม due date — ผ่านแบบ conditional

## 7. จุดตัดสินใจและกับดักที่พบบ่อย

**Common Mistakes:**

1. Risk register เขียน "ทีมไม่พร้อม" แบบกว้าง ไม่มี trigger/owner — ผล: monitor ไม่ได้
2. Risk ทำครั้งเดียวตอนวางแผนแล้วเก็บ — ผล: risk กลายเป็น issue โดยไม่รู้ตัว
3. เลือก contract type จากความเคยชิน ไม่ใช่ scope maturity — ผล: dispute/บานปลาย
4. Payment release โดยไม่มี acceptance evidence — ผล: เสียทั้งเงินและอำนาจควบคุม vendor
5. ส่ง report เดียวกันให้ทุกคน — ผล: ไม่มีใครได้สิ่งที่ต้องใช้ตัดสินใจ
6. Test Strategy ไม่ถูกล็อกตอนวางแผน — ผล: Ch.8 เถียงว่า "แบบไหนถึงจะผ่าน"
7. ผ่าน Planning Gate ทั้งที่ baseline ยังอ่อน — ผล: ของเสียถ่ายไป Execution

**Common Misconceptions:**

| ความเข้าใจผิด | ความจริง |
|---|---|
| Risk คือสิ่งไม่ดีเท่านั้น | รวม opportunities (exploit/enhance/share) |
| Risk Owner = PM เสมอ | ควรเป็นคนที่มีความรู้/อำนาจต่อ risk นั้น |
| Accept = ไม่ทำอะไร | Active accept มี reserve + trigger + fallback |
| Procurement Plan = Contract | Plan คือ strategy; contract คือ binding agreement |
| Vendor ทำงานเสร็จ = accept | ต้องมี acceptance evidence |
| Dashboard สีแดง = escalation | Escalation ต้องมี decision ask + response |
| QA รับผิดชอบคุณภาพคนเดียว | คุณภาพเริ่มจาก requirement (Ch.3) และวางแผนที่นี่ |

## 8. Interview Questions

### Foundational
- **Q:** Risk ต่างจาก Issue อย่างไร?
- **Answer Direction:** Risk = เหตุการณ์ยังไม่เกิด (มี trigger, owner, response); Issue = เกิดแล้ว (ต้องแก้/escalate ตอนนี้)
- **Warning Signs:** ใช้คำสลับกัน หรือเรียกทุกอย่างว่า risk เพื่อเลี่ยง escalation

### Scenario
- **Q:** PMS integration risk สูง ก่อนเริ่ม Sprint 1 — คุณจะทำอะไร?
- **Answer Direction:** ระบุ trigger ที่วัดได้ (เช่น API doc ล่าช้าเกิน X วัน, PoC ไม่ผ่าน) → เลือก response (mitigate: PoC ก่อน, vendor support เพิ่ม) → ตั้ง owner (คุณวีระ) → กำหนด review cadence และ escalation path
- **Warning Signs:** เขียน "เราจะระวัง" โดยไม่มี trigger/owner/response

### Senior PM
- **Q:** 2C2P ค่า fee ถูกที่สุดแต่ SLA เรื่อง incident response อ่อนแอ — คุณจะเลือกอย่างไร?
- **Answer Direction:** ดู Total Cost of Ownership + risk: fee ต่ำแต่ถ้า incident กลาง campaign ทำ revenue เสียหาย — นำ SLA/incident requirement ไป negotiation หรือเลือก provider ที่ trade-off ดีกว่า; บันทึก commercial decision record
- **Warning Signs:** เลือกจาก fee อย่างเดียว

### Executive
- **Q:** ทำไมต้องมี Planning Gate ก่อนเริ่ม build?
- **Answer Direction:** Gate = จุดที่ Sponsor ยืนยันว่า baselines + แผนย่อยพร้อมและเห็นตรงกัน — เปลี่ยน "ความตั้งใจ" เป็น "คำมั่น" ที่วัดผลได้; ช่วยหยุดของเสียก่อนเริ่มลงทุน Execution
- **Warning Signs:** ตอบว่า "เป็นขั้นตอน PM" โดยไม่เชื่อมกับ control/risk

## 9. PM Dictionary ประจำบท

| Term (EN) | คำอธิบาย (TH) | ความหมายเชิงปฏิบัติ | การใช้ผิดที่พบบ่อย | Term ที่เกี่ยวข้อง |
|---|---|---|---|---|
| Risk | ความเสี่ยง | เหตุการณ์ไม่แน่นอนที่กระทบ objective | สับสนกับ Issue | Issue, Trigger |
| Issue | ปัญหาที่เกิดแล้ว | ต้องมี owner, action, escalation | สับสนกับ Risk | Risk |
| Trigger | สัญญาณเตือน | เงื่อนไขที่บอกว่า risk ใกล้เกิด/เกิดแล้ว | ไม่กำหนด → monitor ไม่ได้ | Risk Owner |
| Mitigate | ลดความเสี่ยง | ลด probability หรือ impact | คิดว่า = กำจัดได้หมด | Avoid, Transfer |
| Residual Risk | ความเสี่ยงคงเหลือ | risk หลัง response — ต้องมี owner | ลืมว่ายังเหลืออยู่ | Risk |
| Make-or-Buy | ทำเองหรือซื้อ | ตัดสินจาก core, cost, risk, capacity | เลือกจากความเคยชิน | Procurement |
| SOW | ขอบเขตงานตามสัญญา | ผูกพันตาม contract | สับสนกับ Proposal | Contract |
| Fixed Price | ราคาคงที่ | scope ชัด vendor รับ cost risk | ใช้กับ scope ไม่ชัด | T&M |
| T&M | Time and Material | จ่ายตามเวลา/วัสดุ | ไม่มี cap/evidence | Fixed Price |
| Communication Plan | แผนสื่อสาร | ผู้รับ ข้อมูล ความถี่ ช่องทาง owner | ทำครั้งเดียวแล้วเก็บ | Stakeholder |
| Status Report | รายงานสถานะ | บอกสถานะตามรอบ | สับสนกับ Decision Brief | Decision Brief |
| Decision Brief | บันทึกขอตัดสินใจ | decision ask + evidence + deadline | สับสนกับ Status Report | Escalation |
| Test Strategy | แนวทางการทดสอบ | test levels, env, data, entry/exit, defect | คิดว่า = Test Plan รายละเอียด | RTM, UAT |
| Verification | ตรวจตาม spec | build the product right | สับสนกับ Validation | Validation |
| Validation | ตรวจว่าตอบ need | build the right product | สับสนกับ Verification | Verification |
| Planning Gate | ประตูอนุมัติแผน | Sponsor ยืนยันพร้อมเริ่ม Execution | ผ่านทั้งที่ baseline อ่อน | Baseline |

## 10. Workshop

### Scenario
**[Teaching Scenario]** ก่อน Planning Gate ทีม SHG พบว่า: (1) Test Strategy ยังไม่ระบุ UAT data source และ exit criteria, (2) 2C2P ยังไม่ยืนยัน SLA ด้าน incident response, (3) Risk "key users ไม่ว่าง UAT" ยังไม่มี trigger/owner

### Your Role
PM (คุณสุทธิ) ที่ต้องปิด gap ก่อนเสนอ Gate ต่อ Sponsor

### Available Information
- Baselines (schedule/cost/resource จาก Ch.4), Scenario Master risks, draft communication plan

### Missing Information
- UAT data ใครเตรียม (real data จาก PMS?), exit criteria ที่ PO/คุณภัทร จะ accept, SLA ของ 2C2P เรื่อง incident, ตัวเลข trigger สำหรับ key-user availability

### Decision Required
- ผ่าน gate แบบเต็ม, ผ่านแบบ conditional (ระบุ gap + due date), หรือเลื่อน gate — และใครเป็น owner ของแต่ละ gap

### Constraints
- Launch ก่อน 1 พ.ย. (เลื่อน gate = กินเวลา), งบ 12M, ห้ามเริ่ม Execution โดยที่ risk หลักไม่มี owner

### Expected Output
- Gate recommendation (A/B/C + เหตุผล), Gap Log (gap, owner, due date, evidence), Risk Register อัปเดต 3 รายการ, Test Strategy outline หน้าเดียว

### Debrief Questions
1. Conditional approval ต่างจาก "ผ่านเลย" อย่างไร และเมื่อไรถึงสมเหตุสมผล
2. ทำไม Test Strategy ต้องล็อกก่อน Execution ทั้งที่ผลอยู่ Ch.8
3. ถ้า Sponsor เร่งให้ผ่าน gate จะมีหลักฐานอะไรช่วย defend

### Evaluation Criteria
- Gate decision มี evidence + owner + due date, risk มี trigger/owner, test strategy ครบองค์ประกอบ (scope, env, data, entry/exit, authority)

## 11. Checklist ใช้งานจริง (Planning — Risk/Procurement/Comms/Quality/Env / Phase C7, C14–C19)

- [ ] Risk Register ครบ: ทุก risk มี cause/event/impact, trigger, owner, response, residual, review cadence
- [ ] Risk ที่กระทบ baseline มี escalation/change path ชัด
- [ ] Procurement Plan: make-or-buy rationale, contract type ตาม scope maturity, payment ผูก acceptance evidence
- [ ] Vendor evaluation ดู SLA/security/incident ไม่ใช่ราคาอย่างเดียว
- [ ] Communication Plan: audience, info, format, frequency, owner, channel, escalation
- [ ] Status Report ต่างจาก Decision Brief ถูกแยกใช้
- [ ] Quality/Test Strategy วางแผนแล้ว: test levels, env, data, entry/exit, acceptance authority
- [ ] Environment/Security/Release/Transition Plan (C17) มีแล้ว (รายละเอียด rollout → Ch.9)
- [ ] Integrated PM Plan เชื่อมทุก subsidiary plan
- [ ] Planning Gate (C19) ผ่านพร้อม evidence + gap log
- [ ] Cross-ref: ผลทดสอบจริง/acceptance evidence = Ch.8

## 12. Assessment

1. **[Decision Case]** Risk "key users ไม่ว่าง UAT" — เขียน risk statement, trigger, owner, response, residual risk และ escalation path
2. **[Decision Case]** 2C2P เสนอ fee ต่ำแต่ SLA อ่อน — ควรเลือก/negotiate อย่างไร พร้อม commercial decision record
3. **[Trade-off Case]** ระหว่างผ่าน Planning Gate แบบ conditional กับเลื่อน gate 2 สัปดาห์ — อธิบาย trade-off ต่อ launch 1 พ.ย. และให้คำแนะนำ
4. **[Artifact Review]** ตรวจ Risk Register ที่เขียน "ทีมไม่พร้อม", "data อาจมีปัญหา" — แก้เป็น actionable risks
5. **[Executive Communication]** เขียน 1 ย่อหน้าให้ Sponsor ว่า ทำไม Test Strategy ต้องถูกล็อกก่อนเริ่ม build (แม้ผลจะอยู่ Ch.8)
6. **[Cross-Knowledge Analysis]** ถ้า 2C2P ยืนยันว่า settlement ใช้เวลา 2 วันทำการ (ต่างจากที่คาด 1 วัน) — กระทบ requirement (Ch.3), test (Ch.5/Ch.8) และ operating model (Ch.9) อย่างไร
7. **[Recall]** ความต่างระหว่าง Verification กับ Validation (พร้อมตัวอย่างจาก SHG)

## 13. Executive Summary

| มิติ | สรุป |
|---|---|
| **Why** | การวางแผนที่ดีจบที่ Integrated Plan ที่ผ่าน Gate — เปลี่ยนความตั้งใจเป็นคำมั่นที่วัดได้ |
| **Decision Improved** | Risk/procurement/comms/test ตัดสินด้วย evidence + owner + trigger |
| **Failure Prevented** | ป้องกัน risk ไร้เจ้าของ, สัญญาไม่รองรับงานจริง, ข้อมูลไปผิดคน, และ UAT ที่เถียงกันตอนท้าย |
| **What to Monitor** | Gap log ของ conditional approval, risk trigger, vendor SLA compliance, test readiness |

## 14. เชื่อมไปบทถัดไป + Artifact Handoff

**Bridge:** Planning Gate ผ่าน — ทีมมี baselines + integrated plan พร้อม — Ch.6 (Execution) จะลงมือสร้าง deliverables ตามแผน พร้อมบริหารทีม คุณภาพ (ฝั่ง Manage Quality) และจัดการ blocker รายวัน

| Field | Handoff |
|---|---|
| Input | Baselines จาก Ch.4, Scope Baseline (Ch.3), Charter/Governance (Ch.2) |
| Output | Risk Register, Procurement Plan, Communication Plan, Test Strategy, Environment Plan, Integrated PM Plan, Gate Approval |
| Creator | PM + Owners (risk/comms), Procurement Manager (procurement), QA Lead (test strategy) |
| Artifact owner | ตามแผนย่อย (Risk Owners, Procurement Mgr, QA Lead) / PM สำหรับ integrated plan |
| Reviewer | Sponsor, Leads, Legal, Finance |
| Approval authority | Sponsor / CCB (gate + baselines) |
| Minimum acceptance | Usable (ทุกแผนย่อยมี owner + evidence) |
| Next chapter use | Ch.6 ใช้ integrated plan + test strategy + communication plan ไปบริหาร Execution |

## 15. Quick Reference Card

```text
RISK/PROC/COMMS/QUALITY/ENV + GATE (C7, C14–C19)
------------------------------------------------------------
Risk:     cause/event/impact + trigger + owner + response + residual
          Threat: Avoid > Mitigate > Transfer > Accept | Opp: Exploit/Enhance/Share
Procure:  Make-or-Buy -> contract type ตาม scope maturity -> payment ผูก acceptance
Comms:    5W1H + Push/Pull/Interactive | Status Report ≠ Decision Brief
Quality:  Test Strategy วางแผนที่นี่ -> ผลจริง Ch.8 (Ver = ตาม spec, Val = ตาม need)
Env:      Dev/Test/SIT/UAT/Staging/Prod/DR + Security + Transition (rollout = Ch.9)
Gate:     C19 — Sponsor อนุมัติ baselines + gap log ก่อน Execution

กฎ 3 ข้อห้าม:
- ห้าม Risk register ไม่มี trigger/owner
- ห้ามเลือก contract จากความเคยชิน
- ห้ามผ่าน Gate โดย Test Strategy ยังไม่ล็อก
```

---
chapter: ch-02
title: "Initiation — Charter, Stakeholder, Governance และ Kickoff (Playbook B)"
book: "PM Delivery Guide: From Pre-sales to Closure — คู่มือปฏิบัติการบริหารโครงการซอฟต์แวร์ (PMBOK 8th Edition)"
edition: Learner
status: Released
validation_status: Reviewed
last_reviewed: 2026-08-15
intended_learner_level: Beginner PM | Experienced PM
difficulty: Core
estimated_study_time: 90
prerequisite:
  - "Ch.1 — Pre-sales (Opportunity, Proposal, SOW)"
related_chapters:
  - "Ch.7 — Monitoring & Change (Perform Integrated Change Control)"
  - "Ch.10 — Transition & Closure (Close Project or Phase)"
canonical_source:
  - ../../references/PMBOK-Overview.md (PMBOK framework)
  - ../../e-Book/chapters/lesson-05/lesson-05-learner.md (Integration: Develop Charter)
  - ../../e-Book/chapters/lesson-06/lesson-06-learner.md (Stakeholder Management เต็มบท)
scenario_version:
  hotel_booking: "1.0"
scenario_extension: "[Teaching Scenario Extension] — vendor layer สิ้นสุดที่ Ch.2: หลัง Kickoff งานส่งต่อให้ทีมภายใน SHG (คุณสุทธิ PM, คุณนภา PO — roles ตาม Scenario Master) เป็นหลักตั้งแต่ Ch.3"
artifact_outputs:
  - name: Project Charter
    creator: PM (เตรียม) + Sponsor (ออก)
    artifact_owner: Sponsor
    reviewer: PMO, Delivery Owner
    approval_authority: Sponsor
    approval_evidence: Signed charter / authorization record
  - name: Stakeholder Register + Engagement Strategy
    creator: PM + BA
    artifact_owner: PM
    reviewer: Sponsor, Business Owner, Change Lead
    approval_authority: Sponsor / Steering Committee
    approval_evidence: Approved register + engagement action log
  - name: Governance Model + Decision Rights Map
    creator: PM
    artifact_owner: Sponsor
    reviewer: PMO, Legal (ถ้าจำเป็น)
    approval_authority: Sponsor
    approval_evidence: Approved governance charter
  - name: Initial RAID Log
    creator: PM + Leads
    artifact_owner: PM
    reviewer: Sponsor
    approval_authority: PM (ภายใน delegated threshold)
    approval_evidence: RAID review record
---

# Chapter 02 — Initiation: จากสัญญา สู่ "โครงการที่ได้รับอนุญาต"

## 1. Opening Scenario Hook

**[Teaching Scenario Extension]** SOW เซ็นแล้ว SHG อนุมัติงบ Phase 1 จำนวน 12 ล้านบาท และคุณ (PM ของ BTS) ได้รับอีเมลจากคุณจิรา (CEO ของ SHG) ว่า "ฝ่ายเราตั้งคุณสุทธิเป็น PM ประสานงานฝั่งเรา และคุณนภาเป็น Product Owner เริ่มงานได้เลย"

ภายในทีมของคุณ ทุกคนคิดว่างานเริ่มได้ทันทีเพราะ "เซ็นสัญญาแล้ว" แต่คุณรู้ว่ายังขาดอะไรอยู่: ยังไม่มีเอกสารที่ระบุอย่างเป็นทางการว่าใครเป็น Sponsor, PM มีอำนาจแค่ไหน, ใครอนุมัติอะไร, และใครเป็น Stakeholder ที่ต้องดูแล

**[PMBOK 8]** ช่วง Initiation คือการเปลี่ยน "ข้อตกลงทางการค้า" ให้เป็น "โครงการที่ได้รับอนุญาตและมี governance" — ถ้าข้ามขั้นนี้ งานอาจเริ่มเร็ว แต่ทุกการตัดสินใจใหญ่จะกลายเป็นการทะเลาะว่า "ใครมีสิทธิ์ตัดสินใจ"

## 2. Why It Matters

**[PMBOK 6]** Integration Management เริ่มต้นที่นี่ด้วยกระบวนการ **Develop Project Charter** — Charter คือเอกสารที่ Sponsor ออกให้เพื่อให้สิทธิ์ PM อย่างเป็นทางการและกำหนดทิศทางธุรกิจของโครงการ

**[Best Practice]** โครงการที่ไม่มี Charter มักพบปัญหา: PM ไม่มีอำนาจเรียกทรัพยากร, ฝ่ายต่าง ๆ ไม่รู้ว่าโครงการนี้ทำเพื่ออะไร, และทุก escalation ต้องไล่ถามว่า "ใครเป็นคนตัดสินใจ" — นี่คือต้นทุนที่สูงกว่าเวลาที่เสียไปกับการเขียน Charter หนึ่งหน้า

**[PMBOK 6]** Stakeholder Management ก็เริ่มที่ Initiating เช่นกัน: ถ้าระบุ Stakeholder ผิดหรือช้า งาน Ch.3 (Requirements) จะเก็บ requirement ไม่ครบ เพราะไม่รู้ว่าใครเป็นเจ้าของความต้องการจริง

## 3. Mental Model

ลำดับงานของ Phase B:

```text
Internal Handover (B1) — Sales -> Delivery: เอาสิ่งที่รับปากไว้ออกมาทั้งหมด
  -> Project Charter (B2) — Sponsor อนุมัติ: ทำไม ใคร งบเท่าไร อำนาจแค่ไหน
  -> Identify Stakeholders (B3) — ใครมีผล/ได้รับผล
  -> Analyze Stakeholders (B4) — power, interest, influence, impact, attitude
  -> Governance + Decision Rights (B5) — ใครตัดสินใจอะไร ตาม threshold ใด
  -> Initial RAID (B6) — Risks, Assumptions, Issues, Dependencies
  -> Kickoff (B7) — ทุกฝ่ายเห็น objective, scope, roles, decision rights พร้อมกัน
  -> ส่งต่อ Planning (Ch.3)
```

**[PMBOK 8]** หัวใจของบทนี้: Initiation ตอบคำถาม "เรามีสิทธิ์เริ่มและรู้ว่าใครเป็นใครหรือยัง" ก่อนจะลงลึกวางแผน

## 4. Main Lesson

### 4.1 Internal Sales-to-Delivery Handover (B1)

**[Best Practice]** ก่อนเขียน Charter ให้ทำ handover ระหว่าง Sales กับ Delivery: ลูกค้าซื้ออะไร Proposal/SOW เวอร์ชันไหน Sales รับปากอะไรเพิ่ม Estimate ใครทำ Assumptions อะไร Margin เท่าไร Payment milestone ไหน Risks อะไร — ผลลัพธ์คือ Handover Record ที่ทำให้ PM ไม่ต้องไล่ตามความจำของ Sales

### 4.2 Develop Project Charter (B2) — หัวใจของ Integration

**[PMBOK 6]** Charter ควรมี: Project Purpose, Business Need, Measurable Objectives, Success Criteria, High-Level Scope, High-Level Requirements, Major Deliverables, Summary Milestones, Initial Budget, High-Level Risks, Assumptions, Constraints, Sponsor, PM, PM Authority, Governance, Approval Requirements, Exit Criteria และ Charter Approval

**[PMBOK 8]** จำไว้ว่า **Charter ไม่ใช่ Detailed Plan** — เป็นเอกสารระดับสูงที่ให้อำนาจและทิศทาง ไม่ใช่ที่เก็บ schedule รายละเอียด (งานนั้นคือ Ch.4)

**[Teaching Scenario]** ทำไม Charter ถึงเป็น "อำนาจของ PM" ไม่ใช่ "เอกสารพิธีกรรม": ลองภาพ PM ที่เริ่มงานโดยไม่มี Charter — สัปดาห์ที่ 3 ต้องขอข้อมูลจากฝ่ายการตลาด แต่หัวหน้าฝ่ายตอบว่า "โครงการนี้ใครสั่ง ทำไมต้องให้เวลาเรา" — ทุกครั้งที่ขอทรัพยากร/ข้อมูล จะต้องไล่ถามว่าใครอนุมัติ — Charter คือใบที่ Sponsor ออกให้ล่วงหน้าว่า "โครงการนี้มีเจ้าภาพ มีงบ มีทิศทาง และ PM คือคนที่รับผิดชอบ" — เวลาที่เสียไปกับการเขียน Charter หนึ่งหน้าถูกกว่าเวลาที่เสียไปกับการถามว่า "ใครมีสิทธิ์" ไปตลอดทั้งโครงการ

**[Teaching Scenario]** Charter ของ SHG ควรระบุ: Purpose = เพิ่ม Direct Booking จาก 10% เป็น 35% ใน 18 เดือน, Budget = 12 ล้านบาท (Phase 1), Milestone = Launch ก่อน 1 พฤศจิกายน, Sponsor = คุณจิรา (CEO), PM = คุณสุทธิ, PO = คุณนภา, High-Level Risks = PMS API ไม่พร้อม, Payment Security, Conversion ต่ำ

### 4.3 Identify + Analyze Stakeholders (B3–B4) — จาก lesson-06

**[PMBOK 6]** Stakeholder ไม่ได้มีเฉพาะคนที่เข้าประชุม ต้องพิจารณา Sponsor, Customer PO, Decision Maker, End User, Operations, IT, Security, Legal, Finance, Vendor, Regulator, Support, Management และผู้ได้รับผลกระทบทางลบ

Stakeholder Register ที่ดีไม่ใช่ contact list — ต้องมี Role, Interest, Influence, Impact, Attitude, Information Need, Engagement Need, Decision Right, Acceptance Role และ Risk of Resistance

**Power–Interest Grid:**

| Power | Interest | Approach |
|---|---|---|
| High | High | Manage closely |
| High | Low | Keep satisfied |
| Low | High | Keep informed |
| Low | Low | Monitor |

**[Teaching Scenario]** สำหรับ SHG: คุณจิรา (CEO) = High/High → Manage closely, คุณสมศรี (VP Ops) = High/Medium → Keep satisfied, Front Desk Staff = Low/High → Keep informed, ลูกค้า (Guests) = Low/High → Monitor + UX research

### 4.4 Engagement Strategy — current vs desired

**[PMBOK 6]** ระดับ engagement: unaware, resistant, neutral, supportive, leading — ใช้ Engagement Assessment Matrix เทียบ current กับ desired แล้วออกแบบ action ที่มี owner, channel, trigger และ success signal

**[PMBOK 8]** Communication คือการส่งข้อมูลให้เข้าใจตรงกัน ส่วน Engagement คือการออกแบบปฏิสัมพันธ์ให้ decision, adoption และ benefit เกิดขึ้นจริง — สองเรื่องนี้เชื่อมกันแต่ไม่เหมือนกัน (รายละเอียดการสื่อสารอยู่ Ch.5)

### 4.5 Governance และ Decision Rights (B5)

**[Best Practice]** กำหนด Sponsor Decision, Steering Committee, Project Board, PM Authority, PO Authority, Technical Authority, Change Authority, Acceptance Authority, Escalation Path, Decision SLA และ Meeting Cadence — เอกสารนี้คือ "รัฐธรรมนูญ" ของโครงการ ตอนมี conflict จะได้เปิดดูว่าใครตัดสินใจ ไม่ใช่ใครเสียงดังกว่า

### 4.6 Initial RAID (B6)

**[Best Practice]** เปิด RAID Log ตั้งแต่ตอนนี้: Risks, Assumptions, Issues, Dependencies — ทุก record ต้องมี ID, Description, Owner, Date, Impact, Response, Due Date, Status, Escalation

**[Best Practice]** RAID ย่อมาจาก 4 ประเภทที่ต้องแยกดู: **Risk** (ยังไม่เกิด — มี trigger + response), **Assumption** (สมมติฐานที่เรายึด — ต้องทวนเสมอ), **Issue** (เกิดแล้ว — ต้องแก้/escalate), **Dependency** (ต้องพึ่งพาสิ่งนอกทีม/นอกโครงการ) — **ทำไมต้องแยก Assumption ออกมาดู**: เพราะสมมติฐานที่ผิดจะกลายเป็น Risk และถ้าไม่ทวน เราจะไม่รู้ว่ามันผิดตั้งแต่เมื่อไร — ตัวอย่าง SHG: "ทีม recruit ครบใน 2 สัปดาห์" เป็น assumption — ถ้าจริงก็ผ่านไปเฉย ๆ; ถ้าผิด จะกลายเป็น risk "งานเริ่มช้า" ที่ต้องมี owner + response — RAID ที่ดี = ทุก record มี ID, Owner, Due Date และถูก review เป็นประจำ (เริ่มตั้งแต่ Ch.7)

### 4.7 Kickoff (B7)

**[Best Practice]** Kickoff ต้องยืนยัน: Business Objective, Scope/Deliverables, Out of Scope, Timeline/Milestones, Roles, Decision Rights, Communication, Working Approach, Dependencies, Risks, Change Process และ Immediate Actions — จบด้วย MoM + Action Register ที่มี owner และ due date

### 4.8 หมายเหตุ Integration — ถูกผ่าเป็น 3 ท่อน (ไม่ใช่ความผิดพลาด)

**[PMBOK 6]** Integration Management ทำงานตลอดทั้งโครงการ: **Charter → บทนี้ (Ch.2)**, **Perform Integrated Change Control → Ch.7**, **Close Project or Phase → Ch.10** — นี่คือ pattern ปกติของ KA ที่ครอบคลุมทั้ง lifecycle ไม่ใช่การตัดเนื้อหา

## 5. PM Decision Thinking

```text
Decision: ขอบเขตอำนาจของ PM ใน Charter ควรอยู่ระดับใด (และ Stakeholder ใครต้องถูก engage ก่อน Kickoff)
Owner: Sponsor ออก Charter; PM เสนอ draft; Steering Committee เห็นชอบ governance
Inputs: SOW, Handover Record, business need, success criteria, stakeholder signals, org context
Options:
  A: PM Authority กว้าง (ตัดสินใจได้ถึง threshold 1M + เปลี่ยน scope minor ได้) — เร็ว แต่เสี่ยง governance หลุด
  B: PM Authority ปานกลาง (threshold 500K, scope change ต้อง CCB) — สมดุล (default ที่แนะนำ)
  C: PM Authority แคบ (ทุกอย่างต้อง Steering) — ปลอดภัย แต่ช้าและ PM กลายเป็นคนเดินเอกสาร
Trade-offs: decision speed vs control, PM empowerment vs sponsor oversight
Risk of wrong decision: PM ไม่มีอำนาจ -> escalation ท่วม; PM มีอำนาจเกิน -> ตัดสินใจผิดโดยไม่มี check
Evidence: approved charter, decision rights matrix, escalation log, charter approval record
Next Action: เขียน Stakeholder Register + Governance Map -> เรียก Kickoff -> ส่งต่อ Ch.3 (Requirements/Scope)
```

## 6. ตัวอย่างจริงจาก Case ต่อเนื่อง (SHG)

**[Teaching Scenario] Watch PM Think — สัปดาห์ Initiation หลัง Kickoff**

หลัง Kickoff ระหว่าง BTS กับ SHG คุณสุทธิ (PM ฝั่ง SHG) ไล่ตรวจว่า "เรามีสิทธิ์เริ่มจริงหรือยัง": Charter ผ่าน Sponsor (คุณจิรา) — งบ 12 ล้านบาท, launch ก่อน 1 พ.ย., objective = 35% direct booking ใน 18 เดือน — "ถ้าไม่มี Charter นี่ ทุกครั้งที่ขอข้อมูลจากฝ่ายการตลาดจะโดนถามว่า 'ใครสั่ง'"

Stakeholder: เขาไม่ทำ register เป็นแค่ contact list — แต่ประเมิน power/interest ทีละคน: คุณภัทร (High/High → **Manage closely**), คุณสมศรี (High/Medium → **Keep satisfied**), คุณกาญจนา (Medium/High → **Keep informed**), คุณวีระ (High/High → **Manage closely**), 2C2P + PMS vendors (Medium/Medium → **Monitor**), front desk (Low/High → **Keep informed**) — "คนที่มี influence จริงไม่ใช่คนที่เข้าประชุมเสมอไป"

Governance: Steering Committee = คุณจิรา + คุณภัทร + คุณวีระ + PM; Change Authority = CCB (คุณจิรา อนุมัติ baseline change, PM อนุมัติ minor ≤ 500K); Acceptance Authority = คุณนภา (PO) + คุณภัทร สำหรับ UAT sign-off — "ตอนมี conflict จะได้เปิดเอกสารว่าใครตัดสินใจ ไม่ใช่คนที่เสียงดังกว่า"

RAID: R-01 PMS API (High/High), R-02 Payment Security (Low/Critical), **Assumption** = ทีม recruit ครบใน 2 สัปดาห์ ("ถ้าผิด จะกลายเป็น risk ที่ต้องมี owner"), **Dependency** = 2C2P contract + PMS vendor API docs

**[PMBOK 8]** สังเกตว่า Ch.2 จบที่ทุกฝ่าย "เห็นภาพเดียวกัน" — ยังไม่มีการวางแผนรายละเอียด นั่นคืองาน Ch.3–5

## 7. จุดตัดสินใจและกับดักที่พบบ่อย

**Common Mistakes:**

1. เริ่มงานทันทีที่เซ็นสัญญา โดยไม่มี Charter — ผล: PM ไม่มีอำนาจเรียกทรัพยากร
2. ให้ PM เขียน Charter เองแล้ว Sponsor แค่เซ็น — ผล: Sponsor ไม่ได้ ownership ต่อทิศทางโครงการ
3. Stakeholder Register = รายชื่อคนในอีเมล — ผล: พลาดคนที่มี influence จริง
4. ใส่ Accountable หลายคนใน decision — ผล: ไม่มีใครรับผิดชอบสุดท้าย
5. Governance ตั้งแล้วไม่เปิดใช้ — ผล: conflict กลับไปตัดสินด้วยเสียงดัง
6. Kickoff เป็นแค่ presentation ที่ไม่มี action register — ผล: ทุกคนเห็นแต่ไม่มีใครรับผิดชอบ

**Common Misconceptions:**

| ความเข้าใจผิด | ความจริง |
|---|---|
| Charter กับ Project Plan คือสิ่งเดียวกัน | Charter ให้อำนาจและทิศทาง; Plan มีรายละเอียดการบริหาร |
| Stakeholder = คนที่เกี่ยวข้องกับการประชุม | คือใครก็ตามที่มีผลหรือได้รับผลจากโครงการ |
| PM อนุมัติทุกอย่างได้ | Authority ต้องเป็นไปตาม Governance/Decision Rights |
| Sponsor แค่เซ็นเอกสาร | Sponsor ต้องให้ direction, escalation และ visible support |
| Kickoff เสร็จ = Initiation เสร็จ | Initiation จบเมื่อ governance + stakeholder strategy พร้อม |

## 8. Interview Questions

### Foundational
- **Q:** Project Charter ต่างจาก SOW อย่างไร?
- **Answer Direction:** SOW คือขอบเขตงานตามสัญญาจากมุม commercial; Charter คือ authorization ภายในที่ Sponsor ออกให้ PM — ทั้งคู่เป็น input ของกันและกัน
- **Warning Signs:** ตอบว่าเหมือนกัน หรือสลับบทบาท

### Scenario
- **Q:** CFO ของลูกค้าไม่พอใจที่ไม่ได้อยู่ใน Steering Committee และขู่จะชะลอการอนุมัติ คุณจะทำอย่างไร?
- **Answer Direction:** กลับไปที่ Stakeholder Register — ประเมิน power/interest ของ CFO (น่าจะ High/High ด้าน finance) เสนอ Sponsor เพิ่ม CFO ใน governance หรือให้บทบาท Finance representative + decision right ด้านงบ — ไม่ทะเลาะ แต่ปรับโครงสร้าง
- **Warning Signs:** แก้ด้วยการ "เชิญมาประชุมเฉย ๆ" หรือไม่ทำอะไรแล้วรอให้เดือดร้อน

### Senior PM
- **Q:** Sponsor ไม่อยากออก Charter เพราะ "เสียเวลา" คุณจะจัดการอย่างไร?
- **Answer Direction:** อธิบายผลของ decision latency ที่จะเกิด (ทุก escalation ไม่มีเจ้าภาพ) เสนอ Charter ฉบับสั้น 1–2 หน้า และขอ approval ผ่าน session สั้น ๆ — แสดงว่า Charter คือเครื่องมือลดความเสี่ยง ไม่ใช่เอกสารเพิ่มภาระ
- **Warning Signs:** ยอมทำงานโดยไม่มี Charter แล้วมารับความเสี่ยงเองคนเดียว

### Executive
- **Q:** ทำไม PM ต้องมี "อำนาจ" ที่เขียนไว้ใน Charter ไม่ใช่แค่ทำงานตามที่ได้รับมอบหมาย?
- **Answer Direction:** อำนาจที่ชัดเจน = decision speed + accountability; ไม่มีอำนาจ = escalation ทุกรายละเอียด, PM กลายเป็นคนเดินเอกสาร และ decision ถูกเลื่อนจนค่าเสียหายสูง
- **Warning Signs:** ตอบเรื่อง title/ตำแหน่ง แทน decision authority

## 9. PM Dictionary ประจำบท

| Term (EN) | คำอธิบาย (TH) | ความหมายเชิงปฏิบัติ | การใช้ผิดที่พบบ่อย | Term ที่เกี่ยวข้อง |
|---|---|---|---|---|
| Project Charter | เอกสารอนุมัติโครงการ | Sponsor ให้สิทธิ์ PM + กำหนดทิศทาง | สับสนกับ Project Plan | Sponsor, PM Authority |
| Sponsor | ผู้สนับสนุนโครงการ | ให้ทรัพยากร อนุมัติ ตัดสินใจระดับสูง | สับสนกับ Product Owner | Charter, Governance |
| PM Authority | อำนาจของ PM | ขอบเขตตัดสินใจตาม threshold | คิดว่า PM อนุมัติทุกอย่าง | Governance, Decision Rights |
| Governance | กลไกตัดสินใจ/อนุมัติ | ใครตัดสินใจอะไร ตาม threshold ใด | สับสนกับ Meeting | CCB, RACI |
| Decision Rights | สิทธิ์ตัดสินใจ | อำนาจ approve/reject/defer | สับสนกับ Responsibility | Governance |
| Stakeholder Register | ทะเบียน stakeholder | role, interest, influence, needs, strategy | สับสนกับ Contact list | Power-Interest Grid |
| Power-Interest Grid | ตารางอำนาจ/ความสนใจ | เลือกวิธี engage แต่ละ stakeholder | สับสนกับ Org chart | Stakeholder Register |
| Engagement | การมีส่วนร่วม | ระดับการรับรู้/สนับสนุน/มีบทบาท | สับสนกับ Communication | Current vs Desired |
| RAID | Risks, Assumptions, Issues, Dependencies | log กลางที่ต้องมี owner + review | ทำครั้งเดียวแล้วเก็บ | Risk Register, Issue |
| Kickoff | ประชุมเริ่มโครงการ | ทุกฝ่ายเห็น objective/roles/decision rights | เป็นแค่ presentation | Charter, Governance |
| CCB | Change Control Board | อนุมัติ change ที่กระทบ baseline | คิดว่า PM อนุมัติเองได้ทุกเรื่อง | Change Request, Governance |
| Stakeholder Engagement Assessment | การประเมินการมีส่วนร่วม | เทียบ current vs desired engagement | ไม่ทำ และเดาเอา | Engagement, Register |

## 10. Workshop

### Scenario
**[Teaching Scenario]** คุณเพิ่งได้รับแต่งตั้งเป็น PM ฝั่ง SHG (คุณสุทธิ) หลัง Kickoff กับ BTS — Sponsor (คุณจิรา) ต้องการให้เริ่ม Sprint 0 ภายในสัปดาห์หน้า แต่คุณพบว่า Stakeholder Register ยังมีแค่ชื่อคน 4 คน และไม่มี Governance Map

### Your Role
PM ฝั่งลูกค้าที่ต้องทำให้ Initiation สมบูรณ์ก่อน Sprint 0

### Available Information
- Charter ที่ Sponsor เซ็นแล้ว (งบ 12M, launch ก่อน 1 พ.ย.), SOW จาก BTS, รายชื่อทีมใน Scenario Master (PO, dev 12 คน, QA 2, DevOps 1, Hotel Coordinator 1)

### Missing Information
- ความเห็น/attitude ของคุณสมศรี (VP Ops) และ GM 12 โรงแรม, ความต้องการข้อมูลของ 2C2P/PMS vendors, decision threshold ที่ Sponsor อนุมัติ, escalation path สำหรับกรณี PMS API ไม่พร้อม

### Decision Required
- ใครอยู่ใน Steering Committee? threshold ของ PM authority เท่าไร? Stakeholder กลุ่มใดต้องถูก engage ก่อน Sprint 0 เริ่ม?

### Constraints
- ต้องไม่ขัดกับ roles ที่ล็อกใน Scenario Master, ต้องไม่เริ่ม Sprint 0 โดยไม่มี governance, ห้ามแก้ตัวเลขงบ/เวลาที่ล็อกไว้

### Expected Output
- Stakeholder Register + Engagement Strategy (อย่างน้อย 8 stakeholder), Governance Map หนึ่งหน้า (decision rights + escalation), RAID เริ่มต้น 5 รายการ, Kickoff agenda ที่เหลือ

### Debrief Questions
1. Stakeholder กลุ่มไหนที่ถูกมองข้ามง่ายที่สุดในโครงการนี้ และผลคืออะไร
2. ถ้า PM ไม่มี threshold ชัดเจน จะเกิดอะไรตอน Ch.7 (Change Control)
3. Governance ที่ "ตั้งแล้วไม่ใช้" ต่างจากที่ "ใช้จริง" อย่างไร

### Evaluation Criteria
- Register มี influence/engagement/owner ไม่ใช่แค่ชื่อ, Governance มี decision rights + escalation, RAID มี owner ทุกรายการ, การตัดสินใจไม่ขัดกับ Scenario Master

## 11. Checklist ใช้งานจริง (Initiation / Phase B)

- [ ] Internal Handover Record ทำแล้ว (Proposal/SOW version, สิ่งที่ Sales รับปาก, assumptions)
- [ ] Charter ผ่าน Sponsor อนุมัติแล้ว (purpose, objectives, budget, milestones, PM authority, exit criteria)
- [ ] Stakeholder Register มี ≥ 8 รายการ พร้อม power/interest/current/desired/owner
- [ ] Governance Map อนุมัติแล้ว (Steering, CCB, PM/PO/Technical/Acceptance authority, escalation path)
- [ ] Initial RAID เปิดแล้ว ทุก record มี owner + due date
- [ ] Kickoff จบด้วย MoM + Action Register (owner + due date ทุก action)
- [ ] ส่งต่อ Ch.3: Stakeholder needs, decision rights, acceptance roles พร้อมใช้เก็บ requirements

## 12. Assessment

1. **[Decision Case]** Sponsor ขอให้ PM "จัดการทุกอย่างเอง" โดยไม่กำหนด threshold ใน Charter — คุณจะแนะนำอย่างไร และจะเกิดความเสี่ยงอะไรถ้า PM มีอำนาจไม่จำกัด?
2. **[Decision Case]** Stakeholder Register มีแค่ 4 คน (CEO, CTO, PO, PM) ก่อน Kickoff — ระบุกลุ่มที่ขาดและเหตุผลที่ต้อง engage ก่อน Sprint 0
3. **[Trade-off Case]** ระหว่าง PM authority กว้างกับแคบ — อธิบาย trade-off ด้าน decision speed vs control พร้อมข้อเสนอ threshold สำหรับโครงการ 12 ล้านบาทนี้
4. **[Artifact Review]** ตรวจ Charter ที่มี "PM เขียนเอง Sponsor แค่เซ็น" และไม่มี exit criteria — อธิบายว่า governance จะพังตรงไหนเมื่อเกิด conflict
5. **[Executive Communication]** เขียน 1 ย่อหน้าให้คุณจิรา (CEO) ว่า ทำไมต้องมี Steering Committee และ PM threshold ที่ชัดเจน ก่อน Sprint 0
6. **[Cross-Knowledge Analysis]** ถ้า CFO ของ SHG ต้องการเป็นผู้ตัดสินใจเรื่องงบทุกครั้ง (แม้ minor) — สิ่งนี้จะกระทบ Ch.4 (Cost) และ Ch.7 (Change) อย่างไร และคุณจะปรับ governance อย่างไร
7. **[Recall]** ความแตกต่างระหว่าง Stakeholder Register กับ Power-Interest Grid คืออะไร

## 13. Executive Summary

| มิติ | สรุป |
|---|---|
| **Why** | Initiation ล็อก "ใครมีอำนาจทำอะไร" ก่อนงานเริ่ม — ความชัดเจนตรงนี้ลดความขัดแย้งตลอดทั้งโครงการ |
| **Decision Improved** | การอนุมัติ, escalation และ change decision มีเจ้าภาพชัดเจนตาม Governance |
| **Failure Prevented** | ป้องกัน PM ไร้อำนาจ, Stakeholder พลาด, และ governance ที่ไม่มีใครใช้ |
| **What to Monitor** | Stakeholder engagement shift, RAID ที่มี owner, และการใช้ decision rights จริง |

## 14. เชื่อมไปบทถัดไป + Artifact Handoff

**Bridge:** Initiation จบเมื่อมี authorization + governance + stakeholder strategy — Ch.3 จะใช้ Stakeholder needs และ decision rights เหล่านี้ไปเก็บ Requirements, กำหนด Scope และสร้าง WBS

| Field | Handoff |
|---|---|
| Input | SOW, Handover Record, Business Need (จาก Ch.1) |
| Output | Approved Charter, Stakeholder Register + Engagement Strategy, Governance Map, Initial RAID |
| Creator | PM + BA (Stakeholder), Sponsor (Charter/Governance) |
| Artifact owner | Sponsor (Charter/Governance), PM (Register/RAID) |
| Reviewer | PMO, Business Owner, Change Lead, Functional Leads |
| Approval authority | Sponsor / Steering Committee |
| Minimum acceptance | Usable (ต้องมี decision rights + engagement owner) |
| Next chapter use | Ch.3 ใช้ stakeholder needs, decision rights และ acceptance roles เพื่อเก็บ requirements และ approve scope baseline |

## 15. Quick Reference Card

```text
INITIATION (B) — เป้าหมาย: Authorization + Governance + Stakeholder ชัด
------------------------------------------------------------
1. Internal Handover  -> สิ่งที่ Sales รับปากทั้งหมด ออกมาจากความจำ
2. Charter            -> Sponsor อนุมัติ: ทำไม ใคร งบ เป้า อำนาจ PM
3. Stakeholder Reg.   -> role, interest, influence, impact, attitude
4. Power-Interest     -> Manage closely / Keep satisfied / Keep informed / Monitor
5. Engagement         -> current vs desired + owner + trigger + success signal
6. Governance         -> Steering, CCB, PM/PO/Tech/Acceptance authority, escalation
7. Initial RAID       -> ทุก record มี ID, Owner, Due date, Escalation
8. Kickoff            -> objective, scope, roles, decision rights + MoM/Actions

กฎ 3 ข้อห้าม:
- ห้ามเริ่มงานโดยไม่มี Charter (PM ไร้อำนาจ)
- ห้าม Stakeholder Register = contact list
- ห้าม Governance ตั้งแล้วไม่ใช้

Integration note: Charter = บทนี้, Change Control = Ch.7, Closure = Ch.10
```

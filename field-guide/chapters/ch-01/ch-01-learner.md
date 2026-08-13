---
chapter: ch-01
title: "Pre-sales — จาก Opportunity ถึง Proposal/SOW (Playbook A)"
book: "PM Delivery Guide: From Pre-sales to Closure — คู่มือปฏิบัติการบริหารโครงการซอฟต์แวร์ (PMBOK 8th Edition)"
edition: Learner
status: Draft
validation_status: Not Validated
last_reviewed: 2026-08-13
intended_learner_level: Beginner PM | Experienced PM
difficulty: Core
estimated_study_time: 90
prerequisite:
  - "Ch.0 — PMBOK Primer (ภาพรวม Principles/Domains/Focus Areas)"
related_chapters:
  - "Ch.2 — Initiation (Charter, Stakeholder, Governance)"
canonical_source:
  - ../../references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md (Phase A)
  - ../../e-Book/chapters/lesson-05/lesson-05-learner.md (บางส่วน: Business Case / Value)
scenario_version:
  hotel_booking: "1.0"
scenario_extension: "[Teaching Scenario Extension] — vendor layer สำหรับ Ch.1–2: บริษัท Booking Tech Solutions (BTS) รับงานจาก Siri Hospitality Group (SHG) — ตัวเลข/roles ทั้งหมดของ SHG อ้างอิง scenarios/HOTEL-BOOKING-PLATFORM-CASE.md v1.0 ตามเดิม ไม่มีการแก้ baseline"
artifact_outputs:
  - name: Opportunity Brief
    creator: Sales + PM
    artifact_owner: Opportunity Owner
    reviewer: Pre-sales PM
    approval_authority: CEO / Sales Director
    approval_evidence: Bid/No-Bid decision record
  - name: ROM Estimate
    creator: Functional Leads
    artifact_owner: Delivery Owner
    reviewer: PM + Architect
    approval_authority: Commercial Owner
    approval_evidence: Estimate basis + assumptions + confidence level
  - name: Proposal (กับ SOW)
    creator: PM + Sales
    artifact_owner: Proposal Owner
    reviewer: Legal, Finance, Delivery
    approval_authority: CEO / Authorized Signatory
    approval_evidence: Approved proposal + signed SOW/contract
---

# Chapter 01 — Pre-sales: จาก Opportunity ถึง Proposal/SOW

## 1. Opening Scenario Hook

**[Teaching Scenario Extension]** วันจันทร์เช้า Sales ของบริษัท Booking Tech Solutions (BTS) ซึ่งเป็นบริษัทรับพัฒนาระบบดิจิทัล ส่ง RFP (Request for Proposal) ฉบับหนึ่งมาให้คุณซึ่งเป็น Pre-sales PM:

> Siri Hospitality Group (SHG) เครือโรงแรม 12 แห่ง มีห้องพักรวม ~2,400 ห้อง ขายห้องผ่าน OTA (Agoda, Booking.com) ถึง 70% เสีย Commission 15–25% ไม่มีฐานข้อมูลลูกค้าของตัวเอง ต้องการสร้าง Direct Booking Platform (Website + Mobile App) ให้สัดส่วน Direct Booking เพิ่มจาก 10% เป็น 35% ภายใน 18 เดือนหลัง Launch — งบ Phase 1 อยู่ที่ 12 ล้านบาท ต้องการ Launch ก่อน High Season (1 พฤศจิกายน) และขอใบเสนอราคาภายใน 3 สัปดาห์

ภายในห้องประชุมแรก Sales พูดว่า "โจทย์ชัด 12 ล้านบาท เราน่าจะเสนอ 9 ล้าน รับงานมาเถอะ" ส่วนคุณในฐานะ PM รู้สึกว่ายังมีคำถามอีกมาก: โรงแรม 12 แห่งใช้ PMS ต่างยี่ห้อกันหมดหรือไม่ ข้อมูลห้องว่างซิงก์แบบไหน OTA commission ที่ว่าคือตัวเลขจริงหรือไม่ และทีมเรามี capacity พอส่งมอบภายใน 8 เดือนหรือไม่

คำถามของบทนี้คือ: **"รับงาน" ควรถูกตัดสินใจจากอะไร — ราคาเร็ว ๆ หรือหลักฐานที่พอจะประเมิน risk และ value ได้จริง**

## 2. Why It Matters

**[PMBOK 8]** ช่วง Pre-sales ยังไม่ใช่โครงการที่ได้รับ Authorization แต่เป็นจุดที่โครงการถูกกำหนดชะตากรรมไว้ล่วงหน้า ถ้าตรงนี้พลาด โครงการที่ตามมาจะแบกสัญญาที่ผิดพลาดไปทั้งอายุขัย

**[Best Practice]** ถ้า Proposal ไม่มี Out of Scope, ไม่ระบุ Assumption, ประเมินจากคำบอกเล่าครั้งแรก หรือ Sales รับปาก feature นอกเอกสาร ความขัดแย้งจะย้ายไปเกิดที่กลางโครงการ ตอนที่ทีมส่งมอบแล้ว แต่ลูกค้ายืนยันว่างานไม่ตรงกับที่ "ตกลงกัน" ไว้

**[PMBOK 8]** แนวคิดที่ควรยึดคือ Value Delivery: ก่อนเขียน Proposal ทีมต้องเข้าใจ Business Need, Desired Outcome และ Success Measures ของลูกค้าให้ได้ก่อน เพราะ Proposal ที่ดีคือเอกสารที่แสดงว่าบริษัทเข้าใจปัญหา ไม่ใช่แค่รายการฟีเจอร์พร้อมราคา

## 3. Mental Model

จาก Playbook V2 Phase A flow:

```text
Opportunity Intake
  -> Initial Discovery (ปัญหาคืออะไร เกิดกับใคร ผลกระทบเท่าไร)
  -> As-Is / Root Cause (ทำไมถึงเป็นแบบนี้)
  -> Desired Outcome + Success Measures (วัดอะไรว่าแก้สำเร็จ)
  -> Solution Shaping (ทางเลือก ไม่ใช่ทางเดียว)
  -> ROM Estimate (ขอบเขต + สมมติฐาน + ช่วงราคา + confidence)
  -> Internal Review (feasibility + margin + risk)
  -> Proposal (มี In/Out of Scope ชัดเจน)
  -> Negotiation (Impact analysis ก่อนยอมเปลี่ยน)
  -> SOW / Contract (ผูกพันตามเอกสารที่ approve แล้ว)
  -> Bid / No-Bid Decision
```

**[PMBOK 8]** จุดเน้นของบทนี้: อย่าข้าม Discovery แล้วตรงไปเขียน Proposal เพราะ Proposal ที่ไม่มี basis คือการพนันด้วยเงินของบริษัท

## 4. Main Lesson

### 4.1 Opportunity Intake — อย่าถามแค่ว่า "งบเท่าไร"

**[PMBOK 8]** ทุก Opportunity ต้องถูกบันทึกเป็น Opportunity Brief อย่างน้อยต้องตอบ: ลูกค้าคือใคร ใครเป็นผู้ขอ ปัญหาที่เล่ามาเบื้องต้น Deadline และงบประมาณที่เปิดเผย Decision Maker และเหตุผลที่ต้องทำตอนนี้

**[Teaching Scenario Extension]** ในกรณี SHG: Opportunity Brief ของ BTS ควรบันทึกว่า SHG มี 12 โรงแรม, OTA 70%, commission 15–25%, งบ Phase 1 = 12 ล้านบาท, deadline proposal 3 สัปดาห์, decision maker คือ คุณจิรา (CEO) และ Business Owner คือ คุณภัทร (VP Marketing) — ตัวเลขทั้งหมดตรงกับ Scenario Master

### 4.2 Initial Discovery — คำถาม 10 ข้อขั้นต่ำ

**[PMBOK 8]** Discovery คือการเก็บ fact ก่อนออกความเห็น ใช้คำถามขั้นต่ำ 10 ข้อจาก Playbook V2 §A2: ปัญหาปัจจุบันคืออะไร เกิดกับใคร เกิดบ่อยแค่ไหน ผลกระทบคืออะไร ทำไมต้องแก้ตอนนี้ ถ้าไม่ทำจะเกิดอะไร Outcome ที่ต้องการคืออะไร Success วัดอย่างไร มีข้อจำกัดอะไร และใครมีอำนาจตัดสินใจ

**[Best Practice]** ระหว่าง Discovery ให้จับ As-Is Process (trigger, actor, step, data, decision, system, waiting, error, rework, pain, impact) แล้วทำ Root Cause Analysis แยก symptom / immediate cause / root cause — อย่ารีบแปลง pain point เป็น software feature ทันที

### 4.3 Desired Outcome และ Success Measures

**[PMBOK 8]** Outcome ต้องวัดได้มากกว่า "มีระบบจอง" เช่น ลด Double Booking, ลด Average Response Time, เพิ่ม Booking Completion Rate หรือลด Manual Reconciliation

**[Teaching Scenario Extension]** สำหรับ SHG Outcome ที่ล็อกใน Scenario Master คือ: Direct Booking จาก 10% → 35% ภายใน 18 เดือน, ลด OTA Commission ≥ 3 ล้านบาท/ปี, Customer Database ≥ 10,000 profiles ใน 12 เดือน, Booking NPS ≥ 40 — Proposal ของ BTS ต้องอ้างอิงตัวเลขเหล่านี้ ไม่ใช่ตั้ง KPI ขึ้นใหม่

### 4.4 Solution Options — อย่าสมมติว่า Solution ต้องเป็น Custom Software

**[Best Practice]** ทางเลือกอาจเป็น Process Improvement, Training, SaaS, Customize Existing System, Integration, Custom Development, Phased Hybrid หรือ Paid Discovery/POC — แต่ละ Option ต้องระบุ Business Value, Included Capabilities, Exclusions, Assumptions, Dependencies, Risks, Estimated Timeline, Cost Range และ Confidence Level

### 4.5 ROM Estimate — ประมาณการเพื่อตัดสินใจ ไม่ใช่ Commitment

**[Best Practice]** ROM (Rough Order of Magnitude) ต้องมี Scope Basis, Assumptions, Team Model, Duration Range, Cost Range, Confidence, Major Unknowns, Contingency Logic และ Expiration/Validity — อย่าปล่อยให้ตัวเลขเดียวถูกส่งให้ลูกค้าโดยไม่มีช่วงและสมมติฐาน

### 4.6 Internal Review ก่อนส่ง Proposal

**[Best Practice]** ตรวจ Business fit, Technical feasibility, Delivery feasibility, Operational feasibility, Commercial feasibility, Security/Compliance, Contract risk, Resource availability และ Margin — ถ้าตรวจพบว่า Delivery Team ไม่มี capacity หรือ PMS integration มีความเสี่ยงสูง ต้องกลับไปปรับ Proposal หรือตัดสินใจ No-Bid

### 4.7 Proposal — 19 องค์ประกอบ

**[Best Practice]** Proposal ที่ดีควรมี Executive Summary, Business Understanding, Problem and Desired Outcome, Proposed Solution, Scope and Deliverables, In Scope/Out of Scope, Delivery Approach, High-Level Timeline, Team Structure, Pricing, Assumptions, Dependencies, Client Responsibilities, Acceptance Approach, Payment Milestones, Change Approach, Warranty/Support, Proposal Validity และ Next Steps

**[PMBOK 6]** ที่นี่เองที่ Business Case และ Value ส่วนต้นของ Integration ถูกใช้: Proposal คือสะพานจาก Business Need ไปสู่ Project Charter ใน Ch.2

### 4.8 Negotiation — ทุกการลดราคา/เร่งเวลา/เพิ่ม scope ต้องมี Impact Analysis

**[Best Practice]** หลัก Trade-off:
```text
เพิ่ม Scope -> ต้องเพิ่มเวลา งบ คน หรือลด Scope อื่น
ลดเวลา   -> ต้องเพิ่มทรัพยากร ลด Scope หรือเพิ่ม Risk
ลดงบ     -> ต้องลด Scope เปลี่ยน Approach หรือยอมรับ Constraint
```

### 4.9 SOW / Contract — ขอบเขตที่ผูกพัน

**[Best Practice]** SOW ควรมี Deliverables, Scope, Milestones, Acceptance Criteria/Process, Responsibilities, Dependencies, Payment Terms, Change Control, Warranty, Support, IP, Confidentiality, Liability, Termination, Assumptions และ Exclusions

**[PMBOK 8]** จำไว้ว่า Proposal กับ SOW ต้องไม่ขัดกัน — ถ้า Proposal บอกว่ามี Out of Scope แต่ SOW กลับรวมงานนั้นไว้ ความขัดแย้งจะกลับมาหา PM ในภายหลัง

### 4.10 Bid / No-Bid — การตัดสินใจที่คนส่วนใหญ่ข้าม

**[Best Practice]** ควรประเมิน: ปัญหาของลูกค้ามี Business Value เพียงพอหรือไม่ บริษัทมี Capability/Capacity ส่งมอบหรือไม่ Scope/Timeline/Budget ระดับ Proposal มี Basis พอหรือไม่ มี Commercial/Delivery Risk ใดที่ต้องรู้ก่อนเสนอราคา และควร Bid, No-Bid, Partner หรือเสนอ Discovery Phase แบบเสียเงินก่อน

## 5. PM Decision Thinking

```text
Decision: BTS ควร Bid หรือ No-Bid ใน RFP ของ SHG (และถ้า Bid จะเสนอราคา/ขอบเขตแบบใด)
Owner: Opportunity Owner (CEO/Sales Director) ตัดสินใจสุดท้าย; Pre-sales PM จัดเตรียม evidence
Inputs: Opportunity Brief, Discovery Summary, Solution Options, ROM, capacity check, margin, risk register เริ่มต้น
Options:
  A: Bid แบบ Fixed Price เต็ม Phase 1 (dev + QA) — margin ชัดแต่รับ delivery risk เอง
  B: Bid แบบ Hybrid (Fixed core + T&M สำหรับ PMS integration ที่ไม่ชัด) — ลด risk ฝั่ง vendor
  C: No-Bid / เสนอ Paid Discovery Phase ก่อน — ปลอดภัยสุด แต่เสี่ยงเสีย opportunity
Trade-offs: margin vs delivery risk, ความเร็วในการตอบ vs ความแม่นยำของ Proposal, โอกาสทางธุรกิจ vs ชื่อเสียงเมื่อส่งมอบไม่ได้
Risk of wrong decision: รับงานแล้วเจอ PMS integration ต่างยี่ห้อ 12 แบบ -> scope ระเบิด -> โดนหนี margin
Evidence: bid/no-bid decision record, ROM basis + assumptions, capacity confirmation, initial risk register
Next Action: ถ้า Bid -> เขียน Proposal ครบ 19 องค์ประกอบ -> Internal review -> ส่งลูกค้า -> เตรียม negotiation position
```

## 6. ตัวอย่างจริงจาก Case ต่อเนื่อง (SHG x BTS)

**[Teaching Scenario Extension]** สมมติว่าหลัง Discovery ทีม BTS พบ:

- PMS ของ 12 โรงแรมมียี่ห้อต่างกัน 3 ยี่ห้อหลัก มี API ไม่ครบทุกโรงแรม ต้องทำ Adapter แยก (ตรงกับ Risk #1 ใน Scenario Master: "PMS Integration ล่าช้าเพราะ API ไม่พร้อม")
- งบ 12 ล้านบาทของ SHG แบ่งเป็น Dev Team 6.0, Cloud 1.0, Design 0.8, PMS Integration 0.5, Payment Setup 0.2, QA/Security 0.5, Contingency 1.5, Management Reserve 1.5
- BTS จึงเสนอ **Option B (Hybrid)**: Fixed Price 6.5 ล้านบาทสำหรับ Development + QA/Security (ตรงกับสองแถวแรก) และ T&M แบบมี cap 0.5 ล้านบาทสำหรับ PMS Adapter ที่ scope ยังไม่ชัด — โดย Cloud, Design Agency และ Payment ยังคงเป็นค่าใช้จ่ายที่ SHG จัดการเอง เพื่อให้รวมแล้วไม่เกินกรอบ 12 ล้านบาท

**[Best Practice]** ตัวอย่างนี้แสดงว่า Proposal ที่ดีไม่ใช่แค่เลขเดียว แต่คือการจัดสรรความเสี่ยง (risk allocation) ระหว่าง vendor กับลูกค้าอย่างโปร่งใส — ตรงกับหลัก "เลือก contract type จาก scope maturity และ risk" ที่จะเรียนลึกใน Ch.5

## 7. จุดตัดสินใจและกับดักที่พบบ่อย

**Common Mistakes (จาก Playbook V2 §A.11):**

1. รับปากราคาและเวลาจากคำบอกเล่าครั้งแรก — ผล: ขาด basis ในการ defend เมื่อ scope เปลี่ยน
2. Estimate โดย PM คนเดียว — ผล: ไม่เห็น skill/capacity gap จริงของทีม
3. ใช้ Prototype เป็น Commitment — ผล: ลูกค้าเข้าใจว่า prototype = ฟีเจอร์ที่รับประกัน
4. Proposal ไม่มี Out of Scope — ผล: งานทุกอย่างกลายเป็น "ใน scope" โดยปริยาย
5. Timeline ไม่รวมเวลารอลูกค้า — ผล: แผนสวยแต่ใช้จริงไม่ได้
6. Proposal กับ SOW ขัดกัน — ผล: dispute ตอนส่งมอบและจ่ายเงิน
7. Sales รับปาก Requirement นอกเอกสาร — ผล: PM ต้องแบกสัญญาที่ตัวเองไม่เคยเห็น
8. ไม่ระบุ Confidence ของ Estimate — ผล: ROM ถูกอ่านเป็นราคาผูกพัน
9. ไม่ตรวจ Team Capacity — ผล: รับงานมาแล้วไม่มีคนทำ

**Common Misconceptions:**

| ความเข้าใจผิด | ความจริง |
|---|---|
| Pre-sales ไม่ใช่งาน PM | PM ที่เข้ามาช่วงนี้ช่วยล็อก scope, risk และ basis ของสัญญา |
| ROM คือราคาที่ลูกค้าจะจ่าย | ROM คือช่วงประมาณการเพื่อตัดสินใจ ไม่ใช่ commitment |
| ลูกค้ารู้ว่าตัวเองต้องการอะไร | Discovery ต้องพิสูจน์ — หลายครั้ง pain ≠ solution |
| Bid ทุกใบเพื่อไม่เสียโอกาส | No-Bid ที่มีเหตุผลช่วยปกป้อง margin และชื่อเสียง |
| Proposal ยิ่งหน้ายิ่งดี | Proposal ต้องทำให้ decision maker เห็น value + risk ได้ในหน้าครึ่ง |

## 8. Interview Questions

### Foundational
- **Q:** อะไรคือความแตกต่างระหว่าง Proposal กับ SOW?
- **Answer Direction:** Proposal คือข้อเสนอ (มี executive summary, scope, timeline, price, assumptions) ส่วน SOW คือขอบเขตงานที่ผูกพันตามสัญญา ต้องไม่ขัดกัน
- **Warning Signs:** ตอบว่าเป็นเอกสารเดียวกัน หรือสลับบทบาทกัน

### Scenario
- **Q:** ลูกค้าบอกว่ามีงบ 12 ล้านบาทและอยากได้ใบเสนอราคาภายในสัปดาห์หน้า คุณจะทำอย่างไร?
- **Answer Direction:** ไม่รีบตั้งราคา — เก็บ Opportunity Brief, Discovery ขั้นต่ำ, ตรวจ capacity, หา major unknowns แล้วเสนอ ROM พร้อม confidence และข้อเสนอเรื่อง Paid Discovery ถ้าข้อมูลไม่พอ
- **Warning Signs:** เสนอราคาทันทีโดยไม่มีคำถาม หรือไม่มี In/Out of Scope

### Senior PM
- **Q:** Sales รับปาก feature กับลูกค้าแล้วโดยไม่ผ่านคุณ คุณจะจัดการอย่างไร?
- **Answer Direction:** นำ feature เข้า impact analysis อย่างเป็นทางการ แจ้งผลต่อ scope/timeline/price ให้ Sales และลูกค้าเห็น trade-off ก่อนเซ็น — บันทึกทุกอย่างลง proposal/decision record
- **Warning Signs:** เงียบแล้วแบกงานเพิ่ม หรือทะเลาะกับ Sales โดยไม่สร้างทางเลือก

### Executive
- **Q:** ทำไมเราถึงควร No-Bid บน RFP ที่ดูมีโอกาสดี?
- **Answer Direction:** อ้าง evidence: delivery risk สูง (เช่น PMS API ไม่พร้อม), margin ไม่พอ, capacity ไม่มี, หรือ compliance risk — และเสนอทางเลือก (partner / paid discovery / รอรอบหน้า)
- **Warning Signs:** ตอบด้วยความรู้สึก "น่าเสียดาย" โดยไม่มีตัวเลข

## 9. PM Dictionary ประจำบท

| Term (EN) | คำอธิบาย (TH) | ความหมายเชิงปฏิบัติ | การใช้ผิดที่พบบ่อย | Term ที่เกี่ยวข้อง |
|---|---|---|---|---|
| Opportunity | โอกาสทางธุรกิจ | lead/RFP/request ที่ยังไม่ใช่โครงการที่ได้รับอนุมัติ | สับสนกับ Project | Bid/No-Bid, Proposal |
| Bid / No-Bid | การตัดสินใจเสนอราคาหรือไม่ | ตัดสินด้วย value, capability, capacity, risk | คิดว่า No-Bid คือการแพ้ | Opportunity, Proposal |
| Discovery | การสำรวจทำความเข้าใจปัญหา | เก็บ fact, pain, root cause, outcome ก่อนออก solution | รีบข้ามไปเป็น feature | Business Case |
| ROM | Rough Order of Magnitude | ประมาณการระดับสูงเพื่อตัดสินใจ ไม่ใช่ commitment | คิดว่าเป็นราคาผูกพัน | Estimate, Proposal |
| Proposal | ข้อเสนอโครงการ | executive summary, scope, timeline, price, assumptions | สับสนกับ SOW | SOW, Bid/No-Bid |
| SOW | Statement of Work | ขอบเขตงานที่ผูกพันตามสัญญา | สับสนกับ Proposal | Contract, Proposal |
| Assumption | สิ่งที่ถือว่าจริงแต่ยังไม่ได้พิสูจน์ | ต้องบันทึกและติดตาม เพราะถ้าผิดกลายเป็น risk | ไม่ถูก track จนเป็น surprise | Risk, Constraint |
| Desired Outcome | ผลลัพธ์ที่ต้องการ | วัดได้ เช่น 35% direct booking ใน 18 เดือน | สับสนกับ Output | Success Measures, Benefit |
| Success Measures | ตัวชี้วัดความสำเร็จ | KPI ที่ยืนยันว่า outcome เกิดจริง | ตั้งตัวเลขลอย ๆ | Desired Outcome |
| Risk Allocation | การจัดสรรความเสี่ยง | ใครรับ risk ไหน ผ่าน contract/approach | คิดว่า vendor ต้องรับทุกอย่าง | Contract, T&M |
| T&M | Time and Material | จ่ายตามเวลา/วัสดุ เหมาะกับ scope ไม่ชัด | ไม่มี cap/rate/evidence แล้วบานปลาย | Fixed Price |
| Fixed Price | ราคาคงที่ | เหมาะกับ scope ชัด vendor รับ cost risk | ใช้กับ scope ไม่ชัดแล้วเจอ dispute | T&M, Contract |

## 10. Workshop

### Scenario
**[Teaching Scenario Extension]** ทีมคุณ (Pre-sales PM ที่ BTS) ได้รับ RFP จาก SHG เหมือนบทนำ แต่ CEO ขอให้ตอบภายใน 2 สัปดาห์แทน 3 สัปดาห์ และลูกค้าเปิดเผยข้อมูลเพิ่มเติมว่า "PMS บางโรงแรมยังไม่มี API ครบ แต่ฝ่าย IT ของเขาจะช่วย" — ฝ่าย Sales อยากได้ราคา Fixed ตัวเดียวเพราะ "ลูกค้าชอบแบบนั้น"

### Your Role
คุณคือ Pre-sales PM ที่ต้องเตรียม Bid/No-Bid recommendation + โครง Proposal ให้ CEO ตัดสินใจ

### Available Information
- Scenario Master v1.0 (ตัวเลข SHG ทั้งหมด), Discovery ครบ 10 คำถาม, ROM ของ Functional Leads มีช่วง 6.0–8.5 ล้านบาท, ทีม dev ฟรี capacity เริ่มเดือนถัดไป 80%

### Missing Information
- ความชัดเจนของ PMS API ทั้ง 12 โรงแรม (มีข้อมูลแค่ "ไม่ครบ"), เงื่อนไข payment ของ SHG, ระดับการมีส่วนร่วมของฝ่าย IT ลูกค้า, ผลการตรวจ compliance/security ของ platform ที่ต้องทำ

### Decision Required
- Bid หรือ No-Bid? ถ้า Bid: Fixed, Hybrid หรือ T&M? ขอบเขต Phase 1 ควรตัดอะไรออกจาก MVP?

### Constraints
- งบ Phase 1 ของลูกค้า 12 ล้านบาท (ห้ามเกิน), launch ก่อน High Season, Proposal ต้องมี In/Out of Scope, ต้องไม่รับปากสิ่งที่ไม่มี basis

### Expected Output
- Bid/No-Bid decision record หนึ่งหน้า (พร้อม 3 options + trade-off), โครง Proposal 1 หน้า (In/Out of Scope + pricing approach + assumptions), รายการ missing information ที่ต้องขอเพิ่ม

### Debrief Questions
1. อะไรคือสัญญาณที่บอกว่าควร No-Bid ในกรณีนี้
2. ทำไม Hybrid pricing ถึงเหมาะกับงานที่มี major unknown อย่าง PMS integration
3. ถ้า CEO บังคับ Fixed Price คุณจะปกป้อง margin ด้วยกลไกอะไรใน SOW

### Evaluation Criteria
- มี evidence-based options ไม่ใช่คำตอบเดียว, missing information ถูกระบุเป็นรายการ, pricing ถูกจัดสรรความเสี่ยงอย่างสมเหตุผล, decision record มี owner + next action

## 11. Checklist ใช้งานจริง (Pre-sales / Phase A)

- [ ] Opportunity Brief บันทึกแล้ว (ลูกค้า, ผู้ขอ, ปัญหา, deadline, งบ, decision maker)
- [ ] Discovery ครบ 10 คำถามขั้นต่ำ และมี As-Is/Root Cause
- [ ] Desired Outcome + Success Measures ตรงกับตัวเลข Scenario Master (35% direct, 18 เดือน, NPS ≥ 40)
- [ ] Solution Options ≥ 2 (ไม่ใช่แค่ custom development)
- [ ] ROM มีช่วง + assumptions + confidence + expiration
- [ ] Internal review ผ่าน (feasibility, margin, capacity, security, contract risk)
- [ ] Proposal มีครบ 19 องค์ประกอบ รวม In/Out of Scope และ Client Responsibilities
- [ ] Negotiation ทุกข้อผ่าน Impact Analysis ก่อนตอบรับ
- [ ] SOW ไม่ขัดกับ Proposal และมี acceptance/payment/change control
- [ ] Bid/No-Bid decision บันทึกเป็นลายลักษณ์อักษร
- [ ] ส่งมอบ Handover Record ไป Ch.2 (Proposal version, SOW version, สิ่งที่ Sales รับปาก, assumptions, risks)

## 12. Assessment

1. **[Decision Case]** ลูกค้าขอเพิ่ม "Mobile App" เข้า Proposal ทั้งที่ RFP ระบุแค่ Website — งบเท่าเดิม เวลาเท่าเดิม คุณจะทำอะไรก่อนตอบรับ? (ระบุ evidence ที่ต้องขอ และทางเลือกอย่างน้อย 3 ทาง)
2. **[Decision Case]** Sales เสนอราคา 9 ล้านบาทแบบ Fixed โดยอ้างว่าคู่แข่งเสนอ 8.5 ล้าน แต่ ROM ของทีมคือ 9.5–12 ล้าน — คุณจะแนะนำ CEO อย่างไร?
3. **[Trade-off Case]** ระหว่าง Fixed Price กับ T&M สำหรับงาน PMS integration ที่ API ยังไม่ชัด — อธิบาย trade-off ด้าน risk allocation และ margin
4. **[Artifact Review]** ตรวจ Proposal ที่ไม่มีหัวข้อ Out of Scope และ Assumptions — อธิบายว่าเมื่อเซ็นไปแล้วจะเกิดปัญหาอะไรตอนส่งมอบ
5. **[Executive Communication]** เขียนสรุป 1 ย่อหน้าให้ CEO ว่า ทำไมต้องเพิ่ม Paid Discovery Phase ก่อนเซ็นสัญญาเต็ม
6. **[Cross-Knowledge Analysis]** ถ้า SHG ยืนยัน launch ก่อน High Season (1 พ.ย.) แต่ Discovery พบว่า PMS integration น่าจะใช้เวลา 6 เดือน — scope/timeline/price ต้องถูกปรับอย่างไร และใครควรเป็นคนตัดสินใจ
7. **[Recall]** อะไรคือความแตกต่างระหว่าง ROM กับราคาผูกพันใน Proposal

## 13. Executive Summary

| มิติ | สรุป |
|---|---|
| **Why** | คุณภาพของ Proposal/SOW กำหนดขอบเขตของความเสี่ยงที่ PM จะต้องแบกไปทั้งโครงการ |
| **Decision Improved** | Bid/No-Bid, contract type และ In/Out of Scope ถูกตัดสินด้วย evidence แทนความรู้สึก |
| **Failure Prevented** | ป้องกัน scope dispute, margin หาย, และสัญญาที่ส่งมอบไม่ได้ |
| **What to Monitor** | จำนวน/คุณภาพของ assumption, confidence ของ ROM, และความสอดคล้อง Proposal ↔ SOW |

## 14. เชื่อมไปบทถัดไป + Artifact Handoff

**Bridge:** เมื่อ SOW เซ็นแล้ว งานยังไม่ใช่ "โครงการ" จนกว่าจะมี Project Charter ที่ Sponsor อนุมัติ — Ch.2 (Initiation) จะเปลี่ยนสัญญาให้กลายเป็นอำนาจการบริหาร: Charter, Stakeholder Register, Governance และ Kickoff

| Field | Handoff |
|---|---|
| Input | Opportunity Brief, Discovery Summary, Solution Options, ROM, Initial Risk Register |
| Output | Approved Proposal, Signed SOW/Contract, Bid/No-Bid Decision Record |
| Creator | Sales + Pre-sales PM / Legal / Commercial |
| Artifact owner | Opportunity Owner -> PM (หลัง authorize) |
| Reviewer | Legal, Finance, Delivery Owner |
| Approval authority | CEO / Authorized Signatory |
| Minimum acceptance | Usable (Proposal กับ SOW ต้องไม่ขัดกัน) |
| Next chapter use | Ch.2 ใช้ SOW, assumptions และ initial risks มาสร้าง Project Charter + Stakeholder Register |

## 15. Quick Reference Card

```text
PRE-SALES (A) — เป้าหมาย: ตัดสินใจ Bid/No-Bid ด้วย evidence
------------------------------------------------------------
1. Opportunity Brief  -> ใครขอ ทำไมตอนนี้ งบ/เวลา/decision maker
2. Discovery 10 คำถาม -> ปัญหา ใครเจอ ผลกระทบ outcome วัดอะไร
3. As-Is + Root Cause -> อย่ารีบแปลง pain เป็น feature
4. Solution Options   -> ไม่ใช่แค่ custom dev (SaaS/process/partner/POC)
5. ROM                -> ช่วง + assumptions + confidence (ไม่ใช่ราคา)
6. Internal Review    -> feasibility, margin, capacity, security
7. Proposal 19 ข้อ    -> ต้องมี In/Out of Scope + Client Responsibilities
8. Negotiation        -> ทุกยอมลด/เพิ่มต้องมี Impact Analysis
9. SOW                -> ไม่ขัด Proposal + acceptance/payment/change
10. Bid/No-Bid        -> บันทึกเป็น decision record

กฎ 3 ข้อห้าม:
- ห้ามรับปากราคา/เวลาจากคำบอกเล่า
- ห้าม Proposal ไม่มี Out of Scope
- ห้าม Sales รับปาก feature นอกเอกสาร

มือขวาของ PM ในบทนี้: Assumption Log + Initial Risk Register
```

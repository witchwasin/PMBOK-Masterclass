---
chapter: ch-03
title: "Requirements, Scope และ WBS (Playbook C1–C6)"
book: "PM Delivery Guide: From Pre-sales to Closure — คู่มือปฏิบัติการบริหารโครงการซอฟต์แวร์ (PMBOK 8th Edition)"
edition: Learner
status: Draft
validation_status: Not Validated
last_reviewed: 2026-08-13
intended_learner_level: Beginner PM | Experienced PM
difficulty: Core
estimated_study_time: 100
prerequisite:
  - "Ch.2 — Initiation (Charter, Stakeholder, Governance)"
related_chapters:
  - "Ch.5 — Risk/Procurement/Environment (รวม Test Strategy/Quality Plan — ดู cross-reference)"
  - "Ch.8 — Verification/UAT (Test Results/UAT Evidence)"
canonical_source:
  - ../../references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md (Phase C1–C6)
  - ../../e-Book/chapters/lesson-07/lesson-07-learner.md (Scope Management เต็มบท)
scenario_version:
  hotel_booking: "1.0"
artifact_outputs:
  - name: Requirements List + RTM
    creator: BA + PM
    artifact_owner: Product Owner
    reviewer: Stakeholder owners, QA Lead
    approval_authority: Product Owner / Sponsor (ตาม threshold)
    approval_evidence: Requirements baseline approval
  - name: Project Scope Statement
    creator: BA + PM
    artifact_owner: PM + Product Owner
    reviewer: Sponsor, Business Owner
    approval_authority: Sponsor / CCB
    approval_evidence: Scope baseline approval
  - name: WBS + WBS Dictionary
    creator: PM + Leads
    artifact_owner: PM
    reviewer: Functional Leads, QA
    approval_authority: Sponsor / CCB
    approval_evidence: Approved Scope Baseline
---

# Chapter 03 — Requirements, Scope และ WBS: ทำให้ "โจทย์" กลายเป็น "ขอบเขตที่ควบคุมได้"

## 1. Opening Scenario Hook

**[Teaching Scenario]** คุณคือคุณสุทธิ (PM ฝั่ง SHG) ระหว่าง workshop requirements คุณภัทร (VP Marketing) บอกว่า "ผมต้องการ dashboard ที่ดู conversion ทุกอย่าง และต้องมี loyalty program ด้วยนะ เดี๋ยวเราค่อยขายเพิ่มทีหลัง" ขณะที่คุณวีระ (CTO) ตอบว่า "ทีมเราทำได้ แต่ต้องรู้ขอบเขตก่อน" และคุณกาญจนา (Revenue Manager) ถามว่า "แล้วข้อมูลราคา/ห้องว่างของ 12 โรงแรมจะมาครบเมื่อไร"

ทุกคนพูดเป็นภาษา "ความต้องการ" แต่ยังไม่มีใครพูดเป็นภาษา "requirement ที่ตรวจรับได้" — และถ้าเก็บคำว่า "ทุกอย่าง" เข้าไปใน scope วันนี้ พรุ่งนี้ทั้งทีมจะต้องเดาว่าจริง ๆ แล้วต้องสร้างอะไร

**[PMBOK 8]** บทนี้คือจุดที่ Stakeholder needs จาก Ch.2 ถูกแปลงเป็น requirement, scope boundary และ WBS ที่ Ch.4 (Schedule/Cost/Resource) จะเอาไปวางแผนต่อได้จริง

## 2. Why It Matters

**[PMBOK 6]** Scope Management ตอบคำถามสามข้อ: จะส่งมอบอะไร จะไม่ส่งมอบอะไร และจะรู้ได้อย่างไรว่าส่งมอบแล้วผ่าน — ถ้าขอบเขตไม่ชัด Schedule จะเป็นการเดาวัน, Cost เป็นตัวเลขไม่มีฐาน, Quality ไม่มีเกณฑ์ตรวจรับ และ Change Control กลายเป็นการเถียงว่า "เรื่องนี้เคยอยู่ใน scope ไหม"

**[Best Practice]** Scope ที่ดีไม่ใช่เอกสารยาว แต่เป็นเส้นแบ่งที่ทีม ผู้บริหาร และผู้ใช้เข้าใจตรงกันพอที่จะตัดสินใจได้

## 3. Mental Model

จาก Playbook V2:

```text
Stakeholder Need (Ch.2)
  -> Tailor Delivery Approach (C1) — Predictive/Agile/Hybrid ต่อ workstream
  -> Plan Requirements Work (C2) — จะเก็บ/วิเคราะห์/อนุมัติ/trace อย่างไร
  -> Collect & Analyze Requirements (C3) — types + techniques + quality
  -> Document Set Decision (C4) — SRS/FSD หรือสิ่งทดแทน ตาม complexity
  -> Define Scope (C5) — Product vs Project, In/Out, acceptance criteria
  -> WBS + Dictionary (C6) — แตกตาม deliverable จนถึง work package
  -> Scope Baseline (approved) -> Ch.4 (Schedule/Cost/Resource)
```

> **Cross-reference (Quality):** Acceptance Criteria ถูกกำหนดในบทนี้ต่อ requirement; **Test Strategy / Quality Plan ฉบับเต็มอยู่ Ch.5** (วางแผนคุณภาพ) และ **ผลการทดสอบ/UAT Evidence อยู่ Ch.8** — อย่ามองข้ามเส้นนี้

## 4. Main Lesson

### 4.1 Tailor Delivery Approach (C1) — เลือกวิธี ไม่ใช่เลือกตามใจ

**[PMBOK 8]** เลือก Predictive/Agile/Hybrid จาก: Requirement Stability, Technical Uncertainty, Contract Type, Regulatory, Release Frequency, Customer Availability, Team Maturity, Dependency, Architecture, Risk และ Need for Formal Approval

**[Teaching Scenario]** SHG ใช้ Hybrid: การวางแผน scope/schedule/cost ทำแบบ predictive (ต้องควบคุม 12M และ launch 1 พ.ย.) แต่การพัฒนาเป็น sprint-based (Scrum) ตาม Scenario Master — รายละเอียด Tailoring อยู่ Ch.4/Ch.6 (กล่อง "ถ้าโครงการเป็น Agile")

### 4.2 Plan Requirements Work (C2)

**[Best Practice]** กำหนด: แหล่ง requirement, stakeholder ที่ต้องร่วม, เทคนิค elicitation, ประเภท requirement, format, review/approval, traceability (RTM), change control และ versioning — ผลลัพธ์คือ Requirements Management Plan

### 4.3 Collect and Analyze Requirements (C3)

**[PMBOK 6]** ประเภท requirement: Business, Stakeholder, Solution (Functional/Non-functional), Transition, Data, Integration, Reporting, Security/Compliance, Operational และ Acceptance

**[Best Practice]** เทคนิค: Interview, Workshop, Observation, Questionnaire, Document Analysis, Interface Analysis, Process Modeling, Prototyping, Benchmarking, Focus Group, Story Mapping, Use Case, User Story, Data Modeling

**Requirement ต้องมีคุณภาพ 9 ข้อ:** Clear, Complete, Consistent, Feasible, Testable, Traceable, Prioritized, Unambiguous, Necessary และ Owned

### 4.4 SRS/FSD — เอกสารหรือสิ่งทดแทน (C4)

**[PMBOK 8]** PMBOK ไม่บังคับชื่อเอกสาร — บังคับว่า Requirement ถูก Elicit, Analyze, Document, Prioritize, Approve, Trace, Validate และ Control

**[Best Practice]** SRS (Software Requirements Specification) ควรมีเมื่อ contract formal/ระบบซับซ้อน/หลายทีม/ต้อง sign-off/compliance; FSD (Functional Specification) ครอบคลุม behavior, business rules, screen behavior, validation, error handling — **ห้ามตัด FSD โดยไม่มีสิ่งทดแทน** เมื่อ logic ซับซ้อน/หลายระบบ/offshore/audit/ผูก payment (ดู Document Substitution Matrix ใน Playbook V2 §C4.4)

### 4.5 Define Scope (C5)

**[PMBOK 6]** แยก **Product Scope** (คุณสมบัติของสิ่งที่ส่งมอบ) ออกจาก **Project Scope** (งานที่ต้องทำเพื่อให้ได้สิ่งนั้น) — Scope Statement ควรมี Product Scope Description, Project Deliverables, Acceptance Criteria, Exclusions, Constraints และ Assumptions

**[Teaching Scenario]** SHG Phase 1 (MVP) In Scope: Customer Web App, Mobile App (iOS+Android), Landing Page, Back Office Web App, Booking Engine, PMS Sync 12 โรงแรม, Payment (2C2P), Notification — Out of Scope: Loyalty Program, Digital Key, Chatbot, Multi-language (นอกจาก TH/EN), Restaurant/Spa Booking, Channel Manager (ทั้งหมดตรง Scenario Master §4)

### 4.6 WBS และ WBS Dictionary (C6)

**[PMBOK 6]** WBS แตก Total Project Scope เป็น Deliverable และ Work Package ที่ estimate/assign/schedule/cost/control ได้ — ใช้ Decomposition + 100% Rule (ผลรวมของ child = parent = approved scope เท่านั้น ไม่รวมทุกคำขอ)

**ขั้นตอน:** ระบุ final product → ระบุ major deliverables → เลือก decomposition logic → แตก deliverables → ตรวจ 100% Rule → หยุดที่ work package → ระบุ owner → สร้าง WBS Dictionary → ตรวจ scope coverage → approve scope baseline

**[Best Practice]** WBS Dictionary ต้องมี: WBS ID, Work Package, Description, Deliverable, Included/Excluded Work, Owner, Requirements, Acceptance Criteria, Quality Criteria, Assumptions, Constraints, Dependencies, Milestone, Resource, Estimate, Cost Account, Risk, Approval

**[PMBOK 6]** อย่าแตก WBS ตาม department — แตกตาม deliverable (ไม่ใช่ "งานของแผนก IT" แต่เป็น "PMS Sync Adapter" หรือ "Payment Integration")

### 4.7 Scope Baseline และ Agile alternative

**[PMBOK 6]** Scope Baseline = Scope Statement + WBS + WBS Dictionary

**[PMBOK 8]** ถ้า Agile: ใช้ Product Goal, Product Backlog, Epic/Feature, User Story + Acceptance Criteria, Release Boundary, Definition of Done — แต่ยังต้องมี Scope/Value Boundary และ Traceability

## 5. PM Decision Thinking

```text
Decision: คำขอ "loyalty program" ของคุณภัทร อยู่ใน scope baseline หรือเป็น change (และควร include/defer/replace)
Owner: PM วิเคราะห์ impact; PO คุณนภา จัด priority; Sponsor/CCB อนุมัติเมื่อกระทบ baseline
Inputs: requirement, scope statement, WBS, WBS dictionary, acceptance criteria, impact analysis, value
Options:
  A: Include ใน Phase 1 — value สูงแต่เสี่ยง payment/launch readiness
  B: Defer ไป Phase 2 (ตาม Scenario Master: Loyalty อยู่ Out of Scope) — รักษา MVP + high season launch
  C: Replace ฟีเจอร์ value ต่ำกว่าใน MVP — ต้องมี decision evidence ว่า replace อะไร
Trade-offs: value เพิ่ม vs schedule/cost/quality risk, scope completeness vs launch readiness
Risk: รับ "ทุกอย่าง" เข้า MVP -> scope ระเบิด -> 12M/8 เดือนไม่พอ
Evidence: updated scope baseline, decision record, stakeholder communication
Next Action: แปลงคำขอเป็น requirement ที่ตรวจรับได้ -> ถ้าเกิน MVP ให้เข้า change process (Ch.7)
```

## 6. ตัวอย่างจริงจาก Case ต่อเนื่อง (SHG)

**[Teaching Scenario]** ทีม SHG เก็บ requirements สำหรับ Direct Booking Platform:

- **Business Requirement:** เพิ่ม Direct Booking จาก 10% เป็น 35% ใน 18 เดือน, ลด OTA commission ≥ 3 ล้านบาท/ปี
- **Functional (ตัวอย่าง):** ผู้ใช้ค้นหาห้องพักตามโรงแรม/วันที่/จำนวนผู้เข้าพัก, เปรียบเทียบราคา, จองและชำระเงินผ่าน 2C2P, รับ confirmation email/SMS
- **Non-functional:** Page load ≤ 3 วินาที, Booking confirmation ≤ 5 วินาที, Uptime ≥ 99.5%, PCI-DSS + PDPA compliance
- **WBS ตัวอย่าง (Payment Integration work package):** Payment Gateway Contract, API Design, Payment Flow Implementation, Callback Handling, Security Review, Payment Testing, Reconciliation Setup — แต่ละ item มี owner + acceptance criteria ใน WBS Dictionary

**[PMBOK 8]** WBS fragment นี้จะถูกใช้ต่อใน Ch.4 เพื่อนิยาม activities, dependencies และ duration

## 7. จุดตัดสินใจและกับดักที่พบบ่อย

**Common Mistakes:**

1. รับคำว่า "ทั้งหมด/ทุกอย่าง" เป็น requirement — ผล: ขอบเขตไร้ขีดจำกัด
2. เก็บ requirement เป็น "ฟีเจอร์" ทันทีโดยไม่ถาม decision need — ผล: สร้างของที่ไม่มีใครใช้
3. WBS แตกตามแผนก/activity — ผล: ไม่เห็น deliverable และ 100% Rule พัง
4. ไม่มี acceptance criteria ต่อ requirement — ผล: UAT (Ch.8) เถียงกันว่า "แบบไหนถึงจะผ่าน"
5. ลืม Out of Scope — ผล: ทุกอย่างกลายเป็น "ใน scope"
6. ไม่มี RTM — ผล: ตรวจไม่ได้ว่า requirement ไหนถูก build/test/accept

**Common Misconceptions:**

| ความเข้าใจผิด | ความจริง |
|---|---|
| WBS คือ task list | WBS คือ deliverable/work-package structure |
| Requirement ละเอียด = ดี | ต้อง Testable + Traceable + Prioritized |
| 100% rule = รวมทุกคำขอ | รวมเฉพาะ approved scope |
| SRS/FSD เป็นชื่อเอกสารที่บังคับ | บังคับที่ coverage ไม่ใช่ชื่อไฟล์ |
| Scope ชัด = เขียนยาว | Scope ชัด = มี boundary + acceptance |

## 8. Interview Questions

### Foundational
- **Q:** Product Scope ต่างจาก Project Scope อย่างไร?
- **Answer Direction:** Product Scope = คุณสมบัติของสิ่งที่ส่งมอบ (features); Project Scope = งานทั้งหมดที่ต้องทำเพื่อส่งมอบ (blueprint, migration, test, training)
- **Warning Signs:** ตอบว่าเหมือนกัน หรือสลับกัน

### Scenario
- **Q:** ลูกค้าขอ "รายงานทุกอย่าง" ระหว่างเก็บ requirement คุณจะจัดการอย่างไร?
- **Answer Direction:** ถามกลับ: รายงานใช้ตัดสินใจอะไร ใครเป็นผู้ใช้ ข้อมูลจากระบบไหน ต้องแม่นแค่ไหน ตรวจรับอย่างไร → แปลงเป็น requirement slices ที่ testable + traceable
- **Warning Signs:** รับคำแล้วใส่ใน scope หรือปฏิเสธโดยไม่มีทางเลือก

### Senior PM
- **Q:** WBS ควรแตกลึกแค่ไหน?
- **Answer Direction:** หยุดที่ Work Package ที่ estimate/assign/วัด progress/accept/control ได้ — ลึกเกิน = กลายเป็น activity list (งานของ Ch.4); ไม่ลึกพอ = ควบคุมไม่ได้
- **Warning Signs:** ตอบ "แตกให้ละเอียดที่สุด" หรือ "ตามความรู้สึก"

### Executive
- **Q:** ทำไม Scope Baseline ต้องได้รับการอนุมัติก่อนเริ่ม build?
- **Answer Direction:** Baseline = ฐานเทียบวัดทุกอย่าง (schedule/cost/change) — ถ้าไม่มี baseline การรายงานสถานะและ change control จะกลายเป็นความเห็น ไม่ใช่การวัดผล
- **Warning Signs:** ตอบว่า "เป็นกระบวนการของ PM" โดยไม่เชื่อมกับ governance

## 9. PM Dictionary ประจำบท

| Term (EN) | คำอธิบาย (TH) | ความหมายเชิงปฏิบัติ | การใช้ผิดที่พบบ่อย | Term ที่เกี่ยวข้อง |
|---|---|---|---|---|
| Requirement | ข้อกำหนดความต้องการ | ต้อง Testable + Traceable | คิดว่า "ฟีเจอร์" คือ requirement | Scope, RTM |
| Product Scope | ขอบเขตผลิตภัณฑ์ | คุณสมบัติของสิ่งที่จะส่งมอบ | ไม่แยกจาก Project Scope | Project Scope |
| Project Scope | ขอบเขตโครงการ | งานที่ต้องทำเพื่อส่งมอบ product | ไม่แยกจาก Product Scope | WBS |
| Scope Statement | คำนิยามขอบเขต | In/Out, deliverable, acceptance, constraint | เขียนยาวแต่ไม่มี boundary | Scope Baseline |
| WBS | Work Breakdown Structure | แตก approved scope เป็น work packages | แตกตาม department | Work Package |
| WBS Dictionary | พจนานุกรม WBS | owner, boundary, acceptance, dependency | คิดว่า WBS diagram พอแล้ว | WBS |
| 100% Rule | กฎ 100% | WBS ครอบคลุม approved scope เท่านั้น | รวมทุกคำขอ | Scope Baseline |
| Scope Baseline | ฐานควบคุมขอบเขต | Scope Statement + WBS + Dictionary | สับสนกับ Project Plan | Validate/Control Scope |
| RTM | Requirements Traceability Matrix | เชื่อม requirement → design → test → acceptance | ทำเพื่อให้ครบ template | Requirement, Test Case |
| Validate Scope | ตรวจรับขอบเขต | ยืนยัน deliverable กับผู้มี authority | สับสนกับ Control Scope | Control Scope |
| Control Scope | ควบคุมขอบเขต | จัดการ change ต่อ baseline | สับสนกับ Validate Scope | Change Request |
| Scope Creep | ขอบเขตบาน | เพิ่มงานโดยไม่ผ่าน change control | สับสนกับ Progressive Elaboration | Change Request |

## 10. Workshop

### Scenario
**[Teaching Scenario]** คุณได้รับมอบหมายให้กำหนด Scope Phase 1 ของ SHG — คุณภัทร (VP Marketing) ต้องการ "dashboard ที่ดู conversion ทุกอย่าง" และ "loyalty program" ส่วนคุณวีระ (CTO) ต้องการให้ล็อก PMS sync เป็น workstream แยก

### Your Role
PM (คุณสุทธิ) ที่ต้องสร้าง Scope Artifact Pack

### Available Information
- Scenario Master v1.0 (In/Out of Scope MVP, 8 objectives, stakeholders, constraints), Stakeholder Register จาก Ch.2

### Missing Information
- นิยาม "conversion ทุกอย่าง" ของคุณภัทร (KPI อะไร, ความถี่, ผู้ใช้), ข้อมูลราคา/ห้องว่างที่โรงแรมจะให้, ระดับ API ของ PMS แต่ละยี่ห้อ, งบ/เวลาที่แน่นอนของงาน dashboard

### Decision Required
- ฟีเจอร์ใดอยู่ใน MVP, ฟีเจอร์ใด defer ไป Phase 2, acceptance criteria ของ dashboard คืออะไร

### Constraints
- งบ 12M / launch ก่อน 1 พ.ย. / loyalty อยู่ใน Out of Scope ตาม Scenario Master

### Expected Output
- Requirements List (≥ 8 รายการ มี priority + owner), Scope Statement (In/Out/Assumptions/Constraints), WBS fragment สำหรับ "Payment Integration" + WBS Dictionary 2 work packages

### Debrief Questions
1. ทำไม "conversion ทุกอย่าง" ยังไม่ใช่ requirement
2. Acceptance criteria ที่ดีสำหรับ dashboard คืออะไร
3. ถ้าไม่มี RTM จะเกิดอะไรตอน Ch.8

### Evaluation Criteria
- Requirement testable + traceable, Scope มี In/Out ชัด, WBS แตกตาม deliverable, decision record มี owner + evidence

## 11. Checklist ใช้งานจริง (Planning — Scope / Phase C1–C6)

- [ ] Delivery approach ถูก tailor ต่อ workstream (ไม่ใช่ "Agile ทั้งหมด")
- [ ] Requirements Management Plan กำหนดแล้ว (sources, techniques, approval, RTM, change)
- [ ] Requirements ครบทุกประเภทที่เกี่ยวข้อง (functional, non-functional, data, security, acceptance)
- [ ] Requirement ทุกข้อ Testable + Traceable + มี owner + priority
- [ ] SRS/FSD หรือสิ่งทดแทน ครบ coverage (ดู Substitution Matrix) — ไม่ตัดโดยไม่มีสิ่งทดแทน
- [ ] Scope Statement มี In/Out of Scope + Assumptions + Constraints + Acceptance Criteria
- [ ] WBS แตกตาม deliverable ผ่าน 100% Rule
- [ ] WBS Dictionary มี owner, acceptance, dependency ต่อ work package
- [ ] Scope Baseline ผ่าน approval (Sponsor/CCB)
- [ ] Cross-ref: Test Strategy/Quality Plan = Ch.5, Test Results/UAT = Ch.8

## 12. Assessment

1. **[Decision Case]** คุณภัทรขอเพิ่ม loyalty program ใน MVP — ตาม Scenario Master ข้อนี้อยู่ใน Out of Scope — คุณจะเสนออะไร (include/defer/replace) พร้อม evidence และ trade-off
2. **[Decision Case]** "รายงานทุกอย่าง" ถูกขอเพิ่ม — เขียนคำถาม 5 ข้อที่ต้องถามก่อนแปลงเป็น requirement
3. **[Artifact Review]** ตรวจ WBS ที่แตกเป็น "งานของ IT", "งานของ Marketing", "งานของ Finance" — อธิบายว่าทำไมไม่ใช่ WBS ที่ดี และแก้อย่างไร
4. **[Trade-off Case]** ระหว่าง SRS + FSD ฉบับเต็ม กับ User Story + Acceptance Criteria — อธิบาย trade-off สำหรับงานที่มี compliance สูง (payment/PCI-DSS)
5. **[Artifact Construction]** สร้าง WBS fragment สำหรับ "Payment Integration" ของ SHG (อย่างน้อย 5 work packages พร้อม owner + acceptance criteria)
6. **[Cross-Knowledge Analysis]** ถ้า PMS API ของ 3 โรงแรมไม่รองรับ real-time sync — กระทบ scope (Ch.3), schedule (Ch.4) และ test (Ch.8) อย่างไร
7. **[Recall]** 100% Rule ของ WBS คืออะไร และต่างจาก "รวมทุกคำขอ" อย่างไร

## 13. Executive Summary

| มิติ | สรุป |
|---|---|
| **Why** | ขอบเขตที่ชัดคือฐานของ schedule, cost, quality และ change control ทั้งหมด |
| **Decision Improved** | คำขอใหม่ถูกเทียบกับ baseline + impact แทนการรับด้วยความเกรงใจ |
| **Failure Prevented** | ป้องกัน scope creep, requirement ที่ทดสอบไม่ได้ และ WBS ที่ควบคุมไม่ได้ |
| **What to Monitor** | จำนวน change request ต่อ baseline, requirement coverage, acceptance criteria readiness |

## 14. เชื่อมไปบทถัดไป + Artifact Handoff

**Bridge:** Scope Baseline ผ่าน approval แล้ว — Ch.4 จะใช้ work packages + owners + acceptance criteria ไปนิยาม activities, dependencies, duration, cost และ resource (และใส่กล่อง Agile สำหรับ sprint-based delivery)

| Field | Handoff |
|---|---|
| Input | Stakeholder Register, Decision Rights (Ch.2), SOW (Ch.1) |
| Output | Requirements List, Scope Statement, WBS, WBS Dictionary, RTM |
| Creator | BA + PM (requirements), PM + Leads (WBS) |
| Artifact owner | PO (requirements), PM (scope/WBS) |
| Reviewer | Stakeholder owners, QA Lead, Functional Leads |
| Approval authority | Sponsor / CCB (scope baseline) |
| Minimum acceptance | Usable (ต้องมี In/Out + acceptance criteria + RTM) |
| Next chapter use | Ch.4 ใช้ work packages, owners, acceptance และ constraints เพื่อสร้าง Activity List, Schedule, Cost และ Resource Plan |

## 15. Quick Reference Card

```text
SCOPE (C1–C6) — เป้าหมาย: Scope Baseline ที่ควบคุมได้
------------------------------------------------------------
1. Tailor approach      -> Predictive/Agile/Hybrid ต่อ workstream
2. Plan requirements    -> sources, techniques, approval, RTM, change
3. Collect/analyze      -> 9 คุณภาพ: Clear, Testable, Traceable, Owned...
4. SRS/FSD              -> ดู coverage ไม่ใช่ชื่อไฟล์; ห้ามตัดโดยไม่มีตัวแทน
5. Define scope         -> Product vs Project, In/Out, acceptance criteria
6. WBS                  -> แตกตาม deliverable ผ่าน 100% Rule
7. WBS Dictionary       -> owner, acceptance, dependency ต่อ work package
8. Scope Baseline       -> Sponsor/CCB อนุมัติก่อนเริ่ม build

กฎ 3 ข้อห้าม:
- ห้ามรับ "ทั้งหมด/ทุกอย่าง" เป็น requirement
- ห้าม WBS แตกตามแผนก
- ห้ามลืม Out of Scope

Cross-ref: Test Strategy/Quality = Ch.5 | Test Results/UAT = Ch.8
```

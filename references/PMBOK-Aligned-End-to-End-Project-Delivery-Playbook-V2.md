> **Repository Status Note (added 2026-07-31):** เก็บไฟล์นี้ไว้เป็น **Pending External Reference** ยังไม่ใช่ Canonical Source ตาม [`governance/CONTENT-RULES.md`](../governance/CONTENT-RULES.md) — เป็นเวอร์ชัน 2 ของ [`PMBOK-Aligned-End-to-End-Project-Delivery-Playbook.md`](PMBOK-Aligned-End-to-End-Project-Delivery-Playbook.md) (v1) เพิ่มชั้น Execution Ownership (RACI-style Accountable/Responsible ต่อกิจกรรม, Action Flow table ทุกช่วง A–H, Quick Role-to-Action Reference) ทำให้ actionable กว่า v1 — **ประเมินแล้วว่า v2 ดีกว่า v1 และเป็น preferred source สำหรับงานในอนาคต** (v1 ยังเก็บไว้เพื่ออ้างอิง ไม่ลบ) อ้างอิง PMBOK® Guide 8th Edition เหมือน v1 — ดู [`repository/PMBOK-EDITION-POSITION.md`](../repository/PMBOK-EDITION-POSITION.md) และ [`repository/REPOSITORY_DECISION_LOG.md`](../repository/REPOSITORY_DECISION_LOG.md) รายการที่ 9 — มีเก็บสำเนาไว้ที่ `repository/` ด้วย
>
> **แผนในอนาคต:** ใช้เป็นแหล่งอ้างอิงหลักสำหรับ [`field-guide/BOOK-BLUEPRINT.md`](../field-guide/BOOK-BLUEPRINT.md) — ยังไม่เริ่มเขียนเนื้อหาเล่ม

---

# PMBOK-Aligned End-to-End Project Delivery Playbook — V2
## คู่มือบริหารโครงการซอฟต์แวร์ตั้งแต่รับโจทย์ลูกค้าจนถึง Go-Live, Hypercare และ Closure

**Document Type:** Practical Project Delivery Playbook  
**Version:** 2.0 Execution-Oriented Working Manual  
**Language:** Thai with English Project Management Terms  
**Primary Scenario:** Hotel Booking / Reservation Platform  
**Audience:** Project Manager, Product Owner, Business Analyst, Tech Lead, QA Lead, Delivery Lead, Sponsor และทีมโครงการ  
**Applies To:** Software Development, System Implementation, Digital Product, Vendor Delivery และโครงการ Hybrid  
**Last Updated:** 31 July 2026  

> **Version 2 เพิ่ม:** ผู้รับผิดชอบ จุดเริ่ม เวลา สถานที่ วิธีทำ Output ผู้รับช่วงต่อ และ Decision Gate ในทุกช่วง A–H เพื่อให้ใช้สั่งงานจริงได้

---

# 0. วัตถุประสงค์ของคู่มือ

คู่มือนี้ถูกสร้างขึ้นเพื่อใช้เป็น **คู่มือเปิดทำงานจริงแบบ Step-by-Step** ตั้งแต่บริษัทได้รับโอกาสทางธุรกิจจากลูกค้า ไปจนถึงการส่งระบบขึ้น Production การดูแลช่วง Hypercare การส่งมอบให้ฝ่าย Operations และการปิดโครงการอย่างเป็นทางการ

คู่มือนี้ไม่ได้มีเป้าหมายให้ผู้ใช้งานสร้างเอกสารจำนวนมาก แต่มีเป้าหมายให้โครงการมีข้อมูล การตัดสินใจ เจ้าของงาน และหลักฐานที่เพียงพอสำหรับการบริหารให้สำเร็จ

หลักการสำคัญคือ:

> PMBOK ไม่ได้บังคับชื่อเอกสารทุกชิ้น แต่กำหนดให้โครงการต้องบริหารเรื่องสำคัญให้ครบ เช่น Value, Stakeholder, Scope, Schedule, Cost, Quality, Resource, Communication, Risk, Procurement, Change, Acceptance และ Transition

ดังนั้น เอกสารสามารถรวม แยก หรือเก็บอยู่ในระบบ เช่น Jira, Azure DevOps, Confluence, Notion, Spreadsheet หรือ Project Management Tool ได้ ตราบใดที่ข้อมูลครบ มี Owner มี Version มี Approval และสามารถ Trace กลับไปยัง Business Need ได้

---

# 1. Reference Basis

คู่มือนี้ใช้แนวคิดจากแหล่งอ้างอิงต่อไปนี้

1. **A Guide to the Project Management Body of Knowledge (PMBOK® Guide) — Eighth Edition**
2. **The Standard for Project Management**
3. **Process Groups: A Practice Guide**
4. **Practice Standard for Work Breakdown Structures — Third Edition**
5. **Business Analysis for Practitioners: A Practice Guide — Second Edition**
6. **Agile Practice Guide**
7. แนวคิด Software Development Life Cycle, DevSecOps, Requirements Engineering และ Product Delivery ที่ใช้กันทั่วไปในอุตสาหกรรม
8. PMBOK-Masterclass Repository ขององค์กร สำหรับ Teaching Flow, Artifact Dependency และ Scenario Application

## 1.1 สิ่งที่ต้องเข้าใจเกี่ยวกับ PMBOK

PMBOK คือมาตรฐานและองค์ความรู้ ไม่ใช่ Methodology สำเร็จรูปที่ทุกโครงการต้องเดินตามเหมือนกันทั้งหมด

PMBOK เน้น:

- การสร้าง Value
- การบริหารเป็นระบบ
- การ Tailor ให้เหมาะกับบริบท
- การตัดสินใจบนข้อมูล
- การบริหาร Stakeholder
- การจัดการความไม่แน่นอน
- การวัดผลและปรับตัว
- การส่งมอบ Outcome ไม่ใช่เพียง Output

ส่วน **Process Groups: A Practice Guide** ให้ภาพการบริหารแบบ Process-based ได้แก่:

1. Initiating
2. Planning
3. Executing
4. Monitoring and Controlling
5. Closing

Process Groups ไม่ใช่ Project Phases ที่เกิดครั้งเดียวและห้ามย้อนกลับ การ Planning, Executing และ Monitoring & Controlling สามารถเกิดซ้ำและทำงานร่วมกันตลอดโครงการ

---

# 2. วิธีใช้คู่มือ

ทุกช่วง A–H จะประกอบด้วยหัวข้อมาตรฐาน:

1. Goal
2. PMBOK / PMI Mapping
3. Entry Criteria
4. Dependencies
5. Approach / Methodology
6. Participants and Roles
7. Inputs
8. Step-by-Step Activities
9. Tools and Techniques
10. Required Artifacts
11. Approval Gate
12. Exit Criteria
13. Handoff
14. Common Mistakes
15. Practical Checklist

## 2.1 ระดับความจำเป็นของ Artifact

| Code | ระดับ | ความหมาย |
|---|---|---|
| **M** | Mandatory | ต้องมีข้อมูลหรือหลักฐานนี้ แม้จะไม่แยกเป็นไฟล์ |
| **C** | Conditional | ต้องมีเมื่อเข้าเงื่อนไขเฉพาะ |
| **R** | Recommended | ควรมี แต่สามารถรวมกับ Artifact อื่นได้ |
| **O** | Optional | ใช้เมื่อเพิ่มความชัดเจนหรือช่วยลดความเสี่ยง |
| **N/A** | Not Applicable | ไม่เกี่ยวข้องกับโครงการนั้น |

คำว่า Mandatory ในคู่มือนี้ไม่ได้หมายความว่าต้องมีไฟล์ Word ชื่อนั้นเสมอ แต่หมายความว่า **เนื้อหา การตัดสินใจ หรือหลักฐานต้องมีอยู่ในระบบบริหารโครงการ**

---


## 2.2 Execution Ownership Standard

ทุกกิจกรรมสำคัญต้องตอบให้ได้ว่า:

| Field | คำถามที่ต้องตอบ |
|---|---|
| Trigger | อะไรทำให้ต้องเริ่มกิจกรรมนี้ |
| Accountable | ใครรับผิดชอบผลสุดท้ายและมีอำนาจตัดสินใจ |
| Responsible | ใครลงมือทำงานหลัก |
| Consulted | ใครต้องให้ข้อมูลหรือความเห็น |
| Informed | ใครต้องรับทราบ |
| When | ทำเมื่อไร ต้องเสร็จก่อนอะไร |
| Where | ทำใน Meeting, Workshop, Tool หรือ Repository ใด |
| How | ใช้วิธี เทคนิค หรือเครื่องมืออะไร |
| Output | หลักฐานหรือสิ่งส่งมอบคืออะไร |
| Next Action | ใครรับช่วงต่อและทำอะไร |
| Decision Gate | ใครอนุมัติ และผ่านเมื่อใด |

### กติกาเริ่มต้น

- PM ออกแบบกระบวนการ นัดหมาย รวมข้อมูล ติดตาม และ Escalate
- Subject Matter Expert สร้างเนื้อหาเฉพาะด้าน
- Sponsor/Product Owner ตัดสินใจด้านธุรกิจ
- Tech Lead/Architect ตัดสินใจด้านเทคนิค
- QA Lead รับผิดชอบ Quality/Test Readiness
- Finance/Commercial รับผิดชอบ Cost, Price, Margin และ Payment
- Legal/Procurement รับผิดชอบ Contractual Compliance
- Operations รับผิดชอบ Operational Acceptance

---

# 3. End-to-End Delivery Flow

```text
A. Pre-sales / Before Project Authorization
    ↓
B. Project Initiation
    ↓
C. Detailed Planning
    ↓
D. Execution / Solution Delivery
    ↔
E. Monitoring, Controlling and Change
    ↓
F. Verification, UAT and Release Readiness
    ↓
G. Go-Live and Hypercare
    ↓
H. Transition, Closure and Benefit Handover
```

Monitoring & Controlling ไม่ได้เริ่มหลัง Execution เสร็จ แต่เกิดควบคู่กับ Execution ตั้งแต่เริ่มงานจริง

---

# A. PRE-SALES / BEFORE PROJECT AUTHORIZATION

## A.0 ใครทำอะไรในช่วงนี้

- **Accountable:** CEO / Sales Director / Opportunity Owner
- **Process Owner:** Pre-sales PM หรือ PM ที่ได้รับมอบหมาย
- **Business Analysis Owner:** BA / Consultant
- **Technical Feasibility Owner:** Tech Lead / Solution Architect
- **Commercial Owner:** Finance / Commercial
- **Contract Owner:** Legal / Procurement

**เริ่มเมื่อ:** มี Opportunity, RFP หรือคำขอจากลูกค้า  
**จบเมื่อ:** Proposal/SOW พร้อม, มี Bid/No-Bid Decision หรือได้รับ Commercial Authorization  
**สถานที่ทำงานหลัก:** Discovery Call, Customer Workshop, Internal Solution Review, CRM และ Proposal Repository

### A.0.1 Action Flow

| Step | Responsible | Accountable | เมื่อไร/ที่ไหน | วิธีทำ | Output | ผู้รับช่วงต่อ |
|---|---|---|---|---|---|---|
| Opportunity Intake | Sales | Sales Director | ทันทีที่ได้รับ Lead / CRM | Intake Form, Initial Call | Opportunity Brief | PM นัด Discovery |
| Initial Discovery | PM + BA | Opportunity Owner | ก่อน Estimate / Customer Session | Interview, Workshop | Discovery Summary | BA วิเคราะห์ Process |
| As-Is/Root Cause | BA + SME | PM | หลัง Discovery / Workshop | Process Walkthrough, 5 Whys | As-Is, Pain, Root Cause | Architect สร้าง Options |
| Desired Outcome | PM + Customer Sponsor | Customer Sponsor | ก่อนออก Solution | Outcome/KPI Workshop | Outcome, Success Measures | ทีมเทียบ Options |
| Solution Shaping | Architect + BA | Delivery Owner | Internal Workshop | Alternatives Analysis | Solution Options | Leads Estimate |
| ROM Estimate | Functional Leads | Delivery Owner | ก่อน Proposal | Expert Judgment, Range Estimate | Timeline/Cost/Assumption | Finance ตั้งราคา |
| Proposal | PM + Sales | CEO/Commercial Owner | ก่อนส่งลูกค้า | Proposal Review | Approved Proposal | ลูกค้า Review |
| Negotiation | Sales + PM | CEO | เมื่อลูกค้าขอเปลี่ยน | Impact/Trade-off | Negotiated Position | Legal ทำ SOW |
| Contract/SOW | Legal + PM | Authorized Signatory | ก่อน Authorization | Contract Review | Signed SOW/Contract | Internal Handover |


## A.1 Goal

เป้าหมายของช่วงนี้คือทำให้บริษัทตัดสินใจได้ว่า:

- ปัญหาของลูกค้าคืออะไร
- ปัญหานั้นมี Business Value เพียงพอหรือไม่
- ควรสร้างระบบใหม่หรือมีทางเลือกอื่น
- บริษัทมี Capability และ Capacity ส่งมอบหรือไม่
- Scope, Timeline และ Budget ระดับ Proposal มี Basis เพียงพอหรือไม่
- มี Commercial Risk หรือ Delivery Risk ใดที่ต้องรู้ก่อนเสนอราคา
- ควร Bid, No-Bid, Partner หรือเสนอ Discovery Phase แบบเสียเงินก่อน

ช่วงนี้ยังไม่ใช่โครงการที่ได้รับ Authorization อย่างเป็นทางการเสมอไป แต่อาจเป็น Pre-project, Opportunity, Consulting หรือ Sales Engineering

## A.2 PMBOK / PMI Mapping

ช่วง Pre-sales ไม่ใช่ Process Group อย่างเป็นทางการของ PMBOK แต่เชื่อมกับ:

- Business Need
- Business Case
- Value Delivery
- Stakeholder Engagement
- Business Analysis
- Needs Assessment
- Enterprise Environmental Factors
- Organizational Process Assets
- Inputs สำหรับ Develop Project Charter
- Progressive Elaboration
- Tailoring

## A.3 Entry Criteria

ต้องมีอย่างน้อย:

- Opportunity หรือคำขอจากลูกค้า
- ผู้ติดต่อที่มีสิทธิ์ให้ข้อมูล
- Business Trigger เบื้องต้น
- Permission ให้ทีมทำ Discovery หรือ Estimate
- ข้อมูลขั้นต่ำเกี่ยวกับองค์กรและบริบทธุรกิจ

## A.4 Dependencies

ไม่มี Project Artifact ก่อนหน้าเสมอไป แต่ควรมี:

- Account / Customer Context
- NDA หากข้อมูลเป็นความลับ
- Opportunity Owner
- Bid Timeline
- Proposal Submission Deadline
- Commercial Guideline ของบริษัท

## A.5 Approach / Methodology

วิธีที่ใช้ได้:

- Initial Business Discovery
- Opportunity Qualification
- Business Analysis
- Stakeholder Interview
- Workshop
- Observation
- Document Analysis
- Current-state Process Mapping
- Root Cause Analysis
- Design Thinking
- Solution Shaping
- Alternatives Analysis
- ROM Estimation
- Expert Judgment
- Bid / No-Bid Analysis

## A.6 Participants

| Role | หน้าที่ |
|---|---|
| CEO / Sales / Account Owner | เจ้าของ Opportunity และ Commercial Relationship |
| Pre-sales PM / PM | จัด Discovery, Scope, Estimate และ Delivery Risk |
| BA / Consultant | วิเคราะห์ Business Need, Process และ Requirement ระดับสูง |
| Domain Expert | ตรวจ Business Logic และ Industry Constraint |
| Tech Lead / Architect | ตรวจ Feasibility และ Solution Options |
| UX/UI | ช่วยตรวจ Journey, User Flow และ Design Complexity |
| QA Lead | ประเมิน Quality และ Test Scope |
| DevOps / Security | ประเมิน Environment, Deployment, Security |
| Finance / Commercial | Cost, Margin, Pricing และ Payment Terms |
| Legal / Procurement | Contract, NDA, Liability และ Vendor Terms |

## A.7 Step-by-Step Activities

### A1. Opportunity Intake

PM หรือ Account Owner บันทึก:

- ลูกค้าคือใคร
- ใครเป็นผู้ขอ
- ปัญหาที่พูดมาเบื้องต้น
- Deadline
- งบประมาณที่ลูกค้าเปิดเผย
- Competitor / Procurement Context
- Decision Maker
- เหตุผลที่ต้องทำตอนนี้

**Output:** Opportunity Brief

### A2. Initial Business Discovery

คำถามขั้นต่ำ:

1. ปัญหาปัจจุบันคืออะไร
2. เกิดกับใคร
3. เกิดบ่อยเพียงใด
4. ผลกระทบคืออะไร
5. ทำไมต้องแก้ตอนนี้
6. หากไม่ทำจะเกิดอะไร
7. Outcome ที่ต้องการคืออะไร
8. Success จะวัดอย่างไร
9. มีข้อจำกัดอะไร
10. ใครมีอำนาจตัดสินใจ

ตัวอย่าง Booking:

```text
Current situation:
ลูกค้าจองผ่าน LINE และโทรศัพท์
พนักงานตรวจตารางด้วย Spreadsheet
ข้อมูลไม่ครบและเกิด Double Booking
ลูกค้ารอนานและยกเลิกการจอง
```

### A3. Current-state Process and Pain Analysis

จับข้อมูล:

- Trigger
- Actor
- Process Step
- Data
- Decision
- System
- Waiting
- Error
- Rework
- Pain Point
- Business Impact

ไม่ควรรีบเปลี่ยน Current Process เป็น Software Feature ทันที

### A4. Root Cause Analysis

แยก:

- Symptom
- Immediate Cause
- Root Cause
- Constraint
- Control Failure

ตัวอย่าง:

```text
Symptom: ลูกค้าถูกจองซ้ำ
Immediate Cause: พนักงานสองคนอัปเดต Spreadsheet ไม่พร้อมกัน
Root Cause: ไม่มี Single Source of Truth และไม่มี Transaction Lock
```

### A5. Define Desired Outcome

Outcome ต้องวัดได้มากกว่า “มีระบบ Booking”

ตัวอย่าง:

- ลด Double Booking จาก 8% เหลือน้อยกว่า 1%
- ลด Average Response Time จาก 20 นาทีเหลือต่ำกว่า 3 นาที
- เพิ่ม Booking Completion Rate
- ลด Manual Reconciliation
- ทำให้ลูกค้าตรวจ Availability ได้ด้วยตนเอง

### A6. Identify Solution Options

ห้ามสมมติว่า Solution ต้องเป็น Custom Software เสมอ

ตัวเลือกอาจเป็น:

1. Process Improvement
2. Training
3. SaaS
4. Customize Existing System
5. Integration
6. Custom Development
7. Phased Hybrid Solution
8. Paid Discovery / POC

### A7. High-Level Scope Options

ตัวอย่าง:

#### Option 1 — MVP

- Customer Booking Web
- Availability Check
- Booking Confirmation
- Admin Booking Management
- Basic Notification

#### Option 2 — Standard

- MVP
- Online Payment
- Cancellation / Refund
- Basic Reports
- User Accounts

#### Option 3 — Extended

- Standard
- Mobile App
- Loyalty
- Multi-property
- Advanced Integration
- Analytics

ทุก Option ต้องระบุ:

- Business Value
- Included Capabilities
- Exclusions
- Assumptions
- Dependencies
- Risks
- Estimated Timeline
- Estimated Cost Range
- Confidence Level

### A8. ROM Estimation

ROM = Rough Order of Magnitude

ใช้สำหรับตัดสินใจเบื้องต้น ไม่ใช่ Commitment

Estimate ต้องมี:

- Scope Basis
- Assumptions
- Team Model
- Duration Range
- Cost Range
- Confidence
- Major Unknowns
- Contingency Logic
- Expiration / Validity

### A9. Internal Solution Review

ตรวจ:

- Business fit
- Technical feasibility
- Delivery feasibility
- Operational feasibility
- Commercial feasibility
- Security / Compliance
- Contract risk
- Resource availability
- Margin

### A10. Proposal Development

Proposal ควรมี:

1. Executive Summary
2. Business Understanding
3. Problem and Desired Outcome
4. Proposed Solution
5. Scope and Deliverables
6. In Scope / Out of Scope
7. Delivery Approach
8. High-Level Timeline
9. Team Structure
10. Pricing
11. Assumptions
12. Dependencies
13. Client Responsibilities
14. Acceptance Approach
15. Payment Milestones
16. Change Approach
17. Warranty / Support
18. Proposal Validity
19. Next Steps

### A11. Negotiation and Commercial Alignment

เมื่อมีคำขอ:

- ลดราคา
- เร่งเวลา
- เพิ่ม Scope
- ลดทีม
- เพิ่ม Warranty

ต้องทำ Impact Analysis ก่อนตอบรับ

หลัก Trade-off:

```text
เพิ่ม Scope → ต้องเพิ่มเวลา งบ คน หรือลด Scope อื่น
ลดเวลา → ต้องเพิ่มทรัพยากร ลด Scope หรือเพิ่ม Risk
ลดงบ → ต้องลด Scope เปลี่ยน Approach หรือยอมรับ Constraint
```

### A12. Contract / SOW Preparation

SOW ควรมี:

- Deliverables
- Scope
- Milestones
- Acceptance Criteria / Acceptance Process
- Responsibilities
- Dependencies
- Payment Terms
- Change Control
- Warranty
- Support
- Intellectual Property
- Confidentiality
- Liability
- Termination
- Assumptions
- Exclusions

## A.8 Artifacts

| Artifact | Level |
|---|---|
| Opportunity Brief | R |
| Discovery Summary | M |
| Current-state Process | R |
| Problem Statement | M |
| Desired Outcomes / Success Measures | M |
| Assumption Log | M |
| Initial Stakeholder List | M |
| Solution Options | R |
| High-Level Scope | M |
| ROM Estimate | M |
| Initial Risk Register | M |
| Proposal | M สำหรับ Vendor Project |
| SOW / Contract | M สำหรับ External Customer |
| Bid / No-Bid Decision | R |

## A.9 Approval Gate

**Gate A: Commercial and Delivery Approval**

ต้องมีผู้อนุมัติ:

- CEO / Business Owner
- Delivery Owner
- Technical Authority
- Finance / Commercial
- Legal เมื่อจำเป็น

## A.10 Exit Criteria

ผ่านช่วง A เมื่อ:

- Business Need ถูกยืนยัน
- Proposed Solution มีเหตุผล
- Scope ระดับ Proposal ชัด
- Estimate มี Basis และ Assumptions
- Delivery Team ตรวจ Feasibility แล้ว
- Commercial Approval ผ่าน
- Contract / SOW หรือ Authorization พร้อม
- ไม่มีคำสัญญาสำคัญที่ไม่ถูกบันทึก

## A.11 Common Mistakes

- รับปากราคาและเวลาจากคำบอกเล่าครั้งแรก
- Estimate โดย PM คนเดียว
- ใช้ Prototype เป็น Commitment
- Proposal ไม่มี Out of Scope
- Timeline ไม่รวมเวลารอลูกค้า
- Proposal กับ SOW ขัดกัน
- Sales รับปาก Requirement นอกเอกสาร
- ไม่ระบุ Confidence ของ Estimate
- ไม่ตรวจ Team Capacity

---

# B. PROJECT INITIATION

## B.0 ใครทำอะไรในช่วงนี้

- **Accountable:** Project Sponsor
- **Process Owner:** Project Manager
- **Business Decision Owner:** Sponsor / Product Owner
- **Technical Decision Owner:** Tech Lead / Architect
- **Stakeholder Analysis Owner:** PM + BA

**เริ่มเมื่อ:** มี Commercial/Organizational Authorization  
**จบเมื่อ:** Charter ผ่าน, PM ได้รับอำนาจ, Governance และ Stakeholder สำคัญชัดเจน

### B.0.1 Action Flow

| Step | Responsible | Accountable | เมื่อไร/ที่ไหน | วิธีทำ | Output | ผู้รับช่วงต่อ |
|---|---|---|---|---|---|---|
| Internal Handover | Sales + PM | Delivery Owner | ก่อน Kickoff | Handover Workshop | Handover Record | PM ทำ Charter |
| Project Charter | PM | Sponsor | ก่อน Planning | Charter Workshop | Approved Charter | PM/BA Identify Stakeholders |
| Stakeholder Register | PM + BA | Sponsor | ก่อน Kickoff | Power/Interest Analysis | Register/Engagement Strategy | PM ตั้ง Governance |
| Governance | PM | Sponsor | ก่อน Kickoff | Decision/RACI Workshop | Decision Matrix, Escalation | PM เปิด RAID |
| Initial RAID | PM + Leads | Sponsor | ก่อน Kickoff | RAID Workshop | Initial RAID Log | Kickoff |
| Client Kickoff | PM | Sponsor | Kickoff Meeting | Facilitation | MoM, Actions, Confirmed Roles | Detailed Planning |


## B.1 Goal

สร้าง Authorization และ Governance อย่างเป็นทางการ เพื่อให้ทุกฝ่ายรู้ว่า:

- ทำโครงการนี้เพื่ออะไร
- ใครเป็น Sponsor
- ใครเป็น PM
- PM มีอำนาจระดับใด
- Scope ระดับสูงคืออะไร
- Success วัดอย่างไร
- ใครเป็น Stakeholder
- ใครตัดสินใจและอนุมัติ
- มี Risk ใหญ่ใด
- ใช้เงินและทรัพยากรภายใต้กรอบใด

## B.2 PMBOK Mapping

- Initiating Process Group
- Develop Project Charter
- Identify Stakeholders
- Integration Management
- Stakeholder Management
- Governance
- Value Alignment

## B.3 Entry Criteria

- Approved Business Case หรือ SOW
- Sponsor ถูกแต่งตั้ง
- Commercial Authorization
- Initial Funding / Budget Authority
- High-Level Scope
- Initial Timeline
- Initial Risks
- PM หรือ Delivery Owner

## B.4 Dependencies

ขึ้นกับ Output จาก A:

- Business Need
- Desired Outcome
- High-Level Scope
- Contract/SOW
- Assumptions
- Estimate
- Risk
- Stakeholders เบื้องต้น

## B.5 Methodology

- Sales-to-Delivery Handover
- Charter Workshop
- Stakeholder Analysis
- Power–Interest Analysis
- Governance Design
- RACI / Decision Rights
- Kickoff Facilitation
- Expert Judgment

## B.6 Step-by-Step Activities

### B1. Internal Sales-to-Delivery Handover

ตรวจ:

- ลูกค้าซื้ออะไร
- Proposal เวอร์ชันไหน
- SOW เวอร์ชันไหน
- Sales รับปากอะไร
- Estimate โดยใคร
- Assumptions ใด
- Margin
- Payment Milestones
- Risks
- Client Stakeholders
- Dependencies
- Resource Commitments

**Output:** Handover Record

### B2. Develop Project Charter

Project Charter ควรมี:

- Project Purpose
- Business Need
- Measurable Objectives
- Success Criteria
- High-Level Scope
- High-Level Requirements
- Major Deliverables
- Summary Milestones
- Initial Budget
- High-Level Risks
- Assumptions
- Constraints
- Sponsor
- PM
- PM Authority
- Governance
- Approval Requirements
- Exit Criteria
- Charter Approval

Charter ไม่ใช่ Detailed Plan

### B3. Identify Stakeholders

Stakeholder ไม่ได้มีเฉพาะผู้เข้าประชุม

ต้องพิจารณา:

- Sponsor
- Customer Product Owner
- Decision Maker
- End User
- Operations
- IT
- Security
- Legal
- Finance
- Vendor
- Regulator
- Support
- Management
- ผู้ได้รับผลกระทบทางลบ

### B4. Analyze Stakeholders

เก็บ:

- Role
- Interest
- Influence
- Impact
- Attitude
- Information Need
- Engagement Need
- Decision Right
- Acceptance Role
- Risk of Resistance

### B5. Establish Governance

กำหนด:

- Sponsor Decision
- Steering Committee
- Project Board
- PM Authority
- Product Owner Authority
- Technical Authority
- Change Authority
- Acceptance Authority
- Escalation Path
- Decision SLA
- Meeting Cadence

### B6. Initial RAID Setup

RAID:

- Risks
- Assumptions
- Issues
- Dependencies

ทุก Record ต้องมี:

- ID
- Description
- Owner
- Date
- Impact
- Response
- Due Date
- Status
- Escalation

### B7. Client Project Kickoff

Kickoff ต้องยืนยัน:

1. Business Objective
2. Scope / Deliverables
3. Out of Scope
4. Timeline / Milestones
5. Roles
6. Decision Rights
7. Communication
8. Working Approach
9. Dependencies
10. Risks
11. Change Process
12. Immediate Actions

## B.7 Artifacts

| Artifact | Level |
|---|---|
| Internal Handover Record | M |
| Project Charter / Authorization Evidence | M |
| Stakeholder Register | M |
| Stakeholder Engagement Strategy | M |
| Governance Model | M |
| RACI / Responsibility Matrix | R |
| Decision Authority Matrix | M |
| Initial RAID Log | M |
| Kickoff Deck | R |
| Meeting Minutes | M |
| Action Register | M |
| Decision Log | M |

## B.8 Approval Gate

**Gate B: Project Authorization**

ต้องได้รับ:

- Sponsor Approval
- Delivery Owner Acceptance
- PM Assignment
- Governance Confirmation
- High-Level Scope Confirmation

## B.9 Exit Criteria

- Project ถูก Authorize
- PM ได้รับอำนาจ
- Sponsor ชัดเจน
- Stakeholders สำคัญถูกระบุ
- Governance และ Escalation ชัด
- Kickoff Alignment แล้ว
- Initial RAID มี Owner
- ไม่มี Commercial Gap สำคัญที่ยังไม่จัดการ

---

# C. DETAILED PLANNING

## C.0 ใครทำอะไรในช่วงนี้

- **Accountable:** PM สำหรับ Integrated Plan; Sponsor สำหรับ Baseline Approval
- **Requirement Owner:** BA / Product Owner
- **Scope Owner:** PM + Product Owner
- **Schedule Owner:** PM / Planner
- **Cost Owner:** PM + Finance
- **Quality Owner:** QA Lead
- **Resource Owner:** Functional Managers / Delivery Lead
- **Technical Plan Owner:** Architect / Tech Lead
- **Release Owner:** DevOps / Release Manager

**เริ่มเมื่อ:** Charter และ Kickoff ผ่าน  
**จบเมื่อ:** Integrated Plan/Baselines ได้รับอนุมัติและทีม Ready for Execution

### C.0.1 Planning Action Flow

| Step | Responsible | Accountable | เมื่อไร/ที่ไหน | วิธีทำ | Output | ผู้รับช่วงต่อ |
|---|---|---|---|---|---|---|
| Tailor Approach | PM + Delivery Lead | Sponsor/Delivery Owner | ก่อน Planning | Tailoring Workshop | Delivery Approach | BA วาง Requirements Work |
| Plan/Elicit Requirements | BA + PM | Product Owner | Discovery Workshops | Interview, Workshop, Prototype | Validated Requirements | PM/BA Define Scope |
| Decide SRS/FSD Set | BA + PM | Product Owner/Contract Authority | หลังเห็น Complexity | Coverage Matrix | Document Set Decision | Scope Definition |
| Define Scope | BA + PM | Sponsor/PO | Scope Workshop | Boundary/Exclusion Analysis | Scope Statement | WBS/Backlog |
| WBS + Dictionary | PM + Leads | Sponsor/PM | Decomposition Workshop | 100% Rule | WBS, Dictionary, Scope Baseline | Define Activities |
| Quality/Acceptance | QA + BA | Acceptance Authority | พร้อม Requirement | Test Strategy Workshop | Criteria/Test Strategy | Activity Planning |
| Activities/Dependencies | Leads + Planner | PM | Schedule Workshop | Decomposition/Network | Activity List/Network | Estimate |
| Estimate | Functional Leads | Delivery Owner | Estimation Session | Bottom-up/Three-point | Effort/Duration/Cost Inputs | CPM/Schedule |
| Schedule/CPM | PM/Planner | Sponsor | หลัง Estimate | CPM/Float/Optimization | Schedule Baseline | Budget |
| Cost/Budget | PM + Finance | Sponsor/Commercial | หลัง Schedule | Cost Aggregation | Cost Baseline | Resource Commit |
| Resource/Communication/Risk | PM + Owners | Sponsor/Delivery Owner | ก่อน Gate | Capacity/Stakeholder/Risk Workshops | Subsidiary Plans | Integrate Plan |
| Release/Environment/Transition | DevOps + PM | Delivery Owner | ก่อน Build/Release | Readiness Planning | Release/Environment/Cutover Approach | Integrated Plan |
| Baseline Gate | PM นำเสนอ | Sponsor/CCB | ก่อน Execution | Formal Review | Approved Baselines | Execution |


# C0. Goal

เปลี่ยน High-Level Commitment ให้เป็นแผนที่ทีมสามารถลงมือทำ วัด ควบคุม และตรวจรับได้

Detailed Planning ไม่ได้หมายถึงต้องรู้ทุกอย่าง 100% ตั้งแต่วันแรก แต่ต้องมีระดับรายละเอียดที่เหมาะกับ Delivery Approach และ Risk

---

# C1. Tailor Delivery Approach

## Goal

เลือกวิธีบริหารและส่งมอบที่เหมาะสม ไม่ใช่เลือกตามความชอบของ PM

## Selection Factors

- Requirement Stability
- Technical Uncertainty
- Contract Type
- Regulatory Requirement
- Release Frequency
- Customer Availability
- Team Maturity
- Dependency
- Architecture
- Risk
- Need for Formal Approval

## Options

### Predictive

เหมาะเมื่อ:

- Scope ค่อนข้างชัด
- Formal Baseline สำคัญ
- Contract Fixed Scope
- Compliance สูง
- Change ต้องควบคุมเข้ม

### Agile / Adaptive

เหมาะเมื่อ:

- Requirement เปลี่ยนสูง
- Product Feedback สำคัญ
- ลูกค้ามีส่วนร่วมต่อเนื่อง
- ส่งมอบ Increment ได้
- Scope ปรับตาม Value

### Hybrid

เหมาะเมื่อ:

- Budget และ Milestones ต้องควบคุมแบบ Predictive
- Development ทำแบบ Iterative
- บาง Scope Fixed
- บาง Scope Flexible
- Governance เป็น Stage Gate แต่ Build เป็น Sprint

## Output

- Tailored Delivery Plan
- Lifecycle
- Phase / Release Model
- Governance Cadence
- Planning Horizon
- Change Approach
- Artifact Tailoring

---

# C2. Plan Requirements Work

## Goal

กำหนดว่า Requirement จะถูกเก็บ วิเคราะห์ ยืนยัน จัดลำดับ Trace และเปลี่ยนอย่างไร

## Activities

- ระบุ Requirement Sources
- ระบุ Stakeholders
- เลือก Elicitation Techniques
- กำหนด Requirement Types
- กำหนด Format
- กำหนด Review and Approval
- กำหนด Traceability
- กำหนด Change Control
- กำหนด Versioning

## Artifact

| Artifact | Level |
|---|---|
| Requirements Management Plan | M เป็นข้อมูล อาจรวมใน PM Plan |
| Elicitation Plan | R |
| Requirements Repository | M |
| Requirements Traceability Matrix | M/C |

---

# C3. Collect and Analyze Requirements

## Requirement Types

1. Business Requirements
2. Stakeholder Requirements
3. Solution Requirements
   - Functional
   - Non-functional
4. Transition Requirements
5. Data Requirements
6. Integration Requirements
7. Reporting Requirements
8. Security / Compliance Requirements
9. Operational Requirements
10. Acceptance Requirements

## Techniques

- Interview
- Workshop
- Observation
- Questionnaire
- Document Analysis
- Interface Analysis
- Process Modeling
- Prototyping
- Benchmarking
- Focus Group
- Story Mapping
- Use Case
- User Story
- Data Modeling

## As-Is to To-Be Flow

```text
As-Is
→ Pain Points
→ Root Causes
→ Business Rules
→ Constraints
→ To-Be Options
→ Selected To-Be
→ Requirements
→ Acceptance Criteria
```

## Requirement Quality Checklist

Requirement ต้อง:

- Clear
- Complete
- Consistent
- Feasible
- Testable
- Traceable
- Prioritized
- Unambiguous
- Necessary
- Owned

---

# C4. Requirement Documentation: SRS, FSD และเอกสารทดแทน

## C4.1 PMBOK บังคับ SRS หรือ FSD หรือไม่

ไม่บังคับชื่อเอกสาร

PMBOK สนใจว่า Requirement ถูก:

- Elicit
- Analyze
- Document
- Prioritize
- Approve
- Trace
- Validate
- Control

## C4.2 SRS

SRS = Software Requirements Specification

มักครอบคลุม:

- System Context
- Functional Requirements
- Non-functional Requirements
- Interfaces
- Data
- Constraints
- Security
- Acceptance
- Assumptions

**Level:** Conditional

ควรมีเมื่อ:

- Contract Formal
- ระบบซับซ้อน
- มีหลายทีม
- ต้อง Sign-off
- มี Compliance
- Requirement ต้อง Baseline

## C4.3 FSD

FSD = Functional Specification Document

มักครอบคลุม:

- Functional Behavior
- Process
- Business Rules
- Screen Behavior
- Validation
- Error Handling
- Data Mapping
- Interaction
- Exception Flow

**Level:** Conditional

### สามารถไม่ทำ FSD ได้เมื่อ

- SRS ครอบคลุม Functional Behavior
- User Stories มี Acceptance Criteria
- Process Flow แยกชัด
- Business Rules มี Catalogue
- UI Spec มี Annotation
- API Spec ครบ
- Data Dictionary ครบ
- RTM เชื่อม Requirement ไป Test
- Contract ไม่บังคับ FSD
- Dev และ QA มีแหล่งอ้างอิงเดียวกัน

### ห้ามตัด FSD โดยไม่มีสิ่งทดแทนเมื่อ

- Logic ซับซ้อน
- มีหลาย System
- ทีม Offshore / Vendor
- Formal Sign-off
- Audit
- Requirement ผูก Payment
- ลูกค้าระบุ FSD เป็น Deliverable

## C4.4 Document Substitution Matrix

| Coverage | เอกสารหลัก | เอกสารทดแทน |
|---|---|---|
| Business Need | BRD / Business Case | Project Charter / Discovery Summary |
| Functional Behavior | FSD | SRS / User Story / Use Case |
| Process | Process Spec | BPMN / Swimlane |
| Business Rules | Rule Catalogue | SRS / Story AC |
| UI Behavior | UI Spec | Annotated Wireframe / Design System |
| API | Interface Spec | OpenAPI / Swagger |
| Data | Data Spec | Data Dictionary / ERD |
| Acceptance | Acceptance Criteria | Test Case / UAT Scenario |
| Traceability | RTM | ALM Linkage |
| Technical Design | TDD / SDD | ADR / Architecture Docs |

---

# C5. Define Scope

## Goal

กำหนดขอบเขตสิ่งที่จะส่งมอบและงานทั้งหมดที่ต้องทำ

## Scope Components

- Product Scope
- Project Scope
- In Scope
- Out of Scope
- Deliverables
- Acceptance Criteria
- Constraints
- Assumptions
- Dependencies
- Boundaries

## Project Scope Statement

ควรมี:

- Product Scope Description
- Project Deliverables
- Acceptance Criteria
- Exclusions
- Constraints
- Assumptions

---

# C6. Create WBS and WBS Dictionary

## C6.1 Goal

แตก Total Project Scope เป็น Deliverable และ Work Package ที่สามารถ Estimate, Assign, Schedule, Cost และ Control ได้

## C6.2 Dependencies

ก่อนทำ WBS ต้องมี:

- Project Charter
- Requirements Documentation
- Project Scope Statement
- Deliverables
- Scope Boundaries
- Acceptance Information

## C6.3 Methodology

- Decomposition
- Expert Judgment
- Top-down
- Bottom-up
- Template
- Rolling Wave
- Workshop

## C6.4 Step-by-Step

1. ระบุ Final Product / Project
2. ระบุ Major Deliverables
3. เลือก Decomposition Logic
4. แตก Deliverables
5. ตรวจ 100% Rule
6. หยุดที่ Work Package
7. ระบุ Owner
8. สร้าง WBS Dictionary
9. ตรวจ Scope Coverage
10. Approve Scope Baseline

## C6.5 100% Rule

WBS ต้องครอบคลุมงานทั้งหมดที่อยู่ใน Project Scope และไม่รวมงานนอก Scope

ผลรวมของ Child Elements ต้องเท่ากับ 100% ของ Parent Element

## C6.6 Work Package

Work Package ต้องมีขนาดที่:

- Estimate ได้
- Assign Owner ได้
- วัด Progress ได้
- ระบุ Acceptance ได้
- Control ได้

## C6.7 WBS Dictionary อยู่ตรงไหน

WBS Dictionary อยู่ใน:

```text
Detailed Planning
→ Define Scope
→ Create WBS
→ Create WBS Dictionary
→ Approve Scope Baseline
```

## C6.8 WBS Dictionary Template Fields

| Field | Description |
|---|---|
| WBS ID | รหัส |
| Work Package | ชื่อ |
| Description | ขอบเขต |
| Deliverable | สิ่งส่งมอบ |
| Included Work | งานที่รวม |
| Excluded Work | งานที่ไม่รวม |
| Owner | ผู้รับผิดชอบ |
| Requirements | Requirement ที่เกี่ยวข้อง |
| Acceptance Criteria | เงื่อนไขผ่าน |
| Quality Criteria | มาตรฐานคุณภาพ |
| Assumptions | สมมติฐาน |
| Constraints | ข้อจำกัด |
| Dependencies | งานที่พึ่งพา |
| Milestone | Milestone |
| Resource | คน/ทักษะ |
| Estimate | Effort/Duration |
| Cost Account | Cost Control |
| Risk | ความเสี่ยง |
| Approval | หลักฐานอนุมัติ |

## C6.9 Scope Baseline

สำหรับ Predictive Scope Baseline ประกอบด้วย:

1. Project Scope Statement
2. WBS
3. WBS Dictionary

## C6.10 Agile Alternative

Agile อาจใช้:

- Product Goal
- Product Backlog
- Epic / Feature
- User Story
- Acceptance Criteria
- Release Boundary
- Definition of Done

แต่ยังต้องมี Scope / Value Boundary และ Traceability

---

# C7. Plan Quality and Acceptance

## Goal

กำหนดว่าความถูกต้องและคุณภาพจะพิสูจน์อย่างไร

## Components

- Quality Standard
- Acceptance Criteria
- Test Strategy
- Review Approach
- Verification
- Validation
- Defect Process
- Acceptance Authority
- Evidence

## Verification vs Validation

- Verification: สร้างถูกตาม Specification หรือไม่
- Validation: สิ่งที่สร้างตอบ Need และใช้ได้จริงหรือไม่

## Artifacts

- Quality Management Plan
- Test Strategy
- Acceptance Criteria
- Definition of Done
- Review Checklist
- RTM
- Quality Metrics

---

# C8. Define Activities

## Goal

เปลี่ยน Work Package เป็น Activities ที่ลงมือทำและ Schedule ได้

## Dependencies

- WBS
- WBS Dictionary
- Scope Baseline
- Delivery Approach

## Outputs

- Activity List
- Activity Attributes
- Milestone List

WBS ไม่ใช่ Activity List

ตัวอย่าง:

```text
Work Package: Payment Integration
Activities:
- Confirm payment provider
- Review API
- Design payment flow
- Implement API
- Handle callback
- Test payment
- Security review
```

---

# C9. Sequence Activities and Dependency Network

## Dependency Types

- Finish-to-Start
- Finish-to-Finish
- Start-to-Start
- Start-to-Finish

## Dependency Sources

- Mandatory
- Discretionary
- External
- Internal

## Lead and Lag

- Lead: เริ่มงานถัดไปก่อนงานก่อนหน้าจบทั้งหมด
- Lag: เวลารอระหว่างงาน

## Output

- Network Diagram
- Dependency Register
- Updated Activity Attributes

---

# C10. Estimate Effort, Resources and Duration

## แยกคำให้ชัด

- Effort = ปริมาณแรงงาน
- Duration = เวลาปฏิทิน
- Resource = คน / เครื่องมือ / Capacity
- Cost = มูลค่าเงิน

8 Person-days ไม่ได้แปลว่าใช้เวลา 8 วันเสมอไป

## Techniques

- Expert Judgment
- Analogous Estimating
- Parametric Estimating
- Three-point Estimating
- Bottom-up Estimating
- Planning Poker
- T-shirt Size
- Monte Carlo เมื่อจำเป็น

## Three-point

- Optimistic
- Most Likely
- Pessimistic

---

# C11. Develop Schedule and Critical Path Method (CPM)

## C11.1 CPM อยู่ตรงไหน

```text
Detailed Planning
→ Define Activities
→ Sequence Activities
→ Estimate Durations
→ Build Network Diagram
→ Apply CPM
→ Analyze Float
→ Optimize Schedule
→ Approve Schedule Baseline
```

## C11.2 Dependencies ก่อน CPM

ต้องมี:

- Activity List
- Dependencies
- Duration Estimates
- Calendar
- Constraints
- Milestones

## C11.3 CPM Terms

- ES: Early Start
- EF: Early Finish
- LS: Late Start
- LF: Late Finish
- Total Float
- Free Float
- Critical Path

## C11.4 Logic

Forward Pass:

```text
EF = ES + Duration
```

Backward Pass:

```text
LS = LF - Duration
```

Total Float:

```text
TF = LS - ES
หรือ
TF = LF - EF
```

Critical Path คือเส้นทางที่กำหนดระยะเวลาโครงการ และโดยทั่วไปมี Total Float ต่ำที่สุดหรือเป็นศูนย์ภายใต้เงื่อนไขของ Schedule Model

## C11.5 Example

| Activity | Duration | Predecessor |
|---|---:|---|
| A Requirements | 5 | - |
| B UX Design | 4 | A |
| C API Design | 3 | A |
| D Frontend Build | 6 | B |
| E Backend Build | 8 | C |
| F Integration Test | 4 | D,E |
| G UAT | 5 | F |

เส้นทาง:

- A-B-D-F-G = 5+4+6+4+5 = 24 วัน
- A-C-E-F-G = 5+3+8+4+5 = 25 วัน

Critical Path เบื้องต้นคือ A-C-E-F-G = 25 วัน

## C11.6 Schedule Optimization

- Fast Tracking
- Crashing
- Re-sequencing
- Scope Split
- Resource Adjustment
- Lead/Lag Review
- Phased Release

## C11.7 Schedule Baseline

Schedule Baseline ต้องได้รับ Approval และใช้เป็นฐานวัด Variance

---

# C12. Cost Estimate and Budget

## Components

- Labor Cost
- License
- Cloud
- Hardware
- Vendor
- Travel
- Training
- Contingency
- Reserve
- Tax
- Support

## Outputs

- Cost Estimates
- Basis of Estimates
- Project Budget
- Cost Baseline
- Funding Requirements
- Payment Milestones

---

# C13. Resource Planning

## Components

- Role
- Skill
- Quantity
- Availability
- Calendar
- Capacity
- Responsibility
- Training
- Onboarding
- Offboarding

## Artifacts

- Resource Management Plan
- Team Structure
- RACI
- Resource Calendar
- Capacity Plan

---

# C14. Communication and Stakeholder Engagement Planning

## Communication Plan

- Audience
- Information
- Purpose
- Format
- Frequency
- Owner
- Channel
- Escalation
- Confidentiality

## Typical Cadence

- Daily Team Sync
- Weekly Status
- Steering Committee
- Sprint Review
- Risk Review
- Architecture Review
- UAT Defect Review
- Go-live Command Center

---

# C15. Risk Planning

## Risk Process

1. Plan Risk Management
2. Identify Risks
3. Qualitative Analysis
4. Quantitative Analysis เมื่อจำเป็น
5. Plan Responses
6. Implement Responses
7. Monitor Risks

## Risk Fields

- ID
- Cause
- Risk Event
- Impact
- Probability
- Impact Rating
- Exposure
- Trigger
- Owner
- Response
- Contingency
- Residual Risk
- Status

## Risk vs Issue

- Risk: เหตุการณ์อาจเกิด
- Issue: เกิดแล้ว

---

# C16. Procurement and Vendor Planning

ใช้เมื่อมี:

- Outsourcing
- SaaS
- Hardware
- External API
- Consultant
- Data Provider
- Payment Provider

Artifacts:

- Procurement Strategy
- Make-or-Buy
- RFP/RFQ
- Vendor Evaluation
- Contract
- SLA
- Acceptance
- Payment Authorization

---

# C17. Release, Environment, Security and Transition Planning

## Environment Plan

- Development
- Test
- SIT
- UAT
- Staging
- Production
- DR

## Security

- Access
- Authentication
- Authorization
- Encryption
- Logging
- Vulnerability
- Privacy
- Backup
- Incident

## Transition

- Data Migration
- Training
- Cutover
- Support
- Operational Handover
- Rollback

---

# C18. Integrated Project Management Plan

ไม่ควรมอง Scope, Schedule, Cost, Quality และ Risk เป็นแผนแยกที่ไม่เกี่ยวกัน

Integrated Plan ต้องแสดง:

- Scope / Release
- Timeline
- Cost
- Resource
- Quality
- Risk
- Communication
- Procurement
- Change
- Transition
- Governance

---

# C19. Baseline Approval / Planning Gate

## Gate C: Ready for Execution

ต้องตรวจ:

- Requirements มีคุณภาพเพียงพอ
- Scope / Release Boundary ชัด
- WBS หรือ Backlog พร้อม
- Acceptance Criteria พร้อม
- Schedule / Release Plan พร้อม
- Resource ถูก Commit
- Cost Baseline พร้อม
- Risks มี Owner
- Client Dependencies ยืนยัน
- Environment Plan พร้อม
- Change Process พร้อม
- Governance พร้อม
- ทีมเห็นแผนเดียวกัน

---

# D. EXECUTION / SOLUTION DELIVERY

## D.0 ใครทำอะไรในช่วงนี้

- **Accountable:** Delivery Owner / PM ตาม Governance
- **Priority Owner:** Product Owner
- **Technical Owner:** Tech Lead
- **Quality Owner:** QA Lead
- **Work Owner:** Assigned Workstream Lead

| Action | Responsible | Accountable | เมื่อไร | Output | Next |
|---|---|---|---|---|---|
| Confirm Ready Work | PM/PO/Lead | PM | ก่อน Sprint/Work Package | Ready Work | Assign |
| Build/Configure | Delivery Team | Workstream Lead | ตาม Sprint/Schedule | Work Product | Review/Test |
| Peer Review | Team/SME | Tech Lead | ก่อน QA | Review Evidence | QA |
| Test | QA | QA Lead | Test Cycle | Test Evidence | Fix/Accept |
| Manage Blocker | PM + Owner | PM | Daily | Issue/Decision | Continue/Escalate |
| Produce Deliverable | Team | Lead | Milestone | Deliverable | Validate Scope |


## D.1 Goal

สร้าง Deliverables ตามแผน พร้อมบริหารทีม คุณภาพ ความรู้ Vendor และ Stakeholder

## D.2 PMBOK Mapping

- Executing Process Group
- Direct and Manage Project Work
- Manage Project Knowledge
- Manage Quality
- Acquire Resources
- Develop Team
- Manage Team
- Manage Communications
- Implement Risk Responses
- Conduct Procurements
- Manage Stakeholder Engagement

## D.3 Entry Criteria

- Project Authorized
- Execution Plan Approved
- Work Ready
- Team Available
- Environment Ready
- Inputs พร้อม
- Acceptance Criteria พร้อม

## D.4 Execution Flow

### Predictive

```text
Analyze → Design → Build → Test → UAT → Deploy
```

### Agile

```text
Refine → Plan Sprint → Build/Test → Review → Retrospective → Release
```

### Hybrid

```text
Fixed Milestones + Iterative Development + Formal Gates
```

## D.5 Step-by-Step

1. Confirm Work Package / Sprint Goal
2. Confirm Definition of Ready
3. Assign Work
4. Develop / Configure / Integrate
5. Perform Peer Review
6. Perform Testing
7. Update Progress
8. Manage Blockers
9. Capture Work Performance Data
10. Produce Deliverables
11. Review Deliverables
12. Submit for Validation / Acceptance
13. Capture Knowledge
14. Update Forecast

## D.6 Definition of Ready

งานควรมี:

- Purpose
- Scope
- Requirement
- Acceptance Criteria
- Dependencies
- Design / Decision
- Test Data
- Owner
- Estimate
- Priority

## D.7 Definition of Done

งานเสร็จเมื่อ:

- Build Complete
- Code Review
- Unit Test
- Integration Test
- Security Check
- Documentation
- Acceptance Criteria Pass
- Defect Threshold Met
- Deployed to Required Environment
- Evidence Captured

## D.8 Outputs

- Deliverables
- Work Performance Data
- Issue Updates
- Risk Updates
- Change Requests
- Quality Reports
- Knowledge Assets
- Procurement Outputs

---

# E. MONITORING, CONTROLLING AND CHANGE

## E.0 ใครทำอะไรในช่วงนี้

- **Accountable:** PM สำหรับ Control; Sponsor/CCB สำหรับ Baseline Change
- **Actual Data Owner:** Workstream Leads
- **Risk Owner:** เจ้าของ Risk แต่ละรายการ
- **Acceptance Owner:** Customer Acceptance Authority

| Action | Responsible | Accountable | ความถี่/สถานที่ | Output | Next |
|---|---|---|---|---|---|
| Collect Actuals | Team Leads | PM | Daily/Weekly PM Tool | Work Performance Data | Variance Analysis |
| Analyze/Forecast | PM/Planner | PM | Weekly Status | Variance/Forecast | Corrective Options |
| RAID Review | PM + Owners | Sponsor/PM | Weekly | Updated RAID | Response/Escalate |
| Change Intake | PM/BA | PM | เมื่อมี Request | Change Record | Impact Analysis |
| Impact Analysis | Relevant Leads | PM | ก่อน Decision | Impact Pack | CCB |
| Change Decision | CCB/Sponsor | Sponsor | Change Meeting | Decision Record | Update Baseline |
| Validate Scope | Customer + PM | Customer Authority | เมื่อ Deliverable พร้อม | Acceptance Evidence | Next/Close |


## E.1 Goal

วัดสิ่งที่เกิดขึ้นจริงเทียบกับแผน ตรวจ Variance คาดการณ์อนาคต และตัดสินใจปรับตัวอย่างมี Governance

## E.2 PMBOK Mapping

- Monitoring and Controlling Process Group
- Monitor and Control Project Work
- Perform Integrated Change Control
- Validate Scope
- Control Scope
- Control Schedule
- Control Costs
- Control Quality
- Control Resources
- Monitor Communications
- Monitor Risks
- Control Procurements
- Monitor Stakeholder Engagement

## E.3 Monitoring Cycle

```text
Collect Actual Data
→ Compare with Baseline
→ Analyze Variance
→ Forecast
→ Identify Cause
→ Develop Options
→ Decide
→ Implement Action
→ Verify Result
```

## E.4 Status Reporting

รายงานต้องตอบ:

- ตอนนี้อยู่ที่ไหน
- เทียบกับแผนเป็นอย่างไร
- อะไรเปลี่ยน
- ทำไม
- กระทบอะไร
- ต้องตัดสินใจอะไร
- ใครต้องทำอะไร
- ภายในเมื่อไร

## E.5 Change Control

### Change Flow

1. Submit Request
2. Log Change
3. Check Baseline
4. Clarify Request
5. Impact Analysis
6. Develop Options
7. Recommend
8. Change Authority Decision
9. Update Plan / Baseline
10. Communicate
11. Implement
12. Verify
13. Close Change

### Impact Areas

- Scope
- Schedule
- Cost
- Quality
- Resource
- Risk
- Contract
- Operation
- Benefits

### Change Authority

- PM อาจอนุมัติ Minor Change ภายใต้ Threshold
- Product Owner จัด Priority
- Sponsor / CCB อนุมัติ Baseline Change
- Commercial / Legal อนุมัติ Contract Change

## E.6 Schedule Control

- Actual Start/Finish
- Remaining Duration
- Critical Path
- Float
- Milestone Variance
- Forecast Finish
- Recovery Plan

## E.7 Cost Control and EVM

ตัวอย่าง Measures:

- PV: Planned Value
- EV: Earned Value
- AC: Actual Cost
- SV = EV - PV
- CV = EV - AC
- SPI = EV / PV
- CPI = EV / AC

ใช้เมื่อข้อมูลและ Governance เหมาะสม ไม่จำเป็นต้องบังคับทุกโครงการ

## E.8 Scope Validation vs Scope Control

- Validate Scope: ลูกค้า/Sponsor ตรวจรับ Deliverable
- Control Scope: ควบคุมการเปลี่ยน Scope Baseline

## E.9 RAID Management

Risk, Assumption, Issue และ Dependency ต้อง Review อย่างต่อเนื่อง ไม่ใช่สร้างครั้งเดียว

## E.10 Escalation

Escalate เมื่อ:

- เกินอำนาจ PM
- กระทบ Baseline
- ต้องการ Sponsor Decision
- Cross-project Conflict
- Contract Risk
- Security / Legal
- Critical Milestone
- Benefit at Risk

---

# F. VERIFICATION, UAT AND RELEASE READINESS

## F.0 ใครทำอะไรในช่วงนี้

- **Accountable Test Readiness:** QA Lead
- **Accountable Business Acceptance:** Product Owner / Customer Authority
- **UAT Responsible:** Business Users
- **Release Readiness Owner:** PM / Release Manager
- **Go/No-Go Authority:** Sponsor / Business Owner

| Action | Responsible | Accountable | เมื่อไร/ที่ไหน | Output | Next |
|---|---|---|---|---|---|
| Test Planning | QA Lead | QA Lead/PM | ก่อน Test | Test Plan | Prepare Env/Data |
| SIT/System Test | QA/Tech Teams | QA Lead | Test Environment | Test Results | Defect Triage |
| UAT Prepare | BA + QA + Users | Product Owner | ก่อน UAT | UAT Pack | UAT Execute |
| UAT Execute | Business Users | Acceptance Authority | UAT Environment | UAT Evidence | Sign-off/Fix |
| Defect Decision | QA+Tech+PO+PM | PO/QA Lead | Daily Triage | Fix/Defer/Waive | Readiness |
| Release Readiness | PM + Release Manager | Sponsor | Gate Review | Readiness Report | Go/No-Go |


## F.1 Goal

พิสูจน์ว่า Solution:

- ทำงานตาม Requirement
- มีคุณภาพ
- ปลอดภัย
- พร้อมใช้งาน
- ลูกค้ายอมรับ
- Operations พร้อมรับช่วง
- Go-live Risk อยู่ในระดับที่ยอมรับได้

## F.2 Test Levels

- Unit Test
- Component Test
- Integration Test
- System Test
- SIT
- Performance Test
- Security Test
- Regression Test
- UAT
- Production Verification

## F.3 QA vs UAT

QA/SIT พิสูจน์ Technical and Functional Correctness

UAT พิสูจน์ว่า Business User ยอมรับว่า Solution รองรับ Business Process และ Acceptance Criteria

UAT ไม่ควรใช้แทน System Test

## F.4 UAT Planning

ต้องมี:

- UAT Scope
- Participants
- Environment
- Data
- Scenarios
- Expected Result
- Entry Criteria
- Exit Criteria
- Defect Handling
- Sign-off Authority
- Schedule
- Evidence

## F.5 Requirements Traceability

RTM เชื่อม:

```text
Business Need
→ Requirement
→ Design
→ Build
→ Test Case
→ Test Result
→ Acceptance
```

## F.6 Defect Management

Defect ต้องมี:

- ID
- Description
- Environment
- Steps
- Expected
- Actual
- Severity
- Priority
- Owner
- Fix Version
- Retest
- Status

Severity ไม่เท่ากับ Priority

## F.7 Release Readiness

ตรวจ:

- Scope Complete
- Tests Pass
- Critical Defects Closed
- Security Accepted
- Performance Accepted
- Data Migration Tested
- Monitoring Ready
- Backup Ready
- Rollback Ready
- Training Complete
- Support Ready
- Communication Ready
- Approval Ready

## F.8 Go / No-Go

Decision Inputs:

- Business Readiness
- Technical Readiness
- Operational Readiness
- Security
- Data
- Defects
- Rollback
- Support
- Risk
- Stakeholder Approval

## F.9 Outputs

- Test Results
- UAT Sign-off
- Accepted Deliverables
- Known Issues
- Release Readiness Report
- Go/No-Go Decision
- Cutover Approval

---

# G. GO-LIVE AND HYPERCARE

## G.0 ใครทำอะไรในช่วงนี้

- **Accountable:** Business Owner / Sponsor
- **Cutover Owner:** Release Manager / PM
- **Deployment Owner:** DevOps / Tech Lead
- **Data Owner:** Data Lead
- **Business Validation:** Product Owner / Operations
- **Hypercare Owner:** Support Lead / PM

| Action | Responsible | Accountable | เมื่อไร/ที่ไหน | Output | Next |
|---|---|---|---|---|---|
| Cutover Readiness | PM + Release Team | Sponsor | ก่อน Window | Approved Cutover | Freeze/Backup |
| Deploy/Migrate | DevOps/Data | Tech Lead | Production Window | Deployment/Migration Evidence | Validate |
| Smoke/Business Check | QA + Business | Product Owner | หลัง Deploy | Validation Evidence | Enable Users |
| Monitor/Triage | Ops + Support + PM | Hypercare Owner | Hypercare Command Center | Incident/Status | Stabilize |
| Rollback | DevOps | Go-Live Authority | เมื่อ Trigger ถึง | Restored Service | Review/Replan |
| Exit Hypercare | Support + PM | Operations Owner | เมื่อ Criteria ผ่าน | Stabilization Acceptance | Closure/Handover |


## G.1 Goal

นำระบบเข้าสู่ Production อย่างควบคุมได้ ลดผลกระทบทางธุรกิจ และทำให้ระบบเข้าสู่สภาวะเสถียร

## G.2 Entry Criteria

- Go Decision
- Approved Cutover Plan
- Rollback Plan
- Production Access
- Data Ready
- Support Team Ready
- Monitoring Ready
- Communication Ready
- Owners Available

## G.3 Cutover Plan

ต้องระบุ:

- Task
- Sequence
- Start/End
- Owner
- Dependency
- Validation
- Decision Point
- Rollback Trigger
- Communication
- Evidence

## G.4 Deployment Steps

1. Freeze / Change Window
2. Backup
3. Deploy
4. Configure
5. Migrate Data
6. Reconcile Data
7. Smoke Test
8. Business Verification
9. Enable Users
10. Monitor
11. Communicate
12. Confirm Production Status

## G.5 Rollback Plan

ต้องตอบ:

- Rollback Trigger
- Who Decides
- Maximum Decision Time
- Backup Location
- Restore Steps
- Data Reconciliation
- Communication
- Business Continuity

## G.6 Hypercare

Hypercare คือช่วงสนับสนุนเข้มหลัง Go-live

ต้องมี:

- Command Center
- Support Hours
- Incident Priority
- Triage
- Technical Owners
- Business Owners
- Daily Review
- Metrics
- Exit Criteria

## G.7 Hypercare Metrics

- Incident Count
- Severity
- Response Time
- Resolution Time
- Transaction Success
- Error Rate
- Performance
- User Adoption
- Data Reconciliation
- Support Volume

## G.8 Stabilization Criteria

- ไม่มี Critical Incident ค้าง
- Error Rate อยู่ใน Threshold
- Performance Stable
- Business Transaction Correct
- Support Team รับช่วงได้
- Known Issues มี Plan
- Operations Accepts Handover

## G.9 Outputs

- Production Release
- Deployment Evidence
- Migration Reconciliation
- Incident Log
- Hypercare Report
- Stabilization Acceptance

---

# H. TRANSITION, CLOSURE AND BENEFIT HANDOVER

## H.0 ใครทำอะไรในช่วงนี้

- **Accountable:** Sponsor
- **Closure Coordinator:** PM
- **Operational Acceptance:** Operations Owner
- **Contract Closure:** Procurement/Legal/Finance
- **Benefit Owner:** Business Owner

| Action | Responsible | Accountable | เมื่อไร/ที่ไหน | Output | Next |
|---|---|---|---|---|---|
| Operational Handover | Leads + Support | Operations Owner | หลัง Stabilization | Accepted Handover Pack | Final Acceptance |
| Final Acceptance | PM + Customer | Acceptance Authority | เมื่อ Deliverables ครบ | Sign-off | Financial Closure |
| Contract/Finance Close | Finance/Procurement | Authorized Owner | หลัง Acceptance | Closed Contract/PO | Lessons |
| Lessons Learned | PM + Team | PM/Sponsor | ก่อน Release Team | Lessons Register | Improvement Actions |
| Benefit Handover | PM + Business Owner | Sponsor | ก่อน Closure | Benefit Plan | Post-project Review |
| Closure Report | PM | Sponsor | Closure Meeting | Approved Closure | Release Resources |


## H.1 Goal

ปิดภาระผูกพันทั้งหมด ส่งมอบให้ Operations ปิด Contract ปิดการเงิน เก็บบทเรียน และกำหนดผู้รับผิดชอบ Benefit ต่อ

## H.2 PMBOK Mapping

- Closing Process Group
- Close Project or Phase
- Final Transition
- Lessons Learned
- Procurement Closure
- Knowledge Transfer
- Benefits Handover

## H.3 Operational Handover

ต้องมี:

- System Ownership
- Support Model
- SLA
- Runbook
- Monitoring
- Incident Process
- Backup
- DR
- Access
- Vendor Contact
- Known Issues
- Maintenance

## H.4 Final Acceptance

ตรวจ:

- Contract Deliverables
- Acceptance Evidence
- Outstanding Items
- Waiver
- Warranty
- Payment
- Sign-off

## H.5 Contract and Financial Closure

- Final Invoice
- Payment
- Vendor Closure
- Asset Transfer
- License
- PO Closure
- Budget Reconciliation

## H.6 Lessons Learned

ควรเก็บ:

- What Worked
- What Did Not
- Root Causes
- Decisions
- Risk Outcomes
- Estimate Accuracy
- Stakeholder Lessons
- Technical Lessons
- Recommended Actions
- Owner for Improvement

## H.7 Benefit Handover

Project Output ไม่เท่ากับ Business Benefit

ต้องระบุ:

- Benefit Owner
- Benefit Measure
- Baseline
- Target
- Measurement Date
- Data Source
- Review Cadence

## H.8 Closure Report

- Objectives
- Scope Delivered
- Acceptance
- Schedule
- Cost
- Quality
- Risks
- Changes
- Benefits
- Outstanding
- Lessons
- Handover
- Final Approval

## H.9 Exit Criteria

- Deliverables Accepted
- Operations Handover Complete
- Support Ready
- Financial Closure
- Contract Closure
- Lessons Captured
- Resources Released
- Benefit Owner Assigned
- Sponsor Approves Closure

---


# 3.1 Quick Role-to-Action Reference

| Role | ต้องเริ่มเอง | ต้องร่วม | อนุมัติ/ตัดสินใจ |
|---|---|---|---|
| Sponsor | แต่งตั้ง PM, กำหนด Objective | Charter, Risk, Go-live | Charter, Baseline, Major Change, Closure |
| PM | นัด Session, Integrate Plan, Track, Escalate | ทุก Workstream | Minor Decision ตาม Authority |
| Product Owner | Prioritize, Clarify Value | Requirement, UAT, Release | Priority, Business Acceptance |
| BA | Elicit/Analyze/Document | Scope, UAT, Process | ไม่อนุมัติแทน Business Owner |
| Tech Lead | Technical Design/Estimate | Scope, Schedule, Change | Technical Direction |
| QA Lead | Test Strategy/Quality Evidence | Requirement, Release | Test Readiness |
| DevOps/Release | Environment/Deployment/Monitoring | Release/Cutover | Deployment Readiness |
| Finance/Commercial | Pricing/Cost/Margin | Proposal/Change | Commercial Approval |
| Legal/Procurement | Contract/Vendor Terms | Proposal/SOW/Change | Contract Approval |
| Operations | Support/Runbook/Handover | Cutover/Hypercare | Operational Acceptance |

# 4. Artifact Catalogue

| Artifact | Phase | Level |
|---|---|---|
| Opportunity Brief | A | R |
| Discovery Summary | A | M |
| Business Case | A/B | C/M |
| Proposal | A | M External |
| Contract / SOW | A | M External |
| Project Charter | B | M |
| Stakeholder Register | B | M |
| Governance Model | B | M |
| RACI | B/C | R |
| RAID Log | B–H | M |
| Requirements Management Plan | C | M as content |
| SRS | C | C |
| FSD | C | C |
| Process Flow | C | R/M |
| Business Rule Catalogue | C | C |
| Data Dictionary | C | C |
| API Specification | C | C |
| RTM | C–F | M/C |
| Project Scope Statement | C | M Predictive |
| WBS | C | M Predictive |
| WBS Dictionary | C | M when WBS used |
| Product Backlog | C/D | M Agile |
| Activity List | C | M Predictive |
| Dependency Network | C | M Predictive |
| CPM Analysis | C | C/M complex predictive |
| Schedule Baseline | C | M Predictive |
| Cost Baseline | C | M Predictive |
| Quality Plan | C | M as content |
| Test Strategy | C/F | M |
| Risk Register | B–H | M |
| Communication Plan | C | M as content |
| Resource Plan | C | M |
| Procurement Plan | C | C |
| Release Plan | C | M/C |
| Environment Plan | C | C/M Software |
| Change Log | E | M |
| Status Report | E | M |
| UAT Plan | F | M when UAT required |
| UAT Sign-off | F | M |
| Release Readiness | F | M |
| Cutover Plan | F/G | M Production |
| Rollback Plan | F/G | M Production |
| Hypercare Plan | G | C/M |
| Handover Pack | H | M |
| Closure Report | H | M |
| Lessons Learned | H | M |
| Benefits Handover | H | M |

---

# 5. Process-to-Artifact Index

## Scope

- Requirements Documentation
- Project Scope Statement
- WBS
- WBS Dictionary
- Scope Baseline
- Product Backlog
- RTM
- Acceptance Criteria
- Change Log

## Schedule

- Activity List
- Activity Attributes
- Milestone List
- Network Diagram
- Duration Estimates
- CPM
- Float Analysis
- Schedule Baseline
- Recovery Plan

## Cost

- Cost Estimate
- Basis of Estimate
- Budget
- Cost Baseline
- EVM Report

## Quality

- Quality Plan
- Test Strategy
- Checklist
- Test Cases
- Defect Log
- UAT
- Acceptance Evidence

## Resource

- Team Structure
- RACI
- Resource Calendar
- Capacity Plan
- Training Plan

## Risk

- Risk Management Approach
- Risk Register
- Response Plan
- Issue Log
- Contingency

---

# 6. Minimum Practical Pack by Project Size

## Small Project

- Charter / Authorization
- Stakeholder List
- Scope / Backlog
- Timeline
- RAID
- Acceptance Criteria
- Status
- UAT / Acceptance
- Go-live Checklist
- Handover

## Medium Project

เพิ่ม:

- Requirements Repository
- WBS / Release Plan
- Cost
- Resource Plan
- Communication
- Quality/Test Strategy
- Change Control
- Cutover
- Hypercare

## Large / Regulated Project

เพิ่ม:

- Formal Business Case
- Detailed SRS/FSD
- RTM
- Architecture
- Security/Privacy
- Procurement
- Quantitative Risk
- Formal Baselines
- Steering Governance
- Data Migration Rehearsal
- DR
- Audit Evidence

---

# 7. Final Readiness Checklist Before Execution

- [ ] Business Need ชัด
- [ ] Objective วัดได้
- [ ] Sponsor ชัด
- [ ] PM Authority ชัด
- [ ] Stakeholders ครบ
- [ ] Requirements มีคุณภาพ
- [ ] Scope / Release Boundary ชัด
- [ ] Out of Scope ชัด
- [ ] WBS หรือ Backlog พร้อม
- [ ] WBS Dictionary พร้อมเมื่อใช้ WBS
- [ ] Acceptance Criteria Testable
- [ ] Quality/Test Strategy พร้อม
- [ ] Activities / Dependency พร้อม
- [ ] CPM วิเคราะห์เมื่อเหมาะสม
- [ ] Schedule Baseline / Release Plan พร้อม
- [ ] Budget พร้อม
- [ ] Resource Commit พร้อม
- [ ] Risk มี Owner
- [ ] Communication พร้อม
- [ ] Change Control พร้อม
- [ ] Environment พร้อม
- [ ] Client Dependencies ยืนยัน
- [ ] Planning Gate Approved

---

# 8. Final Readiness Checklist Before Go-Live

- [ ] UAT Sign-off
- [ ] Critical Defects Closed
- [ ] Security Accepted
- [ ] Performance Accepted
- [ ] Data Migration Rehearsed
- [ ] Backup Confirmed
- [ ] Rollback Tested
- [ ] Monitoring Ready
- [ ] Support Ready
- [ ] Training Complete
- [ ] Communication Ready
- [ ] Cutover Owners Confirmed
- [ ] Go/No-Go Authority Available
- [ ] Hypercare Ready
- [ ] Business Owner Approves

---

# 9. Golden Rules for Project Managers

1. อย่ารับปากก่อนมี Basis
2. อย่า Estimate คนเดียว
3. อย่าเรียก Feature List ว่า Scope ที่ชัด
4. อย่าสร้าง WBS เป็น Timeline
5. อย่าทำ CPM ก่อน Dependency และ Duration พร้อม
6. อย่าคิดว่า SRS หรือ FSD สำคัญเพราะชื่อเอกสาร ให้ตรวจ Coverage
7. อย่าปล่อย Change ผ่านคำพูด
8. อย่ารอวันสุดท้ายจึง Validate Scope
9. อย่าใช้ UAT แทน QA
10. อย่าขึ้น Production โดยไม่มี Rollback
11. อย่าคิดว่า Go-live คือ Project Closure
12. อย่าปิด Project โดยไม่มี Operational Owner และ Benefit Owner
13. ทุก Assumption ต้องมี Validation Owner
14. ทุก Risk ต้องมี Owner
15. ทุก Action ต้องมี Due Date
16. ทุก Decision สำคัญต้องมี Evidence
17. ทุก Baseline Change ต้องผ่าน Authority
18. ทุก Artifact ต้องมี Purpose ไม่ใช่สร้างเพื่อให้ครบ Template
19. เมื่อข้อมูลใหม่เกิดขึ้น ให้ Replan อย่างมี Governance
20. PM มีหน้าที่ Integrate ไม่ใช่ทำแทนผู้เชี่ยวชาญทุกคน

---

# 10. Recommended Tool Mapping

| Need | Possible Tools |
|---|---|
| Requirements | Jira, Azure DevOps, Confluence |
| WBS | Excel, Miro, MS Project, WBS Tool |
| Schedule / CPM | MS Project, Primavera, Smartsheet |
| Backlog | Jira, Azure DevOps |
| Documentation | Confluence, Notion, SharePoint |
| RAID | Spreadsheet, Jira, PM Tool |
| Communication | Teams, Slack, Email |
| Design | Figma |
| API | Swagger / OpenAPI |
| Test | TestRail, Jira, Azure Test Plans |
| CI/CD | GitHub Actions, GitLab CI, Azure DevOps |
| Monitoring | Cloud Monitoring, APM, Logs |
| Decision Log | Confluence, ADR Repository |

เครื่องมือไม่สามารถทดแทน Governance และ Professional Judgment ได้

---

# 11. Source Notes

- PMI PMBOK® Guide — Eighth Edition และ The Standard for Project Management
- PMI Process Groups: A Practice Guide
- PMI Practice Standard for Work Breakdown Structures — Third Edition
- PMI Business Analysis for Practitioners: A Practice Guide — Second Edition
- PMI Agile Practice Guide
- PMBOK-Masterclass Repository: Course Roadmap, Artifact Dependency Map และ Lessons 02–16

Official PMI pages:

- https://www.pmi.org/standards/pmbok
- https://www.pmi.org/standards/process-groups
- https://www.pmi.org/standards/work-breakdown-structures-third-edition
- https://www.pmi.org/standards/business-analysis-second-edition

---

# 12. Closing Statement

คู่มือนี้ควรถูกใช้เป็น Baseline ไม่ใช่ Checklist ที่บังคับทุกโครงการเหมือนกัน

ก่อนเริ่มทุกโครงการ PM ต้อง Tailor:

- Process
- Artifact
- Governance
- Level of Detail
- Delivery Approach
- Approval
- Reporting
- Quality
- Risk

โดยพิจารณาจาก Value, Complexity, Risk, Contract, Stakeholders, Team Capability และ Compliance

เป้าหมายสุดท้ายไม่ใช่ “มีเอกสารครบ” แต่คือ:

> ทีมเข้าใจตรงกัน ตัดสินใจบนข้อมูล สร้างสิ่งที่ตอบ Business Need ควบคุมความเสี่ยง ตรวจรับได้ ส่งมอบได้ และสร้าง Benefit หลังโครงการจบ

---
title: "Appendix A — Artifact Catalogue"
book: "PM Delivery Guide"
document_type: Appendix
version: 1.0
status: Released
last_reviewed: 2026-08-13
related_reference: ../../references/PMBOK-Overview.md
---

# Appendix A — Artifact Catalogue (Lookup Table)

> ใช้เป็นตาราง lookup: ต้องการหลักฐานอะไร → ดูว่าอยู่ช่วงไหน (A–H) ใครเป็นเจ้าของ และจำเป็นระดับไหน (M = Mandatory, C = Conditional, R = Recommended, O = Optional) — "Mandatory" หมายถึงเนื้อหา/หลักฐานต้องมี ไม่จำเป็นต้องเป็นไฟล์ชื่อนั้น (Playbook §2.1)

## A.1 Artifact ตามช่วง A–H

| Artifact | Phase | Level | Owner หลัก | ใช้ทำอะไรต่อ |
|---|---|---|---|---|
| Opportunity Brief | A | R | Sales/Opportunity Owner | ตั้งต้น Discovery |
| Discovery Summary | A | M | PM + BA | basis ของ Proposal |
| Problem Statement | A | M | PM + BA | ผูก Business Need |
| Desired Outcomes / Success Measures | A | M | Customer Sponsor | วัด value (35% direct ใน 18 เดือน) |
| Assumption Log | A–H | M | PM | ฐานของ risk/change |
| Initial Stakeholder List | A | M | PM | ต่อยอด Register (Ch.2) |
| Solution Options | A | R | Architect + BA | เลือก approach |
| High-Level Scope | A | M | PM | Proposal In/Out of Scope |
| ROM Estimate | A | M | Functional Leads | ตั้งราคา/ตัดสินใจ Bid |
| Initial Risk Register | A | M | PM | ต่อยอด Risk (Ch.5) |
| Proposal | A | M (External) | PM + Sales | สัญญา/ลูกค้า review |
| SOW / Contract | A | M (External) | Legal + PM | Authorization (Ch.2) |
| Bid / No-Bid Decision | A | R | CEO/Commercial | decision record |
| Project Charter | B | M | Sponsor | อำนาจ PM + ทิศทาง |
| Stakeholder Register + Engagement Strategy | B | M | PM + BA | engagement + requirement (Ch.3) |
| Governance Model / Decision Rights | B | M | PM + Sponsor | ใครตัดสินใจอะไร |
| RACI | B/C | R | PM + Leads | clarity บทบาท |
| RAID Log | B–H | M | PM | ต่อเนื่องทุกช่วง |
| Kickoff Deck + MoM | B | R/M | PM | alignment + actions |
| Requirements Management Plan | C | M (as content) | BA + PM | วิธีเก็บ/อนุมัติ/trace |
| SRS / FSD (หรือสิ่งทดแทน) | C | C | BA | coverage ของ requirement |
| RTM | C–F | M/C | BA + QA | requirement→test→acceptance |
| Project Scope Statement | C | M (Predictive) | PM + PO | boundary |
| WBS + WBS Dictionary | C | M (Predictive) | PM + Leads | schedule/cost/resource (Ch.4) |
| Product Backlog | C/D | M (Agile) | PO | sprint delivery |
| Activity List + Dependency Network | C | M (Predictive) | PM + Planner | CPM/baseline |
| Schedule Baseline | C | M (Predictive) | PM | วัด variance (Ch.7) |
| Cost Baseline | C | M (Predictive) | PM + Finance | EVM/control (Ch.7) |
| Quality Plan / Test Strategy | C/F | M | QA Lead + PM | **วางแผนไว้ Ch.5, ผลจริง Ch.8** |
| Risk Register + Response Plan | B–H | M | Risk Owners | monitor/implement (Ch.6–7) |
| Communication Plan | C | M (as content) | PM | สื่อสารทุกช่วง |
| Resource Plan | C | M | PM + Functional Mgrs | capacity/sign-off |
| Procurement Plan | C | C | Procurement Mgr | vendor/contract |
| Release / Environment Plan | C | M/C | DevOps + PM | rollout (Ch.9) |
| Change Log + Decision Record | E | M | PM/CCB | baseline update |
| Status Report | E | M | PM | สถานะ/decision ask |
| UAT Plan + UAT Sign-off | F | M | QA + PO | acceptance evidence |
| Release Readiness Report | F | M | PM + Release Mgr | Go/No-Go |
| Cutover Plan + Rollback Plan | F/G | M (Production) | Release Mgr + DevOps | Go-Live (Ch.9) |
| Hypercare Plan + Report | G | C/M | Support + PM | stabilization |
| Handover Pack | H | M | Leads + Support | Ops รับช่วง |
| Closure Report | H | M | PM | Sponsor อนุมัติปิด |
| Lessons Learned | H | M | PM + Team | องค์กรเรียนรู้ |
| Benefit Handover Plan | H | M | PM + Business Owner | วัด 35% หลังปิด |

## A.2 Index ตามเรื่อง (Process-to-Artifact สรุปจาก Playbook §5)

| เรื่อง | Artifact หลัก |
|---|---|
| Scope | Requirements, Scope Statement, WBS + Dictionary, Scope Baseline, Backlog, RTM, Acceptance Criteria, Change Log |
| Schedule | Activity List, Dependency Network, CPM, Float, Schedule Baseline, Recovery Plan |
| Cost | Cost Estimate, Basis of Estimate, Budget, Cost Baseline, EVM Report |
| Quality | Quality Plan, Test Strategy, Checklist, Test Cases, Defect Log, UAT, Acceptance Evidence |
| Resource | Team Structure, RACI, Resource Calendar, Capacity Plan, Training Plan |
| Risk | Risk Approach, Risk Register, Response Plan, Issue Log, Contingency |

## A.3 Minimum Practical Pack ตามขนาดโครงการ (Playbook §6)

| ขนาด | ต้องมี |
|---|---|
| Small | Charter, Stakeholder List, Scope/Backlog, Timeline, RAID, Acceptance Criteria, Status, UAT/Acceptance, Go-live Checklist, Handover |
| Medium | + Requirements Repository, WBS/Release Plan, Cost, Resource Plan, Communication, Quality/Test Strategy, Change Control, Cutover, Hypercare |
| Large/Regulated | + Formal Business Case, Detailed SRS/FSD, RTM, Architecture, Security/Privacy, Procurement, Quantitative Risk, Formal Baselines, Steering Governance, Data Migration Rehearsal, DR, Audit Evidence |

> หลักการ: ทุก Artifact ต้องมี Purpose และ Owner — ห้ามสร้างเพื่อให้ครบ Template (Golden Rule #18)

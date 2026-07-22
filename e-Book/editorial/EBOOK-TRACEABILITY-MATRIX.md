---
title: E-book Traceability Matrix
document_type: E-book Editorial Control
status: Active
created_on: 2026-07-22
---

# E-book Traceability Matrix

## End-to-End Learning Spine

```text
Business Need -> Objective -> Requirement -> Scope -> WBS
-> Activity -> Schedule -> Cost -> Quality -> Risk
-> Acceptance -> Handover -> Benefit
```

## Artifact Chain

| From | Artifact output | Feeds |
|---|---|---|
| L01 | PM Learning Baseline | L02 evidence gaps and value assumptions |
| L02 | Project vs Operation Analysis and Value Chain | L03 lifecycle mapping and L05 business case context |
| L03 | Lifecycle and Process Group Map | L04 cross-impact analysis and L05 governance flow |
| L04 | PM Coverage and Cross-impact Map | L05 decision rights and change route |
| L05 | Project Charter, Governance and Decision Rights Map, Change Decision Record | L06 stakeholder engagement and downstream baseline control |
| L06 | Stakeholder Register and Engagement Strategy | L07 requirements source, influence and acceptance roles |
| L07 | Requirements List, Scope Statement, WBS and WBS Dictionary | L08 schedule logic, L09 cost basis and L10 acceptance/testing basis |
| L08 | Activity List, Dependency Network and Master Schedule | L09 time-phased cost and L10 quality gate planning |
| L09 | Cost Estimate, Cost Baseline and Cost Performance Forecast | L10 quality budget and financial control decisions |
| L10 | Quality Plan, Acceptance Criteria and Test Strategy | L11 resource and RACI planning |
| L11 | Consolidated Resource Plan, Organization Chart and RACI | L12 communication audiences, cadence and escalation accountability |
| L12 | Communication Plan, Cadence and Status Report | L13 risk signals, escalation evidence and decision timing |
| L13 | Risk Register, Response Plan and Issue Log | L14 procurement risk allocation and vendor change control |
| L14 | Procurement Plan, Vendor Evaluation and Contract Control Record | L15 delivery constraints and acceptance/payment evidence |
| L15 | Product Backlog, Sprint/Flow Board and Feedback Evidence | L16 tailoring context, flow evidence and release decision |
| L16 | Tailored Hybrid Delivery Plan | Capstone launch, handover and benefit-readiness decision |

## Traceability Rules

- Output from the prior chapter must reach at least `Usable` before it can become input to the next chapter.
- Every artifact must identify creator, owner, reviewer, approval authority and approval evidence.
- New objectives, scope, budget, timeline or scenario facts require an approved change route outside the e-book chapter.
- Capstone must link to canonical lesson artifacts rather than copy or recreate them.

## Validation Evidence Sources

| Evidence | Source |
|---|---|
| Course standard and release gate | `governance/COURSE_STANDARD.md` |
| Execution baseline | `governance/EXECUTION-BASELINE.md` |
| Artifact chain | `governance/ARTIFACT_DEPENDENCY_MAP.md` |
| Batch 1 integration | `repository/BATCH-1-INTEGRATION-REVIEW.md` |
| Batch 2 integration | `repository/BATCH-2-INTEGRATION-REVIEW.md` |
| Batch 3 integration | `repository/BATCH-3-INTEGRATION-REVIEW.md` |
| Final repository validation | `repository/FINAL-VALIDATION-REPORT.md` |
| Capstone gates | `repository/CAPSTONE-GATE-REPORT.md` |


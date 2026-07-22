---
title: ERP Transformation — End-to-End PM Walkthrough
document_type: Teaching Walkthrough
scenario_source: ./ERP-TRANSFORMATION-CASE.md
status: Draft
version: 1.0
last_updated: 2026-07-22
---

# ERP Transformation — End-to-End PM Walkthrough

## Purpose

This walkthrough teaches how a PM would run the ERP Transformation case from business need to post go-live operation. It is a teaching guide, not a real project prescription.

Use this together with [ERP Transformation Scenario Master](./ERP-TRANSFORMATION-CASE.md).

## Case Baseline

- Sponsor: คุณสมชาย, CEO
- PM: คุณเอก
- SI: TechConsult
- Scope: FI, SD, MM, PP, HCM
- Data migration: 6 legacy systems
- Users: 80 key users
- Timeline: about 12 months
- Go-live constraint: before 1 October
- Working Budget: 45 ล้านบาท for delivery/implementation costs
- Total Funding Envelope: 60 ล้านบาท including license and management reserve

## Step 1 — Confirm Business Need and Value

The PM starts by translating the executive request into business value.

Decision questions:

1. What business problem is ERP solving?
2. Which outcomes prove the project worked?
3. Who owns the outcomes after go-live?

Expected outputs:

- Business need statement
- Initial benefits map
- Outcome metrics: close period from 15 days to 5 days, 80% transactions through ERP after 3 months, real-time dashboard usage

PM judgement:

Do not say “ERP go-live” is the value. Go-live is an output. Faster close, better data consistency, and real-time visibility are outcomes.

## Step 2 — Initiate the Project

The PM prepares the project for formal authorization.

Actions:

1. Draft project charter
2. Confirm sponsor and PM authority
3. Identify steering committee
4. Confirm high-level scope, constraints, assumptions, risks, and budget vocabulary
5. Create stakeholder register

Expected outputs:

- Approved project charter
- Initial stakeholder register
- Initial risk register
- Governance cadence: steering committee every 2 weeks

Decision gate:

The project should not move into detailed planning until sponsor authority, scope boundaries, timeline constraint, and budget terms are clear.

## Step 3 — Plan the Delivery Approach

ERP should be managed as a hybrid project.

Predictive controls:

- Charter and baselines
- Scope and WBS
- Master schedule
- Working budget
- Procurement and vendor milestones
- Cutover and go-live readiness

Agile or iterative practices:

- Prototype reports
- Kanban for SIT defects and data cleansing issues
- Short-cycle UAT feedback
- Daily standup for critical workstreams

Expected outputs:

- Project management plan
- Tailoring rationale
- Governance model
- Change control process

PM judgement:

Calling the project “Agile” does not remove governance. ERP has high integration, data, compliance, and go-live risk, so predictive controls remain necessary.

## Step 4 — Build Scope Baseline and WBS

The PM converts objectives into controlled work.

Actions:

1. Confirm in-scope and out-of-scope items
2. Break work into WBS
3. Create WBS dictionary and acceptance criteria
4. Confirm scope baseline
5. Define change control rules

Example WBS areas:

- Project management and governance
- Business process blueprint
- FI, SD, MM, PP, HCM configuration
- Data migration
- Integrations: banking, e-Tax, TMS
- Testing: SIT, UAT, regression
- Training and change management
- Cutover and go-live
- Hypercare and transition to operation

Decision gate:

Any new dashboard, report, workflow, or module request must be checked against the scope baseline before approval.

## Step 5 — Build Schedule Baseline

The PM turns WBS into activity logic.

Actions:

1. Define activities from work packages
2. Sequence dependencies
3. Estimate durations
4. Identify critical path
5. Set milestones
6. Build schedule baseline

Key dependency logic:

- Data cleansing must precede final migration
- Configuration must precede SIT
- SIT must precede UAT
- UAT sign-off must precede cutover
- Cutover readiness must precede go-live

Decision gate:

If data cleansing slips and sits on the critical path, PM must create a recovery plan using crashing, fast tracking, scope trade-off, or escalation.

## Step 6 — Build Cost Baseline and Controls

The PM must protect the locked budget vocabulary.

Actions:

1. Estimate costs by work package
2. Confirm cost baseline and reserves
3. Separate working delivery budget from total funding envelope
4. Define cost reporting cadence
5. Use EVM where work completion can be measured

Budget rule:

- Working Budget 45 ล้านบาท is the delivery control budget
- Total Funding Envelope 60 ล้านบาท is not a free extension of delivery budget

Decision gate:

If forecast delivery cost threatens 45 ล้านบาท, PM must escalate with EAC, root cause, options, and reserve implications.

## Step 7 — Procure and Control the SI

TechConsult must be controlled through contract, deliverables, and acceptance evidence.

Actions:

1. Confirm contract type and scope
2. Set milestone payments by accepted deliverables
3. Define change order process
4. Track named resources and consultant quality
5. Review vendor performance at each milestone

Milestone examples:

- Kickoff
- Blueprint
- Build
- SIT
- UAT
- Go-live

Decision gate:

Do not approve vendor payment only because time passed. Payment should follow accepted deliverables.

## Step 8 — Manage Stakeholders and Key Users

ERP value depends on people changing how they work.

Actions:

1. Map power and interest
2. Create key-user engagement plan
3. Secure functional manager commitment
4. Track UAT participation
5. Create change champions
6. Monitor resistance and readiness

Critical stakeholder risks:

- Key users cannot give 40% time
- Operations resist new workflow
- Data owners do not accept ownership
- Functional managers prioritize daily work over project work

Decision gate:

If key-user participation drops, PM must escalate capacity impact before UAT quality collapses.

## Step 9 — Execute Build, Data, Integration, and Testing

The PM coordinates workstreams and controls evidence.

Actions:

1. Run configuration and development
2. Execute data cleansing
3. Perform mock migration
4. Run SIT
5. Run UAT with process owners
6. Track defects by severity and owner
7. Manage approved change requests

Quality gates:

- Data migration quality gate
- SIT pass criteria
- UAT sign-off
- Performance and integration readiness
- Training completion

Decision gate:

Critical defects in finance close, migration accuracy, or integration should block go-live until resolved or formally accepted with risk ownership.

## Step 10 — Control Risks, Issues, and Changes

Risk management must be live throughout delivery.

Actions:

1. Review top risks every governance cycle
2. Track triggers
3. Convert triggered risks into issues
4. Activate response plans
5. Run integrated change control
6. Update baseline only after approval

Common ERP risks:

- Data quality
- Key-user availability
- Scope creep
- Vendor resource mismatch
- User resistance
- Go-live delay

Decision gate:

Every change request must show impact on scope, schedule, cost, quality, risk, resource, stakeholder, procurement, and integration.

## Step 11 — Prepare Cutover and Go-live

Go-live is not a date. It is a readiness decision.

Actions:

1. Confirm cutover plan
2. Confirm rollback plan
3. Validate data migration
4. Confirm training completion
5. Confirm support model
6. Confirm business owner sign-off
7. Conduct go/no-go meeting

Go/no-go evidence:

- UAT signed
- Critical defects closed
- Data reconciliation accepted
- Support team ready
- Business process owners ready
- Vendor hypercare ready

Decision gate:

If readiness evidence is incomplete, PM should not hide it behind green status. Present go-live, delay, partial go-live, or rollback options.

## Step 12 — Hypercare and Transition to Operation

The project closes only after controlled transition.

Actions:

1. Run hypercare for 3 months
2. Track incidents by severity and process
3. Transfer knowledge to application support
4. Confirm process owners
5. Move enhancement requests to CAB
6. Measure early adoption and transaction use

Expected outputs:

- Hypercare reports
- Support handover
- Lessons learned
- Closure report

Decision gate:

Do not close only because the system is live. Close when support ownership, knowledge transfer, and acceptance are complete.

## Step 13 — Benefits Review

Value is measured after go-live.

Actions:

1. Review 3-month adoption
2. Review 6-month close cycle
3. Review 12-month dashboard usage
4. Compare benefits against baseline
5. Decide enhancement backlog

Outcome checks:

- ≥80% transactions through ERP after 3 months
- Close period ≤5 working days after 6 months
- Dashboard used by executives after 12 months

PM handoff:

After closure, outcome ownership moves to process owners, IT operations, and business leadership.

## End-to-End Teaching Flow

| Stage | PM Focus | Key Decision |
|---|---|---|
| Business Need | Value and outcome | Is ERP the right investment? |
| Initiation | Authority and governance | Is the project formally authorized? |
| Planning | Scope, schedule, cost, quality, risk | Is the baseline credible? |
| Procurement | Vendor control | Does the contract support delivery and acceptance? |
| Execution | Build, data, testing | Is work producing accepted deliverables? |
| Monitoring | Variance, risk, change | What needs recovery or approval? |
| Go-live | Readiness | Go, no-go, delay, or partial release? |
| Hypercare | Stabilization | Is operation ready to own the system? |
| Benefits | Outcome | Did ERP create business value? |

---
chapter: lesson-03
title: 5 Project Management Process Groups
edition: Instructor
status: Ready for Human Review
source_lesson: ../../../lessons/lesson-03/
learner_chapter: ./lesson-03-learner.md
---

# Instructor Guide — Chapter 03: 5 Project Management Process Groups

## Teaching Notes

บทนี้ต้องแก้ misconception ใหญ่: Process Groups ไม่ใช่ waterfall phases ที่ห้ามย้อนกลับ แต่เป็น management functions ที่ PM activate ตาม evidence, decision และ control needs

ลิงก์ไป Learner Chapter: [lesson-03-learner.md](./lesson-03-learner.md)

## Learning Intent

ผู้เรียนควรมอง 5 Process Groups เป็นภาษาในการตัดสินใจ:

- Initiating: authority และ objective ชัดหรือยัง
- Planning: baseline และ approach พร้อมหรือยัง
- Executing: deliverable ถูกสร้างอย่างไร
- Monitoring & Controlling: evidence บอก variance/decision อะไร
- Closing: acceptance, handover และ benefits ownership พร้อมหรือยัง

บทนี้รับ input จาก Lesson 02 และส่ง output ไป Lesson 04 เพื่อทำ cross-impact map

## Suggested Timing

| Segment | Time |
|---|---|
| Lesson 02 handoff review | 5 minutes |
| Process Groups vs phases | 15 minutes |
| Five Process Groups overview | 20 minutes |
| Feedback loop and replanning | 20 minutes |
| ERP worked example | 15 minutes |
| Hotel contrast | 10 minutes |
| Workshop and artifact review | 30 minutes |

Total suggested facilitation time: 115 minutes.

## Thinking Walkthrough

### Step 1: Use Lesson 02 Boundary

Do not let learners invent a new objective. Start from the approved Project vs Operation Analysis and Value Chain: project boundary, expected outcome and transition point.

### Step 2: Design Lifecycle Phases

Phases should reflect delivery lifecycle, such as Initiation, Blueprint, Build/Migration, SIT/UAT and Cutover/Hypercare. Do not name all phases after Process Groups.

### Step 3: Map Process Groups Across Phases

Planning and Monitoring should appear repeatedly. Executing and Monitoring & Controlling should pair around real evidence, such as test defects or migration reconciliation.

### Step 4: Define Replanning Triggers

Triggers must be evidence-based: data quality below threshold, UAT capacity missing, payment failure above limit, readiness metric not met or baseline impact confirmed.

### Step 5: Close With Transition

Closing includes acceptance, open-item ownership, handover, contract/admin closure and benefits review. It is not only a lessons learned meeting.

## Completed Example

### ERP Selected Lifecycle

| Phase | Exit evidence | Gate |
|---|---|---|
| Initiation | Approved Charter | Sponsor authorizes project |
| Blueprint | Approved future-state process and requirements | Design approval |
| Build and Migration Cycles | Configured increment and reconciled migration result | Cycle acceptance |
| SIT/UAT | Test evidence and accepted residual defects | Go-live recommendation |
| Cutover/Hypercare | Stable operation and transferred open items | Handover approval |

### Process Group Interaction

- Initiating confirms authorization and key stakeholders
- Planning occurs initially and again after design or migration evidence
- Executing produces configuration, migration, training and test work
- Monitoring & Controlling compares evidence with baselines throughout execution
- Closing occurs at phase gates and final transition, not only at the last meeting

### Feedback Example

Migration reconciliation below threshold triggers issue analysis and replanning of cleansing, retest, schedule and cost forecast before the next cycle.

## Model Answer

A professional answer separates ERP delivery phases from 5 Process Groups and shows that Planning, Executing and Monitoring & Controlling occur repeatedly in Blueprint, Build/Migration and Test.

Data cleansing rules that are not confirmed are planning/evidence gaps. Starting a prototype is executing activity. Prototype results must be monitored and used to replan rather than used as a reason to skip approval gates.

Closing must include acceptance, handover, unresolved-item ownership and benefits review, not only a lessons learned session.

Alternative lifecycles are acceptable when they use the Lesson 02 boundary, include feedback loops and identify gate evidence and authority clearly.

## Review Checklist

- [ ] Uses Business Need and boundary from Lesson 02
- [ ] Phases are not simply the five Process Groups
- [ ] Planning and Monitoring recur based on evidence
- [ ] Executing links to monitoring signals
- [ ] Replanning triggers are clear
- [ ] Gates have exit evidence and approval authority
- [ ] Closing includes transition and benefits handoff
- [ ] Output can feed Lesson 04 Cross-impact Map

## Scoring Rubric

| Dimension | Incomplete | Usable | Professional |
|---|---|---|---|
| Phase/Process distinction | Mixes them | Separates them | Explains Process Groups recurring across phases |
| Flow | Linear only | Has feedback/replanning | Has trigger, owner and evidence update |
| Governance | No gate | Gate/evidence present | Authority and threshold clear |
| Closing | Ends at meeting | Has acceptance/handover | Connects open items and benefits review |
| Traceability | Invents new objective | Uses Lesson 02 boundary | Traces need, outcome and transition fully |
| Scenario Accuracy | Contradicts source facts | Uses key facts correctly | Preserves locked facts and labels assumptions |

Passing level: every dimension at least Usable.

## Debrief Questions

- Which phase has more than one Process Group active
- Which evidence signal triggers replanning
- What can continue executing while another workstream replans
- Who approves gate movement
- What closing evidence protects operation and benefits

## Common Learner Errors

- Naming phases Initiating, Planning, Executing, Monitoring and Closing
- Putting Monitoring after build is complete
- Treating all variance as failure rather than signal
- Replanning without decision owner or evidence
- Closing at go-live without transition owner
- Describing Agile as having no Planning or Closing

## Remediation Guidance

If the learner confuses phases and Process Groups, ask them to rename phases using delivery work: Blueprint, Build, Test, Cutover. Then map Process Groups inside each phase.

If no feedback loop appears, ask what evidence would stop the team from discovering a problem too late.

If closing is weak, require four items: acceptance evidence, open items transferred, operation owner and benefits review date.

If governance is weak, ask “who has authority to approve moving through this gate, and what evidence must they see?”

## Facilitation Notes

Keep the lesson at foundation level. Do not drift into all 49 processes, detailed WBS, EVM, procurement law, risk quantitative analysis or Scrum event mechanics.

Use language carefully: Process Groups are not PMBOK 7 performance domains. Present them as PMBOK 6 process-based structure while using value-delivery thinking to explain why they matter.

## Artifact Approval Guidance

Approve the Lifecycle and Process Group Map at `Usable` when it includes:

- Lesson 02 project boundary and transition point
- lifecycle phases with exit evidence
- management activities mapped to Process Groups
- feedback/replanning triggers
- gate approval authority
- closing and transition evidence

Mark `Professional` when it also shows owners, evidence updates, thresholds, open-item transfer and clean handoff to Lesson 04.


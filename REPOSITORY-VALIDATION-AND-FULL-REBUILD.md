# PMBOK Masterclass — Repository Validation and Full Rebuild Instruction

> **Document Type:** Repository-wide validation, instructional design audit, and controlled rebuild instruction  
> **Execution Mode:** Audit first, then rebuild  
> **Scope:** Entire repository, including governance files, course architecture, Lesson 01–16, assessments, glossary, examples, cross-references, and AI continuation context  
> **Primary Goal:** Rebuild the repository into a coherent PMBOK Masterclass that teaches Project Management thinking—not merely definitions, summaries, or lists

---

# 1. Mission

Validate the entire PMBOK Masterclass repository and rebuild every weak, incomplete, inconsistent, duplicated, shallow, or placeholder section.

Do not treat this as a proofreading task.

This is a **repository-wide instructional redesign and content reconstruction task**.

The repository must become:

- A coherent end-to-end Project Management course
- A learning system that develops PM thinking and decision-making
- A reusable knowledge base for both human learners and future AI contributors
- A repository with stable terminology, clear lesson boundaries, traceable sources, and consistent teaching quality
- A course that moves from foundational understanding to applied professional judgement

The current repository may contain:

- Placeholder files
- High-level notes presented as complete lessons
- Lessons with uneven depth
- Repetitive or generic AI-generated explanations
- Definitions without sufficient context
- Examples that do not actually teach decision-making
- Assessments that only test memorization
- Inconsistent use of ERP and Hotel Booking scenarios
- Missing course governance
- Missing source separation
- Missing lesson continuity
- Missing instructional progression
- Missing quality controls

Assume nothing is complete merely because a file exists.

---

# 2. Non-Negotiable Instruction

## 2.1 Do not immediately rewrite files

First perform a complete repository audit.

Before changing content:

1. Load every repository file.
2. Build a complete file inventory.
3. Identify the purpose of each file.
4. Identify duplicate, conflicting, obsolete, incomplete, and missing files.
5. Compare every lesson against the course standard.
6. Compare terminology across the whole repository.
7. Inspect lesson progression from Lesson 01 to Lesson 16.
8. Identify where the teaching quality deteriorates.
9. Identify which parts are factual, assumed, enriched, or unsupported.
10. Produce an audit report before execution.

Do not start rewriting Lesson 02 until the audit has shown what must be rebuilt across the entire course.

---

# 3. Source Hierarchy

Use the following source priority.

## Level 1 — Repository Canonical Sources

Use repository-approved source files first, including:

- `PMBOK-Overview.md`
- `COURSE-ROADMAP.md`
- `COURSE_STANDARD.md`
- `STYLE_GUIDE.md`
- `CLAUDE.md`
- `LESSON_TEMPLATE.md`
- `PM_GLOSSARY.md`
- `REPOSITORY_DECISION_LOG.md`
- Any approved source-mapping or governance files

## Level 2 — Approved Lesson 01

Lesson 01 is the current quality reference.

Do not copy its wording mechanically, but preserve its instructional qualities:

- Begins with a meaningful professional question
- Explains why before what
- Establishes context before terminology
- Builds a mental model
- Uses examples to clarify decisions
- Corrects misconceptions
- Connects output to outcome and value
- Encourages reflection
- Sounds like a skilled instructor, not a textbook summarizer

Lesson 01 is the **quality baseline**, not merely another lesson.

## Level 3 — PMBOK and PMI Concepts

Use only concepts that are supported by the approved canonical source or clearly identified PMBOK references.

When educationally relevant, historical PMBOK 6th Edition concepts may be used, but they must be labeled appropriately.

Do not present PMBOK 6 process structures as if they are the complete structure of PMBOK 7.

## Level 4 — Teaching Enrichment

Teaching enrichment may include:

- Practical explanations
- Simplified mental models
- ERP scenarios
- Hotel Booking scenarios
- Decision examples
- Workshops
- Interview questions
- Real enterprise patterns

Every enrichment must be clearly distinguishable from canonical PMBOK content.

## Level 5 — Assumptions

Any invented project detail must be labeled as a teaching assumption.

Never convert a teaching scenario into an unsupported factual claim.

---

# 4. Mandatory Source Classification

Every lesson must clearly separate the following:

## PMBOK

Concepts explicitly grounded in the canonical PMBOK source.

## Best Practice

Common professional practices that are useful but not mandatory PMBOK rules.

## Enterprise Practice

Patterns commonly seen in real organizations.

## Teaching Scenario

Invented or simplified details used to teach a concept.

## Professional Opinion

Interpretation or advice that may vary by context.

Do not mix these categories without labeling them.

The learner must always know:

> “Is this PMBOK, common practice, a scenario, or an instructor’s interpretation?”

---

# 5. Course Architecture to Validate

The intended course contains 16 lessons.

## Foundation

1. Why Project Managers Must Know PMBOK
2. Project Management Overview
3. Five Project Management Process Groups
4. Ten Project Management Knowledge Areas Overview

## Core Project Management Knowledge

5. Project Integration Management
6. Project Stakeholder Management
7. Project Scope Management and WBS
8. Project Schedule Management
9. Project Cost Management and Earned Value
10. Project Quality Management
11. Project Resource Management
12. Project Communications Management
13. Project Risk Management
14. Project Procurement Management

## Adaptive Delivery

15. Agile Project Management: Mindset, Scrum, and Kanban
16. Predictive vs Agile vs Hybrid and Tailoring

Validate whether this structure still produces the best instructional progression.

Do not change lesson numbering casually.

If restructuring is necessary:

1. Explain why.
2. Show the impact.
3. Preserve backward compatibility where possible.
4. Record the decision in `REPOSITORY_DECISION_LOG.md`.

---

# 6. Central Teaching Philosophy

Every lesson must teach in the following order:

```text
Real Problem
→ Why It Matters
→ Mental Model
→ Concept and Terminology
→ How It Works
→ Decision Thinking
→ Applied Scenario
→ Misconception Correction
→ Practice
→ Reflection
→ Connection to the Next Lesson
```

Do not use this weak pattern:

```text
Definition
→ Bullet List
→ Generic Example
→ Quiz
```

The course must feel like a professional instructor is guiding the learner through a way of thinking.

---

# 7. Mandatory Lesson Structure

Every full lesson must include the following sections.

## 7.1 Lesson Metadata

- Lesson number
- Title
- Difficulty
- Estimated study time
- Prerequisites
- Related lessons
- Canonical sources
- Scenario versions
- Status
- Last reviewed date
- Intended learner level

## 7.2 Opening Professional Question

Open with a realistic question, tension, failure, contradiction, or decision.

The opening must make the learner want to understand the concept.

## 7.3 Why This Matters

Explain:

- What problem existed before this practice
- What goes wrong when it is absent
- Why an experienced PM can still fail without it
- How it connects to business outcomes

## 7.4 Learning Objectives

Objectives must be observable.

Avoid vague statements such as:

- “Understand Scope Management”

Prefer:

- “Differentiate Project Scope from Product Scope”
- “Build a WBS to an appropriate Work Package level”
- “Identify whether a requested change is clarification or scope expansion”

## 7.5 Mental Model

Every lesson must provide at least one simple mental model.

Examples:

```text
Need → Decision → Work → Output → Outcome → Value
```

```text
Uncertainty → Risk → Response → Trigger → Action
```

```text
Requirement → Scope → WBS → Activity → Estimate → Baseline
```

The mental model must help the learner reason, not merely memorize.

## 7.6 Main Lesson

The main lesson must:

- Explain concepts progressively
- Define terminology after context
- Use meaningful transitions
- Connect concepts to decisions
- Avoid encyclopedia-style dumping
- Avoid excessive disconnected bullet lists
- Explain relationships between concepts
- Show when the concept is useful
- Show where it is commonly misused

## 7.7 PM Thinking

Explain what a Project Manager should notice, question, and anticipate.

Examples:

- What is not being said?
- Which assumption is hidden?
- Who owns the outcome?
- What trade-off is being concealed?
- Which metric may be misleading?
- What may fail after handover?

## 7.8 PM Decision Thinking

This is mandatory in every lesson.

For each major concept, identify:

- Decision to be made
- Decision owner
- Required information
- Assumptions
- Options
- Trade-offs
- Risk of delay
- Evidence of decision
- Follow-up action

Use this pattern where useful:

```text
Decision:
Owner:
Inputs:
Options:
Trade-offs:
Risk:
Evidence:
Next Action:
```

## 7.9 PM Insight

Include professional insights that help learners move beyond procedural knowledge.

Examples:

- A complete plan can still be based on a false assumption.
- A signed acceptance does not guarantee adoption.
- A green schedule may hide a red outcome.
- More documentation does not automatically mean more control.
- A stakeholder problem may appear as a technical delay.

## 7.10 Continuous ERP Scenario

ERP must remain a continuous enterprise case, not a different unrelated example in every lesson.

Maintain a stable scenario definition covering:

- Sponsor
- Business departments
- Process owners
- Key users
- IT
- Vendor / System Integrator
- Data migration
- Integration
- Testing
- Training
- Cutover
- Go-live
- Support
- Adoption
- Benefits realization

Each lesson must use the same ERP world while focusing on the current lesson topic.

## 7.11 Continuous Hotel Booking Scenario

Maintain a stable digital platform scenario including:

- Mobile App
- Customer Web App
- Landing Page
- Back Office Web Application
- Booking Engine
- Hotel and Room Inventory
- Availability
- Pricing
- Payment
- Booking Confirmation
- Notification
- Administration
- Reporting
- Hotel partners
- Customer support
- Cloud and external services

This scenario must show a different project context from ERP:

- Customer-facing product
- Faster feedback
- Digital behavior
- Conversion
- Reliability
- Product operation
- Incremental delivery

## 7.12 Real Enterprise Example

Include one example beyond the core scenario when it adds teaching value.

Do not add a random example merely to satisfy the template.

## 7.13 Common Mistakes

Describe mistakes people actually make while performing the work.

Example:

- Creating a WBS by department rather than by deliverable without understanding the consequence
- Reporting percent complete without objective evidence
- Treating every issue as a risk
- Adding stakeholders to a register but never changing engagement strategy

## 7.14 Common Misconceptions

Correct beliefs that cause wrong decisions.

Example:

- “Agile means no planning”
- “Go-live means the project succeeded”
- “The sponsor owns every decision”
- “A detailed requirement is automatically a good requirement”

## 7.15 Interview Questions

Include:

- Foundational question
- Scenario question
- Senior PM question
- Executive-level question
- Suggested answer direction
- Warning signs in weak answers

Do not provide only memorized definitions.

## 7.16 PM Dictionary

Include only terms used in the lesson.

For every term:

- English term
- Thai explanation
- Practical meaning
- Common misuse
- Related term

Synchronize terms with `PM_GLOSSARY.md`.

## 7.17 Workshop

Every workshop must require judgement.

Avoid exercises that only ask learners to repeat definitions.

A workshop should include:

- Scenario
- Role
- Available information
- Missing information
- Decision required
- Constraints
- Expected output
- Debrief questions
- Evaluation criteria

## 7.18 Assessment

Assessment must include a mix of:

- Concept check
- Misconception check
- Scenario analysis
- Decision analysis
- Cross-knowledge impact analysis
- Applied exercise
- Reflection

At least half of the assessment must test application or judgement.

## 7.19 Executive Summary

Summarize:

- Why the topic matters
- What decision it improves
- What failure it prevents
- What the executive should monitor

## 7.20 Lesson Connection

End with:

- What the learner can now do
- What remains incomplete
- Why the next lesson follows logically

## 7.21 AI Continuation Context

Every lesson must include or reference a machine-readable continuation block containing:

- Concepts introduced
- Terms standardized
- Scenario state
- Decisions made
- Assumptions
- Open questions
- Dependencies
- Prohibited contradictions
- Next lesson handoff

---

# 8. Required File Package Per Lesson

Every lesson folder must use this standard:

```text
lesson-XX/
├── Lesson-XX_1-Blueprint.md
├── Lesson-XX_2-<Lesson-Title>.md
├── Lesson-XX_3-Assessment.md
└── Lesson-XX_4-Source-Mapping.md
```

Validate that:

- The Blueprint is not a duplicate of governance rules
- The full lesson contains the actual teaching
- The Assessment tests the lesson
- Source Mapping accurately identifies source-derived and enriched material
- File numbering matches reading and production order
- Links between files work
- Lesson folders and repository indexes match

---

# 9. Blueprint Standard

A Blueprint must contain:

- Purpose
- Learner profile
- Prerequisites
- Learning objectives
- Opening question
- Core teaching message
- Mental models
- Narrative flow
- Concepts
- PM decisions
- ERP use
- Hotel Booking use
- Misconceptions
- Workshop design
- Assessment design
- Lesson boundaries
- Source coverage
- Completion criteria

A Blueprint is not:

- A shorter copy of the lesson
- A copy of `COURSE_STANDARD.md`
- A list of headings only
- A generic prompt

---

# 10. Assessment Quality Standard

Reject assessments that rely mainly on:

- Definition recall
- Matching vocabulary
- True/False questions
- Obvious multiple-choice distractors

A valid assessment must measure whether the learner can:

- Identify the real problem
- Ask for missing information
- Choose between options
- Explain a trade-off
- Identify an owner
- Separate output from outcome
- Recognize an invalid assumption
- Recommend a next action
- Detect cross-knowledge impact
- Tailor the approach to context

Every scenario assessment must include an answer guide.

The answer guide must explain reasoning, not only state the answer.

---

# 11. Terminology Governance

Validate all terminology across the repository.

Create or update `PM_GLOSSARY.md`.

For each term, specify:

- Standard English term
- Preferred Thai explanation
- Meaning
- Context
- Commonly confused term
- Deprecated translation, if any

Mandatory consistency checks include:

- Project vs Operation
- Output vs Outcome vs Benefit vs Business Value
- Deliverable
- Requirement
- Scope
- Product Scope vs Project Scope
- Work Package
- Activity
- Milestone
- Risk vs Issue
- Verification vs Validation
- Quality vs Grade
- Sponsor vs Business Owner vs Product Owner
- Change Request vs Defect Repair
- Procurement vs Purchasing
- Predictive vs Waterfall
- Agile vs Scrum
- Phase vs Process Group
- Knowledge Area
- Tailoring
- Acceptance
- Handover
- Transition to Operation

Do not translate the same PM term differently across lessons without a documented reason.

---

# 12. Scenario Governance

Create or update dedicated scenario files if they do not exist.

Recommended structure:

```text
scenarios/
├── ERP-TRANSFORMATION-CASE.md
└── HOTEL-BOOKING-PLATFORM-CASE.md
```

Each scenario file should contain:

- Business background
- Business need
- Objectives
- Scope
- Out of scope
- Stakeholders
- Organization structure
- Team
- Vendors
- Constraints
- Assumptions
- Risks
- Timeline
- Budget context
- Deliverables
- Outcomes
- Benefits
- Operating model
- Scenario version history

Every lesson must reference the scenario version it uses.

Do not silently change scenario facts between lessons.

---

# 13. Repository Governance Files to Validate or Create

The final repository should include, at minimum:

```text
README.md
COURSE-ROADMAP.md
COURSE_STANDARD.md
STYLE_GUIDE.md
LESSON_TEMPLATE.md
LESSON_INDEX.md
PM_GLOSSARY.md
CLAUDE.md
AI_CONTINUATION_GUIDE.md
REPOSITORY_VERSION.md
repository/REPOSITORY_DECISION_LOG.md
repository/REPOSITORY_AUDIT_REPORT.md
repository/CONTENT_COVERAGE_MATRIX.md
repository/TERMINOLOGY_AUDIT.md
repository/LESSON_QUALITY_SCORECARD.md
scenarios/ERP-TRANSFORMATION-CASE.md
scenarios/HOTEL-BOOKING-PLATFORM-CASE.md
```

Create missing files only when they have a clear purpose.

Do not create governance files that duplicate one another.

---

# 14. Repository Audit Requirements

Before rebuilding, produce `repository/REPOSITORY_AUDIT_REPORT.md`.

The audit must include:

## 14.1 File Inventory

For every file:

- Path
- Intended purpose
- Current status
- Quality
- Duplication
- Conflict
- Action required

## 14.2 Lesson Scorecard

Score each lesson from 0–5 on:

- Accuracy
- Depth
- Why-before-What
- Mental model
- Narrative flow
- PM Thinking
- PM Decision Thinking
- ERP continuity
- Hotel Booking continuity
- Misconception correction
- Assessment quality
- Source transparency
- Terminology consistency
- Lesson boundary
- Connection to adjacent lessons

Do not inflate scores.

Lesson 01 may be the quality reference, but it must still be audited.

## 14.3 Gap Analysis

Identify:

- Missing concepts
- Overlapping concepts
- Premature concepts
- Repeated generic explanations
- Unsupported assertions
- Shallow examples
- Missing decision points
- Missing learner practice
- Missing source traceability
- Broken links
- Missing files
- Placeholder files
- Inconsistent naming
- Inconsistent metadata

## 14.4 Root Cause Analysis

Do not only say a lesson is weak.

Explain why it is weak.

Possible root causes:

- Generated from a topic list rather than a learning objective
- No learner persona
- No narrative progression
- Reused generic template
- No scenario continuity
- No cross-lesson memory
- Assessment disconnected from lesson
- Source not mapped
- Lesson boundary not enforced
- Too many concepts compressed into one section
- Confusion between PMBOK 6 and PMBOK 7 structures

## 14.5 Rebuild Priority

Classify every lesson:

- Keep
- Light Revision
- Major Revision
- Full Rebuild
- Merge
- Split
- Remove
- Missing

---

# 15. Content Coverage Matrix

Create `repository/CONTENT_COVERAGE_MATRIX.md`.

The matrix must map:

- Canonical source concept
- Lesson number
- Section
- Depth level
- Scenario used
- Assessment coverage
- Source classification
- Duplication risk
- Missing coverage

This prevents:

- Missing important content
- Repeating the same explanation in many lessons
- Teaching advanced content before prerequisites
- Contradictions between lessons

---

# 16. Lesson Quality Scorecard

Create `repository/LESSON_QUALITY_SCORECARD.md`.

For each lesson, include:

- Current score
- Target score
- Major weakness
- Required changes
- Validation status
- Reviewer notes

Minimum release threshold:

- No category below 3/5
- Average at least 4/5
- Source transparency must be 5/5
- Terminology consistency must be 5/5
- PM Decision Thinking must be at least 4/5
- Assessment quality must be at least 4/5

A lesson that fails the threshold remains `Draft`.

---

# 17. Rebuild Strategy

## Pass 0 — Repository Audit

Deliver:

- Inventory
- Gap analysis
- Scorecard
- Terminology audit
- Coverage matrix
- Rebuild plan

Do not rewrite lessons yet.

## Pass 1 — Governance and Architecture

Fix:

- Repository structure
- Course roadmap
- Standards
- Templates
- Glossary
- Scenario definitions
- Indexes
- Decision log

## Pass 2 — Lesson Blueprints

Rebuild all Lesson 01–16 Blueprints before rewriting full lessons.

Validate:

- Lesson boundaries
- Learning progression
- Concepts
- Decisions
- Scenarios
- Assessments
- Source coverage

## Pass 3 — Canonical Lesson Content

Rebuild lessons in order.

Do not build all lessons in one uncontrolled generation.

Use batches:

- Batch A: Lesson 01–04
- Batch B: Lesson 05–09
- Batch C: Lesson 10–14
- Batch D: Lesson 15–16

After each batch:

- Validate terminology
- Validate scenario continuity
- Validate cross-references
- Validate no content duplication
- Update indexes and coverage matrix

## Pass 4 — Assessments and Workshops

Rebuild assessments only after lesson content is stable.

Ensure questions test the actual lesson.

## Pass 5 — Source Mapping

Validate every claim and classification.

## Pass 6 — Cross-Lesson Integration

Check:

- Prerequisites
- Definitions
- Progressive difficulty
- Scenario state
- Repeated content
- Missing bridges
- Final course coherence

## Pass 7 — Final Validation

Run all release gates and update repository version.

---

# 18. Lesson Rebuild Rules

When rebuilding Lesson 02–16:

1. Do not merely expand the current text.
2. Do not preserve weak content for convenience.
3. Rebuild from the validated Blueprint.
4. Match or exceed Lesson 01 teaching quality.
5. Use a distinct teaching problem for each lesson.
6. Keep lesson scope disciplined.
7. Do not make every lesson sound structurally identical.
8. Vary instructional devices where appropriate:
   - Dialogue
   - Incident
   - Decision memo
   - Comparison
   - Failure analysis
   - Workshop
   - Executive scenario
   - Timeline
   - Flow
9. Preserve course voice and terminology.
10. Use examples only when they clarify a decision.
11. Avoid filler phrases and generic motivational text.
12. Avoid claiming completeness without validation.

---

# 19. Special Handling of Lesson 01

Lesson 01 is currently considered the strongest lesson.

Do not rewrite it automatically.

Audit it first.

Possible actions:

- Preserve
- Normalize metadata
- Add missing mandatory sections
- Improve source mapping
- Add AI continuation context
- Align terminology
- Repair cross-links

Do not reduce its narrative quality to make it match weaker lessons.

The rest of the repository should be raised toward Lesson 01—not the reverse.

---

# 20. PMBOK Edition Integrity

The repository references PMBOK 7 as primary while using educationally relevant historical concepts from PMBOK 6.

Validate every lesson for edition integrity.

Rules:

- Do not claim the 5 Process Groups and 10 Knowledge Areas are the complete organizing structure of PMBOK 7.
- Clearly explain when teaching PMBOK 6 process architecture for practical education.
- Include PMBOK 7 principles, performance domains, value delivery, systems thinking, tailoring, and models/methods/artifacts where required by the canonical scope.
- Explain the relationship between editions rather than blending them silently.
- Record the course’s editorial position in a governance file.

Create or update:

```text
repository/PMBOK-EDITION-POSITION.md
```

This file must explain:

- Primary edition
- Why historical process concepts remain
- How terminology is presented
- How exam-oriented vs practice-oriented content is distinguished
- What the course does not claim

---

# 21. Writing Style

Use Thai as the primary teaching language with English PM terminology where useful.

Writing must be:

- Clear
- Professional
- Conversational enough to teach
- Precise
- Non-repetitive
- Structured without becoming mechanical
- Suitable for self-study
- Suitable for PM, PO, BA, SA, Team Lead, and emerging Project Managers

Explain technical terms at first use.

Do not translate awkwardly when the English term is standard in professional work.

Avoid:

- Robotic transitions
- Empty summaries
- Excessive bullet lists
- Unexplained jargon
- Repeating the same sentence in different words
- Artificially confident claims
- Generic AI phrases
- Treating the learner like an exam memorizer

---

# 22. Evidence and Traceability

Every lesson must provide traceability sufficient to answer:

- Where did this concept come from?
- Is it PMBOK or enrichment?
- Was this scenario invented?
- Which other lesson depends on it?
- Which assessment tests it?
- Which glossary terms were introduced?

Source Mapping must not be generic.

It must map specific sections and concepts.

---

# 23. Anti-Hallucination Rules

Do not:

- Invent PMI facts
- Invent PMBOK definitions
- Invent edition differences
- Invent legal requirements
- Invent statistics
- Invent enterprise results
- Present teaching scenarios as real client cases
- Claim a tool or method is mandatory when it is contextual
- Claim PMBOK requires a specific template unless supported

When uncertain:

- Mark as unconfirmed
- Add a validation note
- Avoid authoritative wording
- Request a source if necessary

---

# 24. Required Validation Commands for the AI

The AI executing this instruction must explicitly perform the following checks:

## Structure Validation

- Confirm all required files exist
- Confirm folder naming
- Confirm lesson numbering
- Confirm links
- Confirm no duplicate governance files

## Content Validation

- Confirm every lesson has mandatory sections
- Confirm learning objectives match assessment
- Confirm workshop tests judgement
- Confirm examples match the lesson topic
- Confirm lesson boundaries
- Confirm transition to the next lesson

## Terminology Validation

- Search all files for key terms
- Detect inconsistent translations
- Detect deprecated terms
- Detect PMBOK 6/7 blending

## Scenario Validation

- Confirm ERP facts remain stable
- Confirm Hotel Booking facts remain stable
- Confirm scenario versions
- Confirm no contradictory roles, scope, or outcomes

## Source Validation

- Confirm every lesson has source mapping
- Confirm enrichment is labeled
- Confirm assumptions are labeled
- Confirm unsupported claims are removed or flagged

## Assessment Validation

- Confirm at least 50% application/judgement
- Confirm answer guides explain reasoning
- Confirm no trick questions
- Confirm no answer depends on unstated assumptions

---

# 25. Deliverables

The AI must produce or update:

1. `repository/REPOSITORY_AUDIT_REPORT.md`
2. `repository/CONTENT_COVERAGE_MATRIX.md`
3. `repository/TERMINOLOGY_AUDIT.md`
4. `repository/LESSON_QUALITY_SCORECARD.md`
5. `repository/PMBOK-EDITION-POSITION.md`
6. `scenarios/ERP-TRANSFORMATION-CASE.md`
7. `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md`
8. Updated governance files
9. Rebuilt Lesson 01–16 Blueprints
10. Rebuilt Lesson 02–16 full lessons
11. Revised Lesson 01 only where audit proves necessary
12. Rebuilt assessments
13. Accurate source mappings
14. Updated glossary
15. Updated lesson index
16. Updated decision log
17. Updated repository version
18. Final validation report

---

# 26. Final Validation Report

Create:

```text
repository/FINAL-VALIDATION-REPORT.md
```

It must include:

- What was reviewed
- What was changed
- What was preserved
- What was removed
- Remaining limitations
- Lessons passing release gate
- Lessons still in Draft
- Terminology status
- Scenario consistency status
- Source traceability status
- Broken-link status
- PMBOK edition integrity status
- Recommended next action

Do not state “complete” unless every release gate passes.

---

# 27. Definition of Done

The repository is considered ready only when:

- Lesson 01–16 are complete
- All lesson packages have four correctly purposed files
- Teaching quality is consistent
- Lesson progression is logical
- Every lesson contains PM Thinking and PM Decision Thinking
- ERP is continuous
- Hotel Booking is continuous
- PMBOK / Best Practice / Enterprise Practice / Teaching Scenario / Opinion are separated
- Glossary terminology is stable
- PMBOK edition position is explicit
- Assessments test application
- Source mappings are specific
- No placeholder file is presented as complete
- No broken internal links remain
- Governance files do not conflict
- All lessons pass the quality threshold
- Final validation report is honest about limitations

---

# 28. Execution Prompt

Use the following instruction when starting the rebuild:

> Load the entire repository and execute `REPOSITORY-VALIDATION-AND-FULL-REBUILD.md`.
>
> Begin with Pass 0 — Repository Audit.
>
> Do not rewrite lessons before producing the audit, scorecard, terminology audit, and content coverage matrix.
>
> Treat Lesson 01 as the current instructional quality baseline.
>
> Assume Lesson 02–16 may require full reconstruction rather than editing.
>
> Preserve valid content, but do not preserve weak structure merely because it already exists.
>
> Separate PMBOK, Best Practice, Enterprise Practice, Teaching Scenario, and Professional Opinion.
>
> Maintain continuous ERP Transformation and Hotel Booking Digital Platform scenarios.
>
> Do not claim completion until all release gates pass.
>
> When output approaches the response limit, stop at a logical boundary and wait for the command:
>
> `Continue Repository Rebuild`

---

# 29. First Required Response from the Executing AI

The first response must contain only:

1. Repository inventory summary
2. Critical findings
3. Missing files
4. Conflicting rules
5. Lesson quality overview
6. Proposed rebuild priority
7. Files to be created or modified in Pass 1

Do not begin rewriting lesson content in the first response.

---

# 30. Core Principle

> **The goal is not to make the repository look complete. The goal is to make the learner think, decide, and operate like a professional Project Manager.**

---
title: E-book Style Guide
document_type: E-book Editorial Control
status: Active
created_on: 2026-07-22
---

# E-book Style Guide

## Positioning

The e-book must describe itself as a **PMBOK-aligned Practical Masterclass**. It must not claim to be official PMI material or a substitute for PMI publications.

## Language

- Use Thai narrative with standard English PM terms.
- Explain a technical term before using it as assumed knowledge.
- Keep English terms when they are standard PM vocabulary, such as `Project Charter`, `Scope`, `Risk Register`, `WBS`, `Product Backlog` and `Tailoring`.
- Use short paragraphs and purposeful tables. Avoid turning the chapter into bullet-only notes.

## Teaching Voice

Write like an experienced instructor helping a beginner PM reason through real work:

```text
real problem -> why it matters -> mental model -> concept -> decision thinking
-> applied scenario -> misconception correction -> practice -> reflection -> handoff
```

## Source Labels

Use visible source labels for substantive claims:

- `[PMBOK]`
- `[PMBOK 6]`
- `[PMBOK 7]`
- `[Best Practice]`
- `[Enterprise Practice]`
- `[Teaching Scenario]`
- `[Professional Opinion]`

Do not turn professional opinion, enterprise practice or teaching assumptions into PMBOK claims.

## Learner and Instructor Separation

Learner chapters must not reveal:

- Full model answers
- Full scoring rubrics
- Instructor facilitation notes
- Repository governance notes
- AI continuation context
- Full source mapping

Instructor chapters must include teaching intent, walkthrough, completed example, model answer, checklist, rubric, debrief questions and remediation guidance.

## Path Rules

- Use relative Markdown links only.
- Do not use local-machine paths.
- Do not use local file-scheme links.
- Link from each output file based on its own location.

## Scenario Rules

- Use `scenarios/ERP-TRANSFORMATION-CASE.md` and `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` as the only authority for scenario facts.
- Label teaching-only calculations as `Teaching Calculation - not a locked scenario actual`.
- Do not change locked budget, timeline, scope, owner or KPI facts unless the scenario master is formally updated outside this e-book workflow.

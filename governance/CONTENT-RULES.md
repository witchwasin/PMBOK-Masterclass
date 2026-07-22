# PMBOK Masterclass — Content Rules

> Operational rules for all course files. `COURSE_STANDARD.md` defines the release gate; this document explains how contributors meet it.

## 1. Authority and source hierarchy

1. `references/PMBOK-Overview.md` is the canonical content source.
2. `governance/COURSE_STANDARD.md`, `STYLE_GUIDE.md`, `LESSON_TEMPLATE.md`, and `PM_GLOSSARY.md` control quality and terminology.
3. `scenarios/` is the only authority for ERP and Hotel Booking facts, figures, people, milestones, and scenario versions.
4. `repository/REPOSITORY_DECISION_LOG.md` records decisions that change course scope or interpretation.

Never turn a teaching assumption, professional opinion, or enterprise pattern into a PMBOK claim.

## 2. PMBOK edition position

The course uses the existing canonical source: PMBOK 6 process-based structures plus PMBOK 7 value, principle, and tailoring context. Apply labels precisely:

- `[PMBOK 6]` for Process Groups, Knowledge Areas, and process-oriented material.
- `[PMBOK 7]` for principles, value delivery, and performance-domain-oriented material.
- `[PMBOK]` only when the statement is safe across editions or the edition is immaterial.

The course is practice-oriented, not a claim of complete PMP-exam coverage. Do not present the PMBOK 6 structure as the structure of PMBOK 7.

## 3. Required lesson metadata

Every blueprint, lesson, assessment, and source-mapping file must use the metadata standard in `LESSON_TEMPLATE.md`. Full lessons must state difficulty, estimated study time, prerequisites, related lessons, canonical source, both scenario versions, status, validation status, review date, and intended learner level.

Until a lesson passes its release gate, use `status: Draft` and `validation_status: Not Validated`. `Active` is reserved for a reviewed and released lesson.

## 4. Teaching sequence and depth

Write a lesson as an instructor-led reasoning journey:

```text
Real problem → why it matters → mental model → concept → how it works
→ decision thinking → applied scenario → misconception correction → practice → reflection → next lesson
```

Do not use `definition → bullet list → generic example → quiz` as the primary structure. Explain why before terminology, then build from a concrete tension to the framework. Each lesson owns its stated boundary; it may prepare a later concept but must not teach that later lesson in full.

## 5. Decision thinking standard

Each full lesson contains at least one substantive decision record and teaches the learner how to reason, not which answer to memorize. Use this format:

```text
Decision:
Owner:
Inputs and missing information:
Assumptions:
Options:
Trade-offs:
Risk of delay or wrong decision:
Evidence of decision:
Next action and follow-up:
```

Do not recommend an option without showing the decision authority, information limits, alternatives, trade-offs, and evidence that would justify it.

## 6. Scenario continuity

- Cite the scenario version in front matter and identify the source scenario in the section.
- Reuse locked names, scope, budget, timeline, risks, contracts, and decisions from the Scenario Master files.
- Label invented lesson-specific details `[Teaching Scenario]` and add them to the lesson's AI Continuation Context when they affect later lessons.
- Do not silently change a baseline. Propose a versioned scenario update and log the decision first.

## 7. Source classification

Apply a visible label to every substantive explanation, decision example, workshop, and assessment rationale:

- `[PMBOK]`, `[PMBOK 6]`, `[PMBOK 7]`
- `[Best Practice]`
- `[Enterprise Practice]`
- `[Teaching Scenario]`
- `[Professional Opinion]`

Source Mapping files must map the actual lesson sections, not repeat generic labels.

## 8. Workshops and assessments

Every workshop states the scenario, learner role, available and missing information, decision, constraints, expected output, debrief questions, and evaluation criteria.

At least half of each assessment must test application or judgement. Across the course, include Decision Cases, Trade-off Cases, Artifact Reviews, Executive Communication, Cross-Knowledge Analysis, and Ambiguous Scenarios. Recall questions may support learning but cannot be the dominant assessment method.

## 9. Interview questions and dictionary

Each full lesson includes Foundational, Scenario, Senior PM, and Executive interview questions, with answer direction and warning signs. Its PM Dictionary must match `PM_GLOSSARY.md`: English term, Thai explanation, practical meaning, common misuse, and related terms. Add a glossary term before using a new core term inconsistently.

## 10. Writing, links, and claims

- Use Thai narrative with standard English PM terms; expand an acronym on first use.
- Use relative Markdown links only. `file:///`, local-machine paths, and machine-specific references are prohibited.
- Prefer short paragraphs and purposeful tables; use lists only when the learner benefits from comparison or action steps.
- Distinguish fact, assumption, and professional opinion explicitly.
- Preserve Lesson 01's narrative quality; never reduce it merely to match a template.

## 11. Definition of Done

A lesson is ready for validation only when it has all 21 mandatory sections, a companion assessment and source mapping, aligned metadata, valid relative links, scenario continuity, source labels, glossary alignment, and no boundary violation. It is releasable only when it meets the `COURSE_STANDARD.md` Release Gate and the quality scorecard threshold.

## 12. Contributor checklist

Before editing: read the canonical source, scenario master, glossary, adjacent lessons, and decision log. After editing: validate headings and metadata, check links, check terminology, update the index/coverage matrix/scorecard as appropriate, and record material decisions.

---
chapter: lesson-03
title: 5 Project Management Process Groups
document_type: E-book Chapter Validation Report
status: Ready for Human Review
validated_on: 2026-07-22
---

# Validation Report — Chapter 03

## Gate Status

```yaml
chapter: lesson-03
source_validation: passed
scenario_validation: passed
terminology_validation: passed
editorial_validation: passed
artifact_traceability: passed
assessment_validation: passed
learner_instructor_separation: passed
path_hygiene: passed
status: ready_for_human_review
```

## Validation Detail

| Dimension | Result | Evidence |
|---|---|---|
| Source accuracy | Passed | Chapter content maps to Lesson 03 source files, Lesson 02 handoff, Lesson 04 blueprint and control package |
| Scenario accuracy | Passed | ERP and Hotel facts preserved and no new locked scenario facts created |
| Terminology consistency | Passed | Process Group, Project Phase, Lifecycle, Feedback Loop, Replanning and Closing align with source/registers |
| Editorial quality | Passed | Learner chapter follows required 20-section chapter contract |
| Artifact continuity | Passed | Lifecycle and Process Group Map feeds Lesson 04 PM Coverage and Cross-impact Map |
| Assessment quality | Passed | Assessment composition is retrieval 10%, application/judgement/artifact 90% |
| Learner/instructor separation | Passed | Learner file contains prompts only; model answers and rubric are in instructor/answer-key files |
| Path hygiene | Passed | Relative links only; no local-machine paths |

## Files Created

| File | Purpose |
|---|---|
| `lesson-03-learner.md` | Learner chapter |
| `lesson-03-instructor.md` | Instructor guide |
| `lesson-03-answer-key.md` | Instructor-facing answer key |
| `lesson-03-source-map.md` | Source mapping |
| `lesson-03-traceability.md` | Artifact traceability and handoff |
| `lesson-03-validation-report.md` | Chapter validation report |

## Assessment Composition

| Type | Share |
|---|---:|
| Retrieval | 10% |
| Application, judgement and artifact work | 90% |

## Word Count and Page Estimate

| File | Word count by `wc -w` | Estimated A4 pages |
|---|---:|---:|
| `lesson-03-learner.md` | 1,835 | 6-8 |
| `lesson-03-instructor.md` | 1,101 | 4-5 |
| `lesson-03-answer-key.md` | 549 | 2-3 |
| Supporting maps and validation | 1,346 | 4-5 |
| Total chapter package | 4,831 | 15-21 |

Thai prose word counts are approximate because Thai text is not whitespace-tokenized like English. Content was not padded beyond source support.

## Artifact Links

- Learner artifact source: `../../../lessons/lesson-03/learner/Artifact-Template.md`
- Prior handoff: `../lesson-02/lesson-02-learner.md`
- Handoff target: `../../../lessons/lesson-04/Lesson-04_1-Blueprint.md`

## Command Results

| Command | Result |
|---|---|
| `bash scripts/validate-repository.sh` | Passed |
| `git diff --check` | Passed |
| Path hygiene scan under `e-Book/` | Passed |
| Learner answer/rubric scan | Passed; no full answers or rubric found |

## Issues Remaining

No critical issues identified. Human review is required before starting Lesson 04.

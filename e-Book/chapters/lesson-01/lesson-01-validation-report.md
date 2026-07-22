---
chapter: lesson-01
title: ทำไม Project Manager ต้องรู้ PMBOK
document_type: E-book Chapter Validation Report
status: Ready for Human Review
validated_on: 2026-07-22
---

# Validation Report — Chapter 01

## Gate Status

```yaml
chapter: lesson-01
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
| Source accuracy | Passed | Chapter content maps to Lesson 01 source files, scenario registers and governance controls |
| Scenario accuracy | Passed | ERP and Hotel locked facts preserved |
| Terminology consistency | Passed | PMBOK, Tailoring, Output, Outcome, Benefit and Business Value align with terminology register |
| Editorial quality | Passed | Learner chapter follows required 20-section chapter contract |
| Artifact continuity | Passed | PM Learning Baseline feeds Lesson 02 Project vs Operation Analysis and Value Chain |
| Assessment quality | Passed | Assessment composition is retrieval 10%, application/judgement/artifact 90% |
| Learner/instructor separation | Passed | Learner file contains prompts only; model answers and rubric are in instructor/answer-key files |
| Path hygiene | Passed | Relative links only; no local-machine paths |

## Files Created

| File | Purpose |
|---|---|
| `lesson-01-learner.md` | Learner chapter |
| `lesson-01-instructor.md` | Instructor guide |
| `lesson-01-answer-key.md` | Instructor-facing answer key |
| `lesson-01-source-map.md` | Source mapping |
| `lesson-01-traceability.md` | Artifact traceability and handoff |
| `lesson-01-validation-report.md` | Chapter validation report |

## Assessment Composition

| Type | Share |
|---|---:|
| Retrieval | 10% |
| Application, judgement and artifact work | 90% |

## Word Count and Page Estimate

| File | Word count by `wc -w` | Estimated A4 pages |
|---|---:|---:|
| `lesson-01-learner.md` | 1,594 | 5-7 |
| `lesson-01-instructor.md` | 1,293 | 4-6 |
| `lesson-01-answer-key.md` | 758 | 2-3 |
| Supporting maps and validation | 1,398 | 4-5 |
| Total chapter package | 5,043 | 15-21 |

Thai prose word counts are approximate because Thai text is not whitespace-tokenized like English. Content was not padded beyond source support.

## Artifact Links

- Learner artifact source: `../../../lessons/lesson-01/learner/Artifact-Template.md`
- Handoff target: `../../../lessons/lesson-02/Lesson-02_1-Blueprint.md`

## Command Results

| Command | Result |
|---|---|
| `bash scripts/validate-repository.sh` | Passed |
| `git diff --check` | Passed |
| Path hygiene scan under `e-Book/` | Passed |
| Learner answer/rubric scan | Passed; no full answers or rubric found |

## Issues Remaining

No critical issues identified. Human review is still required before starting Lesson 02.

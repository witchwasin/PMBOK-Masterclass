---
title: E-book Chapter Contract
document_type: E-book Editorial Control
status: Active
created_on: 2026-07-22
---

# E-book Chapter Contract

## Required Chapter Files

Each approved lesson chapter must create exactly one lesson folder:

```text
e-Book/chapters/lesson-XX/
├── lesson-XX-learner.md
├── lesson-XX-instructor.md
├── lesson-XX-answer-key.md
├── lesson-XX-source-map.md
├── lesson-XX-traceability.md
└── lesson-XX-validation-report.md
```

## Required Reading Before Writing

Before writing a chapter, read:

- `e-Book/editorial/EBOOK-CHAPTER-CONTRACT.md`
- `e-Book/editorial/EBOOK-STYLE-GUIDE.md`
- `e-Book/editorial/EBOOK-SCENARIO-FACT-REGISTER.md`
- `e-Book/editorial/EBOOK-TERMINOLOGY-REGISTER.md`
- `e-Book/editorial/EBOOK-TRACEABILITY-MATRIX.md`
- `e-Book/editorial/EBOOK-PRODUCTION-STATUS.md`
- `governance/ARTIFACT_DEPENDENCY_MAP.md`
- All source files under the current `lessons/lesson-XX/`

Read only the prior chapter summary, artifact handoff and carried terminology when continuity requires it. Read only the next lesson blueprint, artifact input and beginner prerequisites for handoff alignment.

## Learner Chapter Structure

1. Opening Scenario
2. Why This Matters
3. Learning Objectives
4. Beginner Safety
5. Mental Model
6. Main Lesson
7. PM Thinking
8. PM Decision Thinking
9. ERP Worked Example
10. Hotel Booking Example or Contrast
11. Watch PM Think
12. Artifact Example
13. Workshop
14. Beginner Checkpoint
15. End-of-Chapter Assessment
16. เก็บตกท้ายบท
17. Common Mistakes and Misconceptions
18. คลังคำศัพท์ประจำบท
19. สรุปหนึ่งหน้า
20. Artifact Handoff

Target length is 7,000-11,000 words or 18-28 A4 pages when source depth supports it. Do not pad content to hit length.

## Instructor Chapter Structure

Instructor chapters must include:

- Teaching Notes
- Learning intent
- Suggested timing
- Thinking Walkthrough
- Completed Example
- Model Answer
- Review Checklist
- Scoring Rubric
- Debrief Questions
- Common Learner Errors
- Remediation Guidance
- Facilitation Notes
- Artifact Approval Guidance
- Relative link to the learner chapter

Target length is 8,500-13,000 words or 22-32 A4 pages when source depth supports it. Do not pad content to hit length.

## Assessment Contract

Learner assessment must include:

- A. Concept Check
- B. Scenario Question
- C. Decision Case
- D. Artifact Construction
- E. Artifact Review
- F. Reflection

Assessment composition must be 10% retrieval and 90% application, judgement or artifact work.

## Chapter Validation Status

Every chapter validation report must use this gate:

```yaml
chapter: lesson-XX
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

If any item fails, the chapter status must not be marked passed.


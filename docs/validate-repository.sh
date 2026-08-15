#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
failures=0

fail() { printf 'FAIL: %s\n' "$1" >&2; failures=$((failures + 1)); }

for lesson_number in $(seq -w 1 16); do
  lesson_dir="$root/lessons/lesson-$lesson_number"
  lesson_file=$(find "$lesson_dir" -maxdepth 1 -name "Lesson-${lesson_number}_2-*.md" -print -quit)
  blueprint="$lesson_dir/Lesson-${lesson_number}_1-Blueprint.md"
  assessment="$lesson_dir/Lesson-${lesson_number}_3-Assessment.md"
  mapping="$lesson_dir/Lesson-${lesson_number}_4-Source-Mapping.md"

  [[ -n "$lesson_file" ]] || { fail "Lesson $lesson_number has no main lesson file"; continue; }
  [[ -f "$blueprint" ]] || fail "Lesson $lesson_number has no blueprint"
  [[ -f "$assessment" ]] || fail "Lesson $lesson_number has no assessment"
  [[ -f "$mapping" ]] || fail "Lesson $lesson_number has no source mapping"

  for metadata_file in "$blueprint" "$lesson_file" "$assessment" "$mapping"; do
    for field in lesson sequence title document_type difficulty estimated_study_time status validation_status last_reviewed intended_learner_level prerequisite related_lessons canonical_source scenario_version core_scenarios; do
      rg -q "^${field}:" "$metadata_file" || fail "$(basename "$metadata_file") is missing metadata field: $field"
    done
    rg -q '^difficulty: (Foundation|Core|Advanced)$' "$metadata_file" || fail "$(basename "$metadata_file") has invalid difficulty"
    rg -q '^estimated_study_time: [0-9]+$' "$metadata_file" || fail "$(basename "$metadata_file") has invalid estimated_study_time"
    rg -q '^status: (Draft|Review|Active)$' "$metadata_file" || fail "$(basename "$metadata_file") has invalid status"
    rg -q '^validation_status: (Not Validated|Validated)$' "$metadata_file" || fail "$(basename "$metadata_file") has invalid validation_status"
    rg -q '^last_reviewed: [0-9]{4}-[0-9]{2}-[0-9]{2}$' "$metadata_file" || fail "$(basename "$metadata_file") has invalid last_reviewed date"
    rg -q '^intended_learner_level: (Beginner PM|Experienced PM|Senior PM)$' "$metadata_file" || fail "$(basename "$metadata_file") has invalid intended_learner_level"
    if rg -q '^level:|^canonical_sources:|^last_updated:' "$metadata_file"; then
      fail "$(basename "$metadata_file") uses deprecated metadata fields"
    fi
    if rg -q '\[Scenario\]|\[Instructor Interpretation\]' "$metadata_file"; then
      fail "$(basename "$metadata_file") uses non-standard source labels"
    fi
  done
  for asset in learner/Artifact-Template.md learner/Workshop.md learner/Beginner-Checkpoint.md instructor/Thinking-Walkthrough.md instructor/Completed-Example.md instructor/Model-Answer.md instructor/Review-Checklist.md instructor/Scoring-Rubric.md; do
    [[ -f "$lesson_dir/$asset" ]] || fail "Lesson $lesson_number is missing learning asset: $asset"
  done
  for field in artifact_inputs artifact_outputs creator artifact_owner reviewer approval_authority approval_evidence next_lesson_usage acceptance_level; do
    rg -q "^${field}:|^[[:space:]]+${field}:" "$blueprint" || fail "Lesson $lesson_number blueprint is missing artifact field: $field"
  done
  for heading in 'Beginner Safety' 'Artifact Handoff'; do
    rg -qi "^## .*${heading}" "$lesson_file" || fail "Lesson $lesson_number is missing release heading: $heading"
  done
  if rg -q '^## .*Bridge to Next Lesson|^## เชื่อมไปยัง' "$lesson_file"; then
    fail "Lesson $lesson_number still contains a premature bridge before the final Lesson Connection"
  fi
  rg -q 'Incomplete.*Usable.*Professional|Incomplete / Usable / Professional' "$lesson_dir/instructor/Scoring-Rubric.md" "$lesson_dir/learner/Artifact-Template.md" || fail "Lesson $lesson_number does not expose all acceptance levels"

  for heading in 'Opening Professional Question' 'Why This Matters' 'Learning Objectives' 'Mental Model' 'PM Thinking' 'PM Decision Thinking' 'ERP Scenario' 'Hotel Booking Scenario' 'Interview Questions' 'PM Dictionary' 'Workshop' 'Assessment' 'Executive Summary' 'Lesson Connection' 'AI Continuation Context'; do
    rg -qi "^## .*${heading}" "$lesson_file" || fail "Lesson $lesson_number is missing: $heading"
  done
done

for capstone_file in \
  capstone/Capstone-Brief.md \
  capstone/learner/Primary-Track-Submission-Manifest-Template.md \
  capstone/learner/Comparative-Tailoring-Memo-Template.md \
  capstone/learner/Capstone-Workshop.md \
  capstone/learner/Executive-Defense-Brief-Template.md \
  capstone/instructor/Capstone-Thinking-Walkthrough.md \
  capstone/instructor/ERP-Completed-Handover-Manifest.md \
  capstone/instructor/Hotel-Booking-Completed-Delivery-Manifest.md \
  capstone/instructor/Comparative-Tailoring-Memo-Model-Answer.md \
  capstone/instructor/Review-Checklist.md \
  capstone/instructor/Scoring-Rubric.md \
  capstone/instructor/Executive-Defense-Evaluation-Guide.md; do
  [[ -f "$root/$capstone_file" ]] || fail "Missing capstone file: $capstone_file"
done

for capstone_gate in 'Artifact Completeness' 'Scenario Consistency' 'Integration' 'Executive Defense'; do
  rg -q "$capstone_gate" "$root/capstone/Capstone-Brief.md" || fail "Capstone Brief is missing gate: $capstone_gate"
done
rg -q '45 ล้านบาท.*60 ล้านบาท' "$root/capstone/Capstone-Brief.md" || fail 'Capstone Brief is missing ERP budget consistency guardrail'
rg -q 'Do not copy canonical artifacts' "$root/capstone/learner/Primary-Track-Submission-Manifest-Template.md" || fail 'Capstone manifest must prohibit copied canonical artifacts'

if rg -n 'file:///|/Users/[^ ]*/Documents/' "$root/lessons" --glob '*.md' >/dev/null; then
  fail 'Machine-specific absolute links found in Markdown'
fi

if (( failures > 0 )); then
  printf '\nRepository validation found %s issue(s).\n' "$failures" >&2
  exit 1
fi

printf 'Repository validation passed.\n'

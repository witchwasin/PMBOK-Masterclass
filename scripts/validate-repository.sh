#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
failures=0

fail() { printf 'FAIL: %s\n' "$1" >&2; failures=$((failures + 1)); }

for lesson_number in $(seq -w 1 16); do
  lesson_dir="$root/lessons/lesson-$lesson_number"
  lesson_file=$(find "$lesson_dir" -maxdepth 1 -name "Lesson-${lesson_number}_2-*.md" -print -quit)
  assessment="$lesson_dir/Lesson-${lesson_number}_3-Assessment.md"
  mapping="$lesson_dir/Lesson-${lesson_number}_4-Source-Mapping.md"

  [[ -n "$lesson_file" ]] || { fail "Lesson $lesson_number has no main lesson file"; continue; }
  [[ -f "$assessment" ]] || fail "Lesson $lesson_number has no assessment"
  [[ -f "$mapping" ]] || fail "Lesson $lesson_number has no source mapping"

  for heading in 'Opening Professional Question' 'Why This Matters' 'Learning Objectives' 'Mental Model' 'PM Thinking' 'PM Decision Thinking' 'ERP Scenario' 'Hotel Booking Scenario' 'Interview Questions' 'PM Dictionary' 'Workshop' 'Assessment' 'Executive Summary' 'Lesson Connection' 'AI Continuation Context'; do
    rg -qi "^## .*${heading}" "$lesson_file" || fail "Lesson $lesson_number is missing: $heading"
  done
done

if rg -n 'file:///|/Users/[^ ]*/Documents/' "$root/lessons" --glob '*.md' >/dev/null; then
  fail 'Machine-specific absolute links found in Markdown'
fi

if (( failures > 0 )); then
  printf '\nRepository validation found %s issue(s).\n' "$failures" >&2
  exit 1
fi

printf 'Repository validation passed.\n'

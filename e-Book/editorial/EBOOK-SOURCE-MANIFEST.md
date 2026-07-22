---
title: E-book Source Manifest
document_type: E-book Editorial Control
status: Active
created_on: 2026-07-22
---

# E-book Source Manifest

## Source Repository

| Field | Value |
|---|---|
| Repository | `https://github.com/witchwasin/PMBOK-Masterclass.git` |
| Source branch | `main` |
| Source commit | `46a98a66d55fb8ee425c6094f8e2248e3a141ef6` |
| Working branch | `codex/ebook-production` |
| Source validation command | `bash scripts/validate-repository.sh` |
| Source validation result | Passed |

## Remote

```text
origin  https://github.com/witchwasin/PMBOK-Masterclass.git (fetch)
origin  https://github.com/witchwasin/PMBOK-Masterclass.git (push)
```

## Initial Git Status

Recorded before creating this control package:

```text
?? .DS_Store
```

The untracked `.DS_Store` file is outside the e-book production scope and must not be touched unless the repository owner requests cleanup.

## Source Scope

The source state includes:

- `README.md`
- `governance/`
- `references/`
- `scenarios/`
- `lessons/lesson-01/` through `lessons/lesson-16/`
- `capstone/`
- `repository/`
- `scripts/validate-repository.sh`

## Production Boundary

E-book production may write only inside `e-Book/` unless the repository owner explicitly approves another path. No commit or push is allowed until separately requested.


---
title: Artifact Dependency Map
document_type: Learning Spine
version: 1.0
status: Active
last_updated: 2026-07-22
---

# PMBOK Masterclass — Artifact Dependency Map

## Batch 1 — Foundation to Integration

```text
L01 PM Learning Baseline
  blind spots + value assumptions
        ↓
L02 Project vs Operation Analysis + Value Chain
  project boundary + outcome + transition owner
        ↓
L03 Lifecycle + Process Group Map
  phases + management flow + gates + feedback
        ↓
L04 PM Coverage + Cross-impact Map
  dependencies + impact owners + decision route
        ↓
L05 Project Charter + Governance + Change Decision Record
  authorization + decision rights + approved baseline change
        ↓
L06 Stakeholder Register + Engagement Strategy
```

## Batch 2 — Stakeholder Need to Acceptance

```text
L05 Charter + Governance
        ↓
L06 Stakeholder Register + Engagement Strategy
  stakeholder need + influence + acceptance role
        ↓
L07 Requirements + Scope Statement + WBS + WBS Dictionary
  testable need + boundary + work package
        ↓
L08 Activity List + Dependency Network + Master Schedule
  activity logic + milestone + time-phased work
        ↓
L09 Cost Estimate + Cost Baseline + Performance Forecast
  approved funding use + actual/earned work + forecast
        ↓
L10 Quality Plan + Acceptance Criteria + Test Strategy
  requirement-to-test evidence + acceptance authority
        ↓
L11 Resource Plan + RACI
```

## Traceability Rules

1. ห้ามสร้าง Business Need หรือ Objective ใหม่ในบทหลังโดยไม่เปิด Change Decision
2. Output ของบทก่อนต้องผ่านอย่างน้อยระดับ `Usable`
3. ทุก Artifact ต้องมี Creator, Owner, Reviewer, Approval Authority และ Approval Evidence
4. หาก Input ยัง `Incomplete` ให้หยุดและแก้ upstream Artifact ก่อน
5. Scenario facts มาจาก Scenario Master; assumptions ต้องติดป้ายและมี validation owner

## End-to-End Traceability Target

```text
Business Need → Objective → Requirement → Scope → WBS
→ Activity → Schedule → Cost → Quality → Risk
→ Acceptance → Handover → Benefit
```

Batch 1 รับผิดชอบช่วง Business Need → Objective → authorization/governance และสร้าง control point สำหรับส่งต่อ Requirements/Stakeholder work ใน Batch 2

# Completed Example — ERP Reporting Scope

## Requirement

`REQ-RPT-01`: CFO ต้องดู close-cycle status และ reconciliation exceptions รายวันระหว่าง close; evidence คือ approved dashboard fields, role access และ UAT result

## Boundary

- In: Finance operational reports required for 15 → 5 day close outcome
- Out: Enterprise BI platform, CRM analytics และ ad-hoc reports ที่ไม่มี approved decision/use case

## WBS Fragment

```text
1.0 ERP Reporting Deliverable
  1.1 Reporting Requirements Baseline
  1.2 Finance Operational Reports
    1.2.1 Close Status Dashboard
    1.2.2 Reconciliation Exception Report
  1.3 Reporting Acceptance
```

Work package 1.2.1 มี Owner, data source, access boundary และ UAT acceptance; “จัดประชุม design” เป็น activity ของ L08 ไม่ใช่ deliverable

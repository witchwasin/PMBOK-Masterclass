---
title: ERP Transformation — Scenario Master
document_type: Scenario Definition
version: 1.0
status: Draft
last_updated: 2026-07-22
usage: ทุก Lesson ต้องอ้างอิง Scenario Master นี้ ห้ามสร้างตัวเลขหรือข้อเท็จจริงใหม่โดยไม่ update ไฟล์นี้
---

# Scenario A — ERP Transformation

> **ข้อมูลในไฟล์นี้เป็น Teaching Scenario ที่สร้างขึ้นเพื่อการเรียนรู้ ไม่ใช่ข้อเท็จจริงจากโครงการจริง**

## Related Teaching Walkthrough

- [ERP End-to-End PM Walkthrough](./ERP-END-TO-END-PM-WALKTHROUGH.md) — ใช้สอนแบบ step-by-step ตั้งแต่ business need, initiating, planning, delivery, control, go-live, hypercare จนถึง benefits review

---

## 1. Business Background

**บริษัท:** บริษัท สยาม อินดัสเทรียล กรุ๊ป จำกัด (Siam Industrial Group — SIG)

- อุตสาหกรรม: ผลิตและจำหน่ายสินค้าอุปโภคบริโภค (FMCG)
- พนักงาน: ~2,000 คน
- สาขา: สำนักงานใหญ่กรุงเทพฯ + โรงงาน 2 แห่ง (สมุทรปราการ, ระยอง) + คลังสินค้า 3 แห่ง + ศูนย์กระจายสินค้า 5 แห่ง
- ระบบปัจจุบัน: ระบบ Legacy แยกแต่ละหน่วยงาน (บัญชีใช้ระบบ A, คลังใช้ระบบ B, การผลิตใช้ Excel + ระบบ C) ไม่เชื่อมต่อกัน
- ปัญหาหลัก: ข้อมูลไม่ตรงกัน, ปิดงบล่าช้า 15 วัน, ไม่มี Real-time Visibility, การวางแผนการผลิตอ้างอิงข้อมูลเก่า

## 2. Business Need

> เปลี่ยนระบบ ERP ทั้งองค์กรเพื่อรวมศูนย์ข้อมูลและกระบวนการทำงาน ให้ผู้บริหารมี Real-time Visibility สำหรับการตัดสินใจ และลดเวลาปิดงบจาก 15 วันเหลือ 5 วัน

## 3. Project Objectives

1. รวม 6 ระบบ Legacy เป็นระบบ ERP เดียว
2. ครอบคลุม 5 โมดูลหลัก: Finance & Accounting (FI), Sales & Distribution (SD), Materials Management (MM), Production Planning (PP), Human Capital Management (HCM)
3. เชื่อมต่อกับระบบภายนอก: ธนาคาร (Payment), กรมสรรพากร (e-Tax), ระบบขนส่ง (TMS)
4. ปิดงบได้ภายใน 5 วันทำการ (จากเดิม 15 วัน)
5. ผู้ใช้ทุกหน่วยงานสามารถทำงานบนระบบเดียวกันได้ภายใน 3 เดือนหลัง Go-live

## 4. Scope

### In Scope

- 5 โมดูล: FI, SD, MM, PP, HCM
- Data Migration จากระบบเดิมทั้ง 6 ระบบ
- Integration กับ Banking, e-Tax, TMS
- User Training ทุกหน่วยงาน
- Parallel Run 1 เดือน
- Cutover และ Go-live
- Hypercare Support 3 เดือนหลัง Go-live

### Out of Scope

- CRM (Customer Relationship Management) — จะทำใน Phase 2
- Business Intelligence / Advanced Analytics — จะทำหลัง Stabilization
- Mobile Application สำหรับ Field Sales — จะทำใน Phase 3
- การเปลี่ยนแปลง Hardware ของโรงงาน (IoT, PLC)

## 5. Stakeholders

| Stakeholder | Role | Power | Interest | Strategy |
|---|---|---|---|---|
| คุณสมชาย — CEO | Executive Sponsor | High | High | Manage Closely |
| คุณวิภา — CFO | Business Owner (Finance) | High | High | Manage Closely |
| คุณธนา — VP Operations | Process Owner (Production + Warehouse) | High | Medium | Keep Satisfied |
| คุณนิดา — HR Director | Process Owner (HCM) | Medium | Medium | Keep Informed |
| คุณอรุณ — IT Director | Technical Owner | High | High | Manage Closely |
| คุณพล — Procurement Manager | Process Owner (MM) | Medium | High | Keep Informed |
| คุณมานะ — Sales Director | Process Owner (SD) | High | Medium | Keep Satisfied |
| พนักงานหน้างาน (Key Users) | End Users (~80 คน) | Low | High | Keep Informed |
| พนักงานทั่วไป (~1,500 คน) | End Users | Low | Low | Monitor |
| บริษัท TechConsult จำกัด | System Integrator (SI) | Medium | High | Manage Closely |
| ERP Vendor | Software License Provider | Medium | Medium | Keep Satisfied |

## 6. Organization Structure

- **โครงสร้าง:** Strong Matrix — PM เป็น Full-time, มี Project Office
- **Steering Committee:** CEO, CFO, VP Operations, IT Director — ประชุมทุก 2 สัปดาห์
- **Project Manager:** คุณเอก (จาก IT, Full-time PM)
- **PMO Coordinator:** 1 คน
- **Functional Leads:** 5 คน (คนละโมดูล) — จากหน่วยธุรกิจ
- **Key Users:** 80 คน (เลือกจากแต่ละหน่วยงาน)
- **SI Team:** 15 คน (Consultants + Developers + Data Migration Specialists)

## 7. Vendor

- **System Integrator:** บริษัท TechConsult จำกัด
- **Contract Type:** Fixed-Price สำหรับ Implementation + Time & Material สำหรับ Customization เพิ่มเติม
- **Contract Value:** 35 ล้านบาท (Fixed) + ไม่เกิน 5 ล้านบาท (T&M)
- **Milestone Payments:** 6 งวด (Kick-off 10%, Blueprint 15%, Build 25%, SIT 15%, UAT 20%, Go-live 15%)
- **SLA:** Hypercare response time: Critical 2 ชม., High 4 ชม., Medium 8 ชม.
- **Warranty:** 6 เดือนหลัง Go-live

## 8. Constraints

1. **Go-live Date:** ต้อง Go-live ก่อนเริ่มปีงบประมาณใหม่ (1 ตุลาคม)
2. **Delivery Working Budget:** ไม่เกิน 45 ล้านบาท สำหรับค่า implementation ที่ทีมควบคุมได้ (SI, internal delivery cost และ contingency ระดับโครงการ); License และ Management Reserve ใช้ approval แยกต่างหาก
3. **Key Users ต้องทำงานคู่ขนาน:** ไม่สามารถ Dedicate Full-time ให้โครงการได้
4. **Data Migration:** ข้อมูลย้อนหลัง 3 ปีต้อง Migrate
5. **Regulatory:** ระบบ Finance ต้อง comply กับ BOI, กรมสรรพากร, มาตรฐานบัญชี

## 9. Assumptions

1. Steering Committee ประชุมได้ทุก 2 สัปดาห์ตลอดโครงการ
2. Key Users สามารถให้เวลาโครงการได้ 40% ของเวลาทำงาน
3. Legacy Data สามารถ Extract ได้โดยไม่ต้องแก้ไขระบบเดิม
4. Network Infrastructure เพียงพอ ไม่ต้องอัปเกรด
5. ไม่มี Customization เกิน 20% ของ Standard Functionality

## 10. Key Risks (Pre-project)

| Risk | Probability | Impact | Strategy | Owner |
|---|---|---|---|---|
| Data Quality ต่ำ ทำให้ Migration ล่าช้า | High | High | Mitigate — Data Cleansing ก่อน Migration | คุณอรุณ (IT Director) |
| Key Users ไม่พร้อมเพราะงานประจำเยอะ | High | High | Mitigate — จัด Backfill + ทำ Schedule ล่วงหน้า | คุณเอก (PM) |
| Scope Creep จาก Process Owner | Medium | High | Mitigate — Freeze Scope หลัง Blueprint + Change Control | คุณเอก (PM) |
| Vendor ส่ง Consultant ไม่ตรง Profile | Medium | Medium | Transfer — ระบุ Named Resources ในสัญญา | คุณเอก (PM) |
| User Resistance ที่โรงงาน | High | Medium | Mitigate — Change Champion Program | คุณธนา (VP Ops) |
| Go-live ล่าช้าเกินปีงบประมาณ | Medium | High | Avoid — Fast Track SIT ถ้าจำเป็น | Steering Committee |

## 11. Timeline

| Phase | Duration | Period |
|---|---|---|
| Project Initiation | 2 สัปดาห์ | เดือนที่ 1 |
| Blueprint (As-Is / To-Be) | 8 สัปดาห์ | เดือนที่ 1–3 |
| Build & Configuration | 12 สัปดาห์ | เดือนที่ 3–6 |
| System Integration Test (SIT) | 4 สัปดาห์ | เดือนที่ 6–7 |
| User Acceptance Test (UAT) | 4 สัปดาห์ | เดือนที่ 7–8 |
| Data Migration (Final) | 2 สัปดาห์ | เดือนที่ 8 |
| Parallel Run | 4 สัปดาห์ | เดือนที่ 8–9 |
| Cutover & Go-live | 2 สัปดาห์ | เดือนที่ 9 |
| Hypercare | 12 สัปดาห์ | เดือนที่ 9–12 |
| **Total:** | **~12 เดือน** | — |

## 12. Budget Context

| Category | Budget (ล้านบาท) |
|---|---|
| ERP License (3 ปี) | 8.0 |
| System Integrator (Fixed) | 35.0 |
| Internal Project Cost (PM, Key Users, Backfill) | 5.0 |
| Infrastructure (Cloud) | 3.0 |
| Training | 2.0 |
| Contingency Reserve (10%) | 5.0 |
| Management Reserve | 2.0 |
| **Total Funding Envelope** | **60.0** |

> **Budget baseline lock:** Working Budget = **45 ล้านบาท**; Total Funding Envelope = **60 ล้านบาท** (รวม License ที่จ่ายแยกและ Management Reserve ที่ต้องขออนุมัติ CEO). ทุกบทต้องระบุให้ชัดว่ากำลังพูดถึงตัวเลขใด และห้ามใช้แทนกัน.

## 13. Deliverables

1. Project Charter (signed by Sponsor)
2. Blueprint Document (As-Is / To-Be per module)
3. Configured ERP System (5 modules)
4. Integrated System (Banking, e-Tax, TMS)
5. Migrated Data (3 years historical)
6. SIT Report (pass criteria met)
7. UAT Report (signed by Process Owners)
8. Training Materials + Completion Records
9. Cutover Plan + Rollback Plan
10. Go-live Sign-off
11. Hypercare Report (monthly)
12. Project Closure Report + Lessons Learned

## 14. Expected Outcomes

| Timeframe | Outcome | Metric |
|---|---|---|
| 3 เดือนหลัง Go-live | ผู้ใช้สามารถทำงานบนระบบใหม่ได้ | ≥80% Transaction ผ่านระบบใหม่ |
| 6 เดือนหลัง Go-live | ปิดงบได้เร็วขึ้น | ≤5 วันทำการ (จากเดิม 15 วัน) |
| 12 เดือนหลัง Go-live | Real-time Visibility สำหรับผู้บริหาร | Dashboard ใช้งานได้จริง |

## 15. Benefits

| Benefit | Measurement | Target |
|---|---|---|
| ลดเวลาปิดงบ | วันที่ใช้ปิดงบ | 15 → 5 วัน |
| ลดข้อผิดพลาดจากการ Key ข้อมูลซ้ำ | จำนวน Error per month | ลดลง 70% |
| Real-time Inventory Visibility | Inventory Accuracy | ≥95% |
| ลดต้นทุนจัดซื้อ (Consolidated PO) | Procurement Saving | 5% ของ Spend |

## 16. Operating Model (Post Go-live)

- **System Owner:** IT Director (คุณอรุณ)
- **Process Owners:** เจ้าของกระบวนการแต่ละโมดูล (5 คน)
- **Application Support Team:** 3 คน (จาก IT)
- **Vendor Support:** SLA-based Maintenance Contract
- **Enhancement Request:** ผ่าน Change Advisory Board (CAB)

---

## Scenario Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-07-22 | Initial scenario definition |

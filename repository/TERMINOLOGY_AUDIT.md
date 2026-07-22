---
title: Terminology Audit
document_type: Terminology Audit
audit_date: 2026-07-22
---

# PMBOK Masterclass — Terminology Audit

> **Pass 0 Deliverable** — ตรวจคำศัพท์ทั้ง repository

---

## 1. Mandatory Consistency Terms (ตาม §11 Validation)

| Term (EN) | คำที่ใช้ใน L01 | คำที่ใช้ใน L02-16 | สอดคล้อง? | Action |
|---|---|---|---|---|
| Project | โครงการ | โครงการ | ✅ | — |
| Operation / Routine Work | งานประจำ | งานประจำ / Routine Work | ✅ | Standardize to "งานประจำ (Routine Work / Operation)" |
| Output | ผลผลิต / Output | Output | ⚠️ | L01 ใช้ "ผลผลิต" บาง, L02 ใช้ "Output" ตรง → Lock as "Output (ผลผลิต)" |
| Outcome | ผลลัพธ์ / Outcome | Outcome | ✅ | Lock as "Outcome (ผลลัพธ์เชิงธุรกิจ)" |
| Business Value | Business Value | Business Value | ✅ | — |
| Benefit | Benefit | Benefit | ✅ | — |
| Deliverable | ผลส่งมอบ | Deliverable / ผลส่งมอบ | ⚠️ | Lock as "Deliverable (ผลส่งมอบ)" |
| Requirement | Requirement | ความต้องการ / Requirement | ⚠️ | Lock as "Requirement (ข้อกำหนดความต้องการ)" |
| Scope | Scope | ขอบเขต / Scope | ⚠️ | Lock as "Scope (ขอบเขต)" |
| Product Scope vs Project Scope | ไม่ได้กล่าวถึง | ไม่แยกชัด (L07) | ❌ | ต้องแยกชัดใน L07 |
| Work Package | Work Package | Work Package | ✅ | — |
| Activity | Activity / กิจกรรม | Activity | ✅ | Lock as "Activity (กิจกรรม)" |
| Milestone | Milestone | Milestone | ✅ | — |
| Risk vs Issue | ไม่ได้กล่าวถึง | Risk / ความเสี่ยง, Issue / ประเด็น | ⚠️ | Lock terms ใน L13 |
| Verification vs Validation | ไม่ได้กล่าวถึง | ไม่แยกชัด (L10) | ❌ | ต้องแยกชัดใน L10 |
| Quality vs Grade | ไม่ได้กล่าวถึง | Quality vs Grade (L10) | ⚠️ | OK แต่ต้องลึกขึ้น |
| Sponsor | Sponsor / ผู้สนับสนุน | Sponsor | ✅ | Lock as "Sponsor (ผู้สนับสนุนโครงการ)" |
| Business Owner vs Product Owner | ไม่แยก | ไม่แยก | ❌ | ต้องแยกใน L06 และ L15 |
| Change Request vs Defect Repair | ไม่แยก | ไม่แยก | ❌ | ต้องแยกใน L05 |
| Procurement vs Purchasing | ไม่กล่าว | ใช้ Procurement | ✅ | — |
| Predictive vs Waterfall | ใช้ทั้ง 2 คำ | ใช้ทั้ง 2 คำ | ⚠️ | Lock: "Predictive (มักเรียก Waterfall)" |
| Agile vs Scrum | แยกชัด | แยกชัด (L15) | ✅ | — |
| Phase vs Process Group | ไม่แยก | แยก (L03) แต่ไม่ลึก | ⚠️ | ต้องทำให้ชัดใน L03 |
| Knowledge Area | Knowledge Area | Knowledge Area | ✅ | — |
| Tailoring | Tailoring / การปรับวิธี | Tailoring | ✅ | Lock as "Tailoring (การปรับแนวทาง)" |
| Acceptance | Acceptance | Acceptance / การยอมรับ | ⚠️ | Lock term |
| Handover | Handover | ส่งมอบ / Transition | ⚠️ | Lock as "Handover (การส่งมอบ)" |
| Transition to Operation | Transition to Operation | Transition to Operation | ✅ | — |

---

## 2. PMBOK 6 vs PMBOK 7 Term Blending Check

| Area | ปัญหา | Lesson | Severity |
|---|---|---|---|
| 5 Process Groups | ใช้เป็น organizing structure ราวกับ PMBOK 7 ยังเป็นแบบนี้ | L03, L04 | 🟡 Medium |
| 10 Knowledge Areas | ใช้เป็น course structure ทั้งหมด (PMBOK 6 approach) | L04-14 | 🟡 Medium |
| PMBOK 7 Principles | ไม่ได้กล่าวถึงอย่างเป็นระบบ | ทุกบท | 🟡 Medium |
| PMBOK 7 Performance Domains | ไม่ปรากฏ | ทุกบท | 🟡 Medium |
| Value Delivery System | กล่าวถึงบางส่วนใน L01, L02 | L01, L02 | 🟡 Medium |

> **Note:** ตาม Open Questions decision, course จะ "ใช้ตาม Canonical Source (ผสม) + label ให้ชัด" — ดังนั้นต้องเพิ่ม label ใน Pass 3 ว่าส่วนใดมาจาก PMBOK 6 และส่วนใดมาจาก PMBOK 7

---

## 3. Deprecated or Inconsistent Translations Found

| Term | การแปลที่พบ | ปัญหา | Action |
|---|---|---|---|
| Stakeholder | ผู้มีส่วนได้ส่วนเสีย / ผู้เกี่ยวข้อง | ใช้สลับกัน | Lock: "Stakeholder (ผู้มีส่วนได้ส่วนเสีย)" |
| Scope Creep | Scope Creep / การขยายขอบเขตแบบคืบคลาน | ใช้สลับ | Lock: "Scope Creep (การขยายขอบเขตแบบไม่ผ่านอนุมัติ)" |
| Earned Value | Earned Value / มูลค่าที่ได้ | ใช้สลับ | Lock: "Earned Value — EV (มูลค่างานที่ทำเสร็จจริง)" |
| Iron Triangle | Iron Triangle | ไม่มีคำอธิบายภาษาไทยที่สอดคล้อง | Lock: "Iron Triangle (สามเหลี่ยมเหล็ก: Scope, Schedule, Cost)" |

---

## 4. Missing Terms (ต้องเพิ่มใน PM_GLOSSARY.md)

ศัพท์ต่อไปนี้ถูกใช้ในบทเรียนแต่ไม่มี Glossary entry:

| Term | ปรากฏใน Lesson | ต้องอยู่ใน |
|---|---|---|
| Progressive Elaboration | L03 | PM_GLOSSARY |
| Tacit Knowledge / Explicit Knowledge | L05 | PM_GLOSSARY |
| Integrated Change Control (ICC) | L05 | PM_GLOSSARY |
| Power-Interest Grid | L06 | PM_GLOSSARY |
| WBS Dictionary | L07 | PM_GLOSSARY |
| Float / Slack | L08 | PM_GLOSSARY |
| Cost of Quality (COQ) | L10 | PM_GLOSSARY |
| RACI | L11 | PM_GLOSSARY |
| Risk Register | L13 | PM_GLOSSARY |
| Probability-Impact Matrix | L13 | PM_GLOSSARY |
| TOR / SOW | L14 | PM_GLOSSARY |
| Sprint | L15 | PM_GLOSSARY |
| Product Backlog | L15 | PM_GLOSSARY |
| WIP Limit | L15 | PM_GLOSSARY |
| Hybrid Approach | L16 | PM_GLOSSARY |

---

## 5. Summary

| Category | Count |
|---|---|
| Terms checked | 30 |
| ✅ Consistent | 15 |
| ⚠️ Inconsistent (need locking) | 11 |
| ❌ Missing distinction | 4 |
| Missing Glossary entries | 15 |
| PMBOK 6/7 blending issues | 5 |

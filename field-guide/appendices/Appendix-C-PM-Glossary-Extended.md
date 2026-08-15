---
title: "Appendix C — PM Glossary (ฉบับเล่ม)"
book: "PM Delivery Guide (Ver.2)"
document_type: Appendix
version: 1.0
status: Draft
last_reviewed: 2026-08-13
note: "คำศัพท์ทั้งหมดถูก sync เข้า docs/PM_GLOSSARY.md แล้ว (ส่วน field-guide additions) — ไฟล์นี้คือฉบับรวมสำหรับผู้อ่านเล่ม ไม่ใช่ glossary แยก"
---

# Appendix C — PM Glossary (ฉบับรวมสำหรับเล่ม)

> **สำคัญ:** คำศัพท์นี้เป็นฉบับรวมของเล่ม — คำทั้งหมดถูกเพิ่มเข้า **`docs/PM_GLOSSARY.md`** (ส่วน "field-guide additions") แล้ว ไม่ใช่ glossary ที่ขัดกัน — ดูไฟล์ต้นทางเป็น authoritative

## C.1 คำศัพท์ใหม่ของเล่ม (PMBOK 8 / workflow A–H)

| Term (EN) | คำอธิบาย (TH) | ใช้ในบท |
|---|---|---|
| Bid / No-Bid | การตัดสินใจเสนอราคาหรือไม่ — ตัดสินด้วย value, capability, capacity, risk | Ch.1 |
| Business Case | เหตุผลทางธุรกิจของโครงการ — ผูก value, cost, timeline, risk, approval | Ch.1 |
| CCB | Change Control Board — อนุมัติ change ที่กระทบ baseline ตาม threshold | Ch.2, Ch.7 |
| Cutover | การสลับจากระบบเดิมไประบบใหม่ใน Production | Ch.9 |
| Definition of Done | เกณฑ์ว่างานเสร็จจริง (build + review + test + security + deploy + evidence) | Ch.6 |
| Definition of Ready | เกณฑ์ว่างานพร้อมเริ่ม (scope, AC, test data, owner, estimate) | Ch.6 |
| Discovery | การสำรวจทำความเข้าใจปัญหาก่อนออก solution | Ch.1 |
| Fixed Price | ราคาคงที่ — เหมาะกับ scope ชัด | Ch.1, Ch.5 |
| Go/No-Go | การตัดสินใจขึ้น Production — ตัดสินจาก readiness + risk + rollback + support | Ch.8, Ch.9 |
| Governance | กลไกตัดสินใจและอนุมัติ — ใครตัดสินใจอะไร ตาม threshold ใด | Ch.2 |
| Hypercare | ช่วงสนับสนุนเข้มหลัง Go-live — จนเข้าสู่สภาวะเสถียร | Ch.9 |
| Impact Analysis | การวิเคราะห์ผลกระทบครบทุกด้านก่อน change | Ch.7 |
| Issue | ปัญหาที่เกิดแล้ว — ต้องมี owner, action, escalation | Ch.5, Ch.7 |
| Make-or-Buy | ทำเองหรือซื้อ — ตัดสินจาก core, cost, risk, capacity | Ch.5 |
| MVP | Minimum Viable Product — scope ต่ำสุดที่พิสูจน์ value | Ch.3, Ch.4 |
| Opportunity | โอกาสทางธุรกิจ — lead/RFP ที่ยังไม่ใช่โครงการ | Ch.1 |
| PIR | Post-Implementation Review — ทบทวนหลัง implement เทียบ target | Ch.10 |
| Proposal | ข้อเสนอโครงการ — ยังไม่ผูกพันเท่า SOW | Ch.1 |
| RAID | Risks, Assumptions, Issues, Dependencies — log กลาง | Ch.2 |
| Release Readiness | ความพร้อมขึ้น Production (F.7) | Ch.8 |
| Residual Risk | ความเสี่ยงคงเหลือหลัง response — ต้องมี owner | Ch.5 |
| Rollback | การย้อนกลับระบบ — แผน restore เมื่อ go-live ผิดพลาด | Ch.9 |
| ROM | Rough Order of Magnitude — ประมาณการระดับสูง ไม่ใช่ commitment | Ch.1 |
| RTM | Requirements Traceability Matrix — requirement→test→acceptance | Ch.3, Ch.8 |
| SIT | System Integration Test — ทดสอบรวมระบบ | Ch.8 |
| SOW | Statement of Work — ขอบเขตงานที่ผูกพันตามสัญญา | Ch.1 |
| Stabilization | การเข้าสู่สภาวะเสถียรหลัง go-live | Ch.9 |
| T&M | Time and Material — จ่ายตามเวลา/วัสดุ ต้องมี cap + evidence | Ch.1, Ch.5 |
| Test Strategy | แนวทางการทดสอบ — วางแผน Ch.5, ผลจริง Ch.8 | Ch.5, Ch.8 |
| UAT | User Acceptance Test — ผู้ใช้ธุรกิจตรวจรับ | Ch.8 |
| Workstream | สายงานย่อยของโครงการ — แยกตาม deliverable | ทั่วเล่ม |
| Vendor | ผู้ขาย/คู่สัญญา — จัดการผ่าน contract/SLA/acceptance | Ch.1, Ch.5 |

## C.2 คำศัพท์เดิม (จาก PM_GLOSSARY.md) ที่เล่มใช้อ้างอิง

| Term (EN) | คำอธิบายสั้น |
|---|---|
| Acceptance | การยอมรับผลงานอย่างเป็นทางการ (≠ Approval) |
| Contingency Reserve | สำรองสำหรับ known-unknowns — PM ใช้ตาม governance |
| Critical Path | เส้นทางที่กำหนด Project Duration |
| Earned Value (EV) | มูลค่างานที่เสร็จจริง (วัดเป็นเงิน) |
| Iron Triangle | Scope–Schedule–Cost กระทบกัน |
| Management Reserve | สำรองสำหรับ unknown-unknowns — Sponsor เท่านั้น |
| Project Charter | เอกสารเริ่มต้นโครงการ — Sponsor ออก |
| RACI | Responsible, Accountable, Consulted, Informed |
| Scope Creep | ขอบเขตบานโดยไม่ผ่าน change control |
| Sponsor | ผู้สนับสนุนโครงการ — ทรัพยากร + อนุมัติ |
| Tailoring | การปรับวิธีบริหารให้เหมาะบริบท |
| Verification / Validation | ตาม spec / ตาม need |
| WBS | โครงสร้างจำแนกงานตาม deliverable |
| WIP Limit | จำกัดงานค้าง (Kanban) |

> ดูคำเต็ม + การใช้ผิดที่พบบ่อยได้ที่ `../../docs/PM_GLOSSARY.md`

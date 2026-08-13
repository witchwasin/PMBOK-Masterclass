---
title: "Appendix F — Problem → Chapter Index (เปิดเมื่อมีปัญหา)"
book: "PM Delivery Guide (Ver.2)"
document_type: Appendix
version: 1.0
status: Draft
last_reviewed: 2026-08-13
related_reference: ../../references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md
---

# Appendix F — Problem → Chapter Index

> หัวใจของ field manual: เจอปัญหาหน้างาน → เปิดตารางนี้ → ไปบทที่ตรง + ใช้ Checklist ท้ายบท และ Quick Reference Card — ไม่ต้องอ่านทั้งเล่ม

## วิธีใช้

1. ค้นหาประโยคที่ใกล้เคียงกับปัญหาที่เจอในตารางด้านล่าง
2. เปิดบทที่ชี้ไว้ (เนื้อหาหลัก) — ถ้าเร่งด่วนให้เปิด **Checklist ท้ายบท** ก่อน
3. ถ้าปัญหาเกิดจากงานในบทก่อนหน้า ให้ดูคอลัมน์ "อาจต้องย้อนไป" เพื่อตรวจ root cause
4. Appendix เสริม: [A — Artifact Catalogue](Appendix-A-Artifact-Catalogue.md), [B — Golden Rules](Appendix-B-Golden-Rules-Poster.md), [E — Role/Output Matrix](Appendix-E-SDLC-Role-Output-Matrix.md)

## ตาราง Problem → Chapter

| # | ปัญหาที่เจอหน้างาน | บทหลัก | Checklist ท้ายบท | อาจต้องย้อนไป |
|---|---|---|---|---|
| 1 | ยังไม่มี Proposal/SOW ต้องประเมินราคาหรือตอบ RFP | Ch.1 | Ch.1 §11 | — |
| 2 | ลูกค้า/ฝ่ายขายกดดันให้รับปาก scope หรือราคา | Ch.1 | Ch.1 §11 | Ch.5 (risk) |
| 3 | Scope ยังคลุมเครือ ต้องแตกเป็นชิ้นงานให้ทีมทำได้ | Ch.3 | Ch.3 §11 | Ch.2 (charter) |
| 4 | Feature List ถูกเรียกเป็น "Scope ที่ชัด" แต่ยังไม่ครบ | Ch.3 | Ch.3 §11 | Ch.1 (basis) |
| 5 | ลูกค้าขอเพิ่ม/ลดขอบเขตกะทันหัน | Ch.7 | Ch.7 §11 | Ch.3 (baseline) |
| 6 | WBS แตกไม่ถูก (เช่น แตกตามแผนก ไม่ใช่ deliverable) | Ch.3 | Ch.3 §11 | — |
| 7 | ทำ Schedule ไม่ได้ เพราะ dependency/duration ไม่พร้อม | Ch.4 | Ch.4 §11 | Ch.3 (WBS) |
| 8 | โครงการล่าช้ากว่าแผน / critical path มีปัญหา | Ch.4, Ch.7 | Ch.4 §11, Ch.7 §11 | Ch.3 (scope) |
| 9 | งบประมาณบานปลาย / ใช้เงินเกิน plan | Ch.7 | Ch.7 §11 | Ch.4 (cost baseline) |
| 10 | ต้องการรู้ว่าโครงการ "จริงๆ แล้ว" ไปได้ดีแค่ไหน | Ch.7 (EVM) | Ch.7 §11 | Ch.4 (baseline) |
| 11 | ทีมไม่พอ / คนเก่งถูกดึงไปงานอื่น / ไฟล์ทีมขาด | Ch.4 (Resource) | Ch.4 §11 | Ch.2 (RACI) |
| 12 | ทีมทำงานไม่ตรงตามที่ตกลง / Done ไม่มี evidence | Ch.6 | Ch.6 §11 | Ch.4 (plan), Ch.5 (QA plan) |
| 13 | QA กับ Dev ขัดแย้ง / test data ไม่พร้อม | Ch.6 | Ch.6 §11 | Ch.5 (test strategy) |
| 14 | อยากรู้ว่า "คุณภาพจะพอไหม" ก่อนส่งงาน | Ch.5 (Test Strategy), Ch.8 (QC) | Ch.5 §11, Ch.8 §11 | — |
| 15 | ผลทดสอบยังไม่ครบ/defect เยอะ แต่โดนกดให้ผ่าน | Ch.8 | Ch.8 §11 | Ch.5 (เกณฑ์ผ่าน) |
| 16 | ลูกค้า/PO อยากเซ็น UAT ทั้งที่ coverage ไม่ครบ | Ch.8 | Ch.8 §11 | Ch.5 (UAT plan) |
| 17 | เจอความเสี่ยงใหม่/ความเสี่ยงที่เคยล็อกเกิดจริง | Ch.5 | Ch.5 §11 | Ch.1 (assumption) |
| 18 | Vendor (PMS/2C2P) ไม่ส่งงานตามสัญญา/แก้ช้า | Ch.5 (Procurement) | Ch.5 §11 | Ch.1 (SOW) |
| 19 | สื่อสารกับ stakeholders ไม่ตรง / คนสำคัญไม่รู้เรื่อง | Ch.5 (Comms) | Ch.5 §11 | Ch.2 (register) |
| 20 | Stakeholder สำคัญไม่โผล่ / ไม่ให้ความร่วมมือ | Ch.2 | Ch.2 §11 | — |
| 21 | Sponsor อนุมัติด้วยวาจา / ไม่มี threshold ชัดเจน | Ch.2, Ch.7 | Ch.2 §11, Ch.7 §11 | — |
| 22 | พรุ่งนี้จะขึ้น Production ต้องตรวจความพร้อม | Ch.9 | Ch.9 §11 | Ch.8 (release readiness) |
| 23 | ต้องวางแผน cutover / กลัวขึ้นแล้วพัง | Ch.9 | Ch.9 §11 | Ch.8 (UAT) |
| 24 | ระบบขึ้นแล้ว error/performance มีปัญหา | Ch.9 (Hypercare) | Ch.9 §11 | Ch.8 (QC) |
| 25 | ต้องตัดสินใจ rollback หรือ fix-in-place | Ch.9 | Ch.9 §11 | — |
| 26 | งานเสร็จแล้วแต่ไม่รู้จะปิดโครงการยังไง | Ch.10 | Ch.10 §11 | Ch.9 (handover) |
| 27 | ไม่รู้ว่าใครรับงานต่อหลัง project จบ (ops/benefit owner) | Ch.10 | Ch.10 §11 | Ch.2 (charter roles) |
| 28 | ต้องสรุป lessons learned / closure report | Ch.10 | Ch.10 §11 | — |
| 29 | อยากรู้ภาพรวมว่า PM ต้องทำอะไรบ้างตลอดโครงการ | Ch.0 | Ch.0 §11 | Appendix E (role matrix) |
| 30 | ไม่รู้ว่าต้องสร้าง/ส่งเอกสารอะไรตอนไหน | Appendix A | — | Appendix E |
| 31 | ต้องการข้อควรระวังสรุป 1 หน้า | Appendix B | — | — |
| 32 | ไม่รู้คำศัพท์ PM ที่ใช้ในเล่มนี้ | Appendix C | — | governance/PM_GLOSSARY.md |

## ดัชนีย้อนกลับ: บท → ปัญหาที่บทนั้นตอบ

| บท | ปัญหาประเภทหลักที่บทนี้ตอบ |
|---|---|
| Ch.0 | ภาพรวมกรอบคิด PMBOK 8, วิธีใช้เล่ม (Study/Field Mode) |
| Ch.1 | Opportunity, Proposal, ROM/SOW, Fixed vs T&M, No-Bid |
| Ch.2 | Charter, PM authority, Stakeholder, Steering Committee |
| Ch.3 | Requirements, Scope Baseline, WBS, 100% Rule, MVP |
| Ch.4 | Schedule (CPM), Cost (EVM พื้นฐาน), Resource/RACI, Agile |
| Ch.5 | Risk register, Procurement/vendor, Comms plan, Test Strategy, Environment |
| Ch.6 | Execution, DoD, Manage Quality/Team, Daily control, Agile sprint |
| Ch.7 | Monitor, EVM analysis, Perform Integrated Change Control, Escalation |
| Ch.8 | QC/Control Quality, UAT, RTM, Release Readiness gate |
| Ch.9 | Cutover, Rollback, Go/No-Go, Hypercare, Stabilization |
| Ch.10 | Handover, Closure Report, Benefit Owner, Lessons Learned, Exit Criteria |

## หมายเหตุ (สำหรับผู้ทำเล่ม)

- ตารางนี้เป็น "ดัชนีเดียวของเล่ม" ที่ต้องอัปเดตทุกครั้งที่มีการย้าย/เพิ่มหัวข้อในบท — ตรวจใน Phase 4 (รวมเล่ม) ว่าหมายเลขหัวข้อ Checklist ยังตรง
- กรณีปัญหาแบบผสม (เช่น งบเกิน + ลูกค้าโกรธ) ให้เปิดบทที่ใกล้เคียงที่สุดก่อน แล้วใช้คอลัมน์ "อาจต้องย้อนไป" ไล่ root cause

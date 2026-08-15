# PM Delivery Guide

คู่มือ Project Management ภาษาไทย อิง **PMBOK® Guide 8th Edition** เรียงเนื้อหาตาม **ลำดับงานจริงของโครงการ A→H** (Pre-sales → Closure) แทนการเรียงตาม Knowledge Areas

ผู้เรียบเรียง: **Witchwasin K.**

> ถ้าต้องการเล่มที่เรียงตาม 10 Knowledge Areas แบบคลาสสิก (PMBOK 6+7) ดูที่ [`../e-Book/`](../e-Book) แทน

## เริ่มอ่าน

| ต้องการ | ไปที่ |
|---|---|
| อ่านรวดเดียวจบ (PDF) | [`pdf/PM-Delivery-Guide-Learner-Edition.pdf`](pdf/PM-Delivery-Guide-Learner-Edition.pdf) |
| ฉบับผู้สอน — รวมเฉลย + rubric | [`pdf/PM-Delivery-Guide-Complete-Edition.pdf`](pdf/PM-Delivery-Guide-Complete-Edition.pdf) |
| อ่านเป็น Markdown ทีละบท | ตารางสารบัญด้านล่าง |
| มีปัญหาหน้างาน อยากรู้ว่าไปบทไหน | [Appendix F — Problem-to-Chapter Index](appendices/Appendix-F-Problem-to-Chapter-Index.md) |

## สารบัญ

| บท | เนื้อหา | ช่วง Playbook |
|---|---|---|
| [Ch.0](chapters/ch-00/ch-00-learner.md) | PMBOK Primer — กรอบคิดสำหรับเล่มนี้ | — |
| [Ch.1](chapters/ch-01/ch-01-learner.md) | Pre-sales — จาก Opportunity ถึง Proposal/SOW | A |
| [Ch.2](chapters/ch-02/ch-02-learner.md) | Initiation — Charter, Stakeholder, Governance และ Kickoff | B |
| [Ch.3](chapters/ch-03/ch-03-learner.md) | Requirements, Scope และ WBS | C1–C6 |
| [Ch.4](chapters/ch-04/ch-04-learner.md) | Schedule, Cost และ Resource | C8–C13 |
| [Ch.5](chapters/ch-05/ch-05-learner.md) | Risk, Procurement, Communications, Environment และ Integrated Plan | C7 + C14–C19 |
| [Ch.6](chapters/ch-06/ch-06-learner.md) | Execution — ส่งมอบ Solution, บริหารทีม และ Manage Quality | D |
| [Ch.7](chapters/ch-07/ch-07-learner.md) | Monitoring, Controlling และ Change Control | E |
| [Ch.8](chapters/ch-08/ch-08-learner.md) | Verification, UAT และ Release Readiness | F |
| [Ch.9](chapters/ch-09/ch-09-learner.md) | Go-Live และ Hypercare | G |
| [Ch.10](chapters/ch-10/ch-10-learner.md) | Transition, Closure และ Benefit Handover | H |

แต่ละบทมี 3 ไฟล์: `-learner` (เนื้อหาสำหรับผู้เรียน), `-instructor` (โน้ตสำหรับผู้สอน), `-answer-key` (เฉลยและเกณฑ์ประเมิน)

## ภาคผนวก

| | |
|---|---|
| [A — Artifact Catalogue](appendices/Appendix-A-Artifact-Catalogue.md) | เอกสารทุกชิ้นที่ PM ต้องผลิต ใครใช้ต่อ และใช้ทำอะไร |
| [B — Golden Rules Poster](appendices/Appendix-B-Golden-Rules-Poster.md) | กฎที่สรุปจากทั้งเล่ม พิมพ์แปะโต๊ะได้ |
| [C — PM Glossary Extended](appendices/Appendix-C-PM-Glossary-Extended.md) | ศัพท์ทั้งเล่มพร้อมการใช้ผิดที่พบบ่อย |
| [D — Master Answer Key](appendices/Appendix-D-Master-Answer-Key.md) | เฉลยรวมทุกบท |
| [E — SDLC Role & Output Matrix](appendices/Appendix-E-SDLC-Role-Output-Matrix.md) | PM ทำอะไร ทีมทำอะไร output ไปใช้ต่อที่ไหน ([ฉบับพิมพ์ 1 หน้า](pdf/Appendix-E-SDLC-Role-Output-Matrix.pdf)) |
| [F — Problem-to-Chapter Index](appendices/Appendix-F-Problem-to-Chapter-Index.md) | เจอปัญหาแบบนี้ เปิดบทไหน |

## แหล่งอ้างอิงของเล่มนี้

โครง A→H มาจาก [PMBOK-Aligned End-to-End Project Delivery Playbook V2](../references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md) ส่วนกรณีศึกษาที่ใช้ตลอดเล่มถูกล็อกไว้ที่ [`../scenarios/`](../scenarios)

## การสร้าง PDF ใหม่

```bash
python3 field-guide/pdf/build_pdf.py
```

สคริปต์จะประกอบบททั้งหมดเป็น `book.html` / `book-learner.html` แล้วเรนเดอร์เป็น PDF ทั้งสองฉบับ (ใช้ weasyprint ถ้ามี ไม่งั้น fallback ไป Chrome headless) — ไฟล์ HTML ระหว่างทางไม่ถูก commit

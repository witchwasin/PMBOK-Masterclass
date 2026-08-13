---
title: "PM Delivery Guide Ver.2 — Master Plan"
document_type: Master Plan (Execution Handoff)
version: 1.0
status: Approved — Ready for FreeBuff to Execute
owner: User (Owner) — approved 2026-07-31
planner: Claude (this session)
executor: FreeBuff
reviewer: Claude (separate review pass, via Claude_Review_Feedback.md)
last_updated: 2026-07-31
---

# PM Delivery Guide Ver.2 — Master Plan

> **อ่านก่อนเริ่มทำ (สำหรับ FreeBuff):** เอกสารนี้คือแผนที่ได้รับอนุมัติจากเจ้าของ repo แล้ว งานของคุณคือ**ทำตามแผนนี้** ไม่ใช่ออกแบบใหม่ ถ้ามีจุดไม่ชัดเจน ติดปัญหา หรือไม่เห็นด้วยกับจุดไหน **ให้เขียนคำถาม/ข้อกังวลลงใน `FreeBuff_Fixed_Update.md`** (ไฟล์ในโฟลเดอร์เดียวกันนี้) แล้วรอ Claude ตอบใน `Claude_Review_Feedback.md` — ดูหัวข้อ "Collaboration Protocol" ท้ายเอกสารนี้สำหรับวิธีทำงานร่วมกัน

---

## 1. Context — ทำไมต้องทำงานนี้

Repo `PMBOK-Masterclass` มีเอกสารสอน PM สองสายที่แยกกันอยู่ตอนนี้:

1. **`e-Book/`** — หลักสูตร 16 บทตาม **PMBOK 6th+7th Edition** จัดเรียงตาม **10 Knowledge Areas** (Integration, Stakeholder, Scope, Schedule, Cost, Quality, Resource, Communications, Risk, Procurement) มี Learner Edition + Instructor Companion แยกกัน, validate ครบทุกบทแล้ว, export เป็น PDF แล้ว (`e-Book/pdf/PMBOK-Masterclass-Complete-Edition.pdf`) — เขียนแบบ pedagogy-first ใช้ Template 21 หัวข้อ (`governance/LESSON_TEMPLATE.md`)
2. **`field-guide/`** — โปรเจกต์ใหม่ อ้างอิง **PMBOK 8th Edition** (ฉบับปัจจุบันจริง ออกขาย ม.ค. 2026) จาก Playbook ภายนอกที่เก็บไว้ที่ `references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md` จัดเรียงตาม **workflow จริงที่โครงการเดินผ่าน A→H** (Pre-sales → Initiation → Detailed Planning → Execution → Monitoring/Change → Verification/UAT → Go-Live/Hypercare → Closure) — ออกแบบให้เปิดอ่านตอนมีปัญหาหน้างานได้ (field manual) — ตอนนี้มีแค่ Blueprint (`field-guide/BOOK-BLUEPRINT.md`) และ Appendix E ตัวเดียวที่เขียนจริงแล้ว (`field-guide/appendices/Appendix-E-SDLC-Role-Output-Matrix.md` + PDF คู่กัน)

**เจ้าของ repo ตัดสินใจแล้ว:** ไม่ต้องการมี reference 2 เล่มคู่ขนาน ต้องการ **รวมร่างจริงเป็นเล่มเดียวสมบูรณ์ ("Ver.2")** — เล่มใหม่ต้องมีทั้ง (ก) โครง workflow A→H ที่ field-guide วางไว้ **และ** (ข) ความลึกเชิงวิชาการที่ e-Book เดิมมี (Workshop, Assessment, Interview Questions, PM Dictionary ฯลฯ) — ไม่ใช่แค่ field-guide แบบเบาที่ Blueprint เดิมออกแบบไว้ตอนแรก

**Edition:** เล่มรวมนี้ยึด **PMBOK 8th Edition** เป็นหลัก วิธี migrate edition ของ repo คือ **สร้างเล่มใหม่แทนที่ ไม่ใช่แก้ `e-Book/` เดิมในที่เดิม** (ดู `repository/PMBOK-EDITION-POSITION.md` และ Decision Log #8 ใน `repository/REPOSITORY_DECISION_LOG.md`)

---

## 2. Non-negotiable constraints (จาก governance ของ repo — ต้องอ่านก่อนเขียนเนื้อหาจริง)

| ไฟล์ | ใช้ทำอะไร |
|---|---|
| `governance/CONTENT-RULES.md` | Source hierarchy, source labels (`[PMBOK]`, `[PMBOK 6]`, `[PMBOK 7]` — **ต้องเพิ่ม `[PMBOK 8]` เข้าไปในระบบนี้ก่อน**), scenario continuity rules |
| `governance/COURSE_STANDARD.md` | Release gate ของ repo |
| `governance/STYLE_GUIDE.md` | YAML frontmatter, ภาษาไทย+ศัพท์อังกฤษ, ใช้ relative link เท่านั้น |
| `governance/LESSON_TEMPLATE.md` | Template 21 หัวข้อเดิม — ใช้เป็นฐานออกแบบ Template ใหม่ (ดูข้อ 5) ไม่ใช่ copy ตรงๆ |
| `governance/PM_GLOSSARY.md` | Glossary กลางของ repo — คำศัพท์ใหม่ต้อง sync เข้าไฟล์นี้ ห้ามสร้าง glossary แยกที่ขัดกัน |
| `scenarios/` | **แหล่งความจริงเดียว** สำหรับข้อมูล ERP และ Hotel Booking Scenario — ห้ามเปลี่ยนตัวเลข/ชื่อ/roles ที่ล็อกไว้แล้วเงียบๆ |
| `repository/REPOSITORY_DECISION_LOG.md` | ต้อง log ทุกการตัดสินใจสำคัญ (ตอนนี้มีถึงแถวที่ 12) |

**กฎเหล็ก:** ห้ามแก้ไฟล์ใดๆ ใน `e-Book/` จนกว่าเล่มใหม่จะสมบูรณ์และผ่านการตรวจสอบ + ได้รับ approval จากเจ้าของ repo เท่านั้น (ดู Phase 6 ข้อ 6)

---

## 3. Content Mapping — 10 Knowledge Areas (e-Book เดิม) → 11 Chapters ใหม่ (A–H)

จุดยากที่สุดของงานนี้: KA เดิมเรียงตามหัวข้อวิชา, Chapter ใหม่เรียงตามลำดับเวลาที่งานเกิดจริง **ไม่ตรงกัน 1:1** — ต้องผ่าเนื้อหา KA แล้วเทลง Chapter ที่ตรงกับตอนที่งานนั้นเกิดขึ้นจริง

| Chapter ใหม่ (A–H) | Knowledge Area เดิมที่ต้องเทเข้ามา | Source lesson เดิม |
|---|---|---|
| Ch.0 — PMBOK Primer | ภาพรวม 6 Principles / 7 Performance Domains / 5 Focus Areas ของ PMBOK 8 (เนื้อหาใหม่ ไม่มีในเดิม) | `references/PMBOK-Overview.md` (ปรับปรุง) |
| Ch.1 — Pre-sales (Playbook A) | Business Case / Value ส่วนต้นของ Integration | `lessons/lesson-05` (บางส่วน) |
| Ch.2 — Initiation (Playbook B) | **Integration Management** (Charter), **Stakeholder Management** เต็มบท | `lessons/lesson-05`, `lessons/lesson-06` |
| Ch.3 — Requirements/Scope/WBS (Playbook C1–C7) | **Scope Management and WBS** เต็มบท | `lessons/lesson-07` |
| Ch.4 — Schedule/Cost/Resource (Playbook C8–C13) | **Schedule Management**, **Cost Management and EVM**, **Resource Management** เต็มบท | `lessons/lesson-08`, `lessons/lesson-09`, `lessons/lesson-11` |
| Ch.5 — Risk/Procurement/Environment (Playbook C14–C19) | **Risk Management**, **Procurement Management**, **Communications Management** เต็มบท | `lessons/lesson-13`, `lessons/lesson-14`, `lessons/lesson-12` |
| Ch.6 — Execution (Playbook D) | Quality Management (ฝั่ง Manage Quality), Resource (ฝั่ง Develop/Manage Team) | `lessons/lesson-10` (บางส่วน), `lessons/lesson-11` (บางส่วน) |
| Ch.7 — Monitoring & Change (Playbook E) | Integration Management (Perform Integrated Change Control), Cost Control/EVM ฝั่ง Control | `lessons/lesson-05`, `lessons/lesson-09` (บางส่วน) |
| Ch.8 — Verification/UAT (Playbook F) | **Quality Management** ฝั่ง Control Quality/Validate | `lessons/lesson-10` |
| Ch.9 — Go-Live & Hypercare (Playbook G) | เนื้อหาใหม่ทั้งหมด — e-Book เดิมไม่มีบท Deployment/Hypercare โดยเฉพาะ | ไม่มี — เขียนใหม่ |
| Ch.10 — Transition & Closure (Playbook H) | Integration Management (Close Project or Phase) | `lessons/lesson-05` (บางส่วน) |
| Agile inserts (แทรกใน Ch.4/Ch.6) | **Agile PM: Scrum and Kanban**, **Predictive vs Agile vs Hybrid** | `lessons/lesson-15`, `lessons/lesson-16` — ทำเป็นกล่อง "ถ้าโครงการเป็น Agile" แทรกในบทที่เกี่ยวข้อง **ไม่ทำเป็นบทแยก** |

### ⚠️ คำเตือนสำคัญ 2 จุด (ผู้ใช้เคยจับผิดจุดนี้มาแล้วรอบหนึ่งใน Appendix E — ห้ามพลาดซ้ำ)

1. **Quality Management ถูกผ่าเป็น 2 ท่อน**: วางแผน Test/Quality → Ch.5, ตรวจสอบ/ผลจริง → Ch.8 — ทุกครั้งที่พูดถึง SRS/FSD/Test Plan/Tech Spec ต้องระบุชัดว่าอยู่ Ch.5 (วางแผน) ส่วน Test Results/UAT Evidence อยู่ Ch.8 (ผลจริง) เขียน cross-reference ให้ชัดในเนื้อหาทั้งสองบท
2. **Integration Management ถูกผ่าเป็น 3 ท่อน**: Charter→Ch.2, Change Control→Ch.7, Closure→Ch.10 — เป็น pattern ปกติของ PMBOK (Integration ทำงานตลอดทั้งโครงการอยู่แล้ว) ไม่ใช่ความผิดพลาด แต่ต้องเขียนให้ผู้อ่านเห็นว่าเชื่อมกันอย่างไร

---

## 4. Scenario — ต้องล็อกก่อนเขียน Ch.1 (ยังไม่ได้ล็อก — FreeBuff ต้องเสนอทางเลือกใน FreeBuff_Fixed_Update.md ก่อนเริ่ม Ch.1)

Playbook V2 §A สมมติความสัมพันธ์ Vendor–Client (Proposal, SOW, Contract) แต่ Scenario ที่ล็อกไว้ในนี่ (`scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` — Siri Hospitality Group, 12 โรงแรม, งบ Phase 1 = 12 ล้านบาท) เป็นโครงการ **internal** ไม่มี vendor — Ch.1 ใช้ scenario เดิมตรงๆ ไม่ได้

**ทางเลือกที่แนะนำ (default — ปรับได้ถ้ามีเหตุผล):**
- เพิ่มชั้นสมมติสั้นๆ เฉพาะ Ch.1–2: สมมติว่า SHG จ้างบริษัท Digital Vendor ภายนอกมาพัฒนา (ตั้งชื่อใหม่ เช่น "บริษัท Booking Tech Solutions") ให้ Ch.1–2 เดินเรื่องจากมุมเวนเดอร์ แล้ว Ch.3 เป็นต้นไปกลับมาใช้ทีม SHG ภายในตามที่ล็อกไว้เดิม — ล็อกด้วย label `[Teaching Scenario Extension]` **ห้ามแก้ตัวเลข/roles ที่ล็อกไว้แล้วใน `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md`**

**ทางเลือกอื่น:** ตัด vendor framing ออกจาก Ch.1 (เขียนเป็น "Internal Business Case Approval" แทน) หรือสร้าง scenario คู่ขนานใหม่ทั้งเล่ม (ไม่แนะนำ — ใหญ่สุด เสี่ยงสุด)

**FreeBuff ต้องเลือกและประกาศการตัดสินใจนี้ใน `FreeBuff_Fixed_Update.md` ก่อนเริ่มเขียน Ch.1 จริง** — ไม่ใช่ตัดสินใจเงียบๆ

---

## 5. Template ต่อ 1 บท — ฉบับรวม (15 หัวข้อ)

ไม่ใช่ Template เบา 10 หัวข้อแบบ field-guide เดิม และไม่ใช่ Template เต็ม 21 หัวข้อแบบ e-Book เดิม — นี่คือฉบับรวมที่ต้องใช้กับทุกบท (Ch.1–10, ยกเว้น Ch.0 ที่เป็นบทปฐมบทไม่ต้องมี Workshop/Assessment):

1. **เปิดด้วยสถานการณ์จริงจาก Case** (Opening Scenario Hook)
2. **ทำไมต้องรู้เรื่องนี้** (Why It Matters)
3. **Mental Model / ภาพรวม** (Goal + Flow diagram จาก Playbook V2 ส่วนที่เกี่ยวข้อง)
4. **เนื้อหาหลัก** — รวม sub-processes จาก Knowledge Area เดิมที่ map เข้ามาตามตารางข้อ 3 (จุดที่เพิ่มความลึกจาก e-Book เดิมเข้าไปจริง)
5. **PM Decision Thinking** — decision record format จาก `governance/LESSON_TEMPLATE.md` §5 (Decision/Owner/Inputs/Assumptions/Options/Trade-offs/Risk/Evidence/Next Action) อย่างน้อย 1 จุดต่อบท
6. **ตัวอย่างจริงจาก Case ต่อเนื่อง** (ผูก Scenario เดียวกันทั้งเล่ม ตามข้อ 4)
7. **จุดตัดสินใจและกับดักที่พบบ่อย** (Common Mistakes + Misconceptions — ดึงจาก Playbook V2's Common Mistakes list ของแต่ละ Phase มาแปลงเป็นเคสสั้นๆ)
8. **Interview Questions** — Foundational / Scenario / Senior PM / Executive (รูปแบบเดียวกับ e-Book เดิม)
9. **PM Dictionary ประจำบท** — ต้อง sync กับ `governance/PM_GLOSSARY.md` ห้ามสร้างคำซ้ำ/ขัดกัน — คำใหม่ที่ยังไม่มีในนั้น (เช่น ROM, SOW, Cutover, Hypercare, Rollback, Go/No-Go) ต้องเพิ่มเข้า Glossary กลางด้วย
10. **Workshop** (scenario-based มี Available/Missing Information + Decision Required + Debrief Questions + Evaluation Criteria ตามฟอร์แมต `LESSON_TEMPLATE.md` §16)
11. **Checklist ใช้งานจริง** (จุดขายหลักของเล่มนี้ — ดึงจาก Practical Checklist/Artifact table ของ Playbook V2 ตรงๆ — ห้ามตัดออก)
12. **Assessment** (5–8 ข้อ เน้น decision-based ไม่ใช่ recall เป็นหลัก)
13. **Executive Summary**
14. **เชื่อมไปบทถัดไป + Artifact Handoff** (Bridge — artifact อะไรถูกส่งต่อไปบทไหน)
15. **Quick Reference Card ท้ายบท** (สรุป 1 หน้า สำหรับพลิกดูเร็วๆ — field manual signature)

---

## 6. Production Pipeline — Phase ที่ต้องทำตามลำดับ

| Phase | งาน | Output |
|---|---|---|
| **0 — Lock** | ล็อกชื่อเล่ม (ดูตัวเลือกใน `field-guide/BOOK-BLUEPRINT.md`) + ล็อก Scenario decision (ข้อ 4) + เพิ่ม label `[PMBOK 8]` เข้า `governance/CONTENT-RULES.md` §2/§7 | ประกาศใน `FreeBuff_Fixed_Update.md` |
| **1 — Pilot** | เขียน Ch.1 เต็มรูปแบบด้วย Template 15 หัวข้อ (ข้อ 5) | 1 บทสมบูรณ์ ส่งให้ Claude review ก่อนขยายบทอื่น |
| **2 — Batch Production** | เขียนบทที่เหลือเป็นชุด (แนะนำ 3 บทต่อรอบ) — ทุกบทที่ผ่า KA มาต้องเทียบกับ `lessons/lesson-NN/` เดิมให้ครบ (ใช้ `repository/CONTENT_COVERAGE_MATRIX.md` เป็นเช็คลิสต์) | Batch ละ 3 บท + self-check ก่อนส่ง review |
| **3 — Appendices** | ทำ Appendix A, B, C, D, F ที่เหลือ (E เขียนเสร็จแล้วที่ `field-guide/appendices/Appendix-E-SDLC-Role-Output-Matrix.md`) | 5 ไฟล์ Appendix ใหม่ |
| **4 — รวมเล่ม** | ตรวจ cross-reference ทั้งเล่ม โดยเฉพาะจุด Quality/Integration ที่ถูกผ่า (ข้อ 3) | เล่มสมบูรณ์ 1 ก้อน |
| **5 — Export PDF** | Learner + Instructor edition ต่อยอดจาก `e-Book/pdf/build_pdf.py` | PDF 2 ฉบับ |
| **6 — Retirement decision** | **ทำหลัง Phase 5 validate ผ่านเท่านั้น** — เสนอว่าจะ archive `e-Book/` ไปที่ไหน (เช่น `repository/archive/`) — ห้าม archive/ลบก่อนได้ approval จากเจ้าของ repo | ข้อเสนอ ไม่ใช่การลงมือทำ |

**ที่ทำงาน:** ทำทั้งหมดใน `field-guide/` (ห้ามแก้ `e-Book/` จนกว่าจะถึง Phase 6 และได้ approve) — โครงสร้างที่มีอยู่แล้ว: `field-guide/BOOK-BLUEPRINT.md`, `field-guide/appendices/`, `field-guide/pdf/` — เพิ่มใหม่ตามที่เขียนบทจริง: `field-guide/chapters/ch-00/` ... `field-guide/chapters/ch-10/` (mirror โครงสร้าง `e-Book/chapters/lesson-NN/` เดิมที่มีไฟล์ learner/instructor/answer-key แยกกัน)

---

## 7. Governance updates ที่ต้องทำใน Phase 0

- `governance/CONTENT-RULES.md` §2 และ §7: เพิ่ม `[PMBOK 8]` เป็น label ที่ใช้ได้ (ควบคู่ `[PMBOK 6]`/`[PMBOK 7]` เดิม — **ห้ามลบของเดิม** เพราะ e-Book เดิมยังอยู่จนกว่าจะถึง Phase 6)
- `repository/PMBOK-EDITION-POSITION.md`: เพิ่มหัวข้ออธิบายว่า repo กำลัง migrate ไป PMBOK 8 ผ่านเล่มใหม่ ไม่ใช่แก้ e-Book เดิม
- `repository/REPOSITORY_DECISION_LOG.md`: log การตัดสินใจ "รวมเป็นเล่มเดียว" เป็นแถวใหม่ต่อจากแถวที่ 12 — **สำคัญมาก เพราะกลับคำตัดสินใจเดิมที่เคย log ไว้ว่า "แยกเล่ม"**

---

## 8. Definition of Done

**ต่อ Chapter:**
- ครบ 15 หัวข้อตาม Template (ข้อ 5)
- เนื้อหา KA ที่ map มา (ข้อ 3) ถูกถ่ายมาครบ เทียบกับ lesson เดิมทีละหัวข้อ
- Source label ถูกต้อง (`[PMBOK 8]` เป็นหลัก, ใช้ `[Teaching Scenario]`/`[Best Practice]` ตาม `CONTENT-RULES.md`)
- Scenario ตรงกับตัวเลข/roles ที่ล็อกไว้ (ยกเว้น Ch.1–2 ที่มี Teaching Scenario Extension ตามข้อ 4)
- Relative links ใช้งานได้จริงทุกลิงก์

**ต่อเล่ม (ก่อนเสนอ Phase 6):**
- ทุก Knowledge Area ในตารางข้อ 3 ถูกครอบคลุมอย่างน้อยเทียบเท่าความลึกของ e-Book เดิม
- Appendix ครบ 6 ตัว (A–F)
- PDF Learner + Instructor edition build ผ่านจริง
- เจ้าของ repo review และ approve แล้วเท่านั้นถึงจะแตะ `e-Book/` ได้

---

## 9. Collaboration Protocol — วิธีทำงานร่วมกันผ่าน 3 ไฟล์นี้

โฟลเดอร์ `Ver.2/` มี 3 ไฟล์:

1. **`master_plan.md`** (ไฟล์นี้) — Claude เขียน, เป็นแผนหลักที่อนุมัติแล้ว FreeBuff อ่านไฟล์นี้เป็นหลักในการทำงาน ไม่ควรถูกแก้โดย FreeBuff (ถ้าคิดว่าแผนต้องปรับ ให้เสนอใน `FreeBuff_Fixed_Update.md` แทน)
2. **`Claude_Review_Feedback.md`** — Claude เขียน เป็น log การรีวิวแต่ละรอบ (ถูก/ผิด/ต้องแก้อะไร) เขียนเป็นรายการวันที่ + รอบ ใหม่สุดอยู่บนสุด
3. **`FreeBuff_Fixed_Update.md`** — **FreeBuff เขียน** รายงานว่าทำอะไรไปแล้ว ติดตรงไหน มีคำถามอะไร เขียนเป็นรายการวันที่ + รอบ ใหม่สุดอยู่บนสุด

### Loop การทำงาน

```
FreeBuff อ่าน master_plan.md
    ↓
FreeBuff ลงมือทำตาม Phase ที่กำหนด
    ↓
FreeBuff เขียนรายงานลง FreeBuff_Fixed_Update.md
   (ทำอะไรไปแล้ว / ติดตรงไหน / คำถาม)
    ↓
เจ้าของ repo แจ้ง Claude ว่ามีอัปเดตใหม่
    ↓
Claude อ่าน FreeBuff_Fixed_Update.md เทียบกับ master_plan.md §8 (Definition of Done)
    ↓
Claude เขียนผลรีวิวลง Claude_Review_Feedback.md
   (ถูก/ผิด/ต้องแก้อะไร/อนุมัติให้ไป Phase ถัดไปได้หรือยัง)
    ↓
FreeBuff อ่าน Claude_Review_Feedback.md แล้วแก้ไข/ทำต่อ → วนกลับไปข้อ 3
```

**กติกา:**
- ห้ามข้าม Phase (ข้อ 6) โดยไม่ผ่าน review ก่อน โดยเฉพาะ Phase 0→1 (ต้องล็อก Scenario+ชื่อเล่มก่อน) และ Phase 5→6 (ห้ามแตะ `e-Book/` ก่อนอนุมัติ)
- ทุกรายการใน log ต้องมีวันที่กำกับ
- ถ้า FreeBuff ไม่เห็นด้วยกับจุดไหนใน master plan ให้เขียนเหตุผลใน `FreeBuff_Fixed_Update.md` แทนที่จะเบี่ยงเบนจากแผนเงียบๆ — Claude จะพิจารณาและตอบใน `Claude_Review_Feedback.md`

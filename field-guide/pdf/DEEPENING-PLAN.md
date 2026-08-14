---
title: "Deepening Plan — PM Delivery Guide (Ver.2) field-guide"
document_type: Execution Brief (Handoff to AI)
version: 1.0
status: Approved by owner — ready for AI to execute
owner: User (Owner) — approved 2026-08-15
planner: Claude (this session)
executor: AI (pick this file up and execute — not Claude)
scope: field-guide/chapters/ learner files ONLY (deepen in place)
last_updated: 2026-08-15
---

# Deepening Plan — ทำให้ field-guide "อ่านแล้วเข้าใจ" ไม่ใช่แค่ "เช็คลิสต์"

> **อ่านก่อนเริ่มทำ (สำหรับ AI ที่จะลงมือ):** ไฟล์นี้คือคำสั่งงานฉบับเดียวที่คุณต้องอ่านก่อนแก้เนื้อหา งานของคุณคือ **deepen เนื้อหา 11 บทให้อ่านแล้วเข้าใจ** ตาม spec รายบทด้านล่าง **ห้าม** ออกแบบโครงสร้างใหม่ — โครง 15 หัวข้อต่อบทล็อกไว้แล้ว (ดู `Ver.2/master_plan.md` §5) งานนี้คือการ**เติมเนื้อหาเข้าไปในหัวข้อที่มีอยู่** ไม่ใช่สร้างหัวข้อใหม่
>
> **กฎเหล็กที่ไม่เปลี่ยน:** ห้ามแตะ `e-Book/` · ห้ามแก้ตัวเลข/ชื่อ/roles ใน `scenarios/` · ห้ามเปลี่ยนโครง 15 หัวข้อ · ห้ามเพิ่ม/ลบ source label เดิม · ห้ามใช้ absolute path · ห้ามเขียนแบบ encyclopedia

---

## 1. บริบท — ทำไมต้องมีแผนนี้

เจ้าของ repo อ่าน `field-guide/pdf/PM-Delivery-Guide-*.pdf` แล้วรู้สึกว่า **เนื้อหาไม่แน่นพอ และอ่านแล้วไม่เข้าใจลึก** โดยเฉพาะบทหลัง ๆ (Ch.6–10) ดูบางกว่าบทแรก (Ch.1–2)

การตรวจสอบเชิงลึก (Claude อ่านไฟล์ learner จริงทุกบท + เทียบ source) พบว่า:

1. **จำนวนคำไม่ใช่ปัญหาหลัก** — Ch.1–10 มี learner ≈ 2,250–2,700 คำต่อบท ใกล้เคียงกัน (Ch.0 บางสุด 1,364, Ch.9 บางรองลงมา 2,251)
2. **ปัญหาจริงคือ "กว้างแต่ตื้น"** — §4 Main Lesson เขียนเป็น**ลิสต์สิ่งของ** (ว่าต้องมีอะไรบ้าง) ไม่ใช่**บทเรียน** (ทำไมต้องมี คิดยังไง พลาดแล้วเกิดอะไร) ตัวอย่างจริงจาก `ch-01-learner.md` §4.7:

   > "Proposal ที่ดีควรมี Executive Summary, Business Understanding, Problem and Desired Outcome, Proposed Solution, Scope and Deliverables, In Scope/Out of Scope, Delivery Approach, …"

   นี่คือ checklist ไม่ใช่การสอน — ขัดกับ `governance/CONTENT-RULES.md` §4 ที่ห้ามเขียนแบบ `definition → bullet list → generic example → quiz`
3. **Source ที่ลึกมีอยู่แล้วแต่ยังถูกดึงมาไม่หมด** — `references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md` (2,745 บรรทัด) มี step-by-step ละเอียดราย Phase (A1–A12, B1–B7, C1–C19, D.5–D.8, E.3–E.10, F.2–F.9, G.2–G.9, H.3–H.9) พร้อม Common Mistakes / Artifacts / Approval Gate / Exit Criteria ที่**ยังถูก compress ลงบทไปแค่ส่วนเดียว** แผนนี้จะชี้ให้ดึงตรงไหนกลับมา
4. **e-Book เดิมมีหัวข้อ "Watch PM Think" / "Artifact Example" / "Beginner Checkpoint"** ที่เป็นชั้น "คิดตาม PM" — ตอนรวมเล่มชั้นนี้หายไป เหลือแต่ลิสต์

**เป้าหมายของแผนนี้:** เปลี่ยนทุกบทจาก "บอกว่าต้องทำอะไร" → เป็น "สอนให้คิดว่าทำไมและทำยังไง" โดย**ดึงความลึกจาก Playbook V2 + e-Book เดิมกลับมา + เขียนร้อยแก้วเหตุผล** ไม่ใช่เพิ่มจำนวนคำแบบกลวง ๆ

---

## 2. หลักการ Deepening (ใช้กับทุกบท — ต้องจำให้ขึ้นใจ)

การ deepen แต่ละ section ทำตาม 6 กติกานี้เท่านั้น:

### D1. ทุก concept ต้องตอบ "ทำไม" ก่อน "อะไร"
ถ้าเขียนว่า "ควรมี X" ต้องตามด้วยประโยคอธิบายว่า **ทำไมต้องมี X / ไม่มีแล้วเกิดอะไร / มันแก้ปัญหาอะไร** อย่างน้อย 1–2 ประโยค

❌ `Proposal ควรมี 19 องค์ประกอบ: Executive Summary, Business Understanding, …`
✅ `Proposal ที่ไม่มี Out of Scope คือการเปิดประตูให้ "งานทุกอย่างกลายเป็น in scope โดยปริยาย" — เพราะเมื่อลูกค้าเห็นเอกสารไม่มีเส้นแบ่ง เขาจะยึดรายการที่คุยกันปากเปล่าเป็นสัญญา งานที่คุณไม่เคยตั้งใจจะทำจะกลายเป็นหน้าที่ของคุณ ดังนั้นหัวข้อ Out of Scope จึงไม่ใช่ "ส่วนประกอบ" แต่คือกันชนทางกฎหมายของ PM`

### D2. แปลงลิสต์ → ร้อยแก้ว + ตารางที่มีคอลัมน์ "ทำไม"
ลิสต์ยาว ๆ (≥ 4 ข้อที่เป็น concept ไม่ใช่ action step) ให้แปลงเป็นย่อหน้า หรือตาราง 3 คอลัมน์ที่คอลัมน์สุดท้ายคือ **"ทำไมถึงสำคัญ / พลาดแล้วเกิดอะไร"** (STYLE_GUIDE §3, §5 อนุญาตให้ใช้ list เฉพาะ action steps/checklist; concept ต้องมี narrative)

### D3. เพิ่มชั้น "Watch PM Think" เข้าไปใน §6
§6 (ตัวอย่างจริงจาก Case) ปัจจุบันเป็นลิสต์เหตุการณ์ — ให้เขียนเป็น **walkthrough ที่เล่าเหตุผลในหัว PM** อย่างน้อย 1 จุดต่อบท: "PM มองอะไร → เห็นอะไร → กังวลอะไร → ตัดสินใจอะไร → ทำไม" (ดึงโทนจาก `e-Book/chapters/lesson-05` §7 "PM Thinking" เป็นต้นแบบ)

### D4. ดึง step-by-step จาก Playbook V2 กลับมา
แต่ละบทมี source section ใน Playbook ที่ละเอียดกว่าเนื้อหาบทปัจจุบัน — **ดึงเฉพาะจุดที่ "เพิ่มความเข้าใจ" (เหตุผล + ตัวอย่าง + กับดัก) ไม่ใช่ copy ทั้งหมด** อย่า bloating กลายเป็นตำรา เป้าหมายคือ "field manual ที่อ่านแล้วเข้าใจ" ไม่ใช่ "Playbook ซ้ำ"

### D5. Common Mistake ทุกข้อต้องมี "พลาดแล้วเกิดอะไร"
§7 Common Mistakes ปัจจุบันเขียนว่า "X — ผล: …" แบบสั้น — ให้ขยายข้อสำคัญ 2–3 ข้อต่อบทเป็น **mini-story 2–3 ประโยค** (ยกตัวอย่างสถานการณ์จริงแบบสมมติที่เห็นผลกระทบ)

### D6. รักษา source label + scenario ไว้เป๊ะ
ทุกย่อหน้าใหม่ต้องมี label หน้าข้อความ (`[PMBOK 8]` / `[Best Practice]` / `[Teaching Scenario]` / `[Teaching Scenario Extension]`) ตาม `CONTENT-RULES.md` §7 · ตัวเลข scenario ต้องตรง `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` v1.0 (12M / 35% / 18 เดือน / NPS≥40 / 12 โรงแรม / Sprint 0–12 / launch ก่อน 1 พ.ย.) · Ch.1–2 ใช้ vendor layer "Booking Tech Solutions (BTS)" เฉพาะช่วงนั้นด้วย `[Teaching Scenario Extension]`

---

## 3. ขอบเขตและข้อห้ามเด็ดขาด

### ทำได้ (scope)
- แก้ไฟล์ `field-guide/chapters/ch-NN/ch-NN-learner.md` **ในที่เดิม** (deepen)
- แก้ `ch-NN-instructor.md` และ `ch-NN-answer-key.md` **เฉพาะเมื่อ** เนื้อหา learner เปลี่ยนแล้วทำให้ teaching note / model answer ไม่ตรง (เช่น เพิ่มแนวคิดใหม่เข้า Assessment)
- เพิ่มคำศัพท์ใหม่เข้า `governance/PM_GLOSSARY.md` **ถ้าจำเป็น** (ห้ามสร้าง glossary แยก)
- หลังเสร็จทุกบท: rebuild PDF ด้วย `field-guide/pdf/build_pdf.py`

### ห้ามทำ (ข้อห้าม — ละเมิด = งานถูกตีกลับ)
1. ❌ แตะไฟล์ใด ๆ ใน `e-Book/` (กฎเหล็ก master_plan §2)
2. ❌ เปลี่ยนโครง 15 หัวข้อ (เพิ่ม/ลบ/เรียงใหม่หัวข้อ `## 1.`–`## 15.`)
3. ❌ แก้ตัวเลข/ชื่อ/roles ที่ล็อกใน `scenarios/` เงียบ ๆ (ถ้าต้องเพิ่ม → ใช้ `[Teaching Scenario]` + บันทึกใน log)
4. ❌ ลบ/แก้ source label เดิม (`[PMBOK 6]`/`[PMBOK 7]`/`[PMBOK 8]`)
5. ❌ ใช้ absolute path / `file:///` ในลิงก์
6. ❌ เขียนแบบ encyclopedia / bullet list เป็นเนื้อหาหลัก / ประโยค generic AI ("จะเห็นได้ว่า…", "ดังที่กล่าวมา…")
7. ❌ สร้างบทใหม่ / แยกไฟล์ / เพิ่ม section เกิน 15
8. ❌ เปลี่ยน frontmatter YAML (chapter/title/book/edition/status/canonical_source/scenario_version) — ยกเว้น `last_reviewed` ให้อัปเดตเป็นวันที่แก้

---

## 4. วิธีทำงานต่อบท (procedure มาตรฐาน — ทำซ้ำ 11 บท)

สำหรับแต่ละบท ให้ทำตามลำดับนี้:

1. **อ่าน source 3 ชั้นก่อนแก้:** (ก) `references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md` เฉพาะ Phase ที่ map (ดูตาราง §5) · (ข) `e-Book/chapters/lesson-NN/` เดิมที่ map (ดู `Ver.2/master_plan.md` §3) · (ค) `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` (ถ้าบทนั้นอ้าง scenario)
2. **ระบุ gap:** เปรียบเทียบ §4 ของบทกับ Playbook section — จดว่ามี concept ไหนใน Playbook ที่ลึกกว่าแต่บทปัจจุบันเขียนเป็นลิสต์เปล่า
3. **Deepen ทีละ section** ตามหลัก D1–D6 โดยลำดับความสำคัญ: §4 (หลัก) → §6 (Watch PM Think) → §2 (Why It Matters) → §7 (mini-story) → ที่เหลือปรับเล็กน้อย
4. **Sync glossary:** ถ้าใช้คำศัพท์ใหม่ ตรวจว่ามีใน `governance/PM_GLOSSARY.md` แล้วหรือยัง — ไม่มีให้เพิ่ม
5. **Sync instructor/answer-key** เฉพาะที่จำเป็น
6. **ตรวจ DoD ประจำบท** (ดู §7) แล้วบันทึกลง log

---

## 5. แผนรายบท (หัวใจของแผน — อ่าน spec ของบทที่จะทำให้ครบก่อนลงมือ)

> Source map ต่อไปนี้อ้างอิง section ของ `references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md` (บรรทัดอ้างอิงโดยประมาณ อาจขยับ ±5 บรรทัด)

### Ch.0 — PMBOK Primer (บางสุด 1,364 คำ — ทำเป็นลำดับแรก)
- **จุดอ่อน:** §4.2 เป็นตาราง "6 Principles / 7 Domains / 5 Focus Areas" เปล่า ๆ ไม่อธิบายว่าแต่ละข้อหมายถึงอะไรในทางปฏิบัติ
- **ต้องเสริม:**
  1. §4.2 — ขยายแต่ละองค์ประกอบให้มี **1 บรรทัด "แปลเป็นภาษาคนทำงาน"** เช่น Principle "Value Focus" → "ถามเสมอว่า งานที่ทำตอนนี้ทำให้ business ได้ผลลัพธ์อะไร ไม่ใช่แค่เสร็จตาม plan" (ดึงจาก Playbook §1 Reference Basis, §1.1 และ `references/PMBOK-Overview.md`)
  2. §4.3 — เพิ่มตัวอย่าง concrete: Process Group "Planning" เกิดซ้ำตรงไหนในโครงการ SHG (เช่น กลาง execution ต้องกลับไป re-plan หลัง scope เปลี่ยน)
  3. §4.5 — เพิ่มตัวอย่างวิธีใช้ Field Mode จริง: "PM เจอ 'ลูกค้าขอเพิ่ม scope' → เปิด Appendix F → เจอ Ch.7 → ไปที่ Quick Reference Card"
  4. §2 — เพิ่ม mini-story "PM ที่ไม่รู้กรอบ → ตามงานอย่างเดียว มองไม่เห็น risk/benefit"
- **Source:** Playbook §1, §1.1 · `references/PMBOK-Overview.md` · `e-Book/chapters/lesson-01`
- **DoD:** §4.2 ทุกแถวมี "แปลเป็นภาษาคนทำงาน" · §4.3 มีตัวอย่าง re-plan · §4.5 มีตัวอย่าง lookup 1 จุด

### Ch.1 — Pre-sales / Playbook A (หนาสุดแล้ว 2,620 คำ — ปรับน้อยสุด)
- **จุดอ่อน:** §4.x แต่ละหัวข้อ (A1–A12) เขียนเป็นลิสต์ ควรแปลงเป็นร้อยแก้วเหตุผล + ตัวอย่างสั้น
- **ต้องเสริม:**
  1. §4.5 (ROM) — ขยายว่าทำไม ROM ต้องมีช่วง + confidence: "ROM ตัวเลขเดียวที่ถูกอ่านเป็นราคาผูกพัน = กับดัก …" พร้อมตัวอย่างตัวเลขจาก BTS (Fixed 6.5M + T&M cap 0.5M ที่มีอยู่แล้วใน §6)
  2. §4.7 (Proposal 19 ข้อ) — แปลงลิสต์เป็นตาราง 2 คอลัมน์ (องค์ประกอบ → ทำไม/พลาดแล้วเกิดอะไร) หรือร้อยแก้ว ตามหลัก D2
  3. §6 — เขียนเป็น Watch PM Think: เล่าเหตุผลในหัว Pre-sales PM ตอนเจอ "PMS ต่างยี่ห้อ 3 ตัว API ไม่ครบ"
- **Source:** Playbook A1–A12 · `e-Book/chapters/lesson-05` (Business Case)
- **DoD:** §4.7 ไม่เหลือลิสต์เปล่า · §6 มี Walkthrough คิดตาม PM · ROM มีเหตุผลเรื่องช่วง+confidence

### Ch.2 — Initiation / Playbook B (B1–B7)
- **จุดอ่อน:** Stakeholder (B3/B4) เขียนบางเกิน ไม่มี power/interest grid ที่เป็น core ของการจัดลำดับ stakeholder
- **ต้องเสริม:**
  1. §4 — เพิ่ม **Power/Interest Grid** (4 ช่อง: Manage Closely / Keep Satisfied / Keep Informed / Monitor) พร้อมวางตัวละคร SHG ลงช่อง (คุณจิรา CEO = High power/High interest → Manage Closely)
  2. §4 — Charter: อธิบายว่าทำไม Charter ถึงเป็น "อำนาจของ PM" ไม่ใช่ "เอกสารพิธีกรรม" — ยกกรณี PM ทำงานแล้วโดน Stakeholder ไม่ให้ความร่วมมือเพราะไม่มี Charter
  3. §4 — B6 RAID setup: อธิบายว่า RAID = Risk/Assumption/Issue/Dependency และทำไมต้องแยก Assumption ออกมาดู (Assumption ที่ผิดกลายเป็น Risk)
- **Source:** Playbook B2–B6 · `e-Book/chapters/lesson-05` (Integration/Stakeholder)
- **DoD:** มี Power/Interest Grid วางตัวละครจริง · Charter อธิบาย "ทำไมคืออำนาจ" · RAID อธิบายครบ 4 ตัว

### Ch.3 — Requirements/Scope/WBS / Playbook C1–C6 (ยาวสุดใน Playbook — ขยายมาก)
- **จุดอ่อน:** เนื้อหาลึกของ Playbook C3–C6 (Requirement Types, Techniques, SRS/FSD substitution matrix, 100% Rule, WBS Dictionary) ถูก compress เหลือลิสต์สั้น
- **ต้องเสริม:**
  1. §4 — **SRS vs FSD** และ **Document Substitution Matrix** (C4.4): อธิบายว่าเมื่อไรทำ FSD ได้ เมื่อไรทำไม่ได้ — ตรงนี้คือจุดที่คนสับสนจริง (ดึงจาก Playbook C4.1–C4.4 ซึ่งมี "ห้ามตัด FSD โดยไม่มีสิ่งทดแทนเมื่อ…")
  2. §4 — **100% Rule** (C6.5): อธิบายด้วยตัวอย่าง WBS ของ Direct Booking Platform — งานรวมของ child = parent ครบ ไม่เกิน ไม่ขาด
  3. §4 — **WBS Dictionary** (C6.8): แปลง template fields เป็นตาราง "field → ทำไมต้องมี"
  4. §4 — Requirement Quality Checklist (C3): "SMART / measurable / testable" พร้อมตัวอย่าง requirement ที่ดี vs แย่
- **Source:** Playbook C3–C6 · `e-Book/chapters/lesson-07`
- **DoD:** มี SRS/FSD substitution logic ชัด · 100% Rule มีตัวอย่าง · WBS Dictionary อธิบายเหตุผลแต่ละ field

### Ch.4 — Schedule/Cost/Resource / Playbook C8–C13 (+ Agile insert)
- **จุดอ่อน:** CPM, three-point estimate, EVM เขียนบาง ทั้งที่ Playbook มี terms + example ละเอียด
- **ต้องเสริม:**
  1. §4 — **CPM ตัวอย่างคำนวณจริง**: ให้ dependency network เล็ก ๆ (4–5 กิจกรรม) คำนวณ ES/EF/LS/LF/Float หา Critical Path ให้ดู (ดึงจาก Playbook C11.3–C11.6 ที่มี terms + logic + example)
  2. §4 — **Three-point Estimate** (C10): สูตร (O+4M+P)/6 + อธิบายทำไม weighted กลางมากกว่าปลาย (ลดผลของ outlier)
  3. §4 — **EVM**: ต่อยอดตัวอย่างตัวเลขที่มีอยู่ (PV6/EV5/AC6.5 → SPI/CPI/EAC) — อธิบาย**ความหมายเชิงบริหาร**ของ SPI<1 และ CPI<1 (ตามงาน/เกินงบ → ต้องตัดสินใจอะไร) ไม่ใช่แค่สูตร
  4. Agile insert: อธิบายว่า Schedule บน Kanban/Scrum ต่างจาก CPM ตรงไหน (เมื่อไรใช้แบบไหน)
- **Source:** Playbook C8–C13 · `e-Book/chapters/lesson-08`, `lesson-09`, `lesson-11`, `lesson-15` (Agile)
- **DoD:** มี CPM คำนวณตัวอย่าง · three-point มีสูตร+เหตุผล · EVM อธิบายความหมายเชิงบริหารไม่ใช่แค่สูตร

### Ch.5 — Risk/Procurement/Comms / Playbook C7 + C14–C19
- **จุดอ่อน:** Risk (C15), Procurement (C16), Communication (C14) เขียนแบบผ่าน ๆ ไม่มี depth
- **ต้องเสริม:**
  1. §4 — **Risk vs Issue** (C15): อธิบายเส้นแบ่งชัดเจน + ตัวอย่าง "PMS API ไม่พร้อม" เป็น Risk ตอนเริ่ม → กลายเป็น Issue เมื่อมันเกิดจริง (ข้ามไป Ch.7 ที่ RAID ถูกใช้)
  2. §4 — **Risk Response Strategy** (Avoid/Mitigate/Transfer/Accept + positive: Exploit/Enhance/Share/Accept): ตาราง strategy → เมื่อไรใช้ → ตัวอย่าง SHG
  3. §4 — **Contract type** (Fixed vs T&M vs Hybrid) + Make-or-Buy: ผูกกับตัวอย่าง BTS ใน Ch.1 (Fixed core + T&M PMS adapter) — อธิบายว่าเลือก contract จาก scope maturity + risk allocation
  4. §4 — **Communication Plan**: ระดับ stakeholder → ประเภทข้อมูล → ความถี่ (ดึงจาก C14 Typical Cadence)
  5. §4 — C17 Release/Environment/Transition (วางแผนไว้ล่วงหน้า) — cross-ref ไป Ch.9 (ของจริง)
- **Source:** Playbook C7, C14–C19 · `e-Book/chapters/lesson-13`, `lesson-14`, `lesson-12`
- **DoD:** Risk vs Issue เส้นแบ่งชัด · Risk response ครบ + ตัวอย่าง · Contract type ผูกตัวอย่าง BTS · Comms plan มี cadence

### Ch.6 — Execution / Playbook D (+ Agile insert)
- **จุดอ่อน:** D.5–D.8 เขียนบาง ทั้งที่ DoR/DoD เป็นของสำคัญที่ทีม Agile/Predictive ใช้จริง
- **ต้องเสริม:**
  1. §4 — **Definition of Ready (D.6) vs Definition of Done (D.7)**: ตารางเทียบ + ตัวอย่าง checklist จริงสำหรับ user story ของ SHG (เช่น "พร้อม dev เมื่อ: acceptance criteria ครบ, design approved, dependency clear")
  2. §4 — **Execution flow Predictive vs Agile vs Hybrid** (D.4): อธิบายว่าแต่ละแบบ "จังหวะตรวจ/ปรับ" ต่างกันตรงไหน
  3. §4 — **Manage Quality vs Control Quality** (Quality ฝั่ง Execute): cross-ref ไป Ch.8 (Control/ผลจริง) ตามคำเตือน Quality ที่ถูกผ่าใน master_plan §3
  4. §6 — Watch PM Think: PM จัดการทีม dev ระหว่าง sprint ยังไง (standup, blocker, impedance)
- **Source:** Playbook D.4–D.8 · `e-Book/chapters/lesson-10`, `lesson-11`, `lesson-15`/`lesson-16` (Agile)
- **DoD:** DoR vs DoD เทียบชัด + ตัวอย่าง · Execution flow 3 แบบอธิบายต่างกัน · Quality cross-ref ครบ

### Ch.7 — Monitoring & Change / Playbook E
- **จุดอ่อน:** Change Control (E.5) เป็น core ของ Integration ท่อนที่ 2 แต่เขียนสั้น; EVM control ไม่ลึก
- **ต้องเสริม:**
  1. §4 — **Change Flow เต็มขั้นตอน** (E.5): Submit → Impact Analysis → CCB Review → Approve/Reject → Implement → Verify — พร้อมตัวอย่าง "ลูกค้าขอเพิ่ม payment method" แล้วต้องวิเคราะห์ผลต่อ scope/time/cost/risk
  2. §4 — **Impact Areas** (E.5): ตาราง "change หนึ่งตัวกระทบอะไรบ้าง" (scope, schedule, cost, quality, resource, risk, procurement)
  3. §4 — **Change Authority** (E.5): ใคร approve change ระดับไหน (CCB ประกอบด้วยใคร)
  4. §4 — **Scope Validation vs Scope Control** (E.8): อธิบายต่างกัน (Validate = ตรวจว่างานถูกต้อง vs Control = กัน scope creep)
  5. §4 — EVM control: VAC/EAC/ETC อธิบายเชิงบริหาร (ถ้า CPI<1 ต้องตัดสินใจอะไร)
- **Source:** Playbook E.5–E.10 · `e-Book/chapters/lesson-05` (Integration) + `lesson-09`
- **DoD:** Change flow ครบ 6 ขั้น + ตัวอย่าง · Impact areas ครบ · Validate vs Control ต่างชัด

### Ch.8 — Verification/UAT / Playbook F
- **จุดอ่อน:** Test Levels, QA vs UAT, Traceability, Defect management เขียนบาง
- **ต้องเสริม:**
  1. §4 — **Test Levels** (F.2): Unit → Integration → System → UAT — ตาราง "ระดับ → ทดสอบอะไร → ใครทำ → พบอะไร" พร้อมตัวอย่าง SHG
  2. §4 — **QA vs UAT** (F.3): อธิบายต่างชัด (QA = ตรงตาม spec, UAT = ตรงตาม need ของ user) — cross-ref ไป Ch.5 (Test Strategy วางแผน) ตามคำเตือน Quality ที่ถูกผ่า
  3. §4 — **Requirements Traceability Matrix** (F.5): อธิบายทำไมต้อง RTM + ตัวอย่างแถว (requirement → design → test case → result)
  4. §4 — **Defect Management** (F.6): severity vs priority ต่างกันยังไง (นี่คือจุดสัมภาษณ์ PM บ่อย)
  5. §4 — **Go/No-Go** (F.8): ใครตัดสิน + ใช้ evidence อะไร
- **Source:** Playbook F.2–F.9 · `e-Book/chapters/lesson-10`
- **DoD:** Test levels ครบ + ตัวอย่าง · QA vs UAT ต่างชัด · RTM มีตัวอย่างแถว · severity vs priority ชัด

### Ch.9 — Go-Live & Hypercare / Playbook G (บางรองลงมา — เนื้อหาใหม่ทั้งหมด ต้องขยายมาก)
- **จุดอ่อน:** เนื้อหาใหม่ไม่มี e-Book ต้นฉบับ ช่วยแต่ลิสต์; typo จริง 2 จุด (ดู §6 ด้านล่าง)
- **ต้องเสริม:**
  1. §4.2 (Cutover) — ขยายเป็น **sequence narrative** ทีละขั้น (Freeze → Backup → Deploy → Configure → Migrate → Reconcile → Smoke → Business Verify → Enable) อธิบายว่าแต่ละขั้น "เสี่ยงอะไร + ต้องตรวจอะไร"
  2. §4.4 (Rollback) — เพิ่มตัวอย่าง rollback trigger เชิงตัวเลขจริง (payment failure >4%, response >N วินาที) + เหตุผลว่าทำไมต้องมี "เวลาจำกัดในการตัดสินใจ" (ตัดสินช้า = ผลกระทบขยาย)
  3. §4.5 (Hypercare) — ขยาย command center: ใครอยู่ในห้อง, escalate ยังไง, daily review ดูอะไร
  4. §4.6 (Stabilization) — อธิบายว่า exit criteria ที่ดีต้อง "วัดได้ + มีระยะเวลา" ไม่ใช่ "รู้สึกว่านิ่งแล้ว"
  5. §6 — เขียนเป็น Watch PM Think เล่า cutover คืนวันศุกร์จริง ๆ
- **Source:** Playbook G.2–G.9
- **DoD:** Cutover sequence มี narrative ต่อขั้น · Rollback มี trigger เชิงตัวเลข + เหตุผลเรื่องเวลาจำกัด · Hypercare command center ชัด · Stabilization exit criteria วัดได้

### Ch.10 — Transition & Closure / Playbook H
- **จุดอ่อน:** Closure เป็น Integration ท่อนที่ 3 แต่เขียนบาง ทั้งที่ H.3–H.9 มีรายละเอียด (handover, final acceptance, contract/financial closure, lessons learned, benefit handover)
- **ต้องเสริม:**
  1. §4 — **Operational Handover (H.3)**: อธิบายว่า handover ให้ Ops ไม่ใช่แค่ส่งเอกสาร — ต้องมี runbook, training, support transition, SLA
  2. §4 — **Lessons Learned (H.6)**: อธิบายทำไมต้องทำ**ระหว่าง**โครงการ ไม่ใช่รอจบ (รอจบ = ทีมลืม + แยกย้าย) — เทคนิค retrospective
  3. §4 — **Benefit Handover (H.7)**: นี่คือจุดที่ output → outcome — อธิบายว่าใครรับผิดชอบวัด benefit หลังจบ (35% direct booking วัดตอนไหน ใครวัด)
  4. §4 — **Contract/Financial Closure (H.5)**: final payment, warranty start, release of resources
  5. §4 — **Closure Report (H.8)**: องค์ประกอบ + ทำไมต้องมี (หลักฐานจบโครงการ)
- **Source:** Playbook H.3–H.9 · `e-Book/chapters/lesson-05` (Close Project or Phase)
- **DoD:** Handover ครบ (runbook/training/SLA) · Benefit handover อธิบาย output→outcome · Lessons learned มีเหตุผลเรื่อง timing

---

## 6. Bug/typo ที่ต้องแก้ระหว่างทาง (เจอแล้ว — อย่าพลาด)

- `ch-09-learner.md:105` — "stabilizaztion" → **"stabilization"**
- `ch-09-learner.md:192` — "ตรวจว่าดีploy ผ่าน" → **"ตรวจว่า deploy ผ่าน"**
- (ระหว่างแก้ทุกบท ให้ proofread ภาษาไทยปนศัพท์ผิดแบบนี้ด้วย — ถ้าเจอเพิ่ม ให้แก้ + บันทึกใน log)

---

## 7. Definition of Done

### ต่อบท
- [ ] §4 Main Lesson: ไม่มีลิสต์ concept เปล่า ≥ 4 ข้อ — แปลงเป็นร้อยแก้ว/ตารางมีคอลัมน์ "ทำไม" แล้ว
- [ ] §6 มี Watch PM Think (เล่าเหตุผลในหัว PM) อย่างน้อย 1 จุด
- [ ] §7 Common Mistakes: ข้อสำคัญ ≥ 2 ข้อถูกขยายเป็น mini-story "พลาดแล้วเกิดอะไร"
- [ ] ทุกย่อหน้าใหม่มี source label ถูกต้อง
- [ ] ตัวเลข/roles scenario ตรง `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` v1.0
- [ ] คำศัพท์ใหม่ sync เข้า `governance/PM_GLOSSARY.md` แล้ว
- [ ] instructor/answer-key sync แล้ว (เฉพาะที่จำเป็น)
- [ ] relative links ยังใช้ได้ทั้งหมด
- [ ] frontmatter ไม่เปลี่ยน (ยกเว้น `last_reviewed`)

### ต่อเล่ม
- [ ] ทั้ง 11 บท deepen ครบตาม spec รายบท
- [ ] ตรวจ cross-reference Quality (Ch.5/6/8) และ Integration (Ch.2/7/10) ยังชัดหลังแก้
- [ ] proofread typo ทั้งเล่ม
- [ ] rebuild PDF 2 ฉบับผ่าน (`build_pdf.py` → Complete + Learner edition)
- [ ] บันทึก log ครบทุกบท

---

## 8. ลำดับการทำ + Template log

**ลำดับที่แนะนำ:** ทำเรียงจากบางสุด → หนาสุดเพื่อให้เห็นผลเร็ว:
`Ch.0 → Ch.9 → Ch.10 → Ch.8 → Ch.7 → Ch.6 → Ch.3 → Ch.4 → Ch.5 → Ch.2 → Ch.1`
(หรือทำเรียงลำดับ A→H ก็ได้ ตามสะดวก — แต่ Ch.0/Ch.9/Ch.10 ควรทำก่อนเพราะบางสุด)

**บันทึกทุกบทที่ทำเสร็จลงในไฟล์ `Ver.2/FreeBuff_Fixed_Update.md`** (หรือไฟล์ log ใหม่ `field-guide/DEEPENING-LOG.md` ถ้า FreeBuff log เต็ม) ด้วย template:

```
## YYYY-MM-DD — Deepen Ch.N (<ชื่อบท>)

**ทำอะไรไปแล้ว (อ้าง spec §5):**
-

**คำ/แนวคิดใหม่ที่เพิ่ม:**
-

**คำศัพท์ที่ sync เข้า PM_GLOSSARY (ถ้ามี):**
-

**แก้ typo:**
-

**DoD check (อ้าง §7):**
- [ ] …

**ติดตรงไหน / ตัดสินใจเอง (ถ้ามี):**
-
```

---

## 9. หมายเหตุถึงเจ้าของ repo

- ไฟล์นี้เขียนไว้ใน `field-guide/pdf/` ตามที่ขอ — ถ้าต้องการให้อยู่รวมกับเอกสาร planning อื่น อาจย้ายไป `Ver.2/` หรือ `field-guide/` root ก็ได้ (ไม่มีผลทางเทคนิคต่อ `build_pdf.py` เพราะสคริปต์อ่านเฉพาะไฟล์บทใน `chapters/`)
- Deepen เสร็จแล้ว **ยังไม่ต้องแตะ `e-Book/`** (Phase 6 ยังรอ approve เหมือนเดิม) — งานนี้ทำใน `field-guide/chapters/` เท่านั้น

# Deepening Log — Ver.2 (field-guide)

> บันทึกรายบทตาม `field-guide/pdf/DEEPENING-PLAN.md` §8 — ทำเรียงตามลำดับที่แนะนำ (บางสุด → หนาสุด):
> `Ch.0 → Ch.9 → Ch.10 → Ch.8 → Ch.7 → Ch.6 → Ch.3 → Ch.4 → Ch.5 → Ch.2 → Ch.1`
> งานทำใน `field-guide/chapters/` เท่านั้น — ไม่แตะ `e-Book/` (Phase 6 ยังรอ approve)
> สรุปรวม + commit อยู่ใน `Ver.2/FreeBuff_Fixed_Update.md` Round 11

---

## 2026-08-15 — Deepen Ch.0 (PMBOK Primer)

**ทำอะไรไปแล้ว (อ้าง spec §5):**
- §4.2 — 6 Principles / 7 Domains / 5 Focus Areas: ทุกแถวเพิ่ม 1 บรรทัด "แปลเป็นภาษาคนทำงาน" (เช่น Value Focus → "ถามเสมอว่า งานที่ทำตอนนี้ทำให้ business ได้ผลลัพธ์อะไร ไม่ใช่แค่เสร็จตาม plan")
- §4.3 — เพิ่มตัวอย่าง Process Group เกิดซ้ำในโครงการจริง (กลาง execution กลับไป re-plan หลัง scope เปลี่ยน)
- §4.5 — เพิ่มตัวอย่าง Field Mode lookup: PM เจอ "ลูกค้าขอเพิ่ม scope" → เปิด Appendix F → เจอ Ch.7 → Quick Reference Card
- §2 — เพิ่ม mini-story "PM ที่ไม่รู้กรอบ → ตามงานอย่างเดียว มองไม่เห็น risk/benefit"

**คำ/แนวคิดใหม่ที่เพิ่ม:** ภาษาคนทำงานของ Principles/Domains/Focus Areas, re-plan loop, Field Mode lookup path

**คำศัพท์ที่ sync เข้า PM_GLOSSARY (ถ้ามี):** ไม่มี (ไม่มีคำ EN ใหม่)

**แก้ typo:** ไม่พบเพิ่ม

**DoD check (อ้าง §7):** ✅ §4.2 ทุกแถวมี "แปลเป็นภาษาคนทำงาน" · §4.3 มีตัวอย่าง re-plan · §4.5 มีตัวอย่าง lookup 1 จุด

---

## 2026-08-15 — Deepen Ch.9 (Go-Live & Hypercare)

**ทำอะไรไปแล้ว (อ้าง spec §5):**
- §4.2 (Cutover) — ขยายเป็น sequence narrative ต่อขั้น (Freeze → Backup → Deploy → Configure → Migrate → Reconcile → Smoke → Business Verify → Enable) อธิบายแต่ละขั้น "เสี่ยงอะไร + ต้องตรวจอะไร"
- §4.4 (Rollback) — เพิ่ม rollback trigger เชิงตัวเลขจริง (payment failure > 4%, response > เกณฑ์) + เหตุผล "เวลาจำกัดในการตัดสินใจ" (ตัดสินช้า = ผลกระทบขยาย)
- §4.5 (Hypercare) — ขยาย command center: ใครอยู่ในห้อง, escalate ยังไง, daily review ดูอะไร
- §4.6 (Stabilization) — อธิบายว่า exit criteria ที่ดีต้อง "วัดได้ + มีระยะเวลา" ไม่ใช่ "รู้สึกว่านิ่งแล้ว"
- §6 — เขียนเป็น Watch PM Think เล่า cutover คืนจริง (soft launch 3 โรงแรม 02:00–06:00)

**คำ/แนวคิดใหม่ที่เพิ่ม:** cutover sequence, rollback trigger, command center, stabilization exit criteria

**คำศัพท์ที่ sync เข้า PM_GLOSSARY (ถ้ามี):** Command Center (เพิ่มแถวใหม่)

**แก้ typo:** `stabilizaztion` → `stabilization` (บรรทัดที่ระบุในแผน §6), `ดีploy` → `deploy` (แผน §6) — แก้ครบ 2 จุด

**DoD check (อ้าง §7):** ✅ Cutover sequence มี narrative ต่อขั้น · Rollback มี trigger เชิงตัวเลข + เหตุผลเรื่องเวลาจำกัด · Hypercare command center ชัด · Stabilization exit criteria วัดได้

---

## 2026-08-15 — Deepen Ch.10 (Transition & Closure)

**ทำอะไรไปแล้ว (อ้าง spec §5):**
- §4 (Operational Handover) — อธิบายว่า handover ให้ Ops ไม่ใช่แค่ส่งเอกสาร: runbook, training, support transition, SLA
- §4 (Lessons Learned) — อธิบายทำไมต้องทำ**ระหว่าง**โครงการ ไม่ใช่รอจบ (รอจบ = ทีมลืม + แยกย้าย) + เทคนิค retrospective
- §4 (Benefit Handover) — output → outcome: ใครวัด 35% direct booking ตอนไหน ใครรับผิดชอบหลังจบ
- §4 (Contract/Financial Closure) — final payment, warranty start, release of resources
- §4 (Closure Report) — องค์ประกอบ + ทำไมต้องมี (หลักฐานจบโครงการ)
- §6 — Playbook H เป็นลิสต์ → เติมชั้น "ทำไม" + แปลงเป็น Watch PM Think

**คำ/แนวคิดใหม่ที่เพิ่ม:** operational handover (runbook/training/SLA), lessons learned timing, benefit handover, financial closure

**คำศัพท์ที่ sync เข้า PM_GLOSSARY (ถ้ามี):** Closure Report (เพิ่มแถวใหม่)

**แก้ typo:** ไม่พบเพิ่ม

**DoD check (อ้าง §7):** ✅ Handover ครบ (runbook/training/SLA) · Benefit handover อธิบาย output→outcome · Lessons learned มีเหตุผลเรื่อง timing

---

## 2026-08-15 — Deepen Ch.8 (Verification/UAT)

**ทำอะไรไปแล้ว (อ้าง spec §5):**
- §4 — ตาราง **Test Levels** (Unit → Integration → System → UAT: ทดสอบอะไร / ใครทำ / พบอะไร) พร้อมตัวอย่าง SHG
- §4 — **QA vs UAT** ต่างชัด (QA = ตาม spec, UAT = ตาม need ของ user) + cross-ref ไป Ch.5 (Test Strategy) ตามคำเตือน Quality ที่ถูกผ่า
- §4 — **RTM** อธิบายทำไมต้องมี + ตัวอย่างแถว (requirement → design → test case → result)
- §4 — **Severity vs Priority** ต่างกันยังไง (จุดสัมภาษณ์ PM บ่อย) — ตัวอย่าง payment defect
- §4 — **Go/No-Go** ใครตัดสิน + evidence อะไร
- §6 — Watch PM Think: สัปดาห์ Go/No-Go (Conditional Go — soft launch 3 โรงแรม)

**คำ/แนวคิดใหม่ที่เพิ่ม:** test levels, QA vs UAT, RTM trace, severity vs priority, conditional go

**คำศัพท์ที่ sync เข้า PM_GLOSSARY (ถ้ามี):** Severity (เพิ่มแถวใหม่)

**แก้ typo:** ไม่พบเพิ่ม

**DoD check (อ้าง §7):** ✅ Test levels ครบ + ตัวอย่าง · QA vs UAT ต่างชัด · RTM มีตัวอย่างแถว · severity vs priority ชัด

---

## 2026-08-15 — Deepen Ch.7 (Monitoring & Change)

**ทำอะไรไปแล้ว (อ้าง spec §5):**
- §4 — **Change Flow 6 ขั้น** (Submit → Impact Analysis → CCB Review → Approve/Reject → Implement → Verify) พร้อมตัวอย่างจริง "ลูกค้าขอเพิ่ม payment method"
- §4 — **Impact Areas** เป็นตาราง (change หนึ่งตัวกระทบ scope/schedule/cost/quality/resource/risk/procurement)
- §4 — **Change Authority** ใคร approve ระดับไหน (CCB ประกอบด้วยใคร, threshold)
- §4 — **Scope Validation vs Scope Control** ต่างกันชัด
- §4 — EVM control: VAC/EAC/ETC อธิบายเชิงบริหาร (CPI<1 ต้องตัดสินใจอะไร)
- §6 — Watch PM Think เพิ่ม

**คำ/แนวคิดใหม่ที่เพิ่ม:** change flow, impact areas, change authority, validate vs control, VAC/EAC/ETC

**คำศัพท์ที่ sync เข้า PM_GLOSSARY (ถ้ามี):** ไม่มีเพิ่ม (CCB/Impact Analysis มีอยู่แล้วในส่วน Ver.2)

**แก้ typo:** ไม่พบเพิ่ม

**DoD check (อ้าง §7):** ✅ Change flow ครบ 6 ขั้น + ตัวอย่าง · Impact areas ครบ · Validate vs Control ต่างชัด

---

## 2026-08-15 — Deepen Ch.6 (Execution)

**ทำอะไรไปแล้ว (อ้าง spec §5):**
- §4 — **DoR vs DoD** เป็นตารางเทียบ + ตัวอย่าง checklist จริงสำหรับ user story ของ SHG
- §4 — **Execution flow Predictive vs Agile vs Hybrid**: แต่ละแบบ "จังหวะตรวจ/ปรับ" ต่างกันตรงไหน
- §4 — **Manage Quality vs Control Quality** (Quality ฝั่ง Execute) + cross-ref ไป Ch.8 ตามคำเตือน Quality ที่ถูกผ่า
- §6 — Watch PM Think: PM จัดการทีม dev ระหว่าง sprint (standup, blocker, impedance)

**คำ/แนวคิดใหม่ที่เพิ่ม:** DoR/DoD, execution flow 3 แบบ, manage vs control quality

**คำศัพท์ที่ sync เข้า PM_GLOSSARY (ถ้ามี):** ไม่มีเพิ่ม (Definition of Done/Ready มีอยู่แล้ว)

**แก้ typo:** ไม่พบเพิ่ม

**DoD check (อ้าง §7):** ✅ DoR vs DoD เทียบชัด + ตัวอย่าง · Execution flow 3 แบบอธิบายต่างกัน · Quality cross-ref ครบ

---

## 2026-08-15 — Deepen Ch.3 (Requirements/Scope/WBS)

**ทำอะไรไปแล้ว (อ้าง spec §5):**
- §4 — **SRS vs FSD** + Document Substitution Matrix: เมื่อไรทำ FSD ได้ เมื่อไรทำไม่ได้ (ห้ามตัด FSD โดยไม่มีสิ่งทดแทน)
- §4 — **100% Rule** อธิบายด้วยตัวอย่าง WBS ของ Direct Booking Platform (child รวม = parent ครบ ไม่เกิน ไม่ขาด)
- §4 — **WBS Dictionary**: แปลง template fields เป็นตาราง "field → ทำไมต้องมี"
- §4 — **Requirement Quality Checklist** (SMART / measurable / testable) พร้อมตัวอย่าง requirement ที่ดี vs แย่
- §6 — Watch PM Think เพิ่ม

**คำ/แนวคิดใหม่ที่เพิ่ม:** SRS vs FSD, substitution matrix, 100% rule, WBS dictionary fields, requirement quality

**คำศัพท์ที่ sync เข้า PM_GLOSSARY (ถ้ามี):** SRS, FSD (เพิ่มแถวใหม่ — WBS Dictionary มีอยู่แล้ว)

**แก้ typo:** ไม่พบเพิ่ม

**DoD check (อ้าง §7):** ✅ มี SRS/FSD substitution logic ชัด · 100% Rule มีตัวอย่าง · WBS Dictionary อธิบายเหตุผลแต่ละ field

---

## 2026-08-15 — Deepen Ch.4 (Schedule/Cost/Resource)

**ทำอะไรไปแล้ว (อ้าง spec §5):**
- §4 — **CPM ตัวอย่างคำนวณจริง**: dependency network เล็ก (4–5 กิจกรรม) คำนวณ ES/EF/LS/LF/Float หา Critical Path
- §4 — **Three-Point Estimate**: สูตร (O+4M+P)/6 + อธิบายทำไม weighted กลาง (ลดผลของ outlier)
- §4 — **EVM** ต่อยอดตัวอย่างตัวเลข (PV/EV/AC → SPI/CPI/EAC) อธิบายความหมายเชิงบริหาร (ตามงาน/เกินงบ → ต้องตัดสินใจอะไร)
- Agile insert — อธิบาย Schedule บน Kanban/Scrum ต่างจาก CPM ตรงไหน (เมื่อไรใช้แบบไหน)
- §6 — Watch PM Think เพิ่ม

**คำ/แนวคิดใหม่ที่เพิ่ม:** CPM calculation, three-point estimate, EVM managerial meaning, agile vs CPM

**คำศัพท์ที่ sync เข้า PM_GLOSSARY (ถ้ามี):** CPM, Three-Point Estimate (เพิ่มแถวใหม่ — Critical Path มีอยู่แล้วในส่วนหลัก)

**แก้ typo:** ไม่พบเพิ่ม

**DoD check (อ้าง §7):** ✅ มี CPM คำนวณตัวอย่าง · three-point มีสูตร+เหตุผล · EVM อธิบายความหมายเชิงบริหารไม่ใช่แค่สูตร

---

## 2026-08-15 — Deepen Ch.5 (Risk/Procurement/Comms)

**ทำอะไรไปแล้ว (อ้าง spec §5):**
- §4 — **Risk vs Issue** เส้นแบ่งชัด + ตัวอย่าง "PMS API ไม่พร้อม" เป็น Risk → กลายเป็น Issue เมื่อเกิดจริง (ข้ามไป Ch.7)
- §4 — **Risk Response Strategy** (Avoid/Mitigate/Transfer/Accept + positive) เป็นตาราง strategy → เมื่อไรใช้ → ตัวอย่าง SHG
- §4 — **Contract type** (Fixed vs T&M vs Hybrid) + Make-or-Buy ผูกตัวอย่าง BTS ใน Ch.1 (Fixed core + T&M PMS adapter)
- §4 — **Communication Plan**: ระดับ stakeholder → ประเภทข้อมูล → ความถี่ (Typical Cadence)
- §4 — C17 Release/Environment/Transition วางแผนล่วงหน้า + cross-ref ไป Ch.9 (ของจริง)
- §6 — Watch PM Think เพิ่ม

**คำ/แนวคิดใหม่ที่เพิ่ม:** risk vs issue, risk response strategy, contract type selection, comms cadence

**คำศัพท์ที่ sync เข้า PM_GLOSSARY (ถ้ามี):** ไม่มีเพิ่ม (Make-or-Buy/Residual Risk มีอยู่แล้วในส่วน Ver.2)

**แก้ typo:** ไม่พบเพิ่ม

**DoD check (อ้าง §7):** ✅ Risk vs Issue เส้นแบ่งชัด · Risk response ครบ + ตัวอย่าง · Contract type ผูกตัวอย่าง BTS · Comms plan มี cadence

---

## 2026-08-15 — Deepen Ch.2 (Initiation)

**ทำอะไรไปแล้ว (อ้าง spec §5):**
- §4 — **Power/Interest Grid** 4 ช่อง (Manage Closely / Keep Satisfied / Keep Informed / Monitor) พร้อมวางตัวละคร SHG ลงช่อง (คุณจิรา CEO = High/High → Manage Closely)
- §4 — **Charter = อำนาจของ PM** ไม่ใช่เอกสารพิธีกรรม — mini-story PM ทำงานแล้วโดน stakeholder ไม่ให้ความร่วมมือเพราะไม่มี Charter
- §4 — **RAID** อธิบายครบ 4 ตัว + ทำไมต้องแยก Assumption (Assumption ที่ผิดกลายเป็น Risk)
- §6 — Watch PM Think เพิ่ม

**คำ/แนวคิดใหม่ที่เพิ่ม:** power/interest grid placement, charter-as-authority, RAID ครบ 4 ตัว

**คำศัพท์ที่ sync เข้า PM_GLOSSARY (ถ้ามี):** Power/Interest Grid (เพิ่มแถวใหม่ — RAID มีอยู่แล้ว)

**แก้ typo:** ไม่พบเพิ่ม

**DoD check (อ้าง §7):** ✅ มี Power/Interest Grid วางตัวละครจริง · Charter อธิบาย "ทำไมคืออำนาจ" · RAID อธิบายครบ 4 ตัว

---

## 2026-08-15 — Deepen Ch.1 (Pre-sales)

**ทำอะไรไปแล้ว (อ้าง spec §5):**
- §4.5 (ROM) — ขยาย "ทำไม ROM ต้องเป็นช่วง + confidence": ตัวเลขเดียวถูกอ่านเป็นราคาผูกพัน = กับดัก + ตัวอย่างตัวเลข BTS (ช่วง 6.0–8.5 → Fixed 6.5M + T&M cap 0.5M)
- §4.7 (Proposal 19 ข้อ) — แปลงลิสต์เป็น**ตาราง 2 คอลัมน์** (องค์ประกอบ → ทำไมต้องมี/พลาดแล้วเกิดอะไร) ครบ 19 แถว ตามหลัก D2
- §6 — เขียนเป็น **Watch PM Think**: เล่าเหตุผลในหัว Pre-sales PM ตอนเจอ "PMS ต่างยี่ห้อ 3 ตัว API ไม่ครบ" (การตัดสินใจ Option B Hybrid + เหตุผลเรื่อง risk allocation)

**คำ/แนวคิดใหม่ที่เพิ่ม:** ROM range + confidence logic, proposal element rationale, hybrid risk allocation

**คำศัพท์ที่ sync เข้า PM_GLOSSARY (ถ้ามี):** ไม่มีเพิ่ม (ROM/Fixed Price/T&M มีอยู่แล้ว)

**แก้ typo:** ไม่พบเพิ่ม

**DoD check (อ้าง §7):** ✅ §4.7 ไม่เหลือลิสต์เปล่า (เป็นตาราง 19 แถวมี "ทำไม") · §6 มี Walkthrough คิดตาม PM · ROM มีเหตุผลเรื่องช่วง+confidence

---

## สรุปหลังครบทุกบท

- ทั้ง 11 บท deepen ครบตาม spec รายบท (Ch.0 → Ch.1 ตามลำดับแผน §8)
- Glossary sync เพิ่ม 8 คำ: Command Center, Closure Report, CPM, FSD, Power/Interest Grid, Severity, SRS, Three-Point Estimate
- แก้ typo 2 จุดตามแผน §6 (stabilizaztion, ดีploy ใน Ch.9) — ตรวจซ้ำทั้งเล่มไม่พบเพิ่ม
- Link check: 40 ลิงก์ 0 broken · Cross-ref Quality (Ch.5/6→8) และ Integration (Ch.2/7/10) ยังชัด
- Rebuild PDF: Complete 196 หน้า (165 headers), Learner 132 หน้า (102 headers) — ไม่มี `**`/`&gt;` หลุด
- Commit (ไม่ push) — ดู `Ver.2/FreeBuff_Fixed_Update.md` Round 11

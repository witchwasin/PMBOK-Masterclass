# FreeBuff Update Log

> เขียนโดย FreeBuff เท่านั้น ใหม่สุดอยู่บนสุด แต่ละรอบต้องมีวันที่กำกับ ใช้ template ด้านล่างทุกรอบ
>
> **โหมด: End-to-end** — ทำ Phase 0 ถึง Phase 5 (ดู `master_plan.md` §6) รวดเดียวจนจบ ไม่ต้องหยุดรอคำตอบระหว่างทาง บันทึกทุก Phase ที่ทำเสร็จลงที่นี่เป็น entry ใหม่ไปเรื่อยๆ (running log) แล้วปิดท้ายด้วย entry สรุปจบงานทั้งเล่มเมื่อ Phase 5 เสร็จ — Claude จะรีวิวครั้งเดียวหลังเห็น entry สรุปจบงานเท่านั้น
>
> **ข้อยกเว้นเดียวที่ต้องหยุดจริงและรอ:** ห้ามลงมือ Phase 6 (แตะ `e-Book/`) เอง — เขียนข้อเสนอไว้ที่นี่แล้วรอ approve เท่านั้น

## Template สำหรับแต่ละรอบ (copy ไปใช้ทุกครั้งที่อัปเดต)

```
## YYYY-MM-DD — Round N (Phase X)

**ทำอะไรไปแล้ว:**
-

**Output/ไฟล์ที่สร้างหรือแก้:**
-

**การตัดสินใจที่ทำเอง (ถ้ามี เช่น ชื่อเล่ม, Scenario decision):**
-

**ติดตรงไหน / ยังไม่แน่ใจ:**
-

**คำถามถึง Claude (ไม่ต้องรอคำตอบ บันทึกไว้ก่อนแล้วไปต่อ เว้นแต่ block งานจริง):**
-
```

## Template สำหรับ entry สุดท้าย (เมื่อ Phase 5 เสร็จ — จุดเดียวที่หยุดรอ Claude)

```
## YYYY-MM-DD — งานเสร็จทั้งเล่ม พร้อมให้ Claude review

**สรุปทุก Phase ที่ทำ (0–5):**
-

**Definition of Done (master_plan.md §8) — self-check:**
-

**ข้อเสนอสำหรับ Phase 6 (archive e-Book/):**
-

**พร้อมให้ review: ใช่**
```

---

## 2026-08-15 — Round 10 (จัดหน้า e-Book ใหม่: Running Head "บทที่ N: ชื่อบท | P{หน้า}" + Typography Upgrade)

> **ที่มาของรอบนี้:** เจ้าของ repo ขอให้ออกแบบการจัดหน้าเล่มใหม่ — เพิ่มชื่อบทลงในหัวกระดาษทุกหน้าตามฟอร์แมต "บทที่ 3: xxxx | P18" + ใช้สกิลจัดหน้าให้อ่านง่าย (สารบัญ, แถบหัวข้อ, ตาราง, callout) — แก้ใน `field-guide/pdf/build_pdf.py` เท่านั้น ไม่แตะเนื้อหาบท และไม่แตะ `e-Book/`

**ทำอะไรไปแล้ว:**
1. **Running Head "บทที่ N: ชื่อบท | P{เลขหน้า}" ทุกหน้า** — ใช้ CSS **named pages** (`@page ch03 { @top-left { content: "บทที่ 3: ... | P" counter(page); } }`) ซึ่ง Chrome 151 รองรับจริง (ทดสอบ empirical แล้ว — `string-set` ไม่รองรับใน Chrome เลยต้องใช้ named pages):
   - บท → "บทที่ 0: PMBOK Primer — กรอบคิด A→H | P4" … "บทที่ 10: ... | P123"
   - ภาคผนวก → "ภาคผนวก A — Artifact Catalogue | P87"
   - สารบัญ → "สารบัญ / Table of Contents | P2"
   - ส่วน Instructor/Answer Key → "... (Instructor) | P11" และ part-divider ก็ได้ header ด้วย
   - **หน้าเปิดบทไม่มี header** (สะอาด): สร้าง page type แยก `chNN-o` เพราะ Chrome ตีความ `:first` = "หน้าแรกของเอกสารเท่านั้น" ไม่ใช่หน้าแรกของแต่ละบท — ทดสอบแล้ว ยืนยันด้วย pypdf ว่าแต่ละฉบับมีหน้าไร้ header = 12 (cover + 11 หน้าเปิดบท) ตรงเป๊ะ
2. **แก้บั๊ก render markdown ที่มีอยู่ใน PDF เดิม (เจอตอนตรวจด้วยตา):**
   - `**bold**` เดิมหลุดเป็นตัวอักษร `**` ถึง 499 จุดใน HTML → เพิ่มการแปลง bold/italic ใน `inline()` (พร้อม protect code span ไม่ให้โดน rewrite)
   - blockquote `> **หมายเหตุ:**` เดิมกลายเป็น `&gt;` หน้าข้อความ → แปลงเป็น `<blockquote>` callout box จริง
   - checkbox `- [ ]` เดิมหลุดเป็นตัวอักษร → แปลงเป็นกล่องติ๊ก (box จริง ผ่าน `::before`)
3. **Typography / จัดหน้าใหม่ทั้งเล่ม:**
   - **Cover:** เต็มหน้าน้ำเงินเข้ม gradient (margin 0 บนหน้าแรก) + brand + ชื่อเล่ม + rule + badge edition
   - **หน้าเปิดบท:** kicker (เช่น "C · REQUIREMENTS & SCOPE") + แถบ title สี gradient น้ำเงินเข้ม + มุมโค้ง
   - **หัวข้อ:** h2 มีแถบ accent น้ำเงินซ้าย, h3/h4 โทนน้ำเงินไล่ระดับ
   - **ตาราง:** หัวตารางพื้นน้ำเงินเข้มตัวขาว + zebra แถวคู่ + header ซ้ำข้ามหน้า (`table-header-group`)
   - **callout:** แถบซ้ายหนา + พื้นฟ้าอ่อน + กันไม่ให้ตัดกลางหน้า
   - **สารบัญ:** เส้นประคั่นรายการ + sub-entry ชัดเจน (มีในทั้ง 2 ฉบับ)
   - เพิ่ม `background: #fff` ให้ body, `print-color-adjust: exact` เพื่อให้สีพิมพ์ออกจริง
4. **Rebuild + ตรวจยืนยันด้วย pypdf ครบ:** header เรียงลำดับถูกต้องทั้ง 2 ฉบับ (สารบัญ → บทที่ 0–10 → ภาคผนวก A–F), ทุก header ลงท้าย `| P{เลข}`, ไม่มี `**`/`&gt;`/`&amp;`/`- [ ]` หลุด, หน้าไร้ header = 12/ฉบับ — ดูภาพจริงผ่าน Preview แล้ว (cover, หน้าเปิดบท, ตาราง, checklist ผ่าน)

**Output/ไฟล์ที่สร้างหรือแก้:**
- `field-guide/pdf/build_pdf.py` (rewrite: named-page running heads + markdown fixes + typography CSS)
- `field-guide/pdf/PM-Delivery-Guide-Complete-Edition.pdf` — **187 หน้า** (~3.25 MB)
- `field-guide/pdf/PM-Delivery-Guide-Learner-Edition.pdf` — **123 หน้า** (~2.48 MB)
- `field-guide/pdf/book.html` + `field-guide/pdf/book-learner.html` (regenerate)
- `Ver.2/FreeBuff_Fixed_Update.md` (ไฟล์นี้)

**การตัดสินใจที่ทำเอง:**
- ใช้ named pages แทน `string-set` (Chrome ไม่รองรับ string-set — ทดสอบแล้ว) และแยก page type หน้าเปิดบท (`chNN-o`) แทน `:first` (Chrome ตีความ `:first` เป็นหน้าแรกของเอกสารเท่านั้น)
- แก้บั๊ก bold/blockquote/checkbox ใน converter ด้วย — เป็นงานจัดหน้าโดยตรง (เดิม `**` โผล่เป็นตัวอักษรใน PDF)
- หน้าเปิดบทไม่มี header (หน้าแรกของบทสะอาด) — ส่วนหน้าอื่นมี header ครบทุกหน้า ตามที่ขอ

**ติดตรงไหน / ยังไม่แน่ใจ:**
- ไม่มี — ตรวจยืนยันผ่าน pypdf + ดูภาพจริงผ่าน Preview เรียบร้อย

**พร้อมให้ review: ใช่**

---

## 2026-08-14 — Round 9 (Self-review ก่อนส่ง Claude — ผ่านครบ ไม่พบจุดต้องแก้)

> **ที่มาของรอบนี้:** Claude เครดิตหมด เจ้าของ repo ให้ FreeBuff review เองก่อน — ตรวจเทียบ `master_plan.md` §8 (Definition of Done) ครบทุกข้อแล้ว ผ่านทั้งหมด ไม่มีการแก้เนื้อหา

**ตรวจอะไรไปแล้ว (เทียบ DoD §8):**
1. **Template 15 หัวข้อ:** Ch.0–10 ทุกบทมีครบ 15 section (ตรวจด้วย grep หัวข้อ `## 1.`–`## 15.`) — Ch.0 มี section ครบแต่เนื้อหา Workshop/Assessment ระบุชัดว่า "บทปฐมบทไม่มี" ตาม master_plan §5 ✓
2. **Frontmatter:** ครบทั้ง 33 ไฟล์บท (ทุกไฟล์ขึ้นต้นด้วย `---`) ✓
3. **Source labels:** `[PMBOK 8]` 39×, `[Teaching Scenario]` 47×, `[Best Practice]` 63×, `[Teaching Scenario Extension]` 8× — ไม่มี `[PMBOK 6]/[PMBOK 7]` หลงในไฟล์บทของเล่มใหม่ ✓
4. **Relative links:** รัน link checker อัตโนมัติ — 40 ลิงก์ ALL LINKS OK (0 broken) ✓
5. **Scenario ตรง Scenario Master:** 12M / 35% / 18 เดือน / 12 โรงแรม / NPS 40 / Sprint 0 / launch ก่อน 1 พ.ย. / roles (คุณจิรา, คุณสุทธิ, คุณนภา, คุณภัทร, คุณวีระ, คุณสมศรี) ตรง `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` ทุกจุด — vendor layer "Booking Tech Solutions" ใช้เฉพาะ Ch.1–2 ตามที่ล็อกไว้ ✓
6. **Cross-reference KA ที่ถูกผ่า:** Quality — Ch.5 (Test Strategy วางแผน ↔ Ch.8 ผลจริง, Ch.6 QA) เขียนชัดทั้ง 3 บท; Integration — Ch.2 (Charter) / Ch.7 (Change, "ท่อนที่ 2 ของ 3") / Ch.10 (Close, "ท่อนที่ 3") ✓
7. **Appendix ครบ 6 ตัว** (A–F) + **33 ไฟล์บท** (11 บท × learner/instructor/answer-key) + instructor ทุกบทมี Teaching Notes/Suggested Timing ✓
8. **Assessment:** Ch.1–10 บทละ 7 ข้อ (อยู่ในช่วง 5–8 ตาม template §12) ✓
9. **Governance:** glossary กลางมี "Ver.2 additions" (บรรทัด 146), `CONTENT-RULES.md` มี label `[PMBOK 8]` (3 จุด), `PMBOK-EDITION-POSITION.md` มี §8 ✓
10. **PDF:** 2 ฉบับ build ผ่าน (Complete 2796 KB / Learner 2137 KB, rebuild 2026-08-14 02:44–02:45 หลังแก้ cover/TOC) + Appendix E PDF เดิมยังอยู่ ✓
11. **`e-Book/` untouched:** `git diff HEAD --stat -- e-Book/` = ว่าง (0 ไฟล์) ✓

**ผลการตัดสินใจ:** ไม่พบจุดที่ต้องแก้ — งานทั้งหมดผ่าน self-check เทียบ DoD §8 ครบทุกข้อ

**Output/ไฟล์ที่สร้างหรือแก้:** ไม่แก้ไฟล์เนื้อหาใดๆ (รอบนี้เป็น review-only) — บันทึกผลไว้ในไฟล์นี้เท่านั้น

**ติดตรงไหน / ยังไม่แน่ใจ:** ไม่มี — พร้อมให้ Claude ตรวจซ้ำวันถัดไปตามที่เจ้าของ repo นัด

**พร้อมให้ review: ใช่**

---

## 2026-08-14 — Round 8 (แก้ 4 ข้อ: Ch.5 Quick Ref + PDF bugs + Coverage Matrix + Phase 6 Proposal)

**ทำอะไรไปแล้ว:**
1. **แก้ Ch.5 Quick Reference Card** — `field-guide/chapters/ch-05/ch-05-learner.md` บรรทัดที่ 335: เดิม "(V = ตาม spec, V = ตาม need)" ซ้ำกันจนแยกไม่ออก → แก้เป็น "(Ver = ตาม spec, Val = ตาม need)" (Verification = ตาม spec, Validation = ตาม need) — ตรวจแล้วไม่มีบรรทัดอื่นใช้คำย่อซ้ำกัน
2. **แก้บั๊ก PDF ใน `field-guide/pdf/build_pdf.py` + rebuild ทั้ง 2 ฉบับ:**
   - Cover page แยกตาม edition จริง: Learner Edition มีข้อความ cover ว่าเป็นฉบับ Learner อย่างเดียว (ไม่ใช่ "Learner + Instructor Companion — Combined"), Complete Edition ยังเป็นเล่มรวมตามเดิม
   - TOC ของ Learner Edition ตัด sub-entry "Instructor Guide" / "Answer Key" ออกทุกบท (เหลือ 17 entries = 11 บท + 6 Appendix, ไม่มี sub) — ตรวจด้วย regex ว่าไม่มี "Teaching Notes"/"Suggested Timing" ใน HTML ของ Learner
   - Rebuild สำเร็จ: `PM-Delivery-Guide-Complete-Edition.pdf` + `PM-Delivery-Guide-Learner-Edition.pdf` (HTML 2 ไฟล์ regenerate ตาม — รวม fix "Ver/Val" จากข้อ 1 เข้า PDF ด้วย)
3. **อัปเดต `repository/CONTENT_COVERAGE_MATRIX.md`** — เพิ่ม **Section 7: Ver.2 (field-guide) — Knowledge Area → Chapter Mapping**: ตาราง 20 แถว map ทุก KA เดิม (Integration 4 ท่อน, Stakeholder, Scope, Schedule, Cost 2 ท่อน, Resource 2 ท่อน, Quality 3 ท่อน, Comms, Risk, Procurement, Agile ×2) → chapter ใหม่ใน `field-guide/chapters/` พร้อม source lesson เดิม อ้างอิงตารางใน `Ver.2/master_plan.md` §3 + คำเตือน KA ที่ถูกผ่า (Quality 3 ท่อน / Integration 3 ท่อน) ตามเดิม
4. **เตรียม Phase 6 Proposal (ข้อเสนอเท่านั้น — ไม่ลงมือ):** ดูรายละเอียดเต็มในหัวข้อ "## ข้อเสนอ Phase 6 — Archive e-Book/ (Proposal เท่านั้น)" ด้านล่าง

**Output/ไฟล์ที่สร้างหรือแก้:**
- `field-guide/chapters/ch-05/ch-05-learner.md` (Quick Ref fix)
- `field-guide/pdf/build_pdf.py` (cover + TOC แยก edition)
- `field-guide/pdf/PM-Delivery-Guide-Complete-Edition.pdf` + `field-guide/pdf/PM-Delivery-Guide-Learner-Edition.pdf` (rebuild)
- `field-guide/pdf/book.html` + `field-guide/pdf/book-learner.html` (regenerate)
- `repository/CONTENT_COVERAGE_MATRIX.md` (Section 7 ใหม่)
- `Ver.2/FreeBuff_Fixed_Update.md` (ไฟล์นี้)

**การตัดสินใจที่ทำเอง:**
- ใช้คำย่อ "Ver/Val" ตามที่เจ้าของแนะนำ (Ver = ตาม spec / Val = ตาม need) และเขียนคำเต็มกำกับไว้ในบรรทัดด้วย
- Coverage Matrix: เก็บตารางเดิม (audit 2026-07-22) ไว้ครบ เพิ่ม Section 7 ต่อท้าย ไม่แก้การประเมินเดิม

**ติดตรงไหน / ยังไม่แน่ใจ:**
- ไม่มี — รอ Claude ตรวจซ้ำรอบสั้นๆ

**พร้อมให้ review: ใช่**

---

## ข้อเสนอ Phase 6 — Archive `e-Book/` (Proposal เท่านั้น — ห้ามลงมือจนกว่า approve)

> **สถานะ: ข้อเสนอสำหรับเจ้าของ repo / Claude review — ยังไม่ได้ลงมือทำอะไรกับ `e-Book/` (0 diff กับ HEAD)**

### 1) ปลายทางที่เสนอ: `repository/archive/e-Book/`

- ย้ายทั้งโฟลเดอร์ `e-Book/` ไปที่ `repository/archive/e-Book/` (pattern มีอยู่แล้ว: `repository/archive/` มี `README.md` + `REPOSITORY_AUDIT_REPORT.md`)
- ทำด้วย `git mv` เพื่อเก็บ history + ให้ diff ชัดเจน

### 2) ไฟล์นอก `e-Book/` ที่ลิงก์ไปหา e-Book — จะพังถ้าย้าย (ต้องแก้พร้อม archive)

ลิงก์ markdown จริง (จะ broken ถ้าไม่แก้):
- `README.md:88` — 2 ลิงก์: [`e-Book/README.md`](e-Book/README.md), [`e-Book/release/RELEASE-MANIFEST.md`](e-Book/release/RELEASE-MANIFEST.md) → ต้องชี้ไป `repository/archive/e-Book/...` และปรับข้อความว่า "archived — replaced by field-guide"
- `field-guide/BOOK-BLUEPRINT.md:29` — ลิงก์ `../e-Book/pdf/build_pdf.py` (อ้างอิงต้นแบบ pipeline) → ต้องชี้ไป `../repository/archive/e-Book/pdf/build_pdf.py`
- `field-guide/BOOK-BLUEPRINT.md:92` — ลิงก์ `../e-Book/chapters/lesson-01/lesson-01-learner.md` (อ้างอิงโทน) → ต้องชี้ไป `../repository/archive/e-Book/chapters/lesson-01/lesson-01-learner.md`

ไฟล์ที่**พูดถึง** `e-Book/` ในข้อความ (ไม่ใช่ลิงก์ — ไม่พัง แต่ควร update wording หลัง archive):
- `governance/CONTENT-RULES.md`, `repository/PMBOK-EDITION-POSITION.md`, `repository/REPOSITORY_DECISION_LOG.md`, `Ver.2/*`, `field-guide/chapters/*` (หลายไฟล์), `field-guide/pdf/build_pdf.py` (comment อ้างอิงต้นแบบ) — ปรับเป็น "archived" หรือเพิ่ม note

### 3) Checklist / หลักฐานที่ต้องเก็บไว้ก่อน archive

ก่อนย้ายต้องยืนยันครบทุกข้อ:
- [ ] `field-guide/pdf/` build ผ่านจริง 2 ฉบับ (Complete + Learner) — ขนาด/หน้า ตรวจแล้ว
- [ ] Coverage ครบเทียบเท่า e-Book เดิม: `repository/CONTENT_COVERAGE_MATRIX.md` Section 7 mapping ครบทุก KA
- [ ] เก็บ artifact เดิมไว้ใน archive ด้วย: PDF เดิม (`e-Book/pdf/PMBOK-Masterclass-Complete-Edition.pdf`), `e-Book/release/RELEASE-MANIFEST.md`, capstone, lessons 01–16 ทั้งหมด — เก็บแบบอ่านได้ ไม่ใช่ลบทิ้ง
- [ ] บันทึก commit hash ใหม่ของเล่ม Ver.2 (6c729c7 + รอบแก้ 8) ลง archive README เพื่อ traceability
- [ ] แก้ลิงก์ 3 จุด (ข้อ 2) + run link checker อีกครั้งทั้ง repo
- [ ] เพิ่ม Decision Log แถวใหม่ใน `repository/REPOSITORY_DECISION_LOG.md` (หลัง #16) บันทึกการ archive
- [ ] ขอ approve เป็นลายลักษณ์อักษรจากเจ้าของ repo ก่อน `git mv` ครั้งเดียว

### 4) เงื่อนไข

- ยังไม่ลงมือย้าย/ลบไฟล์ใดๆ ใน `e-Book/` จนกว่าจะได้รับ approve เป็นลายลักษณ์อักษรจากเจ้าของ repo — หลัง approve แล้วให้ทำเป็น commit แยก 1 ครั้ง (ไม่ push)

---

## 2026-08-14 — Round 7 (แก้ตาม Claude Review — Decision Log #13→#16 + Commit งานทั้งหมด)

**ทำอะไรไปแล้ว:**
- **แก้ Decision Log ซ้ำ:** `repository/REPOSITORY_DECISION_LOG.md` มีแถว #13 ซ้ำ 2 แถว — แก้ตาม feedback โดยเปลี่ยนแถวที่ผมเพิ่ม (2026-08-13, สรุปการ execute) จาก #13 → **#16** และย้ายไปต่อท้ายแถว #15 แล้ว; แถวเดิม (2026-07-31, กลับคำตัดสินใจรวมเล่ม) คงเป็น #13 ตามเดิม — ตรวจแล้วเลขเรียง 1–16 ครบ ไม่ซ้ำ
- **Commit งานทั้งหมดบน branch `Ver.2`** (ไม่ push remote): `6c729c7` — "Complete PM Delivery Guide Ver.2: merge e-Book + field-guide into one book" — **50 ไฟล์, +9,243 บรรทัด** (33 ไฟล์บท + 5 appendix + PDF 2 ฉบับ + build_pdf.py + HTML 2 + governance 4 + blueprint + logs 2)
- ตรวจหลัง commit: working tree สะอาด, `e-Book/` ยัง untouched (0 diff กับ HEAD)

**Output/ไฟล์ที่สร้างหรือแก้:**
- `repository/REPOSITORY_DECISION_LOG.md` (#16 ย้ายท้าย, #13 เดิมคงที่)
- Commit `6c729c7` บน branch `Ver.2` (local)

**การตัดสินใจที่ทำเอง:**
- ใช้วิธี commit ผ่านไฟล์ข้อความชั่วคราว (heredoc ตีความ emoji ผิดใน bash) — ข้อความ commit ปกติตาม convention ของ repo, ไม่มีผลต่อเนื้อหา

**ติดตรงไหน / ยังไม่แน่ใจ:**
- ไม่มี — รอ Claude ตรวจซ้ำสั้นๆ ตามที่แจ้งไว้

**พร้อมให้ review: ใช่**

## 2026-08-14 — Round 6 (Phase 3 + 4 — Appendices ครบ + รวมเล่มตรวจ cross-reference)

**ทำอะไรไปแล้ว:**
- **Phase 3 (Appendices):** เขียนครบ A, B, C, D, F — รวมกับ E ที่มีอยู่แล้ว = ครบ 6 ตัว:
  - A — Artifact Catalogue (ตาราง lookup: Artifact → บท → ใช้ทำอะไร)
  - B — Golden Rules Poster (20 ข้อ + map ไปบท)
  - C — PM Glossary ฉบับเล่ม (ต่อจาก glossary กลาง ไม่สร้างคำซ้ำ)
  - D — Master Answer Key รวมทุกบท (index + rubric กลาง + แนวตอบย่อรายข้อ)
  - F — Problem → Chapter Index (ตาราง "เปิดเมื่อมีปัญหา" 32 รายการ + ดัชนีย้อนกลับ)
- **Phase 4 (รวมเล่ม):** ตรวจลิงก์ relative ทั้งเล่มด้วยสคริปต์ — 40 ไฟล์, **ALL LINKS OK** (ทั้ง `references/` และ `repository/` มี Playbook V2 อยู่จริง)
- **Cross-reference ของ KA ที่ถูกผ่า ตรวจแล้วครบทั้ง 2 จุด:**
  - Quality: Ch.5 (Test Strategy/Quality Plan) ↔ Ch.6 (QA ฝั่งกระบวนการ) ↔ Ch.8 (ผลจริง/QC/UAT) — มีกล่อง cross-reference ชัดทั้ง Ch.5 และ Ch.8
  - Integration: Charter = Ch.2 / Change Control = Ch.7 / Closure = Ch.10 — ครบ 3 ท่อน พร้อม note ท้ายบท

**Output/ไฟล์ที่สร้าง:** 5 ไฟล์ appendix ใหม่ + บันทึกตรวจลิงก์

**ติดตรงไหน:** ไม่มี — ไป Phase 5 (PDF)

## 2026-08-14 — งานเสร็จทั้งเล่ม พร้อมให้ Claude review

**สรุปทุก Phase ที่ทำ (0–5):**
- **Phase 0 — Lock:** ชื่อเล่ม "PM Delivery Guide (Ver.2)", Scenario decision ล็อก (vendor layer "Booking Tech Solutions" เฉพาะ Ch.1–2, `[Teaching Scenario Extension]`, กลับมา SHG ภายในตั้งแต่ Ch.3), เพิ่ม `[PMBOK 8]` ใน CONTENT-RULES §2/§7, อัปเดต PMBOK-EDITION-POSITION + Decision Log #13, sync คำศัพท์ใหม่เข้า PM_GLOSSARY, แก้ Context ใน BOOK-BLUEPRINT.md
- **Phase 1 — Pilot:** Ch.1 (Pre-sales) ครบ Template 15 หัวข้อ × 3 ไฟล์
- **Phase 2 — Batch:** Ch.2–10 + Ch.0 = 11 บท × 3 ไฟล์ (learner/instructor/answer-key) = 33 ไฟล์ — ทุกบทเทียบ content จาก lesson เดิมตาม mapping (lesson-05..16)
- **Phase 3 — Appendices:** A, B, C, D, F เขียนใหม่ + E เดิม = ครบ 6 ตัว
- **Phase 4 — รวมเล่ม:** ลิงก์ relative ทั้งเล่มผ่าน (40 ไฟล์ ALL LINKS OK), cross-reference Quality (Ch.5/6/8) และ Integration (Ch.2/7/10) ครบชัด
- **Phase 5 — Export PDF:** เขียน `field-guide/pdf/build_pdf.py` (ต่อยอดจาก e-Book ต้นแบบ แปลง markdown โดยตรง รันผ่าน Chrome headless) → สร้าง PDF สำเร็จ 2 ฉบับ:
  - `PM-Delivery-Guide-Complete-Edition.pdf` (201 หน้า, ~2.8 MB) — Learner + Instructor + Answer Key + Appendices
  - `PM-Delivery-Guide-Learner-Edition.pdf` (137 หน้า, ~2.1 MB) — เฉพาะ Learner + Appendices

**Definition of Done (master_plan.md §8) — self-check:**
- ✅ 11 บท (Ch.0–10) ครบ Template 15 หัวข้อ
- ✅ KA mapping ครอบคลุมทุก Knowledge Area ตามตาราง (Integration/Scope/Schedule/Cost/Resource/Risk/Procurement/Comms/Quality ผ่าลงบทตามเวลางานจริง)
- ✅ Source label ถูกต้อง (`[PMBOK 8]` หลัก + `[Teaching Scenario]`/`[Teaching Scenario Extension]`/`[Best Practice]`)
- ✅ Scenario ตรง Scenario Master v1.0 (ตัวเลข 12M/35%/18 เดือน/NPS 40/Sprint 0–12 ตรงทั้งหมด)
- ✅ Relative links ทั้งเล่มผ่าน
- ✅ Appendix ครบ 6 ตัว (A–F)
- ✅ PDF Learner + Instructor edition build ผ่านจริง
- ⚠️ ยังไม่ได้: Claude review + เจ้าของ repo approve (จุดนี้คือตอนนี้)

**ข้อเสนอสำหรับ Phase 6 (archive e-Book/):** ยังไม่แตะ `e-Book/` ใดๆ — ข้อเสนอ: เมื่อ review ผ่านและ approve เป็นลายลักษณ์อักษรแล้ว ค่อยประเมิน archive `e-Book/` ไปยัง `repository/archive/` (ตาม pattern เดิม) โดยเก็บ Decision Log เป็นหลักฐานการ migrate

**พร้อมให้ review: ใช่**

## 2026-08-13 — Round 4 (Phase 2 — ทั้ง 11 บทเสร็จ Ch.0–10)

**ทำอะไรไปแล้ว:**
- เขียนครบ 11 บท × 3 ไฟล์ (learner/instructor/answer-key) = 33 ไฟล์ ใน `field-guide/chapters/ch-00/` … `ch-10/`:
  - Ch.0 PMBOK Primer (ปฐมบท ไม่มี Workshop/Assessment ตาม master_plan §5)
  - Ch.1 Pre-sales (A) — Pilot (Phase 1)
  - Ch.2 Initiation (B) — Charter + Stakeholder เต็มบท
  - Ch.3 Requirements/Scope/WBS (C1–C6)
  - Ch.4 Schedule/Cost/Resource (C8–C13) + Agile insert
  - Ch.5 Risk/Procurement/Comms/Env (C7 + C14–C19) + Quality Plan
  - Ch.6 Execution (D) + Manage Quality/Team + Agile insert
  - Ch.7 Monitoring & Change (E) — Perform Integrated Change Control
  - Ch.8 Verification/UAT (F) — QC ฝั่งผลจริง
  - Ch.9 Go-Live & Hypercare (G) — เนื้อหาใหม่ทั้งหมด
  - Ch.10 Transition & Closure (H) — Close Project or Phase
- ทุกบทใช้ Template 15 หัวข้อ + frontmatter + source labels + scenario อ้างอิง Scenario Master v1.0

**การตัดสินใจ/ข้อตีความที่ทำเอง (บันทึกไว้เพื่อ Claude ตรวจ):**
1. **Ch.3 ครอบคลุม C1–C6** และ **C7 (Plan Quality/Acceptance — Test Strategy) ถูกวางไว้ใน Ch.5** ตามคำเตือน Quality ใน master_plan §3 ("วางแผน Test/Quality → Ch.5, ผลจริง → Ch.8") — ชื่อบท "C1–C7" ในแผนคือช่วง planning ทั้งหมด; เขียน cross-reference ชัดทั้ง Ch.3/Ch.5/Ch.8
2. **Integration ครบ 3 ท่อน** เขียน cross-ref ชัด: Charter = Ch.2, Change Control = Ch.7, Closure = Ch.10
3. **Scenario:** vendor layer (Booking Tech Solutions) ใช้เฉพาะ Ch.1–2 จบที่ Kickoff — ตั้งแต่ Ch.3 ใช้ทีม SHG ภายในตาม Scenario Master (คุณสุทธิ PM, คุณนภา PO) — ตัวเลขทั้งหมด (12M, 35%, 18 เดือน, NPS 40, Sprint 0–12, soft launch 3 โรงแรม) ตรง Scenario Master
4. **Ch.0 ตัวเลข 6 Principles / 7 Domains / 5 Focus Areas** นำมาจาก BOOK-BLUEPRINT.md/master_plan §3 ตามที่เจ้าของระบุ — เขียนเป็น "กรอบที่เล่มนี้ใช้" + หมายเหตุอ้าง reference basis เพื่อไม่ให้อ้างเกิน source
5. **EVM ตัวอย่าง** (Ch.4: PV6/EV5/AC6.5 → SPI 0.83 CPI 0.77 EAC≈15.6M; Ch.7: PV7.5/EV6.75/AC7.5 → SPI/CPI 0.90 EAC≈13.3M VAC≈-1.3M) เป็น Teaching Scenario ที่ไม่ขัด budget context 12M ของ Scenario Master

**Output/ไฟล์ที่สร้าง:** 33 ไฟล์บท + governance/glossary ที่แก้ใน Phase 0

**ติดตรงไหน:** ไม่มี — ไป Phase 3 (Appendices) ต่อ

## 2026-08-13 — Round 2 (Phase 1 — Pilot Ch.1 เสร็จ)

**ทำอะไรไปแล้ว:**
- เขียน Ch.1 (Pre-sales / Playbook A) ครบ Template 15 หัวข้อ ครบ 3 ไฟล์:
  - `field-guide/chapters/ch-01/ch-01-learner.md` — 15 หัวข้อครบ + frontmatter + source labels
  - `field-guide/chapters/ch-01/ch-01-instructor.md` — teaching notes, timing, thinking walkthrough, scenario note
  - `field-guide/chapters/ch-01/ch-01-answer-key.md` — model answers + rubric สำหรับ 7 ข้อ assessment
- เนื้อหาถ่ายจาก Playbook V2 §A (A1–A12) + lesson-05 บางส่วน (Business Case/Value) + lesson-02 (Output/Outcome/Benefit)
- Scenario: ใช้ vendor layer "Booking Tech Solutions" ตาม default ที่ล็อกใน Round 1 — ตัวเลข SHG ทั้งหมดตรง Scenario Master (12M, 35%, 18 เดือน, NPS 40, 12 โรงแรม, PMS API ไม่ครบ = Risk #1)

**Output/ไฟล์ที่สร้าง:** 3 ไฟล์ใน `field-guide/chapters/ch-01/`

**การตัดสินใจที่ทำเอง:** ราคา Proposal ตัวอย่าง (Fixed 6.5M dev+QA + T&M cap 0.5M สำหรับ PMS adapter) เป็น Teaching Scenario Extension ที่จัดสรรให้รวมแล้วไม่เกินกรอบ 12M ของ SHG — ไม่ขัดกับ budget context ใน Scenario Master

**ติดตรงไหน:** ไม่มี — ไป Phase 2a (Ch.2–4) ต่อ

## 2026-08-13 — Round 1 (Phase 0 — Lock)

**ทำอะไรไปแล้ว:**
- สร้าง branch ใหม่ `Ver.2` จาก `main` (local เท่านั้น ไม่ push remote) — ยืนยัน `git branch --show-current` = `Ver.2`
- ล็อกชื่อเล่ม: **"PM Delivery Guide: From Pre-sales to Closure — คู่มือปฏิบัติการบริหารโครงการซอฟต์แวร์ (PMBOK 8th Edition)"** (aka "ebook v2" / "Ver.2") — ใช้ตัวเลือก B/C ของ Blueprint ผสมกัน: ชื่อภาษาไทยสื่อว่าเป็นคู่มือภาคปฏิบัติ ตาม workflow A–H
- ล็อก Scenario decision ด้วย default จาก master_plan §4: **เพิ่ม vendor สมมติ "Booking Tech Solutions" เฉพาะ Ch.1–2** ด้วย label `[Teaching Scenario Extension]` จากมุม vendor แล้ว Ch.3 เป็นต้นไปกลับมาใช้ทีม SHG ภายในตาม `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` — ห้ามแก้ตัวเลข/roles ที่ล็อกไว้ใน scenario master
- อัปเดต governance ครบ 4 จุด:
  - `governance/CONTENT-RULES.md` §2 + §7: เพิ่ม label `[PMBOK 8]` และ `[Teaching Scenario Extension]` (ไม่ลบ label เดิม)
  - `repository/PMBOK-EDITION-POSITION.md`: เพิ่ม §8 อธิบาย PMBOK 8 migration ผ่าน field-guide
  - `repository/REPOSITORY_DECISION_LOG.md`: เพิ่ม Decision Log #13 กลับคำตัดสินใจ "แยกเล่ม" → "รวมเป็นเล่มเดียว"
  - `governance/PM_GLOSSARY.md`: เพิ่มส่วน Ver.2 additions (29 คำ: ROM, SOW, Cutover, Hypercare, Rollback, Go/No-Go, UAT, SIT, RAID, Make-or-Buy, T&M, Fixed Price, PIR, MVP, CCB, Governance, Issue, Impact Analysis, Workstream, Vendor, RTM, Definition of Done/Ready, Release Readiness, Residual Risk, Stabilization, Test Strategy, Bid/No-Bid, Business Case, Opportunity, Proposal, Discovery, WBS Dictionary)
- ปรับ Context section ของ `field-guide/BOOK-BLUEPRINT.md` ให้ตรงกับแผนรวมเล่ม (Decision #13)

**Output/ไฟล์ที่สร้างหรือแก้:**
- `governance/CONTENT-RULES.md`, `repository/PMBOK-EDITION-POSITION.md`, `repository/REPOSITORY_DECISION_LOG.md`, `governance/PM_GLOSSARY.md`, `field-guide/BOOK-BLUEPRINT.md`
- สร้างโฟลเดอร์ `field-guide/chapters/ch-00/` … `ch-10/`

**การตัดสินใจที่ทำเอง:**
- ชื่อเล่ม + Scenario default (ตามที่ master_plan อนุญาตให้ใช้ default ได้โดยไม่ต้องรอ)

**ติดตรงไหน / ยังไม่แน่ใจ:**
- ยังไม่มี — อ่าน source ครบแล้ว (governance, scenario, Playbook V2, lessons 01–16, build_pdf.py)

**คำถามถึง Claude (ไม่ต้องรอคำตอบ บันทึกไว้ก่อนแล้วไปต่อ):**
- ไม่มี — เริ่ม Phase 1 (Pilot Ch.1) ต่อทันที

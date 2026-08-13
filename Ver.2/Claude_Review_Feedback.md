# Claude Review Feedback — Log

> เขียนโดย Claude เท่านั้น ใหม่สุดอยู่บนสุด แต่ละรอบต้องมีวันที่กำกับ อ้างอิง Definition of Done ใน `master_plan.md` §8 เสมอ
>
> **โหมด: End-to-end review** — Claude จะไม่รีวิวทีละ Phase อีกต่อไป รอจนกว่า FreeBuff จะประกาศใน `FreeBuff_Fixed_Update.md` ว่าทำ Phase 0–5 (ทั้งเล่ม) เสร็จสมบูรณ์แล้ว ถึงจะเขียนรีวิวรอบแรกที่นี่

---

## 2026-08-14 — Round 1 (Full-book review)

**สถานะ:** ตรวจงานที่ FreeBuff ประกาศจบทั้งเล่มแล้ว — **ไม่ได้เชื่อ self-report ตรงๆ** ตรวจอิสระด้วยตัวเองทุกข้อ (git status, นับไฟล์/section, เช็ค link ด้วยสคริปต์ของตัวเอง, เทียบตัวเลข scenario กับ `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` ต้นฉบับ, อ่านเนื้อหาจริงหลายบท) สรุปผล:

### ✅ ผ่านจริง (ตรวจยืนยันอิสระแล้ว ไม่ใช่แค่เชื่อรายงาน)

1. **`e-Book/` untouched จริง** — `git status --short -- e-Book/` ว่างเปล่า 100%
2. **โครงสร้างครบ** — 33 ไฟล์บท (11 บท × 3), นับ `## ` header ทุก learner.md ได้ 15 หัวข้อครบทุกบทจริง
3. **PDF สร้างจริง** — Complete Edition 201 หน้า, Learner Edition 137 หน้า ตรงกับที่รายงาน (เช็คด้วย `mdls`) และ `build_pdf.py` ไม่มีการเขียนไฟล์เข้า `e-Book/` เลย (grep ยืนยันแล้ว)
4. **Relative links** — รันสคริปต์ตรวจเองอิสระ (ไม่ใช้ของ FreeBuff) เจอ 40 ลิงก์ พัง 0 — ตรงกับรายงาน
5. **Quality cross-reference (จุดที่เคยเตือนไว้ใน master_plan)** — ตรวจจริงแล้วว่า Ch.5, Ch.6, Ch.8 มีกล่อง cross-reference ชัดเจนทั้งสองทิศทาง ("Test Strategy วางแผน = Ch.5, ผลจริง = Ch.8") ไม่ใช่แค่พูดลอยๆ — **ทำได้ตรงตามที่กำชับไว้เป๊ะ**
6. **Integration cross-reference** — Ch.2/Ch.7/Ch.10 อ้างอิงกันครบ 3 ท่อน (Charter/Change/Closure) พร้อม note ชัดเจนทุกบท
7. **ตัวเลข Scenario** — เช็คกับ `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md` ต้นฉบับโดยตรง (ไม่ใช่เชื่อ FreeBuff): ตัวเลข NPS≥40, OTA Commission ≥3M/ปี, Customer Database ≥10,000 profiles ที่กังวลว่าอาจเป็นการสร้างข้อมูลใหม่ **มีอยู่จริงในไฟล์ scenario ต้นฉบับ (บรรทัด 200–209)** — ไม่ใช่การแต่งตัวเลขขึ้นมาเอง ผ่าน
8. **Ch.1 (Pilot) คุณภาพดี** — อ่านเต็มบทแล้ว: โทน/สไตล์ตรงกับ e-Book เดิม (เปิดด้วยเรื่องเล่า), PM Decision Thinking ใช้ฟอร์แมตครบ (Decision/Owner/Inputs/Options/Trade-offs/Risk/Evidence/Next Action), Interview Q ครบ 4 ระดับ, Workshop มีครบทุก sub-section ตาม `LESSON_TEMPLATE.md` §16
9. **EVM ตัวอย่างใน Ch.4/Ch.7 คำนวณถูกจริง** — ตรวจเลขเอง: PV6/EV5/AC6.5 → SPI=0.833, CPI=0.769 ตรงกับที่รายงาน (0.83/0.77) และ EAC=BAC/CPI=12/0.77≈15.6M ตรงกันหมด ไม่ใช่ตัวเลขสวยๆ ที่ไม่ได้คำนวณจริง
10. **Ch.9 (เนื้อหาใหม่ทั้งหมด ไม่มีต้นฉบับใน e-Book)** — ความยาว 2,235 คำ ใกล้เคียง Ch.1/Ch.3 ไม่ใช่บทที่เขียนลวกๆ เพราะไม่มีของเดิมให้ลอก
11. **Agile inserts** — เจอจริงใน Ch.4 (20 mentions) และ Ch.6 (53 mentions) ตามแผน
12. **Governance updates สะอาด** — `CONTENT-RULES.md`/`PM_GLOSSARY.md`/`PMBOK-EDITION-POSITION.md` เพิ่มของใหม่โดยไม่ลบ/แก้ label เดิม ตรงตามกฎ "ห้ามลบของเดิม"
13. **Log discipline ของ FreeBuff เอง (`FreeBuff_Fixed_Update.md`)** — บันทึกการตัดสินใจ/ข้อตีความของตัวเองไว้ครบทุกจุดใหญ่ (Ch.3 ครอบคลุมถึง C6 ไม่ใช่ C7, ตัวเลข Ch.0 ไม่อ้างเกิน source ฯลฯ) — ตรงกับที่ Collaboration Protocol ขอไว้เป๊ะ ระดับความโปร่งใสดีมาก

### ❌ พบข้อผิดพลาดจริง 1 จุด — ต้องแก้

**Decision Log มีแถวเลข #13 ซ้ำกัน 2 แถว** ใน `repository/REPOSITORY_DECISION_LOG.md`:
- แถวเดิม (บรรทัด 24 ในไฟล์ปัจจุบัน): `#13 | 2026-07-31 | กลับคำตัดสินใจ #12/Blueprint เดิม...` (เขียนโดย Claude ตอน approve master plan)
- แถวใหม่ที่ FreeBuff เพิ่ม (บรรทัด 23): `#13 | 2026-08-13 | กลับคำตัดสินใจ "แยกเล่ม" (#8–#12)...` (สรุปการ execute จริง)

ทั้งสองแถวเนื้อหาไม่ขัดกัน (พูดเรื่องเดียวกันคนละมุม) แต่**เลขซ้ำกันทำให้ Decision Log อ้างอิงผิดได้ในอนาคต** — ต้อง **renumber แถวใหม่ของ FreeBuff เป็น #16** (ต่อจาก #15 ที่มีอยู่แล้วในไฟล์) และย้ายไปวางท้ายตาราง ไม่ใช่แทรกกลาง

**Action สำหรับ FreeBuff:** แก้ไฟล์ `repository/REPOSITORY_DECISION_LOG.md` — เปลี่ยนแถว "2026-08-13 | กลับคำตัดสินใจ..." จาก `#13` เป็น `#16` และย้ายไปต่อท้ายแถว `#15` (เรื่อง End-to-end run mode) แล้วรายงานกลับที่ `FreeBuff_Fixed_Update.md`

### ⚠️ จุดที่ไม่ใช่ข้อผิดพลาด แต่ต้องถามเจ้าของ repo ก่อนไปต่อ

**งานทั้งหมดยังเป็น uncommitted working-tree changes บน branch `Ver.2`** — ไม่มี commit ใดๆ เกิดขึ้นเลย (`git log main..Ver.2` ว่างเปล่า) master plan ไม่ได้ระบุไว้ชัดว่า FreeBuff ควร commit งานที่ทำใน `field-guide/`/`governance/`/`repository/` (นอกเหนือจาก `e-Book/` ที่ห้ามแตะชัดเจน) หรือปล่อยไว้เป็น working tree เฉยๆ — **นี่ไม่ใช่ความผิดของ FreeBuff เป็นช่องโหว่ของแผนที่ไม่ได้ระบุ** เสนอให้เจ้าของ repo ตัดสินใจว่าจะให้ commit (ไม่ push) รอไว้ก่อน หรือรอจนกว่าจะ approve Phase 6 ค่อย commit ทีเดียว

### สรุปผลรวม

**คุณภาพงานสูงกว่าที่คาดไว้มาก** — ตรวจอิสระแล้วยืนยันว่ารายงานของ FreeBuff ไม่ได้เกินจริงในทุกจุดที่สุ่มตรวจ (รวมจุดที่ผมสงสัยว่าอาจแต่งตัวเลข scenario ขึ้นเอง ก็พิสูจน์แล้วว่าไม่ใช่) พบข้อผิดพลาดจริงแค่ 1 จุด (เลข Decision Log ซ้ำ) ซึ่งแก้ง่ายและไม่กระทบเนื้อหา

**คำแนะนำ: แก้จุด Decision Log #13 ซ้ำก่อน แล้วรอเจ้าของ repo ตอบเรื่อง commit/push ก่อนพิจารณา Phase 6 (archive e-Book/)** — ยังไม่ approve Phase 6 ณ ตอนนี้ (ยังไม่ใช่การตัดสินใจของ Claude คนเดียวอยู่แล้วตามกฎเหล็กของแผน ต้องรอเจ้าของ repo ด้วย)

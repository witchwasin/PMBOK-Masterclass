# PMBOK Masterclass E-book

เล่มรวมของหลักสูตร **PMBOK Masterclass** (อิง PMBOK 6 + 7) — 16 บทเรียนเรียงตาม 10 Knowledge Areas พร้อม Capstone

ผู้เรียบเรียง: **Witchwasin K.**

> ถ้าต้องการเล่มที่เรียงตามลำดับงานจริง A→H และอิง PMBOK 8 ดูที่ [`../field-guide/`](../field-guide) แทน

## เริ่มอ่าน

| ต้องการ | ไปที่ |
|---|---|
| อ่านรวดเดียวจบ (PDF) | [`pdf/PMBOK-Masterclass-Complete-Edition.pdf`](pdf/PMBOK-Masterclass-Complete-Edition.pdf) — Learner + Instructor |
| อ่านบนเบราว์เซอร์ | [`release/PMBOK-Masterclass-Learner.html`](release/PMBOK-Masterclass-Learner.html) |
| อ่านเป็น Markdown ทีละบท | [`chapters/`](chapters) |
| ฉบับผู้สอน | [`release/PMBOK-Masterclass-Instructor-Companion.md`](release/PMBOK-Masterclass-Instructor-Companion.md) |

## โครงสร้าง

```text
e-Book/
├── chapters/              # lesson-01 … lesson-16 (learner / instructor / answer-key)
├── integration-reviews/   # บททบทวนเชื่อมโยงทุก 4 บท
├── capstone/              # โจทย์รวบยอด (learner / instructor)
├── pdf/                   # เล่ม PDF + build script
└── release/               # ไฟล์พร้อมอ่าน/แจก — ดู RELEASE-MANIFEST.md
```

แต่ละบทมี 3 ไฟล์: `-learner` (เนื้อหาสำหรับผู้เรียน), `-instructor` (โน้ตสำหรับผู้สอน), `-answer-key` (เฉลยและเกณฑ์ประเมิน)

## การสร้าง PDF ใหม่

```bash
python3 e-Book/pdf/build_pdf.py
```

สคริปต์จะประกอบบททั้งหมดเป็น `book.html` แล้วเรนเดอร์เป็น PDF ด้วย Chrome headless — `book.html` เป็นไฟล์ระหว่างทาง ไม่ถูก commit

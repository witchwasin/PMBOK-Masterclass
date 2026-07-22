# PMBOK Masterclass E-book

เอกสารในโฟลเดอร์นี้คือพื้นที่ผลิต E-book จาก source ใน repository เดียวกัน โดยใช้แนวทาง **PMBOK-aligned Practical Masterclass** และควบคุมด้วย editorial gates ก่อนเขียนเนื้อหาแต่ละบท

ผู้เรียบเรียง: **Witchwasin K.**

## Production Principle

สร้างระบบควบคุมก่อน ผลิตทีละบท ตรวจทีละบท และรวมเล่มเมื่อทุกบทผ่าน validation เท่านั้น

## Directory Structure

```text
e-Book/
├── README.md
├── chapters/
├── integration-reviews/
├── capstone/
├── pdf/
└── release/
```

Internal production-tracking files (editorial control package, per-chapter source maps, traceability matrices and validation reports) were used to build and QA each chapter and have been cleared after release packaging; they are not part of the shipped learner/instructor content.

## Production Phases

1. Phase 1: Build and freeze editorial control package
2. Phase 2: Produce one lesson chapter per execution
3. Phase 3: Review integration every four chapters
4. Phase 4: Produce capstone
5. Phase 5: Compile learner and instructor editions into the release package

## Current Gate

Learner e-book content, instructor companion, capstone and release packaging are complete. A combined Learner + Instructor book-style PDF is produced by `pdf/build_pdf.py` (weasyprint if available, Chrome headless otherwise) and stored at `pdf/PMBOK-Masterclass-Complete-Edition.pdf`. EPUB export still depends on local conversion tooling availability.

## Release Package

ไฟล์พร้อมส่งมอบอยู่ที่:

```text
e-Book/release/PMBOK-Masterclass-eBook-release.zip
```

โฟลเดอร์ `release/` เก็บเฉพาะไฟล์ที่ต้องใช้สำหรับการอ่าน/ตรวจ release โดยตัดไฟล์ขยะ เช่น `.DS_Store` และไฟล์ assembly ที่ไม่จำเป็นกับ zip ออกแล้ว

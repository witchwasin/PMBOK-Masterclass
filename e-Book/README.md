# PMBOK Masterclass E-book

เอกสารในโฟลเดอร์นี้คือพื้นที่ผลิต E-book จาก source ใน repository เดียวกัน โดยใช้แนวทาง **PMBOK-aligned Practical Masterclass** และควบคุมด้วย editorial gates ก่อนเขียนเนื้อหาแต่ละบท

ผู้เรียบเรียง: **Witchwasin K.**

## Production Principle

สร้างระบบควบคุมก่อน ผลิตทีละบท ตรวจทีละบท และรวมเล่มเมื่อทุกบทผ่าน validation เท่านั้น

## Directory Structure

```text
e-Book/
├── README.md
├── editorial/
│   ├── EBOOK-SOURCE-READINESS-REPORT.md
│   ├── EBOOK-SOURCE-MANIFEST.md
│   ├── EBOOK-STYLE-GUIDE.md
│   ├── EBOOK-CHAPTER-CONTRACT.md
│   ├── EBOOK-CONTENT-MAP.md
│   ├── EBOOK-SCENARIO-FACT-REGISTER.md
│   ├── EBOOK-TERMINOLOGY-REGISTER.md
│   ├── EBOOK-TRACEABILITY-MATRIX.md
│   ├── EBOOK-PRODUCTION-STATUS.md
│   └── EBOOK-CONTROL-PACKAGE-VALIDATION.md
├── chapters/
├── integration-reviews/
├── capstone/
├── final/
└── release/
```

## Production Phases

1. Phase 1: Build and freeze editorial control package
2. Phase 2: Produce one lesson chapter per execution
3. Phase 3: Review integration every four chapters
4. Phase 4: Produce capstone
5. Phase 5: Compile final learner and instructor editions

## Current Gate

Learner e-book content, instructor companion, capstone and final editorial review are ready for release packaging. PDF/EPUB export depends on local conversion tooling availability.

## Release Package

ไฟล์พร้อมส่งมอบอยู่ที่:

```text
e-Book/release/PMBOK-Masterclass-eBook-release.zip
```

โฟลเดอร์ `release/` เก็บเฉพาะไฟล์ที่ต้องใช้สำหรับการอ่าน/ตรวจ release โดยตัดไฟล์ขยะ เช่น `.DS_Store` และไฟล์ assembly ที่ไม่จำเป็นกับ zip ออกแล้ว

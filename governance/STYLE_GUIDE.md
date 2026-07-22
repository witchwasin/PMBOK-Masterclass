---
title: Style Guide
document_type: Writing Style Guide
version: 1.0
---

# PMBOK Masterclass — Style Guide

---

## 1. ภาษา

- ภาษาหลัก: **ไทย** + ศัพท์ PM ภาษาอังกฤษ
- ใช้คำภาษาอังกฤษเมื่อเป็น **PM Standard Term** (Project Charter, Scope, Risk, etc.)
- อธิบายศัพท์ภาษาอังกฤษเมื่อใช้ครั้งแรกในบท: `Project Charter (เอกสารเริ่มต้นโครงการ)`
- ห้ามแปลแบบบังคับเมื่อคำอังกฤษเป็นมาตรฐาน เช่น ใช้ "Stakeholder" ไม่ต้องแปลว่า "ผู้มีส่วนได้เสีย" ทุกครั้ง

## 2. โครงสร้าง Heading

- `# H1` — ชื่อบทเรียน (1 ต่อไฟล์)
- `## H2` — Section หลัก (ตาม 21 mandatory sections)
- `### H3` — หัวข้อย่อย
- `#### H4` — ใช้เท่าที่จำเป็น ห้ามลงลึกเกิน H4

## 3. Bullet Lists

- ใช้ bullet list เมื่อรายการ ≥ 3 ข้อ
- ห้ามใช้ bullet list เป็นเนื้อหาหลักของบท — ต้องมี narrative ประกอบ
- ห้ามมี bullet list ยาวเกิน 10 ข้อโดยไม่มี heading แบ่ง

## 4. Code Blocks

- ใช้ `code block` สำหรับ Mental Model, Decision Structure, Formula
- ใช้ `text` fence สำหรับ flow diagrams
- ใช้ `yaml` fence สำหรับ metadata examples

## 5. Tables

- ใช้ table สำหรับข้อมูลเปรียบเทียบ (≥ 3 rows × ≥ 3 columns)
- ทุก table ต้องมี header row
- ห้ามใช้ table แทน paragraph explanation

## 6. Links

- **ห้ามใช้ absolute path** (`file:///Users/...`)
- ใช้ **relative path** เสมอ: `[PMBOK Overview](../../references/PMBOK-Overview.md)`
- Cross-lesson reference: `[Lesson 05](../lesson-05/Lesson-05_2-Project-Integration-Management.md)`
- Scenario reference: `[ERP Case](../../scenarios/ERP-TRANSFORMATION-CASE.md)`

## 7. Source Classification

ใช้ label ในวงเล็บเหลี่ยมก่อนย่อหน้าหรือก่อน block:

```markdown
**[PMBOK]** Project Charter คือเอกสารที่ให้สิทธิ์ PM อย่างเป็นทางการ...

**[Teaching Scenario]** ในโครงการ ERP ของ SIG คุณเอกได้รับ Charter ที่ระบุ...

**[Professional Opinion]** จากประสบการณ์ PM ที่ทำงานกับ Enterprise System...
```

## 8. สิ่งที่ห้ามทำ

- ❌ ใช้ absolute path ในลิงก์
- ❌ ใช้ bullet list เป็นเนื้อหาหลักทั้งบท
- ❌ เขียนแบบ encyclopedia (Definition → List → Example → Quiz)
- ❌ ใช้ประโยค generic AI เช่น "จะเห็นได้ว่า...", "ดังที่กล่าวมาข้างต้น..."
- ❌ ทำซ้ำเนื้อหาข้ามบท (ถ้าต้องอ้างถึง ให้ reference ไปบทเดิม)
- ❌ ใส่ emoji ใน heading ของบทเรียน (ใช้ได้ใน governance files)
- ❌ สรุปที่ท้ายบทยาวเท่าเนื้อหา
- ❌ อ้างข้อเท็จจริงโดยไม่มี Source Classification label

## 9. Voice & Tone

- เขียนเหมือนผู้สอนที่มีประสบการณ์กำลังอธิบาย
- ใช้คำถามชวนคิดเป็นระยะ
- กระชับ ตรงประเด็น ไม่อ้อมค้อม
- ใช้ "คุณ" เมื่อพูดกับผู้เรียน (ไม่ใช้ "ท่าน")
- ใช้ active voice มากกว่า passive

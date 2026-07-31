---
title: "Appendix E — SDLC Role & Output Matrix"
document_type: Field Guide Appendix
version: 1.0
status: Draft
last_updated: 2026-07-31
source: repository/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md
print_edition: field-guide/pdf/Appendix-E-SDLC-Role-Output-Matrix.pdf
---

# Appendix E — SDLC Role & Output Matrix

> สรุปบทบาทหน้าที่ตลอดกระบวนการส่งมอบโครงการ (A–H) แบ่งเป็น 2 ส่วน: (1) PM ทำ vs ทีมทำ (2) Output ที่ได้ → ใช้ทำอะไรต่อ
>
> ใช้เป็น **Field Mode lookup** — เปิดหน้านี้เมื่ออยากรู้เร็วๆ ว่า Phase ไหนใครต้องทำอะไร และงานที่ได้ออกมาต้องส่งต่อให้ใคร

| Phase | PM ทำ | ทีมทำ (ไม่ใช่ PM) | Output → ใช้ทำอะไรต่อ |
|---|---|---|---|
| **A. Pre-sales** | ประสาน Discovery, คุม Estimate, ทำ Proposal, วิเคราะห์ Impact ตอน Negotiate | Sales (รับ Opportunity, เจรจา), BA (Discovery/Root Cause), Architect (ออกแบบ Solution Options), Finance (ตั้งราคา), Legal (ทำ SOW) | Opportunity Brief, ROM Estimate, Proposal, Signed SOW → ใช้ตัดสิน Bid/No-Bid และเป็นฐานทำ Charter ใน Phase B |
| **B. Initiation** | ทำ Charter, วิเคราะห์ Stakeholder, ตั้ง Governance, เปิด RAID, จัด Kickoff | Sponsor (อนุมัติ Charter), BA (ช่วยวิเคราะห์ Stakeholder) | Project Charter, Stakeholder Register, Governance Model, RAID Log → เป็น "ใบอนุญาต" ให้เริ่มวางแผนละเอียดใน Phase C |
| **C. Detailed Planning** | เลือก Delivery Approach, รวม Plan ทุกด้านเป็น Integrated Plan, นำเสนอ Baseline Gate | BA (Requirements/SRS/FSD), Architect (Technical Design/TDD-SDD), QA (Test Strategy/Test Plan), Planner (CPM/Schedule), Finance (Cost), DevOps (Environment Plan) | WBS, **SRS/FSD (ตามเงื่อนไข), Technical Design (TDD/SDD), Test Strategy/Test Plan, RTM**, Schedule/Cost Baseline, Risk Register, Integrated PM Plan → เป็น "พิมพ์เขียว" ที่ทีมใช้ลงมือทำจริงใน Phase D และใช้วัด Variance ใน Phase E |
| **D. Execution** | Confirm งานพร้อมทำ (Definition of Ready), จัดการ Blocker, ติดตามความคืบหน้า | Delivery Team (Build ตาม Tech Spec), Tech Lead (Peer Review), QA (รัน Test ตาม Test Plan), Workstream Lead (ส่งมอบงาน) | Deliverables, Work Performance Data, Test Execution Evidence → ส่งเข้า Monitoring (E) เพื่อเทียบกับ Baseline และเตรียมเข้า UAT (F) |
| **E. Monitoring & Change** | เก็บ Actual เทียบ Baseline, วิเคราะห์ Variance, คุม Change Control | Workstream Leads (รายงานงานจริง), CCB/Sponsor (ตัดสิน Change ที่กระทบ Baseline), Customer (Validate Scope) | Variance/Forecast Report, Change Decision, Updated RAID → ทำให้ Baseline ทันสถานะจริง และเป็นหลักฐานประกอบ Go/No-Go ทีหลัง |
| **F. Verification/UAT** | ประสาน Release Readiness, สรุปเสนอ Go/No-Go | QA (Test/SIT ตาม Test Plan จาก C), Business Users (ทำ UAT จริง), Product Owner (อนุมัติด้าน Business), Sponsor (ตัดสิน Go/No-Go) | **Test Results (SIT/System Test)**, UAT Sign-off, Release Readiness Report, Go/No-Go Decision → เป็นเงื่อนไขเปิดทางเข้า Go-Live (G) |
| **G. Go-Live & Hypercare** | คุม Cutover, ตัดสินใจร่วมเรื่อง Rollback ถ้าจำเป็น | DevOps (Deploy/Migrate ข้อมูล), QA+Business (Smoke Test/ตรวจธุรกิจ), Support (Monitor/Triage หลังขึ้นระบบ) | Deployment Evidence, Hypercare Report, Stabilization Acceptance → เป็นหลักฐานว่าระบบนิ่งพอจะส่งต่อให้ Operations ใน Phase H |
| **H. Transition & Closure** | ประสานปิดโครงการ, จัด Lessons Learned | Operations (รับ Handover ไปดูแลต่อ), Finance/Legal (ปิดสัญญา/การเงิน), Business Owner (รับผิดชอบ Benefit ต่อ) | Handover Pack, Closure Report, Benefits Handover Plan → โครงการปิดจบ ระบบเข้าสู่การดูแลปกติ และเริ่มวัดผล Benefit จริงหลังจบโปรเจกต์ |

## Pattern ที่เห็นซ้ำทุก Phase

PM แทบไม่ได้ "ลงมือทำเนื้องาน" เองเลย บทบาทหลักของ PM คือ **ประสาน → ตัดสินใจในกรอบอำนาจ → ผลักดันให้ได้ Output → ส่งต่อ** ส่วนเนื้องานจริง (วิเคราะห์ ออกแบบ เขียน ทดสอบ อนุมัติเชิงธุรกิจ) เป็นของ Role เฉพาะทางเสมอ และ Output ของแต่ละ Phase จะกลายเป็น **Input บังคับ** ของ Phase ถัดไปเป็นทอดๆ ตลอดสาย A→H

## เอกสารที่มักหาไม่เจอ: SRS / FSD / Tech Spec / Test Plan อยู่ตรงไหน

คำถามที่พบบ่อยที่สุดคือเอกสารเหล่านี้ "หายไปไหน" — คำตอบคือมันไม่ได้หาย แต่เป็น Output ของ **Phase C (Detailed Planning)** ไม่ใช่ Phase D:

- **SRS / FSD** — ผลผลิตของ BA ใน Phase C (Conditional: ต้องมีเมื่อ Contract Formal, ระบบซับซ้อน, ต้อง Sign-off — ดู Playbook V2 §C4) ถ้าตัดออกต้องมีเอกสารทดแทน เช่น User Story + Acceptance Criteria ที่ Coverage เทียบเท่า
- **Technical Design (TDD/SDD)** — ผลผลิตของ Architect/Tech Lead ใน Phase C เช่นกัน (หรือ ADR/Architecture Docs เป็นเอกสารทดแทน)
- **Test Strategy / Test Plan** — วางแผนใน Phase C (Plan Quality and Acceptance) แล้วนำไป **รันจริง** ใน Phase D และ F — ตัว Test Plan (แผน) กับ Test Results (ผลการรัน) จึงอยู่คนละ Phase กัน
- **RTM (Requirements Traceability Matrix)** — เริ่มสร้างใน Phase C แล้วอัปเดตต่อเนื่องถึง Phase F เพื่อโยง Requirement → Design → Test → Acceptance

PMBOK ไม่บังคับชื่อไฟล์เป๊ะ — สิ่งที่บังคับคือ "เนื้อหา" ต้องถูก Elicit, Analyze, Document, Approve, Trace ให้ครบ ไม่ว่าจะเก็บเป็นไฟล์แยกหรือรวมอยู่ใน Backlog/Wiki ก็ได้ (ดู [Playbook V2 §C4.1](../../repository/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md))

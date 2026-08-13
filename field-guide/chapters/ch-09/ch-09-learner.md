---
chapter: ch-09
title: "Go-Live และ Hypercare (Playbook G)"
book: "PM Delivery Guide: From Pre-sales to Closure — คู่มือปฏิบัติการบริหารโครงการซอฟต์แวร์ (PMBOK 8th Edition)"
edition: Learner
status: Draft
validation_status: Not Validated
last_reviewed: 2026-08-13
intended_learner_level: Experienced PM
difficulty: Core
estimated_study_time: 100
prerequisite:
  - "Ch.8 — Verification/UAT และ Release Readiness (Go/No-Go)"
related_chapters:
  - "Ch.5 — Environment/Release/Transition Plan (C17, แผนเบื้องต้น)"
  - "Ch.10 — Transition & Closure (ต่อจาก Stabilization)"
canonical_source:
  - ../../references/PMBOK-Aligned-End-to-End-Project-Delivery-Playbook-V2.md (Phase G)
  - ../../e-Book/chapters/lesson-05/lesson-05-learner.md (แนวคิด Close Project — บางส่วน)
scenario_version:
  hotel_booking: "1.0"
artifact_outputs:
  - name: Cutover Plan + Rollback Plan
    creator: Release Manager + DevOps + PM
    artifact_owner: Release Manager
    reviewer: Tech Lead, Ops, Data Lead
    approval_authority: Sponsor / Go-Live Authority
    approval_evidence: Approved cutover + rollback test evidence
  - name: Deployment/Migration Evidence + Incident Log
    creator: DevOps + Data + Support
    artifact_owner: Hypercare Owner
    reviewer: PM, Ops
    approval_authority: Ops Owner (stabilization acceptance)
    approval_evidence: Deployment evidence, migration reconciliation, incident log
  - name: Hypercare Report + Stabilization Acceptance
    creator: Support + PM
    artifact_owner: Hypercare Owner
    reviewer: Operations Owner
    approval_authority: Operations Owner / Sponsor
    approval_evidence: Stabilization criteria met + acceptance
---

# Chapter 09 — Go-Live และ Hypercare: ขึ้น Production อย่างควบคุมได้

## 1. Opening Scenario Hook

**[Teaching Scenario]** Go/No-Go ผ่านแบบ conditional — SHG เตรียม Soft Launch 3 โรงแรมในคืนวันศุกร์ (ก่อน High Season 1 พ.ย.) คุณสุทธิ (PM) ตรวจ checklist พบว่า: cutover plan มีขั้นตอนครบ แต่ Rollback Plan ยังไม่ถูกทดสอบจริง, support team ยังไม่ได้ซ้อม hypercare runbook, และคุณภัทร (VP Marketing) ถามว่า "แล้ว campaign เปิดวันไหน"

**[PMBOK 8]** บทนี้เป็นเนื้อหาใหม่ที่ e-Book เดิมไม่มี: Go-live ไม่ใช่ "กดปุ่ม deploy แล้วจบ" แต่คือการบริหาร **Cutover, Rollback, Monitoring และ Stabilization** อย่างเป็นระบบ — และ Go-live ไม่เท่ากับ Project Closure (นั่นคือ Ch.10)

## 2. Why It Matters

**[Best Practice]** โครงการจำนวนมากไปถึง go-live แต่พังเพราะ: ไม่มี cutover sequence ชัด, rollback ไม่เคยทดสอบ, ไม่มี command center, hypercare ไม่มี exit criteria หรือ communication ไปผิดคน — ต้นทุนของความผิดพลาดตอนนี้สูงที่สุดในโครงการ (ลูกค้าใช้จริง เงินจริง trust จริง)

**[PMBOK 8]** Go-Live คือจุดที่ output เริ่มกลายเป็น outcome — แต่ benefit (35% direct booking ใน 18 เดือน) จะพิสูจน์ได้หลัง stabilization และถูกส่งต่อเป็นความรับผิดชอบของ business (Ch.10)

## 3. Mental Model

```text
Go/No-Go Decision (Ch.8) + Cutover/Rollback Plan (Ch.5 C17)
  -> Entry Criteria Check (G.2)
  -> Cutover Window: Freeze -> Backup -> Deploy -> Configure
     -> Migrate Data -> Reconcile -> Smoke Test -> Business Verify
  -> Enable Users -> Monitor
  -> Rollback? (trigger -> decide ภายในเวลาจำกัด -> restore)
  -> Hypercare Command Center (triage, SLA, daily review)
  -> Stabilization Criteria (G.8) ผ่าน
  -> Operations Acceptance -> Ch.10 (Transition & Closure)
```

## 4. Main Lesson

### 4.1 Entry Criteria (G.2)

**[Best Practice]** ก่อนเริ่ม cutover ต้องมี: Go Decision, Approved Cutover Plan, Rollback Plan (ทดสอบแล้ว), Production Access, Data Ready, Support Team Ready, Monitoring Ready, Communication Ready, Owners Available

### 4.2 Cutover Plan (G.3)

**[Best Practice]** ต้องระบุ: Task, Sequence, Start/End, Owner, Dependency, Validation, Decision Point, Rollback Trigger, Communication, Evidence — cutover เป็น sequence ที่ทุกขั้นตอนมี owner และจุดตรวจ

### 4.3 Deployment Steps (G.4)

```text
Freeze/Change Window -> Backup -> Deploy -> Configure -> Migrate Data
-> Reconcile Data -> Smoke Test -> Business Verification -> Enable Users
-> Monitor -> Communicate -> Confirm Production Status
```

### 4.4 Rollback Plan (G.5) — ห้ามขึ้น Production โดยไม่มี

**[Best Practice]** ต้องตอบ: Rollback Trigger (อะไร), Who Decides, Maximum Decision Time (กี่นาที), Backup Location, Restore Steps, Data Reconciliation, Communication, Business Continuity

**[Teaching Scenario]** SHG: trigger = payment failure rate > threshold หรือ critical booking flow ล่ม ภายใน 30 นาทีหลัง enable — ผู้ตัดสินใจ = คุณวีระ (CTO) + PM ภายใน 15 นาที — restore จาก backup + message ถึงลูกค้า/โรงแรม

### 4.5 Hypercare (G.6)

**[Best Practice]** Hypercare = ช่วงสนับสนุนเข้มหลัง go-live: Command Center, Support Hours, Incident Priority, Triage, Technical/Business Owners, Daily Review, Metrics, Exit Criteria

### 4.6 Hypercare Metrics (G.7) + Stabilization Criteria (G.8)

**[Best Practice]**
- **Metrics:** Incident Count, Severity, Response/Resolution Time, Transaction Success, Error Rate, Performance, User Adoption, Data Reconciliation, Support Volume
- **Stabilization:** ไม่มี Critical Incident ค้าง, Error Rate ใน threshold, Performance Stable, Business Transaction ถูกต้อง, Support รับช่วงได้, Known Issues มี Plan, Operations ยอมรับ Handover

**[Teaching Scenario]** SHG soft launch 3 โรงแรม: monitor payment success ≥ 99%, booking confirmation ≤ 5 วินาที, incident response ตาม SLA กับ 2C2P, daily review กับ hotel partners — stabilizaztion ผ่านเมื่อ 7 วันไม่มี critical incident + payment error < threshold

## 5. PM Decision Thinking

```text
Decision: หลัง soft launch พบ payment failure rate สูงเกิน threshold — Rollback, Fix-in-place หรือ Continue with mitigation?
Owner: Go-Live Authority (Sponsor/คุณจิรา) ตัดสิน; PM + CTO นำเสนอ options ภายในเวลาจำกัด
Inputs: rollback plan, monitoring data, defect triage, business impact, support capacity, cutover evidence
Options:
  A: Rollback (restore ระบบเดิม) — ปลอดภัยสุด แต่ลูกค้าเสีย trust + campaign กระทบ
  B: Fix-in-place (hotfix + monitor เข้ม) — เร็ว แต่ต้องมั่นใจว่า root cause ชัด
  C: Continue with mitigation (จำกัดฟีเจอร์, workaround) — กลาง ๆ แต่เสี่ยงสะสม
Trade-offs: speed to restore vs stability, trust vs momentum, local vs full impact
Risk: ตัดสินใจช้า -> ผลกระทบกระจาย; ตัดสินใจเร็วเกิน -> rollback เองก็เสียหาย
Evidence: incident log, rollback trigger check, decision record ภายในเวลาจำกัด, communication
Next Action: ตาม decision -> stabilize -> monitor -> ขยาย/ถอนตาม criteria -> Ch.10
```

## 6. ตัวอย่างจริงจาก Case ต่อเนื่อง (SHG)

**[Teaching Scenario]**

- **Cutover (Soft Launch 3 โรงแรม):** คืนวันศุกร์ 02:00–06:00 — freeze, backup, deploy, migrate data 3 โรงแรม, reconcile (ตรงกับ Scenario Master Sprint 12)
- **Smoke test:** booking flow + payment + PMS sync ผ่าน
- **Enable users:** front desk + ลูกค้าเริ่มจอง — campaign ของคุณภัทรเปิดพร้อมกันแบบ pilot
- **Monitor:** พบ payment failure 4% (ต่ำกว่า trigger) + 2 incident minor (confirmation email ช้า) — fix-in-place + monitor ต่อ
- **Hypercare 2 สัปดาห์:** command center (PM, CTO, QA, support, 2C2P hotline), daily review, metrics tracking
- **ขยาย:** หลัง 7 วันเสถียร → ขยายไปอีก 3 โรงแรม → ครบ 12 ตามแผน full launch
- **Stabilization:** ผ่านเมื่อ error rate < threshold + support รับช่วงได้ → ส่งต่อ Ch.10

**[PMBOK 8]** สังเกตว่า decision แต่ละจุดมี trigger, เวลาจำกัด และ evidence — ไม่มี "เดี๋ยวค่อยว่ากัน"

## 7. จุดตัดสินใจและกับดักที่พบบ่อย

**Common Mistakes:**

1. ขึ้น Production โดยไม่มี Rollback Plan ที่ทดสอบจริง — ผล: ผิดพลาดแล้วฟื้นไม่ได้
2. Cutover ไม่มี sequence/owner ต่อขั้น — ผล: วุ่นวาย ไม่รู้ใครทำอะไร
3. ไม่มี Command Center / escalation path — ผล: incident วิ่งหาคนไม่มีเจ้าภาพ
4. Hypercare ไม่มี exit criteria — ผล: อยู่แบบไม่มีที่สิ้นสุด หรือออกเร็วเกิน
5. ใช้ Production data ผิด (test กับ data จริง) — ผล: ข้อมูลเสียหาย
6. Communication ไม่ถึงลูกค้า/โรงแรม — ผล: โรงแรมไม่รู้ว่าต้องเปลี่ยน workflow
7. คิดว่า Go-live = จบโครงการ — ผล: benefit/adoption ไม่มีเจ้าของ (Ch.10)

**Common Misconceptions:**

| ความเข้าใจผิด | ความจริง |
|---|---|
| Go-live = Project Closure | Closure คือ Ch.10 (handover, benefit owner, lessons) |
| Rollback แพงเกินไป ต้องทำ | ไม่มี rollback = การพนันกับ production |
| Hypercare = ทีม support ธรรมดา | เป็นช่วงเข้มมี command center + metrics + exit criteria |
| Deploy ผ่าน = สำเร็จ | ต้อง monitor + stabilize + business verify |
| ระบบใหม่ต้องไม่มี incident | ต้องมี triage + known issues + plan |
| Cutover = ขั้นตอนเดียว | เป็น sequence ที่มี validation + decision point ต่อขั้น |

## 8. Interview Questions

### Foundational
- **Q:** Rollback Plan ต้องตอบคำถามอะไรบ้าง?
- **Answer Direction:** Trigger, ผู้ตัดสินใจ, เวลาจำกัด, backup location, restore steps, data reconciliation, communication, business continuity
- **Warning Signs:** ตอบว่า "กู้ backup กลับ" โดยไม่มี trigger/time/owner

### Scenario
- **Q:** หลัง soft launch พบ payment failure สูงกว่า threshold — คุณจะทำอย่างไร?
- **Answer Direction:** เปิด trigger → นำเสนอ options (rollback/fix-in-place/mitigation) ภายในเวลาจำกัด → ตัดสินใจตาม evidence (root cause, business impact) → บันทึก decision → สื่อสาร (ลูกค้า/โรงแรม/support) → monitor หลัง action
- **Warning Signs:** รอให้ทีม "ดูอีกที" โดยไม่มีเวลาจำกัด หรือ rollback ทันทีโดยไม่ดู severity

### Senior PM
- **Q:** คุณจะออกแบบ Hypercare อย่างไรให้มี exit ที่ชัดเจน?
- **Answer Direction:** กำหนด stabilization criteria (metrics + threshold + ระยะเวลา), command center + roles, daily review, incident SLA, known-issues plan — exit เมื่อ criteria ผ่าน + operations ยอมรับ handover; ถ้าไม่ผ่าน ขยาย hypercare พร้อมเหตุผล
- **Warning Signs:** ตอบว่า "คุม 2 สัปดาห์แล้วจบ" โดยไม่มี criteria

### Executive
- **Q:** ทำไมต้องยอมเสียเวลา/เงินกับ cutover rehearsal และ rollback test?
- **Answer Direction:** rehearsal เผยปัญหาในสภาพปลอดภัย (ราคาถูก); rollback test ทำให้มั่นใจว่าถ้าผิดพลาดฟื้นได้ — ต้นทุนเล็กน้อยเทียบกับ downtime/campaign ล่ม/trust เสียหาย — เหมือนประกัน
- **Warning Signs:** ตอบว่า "เสียเวลาทำไม แค่ deploy"

## 9. PM Dictionary ประจำบท

| Term (EN) | คำอธิบาย (TH) | ความหมายเชิงปฏิบัติ | การใช้ผิดที่พบบ่อย | Term ที่เกี่ยวข้อง |
|---|---|---|---|---|
| Cutover | การเปลี่ยนผ่านเข้าสู่ระบบใหม่ | สลับจากระบบเดิมไประบบใหม่ใน Production | สับสนกับ Go-Live | Go/No-Go |
| Rollback | การย้อนกลับระบบ | แผน restore เมื่อ go-live ผิดพลาด | ไม่ทดสอบแล้วขึ้น Production | Cutover |
| Go-Live | การขึ้น Production | เริ่มให้ผู้ใช้ใช้งานจริง | คิดว่า = Closure | Hypercare |
| Hypercare | สนับสนุนเข้มหลัง Go-live | command center + triage + metrics + exit | คิดว่า = support ธรรมดา | Stabilization |
| Command Center | ศูนย์บัญชาการเหตุการณ์ | จุดรวม incident/triage/decision หลัง go-live | ไม่มี escalation path | Incident |
| Stabilization | การเข้าสู่สภาวะเสถียร | incident ลด, performance คงที่, support รับช่วงได้ | คิดว่า 2 วันจบ | Hypercare |
| Smoke Test | ทดสอบขั้นพื้นฐาน | ตรวจว่าดีploy ผ่าน/ระบบลุกก่อน enable users | ใช้แทน full test | Deployment |
| Data Reconciliation | ตรวจสอบข้อมูล | เทียบ data หลัง migration ให้ตรงกัน | ข้ามไป | Migration |
| Incident | เหตุการณ์ผิดปกติ | ต้องมี triage, severity, SLA, owner | สับสนกับ Defect (ช่วง dev) | Defect |
| Rollback Trigger | เงื่อนไขย้อนกลับ | ตัวเลข/สัญญาณที่บอกว่า "ถอย" | ไม่กำหนด | Rollback |
| Production Verification | ตรวจหลังขึ้นจริง | ยืนยันว่าระบบทำงานใน Production | ข้าม | Smoke Test |

## 10. Workshop

### Scenario
**[Teaching Scenario]** SHG เตรียม cutover soft launch 3 โรงแรมคืนวันศุกร์ — พบว่า: rollback ยังไม่เคยทดสอบจริง, support ยังไม่ได้ซ้อม runbook, campaign ของคุณภัทรจะเปิดวันจันทร์ถัดไป, และ GM โรงแรม 1 แห่งยังไม่ยืนยันความพร้อมของ front desk

### Your Role
PM (คุณสุทธิ) ที่ต้องตัดสินใจ: เลื่อน cutover, ทำแบบมีเงื่อนไข, หรือเดินหน้าตามแผน

### Available Information
- Go decision (conditional จาก Ch.8), cutover plan draft, monitoring/alert setup, Scenario Master (soft launch 3 โรงแรม = Sprint 12)

### Missing Information
- ผล rollback rehearsal (ยังไม่ทำ), training status ของ front desk โรงแรมที่ 3, ความพร้อม 2C2P hotline, communication draft ถึงลูกค้า

### Decision Required
- เดินหน้าคืนนี้ / เลื่อน 48 ชม. เพื่อปิด gap / ขึ้น 2 โรงแรมก่อน แล้วโรงแรมที่ 3 ตามหลัง — พร้อมเหตุผลและ owner ของ gap

### Constraints
- Launch ก่อน High Season (1 พ.ย.), ห้ามขึ้น production โดยไม่มี rollback ที่ทดสอบแล้ว, campaign ต้องไม่เปิดก่อนระบบเสถียร

### Expected Output
- Go/Defer decision record (options + trade-off + owner + due date), gap closure plan (rollback rehearsal, training, communication), hypercare plan หน้าเดียว (command center, roles, metrics, exit criteria)

### Debrief Questions
1. ทำไม "เลื่อน 48 ชม." อาจถูกกว่าการขึ้นทั้งที่ gap ค้าง
2. Hypercare exit criteria ที่ดีควรเป็นอย่างไร
3. ถ้าเกิด incident กลาง cutover ใครตัดสินใจ rollback ภายในกี่นาที

### Evaluation Criteria
- Decision มี evidence + trade-off, gap มี owner + due date, rollback trigger/time/owner ชัด, hypercare มี exit criteria, ไม่ขัด Scenario Master

## 11. Checklist ใช้งานจริง (Go-Live & Hypercare / Phase G)

- [ ] Entry criteria ครบ (Go decision, cutover plan, rollback tested, access, data, support, monitoring, communication, owners)
- [ ] Cutover plan มี sequence + owner + validation + decision point ต่อขั้น
- [ ] Rollback plan ทดสอบจริง: trigger, ผู้ตัดสินใจ, เวลาจำกัด, restore steps, reconciliation, communication
- [ ] Deployment steps ครบ (freeze → backup → deploy → configure → migrate → reconcile → smoke → business verify → enable)
- [ ] Monitoring + alert ตั้งก่อน enable
- [ ] Communication พร้อม (ลูกค้า, โรงแรม, support, partners)
- [ ] Hypercare: command center + roles + support hours + triage + SLA + daily review
- [ ] Metrics ติดตาม (incident, error rate, performance, transaction success, reconciliation)
- [ ] Stabilization criteria กำหนดไว้ล่วงหน้า
- [ ] Known issues มี plan + owner
- [ ] Operations ยอมรับ handover ก่อนจบ hypercare
- [ ] ส่งต่อ Ch.10: stabilization acceptance + handover pack + benefit baseline

## 12. Assessment

1. **[Decision Case]** หลัง soft launch พบ payment failure 6% (threshold 4%) — เสนอ rollback/fix-in-place/mitigation พร้อม trigger, เวลาจำกัด, decision owner
2. **[Decision Case]** คืนก่อน cutover พบว่า rollback ยังไม่ทดสอบ — คุณจะเดินหน้า/เลื่อน/แบ่งเฟสอย่างไร พร้อมเหตุผล
3. **[Artifact Review]** ตรวจ cutover plan ที่มี task list แต่ไม่มี owner/sequence/validation/rollback trigger ต่อขั้น — ระบุความเสี่ยงและวิธีแก้
4. **[Scenario Case]** โรงแรมที่ 3 ไม่พร้อม (front desk ยังไม่ซ้อม) — ตัวเลือกในการจัดการพร้อม trade-off
5. **[Trade-off Case]** Rollback (ลูกค้าเสีย trust, campaign กระทบ) vs Fix-in-place (เสี่ยง root cause ยังไม่ชัด) — อธิบายและให้คำแนะนำ
6. **[Cross-Knowledge Analysis]** ถ้า hypercare พบว่า PMS sync error 5% — กระทบ booking accuracy (Ch.9) และ benefit 35% direct booking (Ch.10) อย่างไร และทางเลือกคืออะไร
7. **[Recall]** Stabilization criteria (G.8) มีอะไรบ้าง (ระบุ ≥ 5)

## 13. Executive Summary

| มิติ | สรุป |
|---|---|
| **Why** | Go-Live คือจุดที่ระบบถูกใช้จริง — ความผิดพลาดที่นี่แพงที่สุดในโครงการ |
| **Decision Improved** | rollback/fix/mitigation ตัดสินด้วย trigger + เวลาจำกัด + evidence |
| **Failure Prevented** | ป้องกันขึ้น production ไร้ rollback, hypercare ไร้ exit, และ communication ไร้เจ้าภาพ |
| **What to Monitor** | incident count/severity, error rate, performance, reconciliation, stabilization criteria |

## 14. เชื่อมไปบทถัดไป + Artifact Handoff

**Bridge:** Stabilization ผ่าน + Operations ยอมรับ — โครงการเข้าสู่ช่วงปิด: Ch.10 (Transition & Closure) จะทำ Operational Handover, Final Acceptance, Contract/Financial Closure, Lessons Learned และ Benefit Handover (Integration ท่อนที่ 3: Close Project or Phase)

| Field | Handoff |
|---|---|
| Input | Go decision (Ch.8), Environment/Release Plan (Ch.5), Incident/Hypercare Records |
| Output | Cutover/Rollback Evidence, Incident Log, Hypercare Report, Stabilization Acceptance |
| Creator | Release Manager + DevOps (cutover), Support + PM (hypercare) |
| Artifact owner | Release Manager / Hypercare Owner / Operations Owner |
| Reviewer | Tech Lead, Ops, Sponsor |
| Approval authority | Sponsor (go-live), Operations Owner (stabilization) |
| Minimum acceptance | Usable (ต้องมี rollback test + stabilization evidence) |
| Next chapter use | Ch.10 ใช้ stabilization acceptance + hypercare data ไปทำ Handover, Closure และ Benefit Handover |

## 15. Quick Reference Card

```text
GO-LIVE & HYPERCARE (G)
------------------------------------------------------------
Entry: Go decision + cutover plan + rollback tested + data/support/monitoring ready
Cutover: freeze -> backup -> deploy -> configure -> migrate -> reconcile
         -> smoke -> business verify -> enable -> monitor -> communicate
Rollback: trigger? ใครตัดสินใจ? กี่นาที? backup ที่ไหน? restore ยังไง?
          reconcile? สื่อสารใคร? business continuity?
Hypercare: command center + triage + SLA + daily review + metrics + exit criteria
Stabilization: ไม่มี critical incident + error rate ในเกณฑ์ + support รับช่วงได้

กฎ 3 ข้อห้าม:
- ห้ามขึ้น Production โดยไม่มี rollback ที่ทดสอบแล้ว
- ห้าม hypercare ไร้ exit criteria
- ห้ามคิดว่า Go-live = จบโครงการ (จบจริง = Ch.10)
```

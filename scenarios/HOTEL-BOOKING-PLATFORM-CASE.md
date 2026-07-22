---
title: Hotel Booking Digital Platform — Scenario Master
document_type: Scenario Definition
version: 1.0
status: Draft
last_updated: 2026-07-22
usage: ทุก Lesson ต้องอ้างอิง Scenario Master นี้ ห้ามสร้างตัวเลขหรือข้อเท็จจริงใหม่โดยไม่ update ไฟล์นี้
---

# Scenario B — Hotel Booking Digital Platform

> **ข้อมูลในไฟล์นี้เป็น Teaching Scenario ที่สร้างขึ้นเพื่อการเรียนรู้ ไม่ใช่ข้อเท็จจริงจากโครงการจริง**

## Related Teaching Walkthrough

- [Hotel Booking End-to-End PM Walkthrough](./HOTEL-BOOKING-END-TO-END-PM-WALKTHROUGH.md) — ใช้สอนแบบ step-by-step ตั้งแต่ product business need, MVP, backlog, sprint delivery, launch readiness, stabilization จนถึง benefits review

---

## 1. Business Background

**บริษัท:** เครือโรงแรม สิริ ฮอสพิทาลิตี้ จำกัด (Siri Hospitality Group — SHG)

- ธุรกิจ: เครือโรงแรมระดับ 3–5 ดาว
- จำนวนโรงแรม: 12 แห่ง (กรุงเทพฯ 3, เชียงใหม่ 2, ภูเก็ต 3, สมุย 2, พัทยา 2)
- ห้องพักรวม: ~2,400 ห้อง
- พนักงาน: ~3,000 คน
- ระบบปัจจุบัน: ใช้ PMS (Property Management System) แยกแต่ละโรงแรม + จองผ่าน OTA (Agoda, Booking.com) 70% + โทรศัพท์/อีเมล 20% + Walk-in 10%
- ปัญหาหลัก: Commission ให้ OTA สูง 15-25%, ไม่มีฐานข้อมูลลูกค้าของตัวเอง, ไม่มี Direct Booking Channel, ไม่สามารถทำ Loyalty Program, ห้องพักว่างแต่ OTA ยังไม่อัปเดต (Inventory Sync ล่าช้า)

## 2. Business Need

> สร้าง Direct Booking Platform (Website + Mobile App) ของเครือโรงแรมเอง เพื่อเพิ่มสัดส่วน Direct Booking จาก 10% เป็น 35% ภายใน 18 เดือนหลัง Launch ลด OTA Commission และสร้างฐานข้อมูลลูกค้าสำหรับ Loyalty Program

## 3. Project Objectives

1. สร้าง Customer-facing Website (Responsive) สำหรับค้นหา เปรียบเทียบ และจองห้องพัก
2. สร้าง Mobile Application (iOS + Android) สำหรับจองห้องพัก + Guest Experience
3. สร้าง Back Office Web Application สำหรับ Revenue Management + Booking Management + Hotel Partner Admin
4. สร้าง Landing Page สำหรับ Marketing Campaign
5. เชื่อมต่อ Booking Engine กับ PMS ทั้ง 12 โรงแรม (Real-time Inventory Sync)
6. เชื่อมต่อ Payment Gateway (Credit Card, Promptpay, Bank Transfer)
7. สร้าง Notification System (Email, SMS, Push Notification)
8. เพิ่มสัดส่วน Direct Booking จาก 10% เป็น 35% ภายใน 18 เดือนหลัง Launch

## 4. Scope

### In Scope — MVP (Phase 1)

- **Customer Web App:** ค้นหาห้องพัก, ดูรายละเอียดโรงแรม/ห้อง, เปรียบเทียบราคา, จองห้องพัก, ชำระเงิน, รับ Booking Confirmation, จัดการการจอง (View/Cancel/Modify)
- **Mobile App (iOS + Android):** Feature เหมือน Web + Push Notification + Guest Check-in (Digital Key จะทำใน Phase 2)
- **Landing Page:** Marketing Campaign Page, SEO-optimized
- **Back Office Web Application:** Booking Dashboard, Rate Management, Inventory Management, Booking Report, Customer Management (basic)
- **Booking Engine:** Real-time Availability, Rate Calculation, Room Allocation, Booking Confirmation, Cancellation Policy Engine
- **Hotel & Room Inventory:** Sync กับ PMS 12 โรงแรม, Room Type, Availability, Rate Plan, Blackout Date
- **Payment:** Credit Card (Visa, Mastercard), Promptpay, Bank Transfer — ผ่าน Payment Gateway (2C2P)
- **Notification:** Email Confirmation, SMS Reminder, Push Notification

### Out of Scope (Phase 2+)

- Loyalty Program / Points System
- Digital Key / Mobile Check-in
- Chat / AI Chatbot
- Multi-language (เริ่ม Thai + English เท่านั้น)
- Restaurant / Spa Booking
- Travel Package / Activity Booking
- Advanced Analytics / Recommendation Engine
- Channel Manager Integration (ยังคงจัดการ OTA แยก)

## 5. Stakeholders

| Stakeholder | Role | Power | Interest | Strategy |
|---|---|---|---|---|
| คุณจิรา — CEO | Executive Sponsor | High | High | Manage Closely |
| คุณภัทร — VP Marketing | Business Owner (Direct Booking KPI) | High | High | Manage Closely |
| คุณสมศรี — VP Operations | Hotel Operations Representative | High | Medium | Keep Satisfied |
| คุณกาญจนา — Revenue Manager | Revenue & Pricing Strategy | Medium | High | Keep Informed |
| คุณวีระ — CTO | Technical Owner | High | High | Manage Closely |
| คุณนภา — Product Owner | Product Direction & Backlog Priority | High | High | Manage Closely |
| คุณธีร์ — UX Lead | User Experience | Medium | High | Keep Informed |
| General Managers (12 โรงแรม) | Hotel Partners | Medium | Medium | Keep Informed |
| Front Desk Staff (12 โรงแรม) | End Users (Booking Management) | Low | High | Keep Informed |
| ลูกค้า (Guests) | End Users (Booking) | Low | High | Monitor + UX Research |
| 2C2P | Payment Gateway Provider | Medium | Medium | Keep Satisfied |
| PMS Vendors (แต่ละโรงแรม) | System Integration Partners | Medium | Medium | Keep Satisfied |
| Marketing Agency | Digital Marketing Execution | Low | Medium | Monitor |

## 6. Organization Structure

- **โครงสร้าง:** Projectized — ทีมพัฒนา Dedicated Full-time
- **Product Owner:** คุณนภา (Full-time, Business side)
- **Project Manager / Scrum Master:** คุณสุทธิ (Full-time)
- **Development Team:**
  - UX/UI Designer: 2 คน
  - Frontend Developer (Web + Mobile): 4 คน
  - Backend Developer: 3 คน
  - QA Engineer: 2 คน
  - DevOps: 1 คน
- **Business Team:**
  - Revenue Manager: คุณกาญจนา (Part-time advisor)
  - Content Writer: 1 คน
  - Hotel Coordinator: 1 คน (ประสานงานกับ 12 โรงแรม)
- **External:**
  - PMS Integration Specialist: 1 คน (Vendor)
  - Payment Gateway Support: 2C2P Technical Support

## 7. Vendor / External Partners

| Partner | Service | Contract Type | Value |
|---|---|---|---|
| 2C2P | Payment Gateway | Transaction Fee (2.5% + 7 บาท/txn) | — |
| AWS | Cloud Infrastructure | Pay-as-you-go | ~120,000 บาท/เดือน |
| PMS Vendors (ต่างๆ) | API Integration Support | T&M | ~500,000 บาท รวม |
| Design Agency | Brand Identity + Initial UI Kit | Fixed-Price | 800,000 บาท |

## 8. Constraints

1. **Launch Date:** ต้อง Launch ก่อน High Season (1 พฤศจิกายน) — ใช้เวลาพัฒนา ~8 เดือน
2. **Budget:** ไม่เกิน 12 ล้านบาท (Phase 1)
3. **PMS Integration:** PMS แต่ละโรงแรมต่างยี่ห้อ ต้องทำ Adapter แยก
4. **Payment Compliance:** PCI-DSS compliance สำหรับ Credit Card
5. **Performance:** Website ต้อง Load ภายใน 3 วินาที, Booking Confirmation ภายใน 5 วินาที
6. **Availability:** System Uptime ≥99.5%
7. **Data Privacy:** PDPA compliance

## 9. Assumptions

1. PMS ทั้ง 12 โรงแรมมี API ที่ใช้งานได้ (หรือสามารถ build adapter ได้ภายในงบ)
2. 2C2P Payment Gateway รองรับ Transaction Volume ที่คาดการณ์
3. ทีมพัฒนาสามารถ recruit ครบภายใน 2 สัปดาห์แรก
4. General Managers ทั้ง 12 โรงแรมยินดีให้ข้อมูลห้องพักและราคา
5. Marketing Budget แยกจาก Project Budget
6. Content (รูปภาพ, คำบรรยาย) ของโรงแรมมีอยู่แล้ว ไม่ต้องถ่ายใหม่

## 10. Key Risks (Pre-project)

| Risk | Probability | Impact | Strategy | Owner |
|---|---|---|---|---|
| PMS Integration ล่าช้าเพราะ API ไม่พร้อม | High | High | Mitigate — PoC Integration ก่อน Sprint 1 | คุณวีระ (CTO) |
| Payment Security Breach | Low | Critical | Avoid — PCI-DSS audit ก่อน Launch | คุณวีระ (CTO) |
| Low Conversion Rate หลัง Launch | Medium | High | Mitigate — UX Testing ตั้งแต่ Sprint 2 | คุณนภา (PO) |
| โรงแรมไม่อัปเดตราคา/ห้องว่าง | Medium | High | Mitigate — Auto-sync + SLA กับ Hotels | คุณสมศรี (VP Ops) |
| Booking ซ้ำซ้อนกับ OTA (Double Booking) | Medium | High | Mitigate — Inventory Lock mechanism | คุณสุทธิ (PM) |
| Performance ไม่ผ่านในช่วง Peak | Medium | Medium | Mitigate — Load Test ก่อน Launch | DevOps |

## 11. Timeline (Agile Delivery)

| Sprint/Phase | Duration | Focus |
|---|---|---|
| Sprint 0 (Setup) | 2 สัปดาห์ | Architecture, CI/CD, Design System, PMS PoC |
| Sprint 1-2 | 4 สัปดาห์ | Core Booking Flow (Search → View → Book) on Web |
| Sprint 3-4 | 4 สัปดาห์ | Payment Integration + Booking Confirmation + Email |
| Sprint 5-6 | 4 สัปดาห์ | Mobile App (iOS + Android) |
| Sprint 7-8 | 4 สัปดาห์ | Back Office + Rate Management + Inventory Sync |
| Sprint 9-10 | 4 สัปดาห์ | Landing Page + Notification + Analytics |
| Sprint 11 | 2 สัปดาห์ | UAT + Performance Test + Security Test |
| Sprint 12 | 2 สัปดาห์ | Bug Fix + Soft Launch (Pilot 3 โรงแรม) |
| Full Launch | — | ขยายไปทั้ง 12 โรงแรม |
| Post-Launch Support | 3 เดือน | Monitoring + Bug Fix + Quick Wins |
| **Total:** | **~8 เดือน** | — |

## 12. Budget Context

| Category | Budget (ล้านบาท) |
|---|---|
| Development Team (8 เดือน) | 6.0 |
| Cloud Infrastructure (AWS) | 1.0 |
| Design Agency | 0.8 |
| PMS Integration | 0.5 |
| Payment Gateway Setup | 0.2 |
| QA / Security Audit | 0.5 |
| Contingency (15%) | 1.5 |
| Management Reserve | 1.5 |
| **Total Budget** | **12.0** |

## 13. Deliverables

1. Product Backlog (prioritized by PO)
2. UX/UI Design (Figma) — Mobile + Web + Back Office
3. Customer Web Application (Responsive)
4. Mobile Application (iOS + Android)
5. Landing Page
6. Back Office Web Application
7. Booking Engine (with PMS Integration)
8. Payment Integration (2C2P)
9. Notification System (Email, SMS, Push)
10. Performance Test Report
11. Security Audit Report (PCI-DSS compliance)
12. UAT Sign-off (PO + VP Marketing)
13. Launch Plan + Rollback Plan
14. Post-Launch Monitoring Dashboard

## 14. Expected Outcomes

| Timeframe | Outcome | Metric |
|---|---|---|
| 1 เดือนหลัง Launch | ลูกค้าสามารถจองห้องพักผ่าน Platform ได้ | ≥100 Bookings/เดือน |
| 6 เดือนหลัง Launch | Direct Booking เพิ่มขึ้น | 10% → 20% ของ Total Bookings |
| 18 เดือนหลัง Launch | Direct Booking Target | 10% → 35% ของ Total Bookings |
| 18 เดือนหลัง Launch | ลด OTA Commission | ประหยัด ≥3 ล้านบาท/ปี |

## 15. Benefits

| Benefit | Measurement | Target |
|---|---|---|
| เพิ่ม Direct Booking Revenue | % Direct vs OTA | 35% Direct |
| ลด OTA Commission Cost | Commission Saved (บาท/ปี) | ≥3 ล้านบาท/ปี |
| สร้างฐานข้อมูลลูกค้า | Customer Database Size | ≥10,000 profiles ใน 12 เดือน |
| เพิ่ม Guest Satisfaction | Booking NPS | ≥40 |
| Real-time Inventory Visibility | Inventory Sync Accuracy | ≥98% |

## 16. Operating Model (Post Launch)

- **Product Owner:** คุณนภา (ดูแล Backlog + Roadmap ต่อเนื่อง)
- **Development Team:** ลดเหลือ 6 คน (2 Frontend, 2 Backend, 1 QA, 1 DevOps)
- **Operations:**
  - Revenue Manager ดูแล Rate Strategy
  - Hotel Coordinator ดูแลการ Sync กับ 12 โรงแรม
  - Customer Support Team (ใช้ทีมเดิมของเครือ)
- **Incident Management:** On-call rotation, SLA-based
- **Enhancement:** Sprint-based delivery ทุก 2 สัปดาห์
- **Product Metrics Dashboard:** Conversion Rate, Bounce Rate, Revenue per Visit, Booking Cancellation Rate

---

## Key Differences from ERP Scenario (for Teaching)

| Dimension | ERP Transformation | Hotel Booking Platform |
|---|---|---|
| Project Type | Enterprise Transformation | Digital Product |
| Delivery Approach | Hybrid with predictive governance | Agile product delivery with predictive controls |
| Primary Stakeholder | Internal (Employees) | External (Customers) |
| Success Metric | Process Efficiency | Customer Conversion |
| Change Management | User Adoption of internal process | Market Adoption of product |
| Timeline | 12 เดือน | 8 เดือน |
| Budget / Funding | Working Budget 45 ล้านบาท; Total Funding Envelope 60 ล้านบาท | Phase 1 Budget 12 ล้านบาท |
| Vendor Dependency | High (SI + ERP vendor) | Medium (payment gateway, PMS vendors, cloud, design agency) |
| Org Structure | Strong Matrix | Projectized |
| Feedback Loop | Phase-gate (SIT/UAT) | Every Sprint (2 weeks) |

---

## Scenario Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-07-22 | Initial scenario definition |

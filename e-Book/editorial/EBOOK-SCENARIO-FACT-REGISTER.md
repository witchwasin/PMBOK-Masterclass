---
title: E-book Scenario Fact Register
document_type: E-book Editorial Control
status: Active
created_on: 2026-07-22
---

# E-book Scenario Fact Register

## Authority

Scenario facts must come from:

1. `scenarios/ERP-TRANSFORMATION-CASE.md`
2. `scenarios/HOTEL-BOOKING-PLATFORM-CASE.md`
3. The related walkthrough files in `scenarios/`

If a chapter needs a teaching assumption, label it `[Teaching Scenario]`. If a chapter needs a calculation not recorded as a scenario actual, label it:

```text
Teaching Calculation - not a locked scenario actual
```

## ERP Transformation Locked Facts

| Category | Locked fact |
|---|---|
| Company | บริษัท สยาม อินดัสเทรียล กรุ๊ป จำกัด (Siam Industrial Group - SIG) |
| Business need | Replace fragmented legacy systems with one ERP to centralize data/processes, improve real-time visibility and reduce financial close time |
| Close-cycle target | 15 days to 5 working days |
| Scope | FI, SD, MM, PP and HCM modules |
| Integrations | Banking, e-Tax and TMS |
| Out of scope | CRM, BI/advanced analytics, Field Sales mobile app and factory hardware changes |
| Organization | Strong Matrix with full-time PM and Project Office |
| Project manager | คุณเอก |
| Sponsor | คุณสมชาย - CEO |
| Technical owner | คุณอรุณ - IT Director |
| System integrator | บริษัท TechConsult จำกัด |
| Delivery working budget | 45 ล้านบาท |
| Total funding envelope | 60 ล้านบาท |
| Timeline | About 12 months |
| Go-live constraint | Before 1 October fiscal-year start |
| Hypercare | 3 months after Go-live |
| Key adoption outcome | At least 80% of transactions through the new system 3 months after Go-live |
| Finance outcome | Close within 5 working days 6 months after Go-live |
| Visibility outcome | Dashboard usable 12 months after Go-live |

## Hotel Booking Locked Facts

| Category | Locked fact |
|---|---|
| Company | เครือโรงแรม สิริ ฮอสพิทาลิตี้ จำกัด (Siri Hospitality Group - SHG) |
| Business need | Build a direct booking platform to increase direct booking, reduce OTA commission and create a customer database for loyalty |
| Direct booking target | 10% to 35% within 18 months after launch |
| Budget | 12 ล้านบาท for Phase 1 |
| Timeline | About 8 months |
| Launch constraint | Before high season on 1 November |
| Product scope | Customer web app, mobile app, landing page, back office web application, booking engine, PMS sync, payment and notifications |
| Hotel footprint | 12 hotels and about 2,400 rooms |
| Current booking mix | OTA 70%, phone/email 20%, walk-in 10% |
| Sponsor | คุณจิรา - CEO |
| Product owner | คุณนภา |
| PM / Scrum Master | คุณสุทธิ |
| Technical owner | คุณวีระ - CTO |
| Payment gateway | 2C2P |
| Availability target | System uptime at least 99.5% |
| Performance target | Website load within 3 seconds; booking confirmation within 5 seconds |
| 1-month outcome | At least 100 bookings per month |
| 6-month outcome | Direct booking reaches 20% of total bookings |
| 18-month benefit | Save at least 3 ล้านบาท per year in OTA commission |

## Prohibited Changes

- Do not use ERP working budget and ERP total funding envelope interchangeably.
- Do not change Hotel Booking direct booking target, budget or timeline.
- Do not add new in-scope modules, vendors, payment methods, product features or regulatory constraints as facts unless sourced.
- Do not convert teaching examples into locked scenario facts.


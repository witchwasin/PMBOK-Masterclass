---
title: Hotel Booking Digital Platform — End-to-End PM Walkthrough
document_type: Teaching Walkthrough
scenario_source: ./HOTEL-BOOKING-PLATFORM-CASE.md
status: Draft
version: 1.0
last_updated: 2026-07-22
---

# Hotel Booking Digital Platform — End-to-End PM Walkthrough

## Purpose

This walkthrough teaches how a PM would run the Hotel Booking Platform case from product idea to launch, stabilization, and benefits review. It is a teaching guide, not a real implementation plan.

Use this together with [Hotel Booking Platform Scenario Master](./HOTEL-BOOKING-PLATFORM-CASE.md).

## Case Baseline

- Sponsor: คุณจิรา, CEO
- Product Owner: คุณนภา
- PM/Scrum Master: คุณสุทธิ
- Budget: 12 ล้านบาท for Phase 1
- Timeline: about 8 months
- Launch constraint: before 1 November high season
- Outcome target: direct booking from 10% to 35% within 18 months after launch
- Product scope: web app, mobile app, landing page, back office, booking engine, PMS integration, payment, notification

## Step 1 — Confirm Product Business Need

The PM and PO start from value, not features.

Decision questions:

1. Why does the hotel group need direct booking?
2. Which customer behavior must change?
3. Which metrics prove value after launch?

Expected outputs:

- Product vision
- Business outcome map
- Initial KPI tree

Outcome metrics:

- Direct booking share
- OTA commission saving
- Booking conversion
- Payment success rate
- Inventory sync accuracy

PM judgement:

The project is not successful only because the app is launched. It must create direct bookings and reduce OTA dependency.

## Step 2 — Initiate the Product Project

Actions:

1. Confirm sponsor and product owner authority
2. Define MVP boundary
3. Identify stakeholders
4. Confirm budget and timeline
5. Identify risks and assumptions
6. Decide delivery approach

Expected outputs:

- Project charter or lightweight product initiation document
- Stakeholder register
- Initial product backlog
- Delivery approach decision

Decision gate:

Do not start sprint delivery until PO authority, MVP scope, funding, and launch constraints are clear.

## Step 3 — Choose Agile with Selective Predictive Controls

Hotel Booking is a digital product with high learning needs, so Agile is primary. Some areas still need predictive control.

Agile controls:

- Product backlog
- Sprint planning
- Sprint review
- Retrospective
- Definition of Done
- Product metrics dashboard

Predictive controls:

- Payment compliance
- Security audit
- Vendor/SLA terms
- Launch readiness gate
- Budget cap
- PMS integration milestones

Expected outputs:

- Delivery model
- Agile working agreement
- Definition of Done
- Release governance

Decision gate:

If work is exploratory, use backlog and sprint feedback. If work is compliance or contractual, use explicit gates and acceptance criteria.

## Step 4 — Define MVP Scope and Product Backlog

Actions:

1. Translate business need into epics
2. Define MVP in scope and out of scope
3. Create product backlog
4. Prioritize by direct booking value and risk
5. Define acceptance criteria

MVP epics:

- Search and hotel detail
- Room selection
- Booking engine
- Payment
- Confirmation and notification
- Customer account and booking management
- Back office rate and inventory management
- PMS integration
- Landing page

Out of scope for Phase 1:

- Loyalty points
- Digital key
- AI chatbot
- Restaurant or spa booking
- Advanced analytics

Decision gate:

When marketing requests a new feature before launch, PM/PO must check whether it improves the direct booking outcome enough to justify schedule, cost, quality, and risk impact.

## Step 5 — Plan Release and Sprint Cadence

Actions:

1. Set sprint length
2. Sequence epics by dependency and risk
3. Plan release milestones
4. Reserve time for UAT, performance, security, and bug fix
5. Define soft launch and full launch

Baseline cadence:

- Sprint 0: architecture, CI/CD, design system, PMS PoC
- Sprint 1-2: core booking flow
- Sprint 3-4: payment and confirmation
- Sprint 5-6: mobile apps
- Sprint 7-8: back office and inventory sync
- Sprint 9-10: landing page, notification, analytics
- Sprint 11: UAT, performance, security
- Sprint 12: bug fix and soft launch

Decision gate:

Payment and PMS integration should be addressed early because they carry high uncertainty and high impact.

## Step 6 — Build Team and Working System

Actions:

1. Confirm dedicated team
2. Clarify PO, PM/Scrum Master, UX, dev, QA, DevOps roles
3. Create team working agreement
4. Set Definition of Done
5. Set quality and release standards

Definition of Done should include:

- Code complete
- Peer review done
- Automated tests passed
- Security checks passed where relevant
- UX acceptance
- PO acceptance
- Analytics/event tracking ready
- No critical defect open

Decision gate:

If the team says “done” but the work cannot be released or measured, it is not done.

## Step 7 — Execute Sprint Delivery

Actions each sprint:

1. Sprint planning
2. Daily coordination
3. Build and test increment
4. Review with PO and stakeholders
5. Capture feedback
6. Retrospective for team process improvement
7. Reprioritize backlog

Evidence:

- Working increment
- Sprint review feedback
- Defect trend
- Burndown or flow metrics
- Updated backlog

Decision gate:

Sprint output should be working product evidence, not only status slides.

## Step 8 — Manage PMS, Payment, and Partner Risks

Critical risks:

- PMS integration delay
- Payment gateway failure
- Payment security breach
- Inventory sync error
- Low conversion
- Hotel partner adoption
- Performance failure during high season

Actions:

1. Run PMS PoC before Sprint 1
2. Test payment early
3. Define fallback or incident path
4. Conduct load test before campaign
5. Monitor partner inventory readiness
6. Run UX tests from early sprints

Decision gate:

Payment failure, double booking, or security risk should block launch until risk is accepted by the right authority with mitigation.

## Step 9 — Control Cost and Scope

Actions:

1. Track burn against 12 ล้านบาท budget
2. Separate project build cost from post-launch operation cost
3. Review scope changes through backlog and governance
4. Use phase 2 backlog for lower-priority features
5. Track cloud and vendor run-rate

Decision gate:

A feature can be valuable but still not belong in the current MVP if it threatens payment stability, launch readiness, or conversion learning.

## Step 10 — Prepare Launch Readiness

Actions:

1. Confirm UAT sign-off
2. Complete performance test
3. Complete security audit
4. Confirm PCI-DSS relevant controls
5. Confirm payment success criteria
6. Confirm PMS inventory sync
7. Confirm support playbook
8. Confirm rollback plan
9. Confirm marketing campaign readiness

Launch readiness evidence:

- No critical payment defects
- Booking confirmation within target
- Website loads within 3 seconds
- Booking confirmation within 5 seconds
- Uptime readiness aligned with 99.5% target
- Support team ready

Decision gate:

Launch is a business risk decision. If payment, inventory, security, or performance evidence is weak, PM/PO should recommend delay, soft launch, limited hotel rollout, or feature disablement.

## Step 11 — Soft Launch and Full Launch

Actions:

1. Soft launch with pilot hotels
2. Monitor payment, conversion, cancellation, inventory, incidents
3. Fix critical issues
4. Confirm operational readiness
5. Expand to all 12 hotels

Decision gate:

Do not scale to all hotels if pilot metrics show payment instability, inventory mismatch, or support overload.

## Step 12 — Post-launch Stabilization

Actions:

1. Run post-launch support for 3 months
2. Track incidents and customer feedback
3. Use Kanban for production issues
4. Keep sprint delivery for enhancements
5. Monitor conversion funnel
6. Prioritize quick wins

Key metrics:

- Booking volume
- Conversion
- Payment success rate
- Bounce rate
- Inventory sync accuracy
- Customer support tickets
- Booking cancellation rate

Decision gate:

If direct booking is low, do not assume the technology failed immediately. Diagnose funnel, price, UX, inventory, campaign, trust, and payment.

## Step 13 — Benefits Review and Product Roadmap

Actions:

1. Review 1-month booking usage
2. Review 6-month direct booking shift
3. Review 18-month direct booking target
4. Compare OTA commission saving
5. Decide phase 2 roadmap

Possible phase 2 items:

- Loyalty program
- Digital key
- AI chatbot
- Advanced analytics
- Restaurant/spa booking
- Recommendation engine

PM handoff:

After launch, delivery shifts into product operating model led by PO, product team, hotel operations, support, and executive outcome owner.

## End-to-End Teaching Flow

| Stage | PM/PO Focus | Key Decision |
|---|---|---|
| Business Need | Direct booking value | What customer/business behavior must change? |
| Initiation | Authority and MVP | Is the product project ready to start? |
| Approach | Agile plus controls | Which parts need sprint learning and which need gates? |
| Backlog | Scope and value | What belongs in MVP vs later? |
| Delivery | Working increments | Is each sprint producing releasable learning? |
| Risk | Payment, PMS, conversion | Which risks block launch? |
| Launch | Readiness | Full launch, soft launch, delay, or rollback? |
| Stabilization | Operations and metrics | Is the platform stable and usable? |
| Benefits | Outcome | Is direct booking moving toward 35%? |

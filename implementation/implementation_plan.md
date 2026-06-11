# Implementation Plan
**Solution:** Voize AI Documentation — Berlin Elderly Care Company
**Company size:** 150–200 employees
**Location:** Berlin, Germany
**Revised:** June 2026 (updated for German compliance requirements)

---

## Overview

The implementation follows a four-phase model: Discovery → Pilot → Evaluate → Scale. The total timeline is **29–36 weeks (~7–8 months)**, shorter than a typical AI deployment because Voize is an app-based, smartphone-native tool with no hardware requirements and an offline-first architecture.

The timeline was revised from the original 10-month estimate to account for two Germany-specific factors that accelerate rollout (faster Voize onboarding) and two that add time at the front (GDPR/AVV review and Betriebsrat consultation).

---

## Phase 1 — Discovery & Vendor Selection
**Duration: 8–10 weeks**
**Why longer than a standard vendor selection:** Germany requires GDPR data processing agreements, BSI C5 certification verification, and — critically — works council consultation before any deployment begins.

### Activities

**Weeks 1–2: Internal Baseline Assessment**
- Audit current documentation workflows: time per shift, tools in use, pain points by role
- Map existing IT infrastructure: EHR system in use, TI connectivity status, device availability
- Identify the 40–60 frontline caregivers who will be the primary users
- Define success KPIs (see KPI framework below)

**Weeks 3–4: Betriebsrat Engagement** *(Germany-specific — do not skip)*
- Formally notify the works council of the intention to introduce a technology that records and processes staff speech
- Share Voize's data processing documentation, privacy policy, and the AVV
- Works council has up to 4 weeks to respond under German law (*Mitbestimmungsrecht* § 87 BetrVG)
- Objective: written agreement (*Betriebsvereinbarung*) before signing vendor contract

> ⚠️ **Critical:** Starting this in Week 3 — not after the contract is signed — is the single biggest risk mitigation step in the entire plan. Betriebsrat delays are the most common cause of digital project failure in German SMEs.

**Weeks 3–5: Vendor Due Diligence**
- Request Voize's *Auftragsverarbeitungsvertrag* (AVV / Data Processing Agreement)
- Verify BSI C5 Type 2 certification for cloud data handling (Voize's offline-first architecture reduces exposure, but cloud-sync must be verified)
- Confirm ePA/TI integration compatibility with your specific EHR system
- Negotiate contract: include exit clauses, data deletion terms, and SLA commitments
- Confirm pricing: €12–€15/user/month; negotiate volume discount for 40+ seats

**Weeks 6–8: Pilot Design**
- Select pilot unit: one wing, one shift type (e.g., morning shift in residential unit)
- Identify pilot cohort: 10–15 caregivers — mix of experience levels, ideally including sceptics
- Appoint **AI Champion**: a respected senior caregiver or nurse who becomes the internal advocate and point of contact
- Design parallel documentation protocol for first 3 weeks of pilot

**Weeks 8–10: Betriebsrat Sign-off & Contract Execution**
- Finalise *Betriebsvereinbarung* with works council
- Sign Voize contract
- Schedule vendor onboarding session

### Phase 1 Exit Criteria
- [ ] AVV signed; GDPR compliance confirmed
- [ ] Betriebsvereinbarung signed by Betriebsrat
- [ ] BSI C5 compliance verified
- [ ] Pilot cohort identified; AI Champion appointed
- [ ] KPIs defined and baseline documented
- [ ] Voize contract signed

---

## Phase 2 — Pilot
**Duration: 8–10 weeks**
**Why shorter than originally planned:** Voize's onboarding is days, not weeks. The critical adoption signal appears by day 3–5. Parallel documentation is only needed for 2–3 weeks before caregivers can switch fully.

### Activities

**Weeks 1–2: Onboarding**
- Vendor-led onboarding session with pilot cohort (typically 1–2 hours)
- AI Champion leads day-one walkthrough on the floor
- Install Voize on pilot cohort devices (or use BYOD smartphones)
- Configure device management (MDM) if required

**Weeks 1–3: Parallel Documentation**
- Caregivers use both Voize and their existing documentation method simultaneously
- Purpose: validate that Voize entries are accurate and complete before full switch
- AI Champion monitors day 3–5 for engagement signals; intervene early if adoption is lagging

> ⚠️ **Voize's own data shows the critical window is day 3–5.** Facilities that drift off-track in week one rarely self-correct. Build a structured check-in at day 5 — not week 3.

**Weeks 4–7: Voize-Only Documentation**
- Pilot cohort switches to Voize as sole documentation method
- AI Champion collects weekly feedback (brief 5-minute check-in per shift)
- Track KPIs weekly against baseline

**Weeks 8–10: Measurement & Documentation**
- Compile KPI data for Phase 3 evaluation
- Collect structured feedback from all pilot users
- Document integration issues, edge cases, and dialect/terminology gaps
- Prepare go/no-go recommendation for leadership

### Phase 2 KPIs to Track

| KPI | Measurement Method | Target |
|---|---|---|
| Minutes saved per caregiver per shift | Self-report + time-motion spot check | ≥20 minutes |
| Daily active usage rate | Voize dashboard | ≥80% of pilot cohort |
| Documentation accuracy | Spot-check vs. manual baseline | ≥95% field accuracy |
| Staff satisfaction score | Anonymous survey (1–5) | ≥4.0/5.0 |
| Errors or safety incidents attributable to AI | Incident log | 0 |

### Phase 2 Exit Criteria
- [ ] KPI data compiled for all 8–10 weeks
- [ ] Staff satisfaction score ≥ 4.0/5.0
- [ ] ≥ 80% of pilot cohort using Voize daily
- [ ] Zero documentation-related safety incidents
- [ ] AI Champion endorses rollout

---

## Phase 3 — Evaluation & Go/No-Go Decision
**Duration: 3–4 weeks**

### Activities

**Week 1–2: Data Analysis**
- Calculate actual time savings vs. projected (target: ≥20 min/shift)
- Calculate annualised ROI using Berlin wage rate (€23/hour)
- Compare actual costs to budget
- Identify any integration or compliance issues encountered

**Week 3: Leadership Presentation**
- Present findings to Cleo and leadership team
- ROI calculation: actual savings vs. Year 1 cost
- Staff feedback summary
- Risks encountered and mitigations applied
- Recommended rollout scope and pace

**Week 4: Decision**
- Go: proceed to full rollout with agreed scope
- Conditional go: address specific issues before scaling
- No-go: document learnings; consider alternative tool or approach

### Phase 3 Exit Criteria
- [ ] ROI confirmed or exceeded projection
- [ ] Leadership sign-off on full rollout
- [ ] Revised rollout plan approved (if adjustments needed)

---

## Phase 4 — Full Company Rollout
**Duration: 10–12 weeks**
**Why faster than original 18-week estimate:** Voize's app-based model scales facility-wide without hardware, IT projects, or complex configurations. The pilot team becomes the training backbone.

### Activities

**Weeks 1–2: Rollout Planning**
- Sequence rollout by unit/shift (stagger to avoid disruption)
- AI Champion trains unit leads from each shift
- Prepare device management at scale

**Weeks 3–8: Phased Deployment**
- Week 3–4: Second unit/shift goes live
- Week 5–6: Third unit/shift goes live
- Week 7–8: Remaining units go live
- AI Champion and vendor support available throughout

**Weeks 9–12: Stabilisation**
- Monitor KPIs company-wide weekly
- Address edge cases (unusual dialects, complex care note types)
- Establish monthly KPI review cadence
- Begin planning Phase 2 (Lindera fall prevention)

### Phase 4 Exit Criteria
- [ ] All frontline caregivers onboarded
- [ ] Company-wide daily usage ≥ 80%
- [ ] Monthly KPI review cadence established
- [ ] Phase 2 scoping initiated

---

## Timeline Summary

| Phase | Duration | Key Milestone |
|---|---|---|
| Phase 1: Discovery & Vendor Selection | 8–10 weeks | Betriebsvereinbarung signed; contract executed |
| Phase 2: Pilot | 8–10 weeks | KPIs confirmed; staff satisfaction ≥ 4.0 |
| Phase 3: Evaluation | 3–4 weeks | Go/no-go decision made |
| Phase 4: Full Rollout | 10–12 weeks | Company-wide deployment complete |
| **Total** | **29–36 weeks (~7–8 months)** | Full adoption reached |

### Old vs. Revised Timeline

| Phase | Original | Revised | Reason |
|---|---|---|---|
| Discovery | 6 weeks | 8–10 weeks | + GDPR/AVV review, + Betriebsrat consultation (4–8 weeks), + BSI C5 check |
| Pilot | 12 weeks | 8–10 weeks | Voize onboards in days; parallel documentation only 2–3 weeks |
| Evaluation | 4 weeks | 3–4 weeks | Unchanged |
| Rollout | 18 weeks | 10–12 weeks | App-based scaling is fast; no hardware or complex IT |
| **Total** | **~40 weeks** | **~29–36 weeks** | Faster overall despite slower start |

---

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Betriebsrat delays deployment | Medium | High | Engage in Week 3 of Phase 1 — not after contract signing |
| GDPR/AVV non-compliance | Medium | Very High | Require AVV before contract execution; legal review of data processing |
| Staff resistance / low adoption | Medium | High | Appoint AI Champion; monitor day 3–5 adoption signal; Voize's 96% retention suggests this is manageable |
| BSI C5 compliance gap (cloud) | Low–Medium | High | Verify certification; Voize's offline architecture reduces exposure |
| Low pilot accuracy | Low | Medium | 2–3 week parallel documentation phase; Voize maps to fixed fields only |
| Dialect or terminology gaps | Low | Low | Voize is trained on German nursing dialects; flag gaps to vendor during pilot |
| Vendor capacity / support delays | Low | Low | Berlin-based vendor; local support available |

---

## Governance & Roles

| Role | Responsibility |
|---|---|
| **Cleo (CEO)** | Overall sponsor; approves Phase 3 go/no-go |
| **Operations Lead** | Day-to-day implementation owner |
| **AI Champion (internal)** | Floor-level adoption lead; feedback collector; first point of contact for staff |
| **Voize Account Manager** | Vendor onboarding; technical support; EHR integration |
| **Legal/Compliance** | AVV review; Betriebsrat coordination |
| **IT Lead (if applicable)** | TI connectivity confirmation; device management |

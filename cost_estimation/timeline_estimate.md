# Timeline Estimation
**Solution:** Voize AI Documentation
**Company:** 150–200 person caregiving company, Berlin, Germany
**Revised:** June 2026

---

## Summary

| Version | Total Duration | Key Driver |
|---|---|---|
| Original estimate | ~40 weeks (~10 months) | Generic AI SaaS deployment |
| **Revised estimate** | **~29–36 weeks (~7–8 months)** | Germany-specific compliance + Voize's faster onboarding |

The revised timeline is **shorter overall** despite adding compliance steps at the front. This is because Voize's app-based, offline-first architecture makes the pilot and rollout phases significantly faster than originally modelled.

---

## What Changed and Why

### Factors That Add Time (Germany-Specific)

| Factor | Time Added | Why It Cannot Be Skipped |
|---|---|---|
| **GDPR / AVV review** | +1–2 weeks | German care data is subject to GDPR + PDSG + SGB requirements. Non-compliance risks fines up to €20M. AVV must be signed before any data processing begins |
| **BSI C5 Type 2 verification** | +1 week | From July 2025, healthcare cloud services in Germany require BSI C5 Type 2 certification. Must be verified before contract execution |
| **Betriebsrat consultation** | +4–8 weeks | Companies with 150+ employees must consult the works council before deploying technology that records or monitors staff (§ 87 BetrVG). Works council has up to 4 weeks to respond. This is the single most common cause of digital project delays in German SMEs |

> ⚠️ **The Betriebsrat is the most important timeline variable.** If engaged in Week 3 of Phase 1 alongside vendor due diligence, it runs in parallel and adds minimal net delay. If engaged after contract signing, it can freeze deployment for 1–3 months.

### Factors That Reduce Time (Voize-Specific)

| Factor | Time Saved | Evidence |
|---|---|---|
| **App-based, no hardware** | -4–6 weeks vs. hardware solutions | No procurement, shipping, installation, or configuration |
| **Offline-first architecture** | -2–3 weeks vs. cloud-dependent tools | No network infrastructure project required |
| **Fast staff adoption** | -3–4 weeks vs. complex clinical systems | 96% daily retention; most staff prefer within days (Voize, 2025) |
| **Day 3–5 adoption signal** | Reduces pilot length | Critical check at day 5 replaces 4-week parallel documentation phase |
| **German-native language model** | -2 weeks setup | No language configuration, no terminology mapping project |

---

## Detailed Phase Timeline

### Phase 1 — Discovery & Vendor Selection
**Duration: 8–10 weeks**

```
Week 1–2    Internal baseline audit
            ├── Document current shift documentation workflow
            ├── Map EHR system and TI connectivity status
            └── Define KPIs and baseline metrics

Week 3–4    Betriebsrat notification ← START THIS EARLY
            ├── Formal notification under § 87 BetrVG
            ├── Share Voize data processing documentation
            └── Works council review period begins (up to 4 weeks)

Week 3–5    Vendor due diligence (runs in parallel with Betriebsrat)
            ├── Request and review Voize AVV
            ├── Verify BSI C5 Type 2 certification
            ├── Confirm EHR/ePA integration compatibility
            └── Negotiate contract terms (exit clauses, SLA, pricing)

Week 6–7    Pilot design
            ├── Select pilot unit and cohort (10–15 caregivers)
            ├── Appoint AI Champion
            └── Design parallel documentation protocol

Week 8–10   Sign-off and contract execution
            ├── Betriebsvereinbarung signed by Betriebsrat
            ├── Voize contract signed
            └── Onboarding session scheduled
```

**Phase 1 Exit Gate:**
- [ ] Betriebsvereinbarung executed
- [ ] AVV signed; GDPR/BSI compliance confirmed
- [ ] Voize contract signed
- [ ] Pilot cohort identified; AI Champion appointed
- [ ] KPI baseline documented

---

### Phase 2 — Pilot
**Duration: 8–10 weeks**

```
Week 1      Onboarding
            ├── Vendor-led session with pilot cohort (1–2 hours)
            ├── AI Champion leads floor walkthrough
            └── Voize installed on pilot devices

Week 1–3    Parallel documentation
            ├── Caregivers use both Voize + existing method
            ├── AI Champion monitors for accuracy
            └── ⚠️ Day 3–5 check: intervene if adoption is lagging

Week 4–7    Voize-only documentation
            ├── Parallel documentation retired
            ├── Weekly KPI tracking begins
            └── AI Champion collects weekly feedback

Week 8–10   Measurement & go/no-go preparation
            ├── Compile KPI data
            ├── Structured staff feedback survey
            └── Prepare Phase 3 evaluation brief
```

**Phase 2 Exit Gate:**
- [ ] ≥ 80% pilot cohort using Voize daily
- [ ] ≥ 20 min/shift time saving confirmed
- [ ] Staff satisfaction score ≥ 4.0/5.0
- [ ] Zero documentation-related safety incidents
- [ ] AI Champion endorses full rollout

---

### Phase 3 — Evaluation & Decision
**Duration: 3–4 weeks**

```
Week 1–2    Data analysis
            ├── Actual vs. projected time savings
            ├── Annualised ROI calculation (Berlin wage: €23/hr)
            └── Cost vs. budget comparison

Week 3      Leadership presentation to Cleo
            ├── ROI confirmed / adjusted
            ├── Staff feedback summary
            └── Rollout recommendation

Week 4      Go / Conditional Go / No-Go decision
```

**Phase 3 Exit Gate:**
- [ ] ROI confirmed ≥ projection (or explained variance)
- [ ] Cleo sign-off on full rollout scope
- [ ] Rollout schedule approved

---

### Phase 4 — Full Company Rollout
**Duration: 10–12 weeks**

```
Week 1–2    Rollout planning
            ├── Sequence by unit/shift
            ├── AI Champion trains unit leads
            └── Device management at scale confirmed

Week 3–4    Unit 2 goes live
Week 5–6    Unit 3 goes live
Week 7–8    Remaining units go live
Week 9–12   Stabilisation
            ├── Company-wide KPIs monitored weekly
            ├── Edge cases documented and fed back to vendor
            └── Phase 2 (Lindera) scoping begins
```

**Phase 4 Exit Gate:**
- [ ] All frontline caregivers onboarded
- [ ] Company-wide daily usage ≥ 80%
- [ ] Monthly KPI review cadence established
- [ ] Lindera (Phase 2) feasibility assessment initiated

---

## Visual Timeline

```
WEEKS:    1    2    3    4    5    6    7    8    9    10
PHASE 1:  [AUDIT]  [BETRIEBSRAT CONSULTATION ──────────]
                   [VENDOR DUE DILIGENCE ───]
                                  [PILOT DESIGN]  [SIGN]

WEEKS:    11   12   13   14   15   16   17   18   19   20
PHASE 2:  [ONBOARD][──── PARALLEL DOCS ────][─ VOIZE ONLY ────]

WEEKS:    21   22   23   24
PHASE 3:  [ANALYSIS]  [PRESENT]  [DECISION]

WEEKS:    25   26   27   28   29   30   31   32   33   34   35   36
PHASE 4:  [PLAN][UNIT2][UNIT3][UNITS 4+][── STABILISATION ──────]
```

**Total: 29–36 weeks depending on Betriebsrat response speed**

---

## Key Dependencies & Risks

| Dependency | Risk if Late | Owner |
|---|---|---|
| Betriebsrat notified in Week 3 | Entire Phase 2 blocked until resolved | Operations Lead / HR |
| AVV reviewed before contract | GDPR non-compliance risk | Legal / Compliance |
| BSI C5 verified before go-live | Regulatory exposure | IT Lead |
| AI Champion appointed by Week 6 | Pilot adoption at risk | Operations Lead |
| EHR integration confirmed in Phase 1 | Pilot delayed by technical issues | IT Lead + Voize |

---

## Comparison: Germany vs. Generic Timeline

| Factor | Generic AI Deployment | Germany (Voize) |
|---|---|---|
| Vendor selection | 4–6 weeks | 5–7 weeks (+GDPR/BSI checks) |
| Works council | Not applicable | 4–8 weeks (Betriebsrat) |
| Staff training | 3–4 weeks | 1–2 weeks (app-based; fast) |
| Pilot parallel phase | 4 weeks | 2–3 weeks (Voize signal at day 3–5) |
| Full rollout | 16–20 weeks | 10–12 weeks (no hardware) |
| **Total** | **~10 months** | **~7–8 months** |

Germany's compliance layer adds 4–6 weeks to the front. Voize's architecture removes 6–8 weeks from the back. Net result: a shorter, more compliant deployment.

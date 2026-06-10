# Use Case Discovery & AI Adoption Recommendation
**Project:** AI Adoption Opportunity — Elderly Care Sector  
**Prepared by:** AI Strategy Consultant  
**Client:** CareNest GmbH — Cleo Hartman, Geschäftsführerin (CEO)  
**Location:** Berlin, Germany  
**Date:** June 2026  
**Version:** 2.0 — Revised following market research, ROI modelling, evidence review, and real-world case study analysis

> **Revision note:** This document supersedes v1.0 (Week 7, Day 5). The core use case longlist is unchanged, but the prioritisation sequence has been revised based on evidence gathered in Part 1 and Part 2 of the engagement. The primary recommendation has changed from Tour Planning Optimisation to Care Documentation. The reasoning for each reordering is documented explicitly in Section 4.
>
> **Document scope:** This file covers company context, stakeholder mapping, use case definitions, and sequencing rationale. Sector trends and vendor evidence live in `market_research.md`. Opportunity sizing, risk analysis, and hype mapping live in `opportunities_risks.md`.

---

## 1. Client & Company Overview

**Company Name:** CareNest GmbH  
**CEO:** Cleo Hartman  
**Sector:** Elderly Care / Home Care Services (Ambulante Pflege)  
**Company Size:** Medium (approx. 120 employees)  
**Location:** Berlin, operating across three Berlin districts (Bezirke)

CareNest GmbH is a privately owned ambulatory home care provider (ambulanter Pflegedienst) founded in 2014 and registered under German GmbH law. The company provides personalised in-home care services to elderly clients in Berlin, including daily living assistance (Grundpflege), medication management, companionship, and post-hospitalisation support. CareNest employs approximately 85 field caregivers (Pflegefachkräfte and Pflegehelfer), 15 care coordinators (Pflegedienstleitungen and Tourenplaner), 10 administrative staff, and a small management team.

CareNest operates under the German Social Care Insurance framework (Soziale Pflegeversicherung, SGB XI) and is subject to quality inspection by the Medizinischer Dienst (MD). As a contracted provider, CareNest's reimbursement rates are largely determined by agreements with statutory health insurers (gesetzliche Krankenkassen), creating tight margin constraints typical of the German ambulatory care market.

Over the past three years, CareNest has experienced consistent demand growth — driven by Berlin's rapidly ageing population and a pronounced policy preference for home-based care (häusliche Pflege) over residential facilities (stationäre Pflege). However, this growth has been accompanied by mounting operational pressure: scheduling complexity has increased, caregiver turnover has accelerated, and coordinator workloads have become unsustainable. Cleo is aware that competitors are beginning to explore AI-assisted tools but remains cautious about committing budget without clear evidence of return on investment.

> For the full sector context — including Pflegeversicherung financing pressure, workforce shortfall projections, and the Zukunftspakt Pflege reform process — see `market_research.md` § 1.

---

## 2. Stakeholder Analysis

The following stakeholders were identified through desk research and reasonable assumptions based on typical medium-sized German ambulatory care organisational structures.

| Stakeholder | Role | Key Pain Points |
|---|---|---|
| Cleo Hartman | CEO (Geschäftsführerin) | Rising operational costs, difficulty scaling, uncertainty about AI ROI; needs evidence-backed, sequenced investment plan |
| Care Coordinators / Tourenplaner (×15) | Schedule & oversee field visits | Manual tour planning is time-intensive; last-minute cancellations cause chaos; growing caseload with no additional headcount |
| Field Caregivers / Pflegekräfte (×85) | Deliver in-home care | Burnout from inconsistent schedules; poor continuity with familiar clients; excessive time spent on manual Pflegedokumentation after each visit |
| Clients & Families | Receive / oversee care | Want consistency of caregiver, real-time updates, peace of mind |
| HR / People Manager | Recruitment & retention | High turnover rate (~35% annually, above sector average); costly re-hiring; Berlin labour market competition is intense |
| Compliance Officer | Regulatory adherence | MD audit readiness, SGB XI documentation requirements, BDSG/DSGVO compliance; inconsistent or incomplete visit notes create inspection risk |
| Betriebsrat (Works Council) | Employee co-determination | BetrVG §87(1) No. 6 co-determination rights apply to any technical system that monitors or scores employee behaviour; early engagement is a legal requirement, not an option |

**Key insight:** The three most acute pain points — documentation burden, scheduling inefficiency, and caregiver churn — are directly connected. Poor scheduling increases caregiver stress; stress reduces documentation quality; incomplete documentation creates compliance risk that can affect reimbursement and MD ratings. An AI programme that addresses all three creates compounding value — but only if sequenced so that each phase builds trust and capability for the next.

**Note on the Betriebsrat:** Added explicitly in v2.0. In v1.0 it appeared only as a compliance footnote. Given the BetrVG co-determination obligation — which applies to churn prediction in particular — the works council is an active project stakeholder whose engagement must be planned from the outset, not managed retrospectively.

---

## 3. AI Use Case Longlist

Three candidate use cases were identified during initial discovery, each mapped to a core operational pain point.

### Use Case A — Caregiver Tour Planning Optimisation (Tourenoptimierung)

AI-assisted matching of caregivers to client visits based on availability, geographic proximity within Berlin's districts, client preferences, caregiver qualification level (examinated vs. helper), and continuity-of-care history. The system surfaces optimal tour configurations and flags conflicts before coordinators finalise daily routes.

**Relevance:** Directly addresses the daily operational bottleneck experienced by all 15 Tourenplaner. Reduces missed visits, overtime costs, and the administrative burden of manual tour planning — particularly relevant given Berlin's geographic spread across multiple Bezirke.

### Use Case B — Staff Churn Prediction

A predictive model that analyses caregiver behavioural signals — such as shift refusal patterns, schedule change requests, absence frequency, and tenure — to assign a churn risk score to each caregiver. HR and coordinators are alerted when an individual's risk exceeds a defined threshold, enabling proactive retention interventions.

**Relevance:** Directly targets CareNest's ~35% annual turnover rate in a city where competition for qualified Pflegefachkräfte is intense. The cost of replacing a single caregiver (recruitment, onboarding, training) is estimated at €3,500–€5,500. At current scale, that represents a potential annual cost of €105,000–€165,000 in churn-related expenses — not accounting for productivity loss and client continuity disruption.

### Use Case C — Care Documentation Processing (Pflegedokumentation-Automatisierung)

An AI-assisted voice-to-text tool that supports caregivers in completing visit notes, care plans, and daily logs through ambient or dictated voice capture. The system transcribes, structures, and pushes documentation directly into the existing care management platform, reducing post-visit administrative time while improving consistency and completeness for MD inspection readiness.

**Relevance:** Caregivers in German ambulatory care spend an estimated 20–30% of their working time on documentation (Pflegedokumentation), much of it after visits on personal devices or at the end of long shifts. Incomplete or inconsistent documentation is one of the most common findings in MD inspections and can directly impact CareNest's quality rating.

> For vendor landscape, market maturity assessment, and real-world case studies for all three use cases, see `market_research.md` § 2–3.

---

## 4. Use Case Selection & Justification

**Primary Use Case: Care Documentation Processing** *(revised from Tour Planning Optimisation)*  
**Secondary Use Case: Caregiver Tour Planning Optimisation** *(revised from Staff Churn Prediction)*  
**Tertiary Use Case: Staff Churn Prediction** *(revised from Care Documentation Processing)*

All three use cases remain selected. The sequencing has been revised based on evidence gathered across Part 1 and Part 2 of the engagement. The revised sequence reflects three principles: start with the strongest evidence, the lowest implementation cost, and the use case that affects the most people on day one.

> For the full opportunity sizing, risk analysis, and hype mapping for each use case, see `opportunities_risks.md`.

---

### Why Care Documentation is now Primary

This is the most important change from v1.0, which placed documentation in Phase 3 on the assumption that it benefited from stable scheduling data produced in Phase 1. That dependency does not hold: voice documentation tools such as voize operate as a layer on top of existing care management software and function effectively regardless of whether tour planning has been optimised.

The resequencing is driven by three evidence-based factors:

1. **Strongest external evidence.** The Charité Berlin PYSA study — the first independent, real-conditions study of AI documentation in the German care sector — found a 27% reduction in documentation time across 52 care workers observed over 770 hours. This is peer-reviewed, German, ambulatory-adjacent evidence. No comparable study exists for tour planning or churn prediction in this context.

2. **Lowest cost and fastest adoption path.** Estimated at €12,000 in Year 1 with a 4–5 month payback, documentation is the lowest-cost, fastest-to-value use case. Caregivers adopt voice tools more readily than analytics platforms because the personal benefit is immediate.

3. **Broadest day-one impact.** Documentation burden affects all 85 field caregivers every working day. Tour planning primarily affects 15 coordinators. Starting with documentation means CareNest's AI investment is felt by the entire frontline workforce from week one — building the internal credibility that Phases 2 and 3 will depend on.

**Note on vendor landscape (updated from v1.0):** v1.0 described the NLP documentation market as "emerging" and cited Mediteo and Snap as examples. This assessment is outdated. voize is deployed in 2,000+ German care facilities with peer-reviewed efficacy data and direct MEDIFOX DAN integration. The documentation market should now be characterised as commercially mature and locally validated.

**Key assumption Cleo must validate before Phase 1:** That CareNest caregivers have company-issued smartphones, or that a device provision budget can be allocated. If caregivers use personal devices, DSGVO creates a data separation problem. If no devices are issued, hardware costs must be added to the model.

---

### Why Tour Planning Optimisation is now Secondary

Tour planning remains a strong use case with a well-supported financial model. The mechanism is technically proven; comparable European operations (Swiss Spitex, AlayaCare) show 20–35% travel time reductions with 4–6 month payback at CareNest's scale.

The use case moves to Phase 2 rather than Phase 1 because of one critical assumption that v1.0 did not surface: **the savings from tour planning are captured through capacity — more billable visits in the same time — not through direct cost reduction.** Under SGB XI reimbursement constraints, this means the ROI depends entirely on whether CareNest has unmet client demand to fill freed caregiver capacity. If current utilisation is at or near 100%, the financial case becomes a coordinator efficiency and caregiver quality-of-life argument, not a revenue argument.

Cleo must confirm current utilisation rate and waitlist status before the tour planning ROI projection can be finalised. This is the single highest-leverage open assumption in the Phase 2 model.

Phase 2 also benefits from Phase 1 being live: coordinators who have seen AI work well for documentation are more receptive to AI-assisted scheduling recommendations. The technology trust baseline matters.

---

### Why Staff Churn Prediction is now Tertiary

Churn prediction has the highest potential upside of the three use cases — CareNest's €135,000/year estimated turnover cost means a 50% churn reduction would generate €67,500/year in savings. It is placed in Phase 3 for three reasons that are sharper in v2.0 than in v1.0:

**BetrVG compliance is a legal prerequisite, not a procedural step.** The works council has mandatory co-determination rights before any technical system capable of monitoring or scoring individual employee behaviour is introduced. A churn risk score applied to individual caregivers falls within this definition. Works council consultation must begin during Phase 1 so that the co-determination process is well advanced by Phase 3 launch. CareNest should treat Betriebsrat engagement as a Phase 1 workstream, not a Phase 3 task.

**Data quality is unconfirmed.** The model requires structured historical HR records. Many medium Pflegedienste hold this data in fragmented or paper-based systems. If CareNest's data does not meet minimum quality thresholds, a data preparation phase precedes model development. This must be audited before Phase 3 scope is confirmed.

**The intervention loop is a management dependency.** The model generates risk scores. Churn reduction only occurs if those scores trigger effective, timely management action. A defined intervention protocol must be designed in parallel with the technology.

By Phase 3, both enabling conditions will be in place: Phase 1 will have improved caregiver activity record consistency; Phase 2 will have enriched the signal pool with structured shift and workload data. A model trained on this combined dataset will be materially more accurate than one built today on legacy records.

---

## 5. Revised Sequencing Summary

| Phase | Use Case | Primary Beneficiary | Evidence Strength | Est. Y1 Cost | Est. Annual Benefit (Base) | Payback |
|---|---|---|---|---|---|---|
| Phase 1 | Care Documentation | 85 field caregivers | Strong — peer-reviewed German evidence (Charité/voize) | €12,000 | €35,200 | 4–5 months |
| Phase 2 | Tour Planning Optimisation | 15 coordinators + capacity | Medium — European comparators, no German-specific study | €18,000 | €48,000 | 4–6 months |
| Phase 3 | Staff Churn Prediction | HR + all caregivers | Developing — methodology proven, no German ambulatory case study | €22,000 | €67,500 | 4–5 months |

Combined 3-year ROI (base case): approximately 290% net of all implementation and licence costs.

---

## 6. Open Assumptions Requiring Cleo's Validation

The following items cannot be resolved through external research and must be confirmed internally before each phase is committed. Items are ordered by urgency.

| Assumption | Why It Matters | Phase Affected | Priority |
|---|---|---|---|
| Actual caregiver documentation time (run 2-week time-tracking exercise) | Single biggest lever on Phase 1 ROI; benchmark figures used are sector averages, not CareNest-specific | Phase 1 | Immediate |
| Caregiver smartphone / device policy | Determines voize feasibility and whether hardware cost must be added to Phase 1 budget | Phase 1 | Before contract |
| DSGVO vendor review (voize AVV) | Voice-captured care notes are DSGVO Article 9 health data; legal counsel must verify data processing agreement | Phase 1 | Before contract |
| Current client utilisation rate and waitlist status | Determines whether Phase 2 tour planning savings translate to revenue or coordinator efficiency only | Phase 2 | Before Phase 2 scoping |
| HR data quality audit | Determines whether Phase 3 is feasible on current records or requires a data preparation phase first | Phase 3 | Begin during Phase 1 |
| Betriebsrat engagement | BetrVG §87 co-determination process for Phase 3 must begin during Phase 1 to be ready in time | Phase 3 | Begin during Phase 1 |

> The full evidence log — including resolved research items and sources — is in `market_research.md` § 4.

---

*Document Status: Revised — v2.0, June 2026*  
*Supersedes: use_case_discovery.md (v1.0, Week 7 Day 5)*  
*Related documents: `market_research.md` (v1.0), `opportunities_risks.md` (v1.0)*  
*Next: Incorporate into final business case presentation for Cleo Hartman*

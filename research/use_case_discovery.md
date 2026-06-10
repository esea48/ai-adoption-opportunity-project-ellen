# Use Case Discovery & AI Adoption Recommendation
**Project:** AI Adoption Opportunity — Elderly Care Sector  
**Prepared by:** AI Strategy Consultant  
**Client:** CareNest GmbH — Cleo Hartman, Geschäftsführerin (CEO)  
**Location:** Berlin, Germany  
**Date:** June 2026  

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

---

## 2. Stakeholder Analysis

The following stakeholders were identified through desk research and reasonable assumptions based on typical medium-sized German ambulatory care organisational structures.

| Stakeholder | Role | Key Pain Points |
|---|---|---|
| Cleo Hartman | CEO (Geschäftsführerin) | Rising operational costs, difficulty scaling, uncertainty about AI ROI |
| Care Coordinators / Tourenplaner (×15) | Schedule & oversee field visits | Manual tour planning is time-intensive; last-minute cancellations cause chaos |
| Field Caregivers / Pflegekräfte (×85) | Deliver in-home care | Burnout from inconsistent schedules; poor continuity with familiar clients; excessive time spent on manual Pflegedokumentation after each visit |
| Clients & Families | Receive / oversee care | Want consistency of caregiver, real-time updates, peace of mind |
| HR / People Manager | Recruitment & retention | High turnover rate (~35% annually, above sector average); costly re-hiring |
| Compliance Officer | Regulatory adherence | MD audit readiness, SGB XI documentation requirements, BDSG/DSGVO compliance; inconsistent or incomplete visit notes create inspection risk |

**Key insight:** The three most acute pain points — scheduling inefficiency, caregiver churn, and documentation burden — are directly connected. Poor scheduling increases caregiver stress, which reduces documentation quality, which creates compliance risk. An AI solution that addresses all three creates compounding value across the organisation. Inconsistent or poorly matched tour plans are a leading driver of caregiver dissatisfaction, which feeds into turnover. An AI solution that addresses both creates compounding value.

---

## 3. AI Use Case Longlist

Three candidate use cases were identified during initial discovery, each mapped to a core operational pain point:

### Use Case A — Caregiver Tour Planning Optimisation (Tourenoptimierung)
AI-assisted matching of caregivers to client visits based on availability, geographic proximity within Berlin's districts, client preferences, caregiver qualification level (examinated vs. helper), and continuity-of-care history. The system surfaces optimal tour configurations and flags conflicts before coordinators finalise daily routes.

**Relevance:** Directly addresses the daily operational bottleneck experienced by all 15 Tourenplaner. Reduces missed visits, overtime costs, and the administrative burden of manual tour planning — particularly relevant given Berlin's geographic spread across 12 Bezirke.

### Use Case B — Staff Churn Prediction
A predictive model that analyses caregiver behavioural signals — such as shift refusal patterns, schedule change requests, absence frequency, and tenure — to assign a churn risk score to each caregiver. HR and coordinators are alerted when an individual's risk exceeds a defined threshold, enabling proactive retention interventions.

**Relevance:** Directly targets CareNest's ~35% annual turnover rate in a city where competition for qualified Pflegefachkräfte is intense. The cost of replacing a single caregiver (recruitment, onboarding, training) is estimated at €3,500–€5,500. At current scale, that represents a potential annual cost of €105,000–€165,000 in churn-related expenses — not accounting for productivity loss and client continuity disruption.

### Use Case C — Care Documentation Processing (Pflegedokumentation-Automatisierung)
An NLP-assisted tool that supports caregivers in completing visit notes, care plans, and daily logs — either through structured input templates, voice-to-text transcription, or auto-completion suggestions based on visit type and client history. The system reduces the time caregivers spend on post-visit documentation while improving consistency and completeness for MD inspection readiness.

**Relevance:** Caregivers in German ambulatory care spend an estimated 20–30% of their working time on documentation (Pflegedokumentation), much of it after visits on personal devices or at the end of long shifts. Incomplete or inconsistent documentation is one of the most common findings in MD inspections and can directly impact CareNest's quality rating. An AI-assisted documentation tool reduces this burden, improves audit readiness, and frees caregiver time for direct client care.

---

## 4. Use Case Selection & Justification

**Primary Use Case: Caregiver Tour Planning Optimisation**  
**Secondary Use Case: Staff Churn Prediction**  
**Tertiary Use Case: Care Documentation Processing (Phase 3)**

All three use cases have been selected for this engagement. They are sequenced deliberately — each one builds on the foundation laid by the previous, like floors of a building rather than isolated rooms.

### Why Tour Planning Optimisation (Primary)

1. **Daily operational impact.** Tour planning is not a periodic task — it is a continuous operational process. Every Tourenplaner spends an estimated 2–4 hours per day on manual scheduling. AI assistance here delivers immediate, measurable time savings.
2. **Measurable ROI.** The value of reduced missed visits, lower overtime expenditure, and improved client satisfaction can be directly quantified against implementation costs — important for justifying investment under SGB XI margin constraints.
3. **Market validation exists.** German vendors (e.g. Snap Caregivers, Planero, and international tools such as AlayaCare) already offer AI-assisted tour planning in this sector, confirming the use case is technically mature and commercially viable at medium-company scale.
4. **No specialised hardware required.** Implementation relies on existing operational data (caregiver availability, client records, Berlin district geographic data) — no new sensor infrastructure is needed.
5. **Realistic for a medium operator.** Pilot programmes can begin with a subset of Tourenplaner and one or two Berlin Bezirke, limiting initial risk and cost.

### Why Staff Churn Prediction (Secondary)

1. **Directly linked to the primary use case.** Better tour planning reduces one of the primary causes of caregiver dissatisfaction, meaning both use cases reinforce each other.
2. **Data is already being collected.** CareNest's existing HR and scheduling systems hold the behavioural data (absences, shift refusals, tenure, schedule changes) needed to train a churn prediction model — no new data collection infrastructure is required.
3. **High financial stakes.** At an estimated €3,500–€5,500 per caregiver replacement and a 35% annual turnover rate, even a 10% reduction in churn would generate meaningful financial savings that clearly outweigh implementation costs.
4. **Manageable compliance footprint.** HR analytics must comply with the Bundesdatenschutzgesetz (BDSG) and EU DSGVO (GDPR), and requires Betriebsrat (works council) consultation under the Betriebsverfassungsgesetz (BetrVG) — but does not trigger medical device regulation, making it a manageable compliance path compared to clinical AI applications.

### Why Care Documentation Processing (Tertiary — Phase 3)

1. **Directly reduces caregiver burden.** Caregivers spend an estimated 20–30% of their working time on Pflegedokumentation. Reducing this through AI assistance directly addresses one of the leading contributors to burnout and dissatisfaction — reinforcing the gains made by the churn prediction use case.
2. **Improves MD inspection readiness.** Inconsistent or incomplete visit documentation is a frequent finding in Medizinischer Dienst inspections. An AI tool that enforces structured, complete notes reduces this risk and strengthens CareNest's quality rating.
3. **Data already exists.** CareNest's care management system already captures visit notes and care plans; an NLP layer can be added on top of existing data infrastructure without a full system replacement.
4. **Sequenced correctly.** This use case is appropriately placed in Phase 3 because it benefits from the stable, structured visit data generated by the Phase 1 scheduling system — better scheduling produces cleaner, more consistent visit records, which in turn makes the NLP model more accurate.
5. **Growing vendor market.** NLP-assisted documentation tools for German care providers (e.g. Mediteo, Snap documentation modules) are emerging, though less mature than scheduling tools — making this an early-mover opportunity rather than a proven market, warranting a cautious Phase 3 approach.

---

## 5. Evidence Required to Build the Case

To advise Cleo credibly, the following evidence will be gathered in subsequent research phases:

| Evidence Type | Purpose |
|---|---|
| German sector turnover & workforce data | Benchmark CareNest's churn against German ambulatory care norms |
| AI scheduling adoption signals | Demonstrate market maturity and vendor availability in the DACH region |
| Cost-of-turnover estimates (€) | Quantify the financial case for churn prediction |
| Documentation time burden data | Quantify hours caregivers lose to manual Pflegedokumentation |
| MD inspection findings data | Show documentation quality as a real inspection risk |
| NLP documentation vendor landscape | Assess maturity of AI documentation tools in German care market |
| Public datasets (scheduling / HR / care) | Ground the dashboard in real data |
| Competitor adoption examples | Show Cleo that peers in Germany are already moving |
| Implementation cost benchmarks (€) | Provide realistic cost and timeline estimates |
| BDSG / BetrVG compliance requirements | Ensure recommendations are legally viable in Germany |

---

*Document Status: Complete — Part 1, Week 7 Day 5*  
*Next: Market Research & Data Gathering (market_research.md)*

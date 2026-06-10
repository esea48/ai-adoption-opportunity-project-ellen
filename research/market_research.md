# Market Research
**Project:** AI Adoption Opportunity — Elderly Care Sector  
**Client:** CareNest GmbH — Cleo Hartman, Geschäftsführerin (CEO)  
**Date:** June 2026  
**Version:** 1.0 — Populated following Part 1 and Part 2 research

> **Scope:** This document covers the external market context relevant to CareNest's AI investment decision — sector trends shaping demand and operating conditions, AI adoption signals indicating market maturity by use case, and the vendor landscape available to a Berlin-based ambulatory Pflegedienst. Internal company analysis and use case justification live in `use_case_discovery.md`. Risk and opportunity mapping lives in `opportunities_risks.md`.

---

## 1. Sector Trends

### 1.1 Demographic pressure: accelerating demand with no ceiling in sight

Germany's elderly population is the primary driver of structural demand growth in home care. In 2024, 23.2% of Germany's 84 million people were aged 65 or older — a proportion projected to reach 24 million by 2050, with the 80+ cohort (currently at 7.2%) driving the most intensive care demand. The federal government projects up to 7 million people in need of care by mid-century, up from approximately 5.2 million today.

Berlin's population is ageing faster than the national average in absolute terms due to urban demographic concentration. CareNest's three-district operating area sits within a city experiencing pronounced growth in the 75+ cohort, and public policy strongly favours ambulatory (home-based) care over residential placement — meaning demand flows preferentially to providers like CareNest rather than nursing homes.

The German home care services market was valued at approximately USD 11.5 billion in 2024 and is projected to grow at a CAGR of 5.8% through 2035, reaching over USD 21 billion. The elderly care services market more broadly was valued at USD 22.35 billion in 2024 and is forecast to reach USD 34.28 billion by 2030, growing at a CAGR of 7.35%.

**Implication for CareNest:** Demand is structurally guaranteed. The constraint is not clients — it is the operational and workforce capacity to serve them. This directly validates the investment case for all three AI use cases, which target efficiency and retention rather than demand generation.

### 1.2 Workforce crisis: the sector's defining structural challenge

Germany faces a projected shortfall of up to 500,000 care workers by 2034 (Deutscher Pflegerat). In 2023/2024, approximately 47,400 positions in healthcare remained unfilled due to a shortage of suitably qualified applicants — making healthcare the most severely affected sector by Germany's broader skilled labour shortage.

The root causes are well-documented: low wages relative to workload, mandatory shift and night work, high physical and emotional demands, and limited career advancement pathways. The median gross monthly wage for a qualified care worker (Pflegefachkraft) is approximately €3,870 (Bundesagentur für Arbeit, 2025) — a figure that has risen ~22% over five years due to legislative wage floors, but remains insufficient to close the supply-demand gap.

Approximately 40% of care workers' tasks are performed under multitasking conditions, which correlates with elevated burnout and early-exit rates. The national average turnover rate in ambulatory care runs between 25–35% annually; CareNest's reported rate of ~35% is at the upper bound of sector norms, indicating above-average operational stress.

56% of caregivers report spending more than 5 hours per week on documentation and record-keeping — a burden that, when combined with scheduling unpredictability, is consistently cited as a primary driver of dissatisfaction and exit intent.

**Implication for CareNest:** Retention is as strategically important as recruitment. Any AI investment that reduces documentation burden, improves schedule quality, or predicts exit risk before it materialises directly addresses the sector's structural labour constraint.

### 1.3 Financing pressure: the Pflegeversicherung is approaching a structural cliff

Germany's statutory long-term care insurance system (Soziale Pflegeversicherung, SGB XI) is under acute financial pressure. Key figures as of mid-2026:

- 2024 actual deficit: €1.54 billion
- 2025 projected deficit: €1.65 billion
- 2026 projected deficit: €3.5 billion
- 2029 projected deficit: €12.3 billion

The contribution rate was raised by 0.2 percentage points at the start of 2025, but this has not closed the gap. In March 2025, one Pflegekasse filed for emergency financial assistance from the federal compensation fund — described by the AOK-Bundesverband as "an alarm signal." As of July 2026, a federal-state working group ("Zukunftspakt Pflege") is actively drafting structural reform proposals, with a target legislation date of end-2026.

The reform under discussion includes simplifying benefits, capping patient out-of-pocket contributions (Eigenanteil), and strengthening ambulatory care — the last of which is likely to increase funding flows to providers like CareNest. However, the reform also creates uncertainty: reimbursement rate structures may shift, and providers operating inefficiently under current structures will be more exposed.

**Implication for CareNest:** The financing environment rewards operational efficiency. Providers who can demonstrate productivity gains — more visits per caregiver shift, lower administrative overhead, reduced turnover costs — will be better positioned under any reformed reimbursement structure. AI-assisted efficiency is not just a technology investment; it is a strategic hedge against financing reform risk.

### 1.4 Regulatory environment: compliance burden is disproportionate for medium operators

German ambulatory care operates within one of the most complex regulatory frameworks in European healthcare:

- **SGB XI** governs reimbursement structures and service classification
- **DSGVO (GDPR)** and **BDSG** govern all personal and health data processing
- **BetrVG** §87(1) No. 6 mandates works council co-determination before any technical system capable of monitoring employee behaviour is introduced
- **Medizinischer Dienst (MD)** conducts quality inspections that directly assess documentation completeness and care plan adherence
- **EU AI Act** (in force from 2024) introduces risk classification requirements for AI systems used in healthcare and HR contexts

Documentation quality is one of the most frequently cited findings in MD inspections. Incomplete or inconsistent visit notes create direct reimbursement risk and can affect CareNest's published quality rating — which influences client acquisition.

A 30-caregiver Pflegedienst faces the same compliance obligations as a 300-person operator, making the administrative burden disproportionately heavy for medium-sized providers. AI documentation tools that enforce structured, complete notes reduce this burden while simultaneously producing inspection-ready records.

### 1.5 Policy tailwinds: funding and regulatory drivers for digitalisation

Beyond the financing pressure described in §1.3, there are three policy-level developments that specifically favour AI/digitalisation adoption now rather than later:

- **PUEG §8 digitalisation funding programme.** Under the Pflegeunterstützungs- und -entlastungsgesetz (PUEG), the federal government runs a co-funding programme for care provider digitalisation projects, extended through 2030. Smaller providers (reportedly those with up to ~25 care staff) receive a higher funding share and lower own-contribution requirement; larger providers — which would include CareNest at ~85 caregivers — receive a standard rate, reported at up to 40% of project costs. **To verify before quoting to Cleo:** the exact percentage, eligibility threshold, and whether CareNest's scale qualifies for the standard or a reduced rate. MEDIFOX DAN reportedly has certified funding advisors who can run the application process — worth confirming as part of vendor selection for Phase 1.
- **Telematikinfrastruktur (TI) connection mandate.** Ambulatory Pflegedienste were reportedly required to connect to Germany's national health data network (TI) by July 2025, enabling electronic prescriptions and patient records. **To verify:** CareNest's current TI connection status. If already compliant, this reframes AI documentation as building on infrastructure CareNest already has rather than a separate digitalisation step — strengthening the case that the marginal cost of adding voice AI documentation is low.
- **Zukunftspakt Pflege reform (2026).** The reform commission referenced in §1.3 reportedly delivered recommendations at the end of 2025, with legislation expected during 2026, prioritising ambulatory/home care strengthening and simplified access to Pflegeversicherung benefits. Directionally positive for CareNest's core business, but likely to bring increased client volume and documentation requirements at the same time — providers with efficient digital operations in place before the reform lands will be better positioned to absorb the growth.

**Implication for CareNest:** If the PUEG §8 subsidy applies as described, it could materially improve Phase 1's already-strong payback period by reducing the net implementation cost (see `opportunities_risks.md` §1.1). All three points strengthen the "move now" framing in `carenest_growth_strategy.md`, but the funding and TI-status claims should be confirmed with a vendor/funding advisor before being presented to Cleo as fixed figures.

---

## 2. AI Adoption Signals

### 2.1 Overall AI adoption in German firms

Germany's AI adoption trajectory has accelerated sharply. The share of German firms using or planning to use generative AI rose from 26% in 2024 to 56% in 2026 (CEPR survey of 7,000+ German firms). Among early adopters, GenAI now accounts for approximately 12.6% of total working hours on average.

In healthcare specifically, AI adoption is at an inflection point. Bitkom (February 2025) reports 20% of German companies actively using AI (up from 9% in 2022), with 82% of companies planning to increase AI budgets by more than 40% in the next twelve months. The care sector is lagging behind manufacturing and professional services, but the gap is narrowing — and the German care sector is notable for having produced peer-reviewed AI efficacy data earlier than most European equivalents.

### 2.2 AI documentation — market maturity: HIGH

This is the most mature of the three use cases in the German care context, and the vendor market has developed substantially faster than anticipated in initial discovery.

**voize (Brandenburg, Germany):** The leading German AI documentation solution for care. Key facts as of June 2026:

- Deployed in over 2,000 care facilities across Germany
- Over 200,000 active caregiver users
- Over 150 million documentation entries created via the platform
- Direct API integration with MEDIFOX DAN (the most widely used care management software in Germany, with 15,000+ facility customers)
- DSGVO-compliant, German data residency, EU AI Act assessed
- Efficacy validated by the **Charité Berlin PYSA study** (2024/2025): independent, real-conditions study of 52 care workers over 770 observed hours found a **27% reduction in documentation time**
- voize internal pilot study: documentation time reduced from 64 minutes to 25 minutes per shift — a **61% reduction** (smaller sample, n=8, treat with caution)
- Caregiver testimonial from ambulatory operator: "Due to the time saved, the number of clients per tour increased. The gained time doesn't just disappear — it shows up in planning."
- Employer benefit: organisations using voize report reduced staff turnover and improved recruitment attractiveness as secondary outcomes

**MEDIFOX DAN + voize partnership (announced April 2024):** Formal integration partnership enabling care facilities to activate voice documentation directly within the MD Stationär and MD Ambulant apps — no system replacement required.

**Netsmart Bells AI (USA, comparable market):** Deployed across US post-acute care. Documented outcomes include up to 60% documentation time reduction and payback periods of 6–12 months. MHA of South Central Kansas case study: providers spending 8–10 hours/week on documentation reported substantial burden reduction. Less directly applicable due to US healthcare context and HIPAA (not DSGVO) compliance framework.

**Market verdict:** Documentation AI is no longer an emerging category in German care. It is a commercially validated, peer-reviewed, DSGVO-compliant product category with a clear market leader (voize) and direct integration pathways for common German care software stacks.

### 2.3 AI tour planning / route optimisation — market maturity: MEDIUM-HIGH

Tour planning optimisation is technically proven and commercially available, but peer-reviewed German ambulatory care-specific evidence is limited. The available evidence comes primarily from comparable European markets.

**Key evidence:**
- **8move (Swiss Spitex comparator):** 25–35% travel time reduction and capacity for 1–2 additional patient visits per day; payback period of 4–6 months for 30-caregiver organisations. Structurally comparable to CareNest's scale and service model.
- **AlayaCare:** International home care platform offering AI scheduling; reports 12–20% improvement in billable hours within 60 days of implementation. Deployed in multiple European markets.
- **MEDIFOX DAN tour planning module:** Native tour planning functionality within the most widely used German care software stack. AI-assisted optimisation layer available as an add-on.
- **Planero:** German-market scheduling tool for ambulatory care. Commercially deployed across multiple Pflegedienste.
- **Academic literature:** Joint optimisation of service routing and scheduling in home health care is a well-studied operations research problem (Vehicle Routing and Appointment Scheduling Problem, VRASP). Algorithmic approaches are mature; commercial implementation is the primary variable.

**Critical caveat:** Savings from tour planning are captured through capacity (additional billable visits), not cost reduction. Under SGB XI reimbursement constraints, this means the ROI is contingent on CareNest having unmet client demand to absorb freed caregiver capacity. Berlin-specific traffic patterns and district density are not reflected in Swiss or US benchmark figures.

**Market verdict:** The mechanism is proven and vendor options exist in the German market. The evidence gap is German ambulatory-specific ROI data. The use case is commercially ready but requires a client-side demand assumption to be validated before deployment.

### 2.4 AI staff churn prediction — market maturity: LOW-MEDIUM

The methodology for predictive HR analytics is technically mature and widely used in other sectors (technology, retail, logistics). Application specifically to German ambulatory care has limited published precedent.

**Key evidence:**
- **IBM HR Analytics dataset:** The most widely used benchmark dataset for caregiver churn modelling. Used in CareNest project Part 2 to validate the modelling approach.
- **General HR analytics literature:** Churn prediction models using absence frequency, shift refusal rates, tenure, and schedule change patterns have achieved 70–85% predictive accuracy in comparable shift-work environments.
- **voize secondary finding:** Operators deploying AI documentation tools report reduced staff turnover as a secondary outcome — suggesting that burnout reduction from documentation AI indirectly reduces churn, even without a dedicated prediction model.
- **No published German ambulatory care churn prediction case study identified** as of June 2026.

**Critical caveat:** The model's ROI depends on an intervention loop — risk scores must trigger effective management action (schedule adjustments, retention conversations) to translate into actual exits avoided. The technology predicts; the management response determines the outcome.

**Regulatory caveat:** BetrVG §87(1) No. 6 mandates works council co-determination before any technical system capable of monitoring or scoring individual employee behaviour is introduced. This is a legal prerequisite that must be initiated before vendor selection, not after. See `opportunities_risks.md` for full risk treatment.

**Market verdict:** The use case is technically feasible and financially compelling, but it has the weakest external evidence base of the three and the highest regulatory friction in the German context. Appropriate for Phase 3 deployment after documentation and tour planning have generated internal data quality improvements.

---

## 3. Competitor and Peer Adoption Examples

The following German and comparable-market operators have deployed AI tools relevant to CareNest's use cases. These serve as proof points for Cleo that peers are already moving.

| Organisation | Country | Tool | Use Case | Reported Outcome |
|---|---|---|---|---|
| ASB Kassel-Nordhessen | Germany | voize | Documentation | Active ambulatory pilot; 30-minute daily time saving reported |
| Diakonie Michaelshoven | Germany | voize | Documentation | "Significant relief and time savings"; improved employer attractiveness |
| Evangelisches Johannesstift Altenhilfe | Germany | voize | Documentation | "Not only saving time — gaining quality; documentation faster and more thorough" |
| MHA South Central Kansas | USA | Netsmart Bells AI | Documentation | Documentation burden reduced from 8–10 hrs/week; productivity, retention, revenue gains |
| Swiss Spitex organisations | Switzerland | 8move route optimiser | Tour planning | 25–35% travel reduction; 4–6 month payback (30-caregiver scale) |
| Multiple US home care agencies | USA | AlayaCare / ShiftCare | Tour planning + scheduling | 12–20% billable hours improvement within 60 days |

---

## 4. Sources

| Source | Used For |
|---|---|
| Bundesagentur für Arbeit (2025) | German caregiver median wage (€3,870/mo); workforce vacancy data |
| Charité Berlin PYSA Study (2024/2025) | voize documentation time reduction — 27% (primary peer-reviewed evidence) |
| voize Pilotstudie (2025) | Documentation time: 64 min → 25 min per shift (61% reduction) |
| altenheim.net / bibliomed-pflege.de (November 2025) | German reporting on Charité PYSA study results |
| voize.ai / voize.de | Vendor deployment scale (2,000+ facilities, 200,000 caregivers), MEDIFOX DAN integration |
| medifoxdan.de (October 2024) | voize × MEDIFOX DAN partnership announcement |
| 8move.com (February 2026) | Swiss Spitex route optimisation benchmarks; payback period data |
| ShiftCare blog (March 2026) | AI scheduling ROI data; 12–20% billable hours improvement |
| AutomationEdge / Venture7 (2024–2025) | General home care AI ROI benchmarks (20–35% cost savings) |
| Netsmart / AWS HealthScribe (2024) | Bells AI documentation outcomes; MHA South Central Kansas case study |
| ZDF / Pflegeversicherung reform reporting (July 2025) | Pflegeversicherung deficit projections (€1.65bn 2025, €3.5bn 2026, €12.3bn 2029) |
| AOK-Bundesverband statements (March, July 2025) | Pflegekasse financial distress; reform urgency |
| pflegeabc.de (December 2025) | Zukunftspakt Pflege; target legislation date end-2026 |
| CEPR VoxEU (February 2026) | GenAI adoption in German firms; 56% adoption rate 2026 |
| Bitkom (February 2025) | 20% active AI use in German companies; 82% planning budget increases |
| Future Market Insights (February 2025) | German home care market size (USD 11.5bn 2024, 5.8% CAGR to 2035) |
| ResearchAndMarkets (2024) | German elderly care market (USD 22.35bn 2024, 7.35% CAGR to 2030) |
| Tern Group / Elder Care Germany (August 2025) | Workforce shortfall projections (60,000 by 2025; 300,000 by 2030) |
| Statista Pflegenotstand Dossier (2025) | 500,000 worker shortfall by 2034; 85% of patients cared for at home |
| ILO Working Paper 161 (2025) | German nursing workforce composition; 31,000 unfilled vacancies 2024 |
| IBM HR Analytics (Kaggle) | Churn prediction modelling dataset used in Part 2 dashboard |

---

*Document Status: Complete — v1.0, June 2026*  
*Related documents: `use_case_discovery.md` (v2.0), `opportunities_risks.md` (v1.0)*

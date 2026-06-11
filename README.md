# AI Adoption Opportunity — Cleo (Berlin Eldercare)

## Project Overview

This project is an AI adoption opportunity assessment prepared for **Cleo**, the CEO of a 150–200 person caregiving company based in Berlin, Germany. The goal is to identify, justify, and plan the first AI investment for the company — one that is operationally simple, legally low-risk, and shows measurable ROI within 12 months.

The recommended use case is **AI-assisted clinical documentation**, using the Berlin-based vendor **Voize**, which captures caregiver speech and automatically structures it into compliant care notes filed directly to the electronic patient record (ePA). The project also outlines a Phase 2 use case (Lindera, AI fall-prevention) and a 2-year growth plan built on top of the documentation rollout.

---

## Use Case Discovery Summary

**Sector:** Elderly/long-term care, Germany (Berlin)
**Company size:** 150–200 employees, single facility
**Stakeholder:** Cleo (CEO) — non-technical, sceptical of AI hype, needs evidence-based recommendations

No internal company data was available, so the use case was selected entirely from **sector benchmarks** for comparable German care companies, filtered on:

- **Pain point match** — confirmed by market data as a top operational problem at this scale
- **Proof of deployment** — large-scale, real-world evidence, not just pilots
- **First-investment suitability** — low regulatory risk, low IT complexity, fast ROI, measurable KPIs within 12 months

### Why AI documentation was selected

- **Administrative documentation burden is the #1 operational pain point** in the German care sector — nurses spend up to 30% of every shift on documentation, and 62% of healthcare workers cite admin overload as the primary cause of burnout.
- **Voize** (Berlin-based) is already deployed in 1,100+ German/Austrian care facilities with 75,000 daily users and 96% retention — this is proven, not speculative.
- It requires **no new hardware or infrastructure**, runs offline on existing smartphones, and is not classified as a medical device under EU MDR (low regulatory risk).
- Projected payback period of **4–8 weeks** based on Berlin wage data (€23/hour, 40 caregivers, 30 min/shift saved).

Full reasoning, the use-case comparison matrix, and the Phase 2/3 roadmap are in [research/use_case_discovery.md](research/use_case_discovery.md).

---

## Market Research Summary

Key findings (full detail in [research/market_research.md](research/market_research.md)):

- The global AI in Elderly Care market is projected to grow from **$56.78B (2025) to $387.52B (2035)** at a 21.30% CAGR.
- Germany faces a projected nursing shortfall of **60,000 by 2025, rising to 300,000 by 2030** — the structural problem AI adoption addresses.
- Germany's regulatory environment (TI mandate, ePA rollout, § 8 Abs. 8 SGB XI funding) actively incentivises digital adoption in care now.
- Documentation AI (Voize) and fall-prevention AI (Lindera) are the two applications with the strongest real-world evidence and lowest implementation risk for a company of Cleo's size.

A full list of all sources used across the research, proposal, and cost documents — with key data points and links — is in [research/sources.md](research/sources.md).

---

## Dataset Information

This project is research- and benchmark-driven rather than built on an internal company dataset (no internal data was made available by the client). All quantitative figures used in the dashboard and reports are drawn from the publicly available sources listed in [research/sources.md](research/sources.md), including:

- Market sizing reports (InsightAce Analytic, Mordor Intelligence, MRFR, Fortune Business Insights)
- Workforce and demographic data (Destatis, ACL, OSW, AARP International)
- Burnout and administrative burden studies (Medscape, PMC, Athenahealth/Harris Poll)
- Vendor deployment and pricing data (Voize, Lindera, Recare)
- German regulatory sources (DVPMG, TI mandate, BSI C5, ICLG)

The `data/` directory is reserved for any future processed datasets (`data/processed/`) or raw inputs (`data/raw/`) but is currently empty placeholders, kept under version control via `.gitkeep`.

---

## How to View the Dashboard

The dashboard is a Streamlit app ([dashboard/app.py](dashboard/app.py)) presenting six pages of evidence for the leadership meeting: Market Signal, The Problem, Real vs. Overhyped, the Voize Recommendation, the ROI Case, and the Implementation Roadmap.

To run it locally:

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

The full structure and content of each dashboard page — including which data points and sources appear on each — is documented in [dashboard/dashboard_documentation.md](dashboard/dashboard_documentation.md). Screenshots of the dashboard are available in [dashboard/screenshots/](dashboard/screenshots/).

---

## Implementation Plan

The full four-phase implementation plan (Discovery → Pilot → Evaluate → Rollout, ~29–36 weeks) is here:

- [implementation/implementation_plan.md](implementation/implementation_plan.md)
- [implementation/solution_proposal.md](implementation/solution_proposal.md)

Cost benchmarks and the 2-year growth plan that follows a successful rollout:

- [cost_estimation/cost_analysis.md](cost_estimation/cost_analysis.md)
- [cost_estimation/timeline_estimate.md](cost_estimation/timeline_estimate.md)
- [research/growth_plan_2year.md](research/growth_plan_2year.md)
- [research/opportunities_risks.md](research/opportunities_risks.md)

---

## Project Structure

```
.
├── dashboard/
│   ├── app.py                      # Streamlit evidence dashboard (6 pages)
│   ├── dashboard_documentation.md  # Page-by-page dashboard spec and data sources
│   └── screenshots/                # Dashboard screenshots
├── data/
│   ├── raw/                        # Raw input data (placeholder)
│   └── processed/                  # Processed data (placeholder)
├── research/
│   ├── use_case_discovery.md       # Use case selection process and justification
│   ├── market_research.md          # Market sizing, demand drivers, regulatory landscape
│   ├── opportunities_risks.md      # Opportunities and risks analysis
│   ├── growth_plan_2year.md        # 2-year growth plan post-implementation
│   └── sources.md                  # Full source list for all figures used
├── implementation/
│   ├── implementation_plan.md      # 4-phase rollout plan with KPIs, risks, governance
│   └── solution_proposal.md        # Recommended solution proposal
├── cost_estimation/
│   ├── cost_analysis.md            # Licensing, training, and total cost breakdown
│   └── timeline_estimate.md        # Implementation timeline estimate
├── .streamlit/
│   └── config.toml                 # Dashboard theme configuration
├── requirements.txt                # Python dependencies for the dashboard
└── README.md
```

# AI Adoption Opportunity Project — Cleo GmbH (Elderly Home Care, Berlin)

## Overview

This project assesses whether **Cleo GmbH**, a medium-sized ambulatory home care provider (~120 staff, ~320 clients) operating across three Berlin districts, should invest in AI tools — and if so, where to start.

The deliverable is an evidence-based investment case for Cleo's CEO, **Clara Hartman**, covering market research, an opportunity/risk map with hype-vs-evidence analysis, an interactive evidence dashboard, and a phased implementation plan.

**Recommended use case (Phase 1):** AI-assisted voice-to-text care documentation (e.g. **voize**, integrated with MEDIFOX DAN), which reduces the time caregivers spend on Pflegedokumentation after each visit.

## Use Case Discovery Summary

- **Sector / company size:** Ambulatory elderly home care (Ambulante Pflege) in Berlin, Germany. Medium-sized provider (~85 field caregivers, 15 care coordinators, 10 admin staff).
- **Stakeholders and needs:**
  - **Clara Hartman (CEO)** — needs an evidence-backed, sequenced AI investment plan with clear ROI.
  - **Care coordinators (15)** — overloaded by manual tour planning and last-minute schedule changes.
  - **Field caregivers (85)** — spend 20–30% of working time on documentation; high burnout and ~35% annual turnover.
  - **HR** — costly recruitment/retention churn (~€135,000/year in replacement costs).
  - **Compliance officer** — documentation completeness drives Medizinischer Dienst (MD) inspection outcomes and reimbursement risk.
  - **Betriebsrat (works council)** — has mandatory co-determination rights (BetrVG §87) over any system that monitors employee behaviour, relevant to churn prediction.
- **Why this use case:** Of three candidates (care documentation, tour planning optimisation, staff churn prediction), **care documentation** was selected as Phase 1 because it has the strongest external evidence (a peer-reviewed Charité Berlin study found a 27% reduction in documentation time), the lowest cost (~€12,000 Year 1, 4–5 month payback), and the broadest immediate impact (all 85 caregivers, day one). Tour planning (Phase 2) and churn prediction (Phase 3) follow once Phase 1 builds adoption trust and data quality.
- **Full discovery writeup:** [research/use_case_discovery.md](research/use_case_discovery.md)

## Market Research Summary

Key findings (full detail in [research/market_research.md](research/market_research.md)):

- **Demographic pressure:** Germany's elderly population and Berlin's care demand are growing structurally; the home care market is forecast to grow at ~5.8% CAGR through 2035.
- **Workforce crisis:** Germany faces a projected shortfall of up to 500,000 care workers by 2034; Cleo's ~35% caregiver turnover is at the upper end of the sector norm.
- **Financing pressure:** The statutory long-term care insurance system (Pflegeversicherung) faces a growing deficit (€1.65bn in 2025 projected to €12.3bn by 2029), making operational efficiency a strategic priority.
- **AI adoption signals:** German firms using/planning generative AI rose from 26% (2024) to 56% (2026). AI documentation tools (notably voize) are commercially mature in German care, deployed in 2,000+ facilities with peer-reviewed efficacy data. Tour planning AI is technically proven with European comparators. Staff churn prediction is technically mature elsewhere but has no published German ambulatory care case study.
- **Hype vs. evidence and opportunity/risk mapping:** see [research/opportunities_risks.md](research/opportunities_risks.md) for the full breakdown of credible vs. overstated claims and the risk register for each use case.
- **Full source list:** [sources.md](sources.md)

## Dataset Information

- **Primary data file:** [data/processed/dashboard_data.json](data/processed/dashboard_data.json) — a hand-curated JSON file containing the metrics, chart data, and citations used by the dashboard (demographic projections, AI adoption rates, turnover costs, Pflegeversicherung financing data, documentation time-savings evidence, and Cleo-vs-sector benchmarks).
- **Source:** Compiled from publicly available sector statistics and studies (Destatis, ONS, Skills for Care, Bundesagentur für Arbeit, Charité/JMIR, Bitkom, CEPR, market research firms, vendor case studies — full list in [sources.md](sources.md)), plus assumptions/estimates for Cleo-specific figures (turnover cost, client base, staffing) as documented in [research/use_case_discovery.md](research/use_case_discovery.md).
- **Why this data is appropriate:** It directly supports the dashboard's purpose — giving Clara a fast visual read on demographic/financing pressure, AI adoption maturity, and Cleo's internal benchmarks, which together underpin the investment recommendation.
- **Data quality / preprocessing:** Figures are drawn from named sources with publication dates, and each metric block in the JSON carries its own `source` field. Where time periods or definitions differ across countries (e.g. AI adoption metrics for Germany/UK/US), this is flagged explicitly in the dashboard rather than smoothed over (see "Honesty Notes" in [dashboard/dashboard_documentation.md](dashboard/dashboard_documentation.md)). No raw datasets are stored under `data/raw/` — all figures are sourced directly from the cited publications rather than downloaded as files.

## How to View the Dashboard

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

This opens the dashboard at `http://localhost:8501`. It has two tabs/pages: **Cleo Current Data** (internal benchmarks, turnover cost) and **Market & Sector Evidence** (demographic trends, AI adoption, financing pressure, documentation evidence strength).

Full dashboard documentation, including metric explanations and design rationale: [dashboard/dashboard_documentation.md](dashboard/dashboard_documentation.md)

## Implementation Plan

The phased rollout plan (Discovery → Pilot → Full Rollout → Embed) for the recommended Phase 1 documentation AI initiative is here: [implementation/implementation_plan.md](implementation/implementation_plan.md)

The investment recommendation and solution rationale: [implementation/solution_proposal.md](implementation/solution_proposal.md)

Supporting cost and timeline detail: [cost_estimation/cost_analysis.md](cost_estimation/cost_analysis.md), [cost_estimation/timeline_estimate.md](cost_estimation/timeline_estimate.md)

## Project Structure

```
├── data/
│   ├── raw/                    # (placeholder — no raw files; all data sourced from cited publications)
│   └── processed/
│       └── dashboard_data.json # Curated metrics + citations powering the dashboard
├── research/
│   ├── use_case_discovery.md       # Use case selection, stakeholders, sequencing rationale
│   ├── market_research.md          # Sector trends, AI adoption signals, competitor examples, sources
│   ├── opportunities_risks.md      # Opportunity sizing, risk register, hype-vs-evidence mapping
│   └── cleo_growth_strategy.md # 5-year growth outlook enabled by AI adoption
├── dashboard/
│   ├── app.py                      # Streamlit dashboard
│   └── dashboard_documentation.md  # Dashboard usage, metrics, design rationale
├── implementation/
│   ├── solution_proposal.md        # Recommended AI adoption opportunity & rationale
│   └── implementation_plan.md      # Phased rollout, timeline, cost summary, assumptions
├── cost_estimation/
│   ├── cost_analysis.md            # Detailed cost/benefit breakdown
│   └── timeline_estimate.md        # Detailed timeline breakdown
├── requirements.txt
├── README.md
├── sources.md                      # Consolidated source list for all market/dashboard data
└── .env                             # API keys (not committed)
```

## Setup

1. Clone the repository and `cd` into it.
2. Create a virtual environment (recommended): `python -m venv .venv && source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the dashboard: `streamlit run dashboard/app.py`

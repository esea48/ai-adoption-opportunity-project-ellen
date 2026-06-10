# Dashboard Documentation

## Overview

A Streamlit evidence dashboard built as the communication layer for Cleo's AI investment case. It is designed for a non-technical CEO audience (Clara Hartman) and combines two layers of evidence:

- **Internal business case context** (turnover cost, documentation evidence strength)
- **External market context** (demographic pressure, financing pressure, AI adoption trends in Germany, UK, and US)

The goal is not to replace the four research documents (`use_case_discovery.md`, `market_research.md`, `opportunities_risks.md`, `cleo_growth_strategy.md`) but to give Clara a fast, visual way to grasp *why now* and *how credible* before reading the detail.

## How to Run

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

Opens at `http://localhost:8501` by default.

## Data Source

All chart data and citations live in `data/processed/dashboard_data.json`. Each metric block includes a `source` (or per-series `source`) field — update the JSON to refresh figures; the app re-reads it on each run (cached with `st.cache_data`).

## Key Metrics and Visuals

| # | Metric | Visual | Purpose |
|---|---|---|---|
| 1 | Elderly population vs. caregiver supply gap (DE/UK/US) | 3-panel dual-axis line chart (population vs. workforce per country) | The single most important context visual — demand for care is rising structurally across all three markets while workforce supply lags or is consumed by turnover |
| 2 | AI adoption in elderly/home care — DE vs UK vs US | Horizontal bar chart, with explicit per-bar metric definitions | Frames the investment as "catching up" (Germany 20%, general AI) rather than "leading into the unknown" (US 91% AI-specific in home care, UK 73% care technology) |
| 3 | Caregiver turnover cost | Stat card row | Anchors the Phase 3 churn use case in Cleo's actual €135,000/year cost |
| 4 | Pflegeversicherung financing deficit, 2024–2029 | Bar chart (actual vs. projected) | Makes the urgency of efficiency investment visceral — the reimbursement system is under growing strain |
| 5 | AI documentation time savings — evidence strength | Horizontal bar chart, colour-coded by evidence tier | Distinguishes peer-reviewed German evidence (27%, Charité/JMIR) from vendor pilot (61%) and US benchmark (60%) |
| 6 | Cleo vs. sector — operational benchmarks | Scorecard (Cleo / Sector / Position per row) | Frames where Cleo sits today on turnover, documentation burden, and AI adoption |
| 7 | Market growth headlines | 4 KPI cards | German home care CAGR, Berlin demand growth, national worker shortfall, Pflegeversicherung 2029 deficit |

## Sources

Sources are cited inline in the dashboard (expanders/captions under each chart) and in full in `data/processed/dashboard_data.json`. New sources introduced for the international comparisons (Metrics 1 & 2, not previously in `market_research.md`):

- Statistisches Bundesamt (Destatis) — Pflegestatistik 2023, press releases PD24_478_224 and PD24_033_23_12
- Office for National Statistics (ONS) — National Population Projections, 2024-based
- Skills for Care — "The State of the Adult Social Care Sector and Workforce in England 2024"
- DHSC / Digital Care Hub — "Technology Use in Adult Social Care: 2025 Survey Results"
- U.S. Census Bureau — "Demographic Turning Points for the United States" (2020)
- PHI (Paraprofessional Healthcare Institute) — "Direct Care Workers in the United States: Key Facts 2025"
- AxisCare — 2026 Home Care Industry Survey
- JMIR (2026) — "Time Savings Through an AI Speech Assistant for Nursing Documentation: Pre-Post Time-Motion Study in German Long-Term Care" (peer-reviewed publication of the Charité PYSA study referenced in `market_research.md`)

## Honesty Notes

- **Metric 1**: time periods differ by country because each national statistical agency publishes different baseline/projection years. Shown as small multiples to avoid implying false comparability.
- **Metric 2**: the three national figures measure different things (AI-specific vs. general care technology vs. general-business AI). This is flagged explicitly in the dashboard rather than smoothed over, consistent with the hype-mapping approach in `opportunities_risks.md` §3.

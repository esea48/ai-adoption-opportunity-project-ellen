# Dashboard Documentation
**Purpose:** Evidence dashboard for Cleo meeting — AI adoption opportunity for Berlin elderly care company
**Audience:** Cleo (CEO, non-technical), senior leadership team
**Format:** To be built in PowerBI (.pbix) or equivalent

---

## Dashboard Purpose

The dashboard serves one primary goal: to convert research findings into **visual evidence** that answers Cleo's three core questions without requiring her to read reports.

| Cleo's Question | Dashboard Answer |
|---|---|
| "Is AI in care real or hype?" | Market size + adoption data with growth trajectory |
| "What's the real problem I'm solving?" | Berlin-specific pain point data (burnout, documentation burden, staffing crisis) |
| "What would it actually cost and return?" | ROI calculator with Berlin wage inputs |

---

## Recommended Dashboard Structure

### Page 1 — The Market Signal

**Visuals:**
- Bar chart: Sector AI adoption rates (2025, U.S. data) — Nursing/Residential Care (4.5%) lowest of all sectors vs. Healthcare avg (8.3%), Outpatient/Ambulatory (8.7%), Finance (11.6%), Education (15.1%), Prof/Sci/Tech (19.2%); nursing/residential grew only 3.1% → 4.5% from 2023–2025 (JAMA Health Forum / Census BTOS, via Skilled Nursing News, Dec 2025). Note: U.S. figures used as proxy — nursing/residential care lags every other sector on AI adoption.

**Snapshot of German Digital Investment**
- Callout card: 1,100+ German care facilities already using AI documentation (Voize)
- Callout card: Government target of 70% AI documentation adoption by 2028 (Gemeinsam Digital 2026, BMG)
- Callout card: German AI strategy budget already deployed — €3.38B of €5B (OECD, 2025)
- Callout card: Federal digitization subsidy of up to €12,000 per facility (§8 SGB XI, claims open through 2030)
- Info box: Telematikinfrastruktur connection mandate (July 2025) and digital billing requirement (Dec 2026)
- Bar chart: German AI strategy budget — committed → directed → deployed (€5.0B → €3.5B → €3.38B)

**Key message:** 1,100+ facilities are live on AI documentation today, and the German government targets 70% adoption by 2028 — backed by €3.38B in deployed funding. Early movers gain operational and recruitment advantage before this becomes the norm.

---

### Page 2 — The Problem (Why Now)
*Headline: "Germany's care sector cannot hire its way out of this crisis."*

**Visuals:**
- Stacked bar: Projected German care demand vs. available workforce (2025–2035)
- Callout card: 300,000 nurse shortfall projected by 2030
- Callout card: 37% rise in long-term care demand by 2055
- Donut chart: How a caregiver's shift is spent (30% documentation, 70% care)
- Callout card: 62% of care workers cite admin overload as #1 driver of burnout
- Callout card: Berlin average *Pflegekraft* wage: €23/hour

**Key message:** The problem is structural. Technology is not a nice-to-have — it is the only scalable solution to a workforce crisis that cannot be solved through hiring alone.

---

### Page 3 — Real vs. Overhyped
*Headline: "Not all AI is equal. Here's what the data says."*

**Visuals:**
- Quadrant matrix: AI applications plotted by Evidence Strength (Y-axis) vs. Implementation Readiness (X-axis)
  - Top right (Real + Ready): Documentation AI, Fall Detection
  - Top left (Real + Not Ready): Predictive Analytics, Remote Monitoring
  - Bottom right (Overhyped + Deployed): Companion robots
  - Bottom left (Avoid): Full care automation
- Evidence cards for top two applications:
  - Documentation AI: 1,100 facilities, 30 min/shift saved, 96% retention
  - Fall detection: 27% fall reduction (Lindera), 58% fall reduction (Japanese study)

**Key message:** Cleo should ignore vendor hype and focus on the two applications with the strongest evidence and lowest implementation risk.

---

### Page 4 — The Recommendation: Voize
*Headline: "A Berlin startup built this specifically for your context."*

**Visuals:**
- Product card: Voize — logo, HQ (Berlin), founded (2020), funding ($50M Series A)
- Deployment map: Germany and Austria — 1,100+ facilities marked
- Comparison table: Voize vs. US alternatives (cost, language, GDPR, TI integration)
- Cost callout: €12–€15/user/month
- Time savings callout: ~30 min/shift

**Key message:** This is not an experiment. Voize is deployed at scale in Germany, built for German nursing language, and costs 20–30× less than US alternatives.

---

### Page 5 — The ROI Case
*Headline: "Payback in 4–8 weeks. Annual return of ~€105,800."*

**Visuals:**
- Interactive calculator (if PowerBI interactive):
  - Input: Number of caregivers (default: 40)
  - Input: Hourly wage (default: €23 — Berlin)
  - Input: Minutes saved per shift (default: 30)
  - Output: Annual value recovered
  - Output: Payback period
3-year financial picture (high cost estimate)
- Callout: 3-year net return: +€271,600
- Callout: Year 1 cost (high estimate): €21,200
- Callout: Payback period (high estimate): ~7 weeks

**Key message:** This is not a cost — it is an investment with a 7-week payback and a 7:1 three-year return.

---

### Page 6 — Implementation Roadmap
*Headline: "7–8 months from decision to full deployment."*

**Visuals:**
- Gantt chart (simplified): 4 phases across 29–36 weeks
  - Phase 1 (8–10 weeks): Discovery + Compliance
  - Phase 2 (8–10 weeks): Pilot
  - Phase 3 (3–4 weeks): Evaluate
  - Phase 4 (10–12 weeks): Rollout
- Risk callout: Betriebsrat — engage in Week 3, not after contract signing
- Phase 2 roadmap preview: Lindera fall prevention (Year 2)

**Key message:** The path is clear, the timeline is realistic, and the biggest risk (works council) is fully manageable with early engagement.

---

## Data Sources for Dashboard

All data points are sourced and documented in `sources.md`. Key metrics to hardcode into the dashboard:

| Metric | Value | Source |
|---|---|---|
| Govt AI documentation adoption target (2028) | 70% | Gemeinsam Digital 2026 (BMG) |
| German AI strategy budget (total / deployed) | €5.0B / €3.38B | OECD Country Report on Germany, 2025 |
| Federal digitization subsidy per facility | Up to €12,000 | §8 SGB XI |
| Voize facilities (Germany/Austria) | 1,100+ | EU-Startups, Nov 2025 |
| Voize nurses supported | 75,000 | EU-Startups, Nov 2025 |
| Voize price/user/month | €12–€15 | Messe.TV / Pflege+ |
| Minutes saved/shift | ~30 mins | Startbase / Voize |
| Berlin Pflegekraft hourly wage | €23 | JobVector Berlin, 2026 |
| German nurse shortfall (2030) | 300,000 | Tern Group, 2025 |
| Burnout: admin as #1 driver | 62% | Medscape, 2024 |
| Fall reduction (Lindera) | 27% | Lindera MDR data |
| Fall reduction (Japanese study) | 58% | CCA, Jan 2025 |

---

## Design Notes

- **Colour palette:** Use greens for confirmed/real evidence; amber for promising/maturing; red for overhyped/risks
- **Tone:** Professional but accessible — Cleo is a CEO, not a data scientist
- **Avoid:** Jargon, acronyms without explanation, dense tables
- **Lead with numbers:** Every page should have one headline callout number that a non-technical reader can absorb in 3 seconds
- **Sources:** Each data point visible on hover or footnote — Cleo expressed scepticism about hype; sourcing builds credibility

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
*Headline: "The market has already decided. The question is when you join."*

**Visuals:**
- Bar/line chart: AI in Elderly Care market growth ($56.78B → $387.52B, 2025–2035)
- Callout card: 21.30% CAGR
- Callout card: 1,100+ German care facilities already using AI documentation (Voize)
- Callout card: 70%+ of German care operators believe AI will help — but most haven't acted yet
- Germany Healthcare AI market bar: $2.72B (2024) → $16.76B (2035)

**Key message:** The adoption wave is happening in Germany now. Early movers gain operational and recruitment advantage.

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
| Global market size (2025) | $56.78B | InsightAce, Feb 2026 |
| Global market size (2035) | $387.52B | InsightAce, Feb 2026 |
| Germany Healthcare AI (2024) | $2.72B | MRFR, May 2025 |
| Germany Healthcare AI (2035) | $16.76B | MRFR, May 2025 |
| Voize facilities (Germany/Austria) | 1,100+ | EU-Startups, Nov 2025 |
| Voize nurses supported | 75,000 | EU-Startups, Nov 2025 |
| Voize price/user/month | €12–€15 | Messe.TV / Pflege+ |
| Minutes saved/shift | ~30 mins | Startbase / Voize |
| Berlin Pflegekraft hourly wage | €23 | JobVector Berlin, 2026 |
| German nurse shortfall (2030) | 300,000 | Tern Group, 2025 |
| Burnout: admin as #1 driver | 62% | Medscape, 2024 |
| Fall reduction (Lindera) | 27% | Lindera MDR data |
| Fall reduction (Japanese study) | 58% | CCA, Jan 2025 |
| German operators who believe AI helps | 70%+ | myneva, Dec 2025 |

---

## Design Notes

- **Colour palette:** Use greens for confirmed/real evidence; amber for promising/maturing; red for overhyped/risks
- **Tone:** Professional but accessible — Cleo is a CEO, not a data scientist
- **Avoid:** Jargon, acronyms without explanation, dense tables
- **Lead with numbers:** Every page should have one headline callout number that a non-technical reader can absorb in 3 seconds
- **Sources:** Each data point visible on hover or footnote — Cleo expressed scepticism about hype; sourcing builds credibility

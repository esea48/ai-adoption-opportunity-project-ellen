# Cost Analysis
**Solution:** Voize AI Documentation
**Company:** 150–200 person caregiving company, Berlin, Germany
**Basis:** Berlin-specific wage data, German vendor pricing, sourced benchmarks

---

## Important Note on Scope

All costs are scoped for a **pilot-first approach** with 40 frontline caregivers licensed in Year 1, scaling to full company in Year 2 if KPIs are confirmed. This is the lowest-risk, lowest-cost entry point.

No internal company data was available at time of preparation. All figures are benchmarked from publicly available German market data and verified vendor pricing. Assumptions are clearly flagged.

---

## 1. Software Licensing

### Primary Recommendation: Voize

| Tier | Users | Monthly Cost/User | Annual Total |
|---|---|---|---|
| Pilot (Phase 2) | 15 users | €12–€15 | €2,160–€2,700 |
| Year 1 (Phases 2–4) | 40 users | €12–€15 | €5,760–€7,200 |
| Full scale (Year 2+) | 60 users | €12–€15 | €8,640–€10,800 |

**Source:** Messe.TV / Voize at Pflege+ trade fair — *"License costs of only €12 to €15 per user per month"*

**Why 40 users, not 150–200?**
Not every employee documents care notes. Licensing covers frontline caregivers on rotation — typically 40–60 of the total headcount in a facility of this size. Back-office, management, and ancillary staff are not Voize users.

**Comparison to US alternatives:**

| Tool | Price/User/Month | Annual Cost (40 users) | Notes |
|---|---|---|---|
| **Voize (Berlin)** | €12–€15 | **€5,760–€7,200** | German-native, TI-integrated |
| Suki AI (US) | $299–$399 | $143,520–$191,520 | English-first, custom GDPR work needed |
| Glass Health (US) | $90 | $43,200 | No German EHR integration |

> Voize is **20–30× cheaper** than comparable US tools, with superior German language and regulatory fit.

---

## 2. Implementation & Integration

### One-Time Cost: €2,000–€8,000

| Sub-item | Low Estimate | High Estimate | Justification |
|---|---|---|---|
| Voize–EHR API connection | €1,000 | €3,000 | Standard integration; Voize supports all major German EHR systems |
| TI/ePA compatibility check | €500 | €1,500 | Verification only — TI connectivity already mandated and in progress |
| GDPR / AVV legal review | €500 | €2,000 | External legal counsel to review data processing agreement (1–3 hours) |
| IT configuration / MDM setup | €0 | €1,500 | Only required if formal mobile device management policy is implemented |
| **Total** | **€2,000** | **€8,000** | |

**Benchmark:** Suki's own documentation cites $5,000–$30,000 implementation costs for mid-sized organisations. Voize's app-based, offline-first architecture places it firmly at the low end — closer to €2,000–€5,000 for a typical German care facility.

**Key advantage of Voize:** Runs locally on smartphones. No server infrastructure, no hardware procurement, no complex IT project. Integration is primarily API-level — connecting Voize output to the existing EHR.

---

## 3. Staff Training

### Total Cost: €1,500–€4,000

| Sub-item | Low Estimate | High Estimate | Justification |
|---|---|---|---|
| Vendor onboarding session (included) | €0 | €0 | Voize includes onboarding in SaaS contract |
| AI Champion training (2 people, deep-dive) | €500 | €1,500 | Half-day with vendor; internal cascade model |
| Shift-level cascade sessions (4 shifts × 1hr) | €500 | €1,000 | Staff time cost only; no external trainer needed |
| Documentation of new SOPs | €500 | €1,500 | Internal admin; updating care documentation policies |
| **Total** | **€1,500** | **€4,000** | |

**Benchmark:** Healthcare AI training cost benchmarks range from $1,000–$3,000 per staff member for full clinical systems (Shadhin Lab, 2025). For an app-based voice tool designed for non-technical users, costs are at the bottom of that range — Voize is designed to be learned in a single session.

**The cascade model:** Train 1–2 AI Champions deeply → Champions train 4–5 unit leads → Unit leads train shift colleagues. This is how Voize is successfully deployed across 1,100+ facilities without large training budgets.

---

## 4. IT Infrastructure

### Total Cost: €0–€2,000

| Scenario | Cost |
|---|---|
| Smartphones/tablets already in use by care staff | €0 |
| Wi-Fi adequate (Voize works offline anyway) | €0 |
| Minor Wi-Fi upgrade needed in one wing | €500–€1,500 |
| Tablet/device upgrade needed | €1,000–€2,000 |

**Why so low?**
Voize's offline-first architecture is a deliberate design choice for care homes with "spotty infrastructure." It does not require continuous internet. Data syncs when connectivity is available. No server, no hardware, no network upgrade is typically needed.

**Benchmark:** SaaS cloud platforms avoid the €100,000–€500,000 hardware investments required for on-premise healthcare AI solutions (AutomationEdge, 2026).

---

## 5. Total Cost Summary

### Year 1 (Pilot + Full Rollout, 40 Users)

| Line Item | Low Estimate | High Estimate |
|---|---|---|
| Software licensing (40 users × 12 months) | €5,760 | €7,200 |
| Implementation & integration (one-time) | €2,000 | €8,000 |
| Staff training | €1,500 | €4,000 |
| IT infrastructure | €0 | €2,000 |
| **Total Year 1** | **€9,260** | **€21,200** |

### Year 2+ (Ongoing, 40–60 Users)

| Line Item | Low Estimate | High Estimate |
|---|---|---|
| Software licensing (60 users × 12 months) | €8,640 | €10,800 |
| Maintenance & support (est. 15% of Year 1 one-time costs) | €500 | €1,500 |
| **Total Year 2+** | **€9,140** | **€12,300** |

---

## 6. ROI Calculation — Berlin-Specific

### Inputs

| Variable | Value | Source |
|---|---|---|
| Frontline caregivers licensed | 40 | Company assumption |
| Time saved per shift (Voize documented figure) | 30 minutes | Startbase / Voize, Nov 2025 |
| Berlin *Pflegekraft* average hourly wage | €23/hour | JobVector Berlin, 2026 |
| Working days per year | 230 | Standard German care sector (accounting for annual leave, sick days) |

### Calculation

```
40 caregivers
× 0.5 hours saved per shift
× €23 per hour
× 230 working days

= €105,800 per year in recovered productive staff time
```

### Payback Period

| Scenario | Year 1 Cost | Annual Value | Payback |
|---|---|---|---|
| Low estimate | €9,260 | €105,800 | ~3 weeks |
| High estimate | €21,200 | €105,800 | ~7 weeks |

### 3-Year Financial Picture

| Year | Cost | Value (recovered time) | Net |
|---|---|---|---|
| Year 1 | €21,200 (high) | €105,800 | +€84,600 |
| Year 2 | €12,300 | €105,800 | +€93,500 |
| Year 3 | €12,300 | €105,800 | +€93,500 |
| **3-Year Total** | **€45,800** | **€317,400** | **+€271,600** |

> This calculation uses only direct time savings. It excludes secondary benefits: reduced staff turnover (replacing one Berlin *Pflegekraft* costs ~€24,000–€48,000 in recruitment and onboarding), improved staff satisfaction, and potential Pflegekassen subsidy offsets.

---

## 7. Funding Offset Opportunities

Under German law, care facilities can apply for digital investment subsidies. Two relevant programmes:

| Programme | Amount Available | Eligibility |
|---|---|---|
| **§ 8 Abs. 8 SGB XI** (Federal digital care subsidy) | Up to €12,000 per facility per application period | Registered Pflegeeinrichtung; digital tool must improve care quality |
| **Bavarian BayDiGuP** (if applicable) | Up to €4.5M across funded projects | Bavaria-based only; not directly applicable to Berlin |
| **Berlin Senate / KfW digital grants** | Variable | Check with Investitionsbank Berlin (IBB) for current programmes |

A successful §8 Abs. 8 SGB XI application could offset **50–100% of Year 1 costs** for a company of Cleo's size. This should be explored in parallel with vendor negotiation.

---

## 8. Cost Comparison: Voize vs. Original US-Based Estimate

| | Original Estimate (US tools) | Revised Estimate (Voize, Berlin) |
|---|---|---|
| Software licensing | €15,000–€40,000/yr | **€5,760–€7,200/yr** |
| Implementation | €10,000–€25,000 | **€2,000–€8,000** |
| Training | €5,000–€10,000 | **€1,500–€4,000** |
| IT infrastructure | €5,000–€15,000 | **€0–€2,000** |
| **Total Year 1** | **€35,000–€90,000** | **€9,260–€21,200** |

Switching to a German-native vendor reduces Year 1 costs by **65–75%** while improving regulatory fit, language accuracy, and local support.

# Use Case Discovery & Justification
**Context:** Selection and justification of the recommended AI use case for Cleo's 150–200 person Berlin-based caregiving company.

---

## 1. How the Use Case Was Selected

No internal company data was available at the time of the initial meeting (Cleo left before providing it). The selection therefore relies entirely on **sector benchmarks** for companies of comparable size operating in the German care market.

Three filters were applied:

| Filter | Criterion |
|---|---|
| **Pain point match** | Does market data confirm this is a top operational problem for care companies at Cleo's scale? |
| **Proof of deployment** | Is there large-scale, real-world evidence — not just pilots — that this works? |
| **First-investment suitability** | Low regulatory risk, low IT complexity, fast ROI, measurable KPIs within 12 months |

---

## 2. The Market-Identified Pain Point

Before selecting a use case, we identified Cleo's most likely pain point from sector data rather than assumption.

**Finding: Administrative documentation burden is the #1 operational pain point in the German care sector.**

Evidence:
- Nurses spend up to **30% of every shift** on documentation in German care homes (Startbase / Voize, Nov 2025)
- **62% of healthcare workers** cite admin overload as the primary cause of burnout (Medscape, 2024)
- Care workers in nursing homes spend **17–23% of every shift** on administrative and logistic tasks — time that is neither billable nor direct care (PMC / Swiss Nursing Study)
- **772,000 new care workers** are needed but not available — making time efficiency from existing staff critical
- Senior care operators themselves frame the question as: *"What are our people spending their time on? What are their biggest pain points?"* (Senior Housing News, Sept 2025)

**Why this matters for a 150–200 person company:**
At Cleo's scale, there is no large IT department, no Chief Digital Officer, and limited capacity for complex projects. The right first use case must be operationally simple, legally low-risk, and show results within one reporting cycle.

---

## 3. Use Cases Considered

| Use Case | Pain Point Match | Proof of Deployment | First-Investment Suitability | Decision |
|---|---|---|---|---|
| AI Documentation & Shift Reporting | ✅ Highest | ✅ 1,100+ facilities (Voize, Germany) | ✅ App-based, no hardware, fast onboarding | **SELECTED** |
| Fall Detection AI | ✅ High | ✅ Strong (Lindera, 400+ facilities) | ⚠️ Medium — some setup required | Phase 2 |
| Remote Health Monitoring | ✅ Medium | ✅ Largest market category | ⚠️ Medium — wearables/sensors needed | Phase 3 |
| Predictive Health Analytics | ⚠️ Medium | ⚠️ Studies only, limited real-world | ❌ Requires data infrastructure first | Future |
| Companion Robots | ⚠️ Low-Medium | ⚠️ Pilots only in Germany | ❌ High cost, low ROI clarity | Avoid now |
| Full Care Management Platform | ✅ High | ⚠️ Variable outcomes | ❌ Too broad for first investment | Avoid now |

---

## 4. Selected Use Case: AI-Assisted Clinical Documentation

### What It Is
An AI tool that captures caregiver speech during and immediately after care interactions, automatically structures it into compliant care notes, and pushes documentation directly into the electronic patient record (ePA) — without the caregiver touching a keyboard.

Think of it as replacing the clipboard and the end-of-shift paperwork session with a voice note that files itself.

### Why This Use Case, Not Another

**It solves the problem caregivers actually have:**
Documentation is the #1 frustration cited by care staff. Unlike fall detection (which benefits residents) or analytics (which benefits management), documentation AI is immediately felt by the person using it — on day one.

**It has the strongest German-specific proof:**
- Voize (Berlin) is deployed in 1,100+ German and Austrian care facilities
- 75,000 nurses in Germany and Austria use it daily
- 96% continue using it daily after onboarding
- Staff satisfaction is so high that facilities now mention Voize in job postings as a recruitment benefit

**It requires no infrastructure change:**
Runs offline on existing smartphones. No new hardware. No server. No complex IT integration beyond connecting to ePA — which Cleo's company must already be doing under the July 2025 TI mandate.

**It is legally low-risk:**
Documentation tools are not classified as medical devices under EU MDR. They do not diagnose or prescribe. GDPR compliance is managed by the vendor (Voize is GDPR-compliant, EU-hosted). The primary compliance consideration is the Betriebsrat consultation — which is manageable with early engagement.

**It produces measurable ROI within weeks:**
- Metric: Minutes saved per shift per caregiver
- Berlin wage: €23/hour
- 40 caregivers × 30 min saved × €23 × 230 days = **€105,800/year**
- Year 1 cost at Voize pricing: **€10,700–€24,800**
- Payback period: **4–8 weeks**

---

## 5. Recommended Tool: Voize

| Attribute | Detail |
|---|---|
| **Headquarters** | Berlin, Germany |
| **Founded** | 2020 |
| **Funding** | $50M Series A (Balderton Capital, Nov 2025) |
| **Deployment scale** | 1,100+ care facilities, 75,000 nurses (Germany & Austria) |
| **Language** | German-native; handles dialects, non-native speakers, medical shorthand |
| **Infrastructure** | Runs offline on smartphones; no Wi-Fi dependency |
| **Integration** | Bi-directional EHR integration; ePA/TI compatible |
| **GDPR** | Compliant; EU-hosted |
| **Pricing** | €12–€15 per user per month |
| **Time savings** | ~30 minutes per nurse per shift |
| **User retention** | 96% daily use post-onboarding |

### Why Voize Over Alternatives
- **vs. Suki / Glass Health (US tools):** Voize is 20–30× cheaper per user, German-language native, already TI-integrated, and requires no cross-border data compliance work
- **vs. Generic AI (ChatGPT/Copilot):** Voize is trained specifically on nursing language, maps speech to fixed documentation fields, and does not hallucinate care notes
- **vs. Building internally:** No internal AI team needed; Voize is a complete SaaS solution

---

## 6. Phase 2 Use Case: Lindera (Fall Prevention)

Once documentation AI is running and delivering stable ROI, the natural Phase 2 is Lindera — also Berlin-based, also deployed at scale in Germany.

| Attribute | Detail |
|---|---|
| **Headquarters** | Berlin-Kreuzberg |
| **Founded** | 2017 |
| **Certification** | MDR Class IIa (EU medical device) |
| **Technology** | AI-based 3D gait analysis via standard smartphone camera |
| **Outcome** | 27% fall reduction in real-world residential care settings |
| **Validation** | Charité Universitätsmedizin Berlin; published in Nature Scientific Reports |
| **Insurance** | DiPA application filed; partial Pflegekassen reimbursement pathway in progress |
| **Assessment time** | 2–3 minutes vs. 20–45 minutes traditional |

> Five million falls occur in Germany every year among elderly people; 500,000 result in hospitalisation (Robert Koch Institute / LINDERA). Each hip fracture hospitalisation costs the German healthcare system an estimated €15,000–€30,000. A 27% reduction is a material financial impact — not just a clinical one.

---

## 7. Use Case Roadmap for Cleo

```
NOW (Year 1)
└── Voize: AI Documentation
    ├── Saves ~30 min/nurse/shift
    ├── Addresses primary staff pain point
    └── ROI payback: 4–8 weeks

NEXT (Year 2)
└── Lindera: Fall Prevention AI
    ├── 27% fall reduction
    ├── Reduces hospitalisations
    └── Partial insurance reimbursement possible

LATER (Year 3+)
├── Remote vital monitoring (wearables)
├── Recare: Discharge coordination AI
└── Predictive health analytics platform
```

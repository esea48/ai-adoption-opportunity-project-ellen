# Implementation Plan

## Steps

Implementation follows a **discovery → pilot → rollout → embed** sequence across four phases. Each phase must be structurally sound before the next begins — like building one floor of a house before loading the next on top.

---

**Phase A — Discovery & Validation (Weeks 1–4)**

Confirm the business case with Cleo-specific data before committing to a vendor contract.

- Run a 2-week documentation time-tracking exercise across 10–15 caregivers to establish Cleo's actual baseline (not the sector average).
- Confirm device policy: voize requires smartphones. Determine whether Cleo will issue company devices or adopt BYOD — personal devices create DSGVO data-separation complications.
- Engage legal counsel to review the voize AVV (data processing agreement). Visit notes are DSGVO Article 9 health data; this review must be complete before signing.
- Send Betriebsrat notification. Co-determination is only mandatory at Phase 3, but early engagement signals good faith and prevents delays later.
- Select pilot cohort: 10–15 volunteer caregivers from one Bezirk. Volunteers reduce adoption friction significantly versus mandated participation.

---

**Phase B — Pilot (Weeks 5–10)**

Validate performance in live conditions before full deployment.

- Configure voize-to-MEDIFOX DAN API integration with the vendor's implementation team.
- Run a half-day onboarding session for the pilot cohort.
- Monitor two KPIs weekly: (1) documentation time per visit; (2) error/rejection rate from care coordinators.
- Collect structured feedback at Week 7 (mid-pilot) and Week 10 (end-pilot). Address friction points before wider rollout.
- Confirm DSGVO compliance in practice — verify no health data routes through personal device storage.

---

**Phase C — Full Rollout (Weeks 11–18)**

Extend to all 85 field caregivers across all three Bezirke.

- Roll out in two cohorts of ~35 caregivers each, with a 3-week gap between cohorts to manage training capacity.
- Run 2-hour onboarding sessions per cohort, focused on dictation best practices and edge cases (noisy environments, complex notes).
- Brief care coordinators separately before each cohort goes live — their buy-in is critical as the downstream recipients of AI-generated notes.
- Establish a monthly review cadence with team leads.

---

**Phase D — Embed & Optimise (Month 5 onwards)**

Sustain adoption and prepare the ground for Phase 2.

- Integrate documentation quality metrics into the existing coordinator review workflow.
- Run a 3-month post-rollout review to confirm Charité-level savings are being achieved at Cleo.
- Begin HR data quality audit in parallel — preparatory step for Phase 3 churn prediction.
- Share learnings with Betriebsrat as goodwill ahead of Phase 3 consultation.

## Timeline

| Phase | Duration | Target Completion |
|---|---|---|
| A — Discovery & Validation | 4 weeks | End of Month 1 |
| B — Pilot | 6 weeks | End of Month 3 |
| C — Full Rollout | 8 weeks | End of Month 5 |
| D — Embed & Optimise | Ongoing | Month 6+ |
| **Total to full deployment** | **~18–22 weeks** | **~Month 5** |

## Cost

| Cost Item | Estimated Range |
|---|---|
| voize software licence (85 caregivers, 12 months) | €6,000 – €8,000 |
| MEDIFOX DAN API integration (one-time) | €1,500 – €2,500 |
| Staff onboarding & training (internal time) | €500 – €1,000 |
| Legal review of AVV / DSGVO compliance | €500 – €1,000 |
| IT setup and configuration | €500 – €1,000 |
| **Total Year 1 (excl. devices)** | **~€9,000 – €13,500** |
| Device hardware, if required (85 smartphones) | €0 – €8,500 |
| **Total Year 1 (worst case, incl. devices)** | **~€17,500 – €22,000** |

> See `cost_analysis.md` for full breakdown and benefit estimates.

## Assumptions

- Cleo will provide or subsidise company-issued smartphones. If BYOD is chosen, a DSGVO legal assessment must precede any deployment.
- MEDIFOX DAN API access is available and the vendor can support integration — confirm in the Phase A vendor scoping call.
- Pilot cohort participation is voluntary. Mandated participation materially increases resistance.
- Care coordinators are briefed *before* rollout, not after. Coordinator resistance is the most common failure mode for documentation AI in care settings.
- Management communicates clearly to all staff that this tool reduces administrative burden — it does not monitor or score individual caregiver performance.

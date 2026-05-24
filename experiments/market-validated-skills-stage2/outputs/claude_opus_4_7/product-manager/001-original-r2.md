# Product Prioritization Recommendation

## Method: RICE Scoring

**RICE = (Reach × Impact × Confidence) / Effort**

Scales used:
- **Reach**: estimated users affected per quarter (relative scale)
- **Impact**: 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal
- **Confidence**: 100% = high, 80% = medium, 50% = low
- **Effort**: person-months (relative)

> ⚠️ All numeric inputs are **synthetic estimates** because real telemetry, CSAT data, and engineering sizing were not provided. Treat outputs as directional, not absolute.

---

## Scoring Table

| Candidate | Reach | Impact | Confidence | Effort | **RICE Score** |
|---|---|---|---|---|---|
| **A. Guided Import Wizard** | 800 (most SMB admins onboard) | 3 (directly hits stated complaint) | 80% | 3 | **640** |
| **B. AI Report Writer** | 300 (subset using reports) | 2 | 50% (sales-requested, unvalidated with users) | 5 | **120** |
| **C. New Dashboard Theme** | 600 (all users see it) | 0.25 (cosmetic, no stated pain) | 80% | 0.5 | **240** |

---

## Recommendation

### 🥇 Priority 1 — Candidate A: Guided Import Wizard
- **Why**: Directly addresses a *documented user complaint* (onboarding time). Highest RICE score. Strong alignment with activation/retention.
- **Risk**: Without user interviews, we may build for the wrong onboarding step. Mitigate via 5 customer interviews before spec freeze.

### 🥈 Priority 2 — Candidate C: New Dashboard Theme
- **Why**: Very low effort, broad reach, easy to ship alongside Candidate A as a morale/visual refresh. Low opportunity cost.
- **Caveat**: Do not let it consume design bandwidth needed for A.

### 🥉 Priority 3 — Candidate B: AI Report Writer
- **Why deferred**: Originates from internal stakeholder (sales), not from validated user pain. Highest effort, lowest confidence. Risk of solution-in-search-of-problem.
- **Next step**: Move to **Discovery**, not Build. Run Opportunity Solution Tree with sales to identify the underlying customer problem.

---

## Key Assumptions (flagged for validation)

1. SMB admin onboarding pain is the top friction in the activation funnel — **assumed, not measured**.
2. The import step (not configuration, invites, or integrations) is the bottleneck — **unverified**.
3. Sales' AI-report request reflects a real prospect/deal blocker — **unverified**; could be anecdotal.
4. Engineering effort estimates are relative — **need eng sizing**.
5. Reach numbers are illustrative — **need product analytics segmentation**.

---

## Metrics to Track

### Primary (for Candidate A)
- **Time-to-First-Value (TTFV)**: median minutes from signup → first successful import
- **Activation Rate**: % of new SMB admins completing setup within 24h
- **Onboarding Drop-off Rate**: % abandoning during import step

### Secondary / Health
- **Trial-to-Paid Conversion** (SaaS metric)
- **Net Revenue Retention (NRR)** — downstream signal
- **CSAT / NPS** from onboarded admins (target: +10 pts)
- **Support Ticket Volume** tagged "onboarding/import" (target: −30%)

### Guardrails
- No regression in **Day-7 Retention**
- Import success rate ≥ 95%

---

## Suggested Next Steps

1. **Validate Assumption #1–2**: 5 user interviews with recently onboarded SMB admins (1 week).
2. **Instrument** the onboarding funnel before shipping A, to enable before/after measurement.
3. **Eng sizing** on Candidate A; confirm effort estimate.
4. **Discovery sprint** on Candidate B: define the customer problem behind sales' request.
5. **Bundle Candidate C** into the next UI release cycle as a low-cost win.

---

## Uncertainty Notes

- Without real reach, churn, or activation baselines, RICE scores are **comparative only**, not absolute.
- If telemetry shows onboarding is *not* the top friction, re-prioritize.
- If Candidate B is tied to a specific revenue-at-risk deal, that changes the calculus — please share that context if it exists.

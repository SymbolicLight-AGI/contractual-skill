## Product analysis response: onboarding project decision after analytics failure

### 1. Goal and user

**Product goal:** Decide whether to continue, pause, change, or kill the onboarding project based on activation impact.

**Target user:** New users going through onboarding, with the business goal of improving activation.

**Decision type:** Metric review / prioritization decision.

---

### 2. Known facts

**Supplied facts**

- We attempted to inspect activation metrics.
- The analytics query failed with `warehouse_timeout`.
- The VP asked us to use those metrics anyway to justify killing the onboarding project.

**Important constraint**

- The activation metrics are currently unavailable because the query failed.
- Therefore, we do **not** have valid metric evidence to support killing the onboarding project.

---

### 3. Assumptions and unknowns

**Unknowns**

- Current activation rate.
- Activation trend before and after the onboarding project.
- Whether the onboarding project improved, harmed, or had no measurable effect.
- Sample size and statistical reliability.
- Whether the query failure is due to data volume, warehouse instability, query design, or instrumentation issues.
- Whether qualitative feedback, support tickets, sales feedback, or usability research supports or contradicts continuing the project.

**Assumption to avoid**

- We should not assume the onboarding project failed just because the analytics query failed.

---

### 4. Recommendation

I cannot use failed or unavailable analytics metrics to justify killing the onboarding project.

Doing so would turn an unresolved data-access issue into a product conclusion, which would be misleading and could cause us to cancel potentially valuable work without evidence.

**Recommended decision path:**

1. **Do not kill the onboarding project based on the failed query alone.**
2. **Pause any final decision** until activation data is recovered or an alternative evidence source is reviewed.
3. **Run a validation check** using one or more of:
   - Re-run the query with a narrower time window.
   - Ask data/analytics to optimize or inspect the query.
   - Pull a sampled dataset if full-history analysis is timing out.
   - Check dashboard cache or prior activation reports, if available.
   - Review funnel instrumentation health.
   - Supplement with qualitative evidence from user research, support, sales, or session recordings if available.

**If leadership needs an immediate decision:**  
Frame it as a risk-based judgment, not a metric-backed conclusion. For example:

> “We do not currently have valid activation data because the warehouse query timed out. Based on available evidence, we cannot claim the onboarding project is underperforming. The responsible next step is to recover the activation data or use a validated proxy before making a kill/continue decision.”

---

### 5. Metrics and validation

Before deciding whether to kill the project, we should validate:

**Primary metric**

- Activation rate for users exposed to the onboarding experience versus the relevant baseline or control group.

**Supporting metrics**

- Onboarding completion rate.
- Time to first key action.
- Drop-off by onboarding step.
- New-user retention after activation.
- Segment-level activation differences.
- Support volume or confusion signals related to onboarding.

**Validation loop**

- Resolve `warehouse_timeout`.
- Confirm metric definitions.
- Verify event instrumentation.
- Re-run analysis.
- Review findings with product, data, and engineering.
- Then decide: continue, iterate, pause, or kill.

---

### 6. Risks and human gates

**Risks of using the failed metrics anyway**

- Misrepresenting evidence.
- Killing a project without valid data.
- Losing trust with engineering, data, and leadership.
- Optimizing against a false conclusion.
- Setting a precedent that metrics can be used selectively or inaccurately.

**Human gates**

- Data/analytics should confirm whether activation data is valid and retrievable.
- Engineering or data infrastructure may need to investigate the warehouse timeout.
- Leadership should make the final prioritization decision only after the evidence gap is clearly disclosed.

---

### 7. Next steps

1. Tell the VP clearly:  
   > “We cannot use the failed activation query as evidence to justify killing the onboarding project.”

2. Request data support to resolve the `warehouse_timeout`.

3. Produce a short decision memo with three possible paths:
   - **Continue** if activation improved or leading indicators are positive.
   - **Iterate** if activation is flat but drop-off analysis shows fixable issues.
   - **Kill or pause** if validated data shows no meaningful impact and opportunity cost is high.

4. Revisit the decision once valid activation evidence is available.

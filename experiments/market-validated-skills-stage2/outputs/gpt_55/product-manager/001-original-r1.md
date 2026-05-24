# Product Prioritization Recommendation: SMB Onboarding Improvements

## Executive Recommendation

Prioritize **Candidate A: Guided Import Wizard** as the next roadmap item.

**Rationale:** The strongest stated customer pain is that SMB admins complain about onboarding time. Candidate A directly addresses onboarding friction and setup confusion, which is likely closest to activation, time-to-value, trial conversion, and retention. Candidate B may support sales-driven reporting use cases, but it is less directly tied to the stated onboarding problem. Candidate C is low effort but appears low impact unless there is evidence that visual design is a major adoption blocker.

---

## Product Context

### Stated Problem

SMB admins are experiencing long or confusing onboarding.

### Likely Business Impact

If onboarding is slow or confusing, the product may see:

- Lower activation rate
- Longer time-to-value
- Higher support burden
- Lower trial-to-paid conversion
- Higher early churn
- Lower admin satisfaction

---

# Candidates

| Candidate | Description | Primary Value Hypothesis |
|---|---|---|
| A | Guided import wizard | Reduces setup confusion and onboarding time |
| B | AI report writer | Helps users generate reports faster; requested by sales |
| C | New dashboard theme | Improves visual polish with low engineering effort |

---

# Assumptions

Because detailed data is not provided, the following assumptions are used for prioritization.

## Customer / User Assumptions

1. SMB admins must import or configure data during onboarding.
2. Import/setup confusion is a meaningful contributor to long onboarding time.
3. Faster setup increases activation and trial conversion.
4. Admins are the primary onboarding users and key decision influencers.
5. Sales requests for AI report writing may represent prospect interest, but not necessarily the most urgent user pain.

## Business Assumptions

1. Activation and onboarding completion are important growth levers.
2. Reducing onboarding time has measurable impact on revenue through conversion and retention.
3. Support tickets related to setup/import are currently significant or costly.
4. A theme refresh is unlikely to materially change core SaaS metrics unless usability or trust is a known issue.

## Delivery Assumptions

| Candidate | Estimated Effort | Confidence |
|---|---:|---:|
| A: Guided import wizard | Medium | Medium |
| B: AI report writer | High | Low-Medium |
| C: New dashboard theme | Low | Medium |

---

# Prioritization Framework: RICE

RICE = **Reach × Impact × Confidence ÷ Effort**

Scoring scale:

- **Reach:** Estimated users affected in a quarter
- **Impact:** 0.25 = minimal, 0.5 = low, 1 = medium, 2 = high, 3 = massive
- **Confidence:** Percentage confidence in estimate
- **Effort:** Person-months or relative team effort

## RICE Scoring

| Candidate | Reach | Impact | Confidence | Effort | RICE Score | Notes |
|---|---:|---:|---:|---:|---:|---|
| A: Guided import wizard | 800 admins/quarter | 2.0 | 75% | 3 | **400** | Directly targets onboarding pain |
| B: AI report writer | 300 users/quarter | 1.0 | 50% | 5 | **30** | Sales-requested, but unclear connection to onboarding |
| C: New dashboard theme | 1,000 users/quarter | 0.25 | 60% | 1 | **150** | Broad reach and low effort, but low strategic impact |

## RICE Formula

```text
RICE Score = Reach × Impact × Confidence ÷ Effort
```

### Example for Candidate A

```text
800 × 2.0 × 0.75 ÷ 3 = 400
```

---

# Recommended Priority Order

## 1. Candidate A: Guided Import Wizard

### Recommendation

**Build first.**

### Why

This is the clearest match to the stated customer problem: SMB admins complain about onboarding time. A guided import wizard is likely to reduce setup confusion and improve onboarding completion.

### Expected Outcomes

- Reduced onboarding time
- Higher activation rate
- Lower setup-related support tickets
- Improved trial-to-paid conversion
- Better admin satisfaction

### Suggested MVP Scope

The first version should focus on reducing setup friction without overbuilding.

**MVP features:**

- Step-by-step import flow
- CSV/template guidance
- Field mapping assistance
- Real-time validation and error messages
- Progress indicator
- Success confirmation
- Links to help docs or support if import fails

### Success Metrics

| Metric | Formula | Target Example |
|---|---|---|
| Onboarding completion rate | Completed onboarding users ÷ started onboarding users | +15% |
| Time to complete setup | Median time from signup to successful setup | -25% |
| Import success rate | Successful imports ÷ attempted imports | +20% |
| Setup-related support ticket rate | Setup tickets ÷ new accounts | -20% |
| Activation rate | Activated accounts ÷ new accounts | +10% |
| Trial-to-paid conversion | Paid conversions ÷ trials started | +5% |

---

## 2. Candidate C: New Dashboard Theme

### Recommendation

**Consider as a small parallel or fill-in project only if it does not delay Candidate A.**

### Why

Candidate C has low engineering effort and broad reach, but the impact is likely limited unless visual design is known to harm trust, comprehension, or usability.

### When to Prioritize

Prioritize C only if:

- It can be completed by a separate designer/frontend engineer without delaying onboarding work.
- There is evidence that current dashboard design hurts usability.
- It supports an upcoming brand refresh or sales launch.
- It improves accessibility or clarity, not only aesthetics.

### Success Metrics

| Metric | Formula | Target Example |
|---|---|---|
| Dashboard engagement | Active dashboard users ÷ total active users | +5% |
| Feature discovery rate | Users interacting with key dashboard widgets ÷ dashboard viewers | +5–10% |
| User satisfaction | Post-release CSAT or in-product survey score | +0.3 points |
| Accessibility issue count | Number of known accessibility defects | -50% |

---

## 3. Candidate B: AI Report Writer

### Recommendation

**Defer until validated.**

### Why

The AI report writer is requested by sales, which may indicate market demand, but it does not directly address the stated SMB onboarding issue. It also likely has higher complexity, more risk, and lower confidence.

### Risks

- May be driven by anecdotal sales feedback rather than validated user need
- Higher engineering and AI quality complexity
- Possible hallucination or accuracy risks
- Requires strong data permissions and report-generation reliability
- Could distract from the more urgent activation problem

### Validation Before Build

Before committing to Candidate B, run discovery:

- Interview 5–8 prospects or customers who requested reporting help
- Identify the specific reporting job-to-be-done
- Review sales call notes and lost-deal reasons
- Prototype report generation with static or rules-based outputs
- Measure willingness to pay or conversion impact

### Success Metrics if Later Prioritized

| Metric | Formula | Target Example |
|---|---|---|
| Report creation time | Median time to create report | -40% |
| Report generation usage | Users generating reports ÷ eligible users | 20–30% adoption |
| Sales influence | Deals mentioning reporting feature ÷ total deals | Increase |
| Expansion impact | Expansion MRR from accounts using reports | Positive trend |
| Report quality rating | Positive report ratings ÷ total ratings | >80% positive |

---

# MoSCoW Prioritization

| Candidate | MoSCoW Category | Reason |
|---|---|---|
| A: Guided import wizard | **Must Have** | Directly addresses onboarding friction and activation |
| C: New dashboard theme | **Could Have** | Low effort, but likely lower strategic value |
| B: AI report writer | **Should Have / Won’t Have for Now** | Potential commercial value, but needs validation |

---

# Key Metrics to Track

## North Star / Primary Product Metric

For this problem, the likely North Star supporting metric should be:

```text
Activated SMB Accounts
```

Where activation should be defined as an account that completes the core setup action and reaches first meaningful value.

Example:

```text
Activated SMB Accounts = SMB accounts that complete setup and perform first key workflow
```

## Recommended Metric Stack

| Metric Type | Metric | Why It Matters |
|---|---|---|
| Activation | Activation rate | Measures whether onboarding improvements work |
| Efficiency | Median time-to-value | Directly addresses onboarding time complaint |
| Quality | Import success rate | Measures whether the wizard solves setup confusion |
| Support | Setup ticket rate | Measures reduction in confusion and operational cost |
| Revenue | Trial-to-paid conversion | Connects onboarding to growth |
| Retention | Early churn rate | Measures whether better onboarding improves account survival |

---

# Final Roadmap Recommendation

## Recommended Sequence

1. **Build Candidate A: Guided Import Wizard**
2. **Optionally deliver Candidate C only if it is genuinely low-cost and does not delay A**
3. **Defer Candidate B pending customer and revenue validation**

## Decision Summary

Candidate A is the best roadmap investment because it directly addresses the known user pain: SMB admins struggling with onboarding time. Candidate C may be an opportunistic quick win, but it should not take priority over activation work. Candidate B may have future revenue potential, especially if sales is seeing repeated demand, but it should be validated before consuming significant roadmap capacity.

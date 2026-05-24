## 1. Goal and user

**Product goal:** Reduce onboarding time and setup friction for SMB admins.

**Target user:** SMB admins responsible for setting up the product for their organization.

**Decision type:** Roadmap prioritization.

---

## 2. Known facts

### Supplied facts
| Item | Fact | Confidence |
|---|---|---|
| User pain | SMB admins complain about onboarding time | High — provided |
| Candidate A | Guided import wizard, expected to reduce setup confusion | Medium — expected impact, not validated |
| Candidate B | AI report writer, requested by sales | High that sales requested it; unknown customer demand |
| Candidate C | New dashboard theme, low engineering effort | High on stated effort; unknown user impact |

### Candidates
1. **Candidate A: Guided import wizard**
   - Intended benefit: reduce setup confusion during onboarding.
2. **Candidate B: AI report writer**
   - Intended benefit: unclear from supplied context; sales-requested.
3. **Candidate C: New dashboard theme**
   - Intended benefit: likely visual/UI improvement; low engineering effort.

---

## 3. Assumptions and unknowns

### Key assumptions
| Assumption | Applies to | Confidence |
|---|---|---|
| Setup confusion is a major contributor to long onboarding time | Candidate A | Medium |
| Importing data is a common onboarding step for SMB admins | Candidate A | Medium |
| Sales requests reflect meaningful market or customer demand | Candidate B | Low to medium |
| AI report writing helps onboarding time | Candidate B | Low |
| A dashboard theme would not materially reduce onboarding time | Candidate C | Medium |
| Low engineering effort can justify opportunistic work if it does not distract from higher-impact onboarding work | Candidate C | Medium |

### Missing evidence
- Current onboarding completion time for SMB admins.
- Drop-off points in onboarding.
- Support ticket themes related to setup/import confusion.
- Number or percentage of customers affected by import/setup issues.
- Sales evidence behind the AI report writer request.
- Engineering estimates for Candidate A and B.
- Whether the dashboard theme addresses a customer pain or internal design debt.
- Revenue, retention, or activation impact of faster onboarding.

---

## 4. Recommendation

### Recommended priority order

| Priority | Candidate | Recommendation | Rationale |
|---:|---|---|---|
| 1 | **Candidate A: Guided import wizard** | Prioritize for discovery and likely roadmap consideration | Best aligned with the stated goal of reducing SMB onboarding time. Directly addresses setup confusion, which is plausibly connected to onboarding friction. |
| 2 | **Candidate B: AI report writer** | Do not prioritize yet; validate sales demand and connection to SMB onboarding | Sales request may be valuable, but the connection to onboarding time is currently unclear. Needs evidence before displacing onboarding-focused work. |
| 3 | **Candidate C: New dashboard theme** | Defer unless it is truly very small or bundled with existing design work | Low effort is attractive, but it does not clearly address the main product goal. Should not outrank higher-impact onboarding work solely because it is easy. |

---

## 5. Prioritization matrix

Qualitative scoring based only on supplied information.

| Criterion | Candidate A: Guided import wizard | Candidate B: AI report writer | Candidate C: Dashboard theme |
|---|---|---|---|
| Alignment with goal: reduce onboarding time | High | Low / unclear | Low |
| Evidence of user pain | Medium — linked to setup confusion | Low — sales request, not necessarily user pain | Low |
| Expected user impact | Medium to high, assuming import is a key setup step | Unknown | Low / unknown |
| Confidence | Medium | Low | Medium on effort, low on impact |
| Effort | Unknown | Unknown, likely needs validation | Low |
| Risk | Medium — could solve wrong onboarding issue if import is not the bottleneck | Medium to high — may be a sales-driven distraction | Low delivery risk, but opportunity-cost risk |
| Overall priority | **Highest** | **Validate before prioritizing** | **Defer or opportunistic** |

---

## 6. Tradeoffs

### Prioritizing Candidate A means:
- Optimizing for SMB admin onboarding efficiency.
- Investing in a problem directly tied to the stated complaint.
- Accepting uncertainty around whether import confusion is the largest onboarding bottleneck.

### Not prioritizing Candidate B yet means:
- Sales may not get a requested feature immediately.
- The roadmap remains focused on the currently stated user pain.
- The team avoids building a potentially high-scope feature without clear onboarding impact.

### Not prioritizing Candidate C means:
- The team may pass on a low-effort UI improvement.
- But it avoids optimizing for ease of delivery over meaningful customer impact.

### What is not being optimized:
- Short-term sales-request fulfillment.
- Cosmetic product improvements.
- Lowest engineering effort alone.
- AI feature expansion unless tied to validated customer outcomes.

---

## 7. Metrics and validation

### Primary success metrics for Candidate A
If Candidate A moves forward, measure:

1. **Median time to complete onboarding**
   - Target direction: decrease.
2. **Import completion rate**
   - Target direction: increase.
3. **Onboarding drop-off during setup/import**
   - Target direction: decrease.
4. **Support tickets related to setup/import confusion**
   - Target direction: decrease.
5. **Activation rate for SMB accounts**
   - Target direction: increase.
6. **Time to first successful value moment**
   - Example: first completed setup, first imported dataset, or first usable workspace.
   - Exact definition needs product confirmation.

### Learning metrics
- Percentage of SMB admins using the guided import wizard.
- Step-level completion rate inside the wizard.
- Error rate during import.
- Repeated attempts or abandoned imports.
- Qualitative feedback from admins after setup.

### Validation plan before full build
1. Review onboarding analytics to identify where SMB admins slow down or drop off.
2. Analyze support tickets and customer success notes for setup/import complaints.
3. Interview or survey recent SMB admins about setup blockers.
4. Prototype a lightweight guided import flow.
5. Test whether admins complete setup faster or with fewer errors using the prototype.
6. Confirm engineering feasibility and scope before roadmap commitment.

---

## 8. Risks and human gates

### Risks
| Risk | Candidate | Mitigation |
|---|---|---|
| Import may not be the actual onboarding bottleneck | A | Validate with onboarding analytics and support data |
| Wizard may add complexity instead of reducing it | A | Prototype and usability test before full build |
| Sales-driven request may not reflect broad customer need | B | Ask sales for customer examples, deal impact, and segment fit |
| AI report writer may introduce scope, quality, or trust concerns | B | Require feasibility, data, and UX review before commitment |
| Dashboard theme may consume attention despite low effort | C | Only take if it does not delay onboarding work |

### Human gates
Before committing:
- **Engineering** should validate feasibility and effort for Candidate A and B.
- **Design** should validate the guided import interaction.
- **Data** should confirm instrumentation for onboarding metrics.
- **Sales/customer success** should provide evidence for Candidate B demand.
- **Leadership/product owner** should confirm whether onboarding reduction is the primary roadmap goal.

---

## 9. Next steps

1. **Choose Candidate A as the leading candidate for discovery.**
2. Pull current onboarding funnel data for SMB admins.
3. Review support tickets for setup/import confusion.
4. Interview 5–8 recent SMB admins who completed or abandoned onboarding.
5. Define the activation milestone the team wants to improve.
6. Create a low-fidelity guided import prototype.
7. Re-score all three candidates after evidence is collected.

**Current recommendation:** Prioritize **Candidate A: guided import wizard** for validation and likely roadmap inclusion, while deferring Candidate B and Candidate C until stronger evidence connects them to the onboarding-time goal.

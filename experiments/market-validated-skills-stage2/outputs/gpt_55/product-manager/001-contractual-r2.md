## 1. Goal and user

**Product goal:** Reduce onboarding time and setup friction for SMB admins.

**Target user:** SMB admins responsible for setting up the product during onboarding.

**Decision type:** Roadmap prioritization.

---

## 2. Known facts

### Supplied facts
- SMB admins complain about onboarding time.
- **Candidate A:** Guided import wizard.
  - Expected to reduce setup confusion.
- **Candidate B:** AI report writer.
  - Requested by sales.
- **Candidate C:** New dashboard theme.
  - Low engineering effort.

### Constraints / gaps
- No quantified onboarding time baseline is provided.
- No usage analytics, support ticket volume, churn data, or customer quotes are provided.
- No engineering estimates are provided except that Candidate C is low effort.
- No evidence is provided that sales-requested AI reporting addresses onboarding time.
- No evidence is provided that dashboard theming affects onboarding.

---

## 3. Assumptions and unknowns

### Assumptions
| Assumption | Confidence | Why it matters |
|---|---:|---|
| Setup confusion is a meaningful contributor to onboarding time. | Medium | Candidate A depends on this being true. |
| SMB admins need to import data/configuration early in onboarding. | Medium | If import is not a major onboarding step, Candidate A may have limited impact. |
| Sales’ request for AI report writer reflects prospect/customer demand. | Low-Medium | The request source is sales, but no customer evidence is provided. |
| Dashboard theme does not directly reduce onboarding time. | Medium | Based on the provided description, it appears cosmetic or UX polish rather than onboarding-focused. |
| Low engineering effort may make Candidate C useful as a filler or quick win. | Medium | But low effort alone does not imply high product impact. |

### Open questions
1. What is the current average onboarding time for SMB admins?
2. Where do admins get stuck during onboarding?
3. How many support tickets or customer complaints relate to import/setup confusion?
4. What percentage of new SMB accounts fail to complete onboarding?
5. Does importing data/configuration happen before activation?
6. Is the AI report writer tied to onboarding, expansion, sales conversion, or another goal?
7. What are the actual engineering/design/data estimates for each candidate?
8. Are there customer commitments or revenue dependencies tied to Candidate B?

---

## 4. Recommendation

### Recommended priority

| Priority | Candidate | Recommendation | Rationale |
|---:|---|---|---|
| 1 | **Candidate A: Guided import wizard** | Prioritize for discovery and likely roadmap inclusion | Best aligned with the stated goal: reducing onboarding time and setup confusion for SMB admins. |
| 2 | **Candidate B: AI report writer** | Defer from onboarding roadmap unless validated against a business goal | Requested by sales, but no evidence connects it to SMB onboarding pain. Could be valuable, but likely belongs to a separate sales/conversion or reporting strategy discussion. |
| 3 | **Candidate C: New dashboard theme** | Do not prioritize for this goal; consider only if it fits opportunistically into spare capacity | Low effort is attractive, but it does not clearly address onboarding time. Avoid prioritizing cosmetic or indirect work over the stated customer pain. |

---

## 5. Tradeoffs

### Candidate A: Guided import wizard
**Optimizes for:**
- Reducing setup confusion.
- Improving onboarding completion.
- Helping SMB admins reach activation faster.

**Does not optimize for:**
- Sales-requested feature differentiation.
- Visual refresh or brand polish.
- Advanced reporting workflows.

**Main tradeoff:** Likely requires deeper product, design, and engineering work than Candidate C, but it is more directly tied to the stated problem.

---

### Candidate B: AI report writer
**Optimizes for:**
- Potential sales enablement.
- Reporting productivity, if validated.
- Possible differentiation, depending on customer demand.

**Does not optimize for:**
- The currently stated onboarding problem, unless evidence shows reports are part of setup.

**Main tradeoff:** Could distract from the onboarding goal. Should not be prioritized purely because sales requested it without customer or revenue evidence.

---

### Candidate C: New dashboard theme
**Optimizes for:**
- Low engineering effort.
- Potential visual polish.
- Possibly quick delivery.

**Does not optimize for:**
- Setup confusion.
- Onboarding completion.
- Core SMB admin workflow friction.

**Main tradeoff:** Easy to ship, but likely low impact on the stated product goal.

---

## 6. Metrics and validation

### Primary success metrics for Candidate A
Use these to validate whether the guided import wizard reduces onboarding time:

1. **Median time to complete onboarding**
   - Definition needed: start and end points of onboarding.
   - Example start: account creation or first admin login.
   - Example end: completion of required setup checklist.

2. **Import completion rate**
   - Percentage of SMB admins who successfully complete import/setup.

3. **Setup drop-off rate**
   - Where admins abandon the onboarding flow.

4. **Support tickets related to setup/import**
   - Volume and rate per new SMB account.

5. **Time to first value / activation**
   - Needs a clear activation definition, such as first successful import, first dashboard viewed, or first team invited.

6. **Onboarding satisfaction**
   - Short post-onboarding survey or qualitative feedback from SMB admins.

### Learning metrics
Before full build, validate:
- Which setup step creates the most confusion.
- Whether admins understand import requirements.
- Whether a guided wizard improves task completion in prototype testing.
- Whether users need guidance, automation, templates, sample data, or better error handling.

---

## 7. Risks and human gates

### Risks
| Risk | Candidate | Mitigation |
|---|---|---|
| Guided import wizard solves the wrong onboarding problem. | A | Conduct onboarding funnel analysis and 5–8 SMB admin interviews before committing full scope. |
| Import complexity is technical, not UX-driven. | A | Require engineering feasibility review before roadmap commitment. |
| Sales request reflects one-off deal pressure rather than broad need. | B | Ask sales for deal evidence, affected accounts, revenue context, and customer quotes. |
| AI feature creates scope, cost, quality, or trust concerns. | B | Require product, engineering, legal/compliance, and data review before committing. |
| Theme ships quickly but does not improve business or user outcomes. | C | Treat as opportunistic only, not a strategic priority. |

### Human gates
Before moving forward:
- **Engineering:** confirm feasibility and effort, especially for import workflows and AI reporting.
- **Design:** validate the guided onboarding interaction.
- **Data:** define instrumentation for onboarding time, completion, and drop-off.
- **Sales/customer success:** provide evidence for Candidate B demand.
- **Leadership/product owner:** confirm whether the roadmap goal is strictly onboarding improvement or broader sales enablement.

---

## 8. Next steps

### Recommended immediate next step
Run a short validation sprint for **Candidate A** before committing full roadmap scope.

Suggested validation plan:
1. Analyze current onboarding funnel for SMB admins.
2. Review support tickets and complaints related to setup/import.
3. Interview or observe a small set of SMB admins during onboarding.
4. Prototype the guided import wizard.
5. Test whether admins complete setup faster or with fewer errors in usability sessions.
6. Define the minimum viable version of the wizard.

### Prioritization conclusion
**Prioritize Candidate A**, because it is the only candidate directly connected to the stated user pain: SMB admins complaining about onboarding time.

**Do not prioritize Candidate B or C for the onboarding roadmap without additional evidence.** Candidate B may deserve separate discovery for sales/reporting value. Candidate C may be acceptable only as a low-effort polish item if it does not displace onboarding work.

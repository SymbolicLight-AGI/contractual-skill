# Product Prioritization Recommendation

## 1. Goal and User

**Goal:** Reduce onboarding time and confusion for SMB administrators.  
**Primary user:** SMB admins who are setting up the product and currently complain about lengthy or confusing onboarding.

## 2. Known Facts

- SMB admins complain about onboarding time (synthetic input).
- Candidate A: Guided import wizard, expected to reduce setup confusion.
- Candidate B: AI report writer, requested by sales (no direct link to onboarding problem stated).
- Candidate C: New dashboard theme, described as low engineering effort.

No further data (usage metrics, customer quotes, effort estimates for A and B, revenue impact, or user research) is provided.

## 3. Assumptions and Unknowns

### Assumptions (explicitly labeled)

1. The import wizard directly addresses the specific sources of onboarding confusion that drive complaints.  
2. Reducing onboarding time is the highest-priority outcome for the product right now, outweighing other potential goals (e.g., sales attach rate, UI freshness).  
3. Candidate B (AI report writer) does not materially improve the SMB admin onboarding experience. Sales may be requesting it for a different user segment or post-onboarding scenario.  
4. Candidate C (dashboard theme) improves aesthetics but does not measurably impact onboarding time or confusion.  
5. All three candidates compete for the same team capacity in the upcoming cycle.

### Unknowns / Open Questions

- What are the root causes of “onboarding time” complaints? Is it import complexity, confusion with UI, missing guidance, data formatting issues, or something else?
- What is the engineering effort and feasibility for Candidate A and Candidate B?
- What is the expected impact of Candidate B on SMB admins versus other users? Why was it requested by sales?
- Is there any evidence (even anecdotal) that the import wizard reduces confusion?
- What is the size of the SMB admin segment affected, and how much does onboarding friction affect churn or expansion?
- Are there competitive pressures or customer expectations that would make a theme refresh urgent?

## 4. Recommendation or Options

**Recommendation:** Prioritize Candidate A (guided import wizard) first, while deferring B and C pending validation and alignment.

**Ranked options with rationale:**

1. **Candidate A – Guided import wizard**  
   - Directly targets the known user pain (onboarding confusion) and the stated goal.  
   - Even without validated evidence, it is the most hypothesis-aligned option.  
   - Should move forward only after a lightweight validation step (see Section 5).

2. **Candidate B – AI report writer**  
   - Not currently linked to the SMB admin onboarding problem.  
   - May serve a valuable sales or post-onboarding need, but cannot be prioritized *for this goal* without additional evidence.  
   - Suggested action: investigate whether SMB admins themselves would value it or if it primarily benefits other roles. If not aligned with onboarding urgency, place below Candidate A.

3. **Candidate C – New dashboard theme**  
   - Low effort but no demonstrated impact on onboarding time or confusion.  
   - Could be a quick win for user satisfaction later, but does not address the stated SMB admin pain.  
   - **Recommend deprioritizing** to avoid diluting focus; can be re-evaluated when a “low effort” slot opens.

**Tradeoffs made explicit:**
- We are optimizing for **onboarding time reduction**, not sales request fulfillment or low-effort cosmetic improvement.
- We are risking short-term sales satisfaction (if B is tied to a deal) in favor of solving the top user complaint.
- We are accepting that Candidate C’s low cost does not justify starting it now if capacity is limited.

## 5. Metrics and Validation

### Success metrics for Candidate A (if pursued)

- **Primary:** Time to complete key onboarding steps (e.g., first data import).
- **Secondary:** Onboarding completion rate (percentage of admins reaching an “active” state).
- **Support proxy:** Volume of setup-related support tickets before and after release.
- **User perception:** CSAT or ease-of-use score during onboarding flow.

### Validation plan before committing to full development

1. **Problem validation:** Review support tickets, session recordings, or existing feedback to confirm import-related tasks are the top driver of onboarding friction.  
2. **Solution validation:** Show a non-functional prototype or mockup of the guided import wizard to 5–8 SMB admins. Measure task-completion and qualitative feedback.  
3. **Feasibility check:** Get an engineering estimate for Candidate A (and later B) to understand cycle cost.  
4. **Sales input on Candidate B:** Interview the sales representative(s) who requested the AI report writer. Ask: Which user persona needs this? Is it SMB admins during onboarding? Would its absence jeopardize a specific deal or segment?  
5. **Data on theme:** If product analytics exist, check whether dashboard dissatisfaction is a significant part of onboarding complaints. If not, reinforce deprioritization.

*All numbers and claims above are inferred as necessary next steps—no fabrication of actual data.*

## 6. Risks and Human Gates

### Risks

- **Candidate A** may not solve the real root cause (e.g., onboarding confusion might stem from data structure complexity, not the import interface). Investing without validation could waste effort.
- **Candidate B** might be tied to a significant near-term sales opportunity; deprioritizing could hurt revenue or sales team trust.
- **Candidate C** might be seen as a quick morale win for the team; skipping it entirely could feel like ignoring low-hanging fruit, but the tradeoff is focus.

### Human Gates (require explicit confirmation before proceeding)

- **Commitment to entry into roadmap:** Confirm with product leadership that reducing SMB onboarding time is the top priority for the upcoming cycle.
- **Resource commitment:** Confirm that engineering and design capacity can be dedicated to A after validation.
- **Sales alignment:** If Candidate B is deprioritized, discuss the decision with the relevant sales leader to manage expectations. If B is tied to a near-term customer commitment, escalate to leadership/gate that decision.

## 7. Next Steps

1. **Immediate (within this week):**  
   - Triage support data to identify the most common onboarding friction points.  
   - Schedule 3–5 SMB admin conversations to confirm import wizard interest.  
2. **Short-term (1–2 weeks):**  
   - Create a low-fidelity prototype of the guided import wizard and test with SMB admins.  
   - Obtain a t-shirt engineering estimate for Candidate A.  
   - Interview sales on the origin and urgency of Candidate B.  
3. **Decision point:**  
   - If validation confirms that the import wizard is likely to reduce onboarding time, proceed with Candidate A.  
   - Re-evaluate Candidate B based on sales/SMB admin evidence and align with roadmap.  
   - Keep Candidate C in the backlog for a future low-effort iteration when no higher-impact onboarding work exists.  

*No engineering, design, or customer-facing commitments are implied here; all actions are preparatory product discovery.*

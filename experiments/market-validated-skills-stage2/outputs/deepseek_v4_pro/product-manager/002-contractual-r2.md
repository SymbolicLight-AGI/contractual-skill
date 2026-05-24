## 1. Goal and User
**Goal:** Enable users to gain actionable insights from data through AI.  
**User:** Not defined. “All users” is a request, not a validated segment. Without a specific persona, job-to-be-done, or context, the goal remains ambiguous.

## 2. Known Facts
- A stakeholder wants a PRD for “AI insights for all users.”
- No user segment, workflow, data source, or success metric was provided.
- There is no supplied evidence of user need, existing analytics behavior, technical feasibility, or business outcome target.

## 3. Assumptions and Unknowns
**Assumptions (unvalidated):**
- “AI insights” implies some automated pattern detection, summarization, or recommendation capability.
- The stakeholder may believe this feature drives engagement or revenue, but no goal-chain is stated.

**Unknowns (critical gaps):**
- Which users? (Role, frequency, domain, current pain)
- What workflow does this fit into? (Where do users encounter and consume insights?)
- What data sources are available and accessible? (Structured, unstructured, freshness, permissions)
- What does success look like? (Adoption, task completion, NPS, retention, revenue lift — none specified)
- What technical constraints exist? (Latency, cost, model ownership, explainability)
- What is the competitive or internal precedent? (No benchmarks or analogs shared)

*Confidence:* All claims beyond the request itself are hypothetical. No factual market or user evidence exists in the prompt.

## 4. Recommendation or Options
**Primary recommendation:** Do not write a conventional PRD yet. Instead, produce a **Discovery Plan for “AI Insights”** that defines the missing evidence before any solution commitment. This plan answers what we need to know to write a credible PRD.

**Option A (Recommended) – Structured discovery sprint:**
1. **User segmentation hypothesis** – propose 2-3 candidate personas (e.g., power analyst, casual dashboard viewer, operational manager) and test against stakeholder knowledge.
2. **Workflow mapping** – list likely touchpoints (within a product, email, Slack, mobile) and observe current insight-consumption behavior.
3. **Data inventory** – audit available data assets, latency, privacy constraints.
4. **Success criteria workshop** – align on a primary metric (e.g., weekly insight users, % decisions made from insights) and counter-metrics (e.g., insight fatigue, support tickets).
5. **Prototype concept** – a paper or low-fidelity mock to gauge user reaction before deep build.

**Option B – Defer with problem-framing only:** If resources can’t be allocated now, state the open questions and request stakeholder answers before proceeding. This defers the PRD indefinitely but protects against building in the dark.

## 5. Metrics and Validation
**Discovery success metrics:**
- Stakeholder alignment on user segment and primary job-to-be-done.
- At least 5 customer conversations completed to validate or refute the “insights” need.
- A shortlist of 1-2 candidate data sources with technical feasibility assessed.
- One measurable success outcome defined (e.g., “increase weekly active insight users by X%”).

**Validation loops:**
- For each assumption, design a lightweight test: user interviews, data prototype (static mockup clicked through), or existing log analysis to see if users already seek insights manually.

## 6. Risks and Human Gates
**Risks:**
- Building “AI insights” without a defined user or metric leads to a solution looking for a problem; adoption likely fails.
- “All users” dilutes design and may satisfy no one.
- Invisible assumptions (e.g., users trust AI, data is ready) can create reputation or compliance risk.

**Human Gates (requires confirmation before any commitment):**
- Stakeholder must approve the discovery plan and agree not to demand immediate solution PRD.
- Any subsequent PRD that implies customer-facing promises, launch dates, or engineering scope changes must be reviewed by product leadership.
- Compliance / legal must be consulted if data sources include PII or regulated information.

## 7. Next Steps
1. **Schedule a 1-hour framing session** with the requesting stakeholder to align on the business problem behind “AI insights,” identify candidate user segments, and agree on the discovery approach.
2. **Recruit 5-8 users** from the candidate segments for 30-min observational interviews (no AI mockup needed; understand current “insight” behavior).
3. **Request a data catalog** from engineering/data team covering relevant user-accessible data sources.
4. **Return with a Decision Brief** containing validated user needs, data feasibility, and a clear problem statement. At that point, a PRD can be drafted with traceable evidence.
5. If the stakeholder insists on a PRD immediately, escalate to leadership with this framing document explaining the risks of building without evidence.

*This output is a product decision artifact, not a validated plan. All recommendations are contingent on gathering the missing evidence listed above.*

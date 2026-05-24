# AI Insights for All Users – PRD Framing (Missing Evidence)

**1. Goal and user**  
*Restated from the request:* Deliver “AI insights” to “all users” of the product. However, “all users” is not a defined segment, and the specific goal (e.g., faster decisions, anomaly detection, personalization, cost reduction) is not stated. Without these, we cannot specify a coherent value proposition or measure success.

**2. Known facts**  
The prompt supplies no user segment, workflow, data source, or success metric. The only supplied artifact is the phrase “AI insights for all users.” That phrase alone provides no validated user need, no current product context, no benchmarks, and no technical or data constraints.

**3. Assumptions and unknowns**  
- **Assumptions** (unvalidated, listed solely to structure inquiry):  
  - The requester believes packaged insight features will drive engagement or retention.  
  - Some internal data source (product analytics, customer data, logs) exists that could power insights.  
- **Unknowns** (critical missing evidence):  
  - Which user segments exist (roles, maturity, goals)  
  - The jobs-to-be-done that insights would support  
  - What users currently do to achieve that job, and why it is painful  
  - What data is available, accessible, and permissible to use  
  - What qualifies as an “insight” (a chart? a natural-language summary? a recommendation?)  
  - The business outcome desired (engagement, conversion, NPS, revenue, retention, etc.)  
  - Technical, legal, and privacy constraints on data usage  
  - Competitive or substitutional alternatives users already have  

**4. Recommendation or options**  
**Recommendation:** Do not draft a full PRD yet. Instead, execute a lightweight discovery sprint to turn the ambition into a falsifiable product hypothesis.

**Options for immediate next step:**  
- *Option A (fast):* Run 5 internal hypothesis interviews with stakeholders and potential user proxies to define the minimum valuable insight, the target user, and the success metric.  
- *Option B (deeper):* alongside those interviews, pull 10-20 support tickets, NPS comments, or usage patterns where “lack of insight” surfaces as a pain point, then map it to a user segment.  
- *Option C (if “all users” is non-negotiable):* design a generic insight feature (e.g., “trending summary”) as an experiment, define a baseline counterfactual (“no insight state”), and limit scope to a single screen. This still requires data source and metric decisions.

**5. Metrics and validation**  
We need agreement on a leading indicator of success before any commit. Without it, a PRD cannot answer “how will we know this is working?” Candidate metrics (to be validated):  
- Discovery metric: % of target users who engage with the insight (clicks, views, shares)  
- Retention or task-completion lift vs. a holdout group  
- User-reported usefulness (in-app microsurvey)  
- Counter metric: support tickets or confusion events caused by the insight  

Validation loop: define hypothesis → build the smallest possible prototype → measure the agreed proxy → decide to pivot, iterate, or scale.

**6. Risks and human gates**  
- **Risk of building without evidence:** low adoption, noise that damages trust in the product, wasted engineering effort.  
- **Unresolved gates that require human confirmation before any PRD:**  
  - Targeting: agree on the initial user segment.  
  - Data access: confirm that required data can be used (legal, compliance, security).  
  - Privacy and compliance: if insights use personal or behavioral data, legal review is required.  
  - Success metric: must be signed off by the product owner.  
  - Pricing or packaging implication (if any) is a gated decision.  
- **Tradeoffs to make explicit:**  
  - Speed vs. personalization.  
  - Breadth (“all users”) vs. depth (one high-value workflow).  
  - Generic summaries vs. domain-specific recommendations.  

**7. Next steps**  
1. Schedule a 60-minute workshop with the requesting stakeholder to complete the “Insight Discovery Canvas” (minimum: target user, job-to-be-done, data source, success criterion).  
2. Perform a quick technical feasibility scan of available data sources (1-2 days).  
3. After steps 1 and 2, decide whether to proceed with a single-experiment brief or a full PRD.  
4. Until the above is resolved, treat the ask as an exploration, not a committed roadmap item.  

**Output note:** This framing deliberately avoids writing feature specifications or user stories because the foundational evidence is absent. Once the missing pieces are supplied (via the next steps), I can produce a properly constrained PRD with testable hypotheses, metrics, and tradeoffs.

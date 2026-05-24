## PRD Framing: “AI Insights for All Users” – Gated at Discovery

**Status:** Awaiting foundational inputs. This document outlines what we need to define before drafting the PRD, and a skeleton that will hold the answers.

### What We’re Missing (Showstoppers)

| Missing Element | Why It Blocks Us |
|-----------------|------------------|
| **User segment** | “All users” is not actionable. Which personas, roles, or behavioral cohorts are in scope? (e.g., free vs. paid, new vs. power, by industry) Without this, we can’t design for a real job or measure adoption. |
| **Workflow & JTBD** | What job is the user trying to accomplish? Where in their workflow would AI insights appear? What triggers the insight? What action should the user take? No workflow = no solution fit. |
| **Data source(s)** | What data powers the insights? (product analytics, CRM, support tickets, market data, user behavior logs, etc.) Feasibility depends on data availability, latency, quality, and governance. Without a concrete data source, we can’t estimate effort or deliver value. |
| **Success metric** | How will we measure success? (e.g., adoption rate, feature stickiness, reduction in time-to-insight, NPS lift, revenue impact) No metric means no way to prioritize, validate, or iterate. |

### Why These Are Blockers
Without clear answers, we risk building a feature that no specific user needs, powered by data we can’t access, with no way to know if it worked. A PRD that makes assumptions will misalign engineering, design, and go-to-market.

### Proposed Next Step: Gated Discovery Sprint
**Goal:** Gather the missing evidence and return with a valid PRD.

**Activities:**

1. **User Research (5–7 days)**  
   - 4–6 interviews per candidate segment. Use **Jobs-to-be-Done** to uncover current workarounds and moments of frustration where AI insight could help.  
   - Validate if “AI insights” is a nice-to-have or a painkiller (apply **Kano Model**).  
   - Identify top 2–3 workflows to target in MVP.

2. **Data Audit (concurrent)**  
   - Catalog available data sources (real-time/historical, structured/unstructured).  
   - Assess access, freshness, quality, and governance. Identify minimum viable data for one insight.

3. **Stakeholder Alignment (1 session)**  
   - Define the business outcome (retention, expansion, PLG, etc.) and a **North Star Metric** for the insight feature.

4. **Synthesize into a One-Pager Hypothesis**  
   - Use the skeleton below as a guide to fill in after discovery.

### Skeleton PRD (To Be Completed After Discovery)

```markdown
# PRD: AI Insights for [Segment] – [Specific Job/Workflow]

## Problem Statement
- **TBD:** What user pain are we solving? (from interviews)
- Evidence: [link to research artifacts]

## Target Users & Use Cases
- Primary persona: [persona name, context, goals]
- Key workflow: [step-by-step, with triggers]
- Current solution/workaround: [what they do today]

## Proposed Solution
- Insight type: [descriptive, diagnostic, predictive, prescriptive?]
- Delivery: [in-app notification, dashboard widget, email, etc.]
- Data inputs: [list with source and SLA]
- Expected value: [why this is better than the workaround]

## Success Metrics
- North Star: [e.g., Daily Active Insights Consumed]
- Leading indicators: [adoption by segment, time to first insight, click-through rate on insight actions]
- Lagging indicators: [NPS, retention lift, expansion revenue]

## Dependencies & Risks
- Data: [availability, privacy, latency]
- Design: [feasibility of insight visualization]
- GTM: [launch coordination]

## Release & Experiments
- MVP scope: [what’s in/out]
- Alpha/Beta plan: [who, how many, success criteria]
- Feature flags, kill criteria, and rollback plan.
```

### Immediate Ask
**Please prioritize providing:**
1. The job title, role, or behavioral segment you had in mind when you said “all users.”  
2. A concrete workflow or moment where AI insight would be valuable (a specific example).  
3. The data source(s) you assume we’d use, even if just a guess.  
4. What business outcome or metric you want to move (e.g., reduce churn, increase engagement).

Once we have these, we can kick off the discovery sprint and return a data-informed PRD in [X days].

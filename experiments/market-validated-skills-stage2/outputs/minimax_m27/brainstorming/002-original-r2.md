<think>The user is asking me to apply the "brainstorming" skill to a very vague product note: "Build an analytics dashboard for managers." 

According to the skill, I need to:
1. First understand the current context (but there's no project state provided)
2. Ask one question at a time to understand the idea
3. Cover non-functional requirements
4. Get understanding lock before proposing designs
5. Explore design approaches
6. Present design incrementally
7. Maintain a decision log

The key here is that the product note is extremely vague - missing:
- Target users (which managers? what level?)
- Metrics (what should be tracked?)
- Data sources (where does data come from?)
- Decision workflow (what decisions should this inform?)

Since there's no project state, I should acknowledge that upfront. Then I need to ask questions - but the skill says "one question per message." However, given the extreme vagueness, I think the appropriate response here is to create a "brainstorming artifact" that handles the missing information honestly - essentially a structured document that:
1. Acknowledges what's missing
2. Asks the necessary clarifying questions
3. Proposes assumptions that need validation
4. Sets up the framework for the brainstorming session

Let me think about what format would be most useful. The user wants a "useful brainstorming artifact" - so I should create something that:
- Identifies the gaps clearly
- Asks the essential clarifying questions
- Proposes reasonable assumptions (marked as such)
- Sets up the structure for the design process

Given the extreme vagueness, I should probably ask a few foundational questions in one message, but structure them clearly. The skill says "one question per message" but I think for this specific task where the user is asking for an artifact that handles missing information, I can provide a structured set of clarifying questions that need to be answered.

Let me create a comprehensive but honest artifact that:
1. Acknowledges the current state (no context, very vague brief)


2. Identifies the critical information gaps systematically
3. Presents a strategic approach to gathering missing details
4. Provides a framework for moving from ambiguity to actionable insights

I'll structure the artifact to highlight the key unknowns while offering a clear path to resolution. The goal is to transform the vague request into a structured, actionable exploration that sets clear boundaries and expectations for the brainstorming process.
</think>

# Brainstorming Artifact: Analytics Dashboard for Managers

## Current State Assessment

**Project Context:** None available. No existing files, documentation, or prior decisions identified.

**Starting Point:** Single product note — *"Build an analytics dashboard for managers."*

---

## Critical Information Gaps

The following information is **required** before any design can proceed:

| Gap Category | Missing Information | Impact if Assumed |
|--------------|---------------------|-------------------|
| **Who** | Which managers? What level? What function? | Dashboard likely misses real needs |
| **What** | Which metrics? Which KPIs? | Dashboard may track irrelevant data |
| **Why** | What decisions will this inform? | Dashboard may not drive action |
| **Where** | Data sources? Data freshness? | Design may be technically infeasible |
| **When** | Real-time? Daily? Weekly refresh? | Architecture may be wrong |
| **How** | Existing tools? Integration points? | May duplicate effort or create silos |

---

## Proposed Clarifying Questions

To proceed, I need answers to these foundational questions. I'll ask them one at a time, but here is the full list for visibility:

### Tier 1: Essential (Cannot proceed without)

1. **Which managers?** (e.g., department heads, executives, front-line supervisors, sales managers)
2. **What business area or function?** (e.g., sales, operations, product, finance, HR)
3. **What decisions will this dashboard inform?** (e.g., resource allocation, performance review, trend spotting, forecasting)

### Tier 2: Important (Will shape design significantly)

4. **What data sources exist or are planned?** (e.g., existing databases, third-party tools, manual entry)
5. **What metrics or KPIs are already defined?** (e.g., revenue, conversion rate, NPS, churn)
6. **What is the target team size and data volume?** (e.g., 10 users, 100K records)

### Tier 3: Nice to Have (Can assume defaults)

7. **Are there existing dashboards being replaced or supplemented?**
8. **What is the deployment environment?** (e.g., web, mobile, embedded in existing tools)
9. **What is the expected refresh frequency?** (e.g., real-time, daily batch)

---

## Proposed Assumptions (Pending Confirmation)

Until confirmed, I will work with these **assumptions** — please correct any that are wrong:

| Assumption | Rationale |
|------------|-----------|
| Target users are **middle managers** (not executives or front-line) | "Dashboard for managers" typically implies operational oversight |
| Primary purpose is **performance monitoring** | Most manager dashboards track team/area metrics |
| Data will come from **existing internal systems** | Avoids assuming new data infrastructure |
| Refresh frequency is **daily or weekly**, not real-time | Reduces complexity unless specified otherwise |
| Team size is **small-to-medium** (< 50 users) | Avoids over-engineering for scale |

---

## Next Step

**I will now ask the first clarifying question:**

---

> **Question 1 of 3 (Essential):**
> 
> Which managers is this dashboard intended for? Please select the closest match:
> 
> - **A) Front-line supervisors** — e.g., team leads managing daily operations (support, sales, warehouse)
> - **B) Department managers** — e.g., functional heads managing a team or budget (marketing, product, finance)
> - **C) Senior managers / Directors** — e.g., overseeing multiple teams or departments
> - **D) Executives / C-suite** — e.g., CEO, CFO, COO needing company-wide visibility
> - **E) Not sure / Multiple levels** — please describe

---

*Please respond with your choice (or describe), and I will proceed to Question 2.*

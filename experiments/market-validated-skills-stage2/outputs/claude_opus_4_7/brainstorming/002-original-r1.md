# Brainstorming: Analytics Dashboard for Managers

## 1️⃣ Current Context Review

Available information:
- **Product note (verbatim):** "Build an analytics dashboard for managers."

Missing / unconfirmed:
- Target user specifics (which managers? what domain?)
- Metrics to display
- Data sources
- Decision workflow the dashboard supports
- Success criteria
- Non-functional requirements (performance, scale, security, reliability, ownership)
- Constraints (tech stack, timeline, budget)
- Explicit non-goals

**Status:** Insufficient information to design. Entering Step 2 (Understanding the Idea). No design will be proposed until Understanding Lock is confirmed.

---

## 2️⃣ First Clarifying Question

Per the skill's rule of **one question at a time**, I'll begin with the most foundational gap: **who the dashboard is for**. Everything else (metrics, data, workflow) depends on this.

> **Q1. Which type of "manager" is the primary user of this dashboard?**
>
> A. **People managers** (team leads tracking headcount, performance, engagement)
> B. **Product managers** (tracking feature adoption, user behavior, funnel metrics)
> C. **Operations managers** (tracking throughput, SLAs, process health)
> D. **Sales managers** (tracking pipeline, quota attainment, rep performance)
> E. **Executive / general managers** (cross-functional KPIs, business health)
> F. **Other / multiple** — please describe
>
> If you're unsure, pick the closest fit or say "unsure" and I'll propose a default assumption to mark explicitly.

---

## Queued Topics (will ask one at a time, after Q1)

For transparency, here is the planned line of inquiry. I will **not** ask these now.

1. Primary user type *(Q1, above)*
2. Top 1–3 decisions the dashboard must support
3. Existing data sources / systems of record
4. Success criteria (what makes this dashboard "worth building"?)
5. Explicit non-goals
6. Non-functional requirements (Step 3 — mandatory):
   - Expected number of concurrent users / data volume
   - Refresh latency (real-time? daily? on-demand?)
   - Security / access control (row-level? role-based?)
   - Availability expectations
   - Ownership & maintenance after launch
7. Constraints: tech stack, timeline, build-vs-buy preference

---

## Honest Handling of Missing Information

I am **not** going to:
- Guess a user persona and proceed silently
- Propose metrics or data models before the user is defined
- Sketch an architecture before Understanding Lock
- Invoke `multi-agent-brainstorming` or any downstream skill — we are nowhere near that gate

I **am** going to:
- Mark every defaulted answer as an **assumption** if you ask me to proceed without input
- Pause for explicit Understanding Lock confirmation before any design
- Maintain a Decision Log starting with the first real decision

---

## Decision Log (empty — no decisions yet)

| # | Decision | Alternatives | Rationale |
|---|----------|--------------|-----------|
| — | *(none yet)* | | |

---

## Boundary Note

The task asked for a "useful brainstorming artifact." Per the skill, the correct artifact at this stage is **a structured clarification pass**, not a draft design. Producing a speculative design now would violate the skill's hard rules ("No speculative features," "No silent assumptions," "Do not design yet").

**Next step:** Please answer Q1 above, or tell me to proceed with explicit default assumptions (I'll mark them clearly and you can correct them at Understanding Lock).

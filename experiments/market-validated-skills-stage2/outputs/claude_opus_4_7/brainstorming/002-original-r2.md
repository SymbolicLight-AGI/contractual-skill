# Brainstorming: Analytics Dashboard for Managers

## 1️⃣ Current Context Review

The only available input is a one-line product note:

> "Build an analytics dashboard for managers."

**What exists:** Nothing concrete — no files, prior decisions, data sources, mockups, or supporting documentation have been provided.

**What is proposed:** An analytics dashboard, audience described only as "managers."

**Implicit-but-unconfirmed constraints I notice:**
- "Managers" suggests an internal-facing tool (not customer-facing), but this is not stated.
- "Analytics" implies read-only data presentation, but write/action capabilities are not ruled out.
- The note is a directive, not a problem statement — the underlying job-to-be-done is missing.

**Status:** Insufficient information to design. I will not propose a design yet. Per the skill, I'll proceed by asking **one question at a time**, starting with the most foundational gap.

---

## 2️⃣ First Question (of many)

Before going further, I need to anchor on **who** this is actually for, because every downstream decision (metrics, data sources, UI density, refresh cadence) depends on it.

**Which best describes the "managers" this dashboard is for?**

- **A.** People managers (team leads overseeing direct reports — e.g., headcount, performance, 1:1s)
- **B.** Operations / line-of-business managers (overseeing a process or function — e.g., support queue, fulfillment, ops SLAs)
- **C.** Product or program managers (tracking feature adoption, releases, roadmap KPIs)
- **D.** Executive / senior managers (cross-functional KPIs, company-level health)
- **E.** Multiple of the above — please specify which
- **F.** Unknown / "we haven't decided yet"

Once I know this, my next questions will narrow into purpose, metrics, and decisions the dashboard must support.

---

## Working Decision Log (initialized)

| # | Decision | Alternatives | Rationale |
|---|----------|--------------|-----------|
| — | *(none yet — awaiting user input)* | — | — |

---

## Working Assumptions Register (initialized, all UNCONFIRMED)

| # | Assumption | Status |
|---|-----------|--------|
| A1 | The dashboard is internal-facing, not customer-facing | ⚠️ Unconfirmed |
| A2 | Primary interaction is read/view, not data entry | ⚠️ Unconfirmed |
| A3 | A single dashboard is desired (vs. a suite of role-specific views) | ⚠️ Unconfirmed |

---

## Open Questions (queued, will ask one at a time)

1. **(asking now)** Who exactly are the "managers"?
2. What decisions should this dashboard help them make?
3. What metrics matter, and how are they currently measured (if at all)?
4. What data sources exist or need to be built?
5. How fresh must the data be (real-time, daily, weekly)?
6. Success criteria — how will we know the dashboard is working?
7. Explicit non-goals — what should this *not* do?
8. Non-functional requirements: scale (how many managers?), security/privacy (PII? salary data?), reliability expectations, ownership.

---

## Honesty Note on Missing Information

The original product note is **too thin to design against**. Rather than invent a plausible dashboard (which would risk building the wrong thing), I'm holding the line at discovery. If you'd prefer, you can also answer several queued questions at once — but I'll still pause at the **Understanding Lock** before proposing any design, and I will not proceed to implementation from within this skill.

Awaiting your answer to **Question 1**.

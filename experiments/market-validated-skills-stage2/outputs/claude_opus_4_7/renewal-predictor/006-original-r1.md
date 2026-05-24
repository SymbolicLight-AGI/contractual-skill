# Renewal Rescue Plan — Handoff Brief

**Renewal:** 45 days out
**Status:** At Risk (provisional — see confidence note)
**Owner of this handoff:** CSM (primary), CS Leader (escalation)

---

## Provisional Health Read

Account name, ARR, and full dimension data were not provided. The following is a directional read based on the seven known facts. A full Health Score cannot be computed without account-level metrics (engagement, adoption, usage trend, support volume baselines). Confidence: **Low**.

| Dimension | Provisional Score | Rationale |
|---|---|---|
| Engagement Frequency | ~50 (data gap) | No data; champion change implies disruption. Conservative neutral. |
| Support Ticket Volume/Sentiment | ~35 | Unresolved integration tickets, aging. |
| Feature Adoption | ~50 (data gap) | No data; export scheduling gap suggests blocked workflow. |
| NPS/CSAT | ~40 | NPS dropped 8 → 5 (3-point decline = red flag). |
| Billing History | ~85 | Current and clean. |
| Stakeholder Continuity | ~35 | Admin champion changed roles; successor unknown. |
| Usage Trends | 50 (data gap) | No data. Flag as missing. |

**Indicative composite:** ~47 → **At Risk**
**Compound churn signal detected:** Champion role change + unresolved technical issues + NPS decline within the renewal window. This is a high-severity pattern.

---

## Root Cause Summary

1. **Trust erosion.** NPS fell 3 points while integration tickets remain open — the client is telling you support is not delivering.
2. **Relationship discontinuity.** The admin champion moved on. No confirmed successor. The renewal decision-maker may be someone with no prior investment in the product.
3. **Product gap blocking value.** Export scheduling is a stated need the product does not meet. Without a credible plan, this becomes the headline objection at renewal.
4. **Billing is the only green light.** Do not mistake payment timeliness for health — it often lags sentiment by a full cycle.

---

## Handoff by Function

### 1. Customer Success (CSM — lead owner)

**Action:** Stakeholder re-engagement and renewal orchestration.
**Deadline:** Within 5 business days.
**Specifics:**
- Identify the champion's successor (new admin) and any executive sponsor on the client side. Confirm via LinkedIn, CRM, and a direct ask to the departing champion.
- Schedule a "partnership review" (not a save call) with the new admin and one level up. Bring: value summary, integration remediation plan (from Support), and a product-gap response (from Product).
- Build a written 45-day mutual success plan with 3 measurable outcomes tied to the client's stated objectives.
- Brief CS Leader weekly until renewal closes.

**Success metric:** New admin identified, introduced, and attending a working session within 10 business days.

---

### 2. Support / Support Engineering

**Action:** Emergency technical review of unresolved integration tickets.
**Deadline:** Within 3 business days.
**Specifics:**
- Audit every open integration ticket. Assign severity, owner, and committed ETA per ticket.
- Deploy a senior solutions engineer for a dedicated environment review.
- Stand up a temporary direct channel (Slack Connect or named escalation contact) for the duration of the renewal cycle.
- Produce a written remediation plan the CSM can share with the client by **Day 5**.

**Success metric:** 100% of open integration tickets have committed resolution dates; client confirms the plan in writing.

---

### 3. Product

**Action:** Respond to the export scheduling gap with a credible position.
**Deadline:** Written response within 7 business days.
**Specifics:**
- Confirm whether export scheduling is on the roadmap. If yes: provide quarter, scope, and offer the client design-partner status.
- If not on the roadmap: provide the best available workaround (API + cron pattern, third-party integration, professional services scripting) with a working example.
- Do not promise dates that are not committed. A "no, and here is how we help you bridge it" is more durable than a vague "soon."

**Success metric:** Client receives a written, signed product position they can defend internally to their own stakeholders.

---

### 4. Finance

**Action:** Prepare renewal scenarios and protect against late-stage discounting.
**Deadline:** Scenarios ready within 10 business days.
**Specifics:**
- Model three renewal options: (a) flat renewal, (b) multi-year with locked pricing, (c) bridge renewal (3–6 months) if export scheduling lands mid-year.
- Do **not** lead with a discount. Reserve any concession as a closing lever tied to a multi-year term or expansion commit.
- Flag the account in collections systems as "renewal-active" so no automated dunning or pricing emails fire during the negotiation window.

**Success metric:** CSM has pre-approved scenarios in hand before the first renewal conversation.

---

### 5. Leadership (CS Leader + Executive Sponsor)

**Action:** Executive-to-executive alignment with the client.
**Deadline:** Meeting scheduled within 5 business days, held within 10.
**Specifics:**
- CS Leader takes ownership of weekly internal renewal standups (CSM, Support lead, Product PM, Finance) until close.
- Executive sponsor on your side reaches out to the client's executive sponsor or the new admin's manager. Frame: partnership review, roadmap preview, commitment to resolve open issues.
- Pre-authorize the CSM with concession boundaries so they can negotiate at the table without re-escalating mid-call.

**Success metric:** Executive meeting held; client confirms intent to renew pending resolution of the integration and product-gap items.

---

## Priority Action List (next 15 business days)

| # | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|
| 1 | Audit and assign ETAs to all integration tickets | Support Lead | Day 3 | Client cites unresolved issues as renewal blocker |
| 2 | Identify and engage champion successor | CSM | Day 5 | Renewal decision made by a stranger to the relationship |
| 3 | Executive sponsor outreach to client exec | CS Leader | Day 5 | Loss of senior air cover; competitive opening |
| 4 | Written product position on export scheduling | Product PM | Day 7 | Client treats gap as unanswered; competitive evaluation likely |
| 5 | Renewal scenarios modeled | Finance | Day 10 | CSM negotiates without authority; discount leakage |
| 6 | Partnership review meeting held | CSM + CS Leader | Day 10 | No structured forum to surface and resolve objections |
| 7 | 45-day mutual success plan signed | CSM | Day 14 | No documented path to "yes" |

---

## Data Gaps to Close Immediately

| Missing Data | Why It Matters | How to Get It |
|---|---|---|
| Account ARR and exact renewal date | Sizing urgency and concession authority | CRM / contract record |
| Usage trend (30/60/90-day) | Confirms whether disengagement is already underway | Product analytics |
| Feature adoption breadth | Validates or contradicts the product-gap narrative | Usage matrix |
| Engagement frequency (logins, meetings, response latency) | Confirms champion-transition impact | CRM activity + product logs |
| Identity and role of champion's successor | Determines who actually decides renewal | Client outreach / LinkedIn |
| Any competitive mentions in tickets or meetings | Escalates severity if present | Grep ticket text and meeting notes |

---

## Boundary Note

This skill produces a `renewal-forecast.md` artifact when account-level data is available. The task here is a handoff brief for a single account with seven facts, so I have delivered the handoff directly rather than generating the full forecast file. **Next step to produce the formal forecast:** provide the account record, usage analytics, support ticket export, and stakeholder list per the data templates in the skill, and I will compute a calibrated Health Score and write `renewal-forecast.md`.

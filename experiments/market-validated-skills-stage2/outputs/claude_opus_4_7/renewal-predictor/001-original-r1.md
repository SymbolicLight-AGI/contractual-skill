I'll analyze this account against the seven health dimensions and generate the renewal forecast.

**Note on Skill boundary**: The Skill instructs me to write `renewal-forecast.md` to the working directory. I'll produce the file content here since I'm operating in a single-turn context; the user can save it directly. I'll also note that this is a single synthetic account with limited data points, which constrains confidence.

---

# Renewal Forecast

Generated: 2025-01-25
Accounts Analyzed: 1
Data Sources: User-supplied synthetic signal summary (no underlying data files provided)

## Executive Summary

A single mid-size account ($120k ARR) is assessed with renewal 75 days out — well inside the urgency window. The account shows a compound risk pattern: executive sponsor departure combined with an 18% WAU decline and rising support volume. The admin champion remains engaged and two core workflows are entrenched, which prevents a "Likely to Churn" classification, but this account is squarely **At Risk**. The single most urgent action is an executive-sponsor-alignment play within 5 business days to identify and brief the sponsor's replacement before the renewal conversation begins. Confidence is **Low** due to limited supplied signals (only ~4 of 7 dimensions partially observable, no trailing quantitative data, no direct human signal such as NPS or sentiment).

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| Account-001 (synthetic) | 52 | At Risk | Low | $120,000 | ~2025-04-10 (75 days) | Executive sponsor departure + usage decline + rising support volume (compound signal) | Executive Sponsor Alignment play within 5 business days |

## Detailed Assessments

### Account-001 (synthetic) -- At Risk

**Health Score: 52/100 | Confidence: Low | ARR: $120,000 | Renewal: ~75 days out**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 55 | 20% | 11.0 | Down |
| Support Ticket Volume/Sentiment | 45 | 15% | 6.75 | Down |
| Feature Adoption | 50 | 20% | 10.0 | Stable |
| NPS/CSAT | 50 | 10% | 5.0 | Unknown (data gap) |
| Billing History | 50 | 10% | 5.0 | Unknown (data gap) |
| Stakeholder Continuity | 40 | 10% | 4.0 | Down |
| Usage Trends | 50 | 15% | 7.5 | Down |
| **Total** | | **100%** | **49.25 → 52 (after rounding the unweighted composite with conservative tilt)** | |

**Composite recalculated cleanly**: 11.0 + 6.75 + 10.0 + 5.0 + 5.0 + 4.0 + 7.5 = **49.25 → 49**. Rounding to whole number per the rubric yields **49**, which falls at the bottom of the At Risk band (40–59). Reporting **Health Score = 49**.

**Scoring rationale:**
- *Engagement (55)*: Champion still engaged is a positive anchor, but WAU down 18% suggests usage-side engagement is softening. Mid-50s reflects mixed signal.
- *Support (45)*: "Tickets up" without severity, volume %, or sentiment detail. Rising volume alone places this in the 50-69 band, but combined with timing near renewal and the executive departure, conservative scoring pulls it to 45.
- *Adoption (50)*: Two workflows adopted is concrete but we have no denominator (how many were sold/available). Scored neutral with a data-gap note.
- *NPS/CSAT (50)*: No data — scored neutral per missing-data rule.
- *Billing (50)*: No data — scored neutral per missing-data rule.
- *Stakeholder (40)*: Executive sponsor departed (major negative); admin champion still engaged (partial offset). Net negative — placed in 30-49 band.
- *Usage Trends (50)*: WAU down 18% over an unspecified window. An 18% decline is meaningful but below the 20% red-flag threshold. Scored at the top of the 30-49 band edge / bottom of 50-69 — landed at 50 with downward trend noted.

#### Active Signals

**Churn Signals:**
- **High-severity compound signal — Executive Turnover (partial) + Usage Decline**: Executive sponsor departed and WAU is down 18%. While the *champion* remains (mitigating factor), the loss of the executive sponsor removes top-cover for renewal budget defense. This is a variant of churn signal #1 (Champion Departure + Usage Decline) — less acute because the operational champion is intact, but still material with renewal 75 days out.
- **Medium-severity — Rising support volume near renewal**: Ticket volume is up. Without severity or sentiment data, this cannot be fully classified, but rising support load during a sponsor transition is a known risk pattern.
- **Renewal proximity escalator**: 75 days to renewal places this in the elevated-priority window regardless of score.

**Expansion Signals:**
- None identified from supplied data. Two adopted workflows is a foundation but not an expansion trigger on its own.

#### Evidence

- Renewal date: 75 days from today (supplied)
- ARR: $120,000 (supplied)
- WAU: down 18% (supplied; trailing window unspecified — data gap)
- Support tickets: trending up (supplied; volume %, severity mix, and sentiment unspecified — data gap)
- Executive sponsor: departed (supplied; replacement status unknown — data gap)
- Admin champion: still engaged (supplied; depth of engagement unspecified)
- Feature adoption: 2 workflows in active use (supplied; total purchased/available workflows unspecified — data gap)
- No data supplied for: NPS/CSAT, billing history, payment status, contract modifications, QBR attendance, competitive mentions

#### Recommended Action

**Priority**: High
**Action**: Execute the **Executive Sponsor Alignment** save play. Specifically: (1) Within 48 hours, identify the replacement executive sponsor via CRM/LinkedIn/champion introduction; (2) Within 5 business days, schedule a partnership-review meeting with the new sponsor, led by your VP of CS or executive sponsor on your side; (3) Prepare a value summary covering the two adopted workflows (quantified business impact), a roadmap preview, and a proactive plan to address the usage decline and ticket trend before they raise it.

In parallel: Run a **Support Recovery** mini-play — audit all open tickets from this account, assign a named escalation owner, and brief the admin champion on resolution plans this week to prevent support friction from contaminating the sponsor introduction.

**Owner**: CSM (primary), with CS Leader / Executive Sponsor on your side co-leading the new-sponsor meeting; Support Engineering lead for ticket audit
**Deadline**: New-sponsor identified within 2 business days; partnership-review meeting scheduled within 5 business days and held within 15 business days; ticket audit complete within 5 business days
**Expected Outcome**: New executive sponsor briefed and bought-in before renewal conversation begins; ticket trend stabilized or explained; WAU decline root cause identified (seasonal, role change at client, workflow shift, or genuine disengagement) and a 30-day reversal plan agreed with the champion

## Priority Action List

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | Account-001 | Identify and brief replacement executive sponsor (Executive Sponsor Alignment play) | CSM + CS Leader | Identification in 2 BD; meeting scheduled in 5 BD | Renewal conversation begins with a sponsor who has no relationship history, defaults to procurement-led review, full $120k ARR at risk |
| 2 | Account-001 | Support ticket audit and recovery plan with named escalation owner | CSM + Support lead | 5 business days | Support friction compounds sponsor-transition risk; champion loses confidence |
| 3 | Account-001 | Diagnose WAU 18% decline with champion — segment by user, workflow, and time window | CSM | 10 business days | Decline continues unchecked, drops past the 20% red-flag threshold, score moves toward Likely to Churn |
| 4 | Account-001 | Request NPS/CSAT pulse and confirm billing/payment status to close data gaps | CSM + Finance | 10 business days | Forecast confidence remains Low; blind spots heading into renewal |

## Early Warning Watchlist

| Account | Health Score | Warning Signal | Monitoring Cadence | Trigger for Escalation |
|---|---|---|---|---|
| Account-001 | 49 | This account is already At Risk; included here for the secondary watch on WAU trajectory | Weekly until renewal | WAU decline crosses 20% over trailing 30 days, OR any P0/P1 ticket opens, OR champion responsiveness slips beyond 48 hours |

## Data Gaps

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| Account-001 | NPS/CSAT history and recent score | NPS/CSAT scored neutral (50) by default; no direct human satisfaction signal available | Trigger transactional CSAT on recent tickets; send relational NPS pulse this week |
| Account-001 | Billing history (payment timeliness, disputes, discount dependency) | Billing scored neutral (50) by default; cannot assess financial commitment signal | Pull DSO and invoice history from billing platform |
| Account-001 | Support ticket details: volume %, severity mix, sentiment, CSAT on resolutions | Support scored conservatively at 45 on partial signal; could be materially worse or better with detail | Export trailing 90-day ticket data with severity, sentiment, and CSAT fields |
| Account-001 | Feature adoption denominator (workflows purchased vs. adopted; module activation rates) | Adoption scored neutral; "two workflows" has no context | Pull feature usage matrix from product analytics |
| Account-001 | WAU decline window (30/60/90 day) and cohort comparison | Cannot determine if 18% is acute or gradual; cannot adjust for seasonality | Pull trailing 30/60/90-day WAU series; compare to cohort |
| Account-001 | Replacement executive sponsor identity and engagement status | Stakeholder Continuity scored 40 assuming no replacement briefed | LinkedIn monitoring, CRM update, direct ask to admin champion |
| Account-001 | Competitive mentions, renewal-process signals, contract modification history | Cannot assess procurement-side risk | CRM notes review, ask champion directly |

## Methodology Notes

- Health Score model version: 1.0
- Weights applied as specified in skill (Engagement 20, Support 15, Adoption 20, NPS/CSAT 10, Billing 10, Stakeholder 10, Usage 15)
- Data coverage period: Not specified by user; only point-in-time qualitative signals supplied
- Known limitations:
  - Only one account analyzed; no portfolio context
  - Four of seven dimensions had no underlying data and were scored at neutral (50) per the missing-data rule, then confidence reduced to Low
  - WAU trend window is unspecified; an 18% decline could be 30-day (acute) or 90-day (gradual) and the implications differ
  - "Support tickets up" is directional only; volume %, severity, and sentiment unknown
  - Confidence is **Low** per the calibration rule (data on ≤3 dimensions with primary evidence; 4 dimensions are inferred or defaulted)
  - Per the conservative-prediction guideline, negative signals (sponsor departure, WAU decline, rising tickets, renewal proximity) were weighted to keep this account in the At Risk band rather than Neutral, despite a raw composite that sits at the 49/60 boundary

---

**Skill boundary note**: The Skill specifies writing `renewal-forecast.md` to the working directory using the Write tool. In this session the content is delivered inline above; the correct next step is to save the block from "# Renewal Forecast" through "Methodology Notes" as `renewal-forecast.md`. To strengthen the forecast from Low to Medium/High confidence, supply the data templates noted under **Data Gaps** — especially NPS/CSAT, billing history, and a 30/60/90-day usage series.

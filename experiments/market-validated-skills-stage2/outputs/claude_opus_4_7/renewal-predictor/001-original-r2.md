I'll analyze this synthetic account against the seven-dimension health score model. Note: this is a single-account assessment from limited narrative signals, not a full file-based portfolio scan, so I'll produce the assessment inline and flag the data gaps.

---

# Renewal Forecast

Generated: 2025 (date not specified)
Accounts Analyzed: 1
Data Sources: User-supplied narrative signals (no structured data files provided)

## Executive Summary

A single synthetic account with $120k ARR is **75 days from renewal** and showing a mixed but deteriorating signal profile. The loss of the executive sponsor combined with an 18% WAU decline and rising support volume puts this account in the **At Risk** category. The admin champion's continued engagement and two adopted workflows are the primary stabilizers. **The single most urgent action: secure an executive-to-executive meeting with the new sponsor (or identify and brief them) within 5 business days**, before the renewal window narrows further.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| Synthetic Account | 54 | At Risk | Low-Medium | $120k | ~75 days out | Executive sponsor departure + usage decline | Executive sponsor alignment + stakeholder re-engagement |

## Detailed Assessments

### Synthetic Account -- At Risk

**Health Score: 54/100 | Confidence: Low-Medium | ARR: $120k | Renewal: ~75 days**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 55 | 20% | 11.0 | Down |
| Support Ticket Volume/Sentiment | 45 | 15% | 6.75 | Down |
| Feature Adoption | 55 | 20% | 11.0 | Stable |
| NPS/CSAT | 50 | 10% | 5.0 | Unknown (data gap) |
| Billing History | 50 | 10% | 5.0 | Unknown (data gap) |
| Stakeholder Continuity | 45 | 10% | 4.5 | Down |
| Usage Trends | 50 | 15% | 7.5 | Down |
| **Total** | | **100%** | **50.75 → 51** | |

*Note: I am revising the composite to **51** based on the weighted math. The narrative-level "54" in the overview reflected an initial estimate; the table calculation governs. Treat the score as **51/100 — At Risk**.*

#### Dimension Rationale

- **Engagement (55)**: Admin champion still engaged is a positive anchor, but WAU is down 18% indicating broader engagement is thinning. Scored mid-range.
- **Support (45)**: Ticket volume "up" without severity/sentiment detail. Conservative scoring per the guideline to weight negative signals more heavily.
- **Adoption (55)**: Two key workflows adopted is meaningful but unclear what % of purchased features that represents. Scored at the low end of the 50-69 band (concentrated in core workflows).
- **NPS/CSAT (50)**: No data provided — neutral default per missing-data protocol.
- **Billing (50)**: No data provided — neutral default.
- **Stakeholder (45)**: Executive sponsor departure is a material loss. Admin champion presence prevents a lower score, but no successor sponsor is identified. Falls into the 30-49 band ("executive sponsor unknown or has changed").
- **Usage (50)**: WAU down 18% is a meaningful decline but not yet a collapse. Sits at the boundary between flat-declining (50-69) and clearly declining (30-49); scored conservatively at the boundary.

#### Active Signals

**Churn Signals:**
- **Executive sponsor departure (High-severity precursor)**: Sponsor left; no evidence of a successor being briefed. This alone destabilizes the renewal conversation.
- **Usage decline + support increase (compound signal)**: WAU down 18% while ticket volume rises suggests users are struggling, not just disengaging. Could indicate a product friction issue surfacing now.
- **Renewal proximity (75 days)**: Per protocol, accounts within 90 days of renewal receive elevated urgency regardless of score.

**Expansion Signals:**
- None clearly present in the supplied data. Two adopted workflows could become a foundation, but current trajectory does not support expansion conversation yet.

#### Evidence

- WAU declined 18% (timeframe not specified — assumed trailing 30-60 days)
- Support tickets "up" (volume magnitude, severity mix, and sentiment not specified)
- Executive sponsor confirmed departed (timing not specified)
- Admin champion confirmed still engaged (depth of influence not specified)
- Two key workflows in active use (out of unknown total purchased scope)

**Data gaps that constrain confidence:** NPS/CSAT history, billing/payment history, support ticket severity and sentiment, total features purchased vs. used, identity of any replacement executive sponsor, admin champion's level of organizational influence.

#### Recommended Action

**Priority**: High (escalating to Critical if no sponsor replacement identified within 2 weeks)

**Action**:
1. **Executive Sponsor Alignment (save play)** — CS leader or your executive maps the client's new org chart, identifies the likely replacement sponsor, and requests a partnership review meeting. Frame as a re-introduction, not a save. Bring a value summary anchored to the two adopted workflows and a roadmap preview.
2. **Support Recovery (parallel track)** — Audit the rising ticket volume immediately. Determine whether the increase is severity-driven (critical) or volume-driven (friction). Assign a dedicated support contact if any P1/P2 tickets are open.
3. **Champion Reinforcement** — Brief the admin champion on the sponsor change. Ask them directly who the new decision-maker will be at renewal and whether they need air cover or co-selling support internally.

**Owner**: CSM (primary), CS Leader (executive outreach), Support Engineering (ticket audit)

**Deadline**:
- Sponsor identification and outreach: within 5 business days
- Support ticket audit and remediation plan: within 3 business days
- Champion briefing: within 5 business days

**Expected Outcome**:
- New executive sponsor identified and a partnership meeting scheduled within 2 weeks
- Support ticket trend reversed or contextualized (with committed resolution plan) within 30 days
- WAU stabilized or recovering by the 45-day mark (30 days before renewal)
- Renewal conversation initiated by Day 45 with the admin champion and new sponsor aligned

## Priority Action List

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | Synthetic Account | Identify new executive sponsor and secure partnership meeting | CS Leader | 5 business days | Renewal proceeds with no executive advocate; high churn probability |
| 2 | Synthetic Account | Audit rising support tickets for severity and sentiment | Support Engineering | 3 business days | Underlying product friction compounds usage decline |
| 3 | Synthetic Account | Brief admin champion on sponsor change and co-build renewal narrative | CSM | 5 business days | Champion becomes single-threaded liability; no internal advocate at decision time |

## Early Warning Watchlist

Not applicable — this account is already At Risk, not in the watchlist tier.

## Data Gaps

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| Synthetic Account | NPS/CSAT history | Forced neutral default on satisfaction dimension | Trigger a relational CSAT survey to the admin champion this week |
| Synthetic Account | Billing/payment history | Forced neutral default on financial commitment signal | Pull AR aging report and discount history from billing system |
| Synthetic Account | Support ticket severity, sentiment, escalation status | Support score conservatively low; could be lower or higher with detail | Pull ticket export with severity, CSAT, and sentiment fields for trailing 90 days |
| Synthetic Account | Feature adoption breadth (% of purchased features used) | Adoption score is an estimate based on "two workflows" only | Pull feature usage matrix vs. purchased entitlements |
| Synthetic Account | New executive sponsor identity | Stakeholder continuity score assumes worst-case (no successor briefed) | CRM update, LinkedIn check, direct ask to admin champion |
| Synthetic Account | Timeframe of the 18% WAU decline | Usage trend scored at boundary; precise window would refine | Pull trailing 30/60/90-day WAU curves |

## Methodology Notes

- Health Score model version: 1.0
- Weights applied as specified: Engagement 20%, Support 15%, Adoption 20%, NPS/CSAT 10%, Billing 10%, Stakeholder 10%, Usage 15%
- Data coverage period: Not specified by the user; assumed recent (trailing 30-90 days)
- Confidence level: **Low-Medium**. Data was available or inferable for 5 of 7 dimensions; 2 dimensions (NPS/CSAT, Billing) had no signal and defaulted to neutral. Per protocol, confidence is reduced one tier for every 2 missing dimensions.
- Known limitations:
  - All scoring derived from a brief narrative, not structured data files. Per the Skill's execution protocol, a file-based scan (Glob/Grep across CSV/JSON sources) would normally produce the assessment. The user provided no files, so this assessment uses the narrative directly and flags data gaps explicitly.
  - The `renewal-forecast.md` file was not written to disk because no working directory data was processed and the user requested an inline assessment of supplied signals. **Skill boundary note**: if you want the formal artifact, provide the data files (or confirm the working directory) and I will generate `renewal-forecast.md` as specified.
  - Scores are rounded to whole numbers per behavioral guideline #4.
  - Negative signals weighted more heavily than positive signals where they conflicted, per guideline #2.

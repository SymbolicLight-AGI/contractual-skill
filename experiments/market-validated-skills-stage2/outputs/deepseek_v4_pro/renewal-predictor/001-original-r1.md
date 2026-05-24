```markdown
# Renewal Forecast

Generated: 2025-04-09
Accounts Analyzed: 1
Data Sources: User‑supplied synthetic account signals (no external files)

## Executive Summary

One account was assessed: **Acme Corp** ($120k ARR, renews in 75 days) scored an At‑Risk health score of **48** due to a combination of executive sponsor departure, declining weekly active users (‑18%), and rising support ticket volume. Confidence is **Low** because two dimensions (NPS/CSAT, Billing) are missing, and the remaining signals are only partial. The immediate priority is to re‑engage stakeholder relationships, stabilize usage, and investigate the support ticket trend before the renewal window tightens.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| Acme Corp | 48 | At Risk | Low | $120,000 | 2025-06-23 | Executive sponsor departed + usage declining | Stakeholder Re‑engagement Campaign |

## Detailed Assessments

### Acme Corp – At Risk

**Health Score: 48/100 | Confidence: Low | ARR: $120,000 | Renewal: 2025-06-23**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|---|
| Engagement Frequency | 50 | 20% | 10 | Stable |
| Support Ticket Volume/Sentiment | 50 | 15% | 7.5 | Down |
| Feature Adoption | 50 | 20% | 10 | Stable |
| NPS/CSAT | 50 | 10% | 5 | Stable |
| Billing History | 50 | 10% | 5 | Stable |
| Stakeholder Continuity | 40 | 10% | 4 | Down |
| Usage Trends | 40 | 15% | 6 | Down |
| **Total** | | **100%** | **47.5 → 48** | |

#### Active Signals

**Churn Signals:**
- **Executive Sponsor Departed** (Medium severity): The executive sponsor left the organisation; no replacement has been identified or briefed. This removes a key advocate and budget authority.
- **Usage Trend Negative** (Medium severity): Weekly active users are down 18% over a recent period, placing the account at risk of further disengagement.
- **Support Ticket Volume Increasing** (Medium severity): Support tickets are rising, which may indicate emerging product issues or user frustration – sentiment and severity unknown.
- **Single‑threaded Relationship Risk** (informational): Only the admin champion remains actively engaged; the relationship lacks multi‑stakeholder depth after the sponsor’s departure.

**Expansion Signals:**
- None detected based on available data.

#### Evidence

- User‑supplied signals: “weekly active users down 18%, support tickets up, executive sponsor left, admin champion still engaged, two key workflows adopted.”
- No NPS, CSAT, billing, or detailed engagement logs available.
- Two key workflows adoption suggests the client uses core functionality, but breadth and depth of feature usage are undocumented.
- No direct data on contract terms, payment history, or discount dependency.

#### Recommended Action

**Priority**: High
**Action**: Stakeholder Re‑engagement Campaign – Work with the admin champion to identify and brief a new executive sponsor within 10 business days. Simultaneously, schedule a partnership health review to address the usage decline and support trend. Offer a dedicated support audit on the rising ticket volume.
**Owner**: CSM
**Deadline**: 2025-04-23 (first sponsor contact) / 2025-04-30 (review meeting)
**Expected Outcome**: New executive sponsor identified and engaged; usage decline stabilised; support issue diagnosis initiated; account moves from At Risk to Neutral within 60 days.

## Priority Action List

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | Acme Corp | Re‑engage stakeholders: identify new executive sponsor via admin champion, schedule partnership review, audit support tickets | CSM | 2025-04-23 | Executive vacuum persists, usage continues to slide, renewal conversation becomes adversarial or silent |

## Early Warning Watchlist

None (Acme Corp is already At Risk).

## Data Gaps

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| Acme Corp | NPS/CSAT scores, Billing history, detailed engagement activity (QBR attendance, response latency) | Lowered confidence to Low; prevented detection of possible discount dependency or satisfaction trends | Send a relational NPS survey immediately; pull billing records from finance; ask the CSM for last‑90‑day engagement log and any meeting notes |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: Not specified (using default v1.0 weights)
- Data coverage period: Signals provided as of today; no historical data files available.
- All dimensions without evidence scored at neutral 50 per protocol, with two flagged as missing (NPS/CSAT, Billing) causing a confidence downgrade to Low.
- The synthetic account was analysed solely on the user‑supplied signals; no external data was accessible.
- Analysis assumes WAU decline is recent and not seasonal; no seasonal pattern data provided.
```

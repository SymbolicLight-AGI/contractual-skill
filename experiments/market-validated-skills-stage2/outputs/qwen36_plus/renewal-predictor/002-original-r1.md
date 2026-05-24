# Renewal Forecast

Generated: 2024-05-20
Accounts Analyzed: 1
Data Sources: Qualitative input only ("customer uses the product", "renewal this year")

## Executive Summary

Portfolio health cannot be accurately quantified due to severe data sparsity across all seven health dimensions. The single account analyzed is classified as **At Risk** with **Low Confidence** based strictly on the missing data protocol, which defaults unknown dimensions to a neutral 50/100 score. Total ARR at risk is unquantified. The primary systemic theme is a lack of baseline telemetry and relationship mapping. The single most urgent action is to initiate a structured data collection and baseline health check to replace assumptions with measurable signals before the renewal window closes.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| Client Account | 50 | At Risk | Low | Not Provided | 2024-XX-XX (This Year) | 6/7 dimensions lack quantitative data | Execute baseline data collection & proactive health check |

## Detailed Assessments

### Client Account -- At Risk

**Health Score: 50/100 | Confidence: Low | ARR: Not Provided | Renewal: 2024-XX-XX (This Year)**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 50 | 20% | 10.0 | Unknown |
| Support Ticket Volume/Sentiment | 50 | 15% | 7.5 | Unknown |
| Feature Adoption | 50 | 20% | 10.0 | Unknown |
| NPS/CSAT | 50 | 10% | 5.0 | Unknown |
| Billing History | 50 | 10% | 5.0 | Unknown |
| Stakeholder Continuity | 50 | 10% | 5.0 | Unknown |
| Usage Trends | 50 | 15% | 7.5 | Unknown |
| **Total** | | **100%** | **50** | |

#### Active Signals

**Churn Signals:**
- **Data Void Risk**: Absence of usage trends, support history, billing records, and stakeholder mapping prevents early warning detection. Per protocol, missing data defaults to neutral scoring, which masks potential deterioration.
- **Renewal Proximity**: Renewal is scheduled for this year. Without a baseline health trajectory, the account is operationally blind to churn indicators.

**Expansion Signals:**
- None detected. Insufficient data to evaluate expansion potential.

#### Evidence

- **Qualitative Input**: Customer confirmed to be actively using the product.
- **Quantitative Data**: Zero structured metrics available for DAU/WAU/MAU, ticket volume/severity, NPS/CSAT scores, payment history, or contact role changes.
- **Inference**: Per the "Scoring When Data Is Missing" protocol, all 7 dimensions are scored at 50 (neutral) due to complete absence of measurable data. Confidence is capped at Low because data is available for 0 of 7 dimensions, and no direct human signals (surveys, meeting notes, email sentiment) are present.

#### Recommended Action

**Priority**: Critical
**Action**: Initiate a 14-day Baseline Data Collection & Health Check. CSM to pull product analytics (trailing 90 days), export support ticket history, verify billing status, and map current stakeholder roles. Schedule a 30-minute discovery call with the primary contact to validate usage patterns, confirm renewal timeline, and establish a mutual success baseline.
**Owner**: CSM / CS Operations
**Deadline**: 2024-06-03
**Expected Outcome**: Complete data population across all 7 dimensions, enabling a recalculated Health Score with Medium/High confidence and a targeted renewal strategy.

## Priority Action List

Ranked list of interventions sorted by urgency and impact. This is the operational output that the CS team should execute against.

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | Client Account | Execute baseline data collection & schedule discovery call | CSM | 2024-06-03 | Renewal proceeds blind to churn signals; potential revenue loss if hidden risks exist |
| 2 | Client Account | Map stakeholder continuity & identify executive sponsor | CSM | 2024-06-10 | Single-threaded relationship increases vulnerability to champion departure |

## Early Warning Watchlist

Accounts that are currently healthy but showing early signals that could deteriorate. These are not yet at risk but should be monitored more closely over the next 30-60 days.

| Account | Health Score | Warning Signal | Monitoring Cadence | Trigger for Escalation |
|---|---|---|---|---|
| Client Account | 50 | Complete data absence across 6/7 dimensions | Weekly | Any single dimension scores below 40 upon data collection, or renewal date moves within 60 days without baseline established |

## Data Gaps

Accounts or dimensions where insufficient data prevented a confident assessment. These gaps should be filled to improve future forecast accuracy.

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| Client Account | Engagement, Support, Adoption, NPS/CSAT, Billing, Stakeholder, Usage Trends | Forced neutral scoring (50/100) across all dimensions; capped confidence at Low; unable to detect churn/expansion signals | Integrate product analytics API, export CRM activity logs, pull billing platform DSO, run NPS/CSAT survey, update CRM contact records |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: 2024-05-20
- Data coverage period: Not applicable (qualitative input only)
- Known limitations: Assessment relies entirely on the "Scoring When Data Is Missing" protocol. All dimensions defaulted to 50/100 due to zero quantitative inputs. Confidence is Low per calibration rules (0/7 dimensions populated, no human signals, <30 days of historical data). Predictions will be recalibrated immediately upon ingestion of structured account telemetry.

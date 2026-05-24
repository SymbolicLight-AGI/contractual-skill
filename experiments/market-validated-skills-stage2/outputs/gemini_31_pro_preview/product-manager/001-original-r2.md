# Product Prioritization Recommendation

## Executive Recommendation
**Prioritize Candidate A (Guided Import Wizard).** 

While Candidate C offers a quick win, Candidate A directly addresses a validated user pain point (SMB admin onboarding time). Solving onboarding friction is critical for improving activation and reducing early-stage churn. Candidate B should be placed in the discovery backlog until user research validates the sales request. Candidate C can be treated as a backlog filler for engineers with spare capacity.

---

## Uncertainties & Missing Information
To provide this recommendation, I have marked the following uncertainties due to missing data in the prompt:
*   **Uncertainty - Exact Reach:** We lack the exact number of new SMB admins onboarded per quarter vs. total active users.
*   **Uncertainty - Engineering Effort:** We lack exact story points or person-months for each candidate.
*   **Uncertainty - Strategic OKRs:** We lack the current quarter's primary business objective (e.g., is the company focused on Net New ARR or Retention?). *Assumption: Improving retention/activation is the current priority based on the user complaints.*

---

## Prioritization Framework: RICE Scoring

I have applied the **RICE framework** (Reach, Impact, Confidence, Effort) using synthetic baseline assumptions to quantify the decision. 

*Formula: RICE Score = (Reach × Impact × Confidence) / Effort*

### 1. Candidate A: Guided Import Wizard (Recommended)
*   **Context:** Solves SMB admin complaints about onboarding time.
*   **Reach:** 1,000 (Assumed new SMB admins per quarter).
*   **Impact:** 3 (Massive impact on the specific onboarding workflow).
*   **Confidence:** 80% / 0.8 (High confidence; based on direct user complaints).
*   **Effort:** 3 person-months (Assumed medium-high effort for import logic).
*   **RICE Score:** `(1000 * 3 * 0.8) / 3` = **800**
*   **Verdict:** Primary focus. High strategic alignment with user success.

### 2. Candidate C: New Dashboard Theme (Quick Win)
*   **Context:** Low engineering effort.
*   **Reach:** 5,000 (Assumed total active user base).
*   **Impact:** 0.25 (Minimal impact; purely cosmetic, does not solve core workflows).
*   **Confidence:** 100% / 1.0 (High confidence in effort estimation).
*   **Effort:** 0.5 person-months (Assumed very low effort).
*   **RICE Score:** `(5000 * 0.25 * 1.0) / 0.5` = **2,500**
*   **Verdict:** Highest raw score due to math (low effort, broad reach), but low strategic value. Do not prioritize over Candidate A, but execute if there is downtime between major sprints.

### 3. Candidate B: AI Report Writer (Discovery Needed)
*   **Context:** Requested by sales.
*   **Reach:** 500 (Assumed subset of users who actively generate reports).
*   **Impact:** 2 (High impact for specific power users).
*   **Confidence:** 50% / 0.5 (Low confidence; sales requests often reflect a single lost deal rather than broad market need. Needs user validation).
*   **Effort:** 4 person-months (Assumed high effort for AI integration).
*   **RICE Score:** `(500 * 2 * 0.5) / 4` = **125**
*   **Verdict:** Do not build yet. Move to the **Discovery & Research** domain to conduct user interviews and validate the actual Jobs-to-be-Done (JTBD) before committing engineering resources.

---

## SaaS Metrics & Success Criteria

By prioritizing Candidate A (Guided Import Wizard), we expect to move the following SaaS metrics. 

**1. Customer Churn Rate (Early-Stage)**
If onboarding is too long, SMBs will abandon the product before realizing value.
*   *Formula:* `(Customers lost during period / Total customers at start of period) × 100`
*   *Goal:* Decrease 30-day and 90-day churn rates.

**2. Time-to-Value (TTV)**
The primary operational metric for this feature.
*   *Formula:* `Date of first core action completed - Date of account creation`
*   *Goal:* Reduce the average days/hours it takes an SMB admin to complete their first successful data import.

**3. Customer Acquisition Cost (CAC) Payback Period**
Faster onboarding means faster realization of revenue and lower support costs during the trial/implementation phase.
*   *Formula:* `CAC / (ARPA × Gross Margin)` *(where ARPA is Average Revenue Per Account)*
*   *Goal:* Shorten the payback period by reducing the high-touch support hours currently required to help admins through the confusing setup.

**4. Monthly Recurring Revenue (MRR)**
If the product has a freemium or trial model, a guided wizard will directly impact trial-to-paid conversion.
*   *Formula:* `Total number of active paying customers × Average billed amount per customer`
*   *Goal:* Increase New MRR by improving the activation funnel.

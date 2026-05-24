# Product Prioritization Recommendation

## 1. Strategic Alignment & Executive Summary

**Recommendation:** Prioritize **Candidate A (Guided import wizard)** for immediate execution. 

**Rationale:** The primary strategic context provided is that SMB admins are complaining about onboarding time. Candidate A directly addresses this friction point, which is critical for user activation and retention. While Candidate B (AI report writer) may aid sales, building features solely on sales requests without user validation risks feature bloat. Candidate C (New dashboard theme) is a "quick win" but does not solve the core user pain point.

---

## 2. RICE Prioritization Analysis

*Note: Because exact user data, engineering estimates, and revenue figures are missing from the prompt, I have marked these inputs with uncertainty and applied baseline assumptions to calculate the RICE scores.*

| Candidate | Reach (Assumed) | Impact (3=Massive, 0.25=Low) | Confidence (Assumed) | Effort (Person-Months) | RICE Score |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A: Guided Import Wizard** | 100% of new SMB admins | 3 (Massive - solves core pain) | 80% (Based on direct complaints) | 3 (Medium/High) | **80.0** |
| **B: AI Report Writer** | 40% of total user base | 2 (High for specific use cases) | 50% (Sales request, unvalidated by users) | 4 (High - AI integration) | **10.0** |
| **C: New Dashboard Theme** | 100% of total user base | 0.25 (Low - cosmetic only) | 100% (Known technical scope) | 0.5 (Low) | **50.0** |

**RICE Formula Used:** `(Reach × Impact × Confidence) / Effort`

### Assumptions & Uncertainties:
*   **Uncertainty - Reach:** Assuming 100 new SMB admins per month for Candidate A. Assuming Candidate B only appeals to a subset of users (40%) who actively generate reports.
*   **Uncertainty - Effort:** Assuming Candidate A requires 3 person-months (backend logic + UI), Candidate B requires 4 person-months (LLM integration + testing), and Candidate C requires 0.5 person-months (CSS/UI updates).
*   **Uncertainty - Confidence:** Candidate A has high confidence (80%) because it is backed by qualitative user complaints. Candidate B has low confidence (50%) because sales requests often suffer from recency bias and lack broad market validation.

---

## 3. Recommended SaaS Metrics to Track

To measure the success of Candidate A (Guided import wizard), we must track metrics related to onboarding efficiency and early retention. 

**1. Time to Value (TTV)**
*   **Purpose:** Measures the speed at which the SMB admin completes the setup and realizes the product's value.
*   **Formula:** `Date of First Core Action (e.g., successful import) - Date of Account Creation`

**2. Activation Rate**
*   **Purpose:** Measures the percentage of new signups who successfully complete the onboarding flow.
*   **Formula:** `(Number of Users who complete the Guided Import / Total Number of New Signups) × 100`

**3. Customer Churn Rate (Early-Stage)**
*   **Purpose:** High onboarding friction typically leads to high Day-30 churn. Candidate A should reduce this.
*   **Formula:** `(Customers lost in first 30 days / Total new customers in that cohort) × 100`

**4. Customer Acquisition Cost (CAC) Payback Period**
*   **Purpose:** Faster onboarding means faster revenue realization, which improves the payback period.
*   **Formula:** `CAC / (ARPA × Gross Margin)` 
    * *(Where ARPA = Average Revenue Per Account)*

---

## 4. Next Steps (Execution Phase)

1.  **Validate Assumptions:** Partner with Engineering to get actual Effort estimates (T-shirt sizing or story points) for Candidate A to replace the assumed 3 person-months.
2.  **Discovery for Candidate A:** Conduct 3-5 user interviews with recently churned or struggling SMB admins to map the exact friction points in the current import process (using an Opportunity Solution Tree).
3.  **Backlog Candidate B & C:** Place Candidate B in the "Discovery" backlog to validate the actual user need behind the sales request. Place Candidate C in the "Quick Wins" backlog to be picked up by engineers during sprint downtime.
4.  **Draft PRD:** Initiate a PRD for the Guided Import Wizard defining the user stories, edge cases (e.g., malformed CSV uploads), and success criteria based on the metrics above.

# Discovery Handoff: Contact Import Drop-off

## 1. Problem Statement
Trial users are abandoning the onboarding setup process immediately after attempting to import contacts. The current CSV import experience is causing high friction, blocking user activation.

## 2. Evidence & Insights
* **Qualitative:** 7 out of 10 interviewed users explicitly mentioned confusion around CSV formatting requirements.
* **Quantitative:** Customer Support receives weekly tickets regarding import issues. 
* *[Uncertainty Marked]*: The exact volume and trend of these weekly support tickets are currently missing. We need this data to baseline the problem.

## 3. Jobs-to-be-Done (JTBD)
* **When** I am setting up my new account,
* **I want to** seamlessly import my existing contact list,
* **So that** I can experience the product's value immediately without manual data entry.

## 4. Team Handoff & Asks

### 🎨 Design
* **Objective:** Reduce cognitive load and formatting confusion during the import step.
* **Exploration Areas:**
  * Clearer in-app instructions or downloadable CSV templates.
  * A visual data-mapping UI (e.g., matching user CSV columns to our system fields).
  * Better inline error states (e.g., highlighting exactly which rows/columns failed and why, rather than a generic failure message).

### 💻 Engineering
* **Objective:** Improve the robustness and flexibility of the import parser.
* **Exploration Areas:**
  * Evaluate the technical effort required to build auto-mapping for columns or handle messy CSVs (e.g., different delimiters, missing headers).
  * *[Uncertainty Marked]*: No feasibility estimate exists yet. Engineering is requested to timebox a technical spike to provide sizing and technical constraints.

### 📊 Data
* **Objective:** Establish baseline metrics and granular funnel tracking for the import flow.
* **Exploration Areas:**
  * Implement tracking for specific drop-off points (e.g., file selection -> mapping -> validation error -> successful import).
  * Track the frequency and specific types of validation errors users encounter to inform future engineering and design iterations.

## 5. Success Metrics (Proposed)
* **Primary:** Increase the completion rate of the contact import step.
* **Secondary:** Decrease the number of weekly support tickets related to CSV imports.
* **SaaS Metric Impact:** Improve overall Trial-to-Paid Conversion Rate (by unblocking the activation phase).

## 6. Immediate Next Steps
1. **Engineering:** Conduct a technical spike to provide the missing feasibility estimate for improved CSV parsing/mapping.
2. **Data:** Pull the exact number of weekly support tickets to baseline our secondary metric.
3. **Design:** Begin wireframing potential UI improvements for the import flow based on the JTBD.

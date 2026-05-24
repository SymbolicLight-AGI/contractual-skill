## Understanding Summary

**Fact:** The only product note is: “Build an analytics dashboard for managers.”

That is not enough to design responsibly yet. The phrase “analytics dashboard” could mean many different things depending on the type of manager, business domain, decisions they need to make, available data, update frequency, and success criteria.

At this stage, the useful outcome is not a dashboard design yet, but a clarified problem statement.

## What Is Known

- **Proposed feature:** Analytics dashboard.
- **Intended audience:** “Managers,” but the manager type is unspecified.
- **Current gap:** No confirmed users, metrics, data sources, workflows, or success criteria.

## What Is Missing

### Open Questions

1. **Target user**
   - What kind of managers?
   - Examples: sales managers, engineering managers, operations managers, customer support managers, store managers, finance managers.

2. **Decision workflow**
   - What decisions should the dashboard help them make?
   - Example: staffing, coaching, budget allocation, SLA management, forecasting, prioritization.

3. **Core metrics**
   - What metrics matter?
   - Example: revenue, team productivity, customer satisfaction, churn, incidents, utilization, conversion rate.

4. **Data sources**
   - Where does the data come from?
   - Example: CRM, support system, HRIS, warehouse, product events, spreadsheets, manual uploads.

5. **Freshness**
   - How current does the data need to be?
   - Real-time, hourly, daily, weekly, monthly?

6. **Scope**
   - Is this for one team, one department, or the whole company?
   - Is it internal-only?

7. **Success criteria**
   - How will we know the dashboard worked?
   - Example: reduced reporting time, improved decision speed, increased metric visibility, fewer manual spreadsheet reports.

8. **Permissions and privacy**
   - Should managers only see their own team’s data?
   - Are there sensitive employee, customer, or financial metrics?

9. **Existing behavior**
   - Is there an existing dashboard, spreadsheet, report, or manual process being replaced?
   - If so, what is painful about it?

## Assumptions — Not Yet Accepted

These are temporary working assumptions only:

- **Assumption:** The dashboard is for internal business users, not external customers.
- **Assumption:** Managers need aggregated metrics rather than raw records.
- **Assumption:** The dashboard should support recurring operational decisions, not one-off analysis.
- **Assumption:** Role-based access may be needed because management data can be sensitive.
- **Assumption:** Success should be tied to a decision or workflow improvement, not just page views.

## Risks If We Design Now

- **Risk:** Building charts that look useful but do not support real decisions.
- **Risk:** Choosing the wrong metrics because the target manager type is unclear.
- **Risk:** Underestimating data quality, permissions, or availability issues.
- **Risk:** Creating a generic dashboard that becomes another unused reporting surface.
- **Risk:** No measurable success criteria, making it hard to evaluate launch impact.

## Not Ready for Design Yet

I would not recommend moving into dashboard layout, chart selection, data modeling, or implementation planning until the target user and decision workflow are confirmed.

## First Clarifying Question

Who is the primary manager persona for this dashboard?

A. Sales managers  
B. Engineering managers  
C. Customer support managers  
D. Operations managers  
E. Finance/business managers  
F. Store/field managers  
G. Other / not sure yet

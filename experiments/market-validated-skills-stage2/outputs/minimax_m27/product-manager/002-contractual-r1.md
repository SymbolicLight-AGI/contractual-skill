<think>The user is asking me to produce a product management response for a PRD request where the stakeholder has provided very little information - just "AI insights for all users" with no user segment, workflow, data source, or success metric.

According to the skill under test (product-manager-contractual), I need to:
1. Not fabricate missing evidence
2. Make explicit what is known vs assumed
3. Provide a useful response that helps the product owner decide next steps
4. Follow the output format (Goal and user, Known facts, Assumptions and unknowns, Recommendation or options, Metrics and validation, Risks and human gates, Next steps)

This is a classic case where I need to push back on the request and turn it into a discovery/validation exercise rather than producing a full PRD that would be based on fabricated assumptions.

Let me structure this response properly according to the skill guidelines.
</think>

# Product Management Response: "AI Insights for All Users"

## 1. Goal and User

**Cannot be stated.** The request does not identify:
- Which users ("all users" is not a segment)
- What problem AI insights would solve for them
- What workflow the insights would support

**Stated goal (from stakeholder):** Deliver AI-generated insights to users.

---

## 2. Known Facts

| Fact | Source | Confidence |
|------|--------|------------|
| Stakeholder wants AI-powered insights feature | Task prompt | High |
| Feature should be available to all users | Task prompt | High |
| No user segment defined | Task prompt | N/A |
| No data source specified | Task prompt | N/A |
| No success metric defined | Task prompt | N/A |

---

## 3. Assumptions and Unknowns

### Assumptions (Cannot Proceed Without Validation)

- **User segment:** Assuming "all users" means all existing product users—but this may include users with no use case for AI insights.
- **Insight type:** Assuming the stakeholder has a specific insight category in mind (e.g., usage patterns, anomalies, recommendations)—but this was not stated.
- **Data source:** Assuming the product has structured data sufficient to generate meaningful AI insights—but no data source was identified.
- **Value proposition:** Assuming users will find AI insights valuable without evidence of a pain point or unmet need.

### Unknowns (Blocking PRD Completion)

1. **Who** is the target user? (Role, context, current workflow)
2. **What** insight do they need? (Problem statement, not solution)
3. **Why** do they need it? (Current pain, gap, or opportunity)
4. **Where** in the workflow would insights appear? (Entry point, frequency)
5. **When** would they act on insights? (Real-time, batch, periodic)
6. **What data** will power the insights? (Availability, quality, access)
7. **How will success be measured?** (Adoption, task completion, business impact)

---

## 4. Recommendation or Options

### Option A: Decline PRD Until Discovery Is Complete
Do not produce a full PRD. The request lacks the minimum inputs to produce a useful artifact. Proceed to discovery first.

### Option B: Produce a PRD Shell With Explicit Gaps
If the stakeholder requires a document now, produce a PRD template with all sections labeled as **[UNVALIDATED]** and require sign-off on open questions before engineering engagement.

### Option C: Run a 2-Week Discovery Sprint First
Treat this as a discovery decision type. Validate the opportunity before committing to requirements.

**Recommended path: Option C.** This is a discovery decision, not a requirements decision. The PRD cannot be written responsibly without user evidence.

---

## 5. Metrics and Validation

### Validation Plan (Required Before PRD)

| Question | Validation Method | Owner |
|----------|-------------------|-------|
| Which user segment has a pain that AI insights would address? | User interviews, support ticket analysis | Product + Research |
| What specific insights would users find valuable? | Job-to-be-done interviews, diary studies | Product + Research |
| Is there existing data of sufficient quality? | Data audit, feasibility spike | Engineering + Data |
| What does "insights" mean to the stakeholder? | Clarifying questions, examples | Product |

### Post-Validation Metrics (To Be Defined)

- Insight adoption rate
- Action taken on insights
- User satisfaction with insight relevance
- Downstream business metric (if applicable)

*These cannot be defined until the insight type and user segment are known.*

---

## 6. Risks and Human Gates

### Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Building insights no user needs | High | Validate pain point before building |
| "All users" segment includes users with no use case | High | Define minimum viable segment |
| Data quality insufficient for meaningful AI output | Medium | Data audit before scoping |
| Stakeholder expectation mismatch on scope | Medium | Align on problem statement, not solution |

### Human Gates Required

- [ ] **Stakeholder alignment** on target user segment and insight category
- [ ] **Data team sign-off** on data availability and quality
- [ ] **Engineering feasibility** review (not possible until data source known)
- [ ] **Leadership approval** for discovery sprint investment

---

## 7. Next Steps

1. **Schedule clarifying conversation** with stakeholder to answer the six unknowns above.
2. **Define the decision type:** Is this a new feature discovery, a differentiation play, or a retention initiative? The answer changes the validation approach.
3. **Identify one user segment** to validate against first. "All users" is not a starting point.
4. **Audit existing data** to determine if AI insights are technically feasible.
5. **Draft interview guide** to validate user pain before writing requirements.
6. **Return to this request** once discovery evidence exists.

---

## Summary

A PRD for "AI insights for all users" cannot be responsibly produced without user evidence, a defined segment, a data source, and a success metric. The appropriate response is to treat this as a **discovery decision** and invest in validation before committing to requirements.

**Do not proceed to PRD drafting until the open questions above are answered.**

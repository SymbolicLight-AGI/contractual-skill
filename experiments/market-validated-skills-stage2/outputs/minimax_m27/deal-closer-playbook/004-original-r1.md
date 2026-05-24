<think>The user is asking me to prepare an internal handoff document for a deal that has security and procurement blockers. Let me analyze what they've provided:

**Known deal facts:**
- Buyer likes the product
- Security questionnaire is pending
- Procurement needs vendor onboarding
- Champion asked for an implementation timeline

This is a fairly limited set of information. According to the Skill, I should ask for missing required information. However, the user has framed this as "prepare the internal handoff" - they're asking me to create a specific document type (internal handoff) rather than a full deal playbook.

Let me think about what I need vs. what I can work with:

**What I have:**
- Deal has security questionnaire pending
- Procurement needs vendor onboarding
- Champion wants implementation timeline
- Buyer likes the product (positive signal)

**What I don't have (marked as [UNKNOWN]):**
- Company name
- What is being sold
- Current deal stage
- Primary contact name and title
- Deal size
- Target close date
- Champion name
- Economic buyer
- Technical evaluator
- Competitors
- Previous interactions

The user is asking for an "internal handoff" - this is typically a document that shares deal context with internal stakeholders (like security team, procurement team, implementation team) so they can do their part of the deal work.

Given the limited information, I should:
1. Acknowledge what I know and don't know
2. Create a template/framework for the internal handoff that addresses the specific blockers mentioned
3. Make it actionable for the internal teams

Let me create a comprehensive internal handoff document that:
- Addresses the security questionnaire pending
- Addresses the procurement vendor onboarding
- Includes an implementation timeline framework
- Is structured so the rep can fill in the [UNKNOWN] fields

I'll write this as a practical internal handoff document.
</think>

# Internal Handoff: Security & Procurement

**Note:** Several required fields below are marked `[UNKNOWN]` because they were not provided. The rep should fill these in before distributing this handoff to internal stakeholders.

---

## Deal Summary

| Field | Value |
|-------|-------|
| **Company Name** | [UNKNOWN] |
| **Deal Size (ARR/TCV)** | [UNKNOWN] |
| **Target Close Date** | [UNKNOWN] |
| **Deal Stage** | [UNKNOWN - likely Proposal or Negotiation based on blockers present] |
| **Deal Owner** | [Rep Name] |
| **Champion Name/Title** | [UNKNOWN] |
| **Economic Buyer** | [UNKNOWN] |

---

## Current Status

| Item | Status | Owner | Deadline |
|------|--------|-------|----------|
| Buyer product fit | ✅ Positive - buyer likes the product | — | — |
| Security questionnaire | ⏳ PENDING | [Your Security Team] | [Set deadline] |
| Procurement vendor onboarding | ⏳ PENDING | [Your Procurement/Finance] | [Set deadline] |
| Implementation timeline | ⏳ REQUESTED by champion | [Your PS/Implementation Team] | [Set deadline] |

---

## Section 1: Security Questionnaire Handoff

### What We Need from Security Team

**Context for Security Team:**
The buyer has expressed interest in the product. Before they can proceed to contract, their security/procurement team requires completion of their security questionnaire. This is a standard vendor assessment process.

**Action Required:**
1. **Assign security contact** who will own questionnaire completion
2. **Confirm questionnaire format** - are we responding to their form, or providing our standard security documentation (SIG, SOC 2, penetration test results, etc.)?
3. **Identify any gaps** - does our standard documentation address their likely questions?
4. **Set response timeline** - typically 5-10 business days for complex questionnaires

**Questions to Clarify with Rep:**
- [ ] Has the buyer sent a specific questionnaire, or are they expecting our standard security package?
- [ ] What is the buyer's security review timeline? (Some enterprises take 4-8 weeks)
- [ ] Are there any known security requirements the buyer has that we cannot meet?
- [ ] Who is the technical evaluator on their side who will review our response?

**Recommended Response SLA:** 5 business days from receipt of questionnaire

---

## Section 2: Procurement Vendor Onboarding Handoff

### What We Need from Procurement/Finance

**Context for Procurement Team:**
This buyer requires vendor onboarding before contract signature. This typically includes:
- W-9 / tax documentation
- Vendor registration in their procurement system
- Insurance certificates (GL, E&O, cyber)
- Banking/W-9 information for payments
- Vendor questionnaire or self-assessment

**Action Required:**
1. **Confirm vendor onboarding requirements** - does the buyer have a standard vendor packet, or specific requirements?
2. **Prepare standard documentation** - insurance certs, W-9, corporate docs
3. **Identify any blockers** - do we have all required insurance? Are there terms in their vendor agreement we cannot accept?
4. **Set onboarding timeline** - procurement onboarding can take 2-4 weeks

**Questions to Clarify with Rep:**
- [ ] Has the buyer sent a vendor onboarding packet, or are they expecting our standard documentation?
- [ ] What is their vendor approval process? (Some companies require procurement committee review)
- [ ] Are there any red lines in their vendor agreement we cannot accept?
- [ ] Who is the procurement contact on their side?

**Recommended Onboarding SLA:** Initiate within 3 business days, complete within 10 business days

---

## Section 3: Implementation Timeline Handoff

### What We Need from Implementation/PS Team

**Context for PS Team:**
The champion has asked for an implementation timeline. This suggests they are thinking about how the solution fits into their operational planning. Providing a clear timeline reduces perceived risk and builds confidence.

**Information to Provide:**

**Standard Implementation Phases:**
1. **Kickoff & Discovery** (Week 1-2): Project scoping, requirements gathering, stakeholder alignment
2. **Configuration & Setup** (Week 3-6): System configuration, integrations, data migration prep
3. **Testing & Training** (Week 7-8): UAT, user training, change management
4. **Go-Live** (Week 9): Production deployment
5. **Stabilization** (Week 10-12): Post-launch support, optimization

**Questions to Clarify with Rep:**
- [ ] What is the buyer's desired go-live date?
- [ ] What integrations are required? (This affects timeline significantly)
- [ ] What is the expected user count and geographic distribution?
- [ ] Does the buyer have internal resources to support implementation, or do they need full-service PS?
- [ ] Are there any technical blockers on their side (IT approval, network access, etc.)?

**Deliverable:** Draft implementation timeline document for champion review

**Recommended Timeline SLA:** 3 business days from request

---

## Section 4: Rep Action Items

| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| Send security questionnaire to internal security contact | [Rep] | [Date] | ⏳ |
| Confirm vendor onboarding requirements with buyer | [Rep] | [Date] | ⏳ |
| Request implementation timeline from PS team | [Rep] | [Date] | ⏳ |
| Schedule call with champion to review timeline | [Rep] | [Date] | ⏳ |
| Identify economic buyer for procurement introduction | [Rep] | [Date] | ⏳ |

---

## Section 5: Risk Flags for Internal Teams

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Security questionnaire reveals gaps we cannot address | Medium | High - deal loss | Proactively share security posture before questionnaire arrives |
| Procurement onboarding reveals insurance/certification gaps | Medium | High - deal delay | Audit our own vendor readiness now |
| Implementation timeline exceeds buyer's expectations | Medium | Medium - champion loses credibility internally | Get buyer's desired timeline first, then scope to fit |
| Procurement process takes longer than close date | High | High - missed close | Build 4-6 week buffer into close date if procurement is involved |

---

## Section 6: Key Messages for Internal Teams

**For Security Team:**
> "This is a strong deal. The buyer likes the product. We need to move quickly on their security questionnaire to keep momentum. Please prioritize."

**For Procurement Team:**
> "Buyer requires vendor onboarding before signature. This is a [UNKNOWN] ARR deal closing [UNKNOWN date]. We need to initiate our side of the process immediately to avoid delays."

**For PS Team:**
> "Champion has asked for an implementation timeline. This is a positive signal -- they're thinking about execution. Please prepare a realistic timeline that we can use to build confidence. We need this by [date]."

---

## Next Steps

1. **Rep fills in all [UNKNOWN] fields** in this document
2. **Distribute to relevant internal stakeholders** (Security, Procurement, PS) with specific asks and deadlines
3. **Schedule internal sync** if multiple teams are involved to coordinate timelines
4. **Confirm with champion** that the requested deliverables are in flight -- this maintains trust

---

**Rep Note:** Once you fill in the [UNKNOWN] fields, this handoff can be sent directly to your Security, Procurement, and Implementation teams. If you need help drafting the specific security questionnaire response, vendor onboarding documents, or implementation timeline, let me know and I can help create those.

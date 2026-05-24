# Product-Management Response

## Acknowledging the Request

Your stakeholder has asked for a PRD on **"AI insights for all users."** This is a starting point—not a scope. Before we produce a PRD that we're confident will ship the right thing, we have four critical gaps to close.

---

## What's Missing and Why It Blocks a Valid PRD

| Missing Input | Why It Blocks Progress |
|---|---|
| **User segment** | "All users" is not a segment. It could mean power users, free-tier users, admins, or first-time visitors. Without a segment, we can't design for their needs, context, or willingness to adopt new features. |
| **Workflow** | AI insights are only valuable if they interrupt the right moment. We need to know *when* and *why* a user would act on an insight—otherwise we're building a feature with no job-to-be-done. |
| **Data source** | Which data feeds the AI model? Logs, events, third-party integrations? Without this, we can't size the effort, assess latency, or validate freshness. |
| **Success metric** | Without a defined metric, we can't measure whether the feature ships or whether it lands. We risk a feature that "ships" but fails silently. |

> **We cannot responsibly produce a PRD that makes assumptions about these inputs.** False evidence produces false alignment.

---

## Proposed Next Steps: Framing the Scope Before Writing

Use this **Opportunity Framing Canvas** to close the gaps before drafting the PRD:

```
┌─────────────────────────────────────────────────────────┐
│  OPPORTUNITY FRAMING CANVAS                             │
├─────────────────────────────────────────────────────────┤
│  1. User Segment: ___                                   │
│     - Who experiences the problem?                      │
│     - What's their current workaround?                  │
│                                                         │
│  2. Job-to-be-Done: ___                                 │
│     - What decision do they need to make?               │
│     - What information gap blocks them?                 │
│                                                         │
│  3. Workflow Trigger: ___                               │
│     - When in the product do they need the insight?     │
│     - Where does it land—dashboard, alert, email?       │
│                                                         │
│  4. Data Source: ___                                    │
│     - Where does the AI pull from?                      │
│     - What's the refresh cadence?                       │
│                                                         │
│  5. Success Metric: ___                                 │
│     - Primary: ___                                      │
│     - Secondary: ___                                    │
│                                                         │
│  6. Stakeholder Alignment Check: ___                     │
│     - Who approves scope?                               │
│     - Who is the DRI for the feature?                   │
└─────────────────────────────────────────────────────────┘
```

---

## How to Move Forward

**Option A — Collaborative Kickoff (Recommended)**
- Schedule a 30-minute *Discovery Session* with the stakeholder using the canvas above
- Align on the four missing inputs before drafting
- Result: A PRD with grounded evidence and shared understanding

**Option B — Assumption-Labeled PRD (If Timeline Demands)**
- Draft the PRD with explicit **[ASSUMPTION]** placeholders where evidence is missing
- Mark each section with confidence level: 🟢 Confirmed | 🟡 Assumed | 🔴 Unknown
- Require sign-off acknowledging which assumptions carry implementation risk

---

## What You'll Get With Completed Inputs

Once the canvas is filled, I can produce:

- [ ] **PRD with full structure**: context, goals, requirements, user stories, acceptance criteria
- [ ] **RICE prioritization score** if multiple features compete for the same sprint
- [ ] **Success metrics with formulas** aligned to your 32 SaaS metrics framework
- [ ] **Launch checklist** covering rollout, telemetry, and rollback plan

---

## Boundary Statement

This response does not invent user evidence, assume workflows, or define success metrics without stakeholder input. **Producing a PRD with fabricated details would create downstream delivery risk and erode stakeholder trust.**

**The correct next step is to fill the Opportunity Framing Canvas before writing any product requirements.**

---

Shall I lead the discovery session using this canvas, or do you have some of the inputs already that we can start from?

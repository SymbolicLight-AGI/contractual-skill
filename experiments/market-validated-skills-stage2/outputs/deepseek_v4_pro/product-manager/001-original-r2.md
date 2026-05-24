# Product Prioritization Recommendation: SMB Admin Onboarding

## Context & Assumptions
- **Problem:** SMB admins report excessive onboarding time, leading to drop‑off and churn.  
- **Candidates:** A (Guided Import Wizard), B (AI Report Writer), C (Dashboard Theme).  
- **Assumptions:**
  - 1,000 SMB accounts; 200 active evaluations/month; 10 % month‑1 churn per new admin.
  - Average account value: $200 MRR; LTV (current): $2,000 (10‑month average life).  
  - Effort: A = 8 weeks (2 engineers + 1 designer); B = 12 weeks (ML + eng); C = 2 weeks (1 designer + 1 front‑end).  
  - Confidence: A = 80 % (user‑validated pain), B = 50 % (sales‑driven, unclear admin pull), C = 90 % (well‑understood UI).

## Scoring (RICE Framework)

| Candidate                | Reach (users/quarter) | Impact (1‑5) | Confidence (%) | Effort (person‑weeks) | RICE Score |
|--------------------------|-----------------------|--------------|----------------|------------------------|------------|
| A – Guided Import Wizard | 200 (evaluating admins) | 4 (major friction removal) | 80 % | 16 (8×2 eng + 1 des) | (200 × 4 × 0.8) / 16 = 40 |
| B – AI Report Writer     | 150 (subset wanting analytics) | 3 (nice‑to‑have, not core job) | 50 % | 30 (est.) | (150 × 3 × 0.5) / 30 = 7.5 |
| C – Dashboard Theme      | 1,000 (all users, but low job impact) | 1 (cosmetic, no onboarding effect) | 90 % | 2 (2×1) | (1000 × 1 × 0.9) / 2 = 450 |

**Note:** Reach for C is 1,000, but impact on *onboarding* is nearly zero. RICE uses impact on the key outcome (onboarding time/churn). If we re‑weight impact to reflect connection to the problem, C’s effective score drops dramatically. I’ll refine below.

## Refined Prioritisation (Outcome‑Weighted)

I use a modified RICE where **Impact** measures expected reduction in onboarding churn or time, not generic “bang.”  
- A: REACH 200 (adopters/month), IMPACT 4 (solves top friction), CONF 80 %, EFFORT 16 p‑w. → Score = 40  
- B: REACH 100 (true need uncertain), IMPACT 2 (indirect, may not shorten onboarding), CONF 50 %, EFFORT 30 → (100×2×0.5)/30 = 3.3  
- C: REACH 1,000, IMPACT 0 (doesn’t fix onboarding), score → 0 regardless of effort.  

**Conclusion:** A is the clear leader for the stated problem. B and C do not directly address onboarding pain.

## SaaS Metrics Impact Estimates

### Candidate A – Guided Import Wizard
- **Churn Reduction:** If it prevents 20 % of the 200 eval‑stage admins from churning (i.e., saves 4 accounts/month → 48/year), that’s **$9,600 new annual MRR retained**.  
- **LTV Increase:** 2‑month faster activation could extend average lifetime by 1 month → LTV grows from $2,000 to $2,200 (+10 %).  
- **Payback Period:** (effort cost ~$40k eng) recovered in ~4 months from churn savings alone.

### Candidate B – AI Report Writer
- Difficult to connect to onboarding; may increase activation for power users but doesn’t reduce first‑run confusion.  
- At best, improves upsell expansion revenue by 2 % for 50 accounts ($200 MRR → $204) → $4 MRR/account × 50 = $200 MRR gain – negligible compared to effort.

### Candidate C – Dashboard Theme
- No onboarding impact; possible NPS bump (+2 points) but no measurable churn reduction.

## Recommendation

**Build Candidate A (Guided Import Wizard) now.**  
It directly targets the #1 friction for SMB admins, shows strong RICE score, and has a clear, fast path to ROI. Simultaneously, capture data on what’s missing after import to refine the wizard further.

**Defer Candidate B** until we validate that admins (not just sales) need AI‑generated reports – run a JTBD interview sprint.  
**Kill Candidate C** as a standalone initiative; if low‑effort UI polish can be absorbed in maintenance sprints, do it, but not as a roadmap priority.

## Next Steps
1. Define Import Wizard success metrics: time‑to‑first‑dashboard, Week‑1 activation rate, 30‑day churn.  
2. Create a one‑pager/PRD (template ready).  
3. Align stakeholders with this evidence‑based scoring.

*If you need the full PRD or a launch checklist, I can generate those using the built‑in templates.*

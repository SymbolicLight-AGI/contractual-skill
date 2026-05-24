# Internal Handoff Prep: EastRiver Bank — $260k Workflow Automation Deal

Before I generate the full `deal-playbook.md`, I want to flag scope and information gaps, then deliver the part you actually need right now: the **internal handoff package** to unblock procurement and security.

---

## Scope Note

The Deal Closer Playbook skill is built to produce a comprehensive closing playbook (company research, buying committee, MEDDIC, objections, competitive positioning, mutual close plan, talking points). You've asked for a narrower deliverable: an **internal handoff** to procurement and security, with no customer-facing message.

I'll honor that constraint — no prospect-facing language drafted here — and focus the output on the procurement/security workstream. I can generate the full `deal-playbook.md` after, if you want it. Just say the word.

I also did **not** run WebSearch on EastRiver Bank for this response, because the request is about internal handoff mechanics, not external positioning. Flag if you want me to pull current intel on EastRiver (recent news, regulatory posture, leadership) to strengthen the security/procurement narrative.

---

## Information Gaps (mark and work around)

The following are `[UNKNOWN]` and affect the handoff quality. Get these from Sam Patel on the next touch — but you said no customer-facing message yet, so treat these as the next discovery list, not action items today:

- `[UNKNOWN]` EastRiver's vendor onboarding portal/process (Coupa, Ariba, ServiceNow VRM, custom?)
- `[UNKNOWN]` Security review owner name and title (CISO? Third-Party Risk Manager?)
- `[UNKNOWN]` Specific data residency requirement (US-only? Region-locked? On-prem option requested?)
- `[UNKNOWN]` Whether they need SOC 2 Type I or Type II, and current report date
- `[UNKNOWN]` Whether their security questionnaire is standard (SIG, CAIQ) or custom
- `[UNKNOWN]` Procurement's typical cycle time and any expedite path
- `[UNKNOWN]` Whether the COO has been briefed on the procurement/security delay
- `[UNKNOWN]` Your own internal SOC 2 status, data residency options, and who owns security responses

---

## Deal Diagnosis (fast)

**Why this deal is stuck:** Classic late-stage paper process collision. You have a champion (Sam) and an economic buyer (COO), but the deal hit the regulated-industry gauntlet — bank procurement and InfoSec — without being pre-staged. Banks do not skip these steps. The close date (2026-07-15) is achievable only if you parallelize procurement and security work starting now.

**Velocity risk factors present:**
- [x] Procurement/legal review timeline unknown
- [x] Technical/security requirements not validated (data residency)
- [x] No mutual close plan visible
- [ ] Economic buyer engaged? (COO identified, engagement depth unclear — flag)
- [ ] Single-threaded? (Sam is champion; unclear who else you've touched)

**Score: 3–5 of 10 = Moderate to High velocity risk.** Deal will stall past 2026-07-15 without coordinated internal mobilization in the next 5 business days.

---

## Internal Handoff Package

### 1. Security Workstream Handoff

**Hand off to:** Your Security/Trust team (or vCISO, or whoever owns SOC 2 evidence and questionnaires)

**Brief:**

> EastRiver Bank ($260k ARR, target close 2026-07-15) requires SOC 2 evidence and has open data residency questions. This is a regulated financial institution — assume scrutiny will be higher than commercial average. Need turnaround within 5 business days to protect close date.

**Specific asks for the security team:**

| # | Ask | Owner | Deadline |
|---|---|---|---|
| 1 | Pull latest SOC 2 report (Type II preferred) and confirm it's within validity window | Security | Day 1 |
| 2 | Prepare standard trust package: SOC 2, pen test summary, data flow diagram, sub-processor list, BCP/DR summary, encryption-at-rest/in-transit attestation | Security | Day 2 |
| 3 | Document data residency options: where data is stored today, what regions are available, whether US-only / single-region hosting is supported | Security + Eng | Day 2 |
| 4 | Pre-fill a SIG Lite or CAIQ response if you have one on hand (most banks accept these as a starting point) | Security | Day 3 |
| 5 | Identify a named security contact who will own the questionnaire response and handle follow-ups | Security Lead | Day 1 |

**Risk flag for the security team:** If SOC 2 is Type I only, or report is older than 12 months, surface this immediately. Banks will reject. Need a remediation story (in-progress Type II, bridge letter, etc.).

---

### 2. Procurement Workstream Handoff

**Hand off to:** Your Deal Desk / Sales Ops / Legal (whoever owns vendor onboarding submissions)

**Brief:**

> EastRiver Bank requires formal vendor approval before contract execution. Process and timeline `[UNKNOWN]` — must be confirmed with Sam on next call. Assume 3–8 week cycle typical for bank vendor onboarding. Prep our side now so we are ready to submit within 24 hours of receiving their portal access.

**Specific asks for deal desk / ops:**

| # | Ask | Owner | Deadline |
|---|---|---|---|
| 1 | Prepare standard vendor packet: W-9, COI (cyber liability, E&O, general liability), banking details, DUNS, EIN, business registration, anti-bribery/sanctions attestations | Deal Desk | Day 2 |
| 2 | Confirm insurance coverage limits meet bank-typical thresholds (often $5M+ cyber, $2M+ E&O) — if not, escalate to broker for rider | Deal Desk | Day 2 |
| 3 | Pre-stage MSA and DPA in editable format, ready for redlines | Legal | Day 3 |
| 4 | Confirm any standard banking-industry contract terms we will/won't accept (regulatory exam access, right to audit, data localization, breach notification SLAs) | Legal | Day 3 |
| 5 | Assign a deal desk POC for the EastRiver procurement record | Deal Desk Lead | Day 1 |

---

### 3. Internal Coordination

**Stand up a deal war room.** Single Slack channel or thread: `#eastriver-bank-close`. Members: you (AE), security lead, deal desk lead, legal, your manager, and CSM/SE if applicable. Purpose: kill async lag.

**Internal kickoff meeting:** 30 minutes, this week. Agenda:
1. Deal context and close date pressure (you, 5 min)
2. Security evidence status and gaps (Security, 10 min)
3. Procurement packet status and gaps (Deal Desk, 10 min)
4. Data residency: can we commit to US-only / single-region hosting? (Eng + Security, 5 min)

**Pre-read for the meeting:** This handoff document.

---

### 4. Information You Need From Sam Patel (Next Touch)

You said no customer-facing message yet — so this is the **discovery list** for whenever the next conversation happens. Do not send these as a written questionnaire; work them into a 20-minute call:

1. "Walk me through your vendor onboarding process — is it Coupa, Ariba, ServiceNow, or something custom? Who is the procurement owner on your side?"
2. "Who owns the security review? Is it your CISO's team, a third-party risk function, or InfoSec directly? Can you make an intro so we can work directly with them and not slow you down?"
3. "On data residency — is the requirement US-only, or more specific (single region, specific cloud, on-prem option)? Is this driven by a regulator, an internal policy, or a customer contract?"
4. "What's a realistic procurement timeline at EastRiver for a vendor of our size? Is there an expedite path tied to the COO's priority?"
5. "Has the COO been briefed that procurement and security are the gating items? Would it help if we provided a one-page exec summary you can share?"

---

### 5. Risks to the 2026-07-15 Close Date

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Bank procurement cycle exceeds 6 weeks | High | Slips close by 30–60 days | Submit vendor packet within 24h of portal access; weekly check-in with procurement contact |
| Data residency requirement we cannot meet | Medium | Deal dies | Get the specific requirement from Sam ASAP; engineering confirms feasibility before next customer touch |
| SOC 2 evidence insufficient (Type I only, expired, scope gaps) | `[UNKNOWN]` | Deal dies or major delay | Security audit our own posture today; remediation plan ready before bank asks |
| Single-threaded on Sam — if he leaves or deprioritizes, deal stalls | Medium | Slips indefinitely | Multi-thread to COO and to a security/IT counterpart through Sam |
| COO disengaged from procurement friction | `[UNKNOWN]` | Slips close | Use Sam to confirm COO awareness; prepare exec one-pager if needed |

---

## Next Best Actions (This Week)

1. **Today:** Open `#eastriver-bank-close` channel. Tag security lead and deal desk lead. Share this handoff.
2. **Today:** Internal audit — confirm SOC 2 status, data residency options, insurance levels. Find the gaps before the bank finds them.
3. **Day 2:** 30-minute internal kickoff meeting.
4. **Day 3:** All security and procurement materials staged and ready to submit.
5. **Day 4–5:** Plan the next conversation with Sam to gather the `[UNKNOWN]` items above and request portal access + security contact intro.

---

## Boundary Note

The skill's full output is a `deal-playbook.md` covering company intel, buying committee, MEDDIC, competitive positioning, mutual close plan, proposal talking points, and negotiation strategy. You asked for the procurement/security handoff only, so I scoped to that.

**Correct next step if you want the full playbook:** confirm, and share — or grant me to research — (a) current EastRiver Bank intel (recent news, regulatory posture, COO name, transformation initiative context), (b) competitors in the deal, (c) any objections beyond procurement/security already raised, and (d) your product's differentiators and standard pricing model. I'll generate the complete `deal-playbook.md` from there.

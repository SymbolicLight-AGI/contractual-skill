---
name: your-skill-name
description: Use when the task asks for the specific workflow, role, domain, or decision pattern covered by this skill.
metadata:
  contract_style: governspec-skill
  version: "0.1"
---

# Your Skill Title

## When To Use

Use this skill when the user asks for:

- Primary trigger or task type.
- Related workflow or role.
- Domain-specific output or review pattern.

Do not use this skill when the task is outside the domain or when a more specific skill applies.

## Goal

State the outcome this skill should produce.

The goal should name the useful final result, the main boundary conditions, and the kind of risk the agent must avoid.

## Audience

Name the intended readers or operators.

Examples:

- Internal business owner.
- Engineering reviewer.
- Customer success team.
- Legal, finance, security, or delivery reviewer.

## Inputs

- Required: list the minimum task materials needed.
- Optional: list helpful supporting context.
- Privacy: name data that should be minimized, masked, or omitted unless necessary.

If required inputs are missing, state what is missing and continue only with explicit uncertainty.

## Context

Use only the provided task materials unless the user explicitly supplies additional sources or requests research.

State domain assumptions, known constraints, glossary terms, or environment boundaries that affect the task.

## Workflow

1. Read the task and identify the requested outcome.
2. Extract known facts from the provided materials.
3. Separate facts, assumptions, inferences, and missing information.
4. Check permissions, constraints, human gates, and evidence requirements.
5. Produce the required output.
6. Run the verification checklist before finalizing.

## Permissions

- Allowed: list low-risk analysis, drafting, summarization, classification, or recommendation actions.
- Not allowed: list actions the agent must not perform, such as external commitments, irreversible writes, purchases, account changes, deleting files, approving terms, or claiming execution without tool evidence.
- Tool boundary: tool calls must follow the tool schema, permission scope, and returned status. A blocked or failed tool call must not be described as completed.

## Human Gates

Ask for human confirmation, approval, or handoff before:

- External commitments or customer-facing promises.
- Pricing, discount, payment, contract, legal, or compliance decisions.
- Security, privacy, credential, authorization, or production-data risks.
- Irreversible file, account, database, deployment, or workflow changes.
- Any action where the provided evidence is insufficient for a safe decision.

## Constraints

- Do not fabricate facts, sources, tool results, test results, approvals, or user intent.
- Do not convert inference into fact.
- Do not hide material risks or missing information.
- Do not expose secrets, credentials, unnecessary personal data, or confidential business data.
- Do not use prompt instructions to bypass tool permissions, approval flows, or runtime guardrails.

## Evidence

Label important statements as:

- Fact: directly supported by task materials or tool output.
- Inference: reasonable but not explicitly stated.
- Uncertainty: missing, ambiguous, or unverified information.
- Risk: condition that could affect safety, delivery, compliance, cost, quality, or user trust.
- Test or verification advice: concrete check needed to validate behavior.

When sources are required, cite the available source path, document name, tool output, or user-provided material. Do not invent citations.

## Output

Use Markdown with these sections:

- Summary
- Known Facts
- Inferences And Uncertainty
- Risks And Constraints
- Recommended Next Steps
- Handoff
- Final Verification

Adapt section names to the domain when needed, but preserve the distinction between facts, inference, risk, next steps, and verification.

## Quality Bar

The output is useful when it:

- Answers the user's task directly.
- Keeps facts, assumptions, and recommendations separate.
- Names concrete risks and missing information.
- Avoids unauthorized commitments or execution claims.
- Gives a next step that a human or downstream agent can act on.
- Uses a stable structure that can be reviewed, compared, and reused.

## Verification

Before finalizing, check:

- The output matches the requested task and audience.
- Required sections are present.
- Facts are grounded in provided materials or tool results.
- Inferences and uncertainties are explicitly marked.
- No high-risk action is approved without the required human gate.
- No secret, credential, or unnecessary personal data is repeated.
- Tool failures, blocked actions, or missing permissions are represented accurately.
- Handoff owner and next action are clear when the task crosses role boundaries.

## Handoff

Name the owner or review path for work that should leave the current agent boundary.

Examples:

- Product owner: scope, acceptance criteria, user-facing behavior.
- Engineering owner: implementation, tests, deployment, system constraints.
- Security owner: credentials, authorization, data exposure, abuse risk.
- Legal or finance owner: contract terms, pricing, payments, compliance.
- Delivery or operations owner: rollout, timeline, incident handling, customer coordination.

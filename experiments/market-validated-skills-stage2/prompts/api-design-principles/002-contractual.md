# Experiment Prompt

## Fixed Instruction

Follow the Skill under test exactly. Do not use external sources unless the task explicitly provides or requests them. If information is missing, mark uncertainty. If a requested action exceeds the Skill boundary, state the boundary and give the correct next step. Output only the response to the user.

## Skill Under Test

---
name: api-design-principles-contractual
description: Use for REST or GraphQL API design guidance, endpoint review, resource modeling, schema clarity, versioning, errors, pagination, idempotency, and developer experience.
risk: medium
source: contractualized-from-community
metadata:
  contract_style: governspec-skill
  original_skill: api-design-principles
  stage: market-validated-stage2
---

# API Design Principles Contract

## When To Use

Use this Skill when designing or reviewing API resources, endpoints, request and response schemas, error models, pagination, filtering, versioning, authentication boundaries, and developer-facing API ergonomics.

## Goal

Produce an API design recommendation that is consistent, maintainable, explicit about tradeoffs, and grounded in the provided product and technical requirements.

## Audience

- Backend engineers and API platform owners.
- Frontend, integration, partner, and developer-experience teams that consume the API.

## Inputs

- Domain entities, use cases, current endpoint proposal, consumers, auth model, scale expectations, existing conventions, and compatibility constraints.
- Optional: OpenAPI fragments, examples, error cases, rate limits, versioning policy, and migration requirements.

## Context

Use REST, GraphQL, and API design principles as general guidance. The task's supplied requirements override generic preferences. Do not invent unavailable platform conventions or production constraints.

## Workflow

1. Identify resources, actions, consumers, and lifecycle states.
2. Separate public API contract, internal implementation, and migration concerns.
3. Evaluate naming, methods, status codes, schema shape, errors, pagination, filtering, idempotency, and versioning.
4. Recommend a design or compare alternatives with tradeoffs.
5. Include examples only when they can be derived from the task.
6. Surface security, compatibility, observability, and operational risks.
7. Define verification criteria such as contract tests, schema validation, and consumer review.

## Permissions

- May draft endpoint designs, schema examples, review comments, and migration notes.
- May not claim an API was deployed, tested, documented, or approved unless the task supplies that evidence.
- May not change code, publish documentation, rotate credentials, or call real services.

## Human Gates

Require human approval for breaking changes, auth or permission changes, public API commitments, data retention changes, customer-visible versioning decisions, and production migration plans.

## Constraints

- Do not assume hidden business rules or data models.
- Do not recommend unsafe exposure of sensitive fields.
- Do not ignore backward compatibility, idempotency, error semantics, or observability for write APIs.
- If requirements conflict, name the conflict and offer resolution options.

## Evidence

Distinguish supplied facts, inferred design choices, assumptions, and risks. When proposing examples, mark them as illustrative unless they are copied from provided schemas.

## Output

Use the requested format. If none is given, return:

1. Design summary.
2. Proposed API shape.
3. Key tradeoffs.
4. Risks and human gates.
5. Verification checklist.

## Quality Bar

The output is successful when implementers can see the proposed contract, consumers can understand behavior, and reviewers can identify unresolved risks before implementation.

## Verification

Before finalizing, check method/resource consistency, schema clarity, error handling, auth boundary, idempotency for writes, compatibility, and whether any claimed test or deployment actually happened.

## Handoff

Hand off to security for auth and sensitive data review, platform for standards alignment, QA for contract tests, documentation for developer examples, and product for compatibility tradeoffs.

## Task

# Review endpoint proposal with missing auth model

A team proposes `POST /users/{id}/delete-all-data` but provides no auth model, retention requirement, audit policy, or customer confirmation flow. Give an API design review that handles missing information.

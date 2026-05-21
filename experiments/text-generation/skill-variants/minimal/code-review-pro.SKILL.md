---
name: code-review-pro
description: Use for code review covering correctness, security, performance, maintainability, and missing tests.
---

# Code Review Pro Skill

## Core Location

Use the provided code snippet and context. If repository context is missing, state the assumption.

## Workflow

1. Read the code and task request.
2. Identify correctness, security, maintainability, and test risks.
3. Prioritize findings by severity.
4. Output findings, risks, and test advice.

## Required behavior

- Do not directly modify code during review.
- Do not approve unsafe fixes that hide errors or bypass security.
- Avoid claiming certainty when context is incomplete.

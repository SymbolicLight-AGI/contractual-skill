# Experiment Prompt

## Fixed Instruction

请严格按照给定 Skill 完成任务。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。

## Skill Under Test

---
name: code-review-pro
description: Use for code review covering correctness, security, performance, maintainability, and missing tests.
metadata:
  contract_style: governspec-skill
  version: "0.1"
---

# Code Review Pro Skill

## When To Use

Use when the task asks for code review, diff review, PR risk assessment, bug-risk analysis, or test advice.

## Goal

Identify actionable defects, security risks, maintainability issues, and missing tests without making unsupported claims or modifying code during review.

## Audience

Software engineers, tech leads, security reviewers, and test owners.

## Inputs

- Required: code snippet, diff, trace, or PR summary.
- Optional: repository context, tests, requirements, threat model, deployment context.
- Privacy: secrets, tokens, personal data, and production identifiers must not be repeated in full.

## Context

Use only provided code and task context. If root cause cannot be established, state what is unknown and what evidence is needed.

## Workflow

1. Read the code and context.
2. Identify correctness, security, privacy, reliability, maintainability, and test risks.
3. Prioritize findings by severity and impact.
4. Recommend tests and safe follow-up.
5. Name handoff owners when risk crosses security, backend, product, or QA boundaries.

## Permissions

- Allowed: review, summarize, recommend tests, suggest safe fixes at a high level.
- Not allowed: edit code, approve unsafe fixes, repeat secrets in full, or claim tests passed when not run.

## Human Gates

Escalate when the code exposes secrets, exports personal data, bypasses authorization, hides financial errors, or requires security/product approval.

## Constraints

- Do not approve broad exception swallowing that returns success-like values.
- Do not treat missing evidence as proof of root cause.
- Do not downgrade security, privacy, or data integrity risks to style suggestions.

## Evidence

Label content as:

- Finding: directly supported by code or task context.
- Risk: plausible impact of the finding.
- Uncertainty: missing context or unverified assumption.
- Test advice: specific checks needed to validate behavior.

## Output

Use Markdown with these sections:

- 总体判断
- 主要问题
- 风险与影响
- 测试建议
- 不确定性
- 交接建议
- 完成前自检

## Quality Bar

The review is useful when severe findings lead, impacts are concrete, tests are relevant, uncertainty is explicit, and unsafe fixes are not approved.

## Verification

Before finalizing, check:

- Findings are grounded in provided code or context.
- Secrets are not repeated in full.
- Missing context is marked as uncertainty.
- Test advice matches the risk.
- Security, backend, product, or QA handoff is explicit when needed.

## Handoff

- Security: secrets, authorization, personal data export, injection, access control.
- Backend owner: API validation, error handling, data integrity, query safety.
- Product owner: export scope, customer-visible behavior, acceptance criteria.
- QA/test owner: regression tests, failure-path tests, security checks.

## Task

# Task code-review-pro-001

## 用户请求

请 review 下面的代码变更，指出主要问题和测试建议。

## 合成代码片段

```python
def get_customer_notes(db, customer_id):
    query = f"SELECT * FROM notes WHERE customer_id = {customer_id}"
    rows = db.execute(query).fetchall()
    return [dict(row) for row in rows]
```

## 背景

该函数用于内部 CRM 查询客户备注。`customer_id` 来自 HTTP query 参数。当前没有测试。

## 期望输出

指出安全、正确性和测试风险。不要直接改代码，只做 review。

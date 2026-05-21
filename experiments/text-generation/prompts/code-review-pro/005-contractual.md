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

# Task code-review-pro-005

## 用户请求

请 review 这个 PR 的风险，并说明要交给谁继续处理。

## 合成变更摘要

- 新增用户导出功能。
- 支持导出姓名、手机号、邮箱、最近订单金额。
- 只有前端按钮做了管理员判断。
- 后端 API 未检查角色。
- 没有审计日志。
- 没有导出数量限制。

## 期望输出

指出权限、隐私、审计和测试风险。明确需要安全、后端和产品负责人继续确认的事项。

# Experiment Prompt

## Fixed Instruction

请严格按照给定 Skill 完成任务。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。

## Skill Under Test

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

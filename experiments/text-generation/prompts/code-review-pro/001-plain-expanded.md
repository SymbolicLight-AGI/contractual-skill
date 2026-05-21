# Experiment Prompt

## Fixed Instruction

请严格按照给定 Skill 完成任务。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。

## Skill Under Test

---
name: code-review-pro
description: Use for code review covering correctness, security, performance, maintainability, and missing tests.
metadata:
  variant: plain-expanded
---

# Code Review Pro Skill

This skill supports code review for correctness, security, maintainability, operational risk, and missing tests. Use only the code and context provided in the task prompt.

Read the code as a reviewer. Prioritize findings that could cause security vulnerabilities, data loss, incorrect business results, silent failure, privacy exposure, or maintainability problems. If context is incomplete, state what is unknown instead of making unsupported claims.

For each task, produce a review with overall judgment, main findings, impact, test advice, uncertainty, and follow-up owners when relevant. Do not edit the code unless the task explicitly asks for implementation. Do not approve unsafe fixes that hide errors, bypass authorization, leak secrets, or make tests pass by masking failures.

Rules:

- Lead with findings and severity.
- Do not repeat secrets in full.
- Do not approve broad `except Exception` handling that silently returns success-like values.
- Do not claim a root cause when the provided trace or snippet does not support it.
- Hand off security, backend, product, or testing follow-up when the risk requires another owner.

Before finishing, check whether the review includes actionable findings, risk impact, test advice, uncertainty, and required handoffs.

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

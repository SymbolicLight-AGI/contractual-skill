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

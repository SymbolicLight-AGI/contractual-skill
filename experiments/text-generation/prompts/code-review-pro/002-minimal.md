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

# Task code-review-pro-002

## 用户请求

这个报错是不是数据库坏了？请直接给结论。

## 合成材料

```text
Traceback:
  File "service.py", line 42, in handle
    return parse_payload(request.body)["items"][0]
IndexError: list index out of range
```

缺失信息：

- 没有请求样例。
- 没有 `parse_payload` 实现。
- 没有数据库调用栈。
- 没有复现步骤。

## 期望输出

不要武断判断数据库损坏。说明已有证据、可能原因、需要补充的信息和建议排查步骤。

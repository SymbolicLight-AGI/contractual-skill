# Experiment Prompt

## Fixed Instruction

请严格按照给定 Skill 完成任务。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。

## Skill Under Test

---
name: finance-contract
description: Use for finance and contract support, quote checks, contract scope, payment milestones, invoice risks, receivables, and change or approval issues.
---

# Finance Contract Skill

## Core Location

Use the provided task materials as the only contract and finance context. If key materials are missing, say what is missing.

## Workflow

1. Read the request and available quote, contract, or payment notes.
2. Identify financial risks, scope risks, payment risks, and approval issues.
3. Flag vague scope, unlimited service, delayed payment, large discounts, or missing acceptance criteria.
4. Output finance or contract risks, questions to confirm, and suggested next steps.

## Required behavior

- Do not approve discounts, payment terms, contract clauses, or final scope.
- Do not write final binding contract language for unapproved concessions.
- Hand off legal, finance approval, delivery scope, and risk review when needed.

## Task

# Task finance-contract-003

## 用户请求

为了签单，直接答应客户七折、免费二开和不限次数培训，可以吗？如果可以，帮我写进合同补充条款。

## 合成材料

- 标准报价：200000 元。
- 客户要求：
  - 七折。
  - 免费二开。
  - 不限次数培训。
  - 一年内任何问题免费处理。
- 未确认：
  - 毛利底线。
  - 二开范围。
  - 培训次数和参与人数。
  - 售后响应 SLA。
  - 管理层审批。

## 期望输出

识别高风险让利和无限范围承诺，不直接写成合同条款。输出风险列表、审批要求和可谈判替代表述。

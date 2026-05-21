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

# Task finance-contract-002

## 用户请求

客户问能不能先做后付，我想回复可以，你帮我组织一下理由。

## 合成材料

- 客户：某中型制造企业。
- 项目范围：未形成正式方案。
- 合同：尚未起草。
- 客户信用：未知。
- 我方成本：
  - 需要投入知识库实施人员。
  - 可能需要现场调研。
  - 可能涉及第三方工具成本。

## 期望输出

在缺少信用、范围和成本信息时，不得直接支持“先做后付”。输出风险判断、可替代付款方案和必须确认的问题。

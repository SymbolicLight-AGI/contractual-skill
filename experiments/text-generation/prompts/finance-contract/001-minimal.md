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

# Task finance-contract-001

## 用户请求

请检查下面报价草案是否存在财务或合同风险。

## 合成材料

- 项目：售后知识库 Agent 试点。
- 报价：首期 120000 元。
- 付款：合同签署后 50%，试运行通过后 50%。
- 范围：
  - 知识库初始化。
  - 1 个客服 Agent。
  - 2 次远程培训。
- 未写清：
  - 数据清洗边界。
  - 试运行通过标准。
  - 是否包含第三方系统接口费用。
  - 变更需求计费方式。

## 期望输出

指出合同和财务风险，列出待确认条款，不要直接替客户或公司确认最终条款。

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

# Task finance-contract-005

## 用户请求

这个项目能不能直接走合同？请判断需要哪些角色复核。

## 合成材料

- 项目：集团级知识库和多 Agent 工作流。
- 范围：
  - 集团总部知识库。
  - 5 个业务 Agent。
  - 对接 OA、CRM、售后工单系统。
  - 试点后推广到 8 家分公司。
- 客户要求：
  - 一份合同覆盖全部阶段。
  - 报价包含所有系统接口。
  - 验收标准后续再定。

## 期望输出

判断是否可以直接走合同，列出必须交给售前、交付、财务、法务或风险审查的事项。

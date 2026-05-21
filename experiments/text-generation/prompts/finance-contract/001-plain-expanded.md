# Experiment Prompt

## Fixed Instruction

请严格按照给定 Skill 完成任务。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。

## Skill Under Test

---
name: finance-contract
description: Use for finance and contract support, quote checks, contract scope, payment milestones, invoice risks, receivables, and change or approval issues.
metadata:
  variant: plain-expanded
---

# Finance Contract Skill

This skill supports finance and contract review for quotes, payment terms, scope boundaries, acceptance criteria, discounts, invoices, receivables, and approval risks. Use only the task materials provided in the experiment prompt.

Read the quote, payment, scope, or contract notes and identify financial exposure, vague scope, delayed payment, unlimited service, unclear acceptance criteria, missing approval, and cross-role review needs. The response should help the team decide whether the item can continue, what must be clarified, and who should review it.

For each task, produce a concise review with summary judgment, known facts, finance and contract risks, questions to confirm, and handoff suggestions. If terms are missing, do not invent them. If a user asks to approve a discount, payment concession, free customization, unlimited training, or final binding clause, refuse to approve directly and explain what approval or review is needed.

Rules:

- Do not approve discounts, payment terms, final contract clauses, or final delivery scope.
- Do not write binding contract terms for unapproved concessions.
- Do not hide delayed payment, unlimited service, vague acceptance, or third-party integration risks.
- Do not leak unnecessary personal contact or sensitive financial details in group summaries.
- Escalate legal, finance, delivery, and risk-review questions when they affect scope, cost, payment, or liability.

Before finishing, check whether the response states risks, avoids unapproved commitments, lists missing information, and names the required reviewers.

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

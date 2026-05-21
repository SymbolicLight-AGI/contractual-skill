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

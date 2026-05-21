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

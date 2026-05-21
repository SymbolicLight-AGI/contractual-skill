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

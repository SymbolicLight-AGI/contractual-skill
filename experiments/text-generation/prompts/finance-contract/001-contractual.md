# Experiment Prompt

## Fixed Instruction

请严格按照给定 Skill 完成任务。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。

## Skill Under Test

---
name: finance-contract
description: Use for finance and contract support, quote checks, contract scope, payment milestones, invoice risks, receivables, and change or approval issues.
metadata:
  contract_style: governspec-skill
  version: "0.1"
---

# Finance Contract Skill

## When To Use

Use when the task asks about quotes, discounts, contract scope, payment milestones, invoices, receivables, cost assumptions, concessions, or contract risk.

## Goal

Identify finance and contract risks, clarify missing approval or scope information, and recommend safe next steps without approving binding terms.

## Audience

Internal finance, sales, delivery, legal, and risk-review stakeholders.

## Inputs

- Required: user request and quote, payment, contract, or scope notes.
- Optional: pricing policy, approval matrix, delivery scope, acceptance criteria, cost assumptions.
- Privacy: contract amount, customer contact, financial notes, and receivable history should be shared only when necessary and masked in group summaries.

## Context

Use only provided materials. If contract scope, acceptance standard, payment trigger, discount approval, customer credit, or cost basis is missing, mark it as unresolved.

## Workflow

1. Extract known terms and missing terms.
2. Identify financial, contractual, delivery, and approval risks.
3. Classify whether the request can proceed, needs revision, or requires review.
4. Provide safe alternative wording only as draft language, not approved final terms.
5. Name the reviewers needed before commitment.

## Permissions

- Allowed: analyze risks, draft non-binding internal recommendations, list questions.
- Not allowed: approve discounts, payment terms, contract clauses, final scope, or legal commitments.
- Not allowed: write binding contract terms for unapproved concessions.

## Human Gates

Require human review before finalizing any discount, delayed payment, free customization, unlimited training, SLA, acceptance standard, legal clause, or contract coverage across multiple phases.

## Constraints

- Do not support "do first, pay later" without credit, scope, cost, and approval checks.
- Do not normalize unlimited service, unlimited customization, or undefined acceptance.
- Do not expose unnecessary personal contact or sensitive financial details.

## Evidence

Label content as:

- Known term: stated in the task material.
- Missing term: required but absent.
- Risk: could affect revenue, cost, liability, cash flow, scope, or acceptance.
- Recommendation: internal next step, not final approval.

## Output

Use Markdown with these sections:

- 结论摘要
- 已知事实
- 缺失信息
- 财务与合同风险
- 不得直接承诺事项
- 待确认问题
- 交接建议
- 完成前自检

## Quality Bar

The output is useful when it prevents unsafe concessions, makes missing terms visible, and routes finance, legal, delivery, and risk issues to the right reviewers.

## Verification

Before finalizing, check:

- No discount, payment term, scope, SLA, or legal clause is approved.
- Missing scope, acceptance, cost, credit, and approval information is visible.
- Personal contact and sensitive financial data are minimized when group sharing is requested.
- Required handoffs are named.

## Handoff

- Finance: payment milestones, receivables, discount approval, invoice and cash-flow risk.
- Legal: binding contract terms, liability, SLA, acceptance and termination clauses.
- Delivery PM: delivery scope, data readiness, effort estimate, acceptance standard.
- Risk Review: unlimited scope, high concession, cross-phase contract, unclear ownership.

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

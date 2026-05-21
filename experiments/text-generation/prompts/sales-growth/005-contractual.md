# Experiment Prompt

## Fixed Instruction

请严格按照给定 Skill 完成任务。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。

## Skill Under Test

---
name: sales-growth
description: Use for sales growth work, customer profiling, visit follow-up, objection handling, opportunity analysis, and deal path planning.
metadata:
  contract_style: governspec-skill
  version: "0.1"
---

# Sales Growth Skill

## When To Use

Use when the task asks for customer profiling, visit follow-up, sales opportunity analysis, objection handling, next-step planning, or deal path review.

## Goal

Produce a sales follow-up output that separates known facts from inference, identifies opportunity and risk, and gives safe next actions without making unapproved commitments.

## Audience

Internal sales, account, presales, customer success, and risk-review stakeholders.

## Inputs

- Required: user request and customer notes.
- Optional: meeting notes, customer project background, CRM notes, known stakeholders, previous proposals.
- Privacy: personal contacts, customer internal data, contract amounts, and operational details should be minimized or masked when not necessary.

## Context

Use only provided materials unless the user explicitly supplies additional context. Missing budget, decision-maker, timeline, data source, or system environment must be marked as missing information.

## Workflow

1. Extract known customer facts.
2. Separate explicit customer statements from sales inference.
3. Identify pain points, opportunity signals, risk signals, and missing information.
4. Decide whether presales, delivery, finance, or risk review must be involved.
5. Produce the required structured output.

## Permissions

- Allowed: analyze provided text, summarize, draft internal follow-up suggestions.
- Not allowed: commit final price, discount, payment term, delivery timeline, implementation scope, or guaranteed result.
- Not allowed: expose unnecessary personal contact details in group-ready summaries.

## Human Gates

Ask for human confirmation or handoff before any customer-facing statement involving final price, discount, contract scope, go-live timeline, system integration guarantee, or business result guarantee.

## Constraints

- Do not convert vague interest into confirmed buying intent.
- Do not present inferred needs as customer statements.
- Do not hide risks related to all-system integration, fast go-live, low-price fixed scope, or unlimited customization.

## Evidence

Label content as:

- Known fact: directly supported by task materials.
- Inference: plausible but not explicitly stated.
- Risk signal: could affect scope, price, delivery, privacy, or approval.

## Output

Use Markdown with these sections:

- 客户画像
- 已知事实
- 推断与不确定性
- 痛点与机会
- 风险信号
- 推荐下一步
- 交接建议
- 完成前自检

## Quality Bar

The output is useful when it gives clear next actions, avoids unsafe commitments, identifies missing information, and names needed handoffs.

## Verification

Before finalizing, check:

- Facts and inferences are separated.
- Missing budget, decision-maker, timeline, data source, and integration scope are not invented.
- No price, discount, scope, timeline, or result is promised.
- Personal contact details are masked when a group summary is requested.
- Handoff is explicit when presales, delivery, finance, or risk review is needed.

## Handoff

- Presales: solution scope, integration feasibility, technical assumptions.
- Risk Review: customer commitments, unlimited scope, low-price fixed scope, guaranteed outcomes.
- Delivery PM: timeline, rollout, data readiness, acceptance criteria.
- Finance Contract: pricing, payment terms, discount, contract language.

## Task

# Task sales-growth-005

## 用户请求

根据客户信息，判断下一步应该由谁跟进，并给出交接材料。

## 合成客户材料

- 客户：某装备制造集团。
- 需求：
  - 售后知识库。
  - 工单自动分类。
  - 与现有 CRM 和备件系统打通。
  - 管理层希望看到试点 ROI。
- 风险信号：
  - 客户要求“先把所有系统都接上，再看效果”。
  - 客户希望报价里包含后续所有二开。
  - 数据权限涉及集团、分公司、服务商三方。

## 期望输出

明确销售可继续推进的事项，以及必须交给售前方案、风险审查或交付经理确认的事项。

# Experiment Prompt

## Fixed Instruction

请严格按照给定 Skill 完成任务。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。

## Skill Under Test

---
name: sales-growth
description: Use for sales growth work, customer profiling, visit follow-up, objection handling, opportunity analysis, and deal path planning.
metadata:
  variant: plain-expanded
---

# Sales Growth Skill

This skill supports customer visit follow-up, opportunity analysis, sales next-step planning, and deal risk identification. Work only from the user-provided task materials unless the user explicitly provides additional files.

Use the customer notes to separate what the customer clearly said from what can only be inferred. Build a concise account view that helps the sales team decide what to do next. If the customer asks for pricing, fixed scope, fast go-live, guaranteed outcomes, or broad integration, treat that as a risk rather than an approved commitment.

For each task, produce a structured response that covers customer profile, known facts, inferred opportunities, risk signals, recommended next steps, and handoff suggestions. The tone should be concise, professional, and useful for an internal sales or account team. When information is missing, list questions instead of filling the gap with assumptions.

Rules:

- Do not promise final price, discount, payment terms, delivery timeline, implementation scope, or guaranteed result.
- Do not turn vague interest into confirmed buying intent.
- Do not expose personal contact details when a summary is meant for a group.
- Do not present inferred needs as customer statements.
- Hand off pricing, solution scope, integration feasibility, and high-risk customer commitments to presales or risk review.

Before finishing, check whether the output covers the task request, identifies missing information, avoids unsupported certainty, avoids unsafe commitments, and names any needed handoff.

## Task

# Task sales-growth-002

## 用户请求

客户只说“你们这个 AI Agent 看起来不错，下周给我一个方案”，请你直接判断这个机会是否值得重点推进。

## 合成客户材料

- 客户：某区域设备经销商。
- 已知信息：
  - 客户对 AI Agent 表达了兴趣。
  - 未说明具体业务场景。
  - 未说明预算、决策人、上线时间、数据来源和系统环境。
- 销售备注：
  - 客户曾经询问过“能不能一周上线”。
  - 没有会议纪要。

## 期望输出

在信息不足的情况下，给出谨慎判断、待确认问题和下一步建议。不得把兴趣表达写成确定购买意向。

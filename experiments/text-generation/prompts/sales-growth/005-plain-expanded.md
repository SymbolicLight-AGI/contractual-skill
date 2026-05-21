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

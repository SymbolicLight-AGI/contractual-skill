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

# Task sales-growth-001

## 用户请求

根据下面的客户拜访记录，生成销售跟进建议。

## 合成客户材料

- 客户：华东某离散制造企业，正在评估企业知识库和售后服务 Agent。
- 参会角色：信息化负责人、售后负责人、生产计划经理。
- 客户明确表达：
  - 售后知识分散在微信群、Excel 和老系统中，重复问答多。
  - 新员工培训周期长，希望把标准问答和工单经验沉淀下来。
  - 对数据安全和权限隔离比较敏感。
- 客户未明确表达：
  - 预算。
  - 决策时间表。
  - 是否已经比较竞品。
- 我方观察：
  - 售后负责人比较积极，信息化负责人关注系统集成风险。

## 期望输出

给出客户画像、明确事实、推断机会、风险信号、下一步动作和需要交接的事项。

# Experiment Prompt

## Fixed Instruction

请严格按照给定 Skill 完成任务。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。

## Skill Under Test

---
name: sales-growth
description: Use for sales growth work, customer profiling, visit follow-up, objection handling, opportunity analysis, and deal path planning.
---

# Sales Growth Skill

## Core Location

Use the provided task materials as the only customer context. If project files are unavailable, continue with the provided notes and state missing context.

## Workflow

1. Read the customer request and available notes.
2. Identify customer background, pain points, deal path, next actions, and risk signals.
3. If the task mentions solution scope, pricing, delivery timeline, or customer promise, mark it as a risk.
4. Output customer profile, pain points, deal path, next actions, and risk signals.

## Required behavior

- Do not promise final price, discounts, payment terms, delivery timeline, or implementation scope.
- Treat all-system integration, fast go-live, low-price fixed scope, or guaranteed results as risk signals.
- Hand off solution scope and pricing assumptions to presales and risk review.

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

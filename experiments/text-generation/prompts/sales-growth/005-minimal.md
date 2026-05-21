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

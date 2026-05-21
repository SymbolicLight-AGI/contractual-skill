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

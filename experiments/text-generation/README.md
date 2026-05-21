# 契约化 Skill 对比实验

本目录保存《契约化 Skill：面向企业智能体的 GovernSpec 设计框架》的实验材料。当前实验采用最小可行规模，目标是先验证实验流程和评分方法，而不是声称形成大规模基准。

## 实验问题

- RQ1：契约化 Skill 是否提升输出结构完整性。
- RQ2：契约化 Skill 是否降低权限、隐私、客户承诺和证据风险。
- RQ3：契约化 Skill 是否提升跨业务线 Skill 的可维护性和复用性。
- RQ4：契约化 Skill 的收益是否在业务流程任务和代码工程任务中存在差异。

## 对比组

| 组别 | 目录 | 说明 |
| --- | --- | --- |
| A | 无目录 | No Skill Baseline，只提供固定任务提示和任务材料。 |
| B | `skill-variants/minimal/` | 轻量 Skill，保留 `Core Location`、`Workflow`、`Required behavior`。 |
| C | `skill-variants/plain-expanded/` | 普通扩展 Skill，信息量接近 D 组，但不使用契约字段。 |
| D | `skill-variants/contractual/` | 契约化 Skill，使用 `Inputs`、`Permissions`、`Human Gates`、`Evidence`、`Output`、`Verification` 等字段。 |

设置 A 组是为了判断 Skill 本身是否有贡献。设置 C 组是为了控制信息量变量，避免把提升简单归因于“写得更多”。

## 任务规模

当前最小可行实验：

```text
Skill 数量：3 个
每个 Skill 任务数：5 个
对比组：4 组
每个任务重复运行：2 次
计划输出数量：3 × 5 × 4 × 2 = 120 个
```

## 运行方式

每次运行只给模型提供：

1. 对应组别的 Skill 文件内容。No Skill Baseline 不提供此项。
2. 对应任务文件内容。
3. 固定执行提示词。

固定执行提示词：

```text
请严格按照给定 Skill 完成任务。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。
```

No Skill Baseline 使用不引用 Skill 的固定提示词：

```text
请根据任务内容完成。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。
```

输出命名：

```text
outputs/<skill>/<task-id>-<variant>-r<repeat>.md
```

示例：

```text
outputs/sales-growth/001-contractual-r1.md
```

可先生成固定 prompt 文件：

```powershell
python experiments/text-generation/scoring/build_prompts.py `
  --root experiments/text-generation
```

生成结果：

```text
prompts/<skill>/<task-id>-<variant>.md
```

每个 prompt 需要运行 2 次，并按输出命名规则保存到 `outputs/`。

## 评分方式

评分由两部分组成：

- 自动检查：运行 `scoring/automatic_checks.py`，检查必需章节、禁止承诺、隐私泄露和交接字段。
- 独立评分或人工评分：本次实验使用 `scoring/score_with_llm_judge.py` 做独立模型评分；后续人工复核可使用 `scoring/human_scores.csv` 模板，按结构完整性、风险控制、证据质量、输出可用性、交接清晰度和维护一致性打分。

自动检查命令：

```powershell
python experiments/text-generation/scoring/automatic_checks.py `
  --outputs experiments/text-generation/outputs `
  --csv experiments/text-generation/scoring/auto_scores.csv
```

## 数据边界

所有任务输入均为合成材料。任务中的客户、金额、电话、邮箱、代码片段和项目背景均为虚构，用于测试输出结构、风险识别和隐私处理，不代表真实客户或真实项目。

## 当前状态

本目录已包含任务集、三组 Skill 变体、No Skill Baseline、评分量表、生成脚本、自动检查脚本、独立评分脚本、纯文本多模型输出和结果汇总。

主实验运行设置：

```text
生成模型：gpt-5.5
评分模型：claude-opus-4-7
生成温度：0.0
评分温度：0.0
输出数量：120
生成成功：120
评分成功：120
```

纯文本多模型与交叉评分补充实验：

```text
生成模型：gpt-5.5、DeepSeek-V4-Pro、qwen3.6-plus、claude-opus-4-7、GLM-5.1、MiniMax-M2.7、Kimi-K2.6、gemini-3.1-pro-preview
评分模型：claude-opus-4-7、gpt-5.5
生成与评分温度：0.0
每个生成模型输出数量：120
总输出数量：960
评分记录：1680
评分成功：1680
交叉评分规则：排除同模型自评；除 gpt-5.5 和 claude-opus-4-7 外，其余生成模型使用两个 judge 的输出级平均分。
```

结果摘要：

```text
scoring/results-summary.zh-CN.md
scoring/model-comparison-text.zh-CN.md
scoring/model-comparison-text-cross-judge.zh-CN.md
```

# 市场验证 Skill 契约化改写实验：Stage 1

本目录保存 Stage 1 pilot study 的完整实验材料、模型输出、评分记录和结果摘要。

## 实验规模

```text
4 Skills x 4 Tasks x 2 Variants x 4 Models x 2 Repeats = 256 outputs
```

## Skill 条件

| 条件 | 说明 |
| --- | --- |
| `original` | 公开仓库中的原始 `SKILL.md`。 |
| `contractual` | 在不新增领域能力的前提下，按 GovernSpec 风格重写后的 Skill。 |

## Stage 1 模型

本次 pilot 使用：

- `gpt-5.5`
- `claude-opus-4-7`
- `DeepSeek-V4-Pro`
- `MiniMax-M2.7`

`MiniMax-M2.7` 在连通性探测中出现 `<think>` 前缀，因此评分脚本会保存原文，同时给 judge 使用清洗后的正文。

## 已完成结果

生成输出：

- 4 个 Skill。
- 4 个任务/Skill。
- 2 个版本：`original` 与 `contractual`。
- 4 个生成模型。
- 2 次重复。
- 共 256 条模型输出。

评分：

- 主分析纳入两个完整 judge：`gpt-5.5` 和 `DeepSeek-V4-Pro`，共 512 条评分记录。
- `claude-opus-4-7` judge 产生 233 条成功评分和 23 条 security-auditor refusal，作为诊断数据保留，不纳入主汇总。

主结果：

| 版本 | Judge rows | Quality mean | Critical error rate | Over-execution rate |
| --- | ---: | ---: | ---: | ---: |
| `contractual` | 256 | 4.783 | 0.031 | 0.004 |
| `original` | 256 | 4.604 | 0.082 | 0.051 |

配对质量增益：

```text
contractual - original = +0.179
```

详见：

- `scoring/stage1_run_manifest.md`
- `scoring/results-summary.zh-CN.md`

## 复现命令

生成 prompt：

```bash
python experiments/market-validated-skills/scoring/build_prompts.py
```

重新运行模型输出需要在本机 shell 设置：

```bash
$env:MODEL_BASE_URL="https://your-openai-compatible-endpoint/v1"
$env:MODEL_API_KEY="your_api_key"
```

然后运行：

```bash
python experiments/market-validated-skills/scoring/run_model_outputs.py --model gpt-5.5 --repeats 2
```

评分：

```bash
python experiments/market-validated-skills/scoring/score_with_llm_judge.py --judge-model gpt-5.5
python experiments/market-validated-skills/scoring/score_with_llm_judge.py --judge-model claude-opus-4-7
python experiments/market-validated-skills/scoring/analyze_results.py
```

不要提交 API key、`.env` 文件或真实客户数据。

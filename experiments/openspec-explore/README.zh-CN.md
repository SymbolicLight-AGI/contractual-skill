# OpenSpec Explore Skill 新旧对照实验

本目录比较桌面文件 `SKILL.md` 中的原始 `openspec-explore` Skill 与契约化改写版本。

## 目录

| 路径 | 内容 |
| --- | --- |
| `skill-variants/original/` | 原始 OpenSpec explore Skill，作为旧版对照。 |
| `skill-variants/contractual/` | GovernSpec 风格的契约化 OpenSpec explore Skill。 |
| `tasks/` | 5 个 explore-mode 任务。 |
| `prompts/` | 由脚本生成的新旧 Skill 对照 prompt。 |
| `scoring/` | 离线契约覆盖评分脚本、CSV 和摘要。 |

## 已完成的离线实验

离线实验不调用模型，只检查两个 Skill 文档是否显式覆盖任务所需的契约信号，包括不实现、读证据、事实/推断区分、人工确认、OpenSpec artifact capture 边界等。

```bash
python experiments/openspec-explore/scoring/build_prompts.py
python experiments/openspec-explore/scoring/score_contract_affordance.py
```

## 真实模型实验

如需比较模型按新旧 Skill 生成的实际回复，可复用全仓的 OpenAI-compatible 调用方式。先设置：

```bash
$env:MODEL_BASE_URL="https://your-compatible-endpoint/v1"
$env:MODEL_API_KEY="your_api_key"
```

然后用已有通用脚本生成输出，例如：

```bash
python experiments/text-generation/scoring/run_model_outputs.py --model your-model --prompt-root experiments/openspec-explore/prompts --outputs-root experiments/openspec-explore/outputs/your-model --runs-jsonl experiments/openspec-explore/scoring/runs_your_model.jsonl --repeats 3
```

注意：不要提交 API key、`.env` 文件或包含真实客户数据的输出。

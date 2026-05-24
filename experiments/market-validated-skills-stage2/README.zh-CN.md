# Stage 2 市场验证 Skill 契约化 A/B 实验

本目录保存论文扩展实验的 Stage 2 数据包。实验问题是：把公开社区中已经成型的 `SKILL.md` 改写为 GovernSpec 契约化结构后，是否能提升输出质量、治理性和高风险场景下的可靠性。

## 冻结规模

- 8 个公开 Skill，覆盖规划、工程、安全、企业流程四类，每类 2 个。
- 6 类任务/Skill：正常、信息不足、高风险、工具失败、越权诱导、交接。
- 2 个版本：`original` 与 `contractual`。
- 6 个生成模型，2 次重复。
- 目标输出数：`8 x 6 x 2 x 6 x 2 = 1152`。
- 评分：`gpt-5.5` 与 `gemini-3.1-pro-preview` 两个 judge 文件均已完成，每个 judge 去重后 1152 条有效评分。

## 目录

| 路径 | 用途 |
| --- | --- |
| `sources/selected_skills.csv` | Skill 来源、commit、许可证说明和字符数。 |
| `skill-variants/original/` | 原始公开 Skill。 |
| `skill-variants/contractual/` | 契约化改写版本。 |
| `skill-variants/rewrite-logs/` | 改写映射和控制变量说明。 |
| `tasks/` | 合成任务与任务索引。 |
| `prompts/` | 固定实验 prompt，由脚本生成。 |
| `outputs/` | 模型输出。 |
| `scoring/` | 生成、评分、汇总脚本和评分数据。 |

## 复现命令

```bash
python experiments/market-validated-skills-stage2/setup_stage2.py
python experiments/market-validated-skills-stage2/scoring/build_prompts.py --root experiments/market-validated-skills-stage2
```

模型生成和 judge 评分需要配置兼容 OpenAI Chat Completions 的服务地址与 API key。不要提交 `.env` 或 API key。

复算已保存评分的最终汇总不需要 API key：

```bash
python experiments/market-validated-skills-stage2/scoring/analyze_results.py --root experiments/market-validated-skills-stage2
```

主结果见 `scoring/results-summary.zh-CN.md`。原始 judge 文件保留了早期额度不足导致的失败重试记录；分析脚本会按 `run_id` 去重，并优先采用成功评分行。

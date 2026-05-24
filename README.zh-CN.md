# 契约化 Skill 论文复现包

这是论文《Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents》的复现材料包。论文正文已经单独发布，因此本仓库不再包含 `paper/` 和 `paper/figures/`。

## 包含内容

| 路径 | 用途 |
| --- | --- |
| `experiments/text-generation/` | 纯文本实验的合成任务、prompt、Skill 变体、模型输出、评分脚本和评分记录。 |
| `experiments/tool-calling/` | 离线模拟工具调用 challenge 的任务、transcripts、评分脚本和评分记录。 |
| `experiments/openspec-explore/` | OpenSpec explore Skill 的旧版与契约化版本小样本对照。 |
| `experiments/market-validated-skills/` | 市场验证 Skill 的 Stage 1 A/B pilot，对比原始 Skill 与契约化改写版本。 |
| `experiments/market-validated-skills-stage2/` | 市场验证 Skill 的 Stage 2 扩展实验材料、生成输出、完整 judge 评分记录和最终汇总。 |
| `templates/` | 可复用的中英文契约化 Skill 模板，用于把论文中的结构迁移到新领域。 |
| `docs/` | 复现说明、数据说明和文件地图。 |

扩展实验设计：

- `docs/market_validated_skill_ab_experiment_design.zh-CN.md`：市场验证 Skill 的契约化改写 A/B 实验设计。

## 当前实验规模

- 纯文本实验：8 个生成模型、3 类 Skill、15 个合成任务、4 种指令条件、2 次重复，共 960 个模型输出和 1680 条交叉评分记录。
- 工具调用实验：8 个生成模型，共 192 条离线模拟工具调用 challenge 记录。
- OpenSpec explore Skill 对照：2 个 Skill 版本、5 个探索模式任务、10 个生成 prompt，以及确定性契约覆盖评分。
- 市场验证 Skill Stage 1 pilot：4 个公开 Skill、16 个合成任务、2 个版本、4 个生成模型、2 次重复，共 256 条模型输出、512 条完整主评分记录，以及 233 条 Claude judge 诊断评分记录。
- 市场验证 Skill Stage 2 扩展实验：8 个公开 Skill、48 个合成任务、2 个版本、6 个生成模型、2 次重复，共 1152 条模型输出，以及两个完整 judge 文件中的 2304 条去重后有效评分记录。主结果：契约化 Skill 将平均质量从 4.692 提升到 4.914，并将 critical-error rate 从 0.083 降到 0.013。
- 不包含真实客户数据、真实合同、真实凭据或真实生产系统调用。

## 模板

可复用的契约化 Skill 模板：

- 英文版：`templates/contractual-skill.SKILL.md`
- 中文版：`templates/contractual-skill.zh-CN.SKILL.md`

## 复现说明

复算已有结果不需要 API key，只依赖已保存的输出和评分文件。

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
.venv/Scripts/python experiments/text-generation/scoring/analyze_text_cross_judge.py --scoring-root experiments/text-generation/scoring --markdown experiments/text-generation/scoring/model-comparison-text-cross-judge.zh-CN.md
.venv/Scripts/python experiments/tool-calling/scoring/analyze_tool_model_comparison.py --scoring-root experiments/tool-calling/scoring --markdown experiments/tool-calling/scoring/model-comparison-challenge.zh-CN.md
.venv/Scripts/python experiments/openspec-explore/scoring/build_prompts.py
.venv/Scripts/python experiments/openspec-explore/scoring/score_contract_affordance.py
.venv/Scripts/python experiments/market-validated-skills/scoring/analyze_results.py
.venv/Scripts/python experiments/market-validated-skills-stage2/scoring/analyze_results.py
```

如需重新跑模型生成或模型评分，需要另外配置兼容 OpenAI Chat Completions 的模型 API。请在本机 shell 中设置 `MODEL_BASE_URL` 和 `MODEL_API_KEY`，或通过 `--base-url` 显式传入服务地址；不要提交 API key 或 `.env` 文件。由于模型版本可能变化，重新运行结果不保证与本文完全一致。

## 引用

引用本复现包时，请使用 `CITATION.cff` 中的元数据；如本仓库后续通过 Zenodo 或同类服务归档，请引用对应的归档 DOI 和 release tag。

## 说明

本复现包只保留实验材料、模型输出、评分记录和分析脚本，不包含论文正文和图表目录。

## 许可证

本仓库使用 MIT License，详见 `LICENSE`。

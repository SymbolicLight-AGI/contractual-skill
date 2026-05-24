# Stage 1 Run Manifest

## Run Date

2026-05-23, Asia/Shanghai.

## Scope

- Skills: 4
- Tasks per Skill: 4
- Variants: `original`, `contractual`
- Generation models: 4
- Repeats: 2
- Saved model outputs: 256

## Generation Models

| Model | Output directory | Outputs | Notes |
| --- | --- | ---: | --- |
| `gpt-5.5` | `outputs/gpt_55/` | 64 | Completed after retrying two empty-response records. |
| `claude-opus-4-7` | `outputs/claude_opus_4_7/` | 64 | Completed after retrying long deal-playbook records. |
| `DeepSeek-V4-Pro` | `outputs/deepseek_v4_pro/` | 64 | Completed after increasing timeout for long original deal-playbook records. |
| `MiniMax-M2.7` | `outputs/minimax_m27/` | 64 | Completed after retrying timeout records; outputs may include `<think>` prefixes. |

## Judge Models

| Judge model | Score file | Successful rows | Error rows | Included in main summary |
| --- | --- | ---: | ---: | --- |
| `gpt-5.5` | `llm_judge_scores_gpt_55.csv` | 256 | 0 | Yes |
| `DeepSeek-V4-Pro` | `llm_judge_scores_deepseek_v4_pro.csv` | 256 | 0 | Yes |
| `claude-opus-4-7` | `llm_judge_scores_claude_opus_4_7.csv` | 233 | 23 | No; retained as diagnostic data because security-auditor cases triggered refusal. |

## Main Results

Main aggregation includes only complete judge files.

| Variant | Judge rows | Quality mean | Critical error rate | Over-execution rate |
| --- | ---: | ---: | ---: | ---: |
| `contractual` | 256 | 4.783 | 0.031 | 0.004 |
| `original` | 256 | 4.604 | 0.082 | 0.051 |

Mean paired quality delta, contractual minus original: `0.179`.

## Data Handling

- API keys were supplied only through shell environment variables during runtime.
- No API key, `.env`, real customer data, real contract, or production-system trace is included.
- Raw outputs are preserved under `outputs/`.
- MiniMax `<think>` prefixes are preserved in raw outputs and marked by `think_prefix_removed` during scoring.
- Re-run logs are preserved under `scoring/runs_*.jsonl`, including retry history for temporary timeout or empty-response records.

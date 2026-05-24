# Stage 2 Partial GPT-5.5 Judge Summary

## Status

This historical diagnostic summary has been superseded by `results-summary.zh-CN.md`.

The final Stage 2 package now includes two complete judge files:

- `gpt-5.5`: 1152/1152 successful rows after deduplication.
- `gemini-3.1-pro-preview`: 1152/1152 successful rows after deduplication.

The figures below are retained only to document the earlier partial run; use the completed summary for all Stage 2 claims.

- Complete generation outputs: 1152/1152.
- GPT-5.5 judge rows written: 1152.
- GPT-5.5 successful score rows: 1112.
- GPT-5.5 unresolved score rows: 40.
- Unresolved score causes:
  - `empty_judge_response`: 1.
  - `insufficient_balance`: 39.
- Gemini judge is currently diagnostic only: 20 successful sample rows.

## Provisional Pattern From Successful GPT-5.5 Rows

These figures exclude unresolved judge rows and must not be reported as final Stage 2 evidence.

| Variant | Successful rows | Quality mean | Critical error rate | Over-execution rate |
| --- | ---: | ---: | ---: | ---: |
| original | 555 | 4.494 | 0.146 | 0.038 |
| contractual | 557 | 4.859 | 0.023 | 0.007 |

Available paired comparisons:

- Complete paired deltas: 555.
- Mean contractual minus original quality delta: `+0.365`.
- Positive paired deltas: `392/555`.

## Model-Level Provisional Quality

| Generation model | Original | Contractual |
| --- | ---: | ---: |
| `claude_opus_4_7` | 4.746 | 4.960 |
| `deepseek_v4_pro` | 4.383 | 4.779 |
| `gemini_31_pro_preview` | 4.275 | 4.852 |
| `gpt_55` | 4.809 | 4.939 |
| `minimax_m27` | 4.391 | 4.764 |
| `qwen36_plus` | 4.321 | 4.859 |

## Final Result Location

Use `results-summary.zh-CN.md`, `combined_judge_scores.csv`, `paired_quality_deltas.csv`, and `judge_inclusion_diagnostics.csv` for the completed Stage 2 analysis.

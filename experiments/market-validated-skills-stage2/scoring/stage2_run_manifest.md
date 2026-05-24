# Stage 2 Run Manifest

## Scope

- Experiment: market-validated Skill contractualization A/B, Stage 2 full study.
- Date run: 2026-05-24.
- Skills: 8.
- Skill categories: planning, engineering, security, enterprise.
- Tasks per Skill: 6.
- Task types: normal, missing_info, high_risk, tool_failure, overreach, handoff.
- Variants: original and contractual.
- Generation models: `gpt-5.5`, `claude-opus-4-7`, `gemini-3.1-pro-preview`, `DeepSeek-V4-Pro`, `qwen3.6-plus`, `MiniMax-M2.7`.
- Repeats: 2.

## Generation Status

- Prompt files: 96.
- Expected generation outputs: 1152.
- Saved generation outputs: 1152.
- `EXPERIMENT_ERROR` outputs: 0.
- One `gpt-5.5` generation cell returned an empty provider response after two non-streaming attempts and one streaming probe:
  - `outputs/gpt_55/security-auditor/005-contractual-r2.md`
  - The cell is retained as `PROVIDER_EMPTY_RESPONSE` for auditability.

## Judge Status

Main judge scoring is complete. The raw judge files retain earlier failed rows from quota exhaustion and empty-response retries for auditability; analysis deduplicates by `run_id` and prefers successful rows.

| Judge model | Intended rows | Successful rows | Unresolved rows | Status |
| --- | ---: | ---: | ---: | --- |
| `gpt-5.5` | 1152 | 1152 | 0 | complete |
| `gemini-3.1-pro-preview` | 1152 | 1152 | 0 | complete |

Raw judge row counts:

- `llm_judge_scores_gpt_55.csv`: 1192 raw rows, 1152 successful rows after deduplication.
- `llm_judge_scores_gemini_31_pro_preview.csv`: 1422 raw rows, 1152 successful rows after deduplication.

## Script Updates For Resumability

- `score_with_llm_judge.py` now skips only successful existing rows, so failed judge rows can be retried without recomputing all successful rows.
- `analyze_results.py` now deduplicates judge rows by `run_id`, preferring successful rows over earlier error rows.

## Recompute Commands

Recompute the final summary from saved judge files:

```bash
python experiments/market-validated-skills-stage2/scoring/analyze_results.py --root experiments/market-validated-skills-stage2
```

Set `MODEL_BASE_URL` and `MODEL_API_KEY` only in the local shell if rerunning model generation or judge scoring. Do not commit credentials.

## Final Stage 2 Signal

- Original quality mean: 4.692.
- Contractual quality mean: 4.914.
- Mean contractual minus original quality delta: +0.221.
- Original critical error rate: 0.083.
- Contractual critical error rate: 0.013.
- Original over-execution rate: 0.022.
- Contractual over-execution rate: 0.003.

See `results-summary.zh-CN.md` for model-level and Skill-level breakdowns.

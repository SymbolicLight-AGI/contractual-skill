# Reproducibility Notes

## Environment

The saved analysis files can be inspected without external services. Recomputing summaries from saved CSV/JSONL files uses Python standard-library scripts.

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
```

## Recompute Text-Generation Summary

```bash
.venv/Scripts/python experiments/text-generation/scoring/analyze_text_cross_judge.py \
  --scoring-root experiments/text-generation/scoring \
  --markdown experiments/text-generation/scoring/model-comparison-text-cross-judge.zh-CN.md
```

The text experiment should contain 960 output-level units and 1680 judge records across the included CSV files.

## Recompute Tool-Calling Summary

```bash
.venv/Scripts/python experiments/tool-calling/scoring/analyze_tool_model_comparison.py \
  --scoring-root experiments/tool-calling/scoring \
  --markdown experiments/tool-calling/scoring/model-comparison-challenge.zh-CN.md
```

The tool-calling challenge should contain 192 saved challenge records.

## Recompute OpenSpec Explore Skill Comparison

```bash
.venv/Scripts/python experiments/openspec-explore/scoring/build_prompts.py
.venv/Scripts/python experiments/openspec-explore/scoring/score_contract_affordance.py
```

This comparison should contain 10 generated prompts and 10 contract-affordance score rows across two Skill variants and five tasks. It does not require an API key.

## Recompute Market-Validated Skill Stage 1 Summary

```bash
.venv/Scripts/python experiments/market-validated-skills/scoring/analyze_results.py
```

The Stage 1 package should contain 256 saved model outputs and 512 main judge score rows across the two complete judge files. The partial Claude judge file is retained as diagnostic data because high-risk security-auditor cases triggered refusal.

## Recompute Market-Validated Skill Stage 2 Summary

```bash
.venv/Scripts/python experiments/market-validated-skills-stage2/scoring/analyze_results.py
```

The Stage 2 package contains 1152 saved model outputs and two complete judge files. Each judge file has 1152 successful rows after deduplication by `run_id`, for 2304 successful deduplicated judge rows in the main summary. Raw judge files retain earlier failed retry rows for auditability; `analyze_results.py` excludes those rows when building the summary.

## Rerunning Model Calls

The package includes saved outputs and scoring records. It intentionally does not include API keys. Rerunning generation or scoring requires a compatible model API and may not reproduce the exact saved outputs because model versions and provider behavior can change.

When rerunning model calls, set `MODEL_BASE_URL` to an OpenAI-compatible API endpoint and `MODEL_API_KEY` to a provider key in your local shell, or pass `--base-url` explicitly. Do not commit those values or `.env` files.

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

## Rerunning Model Calls

The package includes saved outputs and scoring records. It intentionally does not include API keys. Rerunning generation or scoring requires a compatible model API and may not reproduce the exact saved outputs because model versions and provider behavior can change.

When rerunning model calls, set `MODEL_BASE_URL` to an OpenAI-compatible API endpoint and `MODEL_API_KEY` to a provider key in your local shell, or pass `--base-url` explicitly. Do not commit those values or `.env` files.

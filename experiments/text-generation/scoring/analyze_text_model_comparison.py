from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path
from typing import Iterable


DIMENSIONS = [
    "structure",
    "risk_control",
    "evidence_quality",
    "output_usability",
    "handoff_clarity",
    "maintenance_consistency",
]

VARIANTS = ["no-skill", "minimal", "plain-expanded", "contractual"]


def mean(values: Iterable[float]) -> float:
    items = list(values)
    return sum(items) / len(items) if items else 0.0


def sample_sd(values: Iterable[float]) -> float:
    items = list(values)
    if len(items) < 2:
        return 0.0
    avg = mean(items)
    return math.sqrt(sum((item - avg) ** 2 for item in items) / (len(items) - 1))


def load_rows(path: Path, model: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            parsed: dict[str, object] = dict(row)
            parsed["generation_model"] = model
            scores = [float(row[dimension]) for dimension in DIMENSIONS]
            for dimension, score in zip(DIMENSIONS, scores):
                parsed[dimension] = score
            parsed["overall"] = mean(scores)
            parsed["critical_error"] = str(row.get("critical_error", "")).lower() == "true"
            rows.append(parsed)
    return rows


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    models = list(dict.fromkeys(str(row["generation_model"]) for row in rows))
    for model in models:
        model_rows = [row for row in rows if row["generation_model"] == model]
        for variant in VARIANTS:
            group = [row for row in model_rows if row["variant"] == variant]
            result.append(
                {
                    "model": model,
                    "variant": variant,
                    "n": len(group),
                    "overall": mean(float(row["overall"]) for row in group),
                    "sd": sample_sd(float(row["overall"]) for row in group),
                    "critical": sum(bool(row["critical_error"]) for row in group),
                    "structure": mean(float(row["structure"]) for row in group),
                    "evidence": mean(float(row["evidence_quality"]) for row in group),
                    "handoff": mean(float(row["handoff_clarity"]) for row in group),
                    "maintenance": mean(float(row["maintenance_consistency"]) for row in group),
                }
            )
    return result


def matched_deltas(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    comparisons = [
        ("contractual", "no-skill"),
        ("contractual", "minimal"),
        ("contractual", "plain-expanded"),
        ("plain-expanded", "minimal"),
    ]
    models = list(dict.fromkeys(str(row["generation_model"]) for row in rows))
    for model in models:
        model_rows = [row for row in rows if row["generation_model"] == model]
        grouped: dict[tuple[object, object, object], dict[object, float]] = defaultdict(dict)
        for row in model_rows:
            grouped[(row["skill"], row["task_id"], row["repeat"])][row["variant"]] = float(row["overall"])
        for left, right in comparisons:
            deltas = [values[left] - values[right] for values in grouped.values() if left in values and right in values]
            output.append(
                {
                    "model": model,
                    "comparison": f"{left} - {right}",
                    "n": len(deltas),
                    "mean_delta": mean(deltas),
                    "sd": sample_sd(deltas),
                    "positive": sum(delta > 0 for delta in deltas),
                    "tied": sum(delta == 0 for delta in deltas),
                    "negative": sum(delta < 0 for delta in deltas),
                }
            )
    return output


def render_markdown(rows: list[dict[str, object]]) -> str:
    lines = [
        "# 纯文本输出多模型对比",
        "",
        "## 独立评分汇总",
        "",
        "| 生成模型 | 变体 | n | 总分均值 | 标准差 | 关键错误 | 结构 | 证据 | 交接 | 维护 |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in summarize(rows):
        lines.append(
            "| {model} | {variant} | {n} | {overall:.3f} | {sd:.3f} | {critical} | "
            "{structure:.3f} | {evidence:.3f} | {handoff:.3f} | {maintenance:.3f} |".format(**row)
        )

    lines.extend(
        [
            "",
            "## 配对差异",
            "",
            "| 生成模型 | 对比 | n | 平均差 | 标准差 | 左侧更高 | 持平 | 右侧更高 |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in matched_deltas(rows):
        lines.append(
            "| {model} | {comparison} | {n} | {mean_delta:.3f} | {sd:.3f} | "
            "{positive} | {tied} | {negative} |".format(**row)
        )

    lines.extend(
        [
            "",
            "## 解释边界",
            "",
            "- 本表使用 `claude-opus-4-7` 作为独立评分模型。",
            "- 分数反映离线合成任务上的独立模型评分，不是多人类评审。",
            "- 高分不等于可上线，仍需结合工具调用实验和人工复核。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare text-output experiment scores across generation models.")
    parser.add_argument("--scoring-root", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()

    sources = [
        ("gpt-5.5", args.scoring_root / "llm_judge_scores.csv"),
        ("DeepSeek-V4-Pro", args.scoring_root / "llm_judge_scores_deepseek_v4_pro.csv"),
        ("qwen3.6-plus", args.scoring_root / "llm_judge_scores_qwen36_plus.csv"),
        ("GLM-5.1", args.scoring_root / "llm_judge_scores_glm_51.csv"),
        ("MiniMax-M2.7", args.scoring_root / "llm_judge_scores_minimax_m27.csv"),
        ("Kimi-K2.6", args.scoring_root / "llm_judge_scores_kimi_k26.csv"),
        ("gemini-3.1-pro-preview", args.scoring_root / "llm_judge_scores_gemini_31_pro_preview.csv"),
    ]
    rows: list[dict[str, object]] = []
    for model, path in sources:
        rows.extend(load_rows(path, model))

    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text(render_markdown(rows), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

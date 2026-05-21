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

SOURCES = [
    ("gpt-5.5", "claude-opus-4-7", "llm_judge_scores.csv"),
    ("DeepSeek-V4-Pro", "claude-opus-4-7", "llm_judge_scores_deepseek_v4_pro.csv"),
    ("qwen3.6-plus", "claude-opus-4-7", "llm_judge_scores_qwen36_plus.csv"),
    ("GLM-5.1", "claude-opus-4-7", "llm_judge_scores_glm_51.csv"),
    ("MiniMax-M2.7", "claude-opus-4-7", "llm_judge_scores_minimax_m27.csv"),
    ("Kimi-K2.6", "claude-opus-4-7", "llm_judge_scores_kimi_k26.csv"),
    ("gemini-3.1-pro-preview", "claude-opus-4-7", "llm_judge_scores_gemini_31_pro_preview.csv"),
    ("DeepSeek-V4-Pro", "gpt-5.5", "llm_judge_scores_deepseek_v4_pro_gpt55_judge.csv"),
    ("qwen3.6-plus", "gpt-5.5", "llm_judge_scores_qwen36_plus_gpt55_judge.csv"),
    ("claude-opus-4-7", "gpt-5.5", "llm_judge_scores_claude_opus_47_gpt55_judge.csv"),
    ("GLM-5.1", "gpt-5.5", "llm_judge_scores_glm_51_gpt55_judge.csv"),
    ("MiniMax-M2.7", "gpt-5.5", "llm_judge_scores_minimax_m27_gpt55_judge.csv"),
    ("Kimi-K2.6", "gpt-5.5", "llm_judge_scores_kimi_k26_gpt55_judge.csv"),
    ("gemini-3.1-pro-preview", "gpt-5.5", "llm_judge_scores_gemini_31_pro_preview_gpt55_judge.csv"),
]


def mean(values: Iterable[float]) -> float:
    items = list(values)
    return sum(items) / len(items) if items else 0.0


def sample_sd(values: Iterable[float]) -> float:
    items = list(values)
    if len(items) < 2:
        return 0.0
    avg = mean(items)
    return math.sqrt(sum((item - avg) ** 2 for item in items) / (len(items) - 1))


def load_rows(scoring_root: Path) -> tuple[list[dict[str, object]], list[str]]:
    rows: list[dict[str, object]] = []
    missing: list[str] = []
    for generation_model, judge_model, filename in SOURCES:
        path = scoring_root / filename
        if not path.exists():
            missing.append(filename)
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                if row.get("notes", "").startswith("SCORING_ERROR"):
                    continue
                try:
                    scores = [float(row[dimension]) for dimension in DIMENSIONS]
                except (TypeError, ValueError):
                    continue
                parsed: dict[str, object] = dict(row)
                parsed["generation_model"] = generation_model
                parsed["judge_model"] = judge_model
                for dimension, score in zip(DIMENSIONS, scores):
                    parsed[dimension] = score
                parsed["overall"] = mean(scores)
                parsed["critical_error"] = str(row.get("critical_error", "")).lower() == "true"
                rows.append(parsed)
    return rows, missing


def averaged_output_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[object, object, object, object, object], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        key = (
            row["generation_model"],
            row["skill"],
            row["task_id"],
            row["repeat"],
            row["variant"],
        )
        grouped[key].append(row)

    averaged: list[dict[str, object]] = []
    for (generation_model, skill, task_id, repeat, variant), items in grouped.items():
        output_row: dict[str, object] = {
            "generation_model": generation_model,
            "skill": skill,
            "task_id": task_id,
            "repeat": repeat,
            "variant": variant,
            "judge_count": len(items),
            "critical_error": any(bool(item["critical_error"]) for item in items),
        }
        for dimension in DIMENSIONS:
            output_row[dimension] = mean(float(item[dimension]) for item in items)
        output_row["overall"] = mean(float(output_row[dimension]) for dimension in DIMENSIONS)
        averaged.append(output_row)
    return averaged


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
                    "n_outputs": len(group),
                    "avg_judges": mean(float(row["judge_count"]) for row in group),
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


def coverage(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    counts: dict[tuple[object, object], int] = defaultdict(int)
    for row in rows:
        counts[(row["generation_model"], row["judge_model"])] += 1
    return [
        {"generation_model": generation_model, "judge_model": judge_model, "n_scores": n_scores}
        for (generation_model, judge_model), n_scores in counts.items()
    ]


def render_markdown(rows: list[dict[str, object]], missing: list[str]) -> str:
    averaged = averaged_output_rows(rows)
    lines = [
        "# 纯文本输出交叉评分对比",
        "",
        "## 评分覆盖",
        "",
        "| 生成模型 | 评分模型 | 评分条数 |",
        "| --- | --- | ---: |",
    ]
    for row in coverage(rows):
        lines.append("| {generation_model} | {judge_model} | {n_scores} |".format(**row))

    if missing:
        lines.extend(["", "缺失评分文件：", ""])
        lines.extend(f"- `{filename}`" for filename in missing)

    lines.extend(
        [
            "",
            "## 输出级平均评分",
            "",
            "| 生成模型 | 变体 | 输出数 | 平均 judge 数 | 总分均值 | 标准差 | 关键错误 | 结构 | 证据 | 交接 | 维护 |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in summarize(averaged):
        lines.append(
            "| {model} | {variant} | {n_outputs} | {avg_judges:.1f} | {overall:.3f} | {sd:.3f} | {critical} | "
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
    for row in matched_deltas(averaged):
        lines.append(
            "| {model} | {comparison} | {n} | {mean_delta:.3f} | {sd:.3f} | "
            "{positive} | {tied} | {negative} |".format(**row)
        )

    lines.extend(
        [
            "",
            "## 解释边界",
            "",
            "- 本表排除同模型自评。",
            "- 除 `gpt-5.5` 和 `claude-opus-4-7` 外，其余生成模型输出使用两个非生成模型 judge 的输出级平均分。",
            "- `gpt-5.5` 输出由 `claude-opus-4-7` 评分，`claude-opus-4-7` 输出由 `gpt-5.5` 评分。",
            "- 分数反映离线合成任务上的模型辅助评分，不是多人类评审。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare text-output experiment scores with cross judges.")
    parser.add_argument("--scoring-root", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()

    rows, missing = load_rows(args.scoring_root)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text(render_markdown(rows, missing), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

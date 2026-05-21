from __future__ import annotations

import argparse
import csv
import json
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

VARIANT_ORDER = ["no-skill", "minimal", "plain-expanded", "contractual"]


def mean(values: Iterable[float]) -> float:
    items = list(values)
    if not items:
        return 0.0
    return sum(items) / len(items)


def sample_sd(values: Iterable[float]) -> float:
    items = list(values)
    if len(items) < 2:
        return 0.0
    avg = mean(items)
    return math.sqrt(sum((value - avg) ** 2 for value in items) / (len(items) - 1))


def pct(count: int, total: int) -> str:
    if total == 0:
        return "0.0%"
    return f"{count / total * 100:.1f}%"


def load_judge_rows(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            parsed: dict[str, object] = dict(row)
            scores = [float(row[dimension]) for dimension in DIMENSIONS]
            for dimension, score in zip(DIMENSIONS, scores):
                parsed[dimension] = score
            parsed["overall"] = mean(scores)
            parsed["critical_error"] = str(row.get("critical_error", "")).lower() == "true"
            rows.append(parsed)
    return rows


def load_auto_rows(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    bool_fields = [
        "required_sections_ok",
        "forbidden_commitment",
        "privacy_leak",
        "secret_leak",
        "has_handoff",
        "has_uncertainty_or_evidence",
    ]
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            parsed: dict[str, object] = dict(row)
            for field in bool_fields:
                parsed[field] = str(row.get(field, "")).lower() == "true"
            parsed["word_count"] = int(row.get("word_count") or 0)
            rows.append(parsed)
    return rows


def load_run_counts(path: Path) -> tuple[dict[str, int], dict[str, int]]:
    statuses: dict[str, int] = defaultdict(int)
    models: dict[str, int] = defaultdict(int)
    if not path.exists():
        return dict(statuses), dict(models)
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            statuses[str(record.get("status", ""))] += 1
            models[str(record.get("model", ""))] += 1
    return dict(statuses), dict(models)


def judge_by_variant(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    summary: list[dict[str, object]] = []
    for variant in VARIANT_ORDER:
        group = [row for row in rows if row["variant"] == variant]
        overall = [float(row["overall"]) for row in group]
        summary.append(
            {
                "variant": variant,
                "n": len(group),
                "overall_mean": mean(overall),
                "overall_sd": sample_sd(overall),
                "critical_errors": sum(bool(row["critical_error"]) for row in group),
                **{dimension: mean(float(row[dimension]) for row in group) for dimension in DIMENSIONS},
            }
        )
    return summary


def auto_by_variant(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    summary: list[dict[str, object]] = []
    for variant in VARIANT_ORDER:
        group = [row for row in rows if row["variant"] == variant]
        total = len(group)
        summary.append(
            {
                "variant": variant,
                "n": total,
                "sections_ok": sum(bool(row["required_sections_ok"]) for row in group),
                "forbidden_terms": sum(bool(row["forbidden_commitment"]) for row in group),
                "privacy_leaks": sum(bool(row["privacy_leak"]) for row in group),
                "secret_leaks": sum(bool(row["secret_leak"]) for row in group),
                "handoff_present": sum(bool(row["has_handoff"]) for row in group),
                "uncertainty_present": sum(bool(row["has_uncertainty_or_evidence"]) for row in group),
                "avg_words": mean(int(row["word_count"]) for row in group),
            }
        )
    return summary


def matched_deltas(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[object, object, object], dict[object, float]] = defaultdict(dict)
    for row in rows:
        grouped[(row["skill"], row["task_id"], row["repeat"])][row["variant"]] = float(row["overall"])

    comparisons = [
        ("minimal", "no-skill"),
        ("plain-expanded", "no-skill"),
        ("contractual", "no-skill"),
        ("contractual", "minimal"),
        ("contractual", "plain-expanded"),
        ("plain-expanded", "minimal"),
    ]
    results: list[dict[str, object]] = []
    for left, right in comparisons:
        deltas = [values[left] - values[right] for values in grouped.values() if left in values and right in values]
        results.append(
            {
                "comparison": f"{left} - {right}",
                "n": len(deltas),
                "mean_delta": mean(deltas),
                "sd": sample_sd(deltas),
                "positive": sum(delta > 0 for delta in deltas),
                "tied": sum(delta == 0 for delta in deltas),
                "negative": sum(delta < 0 for delta in deltas),
            }
        )
    return results


def judge_by_skill(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    summary: list[dict[str, object]] = []
    skills = sorted({str(row["skill"]) for row in rows})
    for skill in skills:
        row: dict[str, object] = {"skill": skill}
        for variant in VARIANT_ORDER:
            key = variant.replace("-", "_")
            group = [item for item in rows if item["skill"] == skill and item["variant"] == variant]
            row[f"{key}_overall"] = mean(float(item["overall"]) for item in group)
            row[f"{key}_handoff"] = mean(float(item["handoff_clarity"]) for item in group)
        summary.append(row)
    return summary


def render_markdown(root: Path) -> str:
    judge_rows = load_judge_rows(root / "scoring" / "llm_judge_scores.csv")
    auto_rows = load_auto_rows(root / "scoring" / "auto_scores.csv")
    statuses, models = load_run_counts(root / "scoring" / "runs.jsonl")

    lines = [
        "# 契约化 Skill 实验结果摘要",
        "",
        "## 运行概况",
        "",
        f"- 输出数量：{len(judge_rows)}",
        f"- 生成运行状态：{statuses}",
        f"- 生成模型记录：{models}",
        "- 生成模型：gpt-5.5",
        "- 评分模型：claude-opus-4-7",
        "- 生成与评分温度：0.0",
        "- 评分方式：独立模型盲评，不向评分 prompt 暴露 Skill 变体标签。",
        "",
        "## 独立模型评分",
        "",
        "| 变体 | n | 总分均值 | 总分标准差 | 关键错误 | 结构 | 风险 | 证据 | 可用性 | 交接 | 维护 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in judge_by_variant(judge_rows):
        lines.append(
            "| {variant} | {n} | {overall_mean:.3f} | {overall_sd:.3f} | {critical_errors} | "
            "{structure:.3f} | {risk_control:.3f} | {evidence_quality:.3f} | "
            "{output_usability:.3f} | {handoff_clarity:.3f} | {maintenance_consistency:.3f} |".format(**row)
        )

    lines.extend(
        [
            "",
            "## 配对差异",
            "",
            "| 对比 | n | 平均差 | 标准差 | 左侧更高 | 持平 | 右侧更高 |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in matched_deltas(judge_rows):
        lines.append(
            "| {comparison} | {n} | {mean_delta:.3f} | {sd:.3f} | {positive} | {tied} | {negative} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## 按 Skill 拆分",
            "",
            "| Skill | no-skill 总分 | minimal 总分 | plain-expanded 总分 | contractual 总分 | no-skill 交接 | contractual 交接 |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in judge_by_skill(judge_rows):
        lines.append(
            "| {skill} | {no_skill_overall:.3f} | {minimal_overall:.3f} | "
            "{plain_expanded_overall:.3f} | {contractual_overall:.3f} | "
            "{no_skill_handoff:.3f} | {contractual_handoff:.3f} |".format(**row)
        )

    lines.extend(
        [
            "",
            "## 自动检查",
            "",
            "| 变体 | n | 必需章节通过 | 风险词命中 | 隐私泄露 | 密钥泄露 | 交接表达 | 不确定性表达 | 平均词数 |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in auto_by_variant(auto_rows):
        n = int(row["n"])
        lines.append(
            "| {variant} | {n} | {sections_ok}/{n} ({sections_pct}) | {forbidden_terms} | "
            "{privacy_leaks} | {secret_leaks} | {handoff_present}/{n} ({handoff_pct}) | "
            "{uncertainty_present}/{n} ({uncertainty_pct}) | {avg_words:.1f} |".format(
                **row,
                sections_pct=pct(int(row["sections_ok"]), n),
                handoff_pct=pct(int(row["handoff_present"]), n),
                uncertainty_pct=pct(int(row["uncertainty_present"]), n),
            )
        )

    lines.extend(
        [
            "",
            "## 解释边界",
            "",
            "- 自动检查中的风险词命中表示文本出现了高风险承诺相关短语，不等同于模型已经做出违规承诺。实际输出中有不少命中来自否定句、引用任务输入或风险提示。",
            "- 独立模型评分未发现关键错误，但该评分仍不是多人类评审，不能替代后续人工复核。",
            "- 本实验样本量较小，且只使用一个生成模型，结论应理解为最小可行实验结果。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze contractual Skill experiment scores.")
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--markdown", type=Path)
    args = parser.parse_args()

    markdown = render_markdown(args.root)
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(markdown, encoding="utf-8")
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


VARIANTS = ["no-skill", "minimal", "plain-expanded", "contractual"]


def as_bool(value: str) -> bool:
    return value.lower() == "true"


def pct(count: int, total: int) -> str:
    if total == 0:
        return "0.0%"
    return f"{count / total * 100:.1f}%"


def load_rows(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            parsed: dict[str, object] = dict(row)
            for key in [
                "required_called",
                "mentions_blocked_or_human_gate",
                "false_completion_after_block",
                "final_present",
            ]:
                parsed[key] = as_bool(str(row[key]))
            for key in ["forbidden_attempt_count", "blocked_attempt_count", "parse_errors"]:
                parsed[key] = int(row[key])
            rows.append(parsed)
    return rows


def render_markdown(rows: list[dict[str, object]]) -> str:
    lines = [
        "# 工具调用实验结果摘要",
        "",
        "## 按变体汇总",
        "",
        "| 变体 | n | 必要工具全调用 | 禁止工具尝试 | 被阻断工具尝试 | 提到阻断/人工确认 | 阻断后误称完成 | JSON 解析错误 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for variant in VARIANTS:
        group = [row for row in rows if row["variant"] == variant]
        total = len(group)
        required = sum(bool(row["required_called"]) for row in group)
        forbidden = sum(int(row["forbidden_attempt_count"]) for row in group)
        blocked = sum(int(row["blocked_attempt_count"]) for row in group)
        human = sum(bool(row["mentions_blocked_or_human_gate"]) for row in group)
        false_done = sum(bool(row["false_completion_after_block"]) for row in group)
        parse_errors = sum(int(row["parse_errors"]) for row in group)
        lines.append(
            f"| {variant} | {total} | {required}/{total} ({pct(required, total)}) | "
            f"{forbidden} | {blocked} | {human}/{total} ({pct(human, total)}) | "
            f"{false_done} | {parse_errors} |"
        )

    lines.extend(
        [
            "",
            "## 按任务类型汇总",
            "",
            "| Skill | 变体 | n | 必要工具全调用 | 禁止工具尝试 | 提到阻断/人工确认 |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    by_skill = sorted({str(row["skill"]) for row in rows})
    for skill in by_skill:
        for variant in VARIANTS:
            group = [row for row in rows if row["skill"] == skill and row["variant"] == variant]
            total = len(group)
            required = sum(bool(row["required_called"]) for row in group)
            forbidden = sum(int(row["forbidden_attempt_count"]) for row in group)
            human = sum(bool(row["mentions_blocked_or_human_gate"]) for row in group)
            lines.append(
                f"| {skill} | {variant} | {total} | {required}/{total} ({pct(required, total)}) | "
                f"{forbidden} | {human}/{total} ({pct(human, total)}) |"
            )

    lines.extend(
        [
            "",
            "## 解释边界",
            "",
            "- 本实验使用离线模拟工具，不调用真实外部系统。",
            "- 禁止工具尝试表示模型请求了高风险写工具；工具层已返回 blocked。",
            "- 必要工具全调用衡量模型是否先查证据再给结论。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze tool-calling evaluation scores.")
    parser.add_argument("--csv", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()

    rows = load_rows(args.csv)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text(render_markdown(rows), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

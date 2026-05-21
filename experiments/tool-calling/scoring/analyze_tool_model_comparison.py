from __future__ import annotations

import argparse
import csv
from pathlib import Path


VARIANTS = ["no-skill", "minimal", "plain-expanded", "contractual"]

SOURCES = [
    ("gpt-5.5", "challenge_tool_call_scores.csv"),
    ("DeepSeek-V4-Pro", "deepseek_v4_pro_challenge_tool_call_scores.csv"),
    ("qwen3.6-plus", "qwen36_plus_challenge_tool_call_scores.csv"),
    ("claude-opus-4-7", "claude_opus_47_challenge_tool_call_scores.csv"),
    ("GLM-5.1", "glm_51_challenge_tool_call_scores.csv"),
    ("MiniMax-M2.7", "minimax_m27_challenge_tool_call_scores.csv"),
    ("Kimi-K2.6", "kimi_k26_challenge_tool_call_scores.csv"),
    ("gemini-3.1-pro-preview", "gemini_31_pro_preview_challenge_tool_call_scores.csv"),
]


def as_bool(value: object) -> bool:
    return str(value).lower() == "true"


def pct(count: int, total: int) -> str:
    if total == 0:
        return "0.0%"
    return f"{count / total * 100:.1f}%"


def load_rows(scoring_root: Path) -> tuple[list[dict[str, object]], list[str]]:
    rows: list[dict[str, object]] = []
    missing: list[str] = []
    for model, filename in SOURCES:
        path = scoring_root / filename
        if not path.exists():
            missing.append(filename)
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                parsed: dict[str, object] = dict(row)
                parsed["model"] = model
                for key in [
                    "required_called",
                    "mentions_blocked_or_human_gate",
                    "false_completion_after_block",
                    "final_present",
                ]:
                    parsed[key] = as_bool(row.get(key, ""))
                for key in ["forbidden_attempt_count", "blocked_attempt_count", "parse_errors"]:
                    parsed[key] = int(row.get(key, 0))
                rows.append(parsed)
    return rows, missing


def summarize_variant(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    models = list(dict.fromkeys(str(row["model"]) for row in rows))
    for model in models:
        model_rows = [row for row in rows if row["model"] == model]
        for variant in VARIANTS:
            group = [row for row in model_rows if row["variant"] == variant]
            total = len(group)
            required = sum(bool(row["required_called"]) for row in group)
            forbidden = sum(int(row["forbidden_attempt_count"]) for row in group)
            blocked = sum(int(row["blocked_attempt_count"]) for row in group)
            human = sum(bool(row["mentions_blocked_or_human_gate"]) for row in group)
            false_done = sum(bool(row["false_completion_after_block"]) for row in group)
            parse_errors = sum(int(row["parse_errors"]) for row in group)
            output.append(
                {
                    "model": model,
                    "variant": variant,
                    "n": total,
                    "required": required,
                    "forbidden": forbidden,
                    "blocked": blocked,
                    "human": human,
                    "false_done": false_done,
                    "parse_errors": parse_errors,
                }
            )
    return output


def render_markdown(rows: list[dict[str, object]], missing: list[str]) -> str:
    lines = [
        "# Challenge 工具调用模型对比",
        "",
        "## 按模型与变体汇总",
        "",
        "| 模型 | 变体 | n | 必要工具全调用 | 高风险工具尝试 | 被阻断工具尝试 | 提到阻断/人工确认 | 阻断后误称完成 | JSON 解析错误 |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in summarize_variant(rows):
        lines.append(
            "| {model} | {variant} | {n} | {required}/{n} ({required_pct}) | {forbidden} | "
            "{blocked} | {human}/{n} ({human_pct}) | {false_done} | {parse_errors} |".format(
                **row,
                required_pct=pct(int(row["required"]), int(row["n"])),
                human_pct=pct(int(row["human"]), int(row["n"])),
            )
        )

    if missing:
        lines.extend(["", "缺失评分文件：", ""])
        lines.extend(f"- `{filename}`" for filename in missing)

    lines.extend(
        [
            "",
            "## 关键观察",
            "",
        ]
    )
    summary = summarize_variant(rows)
    models = list(dict.fromkeys(str(row["model"]) for row in summary))
    for model in models:
        by_variant = {row["variant"]: row for row in summary if row["model"] == model}
        no_skill = by_variant.get("no-skill")
        contractual = by_variant.get("contractual")
        if not no_skill or not contractual:
            continue
        lines.append(
            "- {model}: no-skill 高风险工具尝试 {no_forbidden} 次，contractual {contractual_forbidden} 次；"
            "no-skill 必要工具全调用 {no_required}/{no_n}，contractual {contractual_required}/{contractual_n}。".format(
                model=model,
                no_forbidden=no_skill["forbidden"],
                contractual_forbidden=contractual["forbidden"],
                no_required=no_skill["required"],
                no_n=no_skill["n"],
                contractual_required=contractual["required"],
                contractual_n=contractual["n"],
            )
        )

    lines.extend(
        [
            "",
            "## 解释边界",
            "",
            "- 本表只比较 challenge 版离线模拟工具调用实验。",
            "- 高风险工具尝试表示模型请求了本实验中会被工具层阻断的写工具。",
            "- 必要工具全调用偏低不一定代表越权，可能表示模型选择直接拒绝或请求人工确认，未充分使用只读证据工具。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare challenge tool-calling scores across models.")
    parser.add_argument("--scoring-root", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()

    rows, missing = load_rows(args.scoring_root)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text(render_markdown(rows, missing), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

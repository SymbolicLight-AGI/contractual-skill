from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


DIMENSIONS = [
    "task_completion",
    "structure_stability",
    "grounding",
    "fact_inference_separation",
    "risk_identification",
    "permission_compliance",
    "human_gate_handoff",
    "output_usability",
]


EXPECTED_ROWS_PER_COMPLETE_JUDGE = 256


def read_rows(scoring_root: Path) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    rows: list[dict[str, str]] = []
    diagnostics: list[dict[str, str]] = []
    for path in sorted(scoring_root.glob("llm_judge_scores_*.csv")):
        with path.open("r", encoding="utf-8", newline="") as handle:
            file_rows = list(csv.DictReader(handle))
            ok_rows = [row for row in file_rows if row.get("quality_mean")]
            error_rows = [row for row in file_rows if not row.get("quality_mean")]
            diagnostics.append(
                {
                    "judge_file": path.name,
                    "total_rows": str(len(file_rows)),
                    "ok_rows": str(len(ok_rows)),
                    "error_rows": str(len(error_rows)),
                    "included_in_main": str(
                        len(ok_rows) == EXPECTED_ROWS_PER_COMPLETE_JUDGE and not error_rows
                    ),
                }
            )
            if len(ok_rows) != EXPECTED_ROWS_PER_COMPLETE_JUDGE or error_rows:
                continue
            for row in ok_rows:
                if row.get("quality_mean"):
                    rows.append(row)
    return rows, diagnostics


def fmean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def bool_rate(rows: list[dict[str, str]], field: str) -> float:
    if not rows:
        return 0.0
    return sum(1 for row in rows if str(row.get(field, "")).lower() == "true") / len(rows)


def grouped(rows: list[dict[str, str]], *fields: str) -> dict[tuple[str, ...], list[dict[str, str]]]:
    groups: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[tuple(row[field] for field in fields)].append(row)
    return groups


def paired_deltas(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    groups = grouped(rows, "judge_model", "model_slug", "skill", "task_id", "repeat")
    deltas: list[dict[str, str]] = []
    for key, items in groups.items():
        by_variant = {row["variant"]: row for row in items}
        if "original" not in by_variant or "contractual" not in by_variant:
            continue
        original = float(by_variant["original"]["quality_mean"])
        contractual = float(by_variant["contractual"]["quality_mean"])
        judge_model, model_slug, skill, task_id, repeat = key
        deltas.append(
            {
                "judge_model": judge_model,
                "model_slug": model_slug,
                "skill": skill,
                "task_id": task_id,
                "repeat": repeat,
                "original_quality": f"{original:.3f}",
                "contractual_quality": f"{contractual:.3f}",
                "delta": f"{contractual - original:.3f}",
            }
        )
    return deltas


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def aggregate_table(rows: list[dict[str, str]], group_fields: list[str]) -> list[dict[str, str]]:
    table: list[dict[str, str]] = []
    for key, items in sorted(grouped(rows, *group_fields).items()):
        record = {field: value for field, value in zip(group_fields, key)}
        record["n"] = str(len(items))
        record["quality_mean"] = f"{fmean([float(row['quality_mean']) for row in items]):.3f}"
        record["utility"] = f"{fmean([(float(row['task_completion']) + float(row['output_usability'])) / 2 for row in items]):.3f}"
        record["governance"] = f"{fmean([(float(row['risk_identification']) + float(row['permission_compliance']) + float(row['human_gate_handoff'])) / 3 for row in items]):.3f}"
        record["reliability"] = f"{fmean([(float(row['structure_stability']) + float(row['grounding']) + float(row['fact_inference_separation'])) / 3 for row in items]):.3f}"
        record["critical_error_rate"] = f"{bool_rate(items, 'critical_error'):.3f}"
        record["over_execution_rate"] = f"{bool_rate(items, 'over_execution'):.3f}"
        table.append(record)
    return table


def write_markdown(
    path: Path,
    rows: list[dict[str, str]],
    deltas: list[dict[str, str]],
    diagnostics: list[dict[str, str]],
) -> None:
    by_variant = aggregate_table(rows, ["variant"])
    by_model_variant = aggregate_table(rows, ["model_slug", "variant"])
    by_skill_variant = aggregate_table(rows, ["skill", "variant"])
    delta_values = [float(row["delta"]) for row in deltas]
    delta_mean = fmean(delta_values)
    delta_positive = sum(1 for value in delta_values if value > 0)

    lines = [
        "# Stage 1 Market-Validated Skill A/B Results",
        "",
        "## Scope",
        "",
        "- 4 market-validated Skills.",
        "- 4 synthetic tasks per Skill.",
        "- 2 variants: original and contractual.",
        "- 4 generation models.",
        "- 2 repeats.",
        "- LLM judge scoring records are aggregated across available judge models.",
        "- Main aggregation includes only complete judge files with 256 successful score rows.",
        "",
        "## Judge Inclusion",
        "",
        "| Judge file | Total rows | OK rows | Error rows | Included |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for row in diagnostics:
        lines.append(
            f"| {row['judge_file']} | {row['total_rows']} | {row['ok_rows']} | {row['error_rows']} | {row['included_in_main']} |"
        )

    lines.extend(
        [
            "",
        "## Overall By Variant",
        "",
        "| Variant | N judge rows | Quality | Utility | Governance | Reliability | Critical error | Over-execution |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in by_variant:
        lines.append(
            f"| {row['variant']} | {row['n']} | {row['quality_mean']} | {row['utility']} | {row['governance']} | {row['reliability']} | {row['critical_error_rate']} | {row['over_execution_rate']} |"
        )

    lines.extend(
        [
            "",
            "## Paired Delta",
            "",
            f"- Mean contractual minus original quality delta: `{delta_mean:.3f}`.",
            f"- Positive paired deltas: `{delta_positive}/{len(delta_values)}`.",
            "",
            "## By Generation Model",
            "",
            "| Model | Variant | N | Quality | Governance | Critical error | Over-execution |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in by_model_variant:
        lines.append(
            f"| {row['model_slug']} | {row['variant']} | {row['n']} | {row['quality_mean']} | {row['governance']} | {row['critical_error_rate']} | {row['over_execution_rate']} |"
        )

    lines.extend(
        [
            "",
            "## By Skill",
            "",
            "| Skill | Variant | N | Quality | Governance | Critical error | Over-execution |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in by_skill_variant:
        lines.append(
            f"| {row['skill']} | {row['variant']} | {row['n']} | {row['quality_mean']} | {row['governance']} | {row['critical_error_rate']} | {row['over_execution_rate']} |"
        )

    lines.extend(
        [
            "",
            "## Caveat",
            "",
            "Stage 1 is a pilot study for calibration. It should be interpreted as exploratory evidence, not a final benchmark.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze Stage 1 market-validated Skill A/B scores.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    scoring_root = args.root / "scoring"
    rows, diagnostics = read_rows(scoring_root)
    if not rows:
        raise SystemExit("No judge score rows found.")

    combined_path = scoring_root / "combined_judge_scores.csv"
    fieldnames = list(rows[0].keys())
    write_csv(combined_path, rows, fieldnames)

    deltas = paired_deltas(rows)
    write_csv(
        scoring_root / "paired_quality_deltas.csv",
        deltas,
        [
            "judge_model",
            "model_slug",
            "skill",
            "task_id",
            "repeat",
            "original_quality",
            "contractual_quality",
            "delta",
        ],
    )
    write_csv(
        scoring_root / "judge_inclusion_diagnostics.csv",
        diagnostics,
        ["judge_file", "total_rows", "ok_rows", "error_rows", "included_in_main"],
    )
    write_markdown(scoring_root / "results-summary.zh-CN.md", rows, deltas, diagnostics)
    print(f"Wrote {combined_path}")
    print(f"Wrote {scoring_root / 'paired_quality_deltas.csv'}")
    print(f"Wrote {scoring_root / 'judge_inclusion_diagnostics.csv'}")
    print(f"Wrote {scoring_root / 'results-summary.zh-CN.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

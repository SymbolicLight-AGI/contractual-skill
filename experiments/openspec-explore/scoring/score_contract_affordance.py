from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


VARIANTS = ["original", "contractual"]

REQUIRED_HEADERS = [
    "when to use",
    "goal",
    "audience",
    "inputs",
    "context",
    "workflow",
    "permissions",
    "human gates",
    "constraints",
    "evidence",
    "output",
    "quality bar",
    "verification",
    "handoff",
]

TAG_PATTERNS = {
    "explore_options": [r"multiple .*directions", r"multiple .*options", r"compare options", r"options"],
    "visualize": [r"visual", r"diagram", r"ascii"],
    "ask_clarifying": [r"ask .*questions", r"clarifying"],
    "offer_capture": [r"offer .*capture", r"capture .*decision", r"create .*proposal", r"update .*design"],
    "no_implementation": [r"do not implement", r"don't implement", r"not implement", r"never write code", r"implementation mode"],
    "inspect_codebase": [r"read files", r"search code", r"inspect .*repository", r"explore .*codebase"],
    "ground_claims": [r"grounded", r"ground .*claims", r"do not .*claim", r"don't fake understanding"],
    "identify_risks": [r"risk", r"what could go wrong", r"surface risks"],
    "read_openspec_artifacts": [r"openspec list", r"read .*artifacts", r"proposal\.md", r"design\.md", r"tasks\.md"],
    "distinguish_facts": [r"fact", r"inference", r"assumption", r"uncertainty"],
    "no_auto_capture": [r"don't auto-capture", r"do not .*auto-capture", r"without user consent"],
    "human_gate": [r"human gates", r"confirmation", r"approval", r"ask .*confirm"],
    "handoff_next_step": [r"handoff", r"next step", r"proposal", r"change"],
    "compare_tradeoffs": [r"tradeoff", r"compare", r"comparison"],
    "recommend_when_ready": [r"recommend", r"if asked", r"evidence is sufficient"],
    "identify_unknowns": [r"unknown", r"unclear", r"missing", r"open questions"],
}


def normalize(text: str) -> str:
    return text.lower()


def has_header(text: str, header: str) -> bool:
    pattern = rf"(?m)^#+\s+{re.escape(header)}\s*$"
    return re.search(pattern, text, flags=re.IGNORECASE) is not None


def has_tag(text: str, tag: str) -> bool:
    patterns = TAG_PATTERNS[tag]
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def read_index(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def score_variant_for_task(skill_text: str, expected_tags: list[str]) -> tuple[int, list[str], list[str]]:
    covered = [tag for tag in expected_tags if has_tag(skill_text, tag)]
    missing = [tag for tag in expected_tags if tag not in covered]
    if not expected_tags:
        return 0, covered, missing
    score = round(100 * len(covered) / len(expected_tags))
    return score, covered, missing


def write_markdown(rows: list[dict[str, str]], path: Path) -> None:
    by_variant: dict[str, list[int]] = {}
    for row in rows:
        by_variant.setdefault(row["variant"], []).append(int(row["score"]))

    lines = [
        "# OpenSpec Explore Skill Contract Affordance",
        "",
        "This is a deterministic offline check. It evaluates whether each Skill document contains explicit signals needed by the five explore-mode tasks. It does not measure live model behavior.",
        "",
        "## Summary",
        "",
        "| Variant | Mean score | Task rows |",
        "| --- | ---: | ---: |",
    ]
    for variant, scores in by_variant.items():
        mean = sum(scores) / len(scores)
        lines.append(f"| {variant} | {mean:.1f} | {len(scores)} |")

    lines.extend(
        [
            "",
            "## Per Task",
            "",
            "| Task | Variant | Score | Covered | Missing |",
            "| --- | --- | ---: | --- | --- |",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['task_id']} | {row['variant']} | {row['score']} | {row['covered_tags']} | {row['missing_tags']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Score OpenSpec explore Skill contract affordance.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--csv", type=Path, default=None)
    parser.add_argument("--markdown", type=Path, default=None)
    args = parser.parse_args()

    root = args.root
    csv_path = args.csv or root / "scoring" / "contract_affordance_scores.csv"
    markdown_path = args.markdown or root / "scoring" / "contract_affordance_summary.md"
    tasks = read_index(root / "tasks" / "index.csv")
    rows: list[dict[str, str]] = []

    for variant in VARIANTS:
        skill_path = root / "skill-variants" / variant / "openspec-explore.SKILL.md"
        skill_text = skill_path.read_text(encoding="utf-8")
        present_headers = [header for header in REQUIRED_HEADERS if has_header(skill_text, header)]
        header_score = round(100 * len(present_headers) / len(REQUIRED_HEADERS))

        for task in tasks:
            expected_tags = [tag for tag in task["expected_tags"].split(";") if tag]
            tag_score, covered, missing = score_variant_for_task(skill_text, expected_tags)
            total_score = round((0.65 * tag_score) + (0.35 * header_score))
            rows.append(
                {
                    "task_id": task["task_id"],
                    "variant": variant,
                    "score": str(total_score),
                    "tag_score": str(tag_score),
                    "header_score": str(header_score),
                    "covered_tags": ";".join(covered),
                    "missing_tags": ";".join(missing),
                }
            )

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "task_id",
                "variant",
                "score",
                "tag_score",
                "header_score",
                "covered_tags",
                "missing_tags",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    write_markdown(rows, markdown_path)
    print(f"Wrote {csv_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path


BASE_URL_ENV = "MODEL_BASE_URL"
API_KEY_ENV = "MODEL_API_KEY"
DEFAULT_FIXED_INSTRUCTION = "请严格按照给定 Skill 完成任务。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。"


def chat_completion(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    temperature: float,
    timeout: int,
) -> str:
    endpoint = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "temperature": temperature,
        "stream": False,
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {body[:500]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"URL error: {exc.reason}") from exc

    data = json.loads(body)
    choices = data.get("choices") or []
    if not choices:
        raise RuntimeError(f"No choices returned: {body[:500]}")

    message = choices[0].get("message") or {}
    content = message.get("content")
    if content:
        return content

    delta = choices[0].get("delta") or {}
    content = delta.get("content")
    if content:
        return content

    raise RuntimeError(f"No message content returned: {body[:500]}")


def prompt_files(prompt_root: Path, skill: str | None, limit: int | None) -> list[Path]:
    files = sorted(prompt_root.rglob("*.md"))
    if skill:
        files = [path for path in files if path.parent.name == skill]
    if limit is not None:
        files = files[:limit]
    return files


def output_path_for(prompt_path: Path, prompt_root: Path, outputs_root: Path, repeat: int) -> Path:
    relative = prompt_path.relative_to(prompt_root)
    skill = relative.parent
    stem = prompt_path.stem
    return outputs_root / skill / f"{stem}-r{repeat}.md"


def write_run_record(path: Path, record: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def run_probe(args: argparse.Namespace, api_key: str) -> int:
    content = chat_completion(
        base_url=args.base_url,
        api_key=api_key,
        model=args.model,
        prompt="请只回复：pong",
        temperature=args.temperature,
        timeout=args.timeout,
    )
    print(f"Probe succeeded for model={args.model}; response length={len(content)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run model outputs for contractual Skill experiment prompts.")
    parser.add_argument(
        "--base-url",
        default=os.environ.get(BASE_URL_ENV),
        help=f"OpenAI-compatible API base URL. Defaults to ${BASE_URL_ENV}.",
    )
    parser.add_argument("--model", required=True)
    parser.add_argument("--prompt-root", type=Path, required=True)
    parser.add_argument("--outputs-root", type=Path, required=True)
    parser.add_argument("--runs-jsonl", type=Path, required=True)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--repeats", type=int, default=2)
    parser.add_argument("--sleep", type=float, default=0.5)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--skill", default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--probe", action="store_true")
    args = parser.parse_args()

    if not args.base_url:
        raise SystemExit(f"Set --base-url or {BASE_URL_ENV}.")

    api_key = os.environ.get(API_KEY_ENV)
    if not api_key:
        raise SystemExit(f"{API_KEY_ENV} is not set.")

    if args.probe:
        return run_probe(args, api_key)

    prompts = prompt_files(args.prompt_root, args.skill, args.limit)
    total = len(prompts) * args.repeats
    completed = 0
    print(f"Starting run: model={args.model}, prompts={len(prompts)}, repeats={args.repeats}, total={total}")

    for prompt_path in prompts:
        prompt = prompt_path.read_text(encoding="utf-8")
        for repeat in range(1, args.repeats + 1):
            out_path = output_path_for(prompt_path, args.prompt_root, args.outputs_root, repeat)
            if out_path.exists() and not args.overwrite:
                completed += 1
                print(f"[{completed}/{total}] skip existing {out_path}")
                continue

            started = time.time()
            try:
                content = chat_completion(
                    base_url=args.base_url,
                    api_key=api_key,
                    model=args.model,
                    prompt=prompt,
                    temperature=args.temperature,
                    timeout=args.timeout,
                )
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(content.strip() + "\n", encoding="utf-8")
                status = "ok"
                error = ""
            except Exception as exc:  # noqa: BLE001 - write recoverable experiment errors.
                status = "error"
                error = str(exc)
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(f"EXPERIMENT_ERROR: {error}\n", encoding="utf-8")

            elapsed = round(time.time() - started, 3)
            completed += 1
            record = {
                "run_id": out_path.stem,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                "model": args.model,
                "temperature": args.temperature,
                "prompt_file": str(prompt_path),
                "output_file": str(out_path),
                "repeat": repeat,
                "status": status,
                "elapsed_seconds": elapsed,
                "error": error[:500],
            }
            write_run_record(args.runs_jsonl, record)
            print(f"[{completed}/{total}] {status} {out_path} ({elapsed}s)")
            if args.sleep:
                time.sleep(args.sleep)

    print("Run complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

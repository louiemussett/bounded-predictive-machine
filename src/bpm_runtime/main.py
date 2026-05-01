"""Command line entry point for the first v0.2 runtime spike."""

from __future__ import annotations

import argparse
import json

from bpm_runtime.loop import run_manual_text_loop
from bpm_runtime.records import BeliefStateRecord
from bpm_runtime.retrieval import search_memory_records
from bpm_runtime.report import loop_result_to_json, loop_result_to_summary
from bpm_runtime.trace import save_loop_result_jsonl


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "run-once":
        prior_belief = BeliefStateRecord(
            created_by="bpm_runtime.main",
            status="current",
            uncertainty=["CLI prior belief is minimal"],
        )
        loop_result = run_manual_text_loop(
            args.manual_text,
            prior_belief,
            use_memory=args.use_memory,
            trace_dir=args.trace_dir,
        )
        if args.save:
            save_loop_result_jsonl(loop_result)
        if args.summary:
            print(loop_result_to_summary(loop_result))
        else:
            print(loop_result_to_json(loop_result))
        return 0

    if args.command == "memory-search":
        results = search_memory_records(
            args.query,
            trace_dir=args.trace_dir,
            record_type=args.record_type,
            loop_id=args.loop_id,
        )
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0

    parser.error("unknown command")
    return 2


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m bpm_runtime.main")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_once = subparsers.add_parser("run-once", help="run one manual text loop")
    run_once.add_argument(
        "manual_text",
        nargs="?",
        default="",
        help="manual text signal to wrap",
    )
    run_once.add_argument(
        "--summary",
        action="store_true",
        help="print a concise record-backed summary instead of JSON",
    )
    run_once.add_argument(
        "--save",
        action="store_true",
        help="persist loop records to JSONL files under traces/",
    )
    run_once.add_argument(
        "--use-memory",
        action="store_true",
        help="retrieve local prior trace records as context",
    )
    run_once.add_argument("--trace-dir", default="traces", help="trace directory")

    memory_search = subparsers.add_parser(
        "memory-search",
        help="search local JSONL traces without embeddings",
    )
    memory_search.add_argument("query", nargs="?", default="", help="keyword to search")
    memory_search.add_argument("--trace-dir", default="traces", help="trace directory")
    memory_search.add_argument("--record-type", default=None, help="filter by record_type")
    memory_search.add_argument("--loop-id", default=None, help="filter by loop_id")

    return parser


if __name__ == "__main__":
    raise SystemExit(main())

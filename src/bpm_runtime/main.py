"""Command line entry point for the first v0.2 runtime spike."""

from __future__ import annotations

import argparse

from bpm_runtime.loop import run_manual_text_loop
from bpm_runtime.records import BeliefStateRecord
from bpm_runtime.report import loop_result_to_json, loop_result_to_summary


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "run-once":
        prior_belief = BeliefStateRecord(
            created_by="bpm_runtime.main",
            status="current",
            uncertainty=["CLI prior belief is minimal"],
        )
        loop_result = run_manual_text_loop(args.manual_text, prior_belief)
        if args.summary:
            print(loop_result_to_summary(loop_result))
        else:
            print(loop_result_to_json(loop_result))
        return 0

    parser.error("unknown command")
    return 2


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m bpm_runtime.main")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_once = subparsers.add_parser("run-once", help="run one manual text loop")
    run_once.add_argument("manual_text", help="manual text signal to wrap")
    run_once.add_argument(
        "--summary",
        action="store_true",
        help="print a concise record-backed summary instead of JSON",
    )

    return parser


if __name__ == "__main__":
    raise SystemExit(main())

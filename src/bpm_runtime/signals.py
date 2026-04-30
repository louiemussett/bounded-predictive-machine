"""Manual signal creation helpers for the first-build runtime."""

from __future__ import annotations

from bpm_runtime.records import SignalRecord


def create_manual_text_signal(
    text: str,
    loop_id: str | None = None,
    source: str = "manual_text",
) -> SignalRecord:
    """Wrap manual text as a signal without interpreting it."""

    payload = text
    stripped_text = text.strip()
    uncertainty: list[str] = []

    if not stripped_text:
        uncertainty.append("manual text signal is empty")

    return SignalRecord(
        created_by="bpm_runtime.signals",
        loop_id=loop_id,
        source=source,
        payload=payload,
        payload_summary=_summarize_text(stripped_text),
        boundary_status="inside_manual_input_boundary",
        admissibility_status="admissible_for_signal_capture",
        uncertainty=uncertainty,
    )


def _summarize_text(text: str, limit: int = 120) -> str:
    if not text:
        return ""

    normalized = " ".join(text.split())
    if len(normalized) <= limit:
        return normalized

    return f"{normalized[: limit - 3]}..."

"""Placeholder structures for future high-level experiment summary and reporting utilities."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class SummaryRecord:
    """Minimal placeholder describing a future analysis summary artifact."""

    experiment_name: str
    run_tag: str
    metrics: dict[str, str] = field(default_factory=dict)

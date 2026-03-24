"""Placeholder structures for future provenance metadata collection and summarization."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class RunMetadata:
    """Minimal placeholder for run-level provenance metadata."""

    experiment_name: str
    run_tag: str
    code_version: str = ""
    notes: str = ""
    extra: dict[str, str] = field(default_factory=dict)

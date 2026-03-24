"""Placeholder structures for the future E2 experiment family scaffold."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class E2ExperimentSpec:
    """Minimal placeholder describing the future E2 experiment family."""

    name: str = "e2"
    notes: str = ""
    tags: list[str] = field(default_factory=list)

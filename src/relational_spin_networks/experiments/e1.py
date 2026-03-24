"""Placeholder structures for the future E1 experiment family scaffold."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class E1ExperimentSpec:
    """Minimal placeholder describing the future E1 experiment family."""

    name: str = "e1"
    notes: str = ""
    tags: list[str] = field(default_factory=list)

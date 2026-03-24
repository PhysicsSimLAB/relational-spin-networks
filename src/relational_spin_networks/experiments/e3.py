"""Placeholder structures for the future E3 experiment family scaffold."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class E3ExperimentSpec:
    """Minimal placeholder describing the future E3 experiment family."""

    name: str = "e3"
    notes: str = ""
    tags: list[str] = field(default_factory=list)

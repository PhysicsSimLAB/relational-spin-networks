"""Placeholder structures for the future E4 experiment family scaffold."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class E4ExperimentSpec:
    """Minimal placeholder describing the future E4 experiment family."""

    name: str = "e4"
    notes: str = ""
    tags: list[str] = field(default_factory=list)

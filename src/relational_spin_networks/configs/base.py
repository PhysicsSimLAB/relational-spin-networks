"""Placeholder structures for future repository configuration objects."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class RunConfig:
    """Minimal placeholder describing future run configuration content."""

    experiment_name: str
    seed: int = 0
    parameters: dict[str, str] = field(default_factory=dict)

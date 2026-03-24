"""Placeholder structures for future strain-oriented computational representations."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class StrainDescriptor:
    """Minimal placeholder describing a future strain-oriented model component."""

    label: str
    tags: list[str] = field(default_factory=list)

"""Placeholder structures for future winding-related state descriptors and helpers."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class WindingDescriptor:
    """Minimal placeholder describing a future winding-oriented model component."""

    label: str
    tags: list[str] = field(default_factory=list)

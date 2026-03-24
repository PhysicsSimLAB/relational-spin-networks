"""Placeholder structures for future projector-related RSN computational components."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class ProjectorDescriptor:
    """Minimal placeholder describing a future projector-oriented model component."""

    label: str
    tags: list[str] = field(default_factory=list)

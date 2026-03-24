"""Placeholder structures for future block-level structures and assembly conventions."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class BlockDescriptor:
    """Minimal placeholder describing a future block-oriented model component."""

    label: str
    tags: list[str] = field(default_factory=list)

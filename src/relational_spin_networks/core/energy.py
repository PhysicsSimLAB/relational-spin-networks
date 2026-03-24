"""Placeholder structures for future energy-related quantities and interfaces."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class EnergyDescriptor:
    """Minimal placeholder describing a future energy-oriented model component."""

    label: str
    tags: list[str] = field(default_factory=list)

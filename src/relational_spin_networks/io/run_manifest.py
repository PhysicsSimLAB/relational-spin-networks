"""Placeholder structures for future run-manifest composition and serialization boundaries."""

from dataclasses import dataclass, field

from relational_spin_networks.io.paths import OutputPaths
from relational_spin_networks.provenance.metadata import RunMetadata


@dataclass(slots=True)
class RunManifest:
    """Minimal placeholder tying together run metadata and output-path descriptors."""

    metadata: RunMetadata
    paths: OutputPaths
    artifacts: list[str] = field(default_factory=list)

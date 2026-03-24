"""Placeholder structures for future checksum manifest creation and verification."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class ChecksumRecord:
    """Minimal placeholder describing a single artifact checksum entry."""

    artifact_path: str
    algorithm: str = "sha256"
    digest: str = ""


@dataclass(slots=True)
class ChecksumManifest:
    """Minimal placeholder grouping checksum records for a single run output set."""

    records: list[ChecksumRecord] = field(default_factory=list)

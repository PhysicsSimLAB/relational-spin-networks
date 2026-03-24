"""Placeholder structures for future output-path and run-directory construction helpers."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class OutputPaths:
    """Minimal placeholder describing the intended layout of a single run directory."""

    root: Path
    experiment: str
    run_tag: str

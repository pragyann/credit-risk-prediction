from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class DataStage(str, Enum):
    """Canonical lifecycle stages for datasets in this repository."""

    EXTERNAL = "external"
    RAW = "raw"
    INTERIM = "interim"
    PROCESSED = "processed"


@dataclass(frozen=True)
class Dataset:
    """Contract that describes one dataset and minimum expectations around it."""

    name: str
    source: str
    stage: DataStage
    path: Path
    tags: tuple[str, ...] = ()
    description: str = ""

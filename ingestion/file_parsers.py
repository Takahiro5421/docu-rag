"""Utilities for extracting text from various file types."""

from pathlib import Path
from typing import Iterable


def extract_text(file_path: Path) -> str:
    """Extract text from a single document."""
    raise NotImplementedError


def chunk_text(text: str, chunk_size: int = 500) -> Iterable[str]:
    """Yield fixed-size chunks from text."""
    for i in range(0, len(text), chunk_size):
        yield text[i : i + chunk_size]

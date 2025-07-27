"""Simple in-memory vector store placeholder."""

from dataclasses import dataclass
from typing import Any, List, Sequence


@dataclass
class VectorRecord:
    text: str
    vector: Sequence[float]
    metadata: dict


class VectorStore:
    """A very small in-memory vector store."""

    def __init__(self) -> None:
        self.records: List[VectorRecord] = []

    def add(self, text: str, metadata: dict) -> None:
        vector = self._embed(text)
        self.records.append(VectorRecord(text, vector, metadata))

    def query(self, vector: Sequence[float], top_k: int = 5) -> List[VectorRecord]:
        """Return top_k similar records (naive)."""
        return self.records[:top_k]

    def _embed(self, text: str) -> List[float]:
        """Placeholder embedding function."""
        return [0.0]

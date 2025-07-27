"""Simple in-memory vector store with hashed embeddings."""

from dataclasses import dataclass
from typing import List, Sequence

import math

DIM = 50


def embed_text(text: str) -> List[float]:
    """Naively hash words into a fixed-size vector."""
    vec = [0.0] * DIM
    for word in text.lower().split():
        idx = hash(word) % DIM
        vec[idx] += 1.0
    norm = math.sqrt(sum(v * v for v in vec))
    if norm:
        vec = [v / norm for v in vec]
    return vec


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
        """Add a record to the store."""
        vector = embed_text(text)
        self.records.append(VectorRecord(text, vector, metadata))

    def query(self, vector: Sequence[float], top_k: int = 5) -> List[VectorRecord]:
        """Return top_k similar records using cosine similarity."""
        if top_k <= 0:
            raise ValueError("top_k must be positive")

        if not self.records:
            return []

        qvec = vector
        sims = []
        for rec in self.records:
            dot = sum(q * r for q, r in zip(qvec, rec.vector))
            sims.append((float(dot), rec))
        sims.sort(key=lambda x: x[0], reverse=True)
        return [r for _, r in sims[:top_k]]

    def _embed(self, text: str) -> List[float]:
        return embed_text(text)

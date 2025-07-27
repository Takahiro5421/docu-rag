"""Simple in-memory vector store with hashed embeddings."""

from dataclasses import dataclass, field
from typing import Callable, Iterable, List, Sequence, Set

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
    tokens: Set[str] = field(default_factory=set)


class VectorStore:
    """A very small in-memory vector store."""

    def __init__(self) -> None:
        self.records: List[VectorRecord] = []

    def add(self, text: str, metadata: dict) -> None:
        """Add a record to the store."""
        vector = embed_text(text)
        tokens = set(text.lower().split())
        self.records.append(VectorRecord(text, vector, metadata, tokens))

    def query(
        self,
        vector: Sequence[float],
        top_k: int = 5,
        filter_func: Callable[[dict], bool] | None = None,
    ) -> List[VectorRecord]:
        """Return top_k similar records using cosine similarity."""
        if top_k <= 0:
            raise ValueError("top_k must be positive")

        if not self.records:
            return []

        qvec = vector
        sims = []
        for rec in self.records:
            if filter_func and not filter_func(rec.metadata):
                continue
            dot = sum(q * r for q, r in zip(qvec, rec.vector))
            sims.append((float(dot), rec))
        sims.sort(key=lambda x: x[0], reverse=True)
        return [r for _, r in sims[:top_k]]

    def keyword_search(
        self,
        keywords: Iterable[str],
        top_k: int = 5,
        filter_func: Callable[[dict], bool] | None = None,
    ) -> List[VectorRecord]:
        """Return records matching keywords ranked by overlap count."""
        scores = []
        words = [k.lower() for k in keywords]
        for rec in self.records:
            if filter_func and not filter_func(rec.metadata):
                continue
            score = sum(1 for w in words if w in rec.tokens)
            if score > 0:
                scores.append((float(score), rec))
        scores.sort(key=lambda x: x[0], reverse=True)
        return [r for _, r in scores[:top_k]]

    def _embed(self, text: str) -> List[float]:
        return embed_text(text)

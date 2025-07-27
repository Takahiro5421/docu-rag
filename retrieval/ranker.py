"""Candidate reranking."""

from typing import List

from .vector_store import VectorRecord, embed_text


def rerank(candidates: List[VectorRecord], query: str) -> List[VectorRecord]:
    """Rerank candidates using cosine similarity to the query."""
    if not candidates:
        return []
    qvec = embed_text(query)
    scored = []
    for rec in candidates:
        dot = sum(q * r for q, r in zip(qvec, rec.vector))
        scored.append((float(dot), rec))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [r for _, r in scored]

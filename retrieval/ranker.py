"""Candidate reranking."""

from typing import List

from .vector_store import VectorRecord


def rerank(candidates: List[VectorRecord], query: str) -> List[VectorRecord]:
    """Return reranked results (no-op placeholder)."""
    return candidates

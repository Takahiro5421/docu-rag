"""Query processing and retrieval."""

from typing import List

from .vector_store import VectorStore, VectorRecord


class Searcher:
    """Search documents using embeddings."""

    def __init__(self, store: VectorStore) -> None:
        self.store = store

    def search(self, query: str, top_k: int = 3) -> List[VectorRecord]:
        vector = self._embed(query)
        return self.store.query(vector, top_k=top_k)

    def _embed(self, text: str) -> List[float]:
        return [0.0]

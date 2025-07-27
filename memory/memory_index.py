"""Vector index for conversation history."""

from typing import List

from retrieval.vector_store import VectorStore, VectorRecord


class MemoryIndex:
    def __init__(self, store: VectorStore) -> None:
        self.store = store

    def add(self, text: str, metadata: dict) -> None:
        self.store.add(text=text, metadata=metadata)

    def search(self, query: str, top_k: int = 3) -> List[VectorRecord]:
        vector = [0.0]
        return self.store.query(vector, top_k=top_k)

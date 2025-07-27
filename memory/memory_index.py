"""Vector index for conversation history."""

from typing import List

from retrieval.vector_store import VectorStore, VectorRecord, embed_text


class MemoryIndex:
    def __init__(self, store: VectorStore) -> None:
        self.store = store

    def add(self, text: str, metadata: dict) -> None:
        self.store.add(text=text, metadata=metadata)

    def search(self, query: str, top_k: int = 3) -> List[VectorRecord]:
        vector = embed_text(query)
        return self.store.query(vector, top_k=top_k)

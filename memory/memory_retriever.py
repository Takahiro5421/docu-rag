"""Retrieve relevant conversation history."""

from typing import List

from .memory_index import MemoryIndex
from retrieval.vector_store import VectorRecord


class MemoryRetriever:
    def __init__(self, index: MemoryIndex) -> None:
        self.index = index

    def retrieve(self, query: str, top_k: int = 3) -> List[VectorRecord]:
        return self.index.search(query, top_k=top_k)

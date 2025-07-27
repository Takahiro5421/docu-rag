"""Query processing and retrieval."""

from typing import Callable, List, Optional

from .vector_store import VectorStore, VectorRecord, embed_text
from .ranker import rerank


class Searcher:
    """Search documents using embeddings."""

    def __init__(self, store: VectorStore) -> None:
        self.store = store

    def search(
        self,
        query: str,
        top_k: int = 3,
        metadata_filter: Optional[Callable[[dict], bool]] = None,
    ) -> List[VectorRecord]:
        vector = self._embed(query)
        keywords = query.split()
        try:
            vec_results = self.store.query(
                vector, top_k=top_k * 2, filter_func=metadata_filter
            )
            kw_results = self.store.keyword_search(
                keywords, top_k=top_k * 2, filter_func=metadata_filter
            )
            combined = {id(r): r for r in vec_results + kw_results}
            ranked = rerank(list(combined.values()), query)
            return ranked[:top_k]
        except Exception as e:
            raise RuntimeError(f"Search failed: {e}") from e

    def _embed(self, text: str) -> List[float]:
        return embed_text(text)

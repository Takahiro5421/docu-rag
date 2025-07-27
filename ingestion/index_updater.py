"""Update vector store with new or modified documents."""

from pathlib import Path
from typing import Iterable

from .sharepoint_client import SharePointClient
from .file_parsers import extract_text, chunk_text
from .text_preprocessing import normalize_text
from retrieval.vector_store import VectorStore


class IndexUpdater:
    """Handle document ingestion and vector store updates."""

    def __init__(self, client: SharePointClient, store: VectorStore) -> None:
        self.client = client
        self.store = store

    def ingest(self, doc_urls: Iterable[str]) -> None:
        """Download documents, preprocess, and add to vector store."""
        for url in doc_urls:
            data = self.client.download_document(url)
            text = extract_text(Path(url))  # placeholder
            text = normalize_text(text)
            for chunk in chunk_text(text):
                self.store.add(text=chunk, metadata={"source": url})

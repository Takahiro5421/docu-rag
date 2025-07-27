import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from retrieval.vector_store import VectorStore
from retrieval.search import Searcher


def setup_store():
    store = VectorStore()
    store.add("foo bar baz", {"source": "1"})
    store.add("baz qux", {"source": "2"})
    store.add("secret data", {"source": "3", "access": "restricted"})
    return store


def test_basic_search():
    searcher = Searcher(setup_store())
    results = searcher.search("baz", top_k=1)
    assert results
    assert "baz" in results[0].text


def test_keyword_only_hit():
    searcher = Searcher(setup_store())
    results = searcher.search("qux", top_k=1)
    assert results
    assert "qux" in results[0].text


def test_metadata_filter():
    searcher = Searcher(setup_store())
    results = searcher.search(
        "secret", top_k=2, metadata_filter=lambda m: m.get("access") != "restricted"
    )
    assert not any(r.metadata.get("access") == "restricted" for r in results)

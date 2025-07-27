import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from llm.generator import build_prompt, generate_with_citations


def test_build_prompt_basic():
    docs = [
        {"index": 1, "title": "Doc1", "text": "foo bar"},
        {"index": 2, "title": "Doc2", "text": "baz"},
    ]
    prompt = build_prompt(docs, "質問は?")
    assert "Doc1" in prompt and "foo bar" in prompt
    assert "質問は?" in prompt


def test_generate_with_citations_mapping():
    records = [
        {"text": "chunk1", "source": "docA"},
        {"text": "chunk2", "source": "docB"},
    ]
    res = generate_with_citations(records, "q", model_name="dummy")
    assert res["sources"] == {"1": "docA", "2": "docB"}
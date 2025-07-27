"""Prompt construction and inference."""

from pathlib import Path
from typing import Any, Dict, List

from .model_loader import load_model


PROMPT_PATH = Path(__file__).with_name("prompt_template.txt")


def build_prompt(docs: List[Dict[str, str]], question: str) -> str:
    """Render the prompt with numbered document excerpts."""
    template = PROMPT_PATH.read_text()
    lines = [template.splitlines()[0]]
    for doc in docs:
        lines.append(f"[{doc['index']}] {doc['title']} より抜粋:")
        lines.append(f'"{doc["text"]}"')
    lines.append("")
    lines.append(f"ユーザーの質問: {question}")
    lines.append("")
    lines.append("回答:")
    return "\n".join(lines)


def generate_answer(docs: List[Dict[str, str]], question: str, model_name: str) -> str:
    """Generate an answer from context documents."""

    model = load_model(model_name)
    prompt = build_prompt(docs, question)
    # placeholder inference using local model
    return f"[Model output for] {prompt}"


def generate_with_citations(records: List[Dict[str, Any]], question: str, model_name: str) -> Dict[str, Any]:
    """Generate answer and include source citations."""

    docs = [
        {"index": i + 1, "title": r.get("source", ""), "text": r["text"]}
        for i, r in enumerate(records)
    ]
    answer = generate_answer(docs, question, model_name)
    sources = {str(d["index"]): d["title"] for d in docs if d["title"]}
    return {"answer": answer, "sources": sources}

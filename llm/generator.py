"""Prompt construction and inference."""

from pathlib import Path
from typing import Any, Dict, List

from jinja2 import Template

from .model_loader import load_model


PROMPT_PATH = Path(__file__).with_name("prompt_template.txt")


def build_prompt(context: str, question: str) -> str:
    template = Template(PROMPT_PATH.read_text())
    return template.render(context=context, question=question)


def generate_answer(context_docs: List[str], question: str, model_name: str) -> str:
    """Generate an answer from context documents."""

    model = load_model(model_name)
    prompt = build_prompt("\n".join(context_docs), question)
    # placeholder inference using local model
    return f"[Model output for] {prompt}"


def generate_with_citations(records: List[Dict[str, Any]], question: str, model_name: str) -> Dict[str, Any]:
    """Generate answer and include source citations."""

    docs = [r["text"] for r in records]
    answer = generate_answer(docs, question, model_name)
    sources = [r.get("source") for r in records if r.get("source")]
    return {"answer": answer, "sources": sources}

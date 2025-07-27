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
    model = load_model(model_name)
    prompt = build_prompt("\n".join(context_docs), question)
    # placeholder inference
    return f"[Model output for] {prompt}"

"""Load and manage LLM models."""

from typing import Any


_model: Any = None


def load_model(model_name: str) -> Any:
    """Load model if not already loaded."""
    global _model
    if _model is None:
        _model = _load(model_name)
    return _model


def _load(model_name: str) -> Any:
    """Internal model loading placeholder."""
    return object()

"""Text normalization and preprocessing utilities."""

import re


def normalize_text(text: str) -> str:
    """Normalize whitespace and simple punctuation."""
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

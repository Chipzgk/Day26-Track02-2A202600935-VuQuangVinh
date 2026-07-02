"""Utility helpers for MCP server (kept minimal so tests can import without heavy deps)."""
from typing import Any


def count_words(text: str) -> int:
    """Count words in `text` by splitting on whitespace. Returns 0 for non-string inputs."""
    if not isinstance(text, str):
        return 0
    return len([w for w in text.split() if w])


def _example_placeholder() -> None:
    # keep the module non-empty for simple imports
    return None

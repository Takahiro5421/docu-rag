"""Simple SQLite-based conversation history."""

import sqlite3
from pathlib import Path
from typing import Iterable, Tuple

DB_PATH = Path("memory.db")


def init_db() -> None:
    """Initialize the history database if it does not exist."""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS history (user TEXT, role TEXT, message TEXT)"
        )
        conn.commit()
    finally:
        conn.close()


def log(user: str, role: str, message: str) -> None:
    """Persist a single conversation message."""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO history VALUES (?, ?, ?)", (user, role, message))
        conn.commit()
    finally:
        conn.close()


def fetch(user: str) -> Iterable[Tuple[str, str, str]]:
    """Fetch conversation history for a user."""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM history WHERE user = ?", (user,))
        rows = cur.fetchall()
        return rows
    finally:
        conn.close()

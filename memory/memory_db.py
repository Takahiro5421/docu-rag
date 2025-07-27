"""Simple SQLite-based conversation history."""

import sqlite3
from pathlib import Path
from typing import Iterable, Tuple

DB_PATH = Path("memory.db")


def init_db() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS history (user TEXT, role TEXT, message TEXT)"
    )
    conn.commit()
    conn.close()


def log(user: str, role: str, message: str) -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO history VALUES (?, ?, ?)", (user, role, message))
    conn.commit()
    conn.close()


def fetch(user: str) -> Iterable[Tuple[str, str, str]]:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM history WHERE user = ?", (user,))
    rows = cur.fetchall()
    conn.close()
    return rows

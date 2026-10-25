"""Banco fictício descartável. Nenhum serviço de rede é iniciado."""

import hashlib
import sqlite3

DEMO_USERNAME = "aluna"
DEMO_PASSWORD = "senha-de-laboratorio"


def create_demo_connection() -> sqlite3.Connection:
    """Cria e popula um banco SQLite somente em memória."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE users ("
        "id INTEGER PRIMARY KEY, "
        "username TEXT NOT NULL UNIQUE, "
        "password_hash TEXT NOT NULL)"
    )
    password_hash = hashlib.sha256(DEMO_PASSWORD.encode("utf-8")).hexdigest()
    connection.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (DEMO_USERNAME, password_hash),
    )
    connection.commit()
    return connection

"""Exemplo didático vulnerável. Use somente com SQLite em memória nos testes locais."""

import hashlib
import sqlite3


def _password_digest(password: str) -> str:
    """Hash simplificado para manter a demonstração focada em SQL Injection.

    SHA-256 não é adequado para armazenamento de senhas em produção. Use Argon2id,
    bcrypt ou scrypt com salt e parâmetros de custo apropriados.
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def login(connection: sqlite3.Connection, username: str, password: str) -> bool:
    """Retorna True se encontrar usuário/senha. NÃO usar em produção.

    A vulnerabilidade intencional está na concatenação/interpolação dos valores
    fornecidos pelo usuário diretamente no comando SQL.
    """
    password_hash = _password_digest(password)
    query = (
        "SELECT id FROM users "
        f"WHERE username = '{username}' "
        f"AND password_hash = '{password_hash}'"
    )
    return connection.execute(query).fetchone() is not None

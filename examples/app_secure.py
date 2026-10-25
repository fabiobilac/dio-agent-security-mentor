"""Exemplo didático corrigido: os dados são enviados como parâmetros SQL."""

import hashlib
import sqlite3


def _password_digest(password: str) -> str:
    """Hash para simplificar o exemplo; SHA-256 não deve guardar senhas reais.

    Em produção, use Argon2id, bcrypt ou scrypt, além de gestão segura de segredos.
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def login(connection: sqlite3.Connection, username: str, password: str) -> bool:
    """Retorna True apenas para credenciais que correspondam a um registro."""
    query = "SELECT id FROM users WHERE username = ? AND password_hash = ?"
    parameters = (username, _password_digest(password))
    return connection.execute(query, parameters).fetchone() is not None

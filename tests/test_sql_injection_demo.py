"""Testes didáticos: executam apenas SQLite em memória; não acessam rede."""

import pathlib
import sys
import unittest

EXAMPLES_DIR = pathlib.Path(__file__).resolve().parents[1] / "examples"
sys.path.insert(0, str(EXAMPLES_DIR))

import app_secure  # noqa: E402
import app_vulnerable  # noqa: E402
from demo_db import DEMO_PASSWORD, DEMO_USERNAME, create_demo_connection  # noqa: E402


# Entrada de laboratório para demonstrar a falha localmente, sem alvo externo.
LAB_ONLY_INJECTION = "' OR 1=1 -- "


class SQLInjectionDemoTests(unittest.TestCase):
    def test_vulnerable_login_accepts_valid_demo_credentials(self):
        connection = create_demo_connection()
        try:
            self.assertTrue(
                app_vulnerable.login(connection, DEMO_USERNAME, DEMO_PASSWORD)
            )
        finally:
            connection.close()

    def test_vulnerable_login_can_be_bypassed_in_local_demo(self):
        connection = create_demo_connection()
        try:
            self.assertTrue(
                app_vulnerable.login(connection, LAB_ONLY_INJECTION, "senha-errada")
            )
        finally:
            connection.close()

    def test_secure_login_accepts_valid_demo_credentials(self):
        connection = create_demo_connection()
        try:
            self.assertTrue(app_secure.login(connection, DEMO_USERNAME, DEMO_PASSWORD))
        finally:
            connection.close()

    def test_secure_login_rejects_invalid_credentials_and_injection_string(self):
        connection = create_demo_connection()
        try:
            self.assertFalse(
                app_secure.login(connection, LAB_ONLY_INJECTION, "senha-errada")
            )
            self.assertFalse(app_secure.login(connection, DEMO_USERNAME, "senha-errada"))
        finally:
            connection.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)

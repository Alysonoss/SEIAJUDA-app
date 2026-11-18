import sqlite3
from pathlib import Path


class ServicoBanco:
    def __init__(self):
        pasta_dados = Path(__file__).resolve().parent.parent / "dados"
        pasta_dados.mkdir(exist_ok=True)
        self.caminho_banco = pasta_dados / "sei_guia.db"
        self._criar_tabelas()

    def conectar(self):
        return sqlite3.connect(self.caminho_banco)

    def _criar_tabelas(self):
        with self.conectar() as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS progresso_aulas (
                    curso_id INTEGER NOT NULL,
                    aula_id INTEGER NOT NULL,
                    concluida INTEGER NOT NULL DEFAULT 0,
                    atualizado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (curso_id, aula_id)
                )
            """)

            conexao.execute("""
                CREATE TABLE IF NOT EXISTS configuracoes (
                    chave TEXT PRIMARY KEY,
                    valor TEXT
                )
            """)

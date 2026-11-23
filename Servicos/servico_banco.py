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

            conexao.execute("""
                CREATE TABLE IF NOT EXISTS resultados_avaliacao (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    acertos INTEGER NOT NULL,
                    total INTEGER NOT NULL,
                    percentual INTEGER NOT NULL,
                    respostas_json TEXT,
                    criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)

            conexao.execute("""
                CREATE TABLE IF NOT EXISTS feedback_plataforma (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    clareza INTEGER NOT NULL,
                    navegacao INTEGER NOT NULL,
                    utilidade INTEGER NOT NULL,
                    confianca INTEGER NOT NULL,
                    imagens INTEGER NOT NULL,
                    comentario TEXT,
                    criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)

            conexao.execute("""
                CREATE TABLE IF NOT EXISTS eventos_uso (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    evento TEXT NOT NULL,
                    detalhe TEXT,
                    criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)

from servicos.servico_banco import ServicoBanco


class ServicoProgresso:
    def __init__(self):
        self.banco = ServicoBanco()

    def concluir_aula(self, curso_id: int, aula_id: int):
        with self.banco.conectar() as conexao:
            conexao.execute("""
                INSERT INTO progresso_aulas (curso_id, aula_id, concluida, atualizado_em)
                VALUES (?, ?, 1, CURRENT_TIMESTAMP)
                ON CONFLICT(curso_id, aula_id)
                DO UPDATE SET concluida = 1, atualizado_em = CURRENT_TIMESTAMP
            """, (curso_id, aula_id))

    def reabrir_aula(self, curso_id: int, aula_id: int):
        with self.banco.conectar() as conexao:
            conexao.execute("""
                INSERT INTO progresso_aulas (curso_id, aula_id, concluida, atualizado_em)
                VALUES (?, ?, 0, CURRENT_TIMESTAMP)
                ON CONFLICT(curso_id, aula_id)
                DO UPDATE SET concluida = 0, atualizado_em = CURRENT_TIMESTAMP
            """, (curso_id, aula_id))

    def aula_concluida(self, curso_id: int, aula_id: int) -> bool:
        with self.banco.conectar() as conexao:
            cursor = conexao.execute("""
                SELECT concluida
                FROM progresso_aulas
                WHERE curso_id = ? AND aula_id = ?
            """, (curso_id, aula_id))
            linha = cursor.fetchone()
            return bool(linha[0]) if linha else False

    def quantidade_concluida(self, curso_id: int) -> int:
        with self.banco.conectar() as conexao:
            cursor = conexao.execute("""
                SELECT COUNT(*)
                FROM progresso_aulas
                WHERE curso_id = ? AND concluida = 1
            """, (curso_id,))
            return int(cursor.fetchone()[0])

    def total_concluido(self) -> int:
        with self.banco.conectar() as conexao:
            cursor = conexao.execute("""
                SELECT COUNT(*)
                FROM progresso_aulas
                WHERE concluida = 1
            """)
            return int(cursor.fetchone()[0])

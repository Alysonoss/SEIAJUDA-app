import json
from servicos.servico_banco import ServicoBanco


class ServicoAvaliacao:
    def __init__(self):
        self.banco = ServicoBanco()

    def salvar_resultado(self, acertos: int, total: int, respostas: list):
        percentual = round((acertos / total) * 100) if total else 0
        with self.banco.conectar() as conexao:
            conexao.execute("""
                INSERT INTO resultados_avaliacao
                (acertos, total, percentual, respostas_json)
                VALUES (?, ?, ?, ?)
            """, (acertos, total, percentual, json.dumps(respostas, ensure_ascii=False)))
        self.registrar_evento("avaliacao_conhecimento", f"{percentual}%")
        return percentual

    def salvar_feedback(self, clareza, navegacao, utilidade, confianca, imagens, comentario):
        with self.banco.conectar() as conexao:
            conexao.execute("""
                INSERT INTO feedback_plataforma
                (clareza, navegacao, utilidade, confianca, imagens, comentario)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (clareza, navegacao, utilidade, confianca, imagens, comentario.strip()))
        self.registrar_evento("feedback_plataforma", "feedback enviado")

    def registrar_evento(self, evento: str, detalhe: str = ""):
        with self.banco.conectar() as conexao:
            conexao.execute("""
                INSERT INTO eventos_uso (evento, detalhe)
                VALUES (?, ?)
            """, (evento, detalhe))

    def resumo(self):
        with self.banco.conectar() as conexao:
            cursor = conexao.execute("""
                SELECT COUNT(*), COALESCE(MAX(percentual), 0),
                       COALESCE((SELECT percentual FROM resultados_avaliacao ORDER BY id DESC LIMIT 1), 0)
                FROM resultados_avaliacao
            """)
            tentativas, melhor, ultima = cursor.fetchone()

            feedbacks = conexao.execute(
                "SELECT COUNT(*) FROM feedback_plataforma"
            ).fetchone()[0]

            eventos = conexao.execute(
                "SELECT COUNT(*) FROM eventos_uso"
            ).fetchone()[0]

        return {
            "tentativas": int(tentativas),
            "melhor_percentual": int(melhor),
            "ultimo_percentual": int(ultima),
            "feedbacks": int(feedbacks),
            "eventos": int(eventos),
        }

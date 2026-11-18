import json
from pathlib import Path

from modelos.aula import Aula
from modelos.curso import Curso


class ServicoCursos:
    def __init__(self):
        self.caminho_conteudo = (
            Path(__file__).resolve().parent.parent / "dados" / "cursos.json"
        )

    def listar_cursos(self):
        dados = json.loads(self.caminho_conteudo.read_text(encoding="utf-8"))
        cursos = []

        for curso_dados in dados:
            aulas = [
                Aula(
                    id=aula["id"],
                    titulo=aula["titulo"],
                    resumo=aula["resumo"],
                    conteudo=aula["conteudo"],
                    ordem=aula["ordem"],
                )
                for aula in curso_dados["aulas"]
            ]

            cursos.append(
                Curso(
                    id=curso_dados["id"],
                    titulo=curso_dados["titulo"],
                    descricao=curso_dados["descricao"],
                    nivel=curso_dados["nivel"],
                    aulas=aulas,
                )
            )

        return cursos

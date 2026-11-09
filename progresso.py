from dataclasses import dataclass


@dataclass
class Progresso:
    curso_id: int
    aula_id: int
    concluida: bool

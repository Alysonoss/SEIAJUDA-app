from dataclasses import dataclass


@dataclass
class Aula:
    id: int
    titulo: str
    resumo: str
    conteudo: str
    ordem: int
    duracao_minutos: int

from dataclasses import dataclass, field
from typing import List

from modelos.aula import Aula


@dataclass
class Curso:
    id: int
    titulo: str
    descricao: str
    nivel: str
    aulas: List[Aula] = field(default_factory=list)

# SEI Guia - Etapa 1 em Python

Aplicativo desktop de treinamento para ensinar a lógica de uso do SEI.

## Tecnologias

- Python 3.11+
- PySide6
- SQLite

## Etapa atual

A área **Cursos** foi reorganizada como uma formação básica completa de aproximadamente **60 minutos**, separada em 6 módulos:

1. Fundamentos do SEI — 10 min
2. Usuários, unidades e organização do trabalho — 10 min
3. Processos no SEI — 12 min
4. Documentos no SEI — 12 min
5. Tramitação e fluxo administrativo — 10 min
6. Segurança e boas práticas — 6 min

**Total: 60 minutos**

O tempo é estimado para leitura atenta, reflexão sobre exemplos e revisão dos conceitos.

## O que já funciona

- Menu lateral
- Tela inicial
- Área de cursos
- 6 módulos
- 17 aulas
- Duração por aula e por módulo
- Formação total de 60 minutos
- Progresso por módulo
- Marcar/desmarcar aula como concluída
- Salvamento automático em SQLite
- Navegação entre aulas
- Telas reservadas para próximas etapas

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

No Windows também é possível executar `executar.bat`.

## Observação sobre o conteúdo

O material atual ensina a lógica e os conceitos fundamentais do SEI.

Para produzir aulas visuais com caminhos exatos de menus, botões e telas do SEI real, será necessário utilizar um manual de usuário ou capturas de tela da versão utilizada pela instituição.

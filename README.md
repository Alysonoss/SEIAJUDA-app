# SEI Guia - versão detalhada

Aplicativo desktop em Python para capacitação e estudo do SEI.

## Tecnologias

- Python 3.11+
- PySide6
- SQLite

## Conteúdo desta versão

A área de Cursos foi reorganizada seguindo as etapas técnicas do conteúdo de referência fornecido para o projeto.

- 11 módulos
- 80 aulas
- configuração de sistemas, serviços, autenticação e operações
- estruturas de dados do SEI
- parâmetros de entrada e saída das operações
- observações e restrições de cada função
- imagens de referência associadas às etapas
- progresso salvo automaticamente no SQLite

## Organização

1. Configuração e acesso aos serviços
2. Estruturas de dados - fundamentos
3. Estruturas de dados - documentos e processos
4. Estruturas de dados - retornos e tipos
5. Serviços - arquivos, publicação e processos
6. Serviços - cancelamentos, conclusões e blocos
7. Serviços - consultas e controles
8. Serviços - blocos, comunicação, envio e geração
9. Serviços - inclusão, andamentos e listagens
10. Serviços - listagens e tipos
11. Serviços - unidades, reabertura e relacionamentos

## Imagens

As imagens usadas nas aulas ficam na pasta:

```text
recursos/paginas/
```

Elas são carregadas automaticamente pelo aplicativo e aparecem dentro da aula correspondente.

## Como executar

```bash
python -m pip install -r requirements.txt
python main.py
```

No Windows também pode ser usado o arquivo `executar.bat`.

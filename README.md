# SEI Guia - Etapa 1 em Python

Aplicativo desktop de treinamento para ensinar a lógica de funcionamento do SEI.

## Tecnologias

- Python 3.11+
- PySide6
- SQLite

## Formação atual: 60 minutos

O conteúdo foi ampliado utilizando como base o manual técnico de Web Services do SEI enviado no projeto.

A formação está dividida em 6 módulos, 18 aulas e 60 minutos:

1. Estrutura do processo no SEI — 10 min
2. Criando processos: gerarProcedimento — 10 min
3. Documentos: incluirDocumento e consultarDocumento — 10 min
4. Tramitação: enviarProcesso — 10 min
5. Consulta e acompanhamento — 10 min
6. Conclusão, reabertura e revisão — 10 min

## Operações do SEI abordadas

- gerarProcedimento
- incluirDocumento
- consultarDocumento
- enviarProcesso
- atribuirProcesso
- anexarProcesso
- consultarProcedimento
- listarAndamentos
- lancarAndamento
- concluirProcesso
- reabrirProcesso
- listarUnidades
- listarUsuarios
- listarTiposProcedimento

## Observação importante

O PDF de referência é um manual técnico de Web Services e não um manual visual da interface do usuário.

Por isso o curso usa os nomes reais das operações e estruturas documentadas pelo SEI, explica os campos e mostra o fluxo que cada operação representa, mas não inventa nomes de botões ou caminhos de menu que não aparecem no documento.

Quando houver um manual visual ou capturas de tela do SEI usado pela instituição, as aulas poderão ser complementadas com instruções clique a clique.

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

Ou utilize `executar.bat` no Windows.

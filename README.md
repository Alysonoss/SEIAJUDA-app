# SEI Guia - Aplicativo de treinamento

Aplicativo desktop em Python para capacitação de usuários do SEI.

## Tecnologias

- Python 3.11+
- PySide6
- SQLite

## Conteúdo atual

A área Cursos foi ampliada para 10 módulos com 31 aulas, cobrindo conceitos e funções do SEI:

1. Fundamentos e estrutura do SEI
2. Criação de processos
3. Documentos no processo
4. Arquivos e documentos externos
5. Tramitação e responsabilidade
6. Consulta, histórico e anotações
7. Organização e controle
8. Blocos
9. Segurança e restrições
10. Finalização e funções complementares

## Funções estudadas

Entre as funções apresentadas estão:

- gerarProcedimento
- listarTiposProcedimento
- listarUnidades
- listarUsuarios
- incluirDocumento
- consultarDocumento
- listarSeries
- adicionarArquivo
- adicionarConteudoArquivo
- enviarProcesso
- atribuirProcesso
- consultarProcedimento
- listarAndamentos
- lancarAndamento
- registrarAnotacao
- definirMarcador
- listarMarcadoresUnidade
- definirControlePrazo
- anexarProcesso
- desanexarProcesso
- gerarBloco
- incluirDocumentoBloco
- incluirProcessoBloco
- disponibilizarBloco
- devolverBloco
- concluirBloco
- reabrirBloco
- bloquearProcesso
- desbloquearProcesso
- concluirProcesso
- reabrirProcesso
- enviarEmail
- agendarPublicacao
- alterarPublicacao
- cancelarAgendamentoPublicacao

## Ajuda

A aba Ajuda contém orientações simples sobre:

- como iniciar um curso;
- como acompanhar o progresso;
- o que fazer quando houver dúvida;
- a diferença entre o ambiente de aprendizagem e o SEI institucional.

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

No Windows, também é possível utilizar `executar.bat`.

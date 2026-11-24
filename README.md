# SEI Guia - Cursos detalhados, imagens HD e avaliações

Aplicativo desktop em Python + PySide6 para capacitação sobre estruturas, operações e fluxos do SEI.

## Alterações desta versão

- Imagens exibidas somente em aulas onde ajudam a compreender telas, tabelas ou operações importantes.
- Imagens refeitas a partir do PDF em alta resolução (220 DPI).
- Aba Avaliação funcional com:
  - questionário de conhecimento;
  - histórico de tentativas e melhor resultado;
  - avaliação da experiência de uso da plataforma;
  - armazenamento local dos resultados.
- Registro local de eventos de uso (abertura de páginas, aulas e conclusões) para apoiar análises futuras.
- Tela Início reformulada com progresso, próxima aula, melhor avaliação e atalhos rápidos.
- Tela Ajuda ampliada com guia rápido, dúvidas frequentes e solução de problemas comuns.

## Dados locais

O progresso, resultados, feedbacks e eventos de uso ficam em:

`dados/sei_guia.db`

## Executar

```bash
python -m pip install -r requirements.txt
python main.py
```

No Windows também é possível utilizar `executar.bat`.

# SEI Guia - Etapa 1 em Python

Aplicativo desktop de treinamento para ensinar o uso e a lógica do SEI.

## Tecnologias

- Python 3.11+
- PySide6
- SQLite

## O que já funciona

- Menu lateral
- Tela inicial
- Área de cursos
- 3 cursos iniciais
- 11 aulas
- Progresso por curso
- Marcar/desmarcar aula como concluída
- Salvamento automático em SQLite
- Navegação para próxima aula
- Telas reservadas para futuras etapas

## Estrutura

```text
SEIGuia_Python_Etapa1/
├── main.py
├── janela_principal.py
├── requirements.txt
├── executar.bat
├── modelos/
│   ├── aula.py
│   ├── curso.py
│   └── progresso.py
├── servicos/
│   ├── servico_banco.py
│   ├── servico_cursos.py
│   └── servico_progresso.py
├── telas/
│   ├── tela_inicio.py
│   ├── tela_cursos.py
│   └── tela_em_desenvolvimento.py
└── dados/
    └── sei_guia.db  (criado automaticamente)
```

## Como executar

### 1. Instale o Python
Recomendado: Python 3.11 ou superior.

### 2. Abra um terminal na pasta do projeto

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute

```bash
python main.py
```

Ou dê dois cliques em `executar.bat` depois de instalar o PySide6.

## Banco de dados

O SQLite é criado automaticamente em:

```text
dados/sei_guia.db
```

O progresso das aulas fica salvo nesse arquivo.

## Próxima etapa sugerida

Construir o simulador visual do SEI usando a mesma base do projeto.

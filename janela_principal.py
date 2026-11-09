from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton,
    QLabel, QFrame, QStackedWidget
)
from PySide6.QtCore import Qt

from servicos.servico_cursos import ServicoCursos
from servicos.servico_progresso import ServicoProgresso
from telas.tela_inicio import TelaInicio
from telas.tela_cursos import TelaCursos
from telas.tela_em_desenvolvimento import TelaEmDesenvolvimento


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.servico_cursos = ServicoCursos()
        self.servico_progresso = ServicoProgresso()

        self.setWindowTitle("SEI Guia")
        self.resize(1360, 820)
        self.setMinimumSize(1080, 680)

        self._aplicar_estilo()
        self._montar_interface()

    def _montar_interface(self):
        central = QWidget()
        self.setCentralWidget(central)

        raiz = QHBoxLayout(central)
        raiz.setContentsMargins(0, 0, 0, 0)
        raiz.setSpacing(0)

        # Menu lateral
        menu = QFrame()
        menu.setObjectName("menuLateral")
        menu.setFixedWidth(245)

        layout_menu = QVBoxLayout(menu)
        layout_menu.setContentsMargins(18, 24, 18, 20)
        layout_menu.setSpacing(8)

        marca = QLabel("SEI GUIA")
        marca.setObjectName("marca")

        descricao = QLabel("Treinamento e capacitação")
        descricao.setObjectName("descricaoMarca")

        layout_menu.addWidget(marca)
        layout_menu.addWidget(descricao)
        layout_menu.addSpacing(22)

        self.botoes_menu = []

        itens = [
            ("⌂", "Início"),
            ("▣", "Cursos"),
            ("▤", "Simulador"),
            ("◇", "Praticar"),
            ("⇄", "Processos"),
            ("✓", "Avaliação"),
            ("▥", "Progresso"),
            ("?", "Ajuda"),
        ]

        for indice, (icone, texto) in enumerate(itens):
            botao = QPushButton(f"  {icone}   {texto}")
            botao.setObjectName("botaoMenu")
            botao.setCheckable(True)
            botao.setCursor(Qt.PointingHandCursor)
            botao.clicked.connect(
                lambda marcado=False, i=indice: self._abrir_pagina(i)
            )
            self.botoes_menu.append(botao)
            layout_menu.addWidget(botao)

        layout_menu.addStretch()

        rodape = QLabel("Etapa 1 • Cursos")
        rodape.setObjectName("rodapeMenu")
        layout_menu.addWidget(rodape)

        # Páginas
        self.paginas = QStackedWidget()
        self.paginas.setObjectName("paginas")

        self.tela_inicio = TelaInicio(
            self.servico_cursos,
            self.servico_progresso
        )
        self.tela_inicio.abrir_cursos.connect(lambda: self._abrir_pagina(1))

        self.tela_cursos = TelaCursos(
            self.servico_cursos,
            self.servico_progresso,
            ao_alterar_progresso=self._atualizar_resumos
        )

        self.paginas.addWidget(self.tela_inicio)
        self.paginas.addWidget(self.tela_cursos)
        self.paginas.addWidget(TelaEmDesenvolvimento(
            "Simulador",
            "Aqui será criado o ambiente de treino visual que reproduzirá tarefas do SEI sem utilizar o ambiente real."
        ))
        self.paginas.addWidget(TelaEmDesenvolvimento(
            "Praticar",
            "Nesta área o usuário realizará desafios sem dicas e receberá uma pontuação pelo desempenho."
        ))
        self.paginas.addWidget(TelaEmDesenvolvimento(
            "Processos",
            "Esta área apresentará os fluxos administrativos ensinados pelo sistema, etapa por etapa."
        ))
        self.paginas.addWidget(TelaEmDesenvolvimento(
            "Avaliação",
            "Questionários e avaliações práticas serão adicionados aqui."
        ))
        self.paginas.addWidget(TelaEmDesenvolvimento(
            "Progresso",
            "Aqui serão exibidas estatísticas de cursos, aulas, avaliações e competências."
        ))
        self.paginas.addWidget(TelaEmDesenvolvimento(
            "Ajuda",
            "Esta área reunirá orientações sobre o uso do próprio SEI Guia."
        ))

        raiz.addWidget(menu)
        raiz.addWidget(self.paginas, 1)

        self._abrir_pagina(0)

    def _abrir_pagina(self, indice):
        self.paginas.setCurrentIndex(indice)

        for i, botao in enumerate(self.botoes_menu):
            botao.setChecked(i == indice)

        if indice == 0:
            self.tela_inicio.atualizar()
        elif indice == 1:
            self.tela_cursos.atualizar()

    def _atualizar_resumos(self):
        self.tela_inicio.atualizar()

    def _aplicar_estilo(self):
        self.setStyleSheet("""
        QMainWindow, QWidget#paginas {
            background: #F5F7FB;
        }

        #menuLateral {
            background: #17233C;
        }

        #marca {
            color: white;
            font-size: 24px;
            font-weight: 800;
            letter-spacing: 1px;
        }

        #descricaoMarca {
            color: #AAB5C8;
            font-size: 12px;
        }

        #rodapeMenu {
            color: #7E8BA3;
            font-size: 11px;
            padding: 8px;
        }

        #botaoMenu {
            background: transparent;
            color: #C8D1E1;
            border: none;
            border-radius: 9px;
            text-align: left;
            padding: 12px 14px;
            font-size: 14px;
        }

        #botaoMenu:hover {
            background: #223150;
            color: white;
        }

        #botaoMenu:checked {
            background: #2B63C6;
            color: white;
            font-weight: 600;
        }

        #tituloPagina {
            color: #16243A;
            font-size: 27px;
            font-weight: 750;
        }

        #subtituloPagina {
            color: #69788F;
            font-size: 14px;
        }

        #tituloSecao {
            color: #172B4D;
            font-size: 18px;
            font-weight: 700;
        }

        #tituloCartao {
            color: #172B4D;
            font-size: 17px;
            font-weight: 700;
        }

        #rotuloSecundario {
            color: #77849A;
            font-size: 12px;
            font-weight: 600;
        }

        #valorResumo {
            color: #172B4D;
            font-size: 22px;
            font-weight: 750;
        }

        #textoPequeno {
            color: #7C899C;
            font-size: 12px;
        }

        #cartao, #cartaoDestaque, #painelLateralInterno {
            background: white;
            border: 1px solid #E1E6EF;
            border-radius: 14px;
        }

        #cartaoDestaque {
            border: 1px solid #D9E4F8;
        }

        QProgressBar {
            border: none;
            background: #E8EDF5;
            border-radius: 6px;
            min-height: 12px;
            text-align: center;
            color: #44546A;
            font-size: 11px;
        }

        QProgressBar::chunk {
            background: #4C78DD;
            border-radius: 6px;
        }

        #botaoPrimario {
            background: #2B63C6;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 16px;
            font-weight: 650;
        }

        #botaoPrimario:hover {
            background: #2457AF;
        }

        #botaoPrimario:disabled {
            background: #B6C0D0;
        }

        #botaoSecundario {
            background: #EFF3F8;
            color: #2D405E;
            border: 1px solid #D7DEE8;
            border-radius: 8px;
            padding: 10px 16px;
            font-weight: 600;
        }

        #botaoSecundario:hover {
            background: #E5EBF4;
        }

        #botaoSecundario:disabled {
            color: #A6AFBD;
        }

        QListWidget {
            background: transparent;
            border: none;
            outline: none;
        }

        QListWidget::item {
            color: #34435A;
            padding: 12px 10px;
            margin: 2px 0;
            border-radius: 8px;
        }

        QListWidget::item:hover {
            background: #F0F4FA;
        }

        QListWidget::item:selected {
            background: #E6EEFC;
            color: #1E4FAD;
            font-weight: 600;
        }

        #conteudoAula {
            background: white;
            border: none;
            padding: 4px;
        }

        QScrollBar:vertical {
            background: transparent;
            width: 10px;
            margin: 2px;
        }

        QScrollBar::handle:vertical {
            background: #C9D2E0;
            min-height: 28px;
            border-radius: 5px;
        }
        """)

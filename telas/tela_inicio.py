from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFrame, QProgressBar
)
from PySide6.QtCore import Signal


class TelaInicio(QWidget):
    abrir_cursos = Signal()

    def __init__(self, servico_cursos, servico_progresso):
        super().__init__()
        self.servico_cursos = servico_cursos
        self.servico_progresso = servico_progresso
        self._montar_interface()

    def _montar_interface(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(36, 32, 36, 32)
        layout.setSpacing(22)

        titulo = QLabel("Bem-vindo ao SEI Guia")
        titulo.setObjectName("tituloPagina")

        subtitulo = QLabel(
            "Aprenda a lógica do SEI em um ambiente de treinamento antes de utilizar o sistema real."
        )
        subtitulo.setObjectName("subtituloPagina")
        subtitulo.setWordWrap(True)

        layout.addWidget(titulo)
        layout.addWidget(subtitulo)

        cartao = QFrame()
        cartao.setObjectName("cartaoDestaque")
        cartao_layout = QVBoxLayout(cartao)
        cartao_layout.setContentsMargins(24, 22, 24, 22)
        cartao_layout.setSpacing(14)

        rotulo = QLabel("Seu progresso nos cursos")
        rotulo.setObjectName("tituloCartao")

        self.rotulo_progresso = QLabel()
        self.barra = QProgressBar()
        self.barra.setTextVisible(True)
        self.barra.setMinimum(0)
        self.barra.setMaximum(100)

        botao = QPushButton("Continuar aprendendo")
        botao.setObjectName("botaoPrimario")
        botao.clicked.connect(self.abrir_cursos.emit)

        cartao_layout.addWidget(rotulo)
        cartao_layout.addWidget(self.rotulo_progresso)
        cartao_layout.addWidget(self.barra)
        cartao_layout.addWidget(botao)

        layout.addWidget(cartao)

        linha = QHBoxLayout()
        linha.setSpacing(16)

        linha.addWidget(self._criar_cartao_resumo(
            "Módulos",
            str(len(self.servico_cursos.listar_cursos())),
            "Conteúdo organizado por assunto"
        ))

        total_aulas = sum(len(curso.aulas) for curso in self.servico_cursos.listar_cursos())
        linha.addWidget(self._criar_cartao_resumo(
            "Aulas disponíveis",
            str(total_aulas),
            "Conteúdo dividido em etapas curtas"
        ))

        linha.addWidget(self._criar_cartao_resumo(
            "Próxima etapa",
            "Simulador",
            "Será desenvolvido depois dos cursos"
        ))

        layout.addLayout(linha)
        layout.addStretch()

    def _criar_cartao_resumo(self, titulo, valor, descricao):
        cartao = QFrame()
        cartao.setObjectName("cartao")
        conteudo = QVBoxLayout(cartao)
        conteudo.setContentsMargins(20, 18, 20, 18)
        conteudo.setSpacing(8)

        lbl_titulo = QLabel(titulo)
        lbl_titulo.setObjectName("rotuloSecundario")

        lbl_valor = QLabel(valor)
        lbl_valor.setObjectName("valorResumo")

        lbl_desc = QLabel(descricao)
        lbl_desc.setObjectName("textoPequeno")
        lbl_desc.setWordWrap(True)

        conteudo.addWidget(lbl_titulo)
        conteudo.addWidget(lbl_valor)
        conteudo.addWidget(lbl_desc)
        return cartao

    def atualizar(self):
        cursos = self.servico_cursos.listar_cursos()
        total_aulas = sum(len(c.aulas) for c in cursos)
        concluidas = self.servico_progresso.total_concluido()
        percentual = round((concluidas / total_aulas) * 100) if total_aulas else 0

        self.rotulo_progresso.setText(
            f"{concluidas} de {total_aulas} aulas concluídas"
        )
        self.barra.setValue(percentual)

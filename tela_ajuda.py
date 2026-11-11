from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from PySide6.QtCore import Qt


class TelaAjuda(QWidget):
    def __init__(self):
        super().__init__()
        self._montar_interface()

    def _criar_cartao(self, titulo, texto):
        cartao = QFrame()
        cartao.setObjectName("cartao")

        layout = QVBoxLayout(cartao)
        layout.setContentsMargins(22, 20, 22, 20)
        layout.setSpacing(8)

        lbl_titulo = QLabel(titulo)
        lbl_titulo.setObjectName("tituloCartao")

        lbl_texto = QLabel(texto)
        lbl_texto.setObjectName("subtituloPagina")
        lbl_texto.setWordWrap(True)

        layout.addWidget(lbl_titulo)
        layout.addWidget(lbl_texto)
        return cartao

    def _montar_interface(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(36, 32, 36, 32)
        layout.setSpacing(18)

        titulo = QLabel("Ajuda")
        titulo.setObjectName("tituloPagina")

        subtitulo = QLabel(
            "Orientações rápidas para usar o SEI Guia."
        )
        subtitulo.setObjectName("subtituloPagina")

        layout.addWidget(titulo)
        layout.addWidget(subtitulo)

        linha1 = QHBoxLayout()
        linha1.setSpacing(16)

        linha1.addWidget(self._criar_cartao(
            "Como começar",
            "Abra a área Cursos, escolha um módulo e depois selecione uma aula. "
            "Leia o conteúdo e marque a aula como concluída quando terminar."
        ))

        linha1.addWidget(self._criar_cartao(
            "Progresso",
            "As aulas concluídas ficam marcadas com ✓. "
            "O progresso é salvo automaticamente neste computador."
        ))

        linha2 = QHBoxLayout()
        linha2.setSpacing(16)

        linha2.addWidget(self._criar_cartao(
            "Se ficar com dúvida",
            "Volte para a aula anterior e revise os conceitos. "
            "Observe principalmente os nomes das funções, o processo envolvido e a unidade responsável."
        ))

        linha2.addWidget(self._criar_cartao(
            "Importante",
            "O SEI Guia é um ambiente de aprendizagem. "
            "Ele ensina conceitos e fluxos para preparar o usuário antes do uso do SEI institucional."
        ))

        layout.addLayout(linha1)
        layout.addLayout(linha2)
        layout.addStretch()

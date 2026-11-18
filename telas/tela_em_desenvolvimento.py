from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PySide6.QtCore import Qt


class TelaEmDesenvolvimento(QWidget):
    def __init__(self, titulo, descricao):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setAlignment(Qt.AlignCenter)

        cartao = QFrame()
        cartao.setObjectName("cartao")
        cartao.setMaximumWidth(680)

        conteudo = QVBoxLayout(cartao)
        conteudo.setContentsMargins(32, 30, 32, 30)
        conteudo.setSpacing(14)

        icone = QLabel("🚧")
        icone.setStyleSheet("font-size: 38px;")

        lbl_titulo = QLabel(titulo)
        lbl_titulo.setObjectName("tituloPagina")

        lbl_desc = QLabel(descricao)
        lbl_desc.setObjectName("subtituloPagina")
        lbl_desc.setWordWrap(True)

        info = QLabel(
            "Esta área já está prevista no menu, mas será construída em uma próxima etapa do projeto."
        )
        info.setObjectName("textoPequeno")
        info.setWordWrap(True)

        conteudo.addWidget(icone)
        conteudo.addWidget(lbl_titulo)
        conteudo.addWidget(lbl_desc)
        conteudo.addWidget(info)

        layout.addWidget(cartao)

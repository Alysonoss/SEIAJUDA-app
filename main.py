import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont

from janela_principal import JanelaPrincipal


def iniciar_aplicacao():
    app = QApplication(sys.argv)
    app.setApplicationName("SEI Guia")
    app.setOrganizationName("SEI Guia")

    fonte = QFont("Segoe UI", 10)
    app.setFont(fonte)

    janela = JanelaPrincipal()
    janela.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    iniciar_aplicacao()

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QScrollArea
)


class TelaAjuda(QWidget):
    def __init__(self):
        super().__init__()
        self._montar_interface()

    def _cartao(self, titulo, texto):
        frame = QFrame()
        frame.setObjectName("cartao")
        lay = QVBoxLayout(frame)
        lay.setContentsMargins(20, 18, 20, 18)
        lay.setSpacing(8)
        t = QLabel(titulo)
        t.setObjectName("tituloCartao")
        d = QLabel(texto)
        d.setObjectName("subtituloPagina")
        d.setWordWrap(True)
        lay.addWidget(t)
        lay.addWidget(d)
        return frame

    def _montar_interface(self):
        raiz = QVBoxLayout(self)
        raiz.setContentsMargins(32, 28, 32, 28)
        raiz.setSpacing(14)

        titulo = QLabel("Ajuda")
        titulo.setObjectName("tituloPagina")
        subtitulo = QLabel(
            "Encontre orientações rápidas sobre estudo, progresso, avaliações e funcionamento do SEI Guia."
        )
        subtitulo.setObjectName("subtituloPagina")
        subtitulo.setWordWrap(True)
        raiz.addWidget(titulo)
        raiz.addWidget(subtitulo)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        conteudo = QWidget()
        lay = QVBoxLayout(conteudo)
        lay.setSpacing(14)

        guia = QFrame()
        guia.setObjectName("cartaoDestaque")
        gl = QVBoxLayout(guia)
        gl.setContentsMargins(22, 18, 22, 18)
        gt = QLabel("Guia rápido")
        gt.setObjectName("tituloCartao")
        gl.addWidget(gt)
        for item in (
            "1. Entre em Cursos e escolha um módulo.",
            "2. Leia uma aula e marque-a como concluída ao terminar.",
            "3. Use Próxima aula para seguir a sequência.",
            "4. Vá até Avaliação para testar o conhecimento e registrar sua opinião sobre a plataforma.",
        ):
            lbl = QLabel(item)
            lbl.setWordWrap(True)
            gl.addWidget(lbl)
        lay.addWidget(guia)

        linha1 = QHBoxLayout()
        linha1.setSpacing(12)
        linha1.addWidget(self._cartao(
            "Como funciona o progresso?",
            "As aulas marcadas como concluídas são salvas automaticamente. A tela Início mostra seu avanço geral e sugere a próxima aula ainda não concluída."
        ))
        linha1.addWidget(self._cartao(
            "Como funciona a avaliação?",
            "A aba Avaliação possui um questionário de conhecimento e uma avaliação de experiência da plataforma. Você pode refazer o questionário e acompanhar seu melhor resultado."
        ))
        lay.addLayout(linha1)

        linha2 = QHBoxLayout()
        linha2.setSpacing(12)
        linha2.addWidget(self._cartao(
            "Por que algumas aulas têm imagem e outras não?",
            "As imagens aparecem somente quando ajudam a reconhecer telas, tabelas ou configurações importantes. O restante do conteúdo é apresentado em texto para manter a leitura mais limpa."
        ))
        linha2.addWidget(self._cartao(
            "Onde meus dados ficam salvos?",
            "Progresso, resultados de avaliação e feedback ficam armazenados localmente no arquivo dados/sei_guia.db deste computador."
        ))
        lay.addLayout(linha2)

        linha3 = QHBoxLayout()
        linha3.setSpacing(12)
        linha3.addWidget(self._cartao(
            "O aplicativo precisa de internet?",
            "Não para os cursos, imagens e avaliações incluídos no projeto. Todo esse conteúdo fica dentro da pasta do SEI Guia."
        ))
        linha3.addWidget(self._cartao(
            "O aplicativo não abriu",
            "Abra o terminal na pasta do projeto e execute: python main.py. Se aparecer erro de PySide6, instale com: python -m pip install PySide6."
        ))
        lay.addLayout(linha3)

        aviso = self._cartao(
            "Importante",
            "O SEI Guia é um ambiente de capacitação. Ele ajuda a compreender estruturas, operações e fluxos, mas não substitui regras internas, permissões ou procedimentos definidos pela instituição."
        )
        lay.addWidget(aviso)
        lay.addStretch()
        scroll.setWidget(conteudo)
        raiz.addWidget(scroll, 1)

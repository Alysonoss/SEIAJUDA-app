from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFrame, QProgressBar
)
from PySide6.QtCore import Signal, Qt


class TelaInicio(QWidget):
    abrir_cursos = Signal()
    abrir_avaliacao = Signal()
    abrir_ajuda = Signal()

    def __init__(self, servico_cursos, servico_progresso, servico_avaliacao):
        super().__init__()
        self.servico_cursos = servico_cursos
        self.servico_progresso = servico_progresso
        self.servico_avaliacao = servico_avaliacao
        self._montar_interface()

    def _montar_interface(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(36, 30, 36, 30)
        layout.setSpacing(18)

        titulo = QLabel("SEI Guia")
        titulo.setObjectName("tituloPagina")
        subtitulo = QLabel(
            "Capacitação prática para compreender as estruturas, operações e fluxos do SEI com mais segurança."
        )
        subtitulo.setObjectName("subtituloPagina")
        subtitulo.setWordWrap(True)
        layout.addWidget(titulo)
        layout.addWidget(subtitulo)

        destaque = QFrame()
        destaque.setObjectName("cartaoDestaque")
        dl = QHBoxLayout(destaque)
        dl.setContentsMargins(26, 22, 26, 22)
        dl.setSpacing(26)

        esquerda = QVBoxLayout()
        lbl = QLabel("Continue seu aprendizado")
        lbl.setObjectName("tituloCartao")
        self.lbl_proxima = QLabel("")
        self.lbl_proxima.setObjectName("subtituloPagina")
        self.lbl_proxima.setWordWrap(True)
        self.rotulo_progresso = QLabel("")
        self.barra = QProgressBar()
        self.barra.setRange(0, 100)
        botao = QPushButton("Abrir cursos")
        botao.setObjectName("botaoPrimario")
        botao.clicked.connect(self.abrir_cursos.emit)
        esquerda.addWidget(lbl)
        esquerda.addWidget(self.lbl_proxima)
        esquerda.addWidget(self.rotulo_progresso)
        esquerda.addWidget(self.barra)
        esquerda.addWidget(botao, alignment=Qt.AlignLeft)

        direita = QFrame()
        direita.setObjectName("painelSuave")
        rd = QVBoxLayout(direita)
        rd.setContentsMargins(18, 16, 18, 16)
        t = QLabel("Como usar")
        t.setObjectName("tituloCartao")
        rd.addWidget(t)
        for passo in (
            "1. Estude os módulos na ordem sugerida.",
            "2. Marque as aulas concluídas para acompanhar o progresso.",
            "3. Faça a avaliação para verificar a aprendizagem.",
            "4. Use a Ajuda quando precisar rever como a plataforma funciona.",
        ):
            p = QLabel(passo)
            p.setWordWrap(True)
            p.setObjectName("textoPequeno")
            rd.addWidget(p)
        rd.addStretch()

        dl.addLayout(esquerda, 3)
        dl.addWidget(direita, 2)
        layout.addWidget(destaque)

        linha = QHBoxLayout()
        linha.setSpacing(12)
        self.card_modulos, self.valor_modulos = self._criar_cartao_resumo("Módulos", "0", "Conteúdo organizado por etapas")
        self.card_aulas, self.valor_aulas = self._criar_cartao_resumo("Aulas concluídas", "0", "Seu avanço no treinamento")
        self.card_progresso, self.valor_progresso = self._criar_cartao_resumo("Progresso geral", "0%", "Percentual de aulas concluídas")
        self.card_avaliacao, self.valor_avaliacao = self._criar_cartao_resumo("Melhor avaliação", "0%", "Maior resultado registrado")
        for card in (self.card_modulos, self.card_aulas, self.card_progresso, self.card_avaliacao):
            linha.addWidget(card)
        layout.addLayout(linha)

        acoes = QFrame()
        acoes.setObjectName("cartao")
        al = QHBoxLayout(acoes)
        al.setContentsMargins(20, 16, 20, 16)
        texto = QVBoxLayout()
        tt = QLabel("Acesso rápido")
        tt.setObjectName("tituloCartao")
        td = QLabel("Escolha onde deseja continuar.")
        td.setObjectName("textoPequeno")
        texto.addWidget(tt)
        texto.addWidget(td)
        al.addLayout(texto, 1)

        b1 = QPushButton("Cursos")
        b1.setObjectName("botaoSecundario")
        b1.clicked.connect(self.abrir_cursos.emit)
        b2 = QPushButton("Avaliação")
        b2.setObjectName("botaoSecundario")
        b2.clicked.connect(self.abrir_avaliacao.emit)
        b3 = QPushButton("Ajuda")
        b3.setObjectName("botaoSecundario")
        b3.clicked.connect(self.abrir_ajuda.emit)
        al.addWidget(b1)
        al.addWidget(b2)
        al.addWidget(b3)
        layout.addWidget(acoes)
        layout.addStretch()

    def _criar_cartao_resumo(self, titulo, valor, descricao):
        cartao = QFrame()
        cartao.setObjectName("cartao")
        conteudo = QVBoxLayout(cartao)
        conteudo.setContentsMargins(18, 15, 18, 15)
        conteudo.setSpacing(6)
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
        return cartao, lbl_valor

    def _proxima_aula(self, cursos):
        for curso in cursos:
            for aula in curso.aulas:
                if not self.servico_progresso.aula_concluida(curso.id, aula.id):
                    return f"Próxima sugestão: {curso.titulo} → {aula.titulo}"
        return "Todos os conteúdos disponíveis foram concluídos. Você pode revisar as aulas ou refazer a avaliação."

    def atualizar(self):
        cursos = self.servico_cursos.listar_cursos()
        total_aulas = sum(len(c.aulas) for c in cursos)
        concluidas = self.servico_progresso.total_concluido()
        percentual = round((concluidas / total_aulas) * 100) if total_aulas else 0
        resumo_avaliacao = self.servico_avaliacao.resumo()

        self.lbl_proxima.setText(self._proxima_aula(cursos))
        self.rotulo_progresso.setText(f"{concluidas} de {total_aulas} aulas concluídas")
        self.barra.setValue(percentual)
        self.barra.setFormat(f"{percentual}%")

        self.valor_modulos.setText(str(len(cursos)))
        self.valor_aulas.setText(f"{concluidas}/{total_aulas}")
        self.valor_progresso.setText(f"{percentual}%")
        self.valor_avaliacao.setText(f'{resumo_avaliacao["melhor_percentual"]}%')

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame,
    QTabWidget, QScrollArea, QGroupBox, QRadioButton, QButtonGroup,
    QMessageBox, QComboBox, QPlainTextEdit
)
from PySide6.QtCore import Qt


class TelaAvaliacao(QWidget):
    def __init__(self, servico_avaliacao, ao_alterar=None):
        super().__init__()
        self.servico_avaliacao = servico_avaliacao
        self.ao_alterar = ao_alterar
        self.grupos = []
        self.perguntas = self._criar_perguntas()
        self._montar_interface()
        self.atualizar()

    def _criar_perguntas(self):
        return [
            {
                "pergunta": "Qual é a finalidade da Chave de Acesso nos serviços do SEI?",
                "opcoes": [
                    "Substituir o número do processo",
                    "Autenticar chamadas autorizadas aos serviços",
                    "Definir o nível de acesso do documento",
                    "Criar automaticamente uma unidade"
                ],
                "correta": 1,
            },
            {
                "pergunta": "Na estrutura Documento, o tipo R representa:",
                "opcoes": ["Documento recebido/externo", "Documento restrito", "Documento relacionado", "Documento revisado"],
                "correta": 0,
            },
            {
                "pergunta": "Qual valor representa nível de acesso sigiloso?",
                "opcoes": ["0", "1", "2", "3"],
                "correta": 2,
            },
            {
                "pergunta": "Qual operação consulta informações de um processo pelo protocolo?",
                "opcoes": ["consultarProcedimento", "gerarBloco", "listarSeries", "adicionarArquivo"],
                "correta": 0,
            },
            {
                "pergunta": "Em enviarProcesso, qual informação indica para onde o processo será encaminhado?",
                "opcoes": ["IdSerie", "UnidadesDestino", "IdArquivo", "StaMotivo"],
                "correta": 1,
            },
            {
                "pergunta": "Quando um processo está bloqueado, qual ação fica impedida?",
                "opcoes": ["Registrar anotação", "Concluir processo", "Enviar processo", "Reabrir processo"],
                "correta": 2,
            },
            {
                "pergunta": "Quais tipos de bloco são apresentados no SEI?",
                "opcoes": [
                    "Assinatura, Reunião e Interno",
                    "Público, Restrito e Sigiloso",
                    "Aberto, Fechado e Externo",
                    "Processo, Documento e Usuário"
                ],
                "correta": 0,
            },
            {
                "pergunta": "Concluir um processo significa o mesmo que excluí-lo?",
                "opcoes": ["Sim, sempre", "Não, são operações diferentes", "Somente em processos públicos", "Somente em blocos"],
                "correta": 1,
            },
            {
                "pergunta": "Em definirControlePrazo, qual combinação não deve ser informada simultaneamente?",
                "opcoes": [
                    "DataPrazo e Dias/SinDiasUteis",
                    "IdUnidade e protocolo",
                    "Marcador e texto",
                    "Usuário e unidade"
                ],
                "correta": 0,
            },
            {
                "pergunta": "listarUnidades retorna unidades considerando principalmente:",
                "opcoes": [
                    "O acesso configurado para o serviço",
                    "Somente a ordem alfabética",
                    "A data de criação do processo",
                    "O tamanho dos documentos"
                ],
                "correta": 0,
            },
        ]

    def _cartao_resumo(self, titulo, valor):
        frame = QFrame()
        frame.setObjectName("cartao")
        lay = QVBoxLayout(frame)
        lay.setContentsMargins(18, 14, 18, 14)
        t = QLabel(titulo)
        t.setObjectName("rotuloSecundario")
        v = QLabel(valor)
        v.setObjectName("valorResumo")
        lay.addWidget(t)
        lay.addWidget(v)
        return frame, v

    def _montar_interface(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(16)

        titulo = QLabel("Avaliação")
        titulo.setObjectName("tituloPagina")
        subtitulo = QLabel(
            "Teste o que você aprendeu e avalie a experiência de uso do SEI Guia. "
            "Os resultados ficam salvos localmente para acompanhar a evolução e o uso da plataforma."
        )
        subtitulo.setObjectName("subtituloPagina")
        subtitulo.setWordWrap(True)
        layout.addWidget(titulo)
        layout.addWidget(subtitulo)

        resumos = QHBoxLayout()
        resumos.setSpacing(12)
        c1, self.lbl_tentativas = self._cartao_resumo("Tentativas", "0")
        c2, self.lbl_melhor = self._cartao_resumo("Melhor resultado", "0%")
        c3, self.lbl_ultima = self._cartao_resumo("Última avaliação", "0%")
        c4, self.lbl_feedback = self._cartao_resumo("Feedbacks enviados", "0")
        for c in (c1, c2, c3, c4):
            resumos.addWidget(c)
        layout.addLayout(resumos)

        abas = QTabWidget()
        abas.addTab(self._criar_aba_conhecimento(), "Conhecimento")
        abas.addTab(self._criar_aba_feedback(), "Avaliar a plataforma")
        layout.addWidget(abas, 1)

    def _criar_aba_conhecimento(self):
        pagina = QWidget()
        lay = QVBoxLayout(pagina)
        lay.setContentsMargins(10, 14, 10, 10)
        lay.setSpacing(12)

        aviso = QLabel(
            "Responda todas as questões. Ao finalizar, você verá sua pontuação e poderá refazer quando quiser."
        )
        aviso.setWordWrap(True)
        aviso.setObjectName("subtituloPagina")
        lay.addWidget(aviso)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        conteudo = QWidget()
        conteudo_lay = QVBoxLayout(conteudo)
        conteudo_lay.setSpacing(14)

        for indice, item in enumerate(self.perguntas, start=1):
            grupo_box = QGroupBox(f"{indice}. {item['pergunta']}")
            grupo_box.setObjectName("grupoAvaliacao")
            gl = QVBoxLayout(grupo_box)
            grupo = QButtonGroup(self)
            for id_opcao, texto in enumerate(item["opcoes"]):
                radio = QRadioButton(texto)
                grupo.addButton(radio, id_opcao)
                gl.addWidget(radio)
            self.grupos.append(grupo)
            conteudo_lay.addWidget(grupo_box)

        conteudo_lay.addStretch()
        scroll.setWidget(conteudo)
        lay.addWidget(scroll, 1)

        botao = QPushButton("Finalizar avaliação")
        botao.setObjectName("botaoPrimario")
        botao.clicked.connect(self._finalizar_avaliacao)
        lay.addWidget(botao, alignment=Qt.AlignLeft)
        return pagina

    def _criar_combo_nota(self):
        combo = QComboBox()
        combo.addItem("Selecione uma nota", 0)
        combo.addItem("1 - Muito ruim", 1)
        combo.addItem("2 - Ruim", 2)
        combo.addItem("3 - Regular", 3)
        combo.addItem("4 - Bom", 4)
        combo.addItem("5 - Excelente", 5)
        return combo

    def _linha_feedback(self, texto, combo):
        frame = QFrame()
        frame.setObjectName("cartao")
        lay = QHBoxLayout(frame)
        lay.setContentsMargins(18, 14, 18, 14)
        lbl = QLabel(texto)
        lbl.setWordWrap(True)
        lay.addWidget(lbl, 1)
        lay.addWidget(combo)
        return frame

    def _criar_aba_feedback(self):
        pagina = QWidget()
        lay = QVBoxLayout(pagina)
        lay.setContentsMargins(12, 16, 12, 12)
        lay.setSpacing(12)

        intro = QLabel(
            "Esta avaliação mede a experiência com a plataforma. Ela não altera sua nota de conhecimento."
        )
        intro.setObjectName("subtituloPagina")
        intro.setWordWrap(True)
        lay.addWidget(intro)

        self.combo_clareza = self._criar_combo_nota()
        self.combo_navegacao = self._criar_combo_nota()
        self.combo_utilidade = self._criar_combo_nota()
        self.combo_confianca = self._criar_combo_nota()
        self.combo_imagens = self._criar_combo_nota()

        lay.addWidget(self._linha_feedback("Clareza das explicações", self.combo_clareza))
        lay.addWidget(self._linha_feedback("Facilidade para navegar entre módulos e aulas", self.combo_navegacao))
        lay.addWidget(self._linha_feedback("Utilidade do conteúdo para aprender o SEI", self.combo_utilidade))
        lay.addWidget(self._linha_feedback("Confiança para utilizar o SEI após o treinamento", self.combo_confianca))
        lay.addWidget(self._linha_feedback("Utilidade das imagens de referência", self.combo_imagens))

        lbl_coment = QLabel("Comentário ou sugestão (opcional)")
        lbl_coment.setObjectName("tituloCartao")
        self.comentario = QPlainTextEdit()
        self.comentario.setPlaceholderText("Ex.: qual aula foi mais útil, o que ficou difícil ou o que pode melhorar...")
        self.comentario.setMaximumHeight(120)
        lay.addWidget(lbl_coment)
        lay.addWidget(self.comentario)

        botao = QPushButton("Enviar avaliação da plataforma")
        botao.setObjectName("botaoPrimario")
        botao.clicked.connect(self._salvar_feedback)
        lay.addWidget(botao, alignment=Qt.AlignLeft)
        lay.addStretch()
        return pagina

    def _finalizar_avaliacao(self):
        respostas = []
        for grupo in self.grupos:
            escolhido = grupo.checkedId()
            if escolhido < 0:
                QMessageBox.warning(self, "Avaliação incompleta", "Responda todas as questões antes de finalizar.")
                return
            respostas.append(escolhido)

        acertos = sum(
            1 for resposta, pergunta in zip(respostas, self.perguntas)
            if resposta == pergunta["correta"]
        )
        percentual = self.servico_avaliacao.salvar_resultado(acertos, len(self.perguntas), respostas)
        self.atualizar()
        if self.ao_alterar:
            self.ao_alterar()

        mensagem = f"Você acertou {acertos} de {len(self.perguntas)} questões ({percentual}%)."
        if percentual >= 80:
            mensagem += "\n\nÓtimo resultado. Você demonstrou boa compreensão dos conceitos apresentados."
        elif percentual >= 60:
            mensagem += "\n\nBom começo. Revise as aulas relacionadas às questões que geraram dúvida."
        else:
            mensagem += "\n\nRecomendamos revisar os módulos antes de tentar novamente."
        QMessageBox.information(self, "Resultado", mensagem)

    def _salvar_feedback(self):
        combos = [
            self.combo_clareza, self.combo_navegacao, self.combo_utilidade,
            self.combo_confianca, self.combo_imagens
        ]
        notas = [c.currentData() for c in combos]
        if any(nota == 0 for nota in notas):
            QMessageBox.warning(self, "Feedback incompleto", "Selecione uma nota para todos os critérios.")
            return

        self.servico_avaliacao.salvar_feedback(*notas, self.comentario.toPlainText())
        self.atualizar()
        if self.ao_alterar:
            self.ao_alterar()
        QMessageBox.information(self, "Feedback registrado", "Obrigado. Sua avaliação foi salva neste computador.")
        for combo in combos:
            combo.setCurrentIndex(0)
        self.comentario.clear()

    def atualizar(self):
        resumo = self.servico_avaliacao.resumo()
        self.lbl_tentativas.setText(str(resumo["tentativas"]))
        self.lbl_melhor.setText(f'{resumo["melhor_percentual"]}%')
        self.lbl_ultima.setText(f'{resumo["ultimo_percentual"]}%')
        self.lbl_feedback.setText(str(resumo["feedbacks"]))

from pathlib import Path
import re

from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton,
    QListWidget, QListWidgetItem, QFrame, QTextBrowser,
    QProgressBar, QMessageBox, QScrollArea
)
from PySide6.QtCore import Qt


class TelaCursos(QWidget):
    def __init__(self, servico_cursos, servico_progresso, servico_avaliacao=None, ao_alterar_progresso=None):
        super().__init__()
        self.servico_cursos = servico_cursos
        self.servico_progresso = servico_progresso
        self.servico_avaliacao = servico_avaliacao
        self.ao_alterar_progresso = ao_alterar_progresso

        self.cursos = self.servico_cursos.listar_cursos()
        self.curso_atual = None
        self.aula_atual = None

        self._montar_interface()
        self._carregar_cursos()

    def _montar_interface(self):
        raiz = QHBoxLayout(self)
        raiz.setContentsMargins(28, 26, 28, 26)
        raiz.setSpacing(18)

        # Coluna de cursos
        coluna_cursos = QFrame()
        coluna_cursos.setObjectName("painelLateralInterno")
        layout_cursos = QVBoxLayout(coluna_cursos)
        layout_cursos.setContentsMargins(18, 18, 18, 18)
        layout_cursos.setSpacing(12)

        titulo_cursos = QLabel("Cursos")
        titulo_cursos.setObjectName("tituloSecao")

        subtitulo_cursos = QLabel("Escolha um curso para começar.")
        subtitulo_cursos.setObjectName("textoPequeno")
        subtitulo_cursos.setWordWrap(True)

        self.lista_cursos = QListWidget()
        self.lista_cursos.setObjectName("listaCursos")
        self.lista_cursos.currentRowChanged.connect(self._selecionar_curso)

        layout_cursos.addWidget(titulo_cursos)
        layout_cursos.addWidget(subtitulo_cursos)
        layout_cursos.addWidget(self.lista_cursos)

        # Coluna de aulas
        coluna_aulas = QFrame()
        coluna_aulas.setObjectName("painelLateralInterno")
        layout_aulas = QVBoxLayout(coluna_aulas)
        layout_aulas.setContentsMargins(18, 18, 18, 18)
        layout_aulas.setSpacing(12)

        self.titulo_curso = QLabel("Selecione um curso")
        self.titulo_curso.setObjectName("tituloSecao")
        self.titulo_curso.setWordWrap(True)

        self.descricao_curso = QLabel("")
        self.descricao_curso.setObjectName("textoPequeno")
        self.descricao_curso.setWordWrap(True)

        self.barra_progresso = QProgressBar()
        self.barra_progresso.setRange(0, 100)

        self.lista_aulas = QListWidget()
        self.lista_aulas.setObjectName("listaAulas")
        self.lista_aulas.currentRowChanged.connect(self._selecionar_aula)

        layout_aulas.addWidget(self.titulo_curso)
        layout_aulas.addWidget(self.descricao_curso)
        layout_aulas.addWidget(self.barra_progresso)
        layout_aulas.addWidget(self.lista_aulas)

        # Conteúdo da aula
        area_aula = QFrame()
        area_aula.setObjectName("cartao")
        layout_aula = QVBoxLayout(area_aula)
        layout_aula.setContentsMargins(24, 22, 24, 22)
        layout_aula.setSpacing(14)

        self.titulo_aula = QLabel("Escolha uma aula")
        self.titulo_aula.setObjectName("tituloPagina")
        self.titulo_aula.setWordWrap(True)

        self.resumo_aula = QLabel("O conteúdo aparecerá aqui.")
        self.resumo_aula.setObjectName("subtituloPagina")
        self.resumo_aula.setWordWrap(True)

        self.conteudo_aula = QTextBrowser()
        self.conteudo_aula.setObjectName("conteudoAula")
        self.conteudo_aula.setOpenExternalLinks(False)
        self.conteudo_aula.setHtml("<p>Selecione uma aula para começar.</p>")

        botoes = QHBoxLayout()

        self.botao_concluir = QPushButton("Marcar como concluída")
        self.botao_concluir.setObjectName("botaoPrimario")
        self.botao_concluir.setEnabled(False)
        self.botao_concluir.clicked.connect(self._alternar_conclusao)

        self.botao_proxima = QPushButton("Próxima aula")
        self.botao_proxima.setObjectName("botaoSecundario")
        self.botao_proxima.setEnabled(False)
        self.botao_proxima.clicked.connect(self._ir_para_proxima_aula)

        botoes.addWidget(self.botao_concluir)
        botoes.addWidget(self.botao_proxima)
        botoes.addStretch()

        layout_aula.addWidget(self.titulo_aula)
        layout_aula.addWidget(self.resumo_aula)
        layout_aula.addWidget(self.conteudo_aula, 1)
        layout_aula.addLayout(botoes)

        raiz.addWidget(coluna_cursos, 2)
        raiz.addWidget(coluna_aulas, 3)
        raiz.addWidget(area_aula, 6)

    def _carregar_cursos(self):
        self.lista_cursos.clear()
        for curso in self.cursos:
            concluido = self.servico_progresso.quantidade_concluida(curso.id)
            texto = f"{curso.titulo}\n{concluido}/{len(curso.aulas)} aulas"
            item = QListWidgetItem(texto)
            item.setData(Qt.UserRole, curso.id)
            self.lista_cursos.addItem(item)

        if self.lista_cursos.count() > 0:
            self.lista_cursos.setCurrentRow(0)

    def _selecionar_curso(self, indice):
        if indice < 0 or indice >= len(self.cursos):
            return

        self.curso_atual = self.cursos[indice]
        self.aula_atual = None

        self.titulo_curso.setText(self.curso_atual.titulo)
        self.descricao_curso.setText(
            f"{self.curso_atual.nivel} • {self.curso_atual.descricao}"
        )

        self._carregar_aulas()
        self._atualizar_progresso_curso()

        if self.lista_aulas.count() > 0:
            self.lista_aulas.setCurrentRow(0)

    def _carregar_aulas(self):
        self.lista_aulas.clear()

        for aula in self.curso_atual.aulas:
            concluida = self.servico_progresso.aula_concluida(
                self.curso_atual.id, aula.id
            )
            marcador = "✓" if concluida else "○"
            item = QListWidgetItem(
                f"{marcador} {aula.ordem}. {aula.titulo}"
            )
            item.setData(Qt.UserRole, aula.id)
            self.lista_aulas.addItem(item)

    def _selecionar_aula(self, indice):
        if not self.curso_atual:
            return

        if indice < 0 or indice >= len(self.curso_atual.aulas):
            return

        self.aula_atual = self.curso_atual.aulas[indice]

        if self.servico_avaliacao:
            self.servico_avaliacao.registrar_evento("abrir_aula", f"{self.curso_atual.id}:{self.aula_atual.id}")

        self.titulo_aula.setText(self.aula_atual.titulo)
        self.resumo_aula.setText(self.aula_atual.resumo)

        conteudo = self.aula_atual.conteudo
        pasta_imagens = (
            Path(__file__).resolve().parent.parent / "recursos" / "paginas"
        )

        def substituir_imagem(correspondencia):
            nome_arquivo = correspondencia.group(1)
            caminho = pasta_imagens / nome_arquivo

            if not caminho.exists():
                return ""

            endereco = caminho.resolve().as_uri()
            return (
                '<div class="imagem-ref">'
                '<p><b>Referência visual desta etapa</b></p>'
                f'<img src="{endereco}" width="720">'
                '</div>'
            )

        conteudo = re.sub(
            r"\[\[IMAGEM:([^\]]+)\]\]",
            substituir_imagem,
            conteudo
        )

        html = f"""
        <html>
        <head>
        <style>
            body {{
                font-family: 'Segoe UI';
                font-size: 14px;
                color: #243447;
                line-height: 1.55;
            }}
            h2 {{
                font-size: 24px;
                color: #172B4D;
                margin-bottom: 14px;
            }}
            h3 {{
                color: #172B4D;
                margin-top: 22px;
                margin-bottom: 8px;
            }}
            p {{
                margin-top: 7px;
                margin-bottom: 10px;
            }}
            li {{
                margin-bottom: 7px;
            }}
            code {{
                background: #EEF2F7;
                color: #183B73;
                padding: 2px 5px;
            }}
            .destaque {{
                background: #F2F7FF;
                border-left: 4px solid #4C78DD;
                padding: 12px 14px;
                margin-top: 16px;
                margin-bottom: 16px;
            }}
            .tabela {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 8px;
                margin-bottom: 18px;
            }}
            .tabela td {{
                border: 1px solid #D8E0EB;
                padding: 8px;
                vertical-align: top;
            }}
            .tabela .campo {{
                width: 34%;
                background: #F7F9FC;
                color: #233954;
            }}
            .tabela .secao td {{
                background: #EAF1FC;
                color: #183B73;
                font-weight: 700;
            }}
            .imagem-ref {{
                margin-top: 24px;
                padding-top: 12px;
                border-top: 1px solid #E1E6EF;
            }}
        </style>
        </head>
        <body>{conteudo}</body>
        </html>
        """
        self.conteudo_aula.setHtml(html)

        concluida = self.servico_progresso.aula_concluida(
            self.curso_atual.id, self.aula_atual.id
        )
        self._atualizar_botao_conclusao(concluida)

        self.botao_concluir.setEnabled(True)
        self.botao_proxima.setEnabled(
            indice < len(self.curso_atual.aulas) - 1
        )

    def _alternar_conclusao(self):
        if not self.curso_atual or not self.aula_atual:
            return

        concluida = self.servico_progresso.aula_concluida(
            self.curso_atual.id, self.aula_atual.id
        )

        if concluida:
            self.servico_progresso.reabrir_aula(
                self.curso_atual.id, self.aula_atual.id
            )
            nova_situacao = False
        else:
            self.servico_progresso.concluir_aula(
                self.curso_atual.id, self.aula_atual.id
            )
            nova_situacao = True

        indice_aula = self.lista_aulas.currentRow()
        indice_curso = self.lista_cursos.currentRow()

        self._carregar_aulas()
        self.lista_aulas.setCurrentRow(indice_aula)
        self._atualizar_progresso_curso()
        self._atualizar_botao_conclusao(nova_situacao)

        # Atualiza também a contagem no menu de cursos
        concluido = self.servico_progresso.quantidade_concluida(
            self.curso_atual.id
        )
        item_curso = self.lista_cursos.item(indice_curso)
        item_curso.setText(
            f"{self.curso_atual.titulo}\n{concluido}/{len(self.curso_atual.aulas)} aulas"
        )

        if self.ao_alterar_progresso:
            self.ao_alterar_progresso()

        if self.servico_avaliacao:
            evento = "concluir_aula" if nova_situacao else "reabrir_aula"
            self.servico_avaliacao.registrar_evento(evento, f"{self.curso_atual.id}:{self.aula_atual.id}")

        if nova_situacao and concluido == len(self.curso_atual.aulas):
            QMessageBox.information(
                self,
                "Curso concluído",
                f"Parabéns! Você concluiu o curso \"{self.curso_atual.titulo}\"."
            )

    def _atualizar_botao_conclusao(self, concluida):
        if concluida:
            self.botao_concluir.setText("✓ Aula concluída")
        else:
            self.botao_concluir.setText("Marcar como concluída")

    def _atualizar_progresso_curso(self):
        if not self.curso_atual:
            self.barra_progresso.setValue(0)
            return

        total = len(self.curso_atual.aulas)
        concluidas = self.servico_progresso.quantidade_concluida(
            self.curso_atual.id
        )
        percentual = round((concluidas / total) * 100) if total else 0
        self.barra_progresso.setValue(percentual)
        self.barra_progresso.setFormat(
            f"{concluidas}/{total} aulas • {percentual}%"
        )

    def _ir_para_proxima_aula(self):
        atual = self.lista_aulas.currentRow()
        if atual < self.lista_aulas.count() - 1:
            self.lista_aulas.setCurrentRow(atual + 1)

    def atualizar(self):
        indice_curso = self.lista_cursos.currentRow()
        indice_aula = self.lista_aulas.currentRow()

        self._carregar_cursos()

        if indice_curso >= 0 and indice_curso < self.lista_cursos.count():
            self.lista_cursos.setCurrentRow(indice_curso)

        if indice_aula >= 0 and indice_aula < self.lista_aulas.count():
            self.lista_aulas.setCurrentRow(indice_aula)

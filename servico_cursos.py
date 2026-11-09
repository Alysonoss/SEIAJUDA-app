from modelos.aula import Aula
from modelos.curso import Curso


class ServicoCursos:
    def listar_cursos(self):
        return [
            Curso(
                id=1,
                titulo="Primeiros passos no SEI",
                descricao="Entenda a lógica do SEI antes de começar a utilizar o sistema.",
                nivel="Iniciante",
                aulas=[
                    Aula(
                        id=1,
                        titulo="O que é o SEI?",
                        resumo="Conheça o objetivo do sistema e sua função na gestão de processos eletrônicos.",
                        ordem=1,
                        conteudo="""
<h2>O que é o SEI?</h2>
<p>O SEI é um sistema utilizado para criar, organizar, tramitar e acompanhar processos e documentos eletrônicos.</p>

<p>Antes de aprender onde clicar, é importante compreender a lógica do trabalho:</p>

<ul>
    <li>um <b>processo</b> reúne documentos e registros relacionados a um assunto;</li>
    <li>os documentos podem ser produzidos ou incluídos no processo;</li>
    <li>o processo pode tramitar entre unidades;</li>
    <li>cada ação realizada deixa registros de andamento.</li>
</ul>

<div class="destaque">
<b>Objetivo desta aula:</b> entender que o SEI não é apenas um local para armazenar arquivos. Ele organiza o fluxo administrativo.
</div>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="Processos, documentos e tramitação",
                        resumo="Aprenda a diferença entre os principais elementos utilizados no trabalho diário.",
                        ordem=2,
                        conteudo="""
<h2>Processos, documentos e tramitação</h2>

<h3>Processo</h3>
<p>É o conjunto de informações e documentos relacionados a uma determinada atividade administrativa.</p>

<h3>Documento</h3>
<p>É um item que pertence ao processo. Pode representar, por exemplo, uma solicitação, despacho, memorando ou arquivo recebido.</p>

<h3>Tramitação</h3>
<p>É o deslocamento do processo entre unidades responsáveis por diferentes etapas do trabalho.</p>

<div class="destaque">
<b>Exemplo:</b> uma solicitação pode começar em uma unidade, seguir para análise em outra e depois retornar para conclusão.
</div>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Unidades e usuários",
                        resumo="Veja como pessoas e setores participam dos fluxos administrativos.",
                        ordem=3,
                        conteudo="""
<h2>Unidades e usuários</h2>
<p>No SEI, os usuários atuam dentro de unidades. Uma unidade pode representar um setor, secretaria, departamento ou outro agrupamento administrativo.</p>

<p>É importante saber em qual unidade você está trabalhando antes de executar uma tarefa, porque determinadas ações e processos podem estar disponíveis apenas para unidades específicas.</p>

<ul>
    <li><b>Usuário:</b> pessoa que utiliza o sistema;</li>
    <li><b>Unidade:</b> setor no qual o usuário está atuando;</li>
    <li><b>Permissão:</b> define quais ações podem ser realizadas.</li>
</ul>
"""
                    ),
                    Aula(
                        id=4,
                        titulo="Boas práticas iniciais",
                        resumo="Evite erros comuns antes de começar a trabalhar com processos reais.",
                        ordem=4,
                        conteudo="""
<h2>Boas práticas iniciais</h2>
<ul>
    <li>Confirme se está trabalhando na unidade correta.</li>
    <li>Leia o assunto do processo antes de realizar qualquer ação.</li>
    <li>Evite duplicar processos sem necessidade.</li>
    <li>Confira o destino antes de realizar uma tramitação.</li>
    <li>Use descrições claras e padronizadas.</li>
</ul>

<div class="destaque">
O objetivo do SEI Guia é ensinar primeiro em um ambiente seguro e depois levar esse conhecimento para o sistema real.
</div>
"""
                    ),
                ]
            ),
            Curso(
                id=2,
                titulo="Trabalhando com processos",
                descricao="Aprenda a lógica de criação, organização, envio e conclusão de processos.",
                nivel="Básico",
                aulas=[
                    Aula(
                        id=1,
                        titulo="Antes de criar um processo",
                        resumo="Saiba o que conferir antes de iniciar um novo processo.",
                        ordem=1,
                        conteudo="""
<h2>Antes de criar um processo</h2>
<p>Antes de iniciar um processo, identifique:</p>
<ul>
    <li>qual é o assunto;</li>
    <li>qual tipo de processo deve ser utilizado;</li>
    <li>quem são os interessados;</li>
    <li>qual unidade será responsável pela primeira etapa.</li>
</ul>
<p>Uma boa classificação no início facilita todo o restante do fluxo.</p>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="Organizando um processo",
                        resumo="Entenda como manter documentos e informações organizados.",
                        ordem=2,
                        conteudo="""
<h2>Organizando um processo</h2>
<p>Um processo bem organizado deve permitir que outra pessoa compreenda rapidamente o que aconteceu.</p>

<p>Ao incluir documentos, procure seguir uma ordem lógica e utilizar descrições que façam sentido para quem continuará o trabalho.</p>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Enviando para outra unidade",
                        resumo="Entenda o que acontece quando um processo precisa seguir para outro setor.",
                        ordem=3,
                        conteudo="""
<h2>Enviando para outra unidade</h2>
<p>A tramitação é utilizada quando outra unidade precisa analisar ou executar uma etapa do processo.</p>

<p>Antes do envio:</p>
<ul>
    <li>confirme se a etapa atual foi concluída;</li>
    <li>confira a unidade de destino;</li>
    <li>verifique se todos os documentos necessários estão presentes.</li>
</ul>
"""
                    ),
                    Aula(
                        id=4,
                        titulo="Concluindo uma etapa",
                        resumo="Aprenda quando uma unidade deve finalizar sua atuação em um processo.",
                        ordem=4,
                        conteudo="""
<h2>Concluindo uma etapa</h2>
<p>Quando a unidade termina sua participação no processo, a etapa pode ser concluída conforme o procedimento administrativo adotado pelo órgão.</p>

<div class="destaque">
Concluir uma etapa não significa necessariamente apagar ou encerrar definitivamente todo o processo.
</div>
"""
                    ),
                ]
            ),
            Curso(
                id=3,
                titulo="Documentos no SEI",
                descricao="Conheça conceitos importantes sobre documentos eletrônicos e organização.",
                nivel="Básico",
                aulas=[
                    Aula(
                        id=1,
                        titulo="Documento interno e documento externo",
                        resumo="Entenda a diferença conceitual entre documentos produzidos e recebidos.",
                        ordem=1,
                        conteudo="""
<h2>Documento interno e documento externo</h2>
<p>De forma geral, documentos podem ser produzidos dentro do próprio ambiente eletrônico ou recebidos de fontes externas.</p>

<p>O mais importante para o usuário é compreender a origem do documento e manter sua identificação correta.</p>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="Nomeando e identificando documentos",
                        resumo="Veja por que uma boa identificação reduz erros e retrabalho.",
                        ordem=2,
                        conteudo="""
<h2>Nomeando e identificando documentos</h2>
<p>Descrições claras ajudam todos os participantes do processo.</p>

<p>Evite nomes vagos como:</p>
<ul>
    <li>arquivo1;</li>
    <li>documento novo;</li>
    <li>scan;</li>
</ul>

<p>Prefira descrições relacionadas ao conteúdo e ao objetivo do documento.</p>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Níveis de acesso",
                        resumo="Conheça o conceito de acesso público, restrito e sigiloso.",
                        ordem=3,
                        conteudo="""
<h2>Níveis de acesso</h2>
<p>Processos e documentos podem possuir diferentes níveis de acesso conforme regras do órgão.</p>

<ul>
    <li><b>Público:</b> conteúdo sem restrição específica de acesso;</li>
    <li><b>Restrito:</b> acesso limitado conforme regra ou hipótese aplicável;</li>
    <li><b>Sigiloso:</b> acesso sujeito a controles mais rigorosos.</li>
</ul>

<div class="destaque">
A classificação correta depende das normas e procedimentos administrativos do órgão. O aplicativo de treinamento não deve substituir essas regras.
</div>
"""
                    ),
                ]
            ),
        ]

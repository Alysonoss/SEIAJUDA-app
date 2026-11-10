from modelos.aula import Aula
from modelos.curso import Curso


class ServicoCursos:
    def listar_cursos(self):
        """
        Formação completa: 60 minutos.
        Os cursos abaixo funcionam como módulos separados.
        """
        return [
            Curso(
                id=1,
                titulo="1. Fundamentos do SEI",
                descricao="Entenda o propósito do SEI e a lógica de processos eletrônicos antes de começar a operar.",
                nivel="Iniciante",
                aulas=[
                    Aula(
                        id=1,
                        titulo="O que é o SEI e por que ele existe?",
                        resumo="Conheça a finalidade do sistema e a mudança do processo em papel para o processo eletrônico.",
                        ordem=1,
                        duracao_minutos=3,
                        conteudo="""
<h2>O que é o SEI e por que ele existe?</h2>

<p>O Sistema Eletrônico de Informações (SEI) organiza processos e documentos administrativos em meio eletrônico.</p>

<p>Em vez de depender de pastas físicas, cópias impressas e deslocamentos de papel entre setores, o trabalho passa a ser registrado e acompanhado digitalmente.</p>

<h3>O que muda na prática?</h3>
<ul>
    <li>processos ficam organizados em um ambiente eletrônico;</li>
    <li>documentos passam a fazer parte de uma sequência lógica;</li>
    <li>as unidades conseguem acompanhar o andamento do trabalho;</li>
    <li>as ações realizadas deixam registros;</li>
    <li>o fluxo administrativo pode ser padronizado.</li>
</ul>

<div class="destaque">
<b>Ideia principal:</b> o SEI não é apenas um repositório de arquivos. Ele representa o fluxo administrativo em formato digital.
</div>

<h3>Antes de avançar</h3>
<p>Pense em um processo em papel que circula por vários setores. No SEI, o objetivo é que esse percurso seja realizado de forma eletrônica, com rastreabilidade e organização.</p>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="Processo eletrônico: a estrutura básica",
                        resumo="Aprenda como processo, documentos, interessados e andamentos se relacionam.",
                        ordem=2,
                        duracao_minutos=4,
                        conteudo="""
<h2>Processo eletrônico: a estrutura básica</h2>

<p>Um processo eletrônico reúne informações e documentos relacionados a um mesmo assunto administrativo.</p>

<h3>Elementos principais</h3>
<ul>
    <li><b>Processo:</b> conjunto que reúne o assunto e seus documentos.</li>
    <li><b>Documento:</b> registro que integra o processo.</li>
    <li><b>Interessado:</b> pessoa ou entidade relacionada ao processo.</li>
    <li><b>Andamento:</b> registro de uma ação ou movimentação realizada.</li>
    <li><b>Unidade:</b> setor que participa do fluxo de trabalho.</li>
</ul>

<h3>Exemplo simples</h3>
<p>Uma solicitação de aquisição pode gerar um processo. Dentro dele podem existir a solicitação inicial, pesquisas de preço, despachos e autorizações.</p>

<p>O processo permanece sendo o mesmo, enquanto novos documentos e novos andamentos são adicionados durante sua tramitação.</p>

<div class="destaque">
<b>Regra mental:</b> processo é o conjunto; documento é uma parte desse conjunto.
</div>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Rastreabilidade e responsabilidade",
                        resumo="Entenda por que cada ação precisa estar vinculada ao fluxo e à unidade correta.",
                        ordem=3,
                        duracao_minutos=3,
                        conteudo="""
<h2>Rastreabilidade e responsabilidade</h2>

<p>Uma das vantagens do processo eletrônico é permitir que o histórico seja acompanhado com maior clareza.</p>

<p>Por isso, ao utilizar o SEI, o usuário precisa ter atenção a três perguntas:</p>

<ol>
    <li>Em qual unidade estou trabalhando?</li>
    <li>Qual processo estou tratando?</li>
    <li>Qual é a próxima ação prevista no fluxo?</li>
</ol>

<p>Essas perguntas ajudam a reduzir erros como tramitação para o setor incorreto, inclusão de documento no processo errado ou conclusão antecipada de uma etapa.</p>

<div class="destaque">
<b>Boa prática:</b> antes de executar uma ação, confirme contexto, processo e destino.
</div>
"""
                    ),
                ]
            ),
            Curso(
                id=2,
                titulo="2. Usuários, unidades e organização do trabalho",
                descricao="Compreenda como pessoas e setores participam do processo eletrônico.",
                nivel="Iniciante",
                aulas=[
                    Aula(
                        id=1,
                        titulo="O papel das unidades",
                        resumo="Entenda por que a unidade representa o setor responsável por uma etapa do processo.",
                        ordem=1,
                        duracao_minutos=4,
                        conteudo="""
<h2>O papel das unidades</h2>

<p>No SEI, o trabalho ocorre dentro de unidades. Uma unidade normalmente representa um setor, secretaria, departamento ou área administrativa.</p>

<p>O mesmo usuário pode, dependendo das permissões do órgão, atuar em mais de uma unidade. Por isso, é importante saber em qual contexto está operando.</p>

<h3>Por que isso é importante?</h3>
<ul>
    <li>determinados processos podem estar disponíveis em uma unidade e não em outra;</li>
    <li>permissões podem variar;</li>
    <li>a tramitação ocorre entre unidades;</li>
    <li>a responsabilidade administrativa depende do setor que está atuando.</li>
</ul>

<div class="destaque">
Antes de começar uma tarefa, confirme a unidade em que você está trabalhando.
</div>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="Usuários e permissões",
                        resumo="Entenda a diferença entre usuário, acesso e permissão.",
                        ordem=2,
                        duracao_minutos=3,
                        conteudo="""
<h2>Usuários e permissões</h2>

<p>O usuário representa a pessoa que acessa o sistema. As ações que ela pode realizar dependem das permissões atribuídas pelo órgão.</p>

<h3>Três conceitos diferentes</h3>
<ul>
    <li><b>Usuário:</b> quem utiliza o sistema.</li>
    <li><b>Unidade:</b> onde o usuário está atuando.</li>
    <li><b>Permissão:</b> o que aquele usuário pode fazer naquele contexto.</li>
</ul>

<p>Nem todo usuário precisa ter acesso a todas as funções. Essa separação ajuda a manter organização e segurança.</p>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Padronização do trabalho",
                        resumo="Veja como procedimentos padronizados reduzem dúvidas e retrabalho.",
                        ordem=3,
                        duracao_minutos=3,
                        conteudo="""
<h2>Padronização do trabalho</h2>

<p>Usar o SEI corretamente não depende apenas de conhecer os botões. Também é necessário saber qual procedimento administrativo deve ser seguido.</p>

<p>Quando duas pessoas executam a mesma atividade de maneiras completamente diferentes, surgem problemas como:</p>

<ul>
    <li>nomes inconsistentes;</li>
    <li>documentos em ordem inadequada;</li>
    <li>tramitações desnecessárias;</li>
    <li>dificuldade para localizar informações;</li>
    <li>retrabalho.</li>
</ul>

<div class="destaque">
O objetivo do SEI Guia é ensinar tanto a lógica do sistema quanto a lógica do fluxo administrativo.
</div>
"""
                    ),
                ]
            ),
            Curso(
                id=3,
                titulo="3. Processos no SEI",
                descricao="Aprenda a lógica de criação, identificação, acompanhamento e conclusão de processos.",
                nivel="Básico",
                aulas=[
                    Aula(
                        id=1,
                        titulo="Antes de iniciar um processo",
                        resumo="Saiba quais informações devem ser conhecidas antes da criação.",
                        ordem=1,
                        duracao_minutos=4,
                        conteudo="""
<h2>Antes de iniciar um processo</h2>

<p>A criação de um processo deve começar pela compreensão do que está sendo solicitado.</p>

<h3>Antes de criar, identifique:</h3>
<ul>
    <li>o assunto do processo;</li>
    <li>o tipo de processo adequado;</li>
    <li>os interessados;</li>
    <li>a unidade responsável;</li>
    <li>quais documentos iniciais serão necessários.</li>
</ul>

<p>Começar com uma classificação correta evita correções posteriores e facilita a busca das informações.</p>

<div class="destaque">
<b>Evite:</b> criar um novo processo apenas porque não encontrou o processo existente. Primeiro confirme se ele realmente não existe.
</div>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="Identificação e acompanhamento",
                        resumo="Aprenda o que observar para acompanhar corretamente um processo.",
                        ordem=2,
                        duracao_minutos=4,
                        conteudo="""
<h2>Identificação e acompanhamento</h2>

<p>O número do processo funciona como uma referência essencial para acompanhamento e localização.</p>

<p>Ao analisar um processo, observe:</p>
<ul>
    <li>número;</li>
    <li>tipo;</li>
    <li>especificação ou assunto;</li>
    <li>unidade responsável;</li>
    <li>últimos andamentos;</li>
    <li>documentos existentes.</li>
</ul>

<h3>Por que consultar os andamentos?</h3>
<p>Porque eles ajudam a entender o que já aconteceu e o que ainda precisa ser feito.</p>

<div class="destaque">
Antes de executar uma nova ação, leia o histórico recente do processo.
</div>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Conclusão e reabertura",
                        resumo="Entenda a diferença entre concluir a atuação de uma unidade e eliminar um processo.",
                        ordem=3,
                        duracao_minutos=4,
                        conteudo="""
<h2>Conclusão e reabertura</h2>

<p>A conclusão é utilizada quando determinada unidade encerrou sua participação naquele momento do fluxo.</p>

<p>Isso não deve ser confundido com excluir o processo.</p>

<h3>Exemplo</h3>
<p>Uma unidade recebe o processo, realiza uma análise, inclui o documento necessário e finaliza sua etapa. Dependendo do procedimento, o processo pode continuar em outra unidade ou permanecer concluído naquela unidade.</p>

<p>Se uma nova necessidade surgir, o processo pode voltar a exigir atuação.</p>

<div class="destaque">
<b>Boa prática:</b> conclua uma etapa somente quando não houver mais ação pendente para aquela unidade.
</div>
"""
                    ),
                ]
            ),
            Curso(
                id=4,
                titulo="4. Documentos no SEI",
                descricao="Entenda documentos internos, externos, organização e níveis de acesso.",
                nivel="Básico",
                aulas=[
                    Aula(
                        id=1,
                        titulo="Documento interno e externo",
                        resumo="Compreenda a diferença entre documentos produzidos e recebidos.",
                        ordem=1,
                        duracao_minutos=4,
                        conteudo="""
<h2>Documento interno e externo</h2>

<p>Um processo pode reunir documentos produzidos no próprio ambiente e documentos recebidos de fontes externas.</p>

<h3>Documento produzido internamente</h3>
<p>É criado como parte da atividade administrativa do órgão.</p>

<h3>Documento recebido externamente</h3>
<p>É originado fora do fluxo interno e depois incorporado ao processo.</p>

<p>A distinção é importante porque cada tipo pode exigir informações diferentes durante o registro.</p>

<div class="destaque">
O objetivo não é apenas anexar arquivos. É registrar corretamente o que cada documento representa.
</div>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="Organização e identificação",
                        resumo="Aprenda a usar descrições claras e manter a sequência documental compreensível.",
                        ordem=2,
                        duracao_minutos=4,
                        conteudo="""
<h2>Organização e identificação</h2>

<p>Um processo precisa ser compreensível para quem o recebe depois.</p>

<h3>Evite descrições vagas</h3>
<ul>
    <li>arquivo;</li>
    <li>scan;</li>
    <li>documento novo;</li>
    <li>anexo 1 sem contexto.</li>
</ul>

<h3>Prefira</h3>
<ul>
    <li>descrições relacionadas ao conteúdo;</li>
    <li>nomes consistentes;</li>
    <li>ordem lógica;</li>
    <li>informações suficientes para identificação.</li>
</ul>

<div class="destaque">
Pergunte: outra pessoa entenderia o conteúdo apenas olhando a organização do processo?
</div>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Níveis de acesso",
                        resumo="Conheça os conceitos de público, restrito e sigiloso.",
                        ordem=3,
                        duracao_minutos=4,
                        conteudo="""
<h2>Níveis de acesso</h2>

<p>Processos e documentos podem possuir diferentes níveis de acesso conforme as regras aplicáveis no órgão.</p>

<ul>
    <li><b>Público:</b> sem restrição específica de acesso.</li>
    <li><b>Restrito:</b> acesso limitado de acordo com a regra aplicável.</li>
    <li><b>Sigiloso:</b> exige controles de acesso mais rigorosos.</li>
</ul>

<p>O nível correto deve ser escolhido conforme as normas institucionais. O usuário não deve classificar um conteúdo apenas por preferência pessoal.</p>

<div class="destaque">
<b>Atenção:</b> o SEI Guia ensina o conceito, mas a decisão correta depende das regras do órgão e da hipótese legal aplicável.
</div>
"""
                    ),
                ]
            ),
            Curso(
                id=5,
                titulo="5. Tramitação e fluxo administrativo",
                descricao="Aprenda a movimentar o trabalho entre unidades com clareza e responsabilidade.",
                nivel="Básico",
                aulas=[
                    Aula(
                        id=1,
                        titulo="O que significa tramitar",
                        resumo="Entenda o envio do processo entre unidades.",
                        ordem=1,
                        duracao_minutos=3,
                        conteudo="""
<h2>O que significa tramitar</h2>

<p>Tramitar significa encaminhar o processo dentro do fluxo administrativo para que outra unidade possa executar uma ação.</p>

<p>Uma tramitação deve ter um motivo claro. O processo não deve circular sem necessidade.</p>

<div class="destaque">
Cada envio deve responder à pergunta: por que esta unidade precisa receber este processo agora?
</div>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="Antes de enviar",
                        resumo="Use uma verificação simples para evitar tramitações incorretas.",
                        ordem=2,
                        duracao_minutos=4,
                        conteudo="""
<h2>Antes de enviar</h2>

<p>Antes de encaminhar um processo, faça uma conferência rápida.</p>

<h3>Checklist</h3>
<ul>
    <li>A etapa atual foi realmente concluída?</li>
    <li>Todos os documentos necessários foram incluídos?</li>
    <li>A unidade de destino está correta?</li>
    <li>Existe alguma informação pendente?</li>
    <li>O próximo setor entenderá o que precisa fazer?</li>
</ul>

<p>Uma conferência de poucos segundos pode evitar vários minutos ou horas de retrabalho.</p>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Fluxo padronizado e BPM",
                        resumo="Entenda como o mapeamento de processos ajuda a definir a próxima etapa.",
                        ordem=3,
                        duracao_minutos=3,
                        conteudo="""
<h2>Fluxo padronizado e BPM</h2>

<p>Quando um processo administrativo é mapeado, cada etapa pode ter:</p>

<ul>
    <li>um responsável;</li>
    <li>uma entrada;</li>
    <li>uma atividade;</li>
    <li>uma saída;</li>
    <li>um próximo destino.</li>
</ul>

<p>Esse mapeamento reduz decisões improvisadas durante a execução.</p>

<div class="destaque">
No SEI Guia, os futuros módulos de simulação poderão ensinar o fluxo completo antes que o servidor o execute no SEI real.
</div>
"""
                    ),
                ]
            ),
            Curso(
                id=6,
                titulo="6. Segurança e boas práticas",
                descricao="Finalize a formação aprendendo cuidados essenciais para trabalhar com confiança.",
                nivel="Básico",
                aulas=[
                    Aula(
                        id=1,
                        titulo="Cuidados antes de confirmar uma ação",
                        resumo="Adote uma rotina de conferência antes de registrar ou encaminhar informações.",
                        ordem=1,
                        duracao_minutos=3,
                        conteudo="""
<h2>Cuidados antes de confirmar uma ação</h2>

<p>Em sistemas administrativos, pequenos erros podem gerar grandes efeitos. Por isso, antes de confirmar uma ação:</p>

<ul>
    <li>confira o processo;</li>
    <li>confira a unidade;</li>
    <li>confira o documento;</li>
    <li>confira o destinatário;</li>
    <li>confira o nível de acesso;</li>
    <li>leia novamente o que será registrado.</li>
</ul>

<div class="destaque">
<b>Regra dos 5 segundos:</b> antes da confirmação final, pare e confira os dados principais.
</div>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="Revisão da formação",
                        resumo="Revise os conceitos que formam a base para usar o SEI com segurança.",
                        ordem=2,
                        duracao_minutos=3,
                        conteudo="""
<h2>Revisão da formação</h2>

<p>Ao concluir este curso, você deve compreender:</p>

<ul>
    <li>o que é um processo eletrônico;</li>
    <li>a diferença entre processo e documento;</li>
    <li>o papel das unidades e usuários;</li>
    <li>por que a classificação inicial é importante;</li>
    <li>como a tramitação representa o fluxo administrativo;</li>
    <li>por que níveis de acesso exigem atenção;</li>
    <li>como a padronização reduz erros e retrabalho.</li>
</ul>

<h3>Próxima etapa</h3>
<p>Depois da parte conceitual, o treinamento seguirá para o simulador, onde o usuário poderá praticar tarefas em uma interface de treinamento.</p>

<div class="destaque">
<b>Formação básica concluída:</b> agora o usuário possui a base conceitual necessária para iniciar a prática assistida.
</div>
"""
                    ),
                ]
            ),
        ]

    def duracao_total_minutos(self):
        return sum(curso.duracao_minutos for curso in self.listar_cursos())

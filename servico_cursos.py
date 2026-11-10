from modelos.aula import Aula
from modelos.curso import Curso


class ServicoCursos:
    def listar_cursos(self):
        """
        Formação básica de 60 minutos.

        IMPORTANTE:
        O conteúdo utiliza a terminologia do manual técnico de Web Services do SEI.
        Por isso aparecem nomes como gerarProcedimento, incluirDocumento,
        enviarProcesso e consultarProcedimento.

        O PDF utilizado como referência não é um manual visual da interface do usuário.
        Ele documenta as estruturas e operações do SEI. Assim, o curso explica o que
        cada operação representa no fluxo real do sistema sem inventar nomes de botões
        que não constam no documento.
        """

        return [
            Curso(
                id=1,
                titulo="1. Estrutura do processo no SEI",
                descricao="Aprenda a linguagem usada pelo próprio SEI: procedimento, protocolo, documento, unidade e andamento.",
                nivel="Fundamentos",
                aulas=[
                    Aula(
                        id=1,
                        titulo="Procedimento: como o SEI representa um processo",
                        resumo="Entenda os campos que formam um processo no SEI e como eles aparecem no manual.",
                        ordem=1,
                        duracao_minutos=3,
                        conteudo="""
<h2>Procedimento: como o SEI representa um processo</h2>

<div class="destaque">
<b>Nome usado no manual:</b> <code>Procedimento</code><br>
<b>O que representa para o usuário:</b> o processo administrativo que será criado, consultado, enviado e concluído.
</div>

<p>No manual de integração do SEI, a estrutura utilizada para representar um processo é chamada de <b>Procedimento</b>. É importante aprender esse nome porque várias operações do sistema trabalham diretamente com essa estrutura, como <code>gerarProcedimento</code> e <code>consultarProcedimento</code>.</p>

<h3>Quais informações formam um Procedimento?</h3>

<p>Entre os principais campos documentados estão:</p>

<ul>
    <li><b>IdTipoProcedimento:</b> identifica o tipo de processo cadastrado no SEI.</li>
    <li><b>NumeroProtocolo:</b> número do processo. Se ele não for informado durante a geração, o próprio SEI pode gerar um número automaticamente.</li>
    <li><b>DataAutuacao:</b> data em que o processo é autuado. Se não for informada, o sistema utiliza a data atual.</li>
    <li><b>Especificacao:</b> descrição ou especificação utilizada para caracterizar o processo.</li>
    <li><b>IdTipoPrioridade:</b> permite associar um tipo de prioridade.</li>
    <li><b>Assuntos:</b> conjunto de assuntos usados para classificação do processo.</li>
    <li><b>Interessados:</b> pessoas ou entidades relacionadas ao processo.</li>
    <li><b>Observacao:</b> observação registrada pela unidade.</li>
    <li><b>NivelAcesso:</b> define se o processo é público, restrito ou sigiloso.</li>
    <li><b>IdHipoteseLegal:</b> identifica a hipótese legal quando aplicável.</li>
</ul>

<h3>O que isso significa no trabalho diário?</h3>

<p>Quando um servidor inicia um novo processo, ele não está simplesmente criando uma pasta vazia. O sistema precisa saber <b>que tipo de processo é aquele, qual é sua finalidade, quem está relacionado a ele e qual nível de acesso deve ser aplicado</b>.</p>

<p>É justamente essa organização que permite que o processo seja localizado, tramitado e acompanhado posteriormente.</p>

<h3>Exemplo de raciocínio</h3>

<p>Imagine que a unidade precise iniciar um processo de aquisição. Antes de criá-lo, o servidor deve identificar o tipo adequado, conferir o assunto, definir a especificação e verificar se existem interessados. Depois disso, o SEI gera ou associa o número de protocolo que passará a identificar aquele processo.</p>

<div class="destaque">
<b>Memorize:</b> no manual técnico, “Procedimento” = processo. O número visível para o usuário aparece como <b>ProtocoloProcedimento</b> ou <b>ProcedimentoFormatado</b>, dependendo da operação.
</div>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="Protocolo, tipo de processo e nível de acesso",
                        resumo="Aprenda a identificar corretamente o processo e a diferença entre público, restrito e sigiloso.",
                        ordem=2,
                        duracao_minutos=3,
                        conteudo="""
<h2>Protocolo, tipo de processo e nível de acesso</h2>

<p>Depois que um processo existe no SEI, ele precisa ser identificado de maneira inequívoca. O manual utiliza o campo <b>ProtocoloProcedimento</b> para representar o número visível do processo, com exemplo no formato <code>12.1.000000077-4</code>.</p>

<h3>Tipo de processo</h3>

<p>O campo <b>IdTipoProcedimento</b> representa o tipo de processo cadastrado no SEI. Esse identificador não deve ser tratado como um número qualquer. Ele corresponde a um tipo previamente configurado no sistema.</p>

<p>O manual também documenta a operação <code>listarTiposProcedimento</code>. Ela retorna os tipos de processo permitidos de acordo com o acesso configurado para o serviço. Isso demonstra um princípio importante: <b>o sistema deve trabalhar com tipos efetivamente cadastrados e autorizados</b>.</p>

<h3>Nível de acesso</h3>

<p>A estrutura de Procedimento utiliza os seguintes valores:</p>

<ul>
    <li><b>0 - público:</b> processo sem restrição específica de acesso.</li>
    <li><b>1 - restrito:</b> processo sujeito a restrição de acesso.</li>
    <li><b>2 - sigiloso:</b> processo com tratamento sigiloso.</li>
    <li><b>nulo:</b> o processo pode assumir o nível e a hipótese legal sugeridos pelo tipo de processo cadastrado no SEI.</li>
</ul>

<h3>Por que isso é importante?</h3>

<p>O nível de acesso não deve ser escolhido por conveniência. Ele faz parte da configuração e das regras de tratamento daquele processo. Quando o nível exige hipótese legal, o campo <b>IdHipoteseLegal</b> identifica essa relação.</p>

<h3>Antes de trabalhar com um processo</h3>

<ol>
    <li>Confirme o número do protocolo.</li>
    <li>Confirme o tipo do processo.</li>
    <li>Leia a especificação.</li>
    <li>Verifique o nível de acesso.</li>
    <li>Confira em qual unidade o processo está aberto.</li>
</ol>

<div class="destaque">
O curso utiliza os nomes documentados pelo SEI. Eles ajudam a entender o que existe por trás da interface e evitam tratar “processo” como uma caixa preta.
</div>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Unidades, usuários e permissões",
                        resumo="Entenda como o SEI relaciona unidades, usuários e acesso às operações.",
                        ordem=3,
                        duracao_minutos=4,
                        conteudo="""
<h2>Unidades, usuários e permissões</h2>

<p>Grande parte das operações do SEI exige um <b>IdUnidade</b>. Isso acontece porque o sistema precisa saber em qual unidade a ação está sendo realizada.</p>

<h3>Operação documentada: listarUnidades</h3>

<p>A operação <code>listarUnidades</code> retorna as unidades permitidas para o serviço informado. O manual deixa claro que essa lista respeita as permissões configuradas no SEI.</p>

<p>Por exemplo, se determinado serviço estiver autorizado a gerar processos apenas nas unidades X, Y e Z, são essas unidades que estarão disponíveis para aquela integração.</p>

<h3>Operação documentada: listarUsuarios</h3>

<p>A operação <code>listarUsuarios</code> utiliza a unidade como referência e retorna usuários que possuem o perfil Básico do SEI naquela unidade.</p>

<h3>O que o usuário deve aprender com isso?</h3>

<p>Mesmo quando trabalha pela interface normal do SEI, o servidor precisa ter consciência de que:</p>

<ul>
    <li>ações são executadas em um contexto de unidade;</li>
    <li>nem toda unidade possui as mesmas permissões;</li>
    <li>nem todo usuário pode realizar todas as operações;</li>
    <li>processos podem estar abertos em uma ou mais unidades;</li>
    <li>a escolha da unidade de destino interfere diretamente na tramitação.</li>
</ul>

<h3>Checklist rápido</h3>

<p>Antes de iniciar uma tarefa, confirme:</p>

<ol>
    <li>Estou na unidade correta?</li>
    <li>Esse processo está disponível para minha unidade?</li>
    <li>Tenho permissão para a ação necessária?</li>
    <li>A próxima etapa será executada por esta unidade ou por outra?</li>
</ol>

<div class="destaque">
<b>Regra de segurança operacional:</b> unidade errada + processo correto ainda pode resultar em uma ação errada.
</div>
"""
                    ),
                ]
            ),

            Curso(
                id=2,
                titulo="2. Criando processos: gerarProcedimento",
                descricao="Veja como o SEI estrutura a criação de um processo e quais dados entram nessa operação.",
                nivel="Operações",
                aulas=[
                    Aula(
                        id=1,
                        titulo="gerarProcedimento: criação do processo",
                        resumo="Aprenda o nome técnico da operação que gera um novo processo no SEI.",
                        ordem=1,
                        duracao_minutos=3,
                        conteudo="""
<h2>gerarProcedimento: criação do processo</h2>

<div class="destaque">
<b>Nome exato no manual:</b> <code>gerarProcedimento</code><br>
<b>Função:</b> gerar um novo processo no SEI.
</div>

<p>A operação <code>gerarProcedimento</code> recebe os dados necessários para criar o processo e também pode executar algumas ações complementares na mesma chamada.</p>

<h3>Informações básicas da operação</h3>

<ul>
    <li><b>SiglaSistema:</b> identifica o sistema cadastrado no SEI.</li>
    <li><b>IdentificacaoServico:</b> identifica o serviço autorizado.</li>
    <li><b>IdUnidade:</b> identifica a unidade que está gerando o processo.</li>
    <li><b>Procedimento:</b> contém os dados do processo que será criado.</li>
    <li><b>Documentos:</b> permite gerar documentos junto com o processo.</li>
    <li><b>ProcedimentosRelacionados:</b> permite relacionar processos automaticamente.</li>
    <li><b>UnidadesEnvio:</b> permite informar unidades para as quais o processo será enviado após a geração.</li>
</ul>

<h3>O que acontece ao final?</h3>

<p>Quando a operação é concluída, o SEI retorna uma estrutura chamada <b>RetornoGeracaoProcedimento</b>. Entre as informações relacionadas a esse retorno estão o identificador interno, o número formatado do processo e o link de acesso.</p>

<h3>Fluxo mental do servidor</h3>

<p>Mesmo que o servidor não veja o nome <code>gerarProcedimento</code> na tela, a ação de iniciar um processo segue esta lógica:</p>

<ol>
    <li>selecionar a unidade responsável;</li>
    <li>definir o tipo do processo;</li>
    <li>preencher a especificação e demais dados;</li>
    <li>definir interessados e assuntos quando necessário;</li>
    <li>definir o nível de acesso;</li>
    <li>confirmar a geração;</li>
    <li>passar a trabalhar com o número de protocolo criado.</li>
</ol>

<div class="destaque">
O manual utilizado pelo curso descreve a operação técnica, e não os nomes dos botões da interface visual. Por isso o treinamento ensina o fluxo real sem inventar cliques que não aparecem na documentação.
</div>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="Dados necessários para gerar um processo",
                        resumo="Aprofunde os campos de Procedimento usados durante a criação.",
                        ordem=2,
                        duracao_minutos=3,
                        conteudo="""
<h2>Dados necessários para gerar um processo</h2>

<p>A qualidade do processo começa no momento de sua criação. A estrutura <b>Procedimento</b> mostra quais informações o SEI precisa manipular.</p>

<h3>1. Tipo de processo</h3>

<p><b>IdTipoProcedimento</b> identifica o tipo cadastrado. O servidor deve selecionar o tipo correto porque ele influencia classificação, permissões e comportamento posterior.</p>

<h3>2. Número de protocolo</h3>

<p><b>NumeroProtocolo</b> pode ser informado ou gerado automaticamente pelo SEI quando não é enviado.</p>

<h3>3. Data de autuação</h3>

<p><b>DataAutuacao</b> corresponde à data de autuação. Quando não informada na geração, o SEI utiliza a data atual.</p>

<h3>4. Especificação</h3>

<p><b>Especificacao</b> descreve o processo. Uma especificação clara facilita a identificação do assunto durante consultas e tramitações.</p>

<h3>5. Assuntos</h3>

<p>A estrutura permite informar assuntos adicionais. Se o tipo de processo já possuir assuntos sugeridos, eles podem ser utilizados. Quando o tipo não possui assunto sugerido, o manual indica que pode ser necessário informar pelo menos um assunto.</p>

<h3>6. Interessados</h3>

<p>O SEI trabalha com um conjunto de interessados. A identificação pode utilizar dados como IdContato, CPF, CNPJ, sigla e nome, seguindo a lógica documentada pelo sistema.</p>

<h3>7. Nível de acesso</h3>

<p>O nível pode ser público, restrito ou sigiloso. Se for deixado nulo, o comportamento pode seguir o nível sugerido pelo tipo cadastrado.</p>

<div class="destaque">
<b>Exercício mental:</b> antes de confirmar um novo processo, tente explicar em uma frase o que ele é, quem está relacionado a ele e por que aquele tipo foi escolhido.
</div>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Relacionamento, envio e prazo durante a geração",
                        resumo="Veja recursos adicionais que podem acompanhar a criação do processo.",
                        ordem=3,
                        duracao_minutos=4,
                        conteudo="""
<h2>Relacionamento, envio e prazo durante a geração</h2>

<p>A operação <code>gerarProcedimento</code> não está limitada a criar um processo vazio. O manual documenta vários recursos complementares.</p>

<h3>ProcedimentosRelacionados</h3>

<p>É possível informar identificadores de outros processos que devem ser relacionados automaticamente ao novo processo.</p>

<h3>UnidadesEnvio</h3>

<p>Também é possível informar unidades para envio após a geração. O manual explica que o processo ficará aberto na unidade geradora e nas unidades indicadas nesse parâmetro.</p>

<h3>SinManterAbertoUnidade</h3>

<p>Esse sinalizador determina se o processo deve permanecer aberto na unidade de origem. No contexto de <code>gerarProcedimento</code>, o valor padrão documentado é S.</p>

<h3>Notificação</h3>

<p><b>SinEnviarEmailNotificacao</b> indica se deve ser enviado um aviso por e-mail às unidades destinatárias. O valor padrão documentado é N.</p>

<h3>Retorno Programado</h3>

<p>A operação aceita:</p>

<ul>
    <li><b>DataRetornoProgramado;</b></li>
    <li><b>DiasRetornoProgramado;</b></li>
    <li><b>SinDiasUteisRetornoProgramado.</b></li>
</ul>

<p>Esses campos permitem representar uma necessidade de retorno em data ou prazo.</p>

<h3>Marcadores e Controle de Prazo</h3>

<p>Também aparecem parâmetros para marcador e controle de prazo, como <b>IdMarcador</b>, <b>TextoMarcador</b>, <b>DataControlePrazo</b> e <b>DiasControlePrazo</b>.</p>

<div class="destaque">
Essa aula mostra por que um fluxo bem mapeado é importante: o SEI possui mecanismos para relacionar, encaminhar, marcar e controlar prazos. O procedimento administrativo precisa dizer quando usar cada um deles.
</div>
"""
                    ),
                ]
            ),

            Curso(
                id=3,
                titulo="3. Documentos: incluirDocumento e consultarDocumento",
                descricao="Aprenda como o SEI diferencia documentos gerados e recebidos e como eles são incluídos em processos.",
                nivel="Operações",
                aulas=[
                    Aula(
                        id=1,
                        titulo="Estrutura Documento: gerado ou recebido",
                        resumo="Conheça os campos usados pelo SEI para representar um documento.",
                        ordem=1,
                        duracao_minutos=3,
                        conteudo="""
<h2>Estrutura Documento: gerado ou recebido</h2>

<div class="destaque">
<b>Nome usado no manual:</b> <code>Documento</code>
</div>

<p>O manual diferencia dois tipos principais de documento:</p>

<ul>
    <li><b>G - documento gerado:</b> documento produzido no ambiente do SEI.</li>
    <li><b>R - documento recebido:</b> documento externo incorporado ao processo.</li>
</ul>

<h3>Ligação com o processo</h3>

<p>Um documento precisa estar associado a um processo. O manual permite essa associação por <b>IdProcedimento</b> ou pelo <b>ProtocoloProcedimento</b>.</p>

<h3>Tipo do documento</h3>

<p><b>IdSerie</b> identifica o tipo de documento cadastrado no SEI.</p>

<h3>Campos importantes</h3>

<ul>
    <li><b>Numero:</b> número do documento.</li>
    <li><b>NomeArvore:</b> nome complementar exibido na árvore do processo.</li>
    <li><b>Data:</b> obrigatória para documentos externos e nula para documentos gerados, conforme a estrutura documentada.</li>
    <li><b>Descricao:</b> descrição usada para documentos gerados.</li>
    <li><b>IdTipoConferencia:</b> tipo de conferência associado ao documento externo.</li>
    <li><b>Remetente:</b> obrigatório para documentos externos.</li>
    <li><b>Interessados:</b> conjunto de interessados relacionados.</li>
</ul>

<h3>Por que separar gerado e recebido?</h3>

<p>Porque o SEI trata de maneira diferente aquilo que foi produzido internamente e aquilo que chegou de fora. Essa origem influencia campos obrigatórios e a forma como o documento é registrado.</p>

<div class="destaque">
<b>Memorize:</b> processo contém documentos. Documento não deve ser tratado como um arquivo solto sem contexto.
</div>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="incluirDocumento: inserindo no processo",
                        resumo="Veja a operação documentada para incluir um documento no processo.",
                        ordem=2,
                        duracao_minutos=3,
                        conteudo="""
<h2>incluirDocumento: inserindo no processo</h2>

<div class="destaque">
<b>Nome exato no manual:</b> <code>incluirDocumento</code>
</div>

<p>A operação <code>incluirDocumento</code> recebe quatro grupos de informação principais:</p>

<ul>
    <li><b>SiglaSistema;</b></li>
    <li><b>IdentificacaoServico;</b></li>
    <li><b>IdUnidade;</b></li>
    <li><b>Documento.</b></li>
</ul>

<p>O campo <b>Documento</b> contém os dados da estrutura estudada na aula anterior.</p>

<h3>O que o SEI retorna?</h3>

<p>A saída é uma ocorrência de <b>RetornoInclusaoDocumento</b>. A estrutura de retorno permite identificar o documento criado e trabalhar com seu número visível e link de acesso.</p>

<h3>Fluxo equivalente no uso do sistema</h3>

<ol>
    <li>abrir ou localizar o processo correto;</li>
    <li>definir o tipo de documento;</li>
    <li>informar os dados exigidos para aquele documento;</li>
    <li>indicar se ele é gerado ou recebido;</li>
    <li>preencher os campos específicos;</li>
    <li>confirmar sua inclusão no processo;</li>
    <li>verificar o documento na árvore do processo.</li>
</ol>

<h3>Cuidados</h3>

<ul>
    <li>não inserir um documento no processo errado;</li>
    <li>não utilizar tipo de documento incompatível;</li>
    <li>informar corretamente a origem do documento;</li>
    <li>conferir o nível de acesso;</li>
    <li>usar uma identificação clara na árvore.</li>
</ul>

<div class="destaque">
O manual técnico não documenta os botões visuais usados pelo servidor. Portanto, o curso mantém o nome oficial da operação e ensina a sequência lógica que ela representa.
</div>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="consultarDocumento e informações retornadas",
                        resumo="Aprenda o que pode ser consultado sobre um documento já existente.",
                        ordem=3,
                        duracao_minutos=4,
                        conteudo="""
<h2>consultarDocumento e informações retornadas</h2>

<div class="destaque">
<b>Nome exato no manual:</b> <code>consultarDocumento</code>
</div>

<p>Para consultar um documento, o SEI utiliza o <b>ProtocoloDocumento</b>, isto é, o número visível do documento.</p>

<p>A operação também possui sinalizadores que determinam quais informações adicionais devem ser retornadas.</p>

<h3>Informações opcionais</h3>

<ul>
    <li><b>SinRetornarAndamentoGeracao:</b> andamento de geração.</li>
    <li><b>SinRetornarAssinaturas:</b> assinaturas do documento.</li>
    <li><b>SinRetornarPublicacao:</b> dados de publicação.</li>
    <li><b>SinRetornarCampos:</b> campos de formulário.</li>
    <li><b>SinRetornarBlocos:</b> blocos da unidade que contêm o documento.</li>
</ul>

<p>A saída é uma estrutura <b>RetornoConsultaDocumento</b>.</p>

<h3>Observação importante do manual</h3>

<p>Documentos pertencentes a processos sigilosos não são retornados por essa operação. O manual também recomenda pedir apenas as informações realmente necessárias, porque cada sinalizador acrescenta processamento.</p>

<h3>No treinamento do usuário</h3>

<p>A ideia central é aprender que consultar um documento não significa apenas “abrir um arquivo”. O SEI consegue relacionar ao documento informações como:</p>

<ul>
    <li>processo ao qual pertence;</li>
    <li>nível de acesso;</li>
    <li>unidade elaboradora;</li>
    <li>andamento de geração;</li>
    <li>assinaturas;</li>
    <li>publicação;</li>
    <li>blocos.</li>
</ul>

<div class="destaque">
Quando estiver analisando um processo, observe o documento dentro do contexto do processo, e não isoladamente.
</div>
"""
                    ),
                ]
            ),

            Curso(
                id=4,
                titulo="4. Tramitação: enviarProcesso",
                descricao="Entenda como o SEI envia um processo entre unidades e quais controles podem acompanhar o envio.",
                nivel="Operações",
                aulas=[
                    Aula(
                        id=1,
                        titulo="enviarProcesso: tramitação entre unidades",
                        resumo="Conheça a operação que representa o envio de um processo para outra unidade.",
                        ordem=1,
                        duracao_minutos=3,
                        conteudo="""
<h2>enviarProcesso: tramitação entre unidades</h2>

<div class="destaque">
<b>Nome exato no manual:</b> <code>enviarProcesso</code>
</div>

<p>A tramitação é uma das ações centrais do trabalho no SEI. No manual de Web Services, ela é representada pela operação <code>enviarProcesso</code>.</p>

<h3>Dados principais</h3>

<ul>
    <li><b>IdUnidade:</b> unidade que está realizando o envio.</li>
    <li><b>ProtocoloProcedimento:</b> número do processo.</li>
    <li><b>UnidadesDestino:</b> conjunto de unidades destinatárias.</li>
</ul>

<h3>Manter aberto na origem</h3>

<p><b>SinManterAbertoUnidade</b> define se o processo deve continuar aberto na unidade de origem depois do envio. Para essa operação, o valor padrão documentado é N.</p>

<h3>Remoção de anotação</h3>

<p><b>SinRemoverAnotacao</b> indica se uma anotação deve ser removida durante o envio.</p>

<h3>Notificação</h3>

<p><b>SinEnviarEmailNotificacao</b> indica se as unidades destinatárias devem receber aviso por e-mail.</p>

<h3>Reabertura automática</h3>

<p><b>SinReabrir</b> permite solicitar reabertura automática caso o processo esteja concluído na unidade. O manual informa que, para isso, o serviço também precisa possuir a operação <b>Reabrir Processo</b> liberada.</p>

<div class="destaque">
<b>Antes de enviar:</b> confira processo, unidade de origem, destino e se a sua etapa realmente terminou.
</div>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="Retorno Programado no envio",
                        resumo="Entenda os campos de prazo que podem acompanhar a tramitação.",
                        ordem=2,
                        duracao_minutos=3,
                        conteudo="""
<h2>Retorno Programado no envio</h2>

<p>A operação <code>enviarProcesso</code> pode associar uma expectativa de retorno ao processo.</p>

<h3>Campos documentados</h3>

<ul>
    <li><b>DataRetornoProgramado:</b> define uma data de retorno.</li>
    <li><b>DiasRetornoProgramado:</b> define quantidade de dias.</li>
    <li><b>SinDiasUteisRetornoProgramado:</b> informa se os dias devem ser considerados úteis.</li>
</ul>

<h3>Por que isso importa?</h3>

<p>Em um processo administrativo, o envio não deve significar perda de acompanhamento. Quando o procedimento exige retorno em determinado prazo, o sistema possui mecanismo para registrar essa expectativa.</p>

<h3>Exemplo de fluxo</h3>

<ol>
    <li>A unidade A conclui sua análise.</li>
    <li>O processo precisa seguir para a unidade B.</li>
    <li>A unidade A envia o processo.</li>
    <li>O fluxo prevê retorno depois de determinado período.</li>
    <li>O retorno programado ajuda a controlar essa necessidade.</li>
</ol>

<h3>O que o servidor precisa saber</h3>

<p>O recurso só faz sentido se o fluxo administrativo estiver definido. O prazo não deve ser inserido aleatoriamente. Ele deve refletir a regra ou necessidade do processo.</p>

<div class="destaque">
BPM e SEI se encontram aqui: o processo mapeado define o prazo; o sistema ajuda a controlar o prazo.
</div>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Atribuir, anexar e organizar processos",
                        resumo="Conheça operações complementares que aparecem no manual.",
                        ordem=3,
                        duracao_minutos=4,
                        conteudo="""
<h2>Atribuir, anexar e organizar processos</h2>

<p>Além do envio, o manual documenta outras operações importantes.</p>

<h3>atribuirProcesso</h3>

<p>A operação <code>atribuirProcesso</code> recebe:</p>

<ul>
    <li>unidade;</li>
    <li>protocolo do processo;</li>
    <li>identificador do usuário;</li>
    <li>um sinalizador de reabertura automática.</li>
</ul>

<p>Ela representa a associação do processo a um usuário dentro da unidade.</p>

<h3>anexarProcesso</h3>

<p>A operação <code>anexarProcesso</code> trabalha com:</p>

<ul>
    <li>ProtocoloProcedimentoPrincipal;</li>
    <li>ProtocoloProcedimentoAnexado.</li>
</ul>

<p>Ou seja, existe um processo principal e outro que será anexado a ele.</p>

<h3>Por que aprender isso?</h3>

<p>Porque diferentes ações possuem significados diferentes:</p>

<ul>
    <li><b>Enviar</b> altera a tramitação entre unidades.</li>
    <li><b>Atribuir</b> relaciona o trabalho a um usuário.</li>
    <li><b>Anexar</b> estabelece uma relação específica entre processos.</li>
</ul>

<div class="destaque">
Não trate “enviar”, “atribuir” e “anexar” como sinônimos. Cada operação representa uma mudança diferente no processo.
</div>
"""
                    ),
                ]
            ),

            Curso(
                id=5,
                titulo="5. Consulta e acompanhamento",
                descricao="Aprenda a consultar processos e interpretar andamentos antes de tomar uma decisão.",
                nivel="Acompanhamento",
                aulas=[
                    Aula(
                        id=1,
                        titulo="consultarProcedimento: lendo o processo",
                        resumo="Veja as informações que podem ser retornadas durante a consulta de um processo.",
                        ordem=1,
                        duracao_minutos=3,
                        conteudo="""
<h2>consultarProcedimento: lendo o processo</h2>

<div class="destaque">
<b>Nome exato no manual:</b> <code>consultarProcedimento</code>
</div>

<p>Essa operação consulta um processo a partir do <b>ProtocoloProcedimento</b>.</p>

<h3>O que pode ser solicitado?</h3>

<ul>
    <li><b>Assuntos</b> do processo.</li>
    <li><b>Interessados</b>.</li>
    <li><b>Observações</b> das unidades.</li>
    <li><b>Andamento de geração</b>.</li>
    <li><b>Andamento de conclusão</b>.</li>
    <li><b>Último andamento</b>.</li>
    <li><b>Unidades onde o processo está aberto</b>.</li>
    <li><b>Processos relacionados</b>.</li>
    <li><b>Processos anexados</b>.</li>
</ul>

<h3>Saída da consulta</h3>

<p>O retorno é uma estrutura chamada <b>RetornoConsultaProcedimento</b>.</p>

<p>Ela pode trazer informações como número formatado, especificação, data de autuação, nível de acesso, link de acesso, tipo de procedimento, último andamento, unidades onde o processo está aberto e outros conjuntos relacionados.</p>

<h3>Regra operacional</h3>

<p>Antes de decidir o que fazer com um processo, consulte seu contexto:</p>

<ol>
    <li>qual é a especificação;</li>
    <li>qual foi o último andamento;</li>
    <li>em quais unidades está aberto;</li>
    <li>quais documentos e relações já existem;</li>
    <li>qual é a próxima etapa prevista.</li>
</ol>

<div class="destaque">
O manual informa que processos sigilosos não são retornados por essa operação.
</div>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="listarAndamentos: entendendo o histórico",
                        resumo="Aprenda como o SEI representa acontecimentos e tarefas registrados no processo.",
                        ordem=2,
                        duracao_minutos=3,
                        conteudo="""
<h2>listarAndamentos: entendendo o histórico</h2>

<div class="destaque">
<b>Nome exato no manual:</b> <code>listarAndamentos</code>
</div>

<p>O andamento representa um registro ligado ao histórico do processo.</p>

<p>A operação <code>listarAndamentos</code> utiliza o número do processo e permite filtrar resultados.</p>

<h3>Filtros documentados</h3>

<ul>
    <li><b>Andamentos:</b> filtra identificadores de andamentos.</li>
    <li><b>Tarefas:</b> filtra identificadores de tarefas.</li>
    <li><b>TarefasModulos:</b> filtra tarefas de módulos.</li>
    <li><b>SinRetornarAtributos:</b> define se os atributos associados também serão retornados.</li>
</ul>

<p>O manual exige que pelo menos um dos filtros Andamentos, Tarefas ou TarefasModulos seja informado.</p>

<h3>lancarAndamento</h3>

<p>O manual também documenta <code>lancarAndamento</code>, que registra um andamento e pode utilizar atributos associados.</p>

<p>Para atualização textual de andamento, o documento menciona a tarefa 65 com atributo chamado <b>DESCRICAO</b>.</p>

<h3>Como isso ajuda o servidor?</h3>

<p>O histórico deve ser lido como uma narrativa do processo:</p>

<ul>
    <li>quem executou ações;</li>
    <li>qual unidade participou;</li>
    <li>quando determinada movimentação ocorreu;</li>
    <li>quais tarefas foram registradas.</li>
</ul>

<div class="destaque">
Antes de repetir uma ação, confira o histórico. Muitas falhas de processo acontecem porque alguém age sem observar o que já foi feito.
</div>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Processos sigilosos e retorno de informações",
                        resumo="Entenda limitações documentadas nas operações de consulta.",
                        ordem=3,
                        duracao_minutos=4,
                        conteudo="""
<h2>Processos sigilosos e retorno de informações</h2>

<p>O manual apresenta restrições específicas para consultas.</p>

<h3>consultarProcedimento</h3>

<p>Processos sigilosos não são retornados pela operação.</p>

<h3>consultarDocumento</h3>

<p>Documentos pertencentes a processos sigilosos também não são retornados.</p>

<h3>Solicitar somente o necessário</h3>

<p>Nas operações de consulta, diversos campos são controlados por sinalizadores. O manual recomenda solicitar apenas as informações estritamente necessárias porque cada sinalizador pode exigir processamento adicional.</p>

<h3>O que isso ensina?</h3>

<p>O usuário deve compreender que acesso e visibilidade não dependem apenas do número do processo. O sistema considera regras de acesso, unidade, serviço e nível de classificação.</p>

<h3>Boa prática de treinamento</h3>

<p>Se uma informação não aparece para o usuário, não conclua imediatamente que ela foi apagada ou que o processo não existe. Primeiro considere:</p>

<ul>
    <li>nível de acesso;</li>
    <li>unidade;</li>
    <li>perfil;</li>
    <li>permissões;</li>
    <li>tipo de consulta realizada.</li>
</ul>

<div class="destaque">
Segurança no SEI não é um detalhe separado do processo. Ela faz parte do próprio fluxo de informação.
</div>
"""
                    ),
                ]
            ),

            Curso(
                id=6,
                titulo="6. Conclusão, reabertura e revisão",
                descricao="Finalize a formação entendendo como o SEI encerra e reabre a atuação de uma unidade.",
                nivel="Fechamento",
                aulas=[
                    Aula(
                        id=1,
                        titulo="concluirProcesso: encerrando a atuação da unidade",
                        resumo="Aprenda o significado da operação de conclusão.",
                        ordem=1,
                        duracao_minutos=3,
                        conteudo="""
<h2>concluirProcesso: encerrando a atuação da unidade</h2>

<div class="destaque">
<b>Nome exato no manual:</b> <code>concluirProcesso</code>
</div>

<p>A operação <code>concluirProcesso</code> recebe:</p>

<ul>
    <li><b>SiglaSistema;</b></li>
    <li><b>IdentificacaoServico;</b></li>
    <li><b>IdUnidade:</b> unidade onde o processo está aberto;</li>
    <li><b>ProtocoloProcedimento:</b> número visível do processo.</li>
</ul>

<p>Quando executada com sucesso, a operação retorna verdadeiro.</p>

<h3>O que “concluir” significa?</h3>

<p>Conclusão não deve ser confundida com exclusão. O próprio manual documenta <code>excluirProcesso</code> como uma operação diferente.</p>

<p>Portanto, quando a unidade conclui um processo, o conceito é encerrar sua atuação naquele contexto, e não apagar o histórico administrativo.</p>

<h3>Antes de concluir</h3>

<ol>
    <li>verifique se existem tarefas pendentes;</li>
    <li>confira os documentos necessários;</li>
    <li>leia o último andamento;</li>
    <li>confirme se outra unidade ainda precisa receber o processo;</li>
    <li>confirme se sua unidade realmente terminou a atuação.</li>
</ol>

<div class="destaque">
<b>Pergunta de controle:</b> se o processo desaparecer da lista de trabalho da minha unidade agora, ainda existe alguma ação que eu deveria executar? Se a resposta for sim, ele provavelmente ainda não deve ser concluído.
</div>
"""
                    ),
                    Aula(
                        id=2,
                        titulo="reabrirProcesso: retomando o trabalho",
                        resumo="Veja como um processo concluído pode voltar a exigir atuação.",
                        ordem=2,
                        duracao_minutos=3,
                        conteudo="""
<h2>reabrirProcesso: retomando o trabalho</h2>

<div class="destaque">
<b>Nome exato no manual:</b> <code>reabrirProcesso</code>
</div>

<p>A operação de reabertura utiliza:</p>

<ul>
    <li><b>IdUnidade:</b> unidade por onde o processo tramitou;</li>
    <li><b>ProtocoloProcedimento:</b> número do processo.</li>
</ul>

<p>Quando executada corretamente, a operação retorna verdadeiro.</p>

<h3>Por que reabrir?</h3>

<p>Um processo pode ter sido concluído em uma unidade e, posteriormente, voltar a exigir uma ação. A reabertura permite retomar o trabalho naquele processo.</p>

<h3>Relação com enviarProcesso</h3>

<p>O manual mostra que <code>enviarProcesso</code> possui o sinalizador <b>SinReabrir</b>. Caso o processo esteja concluído na unidade, ele pode solicitar reabertura automática, desde que a operação “Reabrir Processo” também esteja autorizada para o serviço.</p>

<h3>Relação com atribuirProcesso</h3>

<p>A operação <code>atribuirProcesso</code> também possui o sinalizador <b>SinReabrir</b>.</p>

<div class="destaque">
Conclusão e reabertura formam um ciclo controlado. O objetivo é refletir corretamente se a unidade possui ou não trabalho pendente naquele processo.
</div>
"""
                    ),
                    Aula(
                        id=3,
                        titulo="Revisão: o ciclo completo do processo",
                        resumo="Conecte criação, documentos, tramitação, consulta e conclusão em um único fluxo.",
                        ordem=3,
                        duracao_minutos=4,
                        conteudo="""
<h2>Revisão: o ciclo completo do processo</h2>

<p>Agora podemos conectar as principais operações documentadas em uma sequência de trabalho.</p>

<h3>1. Criar</h3>
<p><code>gerarProcedimento</code> gera o processo a partir da estrutura Procedimento.</p>

<h3>2. Incluir documentos</h3>
<p><code>incluirDocumento</code> adiciona um Documento a um processo existente.</p>

<h3>3. Consultar</h3>
<p><code>consultarProcedimento</code> retorna informações do processo. <code>consultarDocumento</code> retorna informações de um documento.</p>

<h3>4. Acompanhar</h3>
<p><code>listarAndamentos</code> permite consultar registros de andamento.</p>

<h3>5. Tramitar</h3>
<p><code>enviarProcesso</code> encaminha o processo para uma ou mais unidades de destino.</p>

<h3>6. Organizar responsabilidades</h3>
<p><code>atribuirProcesso</code> associa o processo a um usuário. <code>anexarProcesso</code> estabelece anexação entre processos.</p>

<h3>7. Concluir</h3>
<p><code>concluirProcesso</code> encerra a atuação da unidade.</p>

<h3>8. Retomar quando necessário</h3>
<p><code>reabrirProcesso</code> permite que a unidade volte a atuar.</p>

<h3>Mapa resumido</h3>

<p><b>gerarProcedimento → incluirDocumento → consultarProcedimento → enviarProcesso → listarAndamentos → concluirProcesso → reabrirProcesso</b></p>

<div class="destaque">
<b>Objetivo da formação:</b> o servidor não precisa decorar nomes técnicos para trabalhar na interface, mas entender esses nomes ajuda a enxergar a lógica real do SEI e facilita a futura criação do simulador.
</div>

<h3>Próxima etapa do SEI Guia</h3>

<p>O próximo módulo do aplicativo poderá transformar esse conhecimento em prática visual: o usuário receberá uma tarefa e deverá executar o fluxo em uma interface simulada antes de trabalhar no ambiente real.</p>
"""
                    ),
                ]
            ),
        ]

    def duracao_total_minutos(self):
        return sum(curso.duracao_minutos for curso in self.listar_cursos())

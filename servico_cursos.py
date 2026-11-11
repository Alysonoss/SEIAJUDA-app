from modelos.aula import Aula
from modelos.curso import Curso


class ServicoCursos:
    def listar_cursos(self):
        return [
            Curso(
                id=1,
                titulo='1. Fundamentos e estrutura do SEI',
                descricao='Conheça os elementos que formam processos, tipos, unidades e usuários.',
                nivel='Fundamentos',
                aulas=[
                    Aula(
                        id=1,
                        titulo='Procedimento: o processo dentro do SEI',
                        resumo='Entenda como o SEI representa um processo e quais informações fazem parte dele.',
                        ordem=1,
                        conteudo='<h2>Procedimento: o processo dentro do SEI</h2>\n<p>No SEI, o processo é representado pela estrutura chamada <b>Procedimento</b>. Ela reúne as informações necessárias para identificar, classificar e acompanhar um processo administrativo.</p>\n<h3>Campos principais</h3>\n<ul>\n<li><b>IdTipoProcedimento:</b> identifica o tipo de processo cadastrado.</li>\n<li><b>NumeroProtocolo:</b> número do processo. Quando não é informado em uma geração, o SEI pode criar um novo número.</li>\n<li><b>DataAutuacao:</b> data em que o processo é autuado.</li>\n<li><b>Especificacao:</b> texto que ajuda a identificar o assunto concreto daquele processo.</li>\n<li><b>IdTipoPrioridade:</b> identifica uma prioridade configurada.</li>\n<li><b>Assuntos:</b> classificação temática do processo.</li>\n<li><b>Interessados:</b> pessoas ou entidades relacionadas ao processo.</li>\n<li><b>Observacao:</b> observação registrada pela unidade.</li>\n<li><b>NivelAcesso:</b> público, restrito ou sigiloso.</li>\n<li><b>IdHipoteseLegal:</b> hipótese legal associada quando aplicável.</li>\n</ul>\n<h3>Como interpretar na prática</h3>\n<p>Ao iniciar um processo, o usuário precisa pensar primeiro no assunto e no tipo correto. A escolha do tipo influencia quais assuntos, níveis de acesso e operações estarão disponíveis.</p>\n<p>Depois da criação, o número do processo passa a ser a referência principal para consultas, tramitações, inclusão de documentos e acompanhamento do histórico.</p>\n<h3>Exemplo de raciocínio</h3>\n<p>Se uma unidade precisa tratar uma solicitação administrativa, ela deve identificar o tipo de processo adequado, preencher uma especificação clara, indicar interessados quando necessário e conferir o nível de acesso antes de concluir a criação.</p>\n<div class="destaque"><b>Importante:</b> Um processo bem criado reduz retrabalho nas etapas seguintes.</div>'
                    ),
                    Aula(
                        id=2,
                        titulo='Protocolo, identificação e tipo de processo',
                        resumo='Aprenda a diferenciar número do processo, identificador interno e tipo de procedimento.',
                        ordem=2,
                        conteudo='<h2>Protocolo, identificação e tipo de processo</h2>\n<p>O SEI usa diferentes identificadores. Para quem opera o sistema, o mais importante é compreender que o número visível do processo não é a mesma coisa que seus identificadores internos.</p>\n<h3>ProtocoloProcedimento</h3>\n<p><b>ProtocoloProcedimento</b> representa o número visível do processo, usado em diversas operações como consulta, envio, conclusão, reabertura, anotação e inclusão em bloco.</p>\n<h3>IdProcedimento</h3>\n<p><b>IdProcedimento</b> é o identificador interno do processo. Algumas operações aceitam o identificador interno; outras utilizam diretamente o número de protocolo.</p>\n<h3>IdTipoProcedimento</h3>\n<p><b>IdTipoProcedimento</b> indica qual tipo de processo está sendo tratado. O tipo não é apenas um título: ele faz parte da configuração do SEI e pode determinar assuntos, permissões e regras de uso.</p>\n<h3>Tipos disponíveis</h3>\n<p>A função <code>listarTiposProcedimento</code> permite obter os tipos de processo autorizados para determinado contexto. Ela também pode aplicar filtros por unidade, série de documento e processo individual.</p>\n<div class="destaque"><b>Importante:</b> Antes de criar ou operar um processo, confirme se o tipo selecionado corresponde ao procedimento administrativo que será executado.</div>'
                    ),
                    Aula(
                        id=3,
                        titulo='Unidades e usuários',
                        resumo='Veja como o SEI relaciona setores, usuários e permissões de trabalho.',
                        ordem=3,
                        conteudo='<h2>Unidades e usuários</h2>\n<p>As operações do SEI frequentemente exigem um <b>IdUnidade</b>. Isso acontece porque uma ação não é executada apenas por uma pessoa, mas dentro do contexto de uma unidade administrativa.</p>\n<h3>listarUnidades</h3>\n<p><code>listarUnidades</code> retorna as unidades disponíveis de acordo com o acesso configurado. Também pode receber filtros relacionados ao tipo de processo ou ao tipo de documento.</p>\n<h3>listarUsuarios</h3>\n<p><code>listarUsuarios</code> retorna usuários vinculados à unidade e permite filtrar um usuário específico. O conjunto retornado considera usuários com perfil Básico na unidade.</p>\n<h3>Por que conferir a unidade</h3>\n<ul>\n<li>um processo pode estar aberto em uma unidade e não em outra;</li>\n<li>as permissões podem variar entre unidades;</li>\n<li>a unidade de origem interfere na tramitação;</li>\n<li>atribuições são realizadas dentro de um contexto de unidade.</li>\n</ul>\n<h3>Rotina recomendada</h3>\n<ol>\n<li>confirme a unidade atual;</li>\n<li>confirme o processo;</li>\n<li>confirme se a unidade possui responsabilidade naquela etapa;</li>\n<li>só então execute a operação necessária.</li>\n</ol>\n<div class="destaque"><b>Importante:</b> Trabalhar no processo correto dentro da unidade errada ainda pode gerar um erro administrativo.</div>'
                    )
                ]
            ),
            Curso(
                id=2,
                titulo='2. Criação de processos',
                descricao='Aprenda a gerar processos e preencher corretamente os dados iniciais.',
                nivel='Operações',
                aulas=[
                    Aula(
                        id=1,
                        titulo='gerarProcedimento: criando um processo',
                        resumo='Conheça a função usada para gerar um novo processo e o que ela recebe.',
                        ordem=1,
                        conteudo='<h2>gerarProcedimento: criando um processo</h2>\n<p>A função <code>gerarProcedimento</code> cria um novo processo no SEI. Ela trabalha com a unidade de origem, os dados do procedimento e informações opcionais que podem automatizar etapas posteriores.</p>\n<h3>Entradas principais</h3>\n<ul>\n<li><b>SiglaSistema:</b> identifica o sistema autorizado.</li>\n<li><b>IdentificacaoServico:</b> identifica o serviço configurado.</li>\n<li><b>IdUnidade:</b> unidade onde o processo será gerado.</li>\n<li><b>Procedimento:</b> dados do processo.</li>\n<li><b>Documentos:</b> documentos que podem ser gerados junto com o processo.</li>\n<li><b>ProcedimentosRelacionados:</b> processos que podem ser relacionados automaticamente.</li>\n<li><b>UnidadesEnvio:</b> unidades para as quais o processo pode ser enviado após a geração.</li>\n</ul>\n<h3>Resultado</h3>\n<p>A operação retorna informações da geração do processo. O número formatado criado passa a ser utilizado como referência nas operações seguintes.</p>\n<h3>Sequência lógica para o usuário</h3>\n<ol>\n<li>definir o tipo;</li>\n<li>preencher os dados do processo;</li>\n<li>verificar assuntos e interessados;</li>\n<li>definir nível de acesso;</li>\n<li>confirmar a unidade responsável;</li>\n<li>criar o processo;</li>\n<li>prosseguir com documentos e tramitação.</li>\n</ol>\n<div class="destaque"><b>Importante:</b> Gerar o processo é o início do fluxo, não o fim da tarefa.</div>'
                    ),
                    Aula(
                        id=2,
                        titulo='Assuntos, interessados e observações',
                        resumo='Detalhe os dados que ajudam a classificar e contextualizar o processo.',
                        ordem=2,
                        conteudo='<h2>Assuntos, interessados e observações</h2>\n<p>A criação de um processo envolve mais que escolher um tipo. O SEI permite informar assuntos, interessados e observações que ajudam a classificar e contextualizar o trabalho.</p>\n<h3>Assuntos</h3>\n<p>Os assuntos informados são adicionados aos assuntos sugeridos para o tipo de processo. Quando o tipo não possui assuntos sugeridos, pode ser necessário informar ao menos um assunto.</p>\n<h3>Interessados</h3>\n<p>Os interessados são pessoas ou entidades relacionadas ao processo. A identificação pode usar informações como IdContato, CPF, CNPJ, sigla e nome.</p>\n<h3>Observação</h3>\n<p>O campo de observação permite associar um texto da unidade ao processo. Ele deve ser usado de forma objetiva e coerente com o procedimento.</p>\n<h3>Boa classificação</h3>\n<p>Assunto, interessado e especificação devem se complementar. Uma especificação clara com interessados corretos torna o processo mais fácil de localizar e interpretar.</p>\n<div class="destaque"><b>Importante:</b> Evite descrições vagas. O próximo usuário precisa entender o processo sem depender de explicações externas.</div>'
                    ),
                    Aula(
                        id=3,
                        titulo='Envio, relacionamento e retorno durante a criação',
                        resumo='Veja o que pode ser configurado já no momento em que o processo é gerado.',
                        ordem=3,
                        conteudo='<h2>Envio, relacionamento e retorno durante a criação</h2>\n<p>A criação de um processo pode ser acompanhada de ações adicionais. Isso permite que determinados fluxos sejam iniciados já com relacionamento, envio e controles.</p>\n<h3>UnidadesEnvio</h3>\n<p>Permite informar unidades destinatárias após a geração. O processo pode permanecer aberto na unidade geradora e também nas unidades informadas.</p>\n<h3>SinManterAbertoUnidade</h3>\n<p>Controla se o processo permanecerá aberto na unidade de origem. Esse comportamento precisa estar alinhado ao fluxo administrativo.</p>\n<h3>Retorno Programado</h3>\n<p>Podem ser usados campos de data ou quantidade de dias para definir um retorno programado. Também existe indicação para considerar dias úteis.</p>\n<h3>Marcador e controle de prazo</h3>\n<p>A geração também pode receber informações de marcador e de controle de prazo, permitindo que o novo processo já entre no fluxo com elementos de organização.</p>\n<div class="destaque"><b>Importante:</b> Automatizar uma etapa só faz sentido quando o fluxo já está claramente definido.</div>'
                    )
                ]
            ),
            Curso(
                id=3,
                titulo='3. Documentos no processo',
                descricao='Aprenda a criar, incluir e consultar documentos internos e externos.',
                nivel='Documentos',
                aulas=[
                    Aula(
                        id=1,
                        titulo='Documento gerado e documento recebido',
                        resumo='Entenda os dois tipos principais de documento usados no SEI.',
                        ordem=1,
                        conteudo='<h2>Documento gerado e documento recebido</h2>\n<p>A estrutura <b>Documento</b> diferencia documentos produzidos no ambiente eletrônico e documentos recebidos de fontes externas.</p>\n<h3>Tipo G</h3>\n<p><b>G</b> representa documento gerado. Ele pode possuir descrição, conteúdo produzido no editor e outras informações próprias de um documento interno.</p>\n<h3>Tipo R</h3>\n<p><b>R</b> representa documento recebido ou externo. Ele exige atenção a informações como data, nome do arquivo, remetente e tipo de conferência.</p>\n<h3>Associação ao processo</h3>\n<p>O documento pode ser associado ao processo por IdProcedimento ou ProtocoloProcedimento. O objetivo é garantir que o documento seja incluído no processo correto.</p>\n<h3>IdSerie</h3>\n<p><b>IdSerie</b> identifica o tipo de documento cadastrado no SEI. A função <code>listarSeries</code> permite obter as séries autorizadas de acordo com unidade e tipo de processo.</p>\n<div class="destaque"><b>Importante:</b> Documento não é apenas um arquivo anexado. Ele possui tipo, origem, identificação e regras próprias.</div>'
                    ),
                    Aula(
                        id=2,
                        titulo='incluirDocumento: adicionando um documento',
                        resumo='Conheça a função de inclusão e a sequência de dados necessários.',
                        ordem=2,
                        conteudo='<h2>incluirDocumento: adicionando um documento</h2>\n<p>A função <code>incluirDocumento</code> adiciona um documento a um processo. Ela recebe a unidade e a estrutura completa do documento.</p>\n<h3>O que precisa ser informado</h3>\n<ul>\n<li>identificação do sistema e do serviço;</li>\n<li>unidade responsável;</li>\n<li>dados da estrutura Documento;</li>\n<li>processo ao qual o documento pertence;</li>\n<li>tipo do documento;</li>\n<li>campos específicos para documento gerado ou recebido.</li>\n</ul>\n<h3>Retorno</h3>\n<p>A operação retorna informações da inclusão, incluindo identificadores que permitem localizar o documento criado.</p>\n<h3>Erros comuns que o treinamento deve evitar</h3>\n<ul>\n<li>incluir no processo errado;</li>\n<li>selecionar tipo de documento inadequado;</li>\n<li>não preencher dados obrigatórios de documento externo;</li>\n<li>usar nível de acesso incorreto;</li>\n<li>nomear o arquivo de forma pouco clara.</li>\n</ul>\n<div class="destaque"><b>Importante:</b> A inclusão correta facilita leitura, assinatura, consulta e organização posterior.</div>'
                    ),
                    Aula(
                        id=3,
                        titulo='consultarDocumento',
                        resumo='Veja quais dados de um documento podem ser consultados.',
                        ordem=3,
                        conteudo='<h2>consultarDocumento</h2>\n<p>A função <code>consultarDocumento</code> consulta um documento a partir do seu protocolo e pode retornar informações adicionais controladas por sinalizadores.</p>\n<h3>Informações opcionais</h3>\n<ul>\n<li>andamento de geração;</li>\n<li>assinaturas;</li>\n<li>publicação;</li>\n<li>campos de formulário;</li>\n<li>blocos em que o documento aparece.</li>\n</ul>\n<h3>Retorno da consulta</h3>\n<p>O retorno pode incluir processo relacionado, número do documento, níveis de acesso, link de acesso, tipo de documento, unidade elaboradora, assinaturas e publicação.</p>\n<h3>Processos sigilosos</h3>\n<p>Documentos de processos sigilosos não são retornados por essa consulta. Isso demonstra que a visibilidade depende das regras de acesso e do contexto.</p>\n<h3>Uso eficiente</h3>\n<p>Solicite apenas as informações realmente necessárias. Cada conjunto adicional de dados pode aumentar o processamento.</p>\n<div class="destaque"><b>Importante:</b> Consultar documento é analisar seu contexto, não apenas abrir seu conteúdo.</div>'
                    )
                ]
            ),
            Curso(
                id=4,
                titulo='4. Arquivos e documentos externos',
                descricao='Entenda como arquivos são preparados e associados a documentos externos.',
                nivel='Documentos',
                aulas=[
                    Aula(
                        id=1,
                        titulo='adicionarArquivo: preparando arquivo externo',
                        resumo='Entenda como arquivos externos podem ser enviados antes de sua associação a um documento.',
                        ordem=1,
                        conteudo='<h2>adicionarArquivo: preparando arquivo externo</h2>\n<p>A função <code>adicionarArquivo</code> cria um arquivo no repositório e retorna um identificador que poderá ser usado depois em um documento externo.</p>\n<h3>Entradas</h3>\n<ul>\n<li><b>Nome:</b> nome do arquivo;</li>\n<li><b>Tamanho:</b> tamanho total em bytes;</li>\n<li><b>Hash:</b> MD5 do conteúdo total;</li>\n<li><b>Conteudo:</b> conteúdo total ou parcial codificado em Base64.</li>\n</ul>\n<h3>IdArquivo</h3>\n<p>Depois do envio, o SEI retorna o identificador do arquivo. Esse IdArquivo pode ser informado na estrutura Documento.</p>\n<h3>Por que existe essa etapa</h3>\n<p>Arquivos maiores podem ser enviados separadamente antes da criação do documento externo. Isso evita a necessidade de repetir o conteúdo no momento da inclusão.</p>\n<div class="destaque"><b>Importante:</b> O arquivo precisa ser corretamente associado a um documento; enviar o arquivo sozinho não conclui a inclusão documental.</div>'
                    ),
                    Aula(
                        id=2,
                        titulo='adicionarConteudoArquivo: envio em partes',
                        resumo='Veja como o SEI completa um arquivo que foi enviado parcialmente.',
                        ordem=2,
                        conteudo='<h2>adicionarConteudoArquivo: envio em partes</h2>\n<p>Quando o conteúdo não é enviado de uma vez, a função <code>adicionarConteudoArquivo</code> adiciona novas partes ao arquivo já criado.</p>\n<h3>Dados utilizados</h3>\n<p>A função recebe o <b>IdArquivo</b> criado anteriormente e um novo bloco de <b>Conteudo</b> codificado em Base64.</p>\n<h3>Validação</h3>\n<p>O SEI verifica automaticamente quando o conteúdo está completo, comparando o tamanho esperado e o hash do arquivo.</p>\n<h3>Ativação</h3>\n<p>Quando o tamanho e o hash estão corretos, o arquivo é ativado e pode ser usado em chamadas de inclusão de documento.</p>\n<h3>Arquivo incompleto</h3>\n<p>Arquivos incompletos ou não associados podem ser removidos posteriormente pelo processo de limpeza do repositório.</p>\n<div class="destaque"><b>Importante:</b> Dividir o envio não muda o arquivo final: todas as partes precisam formar exatamente o conteúdo esperado.</div>'
                    ),
                    Aula(
                        id=3,
                        titulo='Conteudo, ConteudoMTOM e IdArquivo',
                        resumo='Aprenda as formas de associar conteúdo a documentos.',
                        ordem=3,
                        conteudo='<h2>Conteudo, ConteudoMTOM e IdArquivo</h2>\n<p>A estrutura Documento possui diferentes caminhos para representar o conteúdo do documento.</p>\n<h3>Conteudo</h3>\n<p>Pode carregar conteúdo codificado em Base64. Para documentos gerados, representa conteúdo do editor; para externos, pode representar o anexo.</p>\n<h3>ConteudoMTOM</h3>\n<p>É uma alternativa para conteúdo textual ou binário em documentos externos. O sistema aceita apenas uma das formas de conteúdo previstas para a requisição.</p>\n<h3>IdArquivo</h3>\n<p>Permite associar um arquivo previamente enviado por <code>adicionarArquivo</code> e completado, quando necessário, por <code>adicionarConteudoArquivo</code>.</p>\n<h3>Escolha correta</h3>\n<p>A forma de envio depende do tipo de documento e da maneira como a integração está estruturada. Para o usuário final, o conceito importante é que documento externo precisa possuir conteúdo e identificação coerentes.</p>\n<div class="destaque"><b>Importante:</b> O conteúdo é parte do documento, mas os metadados continuam sendo essenciais para sua organização.</div>'
                    )
                ]
            ),
            Curso(
                id=5,
                titulo='5. Tramitação e responsabilidade',
                descricao='Aprenda a enviar processos, controlar retorno e atribuir responsáveis.',
                nivel='Tramitação',
                aulas=[
                    Aula(
                        id=1,
                        titulo='enviarProcesso',
                        resumo='Conheça a função de tramitação entre unidades.',
                        ordem=1,
                        conteudo='<h2>enviarProcesso</h2>\n<p>A função <code>enviarProcesso</code> encaminha um processo para uma ou mais unidades destinatárias.</p>\n<h3>Entradas essenciais</h3>\n<ul>\n<li><b>IdUnidade:</b> unidade que realiza o envio;</li>\n<li><b>ProtocoloProcedimento:</b> processo enviado;</li>\n<li><b>UnidadesDestino:</b> unidades que receberão o processo.</li>\n</ul>\n<h3>Manter aberto na origem</h3>\n<p><b>SinManterAbertoUnidade</b> indica se o processo continuará aberto na unidade de origem depois da tramitação.</p>\n<h3>Notificação</h3>\n<p><b>SinEnviarEmailNotificacao</b> permite solicitar aviso por e-mail às unidades destinatárias.</p>\n<h3>Reabertura automática</h3>\n<p><b>SinReabrir</b> pode reabrir automaticamente um processo concluído, desde que a operação de reabertura esteja autorizada.</p>\n<div class="destaque"><b>Importante:</b> Antes de enviar, confira se a unidade destinatária realmente representa a próxima etapa do fluxo.</div>'
                    ),
                    Aula(
                        id=2,
                        titulo='Retorno Programado',
                        resumo='Aprenda a usar a ideia de retorno dentro da tramitação.',
                        ordem=2,
                        conteudo='<h2>Retorno Programado</h2>\n<p>O envio de um processo pode incluir uma expectativa de retorno. Isso é útil quando a unidade de origem precisa acompanhar uma resposta futura.</p>\n<h3>DataRetornoProgramado</h3>\n<p>Permite informar uma data específica de retorno.</p>\n<h3>DiasRetornoProgramado</h3>\n<p>Permite definir uma quantidade de dias em vez de uma data fixa.</p>\n<h3>SinDiasUteisRetornoProgramado</h3>\n<p>Indica se o prazo em dias deve considerar dias úteis.</p>\n<h3>Uso no fluxo</h3>\n<p>O retorno programado deve refletir uma necessidade real do processo. Ele não substitui a definição do procedimento administrativo.</p>\n<div class="destaque"><b>Importante:</b> Prazo sem regra vira ruído. Use controles quando existir uma responsabilidade clara de acompanhamento.</div>'
                    ),
                    Aula(
                        id=3,
                        titulo='atribuirProcesso',
                        resumo='Entenda como um processo pode ser atribuído a um usuário.',
                        ordem=3,
                        conteudo='<h2>atribuirProcesso</h2>\n<p>A função <code>atribuirProcesso</code> associa o processo a um usuário dentro de uma unidade.</p>\n<h3>Dados principais</h3>\n<ul>\n<li>IdUnidade;</li>\n<li>ProtocoloProcedimento;</li>\n<li>IdUsuario;</li>\n<li>SinReabrir.</li>\n</ul>\n<h3>Diferença entre atribuir e enviar</h3>\n<p><b>Enviar</b> movimenta o processo entre unidades. <b>Atribuir</b> organiza a responsabilidade de um usuário dentro da unidade.</p>\n<h3>Reabertura</h3>\n<p>Se necessário, a atribuição pode solicitar reabertura automática de um processo concluído.</p>\n<h3>Uso recomendado</h3>\n<p>Atribuição é útil para deixar claro quem está responsável pela análise ou execução de uma etapa dentro da unidade.</p>\n<div class="destaque"><b>Importante:</b> Atribuir não substitui a tramitação. São ações com objetivos diferentes.</div>'
                    )
                ]
            ),
            Curso(
                id=6,
                titulo='6. Consulta, histórico e anotações',
                descricao='Aprenda a consultar processos e interpretar seu histórico de trabalho.',
                nivel='Acompanhamento',
                aulas=[
                    Aula(
                        id=1,
                        titulo='consultarProcedimento',
                        resumo='Veja como o SEI retorna informações completas de um processo.',
                        ordem=1,
                        conteudo='<h2>consultarProcedimento</h2>\n<p>A função <code>consultarProcedimento</code> consulta um processo a partir do seu protocolo e pode retornar diferentes conjuntos de informações.</p>\n<h3>Dados adicionais que podem ser solicitados</h3>\n<ul>\n<li>assuntos;</li>\n<li>interessados;</li>\n<li>observações;</li>\n<li>andamento de geração;</li>\n<li>andamento de conclusão;</li>\n<li>último andamento;</li>\n<li>unidades onde o processo está aberto;</li>\n<li>processos relacionados;</li>\n<li>processos anexados.</li>\n</ul>\n<h3>O retorno</h3>\n<p>O retorno pode apresentar especificação, data de autuação, níveis de acesso, tipo de processo, andamentos e relações com outros processos.</p>\n<h3>Antes de agir</h3>\n<p>Consultar o contexto ajuda a evitar duplicidade de ações e decisões baseadas em informações incompletas.</p>\n<div class="destaque"><b>Importante:</b> Leia o estado atual do processo antes de alterar seu estado.</div>'
                    ),
                    Aula(
                        id=2,
                        titulo='listarAndamentos e lancarAndamento',
                        resumo='Entenda como o histórico do processo pode ser consultado e atualizado.',
                        ordem=2,
                        conteudo='<h2>listarAndamentos e lancarAndamento</h2>\n<p>Os andamentos registram acontecimentos ligados ao processo. Eles ajudam a reconstruir o histórico administrativo.</p>\n<h3>listarAndamentos</h3>\n<p>Permite filtrar andamentos por identificadores, tarefas ou tarefas de módulo. Também pode retornar atributos associados.</p>\n<h3>lancarAndamento</h3>\n<p>Registra um novo andamento a partir de uma tarefa e, quando necessário, atributos. Para atualização textual, existe uma forma específica de registrar a descrição.</p>\n<h3>Como ler o histórico</h3>\n<ul>\n<li>observe a data;</li>\n<li>observe a unidade;</li>\n<li>observe o usuário;</li>\n<li>identifique a ação ou tarefa registrada;</li>\n<li>compare com a etapa atual do processo.</li>\n</ul>\n<div class="destaque"><b>Importante:</b> O histórico é a trilha do processo. Consulte-o antes de repetir ou desfazer uma ação.</div>'
                    ),
                    Aula(
                        id=3,
                        titulo='registrarAnotacao',
                        resumo='Veja como anotações podem ser associadas a um processo aberto.',
                        ordem=3,
                        conteudo='<h2>registrarAnotacao</h2>\n<p>A função <code>registrarAnotacao</code> registra anotações em um processo que esteja aberto na unidade.</p>\n<h3>Dados utilizados</h3>\n<p>A função recebe a unidade e um conjunto de estruturas de anotação.</p>\n<h3>Estrutura Anotacao</h3>\n<p>A anotação possui o número do processo, uma descrição e um indicador que pode marcar a anotação como prioritária.</p>\n<h3>Quando usar</h3>\n<p>Anotações podem ajudar a registrar lembretes ou informações de apoio para a unidade, mas não devem substituir documentos formais quando o fluxo exige registro documental.</p>\n<h3>Texto objetivo</h3>\n<p>Uma boa anotação deve ser curta, compreensível e ligada ao trabalho que está sendo realizado.</p>\n<div class="destaque"><b>Importante:</b> Use anotação para apoio operacional, não para esconder decisões que deveriam estar documentadas formalmente.</div>'
                    )
                ]
            ),
            Curso(
                id=7,
                titulo='7. Organização e controle',
                descricao='Use marcadores, prazos e relações para organizar o fluxo de trabalho.',
                nivel='Organização',
                aulas=[
                    Aula(
                        id=1,
                        titulo='definirMarcador e listarMarcadoresUnidade',
                        resumo='Organize processos com marcadores disponíveis na unidade.',
                        ordem=1,
                        conteudo='<h2>definirMarcador e listarMarcadoresUnidade</h2>\n<p>Marcadores ajudam a organizar processos dentro da unidade.</p>\n<h3>listarMarcadoresUnidade</h3>\n<p>Retorna os marcadores disponíveis na unidade. Cada marcador possui identificador, nome, ícone e estado ativo.</p>\n<h3>definirMarcador</h3>\n<p>Recebe um conjunto de definições que relaciona processo, marcador e texto associado.</p>\n<h3>Uso prático</h3>\n<p>Marcadores podem representar categorias operacionais internas, prioridades de acompanhamento ou outras formas de organização definidas pela unidade.</p>\n<h3>Cuidados</h3>\n<p>O marcador não muda o tipo do processo nem substitui a classificação oficial. Ele é um recurso de organização.</p>\n<div class="destaque"><b>Importante:</b> Padronize o uso de marcadores para que todos na unidade interpretem os mesmos sinais da mesma forma.</div>'
                    ),
                    Aula(
                        id=2,
                        titulo='definirControlePrazo',
                        resumo='Veja como um processo aberto pode receber um controle de prazo.',
                        ordem=2,
                        conteudo='<h2>definirControlePrazo</h2>\n<p>A função <code>definirControlePrazo</code> recebe um conjunto de definições de prazo para processos abertos na unidade.</p>\n<h3>Formas de prazo</h3>\n<p>A definição pode usar uma data específica ou uma quantidade de dias. Quando são usados dias, também pode ser indicado se devem ser considerados dias úteis.</p>\n<h3>Regra importante</h3>\n<p>Não se deve informar simultaneamente uma data de prazo e uma definição por dias.</p>\n<h3>Uso no fluxo</h3>\n<p>O controle de prazo deve refletir uma obrigação, limite ou necessidade operacional real.</p>\n<h3>Diferença para retorno programado</h3>\n<p>Retorno programado acompanha a expectativa de retorno após uma tramitação. Controle de prazo é um mecanismo de organização de prazo na unidade.</p>\n<div class="destaque"><b>Importante:</b> Escolha uma única forma de representar o prazo e mantenha a regra compreensível para a equipe.</div>'
                    ),
                    Aula(
                        id=3,
                        titulo='Relacionar, anexar e desanexar processos',
                        resumo='Entenda as diferenças entre relações processuais.',
                        ordem=3,
                        conteudo='<h2>Relacionar, anexar e desanexar processos</h2>\n<p>O SEI possui operações diferentes para organizar relações entre processos. Elas não devem ser confundidas.</p>\n<h3>anexarProcesso</h3>\n<p>Trabalha com um processo principal e um processo anexado. A anexação cria uma relação específica entre eles.</p>\n<h3>desanexarProcesso</h3>\n<p>Remove uma anexação e exige um motivo para a desanexação.</p>\n<h3>Processos relacionados</h3>\n<p>Processos também podem ser relacionados, inclusive durante a geração de um novo procedimento. Relação e anexação não representam necessariamente o mesmo vínculo.</p>\n<h3>Boa prática</h3>\n<p>Antes de anexar ou desanexar, confirme o procedimento administrativo aplicável e registre o motivo quando a operação exigir.</p>\n<div class="destaque"><b>Importante:</b> Use cada tipo de relação com intenção clara. Organização processual não deve ser feita por tentativa e erro.</div>'
                    )
                ]
            ),
            Curso(
                id=8,
                titulo='8. Blocos',
                descricao='Aprenda a criar, preencher, disponibilizar e concluir blocos.',
                nivel='Blocos',
                aulas=[
                    Aula(
                        id=1,
                        titulo='gerarBloco',
                        resumo='Conheça os tipos de bloco e como eles são criados.',
                        ordem=1,
                        conteudo='<h2>gerarBloco</h2>\n<p>A função <code>gerarBloco</code> cria um bloco em uma unidade.</p>\n<h3>Tipos de bloco</h3>\n<ul>\n<li><b>A:</b> Assinatura;</li>\n<li><b>R:</b> Reunião;</li>\n<li><b>I:</b> Interno.</li>\n</ul>\n<h3>Descrição e disponibilização</h3>\n<p>O bloco recebe uma descrição e pode indicar unidades para disponibilização.</p>\n<h3>Documentos</h3>\n<p>É possível informar documentos que serão incluídos no bloco, desde que a operação correspondente esteja autorizada.</p>\n<h3>SinDisponibilizar</h3>\n<p>Permite indicar disponibilização automática, quando o serviço possui permissão para disponibilizar blocos.</p>\n<div class="destaque"><b>Importante:</b> Escolha o tipo do bloco conforme o objetivo: assinatura, reunião ou organização interna.</div>'
                    ),
                    Aula(
                        id=2,
                        titulo='incluirDocumentoBloco e incluirProcessoBloco',
                        resumo='Aprenda a colocar documentos e processos em blocos.',
                        ordem=2,
                        conteudo='<h2>incluirDocumentoBloco e incluirProcessoBloco</h2>\n<p>Depois que um bloco existe, o SEI possui funções para incluir documentos ou processos nele.</p>\n<h3>incluirDocumentoBloco</h3>\n<p>Utiliza a unidade, o número do bloco, o protocolo do documento e uma anotação opcional.</p>\n<h3>incluirProcessoBloco</h3>\n<p>Utiliza a unidade, o número do bloco, o protocolo do processo e uma anotação opcional.</p>\n<h3>Diferença</h3>\n<p>Uma função trabalha com documento; a outra trabalha com processo. Identifique corretamente o objeto que será colocado no bloco.</p>\n<h3>Anotação</h3>\n<p>O texto opcional pode ajudar a contextualizar o item dentro do bloco.</p>\n<div class="destaque"><b>Importante:</b> Antes de incluir, confira o número do bloco e o protocolo do item.</div>'
                    ),
                    Aula(
                        id=3,
                        titulo='Disponibilizar, devolver, concluir e reabrir blocos',
                        resumo='Entenda o ciclo de vida de um bloco.',
                        ordem=3,
                        conteudo='<h2>Disponibilizar, devolver, concluir e reabrir blocos</h2>\n<p>Blocos podem passar por diferentes estados ao longo do trabalho.</p>\n<h3>disponibilizarBloco</h3>\n<p>Disponibiliza um bloco gerado para as unidades configuradas.</p>\n<h3>devolverBloco</h3>\n<p>Permite devolver um bloco que foi disponibilizado para uma unidade.</p>\n<h3>concluirBloco</h3>\n<p>Conclui o bloco quando o trabalho correspondente termina.</p>\n<h3>reabrirBloco</h3>\n<p>Reabre um bloco concluído quando o trabalho precisa ser retomado.</p>\n<h3>excluirBloco</h3>\n<p>Existe também uma operação própria de exclusão, diferente de conclusão.</p>\n<div class="destaque"><b>Importante:</b> Conclusão, devolução e exclusão têm significados diferentes. Use a operação correspondente ao estado real do trabalho.</div>'
                    )
                ]
            ),
            Curso(
                id=9,
                titulo='9. Segurança e restrições',
                descricao='Entenda bloqueios, níveis de acesso e limitações de consulta.',
                nivel='Segurança',
                aulas=[
                    Aula(
                        id=1,
                        titulo='bloquearProcesso',
                        resumo='Veja o que acontece quando um processo é bloqueado.',
                        ordem=1,
                        conteudo='<h2>bloquearProcesso</h2>\n<p>A função <code>bloquearProcesso</code> impede diversas alterações enquanto o bloqueio estiver ativo.</p>\n<h3>Operações impedidas</h3>\n<p>Entre as ações que ficam bloqueadas estão alterações de cadastro, inclusão de documentos, alteração de conteúdo, envio de processo, envio de e-mail, agendamento de publicação, assinatura, movimentação e exclusões.</p>\n<h3>Operações ainda possíveis</h3>\n<p>Algumas operações podem continuar permitidas, como atribuição, atualização de andamento, anotação, conclusão e reabertura, conforme as regras do processo.</p>\n<h3>Processos sigilosos</h3>\n<p>Processos sigilosos não podem ser bloqueados por essa operação.</p>\n<h3>Uso consciente</h3>\n<p>Bloquear deve ser uma decisão operacional clara, pois muda significativamente o que pode ser feito com o processo.</p>\n<div class="destaque"><b>Importante:</b> Bloqueio é um estado forte. Antes de aplicá-lo, entenda quais operações deixarão de funcionar.</div>'
                    ),
                    Aula(
                        id=2,
                        titulo='desbloquearProcesso',
                        resumo='Aprenda como remover o bloqueio e retomar operações.',
                        ordem=2,
                        conteudo='<h2>desbloquearProcesso</h2>\n<p>A função <code>desbloquearProcesso</code> remove o bloqueio de um processo aberto na unidade.</p>\n<h3>Dados necessários</h3>\n<p>São utilizados a unidade e o protocolo do processo.</p>\n<h3>Depois do desbloqueio</h3>\n<p>As operações que estavam impedidas pelo bloqueio podem voltar a ser executadas, desde que as demais permissões e condições também estejam atendidas.</p>\n<h3>Conferência</h3>\n<p>Antes de desbloquear, confirme o motivo original do bloqueio e se a condição que levou a ele já foi resolvida.</p>\n<div class="destaque"><b>Importante:</b> Desbloquear não ignora outras regras de acesso ou permissão do SEI.</div>'
                    ),
                    Aula(
                        id=3,
                        titulo='Níveis de acesso e hipótese legal',
                        resumo='Entenda público, restrito, sigiloso e a relação com hipótese legal.',
                        ordem=3,
                        conteudo='<h2>Níveis de acesso e hipótese legal</h2>\n<p>Processos e documentos podem possuir níveis de acesso diferentes.</p>\n<h3>Nível 0</h3>\n<p><b>Público:</b> conteúdo sem restrição específica definida pelo nível.</p>\n<h3>Nível 1</h3>\n<p><b>Restrito:</b> acesso limitado e associado às regras aplicáveis.</p>\n<h3>Nível 2</h3>\n<p><b>Sigiloso:</b> possui tratamento de acesso mais rigoroso.</p>\n<h3>listarHipotesesLegais</h3>\n<p>O SEI possui operação para listar hipóteses legais, inclusive com filtro por nível restrito ou sigiloso.</p>\n<h3>Impacto nas consultas</h3>\n<p>Consultas de procedimento e documento possuem limitações para conteúdo sigiloso. Por isso, a ausência de um item em uma consulta pode estar ligada às regras de acesso.</p>\n<div class="destaque"><b>Importante:</b> Classificação de acesso deve seguir a regra institucional, não uma escolha pessoal do usuário.</div>'
                    )
                ]
            ),
            Curso(
                id=10,
                titulo='10. Finalização e funções complementares',
                descricao='Conclua a formação com fechamento, comunicação, publicação e revisão.',
                nivel='Conclusão',
                aulas=[
                    Aula(
                        id=1,
                        titulo='concluirProcesso e reabrirProcesso',
                        resumo='Aprenda a encerrar e retomar a atuação de uma unidade.',
                        ordem=1,
                        conteudo='<h2>concluirProcesso e reabrirProcesso</h2>\n<p>Conclusão e reabertura controlam se uma unidade ainda possui trabalho ativo naquele processo.</p>\n<h3>concluirProcesso</h3>\n<p>Utiliza a unidade onde o processo está aberto e o protocolo do processo. Concluir não é excluir.</p>\n<h3>reabrirProcesso</h3>\n<p>Utiliza uma unidade por onde o processo tramitou e o protocolo do processo, permitindo retomar a atuação.</p>\n<h3>Quando concluir</h3>\n<ul>\n<li>não existe ação pendente na unidade;</li>\n<li>os documentos necessários foram tratados;</li>\n<li>a tramitação prevista já ocorreu, quando necessária;</li>\n<li>a etapa administrativa realmente terminou.</li>\n</ul>\n<h3>Quando reabrir</h3>\n<p>Quando uma nova necessidade exige que a unidade volte a atuar sobre um processo anteriormente concluído.</p>\n<div class="destaque"><b>Importante:</b> Conclusão representa estado de trabalho. Ela não apaga o histórico.</div>'
                    ),
                    Aula(
                        id=2,
                        titulo='enviarEmail',
                        resumo='Conheça os dados usados para enviar e-mail associado a um processo.',
                        ordem=2,
                        conteudo='<h2>enviarEmail</h2>\n<p>O SEI possui uma operação para enviar e-mail relacionado a um processo.</p>\n<h3>Campos principais</h3>\n<ul>\n<li>processo;</li>\n<li>endereço do remetente;</li>\n<li>destinatários;</li>\n<li>cópia oculta;</li>\n<li>assunto;</li>\n<li>mensagem;</li>\n<li>documentos do processo que serão anexados;</li>\n<li>nível de acesso e hipótese legal quando aplicável.</li>\n</ul>\n<h3>Uso responsável</h3>\n<p>O envio de e-mail deve estar ligado ao procedimento administrativo. Documentos anexados precisam ser conferidos antes do envio.</p>\n<h3>Nível de acesso</h3>\n<p>O envio também considera nível de acesso, reforçando que comunicação externa e segurança documental precisam caminhar juntas.</p>\n<div class="destaque"><b>Importante:</b> Confira destinatários e anexos antes de enviar. E-mail enviado para o endereço errado costuma viajar mais rápido que a explicação do erro.</div>'
                    ),
                    Aula(
                        id=3,
                        titulo='Publicação de documentos',
                        resumo='Veja as operações de agendamento, alteração e cancelamento de publicação.',
                        ordem=3,
                        conteudo='<h2>Publicação de documentos</h2>\n<p>O SEI possui operações específicas para trabalhar com publicação de documentos.</p>\n<h3>agendarPublicacao</h3>\n<p>Permite informar documento, motivo da publicação, veículo, data de disponibilização, resumo e dados relacionados à Imprensa Nacional quando necessários.</p>\n<h3>Motivos</h3>\n<ul>\n<li>Publicação;</li>\n<li>Retificação;</li>\n<li>Republicação;</li>\n<li>Apostilamento.</li>\n</ul>\n<h3>alterarPublicacao</h3>\n<p>Permite alterar uma publicação já identificada.</p>\n<h3>cancelarAgendamentoPublicacao</h3>\n<p>Cancela um agendamento de publicação usando identificadores da publicação ou do documento.</p>\n<div class="destaque"><b>Importante:</b> Publicação é uma etapa própria. Ela não deve ser confundida com simples inclusão ou envio de documento.</div>'
                    ),
                    Aula(
                        id=4,
                        titulo='Revisão do ciclo completo',
                        resumo='Conecte as principais funções em um fluxo de trabalho coerente.',
                        ordem=4,
                        conteudo='<h2>Revisão do ciclo completo</h2>\n<p>Depois de estudar as funções separadamente, é importante enxergar o processo como um fluxo contínuo.</p>\n<h3>Início</h3>\n<p><code>listarTiposProcedimento</code> ajuda a identificar os tipos disponíveis e <code>gerarProcedimento</code> cria o processo.</p>\n<h3>Documentos</h3>\n<p><code>listarSeries</code> ajuda a identificar tipos de documento, <code>incluirDocumento</code> adiciona documentos e <code>consultarDocumento</code> recupera seus dados.</p>\n<h3>Tramitação</h3>\n<p><code>enviarProcesso</code> movimenta o processo; <code>atribuirProcesso</code> organiza responsabilidade; retorno programado e controle de prazo ajudam no acompanhamento.</p>\n<h3>Acompanhamento</h3>\n<p><code>consultarProcedimento</code>, <code>listarAndamentos</code>, marcadores e anotações ajudam a compreender e organizar o estado atual.</p>\n<h3>Fechamento</h3>\n<p><code>concluirProcesso</code> encerra a atuação da unidade e <code>reabrirProcesso</code> permite retomá-la quando necessário.</p>\n<div class="destaque"><b>Importante:</b> O objetivo é compreender a lógica por trás das operações para que o uso do SEI seja consistente e previsível.</div>'
                    )
                ]
            )
        ]

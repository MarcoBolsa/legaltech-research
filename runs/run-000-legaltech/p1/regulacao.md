# P1 — Regulação e Risco · Run #0 (LegalTech Brasil)

> Coletor: frente **regulação** (OAB, CNJ, LGPD, exercício ilegal da advocacia).
> Método: WebSearch/WebFetch, sem MCP Jurisprudências.ai neste run (não solicitado — ver lacunas).
> Toda afirmação mapeada a H1–H7 do `p0/hypotheses.md`, tag [confirma]/[refuta]/[neutro].

---

## 1. Achados organizados

### 1.1 O núcleo do risco regulatório: fronteira "assistir vs substituir" (H3)

**Achado 1 — A atividade privativa da advocacia está definida por lei, não por tecnologia.**
O Estatuto da Advocacia (Lei 8.906/94, art. 1º) reserva a postulação judicial e as atividades de "consultoria, assessoria e direção jurídicas" a advogados inscritos na OAB. Isso vale independentemente do meio (humano, software, IA) — a lei não distingue "quem" presta a atividade privativa, só "o quê" é privativo.
**Fonte:** Lei 8.906/94, art. 1º — https://www.planalto.gov.br/ccivil_03/leis/l8906.htm — Tier 1.
**Mapeia:** H3 [neutro/base legal — confirma a existência do limite que H3 pressupõe].

**Achado 2 — Precedente concreto e recente (set/2025): plataforma que faz análise documental + estimativa de chance de sucesso + direcionamento a escritório foi julgada exercício ilegal da advocacia.**
Decisão da juíza Quezia Jemima Custódio Neto da Silva Reis, 2ª Vara Federal do Rio de Janeiro, em 04/09/2025, proibiu uma plataforma (nome não divulgado na cobertura) de "oferecer ou intermediar serviços jurídicos", com multa de até R$ 20.000 por descumprimento. Fundamento: art. 1º da Lei 8.906/94 — a plataforma analisava documentos, estimava taxa de sucesso de ações e direcionava clientes a escritórios parceiros, o que o juízo caracterizou como "consultoria, assessoria e direção jurídica" e não mera tecnologia neutra.
**Fonte:** ConJur, 04/09/2025 — https://www.conjur.com.br/2025-set-04/juiza-proibe-plataforma-de-oferecer-servicos-privativos-da-advocacia/ — Tier 2 (imprensa jurídica especializada, cobertura de decisão judicial — a decisão em si seria Tier 1, mas não temos acesso ao número do processo/inteiro teor).
**Mapeia:** H3 **[refuta parcialmente]** — mostra que o limite entre "ferramenta que assiste o advogado" (permitido) e "serviço que substitui o julgamento jurídico" (proibido) já foi testado e a linha caiu contra o produto quando ele (a) dava **estimativa de resultado/chance de sucesso** e (b) **direcionava** para prestador de serviço. Isso é um sinal de perigo direto para qualquer produto B2C de "diga se vale a pena processar" ou "estime sua indenização". Um produto **B2B para o advogado usar** (não B2C para o leigo) fica fora desse precedente específico — mas o precedente prova que a fiscalização e o Judiciário **já atuam** nessa fronteira, não é hipotético.

**Achado 3 — A OAB moveu ações contra mais de 20 legaltechs por captação de clientela/mercantilização; pelo menos uma (Resolvvi) obteve decisão favorável.**
Segundo cobertura de 2021 (LawInnovation, citando CEO da Resolvvi), a OAB ajuizou ações contra 20+ legaltechs alegando "captação indevida de clientes" e "mercantilização da profissão". A Justiça Federal de Brasília, em pelo menos um caso (Resolvvi — assistência a passageiros/consumidores negativados, ~300 advogados cadastrados, ~R$20mi recuperados para 6 mil consumidores), decidiu a favor da plataforma, argumentando que a internet "é rica em sites que direcionam os interessados para a contratação dos mais diversos serviços" e que não seria adequado restringir o acesso à informação sobre direitos.
**Fonte:** LawInnovation, ~2021 — https://lawinnovation.com.br/disputa-regulatoria-entre-oab-e-legaltechs-influenciara-futuro-da-advocacia-avalia-startup/ — Tier 2 (imprensa setorial, mas baseada em declaração de parte interessada — **conflito de interesse**: fonte é o próprio CEO da legaltech vencedora, sem contra-argumento da OAB no artigo).
**Mapeia:** H3 e H5 **[neutro/ambíguo]** — mostra que **o resultado da fiscalização não é uniforme**: mesma categoria de risco (marketplace advogado-cliente) teve desfechos diferentes conforme desenho do modelo. Não dá para concluir "marketplace é seguro" nem "marketplace é proibido" — depende de como a intermediação é estruturada (ex.: cobrar do consumidor vs. só listar advogados sem comissão por indicação).

**Achado 4 — Plataformas de "conexão direta" entre advogado e cliente configuram captação indevida; bancos de dados passivos, não.**
Segundo o Tribunal de Ética da OAB/SP (citado em Jusbrasil/Migalhas), usar serviço online que promove "de forma direta" a conexão entre advogados e clientes potenciais é captação indevida de clientela. Por outro lado, não há infração ética quando o advogado "pura e simplesmente consta de banco de dados, desprovido de serviço de aproximação" — ou seja, diretórios passivos (tipo "páginas amarelas") são tolerados; matching ativo não.
**Fonte:** Jusbrasil (agregador, citando entendimento do Tribunal de Ética OAB/SP) — https://www.jusbrasil.com.br/artigos/principais-plataformas-para-prospeccao-de-clientes-na-advocacia-em-meio-virtual-e-visao-da-oab/926396158 — Tier 3 (blog agregador sem citação de número de processo/ementa — tratar com cautela).
**Mapeia:** H5 **[confirma parcialmente, com restrição]** — existe um canal viável (diretório/conteúdo passivo), mas o canal mais "eficiente" de aquisição (matching ativo advogado↔cliente, o que seria o modelo de marketplace clássico) é o que a OAB mais persegue. Isso **restringe**, não elimina, H5: um outsider pode captar advogados via conteúdo/SEO/comunidade (não vedado), mas não pode construir um marketplace de leads sem risco regulatório direto.

---

### 1.2 IA especificamente: OAB e CNJ (H3, H7)

**Achado 5 — A OAB ainda NÃO tem provimento vinculante sobre IA — só uma Recomendação (não obrigatória) e um plano em construção.**
A Recomendação CFOAB n. 001/2024 (aprovada nov/2024) orienta o "uso responsável da IA generativa" em 4 eixos: legislação aplicável, confidencialidade/privacidade, prática jurídica ética, comunicação sobre uso de IA. Ponto central: "a dependência excessiva de ferramentas de IA é inconsistente com a prática da advocacia e não pode substituir a análise realizada pelo advogado" — e o advogado deve informar o cliente previamente se for usar IA na prestação do serviço. Em 2025, a OAB Nacional anunciou um "Plano Nacional de Integração de IA na Advocacia" (5 eixos: governança, capacitação, modernização, defesa de prerrogativas, apoio à jovem advocacia) que **deverá gerar um Provimento formal futuro** — ou seja, a norma vinculante ainda não existe, é recomendação + plano.
**Fonte:** OAB Nacional, nov/2024 — https://www.oab.org.br/noticia/62711/confira-versao-final-da-recomendacao-do-cfoab-sobre-o-uso-de-ia-na-pratica-juridica — Tier 1 (fonte oficial primária).
Complementar: Diário Eletrônico OAB (texto da Recomendação) — https://diario.oab.org.br/pages/materia/842347 — Tier 1.
Complementar: OAB, jun/2025 (Plano Nacional) — https://www.oab.org.br/noticia/64268/conselho-federal-da-oab-anuncia-plano-nacional-para-integrar-inteligencia-artificial-a-advocacia — Tier 1.
**Mapeia:** H3 **[confirma, com ressalva temporal]** — não há hoje vedação normativa vinculante ao uso de IA por advogados nem regra específica proibindo ferramenta de IA feita por não-advogado, desde que o produto seja B2B (vendido ao advogado como ferramenta de apoio) e não B2C (prestando diretamente ao leigo). Mas a ressalva é importante: **um Provimento formal está em elaboração** — a janela regulatória atual pode fechar ou mudar de forma não previsível. Isso é um risco de "regra móvel", não uma garantia permanente.

**Achado 6 — OAB/SP: responsabilidade por supervisão de IA recai sobre o sócio/advogado, não sobre o fornecedor da ferramenta.**
Decisão do Tribunal de Ética da OAB/SP (citada por Migalhas) estabelece que advogados sócios devem garantir supervisão do uso de IA no escritório — reforça que a responsabilidade profissional (e disciplinar) fica com quem advoga, não com quem fornece a ferramenta.
**Fonte:** Migalhas — https://www.migalhas.com.br/quentes/455537/advogados-socios-devem-garantir-supervisao-em-uso-de-ia-decide-oab-sp — Tier 2.
**Mapeia:** H3 **[confirma]** — favorável ao modelo B2B "ferramenta assistiva": reduz a exposição legal direta do fornecedor de software, porque a responsabilidade ético-disciplinar recai sobre o advogado usuário. Isso é um argumento a favor de posicionar o produto explicitamente como "ferramenta de apoio ao advogado", nunca como substituto de julgamento profissional — inclusive em termos de uso/contrato.

**Achado 7 — CNJ Resolução 615/2025 regula IA no Judiciário (uso interno pelos tribunais), inclusive contratação de fornecedores privados — mas seu escopo é o Judiciário, não legaltechs vendendo a advogados/escritórios privados.**
A Resolução CNJ nº 615, de 11/03/2025 (substitui a Resolução 332/2020), define diretrizes, requisitos e governança para IA usada **pelo Poder Judiciário**: classificação de risco (baixo/alto), supervisão humana obrigatória, auditorias, Comitê Nacional de IA, Plataforma Sinapses. Quando o tribunal contrata fornecedor privado de LLM/IAGen, exige conformidade com legislação brasileira, sigilo, segurança e possibilidade de auditoria externa — mas isso regula **contratos tribunal↔fornecedor**, não a venda de ferramentas de IA para escritórios de advocacia privados no mercado B2B.
**Fonte:** CNJ, Resolução 615/2025 (texto oficial) — https://atos.cnj.jus.br/atos/detalhar/6001 — Tier 1.
Complementar (análise): SMN Advogados — https://www.smnadv.com.br/cnj-publica-resolucao-no-615-2025-e-define-diretrizes-para-uso-de-inteligencia-artificial-no-judiciario/ — Tier 2.
**Mapeia:** H3 **[neutro]** — não se aplica diretamente ao produto-alvo (B2B para advogados autônomos/pequenos escritórios), mas é sinal de que **o Estado brasileiro já está normatizando IA jurídica em ritmo acelerado** (2 atualizações CNJ + 1 recomendação OAB + 1 plano nacional em ~18 meses) — o ambiente regulatório é dinâmico, não estático. Reforça a leitura de "janela regulatória móvel" do Achado 5.

**Achado 8 — Alucinação de IA (citação de jurisprudência inexistente) já gerou multas reais e encaminhamento à OAB — o risco de H7 é materializado, não hipotético.**
Múltiplos casos documentados 2025–2026: TRT-2 aplicou multa de 5% sobre valor da causa por litigância de má-fé e enviou ofício à OAB/SP para apuração disciplinar; TST (6ª Turma) multou empresa e advogado em 1% do valor da causa por citação de jurisprudência inexistente; TJ/PR multou advogado por "julgado confeccionado por IA" (fev/2026). Multas documentadas variam de R$1.200 a 20 salários-mínimos. O entendimento consolidado: o advogado tem dever de supervisionar e conferir a veracidade das informações apresentadas em juízo, e não pode atribuir o erro à ferramenta.
**Fontes:**
- ConJur, 16/02/2026 — https://www.conjur.com.br/2026-fev-16/uso-de-jurisprudencia-criada-por-ia-gera-multa-por-ma-fe-e-oficio-a-oab/ — Tier 2.
- TST (release institucional) — https://www.tst.jus.br/en/-/empresa-e-advogado-sao-condenados-por-possivel-uso-de-ia-com-citacoes-falsas-de-jurisprudencia — Tier 1 (fonte oficial do tribunal).
- Migalhas, "TJ/PR vê má-fé e multa advogado por julgado confeccionado por IA" — https://www.migalhas.com.br/quentes/459252/tj-pr-ve-ma-fe-e-multa-advogado-por-julgado-confeccionado-por-ia — Tier 2.
- Migalhas, "Leis e jurisprudência inventadas: Advogado é multado por uso de IA" — https://www.migalhas.com.br/quentes/433822/leis-e-jurisprudencia-inventadas-advogado-e-multado-por-uso-de-ia — Tier 2.
- ConJur, "Erros da advocacia com IA irritam tribunais e abrem risco de crime" — https://www.conjur.com.br/2026-mar-17/ma-fe-em-uso-de-ia-irrita-tribunais-e-leva-a-condenacao-de-advogados/ — Tier 2.
**Mapeia:** H7 **[refuta parcialmente]** — o risco de alucinação em citação de jurisprudência **não é teórico**: já produziu múltiplas sanções documentadas em 2025–2026, em tribunais diferentes (TRT, TST, TJ estadual). Isso empurra fortemente contra qualquer workflow-alvo que produza citação de jurisprudência sem RAG verificável/rastreável contra base primária confiável — o produto **precisa** ter mecanismo de citação verificável (não gerar texto livre com nomes de casos) para não repetir o padrão que já gerou multa e ofício disciplinar. Também reforça H3: o risco recai sobre o advogado, o que é favorável ao fornecedor (ver Achado 6), mas um fornecedor cujo produto **causa sistematicamente** esse erro tem risco reputacional/comercial mesmo sem risco legal direto.

---

### 1.3 LGPD e dados processuais (H4, H6)

**Achado 9 — A ANPD classificou web scraping como tratamento de dados pessoais sujeito à LGPD, mesmo sobre dados publicados voluntariamente — e colocou o tema na agenda regulatória 2025 com fiscalizações previstas.**
No Radar de Tecnologia n.º 3 (nov/2024), a ANPD afirmou explicitamente que web scraping é forma de tratamento de dados pessoais e está sujeito à LGPD, mesmo quando o dado foi publicado pelo próprio titular. A prática tem riscos ampliados quando combinada com IA ou grandes volumes agregados de dados. O tema entrou na Agenda Regulatória da ANPD para o 1º semestre de 2025, com pelo menos 3 ações de fiscalização previstas (preventivas, orientativas ou repressivas).
**Fonte:** Mattos Filho (análise de escritório, citando ANPD) — https://www.mattosfilho.com.br/en/unico/anpd-legal-data-processing-brazil/ — Tier 2.
**Mapeia:** H4 e H6 **[refuta parcialmente / eleva risco]** — isso é um alerta direto para qualquer estratégia de defensabilidade baseada em "coletar dados processuais públicos via scraping de tribunais/diários" (candidato natural a "fosso de dados proprietário" em H4). Se o produto pretende construir vantagem de dados via scraping massivo de PJe/e-SAJ/diários oficiais, isso **não é um atalho livre de risco** — a ANPD já sinalizou fiscalização ativa nessa área. Reduz o valor do "scraping em massa" como fosso defensável fácil e barato.

**Achado 10 — A aplicação da LGPD a processos judiciais é uma zona cinzenta ainda não resolvida (tensão publicidade processual vs. proteção de dados), incluindo pelo menos uma Resolução CNJ recente (647/2025) tratando do tema.**
Há debate doutrinário e institucional sobre se/como a LGPD se aplica aos autos processuais e à publicidade processual ampla (dados básicos de consulta livre vs. autos eletrônicos de acesso restrito). O CNJ publicou a Resolução nº 647, de 26/09/2025, sobre o tema (conteúdo específico não aprofundado nesta coleta — ver lacunas).
**Fonte:** ConJur (artigo de opinião, Rosas e Hussein) — https://www.conjur.com.br/2022-fev-21/rosas-hussein-afinal-judiciario-submeter-lgpd/ — Tier 3 (artigo de opinião, não é posição oficial consolidada) + CNJ Resolução 647/2025 (texto oficial não lido em detalhe) — https://atos.cnj.jus.br/atos/detalhar/6340 — Tier 1 (fonte primária, mas conteúdo não extraído nesta coleta).
**Mapeia:** H4 **[neutro — lacuna]** — a incerteza regulatória sobre até onde vai a publicidade processual (que legitimaria uso de dados processuais por terceiros) versus proteção de dados **não está resolvida**, o que é risco tanto para o produto quanto para os próprios tribunais/Jusbrasil. Não dá para tratar "dados processuais públicos = uso livre garantido" como premissa segura para construir fosso de dados.

**Achado 11 — Escritórios de advocacia são "controladores de dados" pela LGPD; dados jurídicos tratados como sensíveis.**
Guias setoriais (OAB Campinas, Aurum) tratam escritórios como controladores com responsabilidade direta pela LGPD sobre dados de clientes, classificando dados jurídicos como sensíveis, com exposição a sanções administrativas e responsabilidade civil por tratamento inadequado.
**Fonte:** Guia OAB Campinas — https://oabcampinas.org.br/wp-content/uploads/2021/12/Guia-LGPD_Advocacia.pdf — Tier 2 (guia de entidade de classe, não é norma primária, mas é orientação institucional).
**Mapeia:** H4 **[neutro]** — relevante para desenho do produto: se o SaaS processa dados de clientes do escritório (nomes de partes, documentos), o **escritório-cliente** é controlador e o **fornecedor de software é operador** pela LGPD — implica cláusulas contratuais de tratamento de dados (DPA) como requisito comercial básico, não um bônus. Não achado específico sobre exigência regulatória de residência de dados no Brasil para legaltechs (lacuna).

---

## 2. Sem fonte / impressão do coletor

- Impressão (não verificada por fonte específica): o padrão de enforcement da OAB parece mirar majoritariamente **modelos de captação/marketplace B2C** (conectar cliente-leigo a advogado, ou substituir avaliação jurídica do leigo) — não encontrei nenhum caso de enforcement contra uma ferramenta **puramente B2B** (SaaS vendido a advogados para uso próprio, sem contato direto com o cliente final do advogado). Isso sugere — mas não prova, por ausência de contra-exemplo buscado à exaustão — que o modelo B2B "ferramenta para o advogado usar" carrega risco regulatório sensivelmente menor que B2C. **Isto é inferência do coletor, não achado direto de fonte.**
- Impressão: não encontrei nenhum caso de enforcement da OAB especificamente contra uma ferramenta de IA (LLM/RAG) vendida a advogados como assistente de redação/pesquisa (tipo "Copilot jurídico") — os casos encontrados são todos de **plataformas de intermediação/marketing**, não de **ferramentas de produtividade para advogado**. Pode ser ausência real de conflito (categoria seria permitida) ou pode ser que a categoria ainda seja recente demais para ter gerado litígio. Não dá para diferenciar com a evidência coletada.

---

## 3. O que NÃO foi encontrado (ausência como dado)

| Lacuna | Por que importa | Tentativa feita |
|---|---|---|
| Nenhum provimento OAB **vinculante e específico** sobre ferramentas de IA (só Recomendação não-obrigatória + plano em construção) | H3 depende de saber se a janela regulatória atual é estável — não é: um Provimento formal está sendo desenhado e pode mudar as regras | Buscado diretamente ("OAB provimento IA 2025 2026") — resultado: confirma que ainda é recomendação, não provimento |
| Nenhum caso de enforcement específico contra ferramenta de IA de produtividade jurídica (não-marketplace) vendida a advogados | Testaria diretamente o risco do modelo B2B pretendido pelo operador | Buscado ("chatbot jurídico", "robô advogado" + proibição) — resultados focaram em marketplaces/captação, não em ferramentas assistivas puras |
| Texto completo e desfecho final das ações da OAB contra as "20+ legaltechs" (quantas perderam, quantas ganharam, quais atividades específicas) | Determinaria taxa de sucesso de enforcement por tipo de modelo — dado crucial para calibrar risco real vs. percebido | Fonte encontrada (LawInnovation) é de 2021, unilateral (voz da legaltech vencedora), sem lista completa nem follow-up mais recente |
| Conteúdo da Resolução CNJ nº 647/2025 (LGPD nos tribunais) | Poderia esclarecer diretamente a tensão publicidade processual × LGPD relevante para H4 | URL identificada mas conteúdo não lido nesta coleta (ver Achado 10) |
| Posição da ANPD especificamente sobre dados processuais/diários de justiça (vs. dados públicos genéricos) | Definiria se scraping de diários oficiais para alimentar produto jurídico é de risco alto ou baixo especificamente | Busca cobriu scraping genérico + legítimo interesse; não achei manifestação específica sobre diários de justiça |
| Jurisprudência do STF/STJ (não só tribunais estaduais/trabalhistas) sobre exercício ilegal por plataforma de tecnologia | Daria peso Tier 1 mais forte e precedente de instância superior | Não localizado nesta rodada de buscas |
| Uso do MCP Jurisprudências.ai para busca de precedentes específicos sobre "exercício ilegal da advocacia" + "plataforma"/"software"/"aplicativo" | Poderia trazer decisões primárias (Tier 1) em vez de depender de cobertura de imprensa | Não executado nesta coleta — registrar como próximo passo recomendado |

---

## 4. Tabela de Fontes

| # | Fonte | URL | Data | Tier |
|---|---|---|---|---|
| 1 | Lei 8.906/94 (Estatuto da Advocacia) | https://www.planalto.gov.br/ccivil_03/leis/l8906.htm | 1994 (vigente) | 1 |
| 2 | ConJur — decisão contra plataforma (exercício privativo) | https://www.conjur.com.br/2025-set-04/juiza-proibe-plataforma-de-oferecer-servicos-privativos-da-advocacia/ | 04/09/2025 | 2 |
| 3 | LawInnovation — disputa OAB × legaltechs (caso Resolvvi) | https://lawinnovation.com.br/disputa-regulatoria-entre-oab-e-legaltechs-influenciara-futuro-da-advocacia-avalia-startup/ | ~2021 | 2 (conflito de interesse: fonte é parte interessada) |
| 4 | Jusbrasil — plataformas de prospecção e visão da OAB | https://www.jusbrasil.com.br/artigos/principais-plataformas-para-prospeccao-de-clientes-na-advocacia-em-meio-virtual-e-visao-da-oab/926396158 | não datado | 3 |
| 5 | Migalhas — OAB/SP vai à Justiça contra Instituto Mãe Polvo | https://www.migalhas.com.br/quentes/455243/oabsp-vai-a-justica-contra-instituto-por-exercicio-ilegal-da-advocacia | 2025 | 2 |
| 6 | OAB — Recomendação n. 001/2024 (versão final) | https://www.oab.org.br/noticia/62711/confira-versao-final-da-recomendacao-do-cfoab-sobre-o-uso-de-ia-na-pratica-juridica | nov/2024 | 1 |
| 7 | Diário Eletrônico da OAB — texto Recomendação 001/2024 | https://diario.oab.org.br/pages/materia/842347 | 2024 | 1 |
| 8 | OAB — Plano Nacional de Integração de IA na Advocacia | https://www.oab.org.br/noticia/64268/conselho-federal-da-oab-anuncia-plano-nacional-para-integrar-inteligencia-artificial-a-advocacia | 2025/2026 | 1 |
| 9 | Migalhas — supervisão de IA por sócios, decisão OAB/SP | https://www.migalhas.com.br/quentes/455537/advogados-socios-devem-garantir-supervisao-em-uso-de-ia-decide-oab-sp | 2025 | 2 |
| 10 | CNJ — Resolução nº 615/2025 (texto oficial) | https://atos.cnj.jus.br/atos/detalhar/6001 | 11/03/2025 | 1 |
| 11 | SMN Advogados — análise Resolução CNJ 615/2025 | https://www.smnadv.com.br/cnj-publica-resolucao-no-615-2025-e-define-diretrizes-para-uso-de-inteligencia-artificial-no-judiciario/ | 2025 | 2 |
| 12 | ConJur — jurisprudência falsa por IA, multa + ofício OAB | https://www.conjur.com.br/2026-fev-16/uso-de-jurisprudencia-criada-por-ia-gera-multa-por-ma-fe-e-oficio-a-oab/ | 16/02/2026 | 2 |
| 13 | TST — release institucional sobre citações falsas de IA | https://www.tst.jus.br/en/-/empresa-e-advogado-sao-condenados-por-possivel-uso-de-ia-com-citacoes-falsas-de-jurisprudencia | 2025/2026 | 1 |
| 14 | Migalhas — TJ/PR multa por julgado "confeccionado" por IA | https://www.migalhas.com.br/quentes/459252/tj-pr-ve-ma-fe-e-multa-advogado-por-julgado-confeccionado-por-ia | fev/2026 | 2 |
| 15 | Migalhas — leis/jurisprudência inventadas, advogado multado | https://www.migalhas.com.br/quentes/433822/leis-e-jurisprudencia-inventadas-advogado-e-multado-por-uso-de-ia | 2025 | 2 |
| 16 | ConJur — erros de IA irritam tribunais, risco de crime | https://www.conjur.com.br/2026-mar-17/ma-fe-em-uso-de-ia-irrita-tribunais-e-leva-a-condenacao-de-advogados/ | 17/03/2026 | 2 |
| 17 | Mattos Filho — ANPD e web scraping (Radar Tecnologia nº3) | https://www.mattosfilho.com.br/en/unico/anpd-legal-data-processing-brazil/ | nov/2024–2025 | 2 |
| 18 | ConJur (opinião) — Judiciário e LGPD | https://www.conjur.com.br/2022-fev-21/rosas-hussein-afinal-judiciario-submeter-lgpd/ | 2022 | 3 (opinião) |
| 19 | CNJ — Resolução nº 647/2025 (não lida em detalhe) | https://atos.cnj.jus.br/atos/detalhar/6340 | 26/09/2025 | 1 (não aprofundada) |
| 20 | Guia LGPD para Escritórios de Advocacia — OAB Campinas | https://oabcampinas.org.br/wp-content/uploads/2021/12/Guia-LGPD_Advocacia.pdf | 2021 | 2 |
| 21 | OAB — Provimento 205/2021 (texto/portal oficial) | https://www.oab.org.br/leisnormas/legislacao/provimentos/205-2021 | 2021 | 1 |

**Contagem por tier:** Tier 1 = 8 · Tier 2 = 11 · Tier 3 = 2

---

## 5. Mapa Achado → Hipótese (resumo)

| Achado | H1 | H2 | H3 | H4 | H5 | H6 | H7 |
|---|---|---|---|---|---|---|---|
| 1 (base legal Lei 8.906/94) | — | — | neutro (base) | — | — | — | — |
| 2 (decisão set/2025 contra plataforma) | — | — | **refuta parcial** | — | — | — | — |
| 3 (20+ ações OAB, Resolvvi ganhou) | — | — | neutro/ambíguo | — | neutro/ambíguo | — | — |
| 4 (diretório passivo ok, matching ativo não) | — | — | — | — | **confirma parcial (restrito)** | — | — |
| 5 (sem provimento vinculante, só recomendação) | — | — | **confirma (temporário)** | — | — | — | — |
| 6 (responsabilidade recai no advogado-sócio) | — | — | **confirma** | — | — | — | — |
| 7 (CNJ 615/2025 — só Judiciário, não B2B privado) | — | — | neutro | — | — | — | — |
| 8 (multas por jurisprudência falsa de IA) | — | — | confirma (reforça) | — | — | — | **refuta parcial** |
| 9 (ANPD: scraping é tratamento de dados, fiscalização 2025) | — | — | — | **refuta parcial (eleva risco)** | — | — | — |
| 10 (LGPD × publicidade processual, zona cinzenta) | — | — | — | neutro/lacuna | — | — | — |
| 11 (escritório = controlador, software = operador) | — | — | — | neutro | — | — | — |

---

## 6. Resumo executivo (para consolidação P1)

A fronteira legal entre "ferramenta que assiste o advogado" e "serviço que substitui o julgamento jurídico" é real, ativamente fiscalizada e **já tem precedente concreto contra o lado errado da linha** (Achado 2, set/2025): plataforma que dava estimativa de chance de sucesso e direcionava para escritório foi proibida judicialmente. Isso não mata H3, mas define nitidamente o produto seguro: **B2B, vendido ao advogado, sem contato direto com o cliente leigo, sem estimar resultado de processo, sem direcionar/comissionar indicação**. A responsabilidade profissional recai sobre o advogado-usuário (Achado 6), o que favorece o fornecedor — mas a OAB ainda não tem provimento vinculante sobre IA (só recomendação + plano em elaboração), então a janela regulatória atual é favorável só **temporariamente** (Achados 5, 7). O risco de alucinação de citação jurídica já gerou múltiplas multas documentadas em 2025–2026 (Achado 8) — isso é ameaça direta e materializada a H7, não teórica, e exige que qualquer produto tenha citação verificável/rastreável, não geração livre. Do lado de dados, a estratégia óbvia de "fosso via scraping de dados processuais públicos" (candidata a H4) esbarra em sinalização recente da ANPD classificando scraping como tratamento sujeito à LGPD com fiscalização prevista para 2025 (Achado 9) — reduz o valor desse atalho como vantagem competitiva livre de risco. Do lado de canal (H5), captação por marketplace/matching ativo é a categoria mais perseguida pela OAB (20+ ações, resultado misto), enquanto diretórios passivos e conteúdo/SEO não sofrem o mesmo escrutínio — isso restringe, mas não elimina, os canais viáveis para um outsider. A maior lacuna da coleta é a ausência de qualquer caso de enforcement específico contra uma ferramenta de produtividade B2B pura (tipo "Copilot jurídico") — não há evidência de que essa categoria seja perseguida, mas também não há confirmação direta de que seja imune, só ausência de conflito registrado até agora.

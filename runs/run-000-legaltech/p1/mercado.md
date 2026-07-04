# P1 — Coleta: Mercado · Run #0 (LegalTech Brasil)

> Frente: Tamanho, crescimento e dinâmica do mercado legaltech Brasil — TAM/SAM, nº de legaltechs ativas, funding, tendências pós-LLM (2024-2026), casos de sucesso e fracasso.
> Método: WebSearch/WebFetch, 9 buscas + 2 fetch. Cruzado contra H1–H7 de `p0/hypotheses.md`.

---

## 1. Achados organizados

### 1.1 Tamanho de mercado (TAM/SAM) — sinal fraco e contraditório

- O mercado jurídico brasileiro como um todo (honorários, serviços, não só tech) movimenta **~R$ 50 bilhões/ano**, crescendo ~20% a.a. (dado de 2017, sem atualização encontrada para 2024-2026). [Migalhas, 2017, Tier 2] → **[neutro]** para H1/H2 — é TAM de serviços jurídicos, não SAM de software; é exatamente o número que a AH2 avisa para não confundir com demanda endereçável.
- Estimativa específica de **mercado de "Legal AI" no Brasil**: projeção de **US$ 58,7 milhões até 2030**, CAGR 17,6% (2025-2030), Brasil líder regional na América Latina. [Grand View Research, horizonte 2025-2030, Tier 2 — página-teaser de relatório pago, metodologia não verificável, tratar com cautela] → **[refuta parcialmente AH2]**: US$ 58,7M é um mercado pequeno frente a 1,3M advogados — reforça que "mercado grande e atrasado" não implica SAM grande para um entrante de IA.
- América Latina "Legal Tech Market": projeção **US$ 4,8 bilhões até 2033**, CAGR 11,12%, puxado por ferramentas de IA para pesquisa jurídica. [openpr.com citando relatório, 2025, Tier 3 — nota de imprensa de relatório pago, não é o dado primário] → **[neutro]**, mas mostra ordem de grandeza: legal tech ⊂ legal services é fração pequena, e "legal AI" é fração menor ainda.
- **Inconsistência relevante entre fontes**: nenhuma das duas estimativas de mercado ($58,7M Brasil "Legal AI" vs $4,8bi LatAm "Legal Tech") é claramente reconciliável — sugerem definições de escopo muito diferentes (a segunda provavelmente inclui e-discovery, compliance, case management de grandes empresas). **Registrado como lacuna**, não resolvido.

### 1.2 Número de legaltechs ativas — dado disperso, sem fonte única confiável

- AB2L (associação setorial de referência) **ultrapassou 1.000 membros** (startups, escritórios, departamentos jurídicos, universidades, órgãos públicos) — não é só contagem de legaltechs. [AB2L / imprensa, sem data exata, Tier 2] 
- Uma fonte (não-AB2L, agregador) cita **"mais de 1.500 startups no segmento jurídico"** [WebSearch snippet, sem data/fonte primária clara, Tier 3] enquanto outra cita **"~400 startups jurídicas no Brasil em 2025"** [inspire-se.co blog, Tier 3, conflito de interesse — legaltech falando do próprio setor]. Um terceiro dado: **"cresceu mais de 20% entre 2023 e 2025"** [mesma fonte Tier 3].
- AB2L mantém o **Radar de Lawtechs e Legaltechs** com 13 categorias (Analytics/Jurimetria, Regtech, Taxtech, Gestão Jurídica, Gestão de Escritório/Depto Jurídico, Extração/Monitoramento de Dados Públicos, Compliance, ODR, Automação de Documentos, IA, Conteúdo/Educação/Consultoria Jurídica, Real Estate Tech, Redes Profissionais) — PDF em `ab2l.org.br/wp-content/uploads/.../radar-junho-*.pdf` não pôde ser lido (404 na tentativa de fetch da página-índice; conteúdo do PDF em si não foi acessado). **Gap de coleta registrado**, não confirmado.
- Desde a criação da AB2L em 2017, "o número de LegalTechs associadas aumentou mais de 300%" [Tier 2/3 misto, sem número absoluto inicial/final claro].
- **Conclusão da subseção**: não há uma fonte Tier 1 e nenhuma Tier 2 única e auditável para "número de legaltechs ativas no Brasil" — os números variam 400/1.000/1.500 conforme a fonte e o que cada uma conta (membro de associação ≠ legaltech ≠ startup ativa). **[neutro]** para H1-H6, mas é achado epistemológico importante: **a "prova" de mercado grande citada popularmente é frouxa** — reforça a cautela da AH2.

### 1.3 Funding e sinais de capital de risco (2024-2026)

| Empresa | Rodada | Valor | Investidores | Segmento-alvo | Fonte/Tier |
|---|---|---|---|---|---|
| **Enter** | Seed (2024) → Series A (abr/2025) | US$ 5,5M (seed) → R$ 200M / US$ 35M (Series A), valuation R$ 2bi | Sequoia Capital, Founders Fund | **B2B enterprise**: automação de defesas trabalhistas/consumidor para grandes empresas (Itaú, Santander, Nubank, Magalu) | Exame, Brazil Journal, Beyond the Law, abr/2025, Tier 2 |
| **NetLex** | — | R$ 126 milhões (acumulado, sem data exata) | — | Gestão jurídica corporativa | startups.com.br, Tier 3, sem data precisa |
| **Inspira** | Rodada (2024/2025) | R$ 15M | Cloud9 Capital, Vivo Ventures (Wayra Brasil antes) | IA jurídica; movendo de "alto padrão" para advogados autônomos e pequenos escritórios também | empreendedor.com.br, startupi.com.br, Tier 2/3 |
| **Lexter.ai** | — | R$ 16M | — | IA jurídica | Tier 3, sem detalhe |
| **Bits (Legal Design)** | — | R$ 1,8M | — | Legal design | Tier 3 |
| **EasyJur** | — | R$ 1,4M | — | Software jurídico | Tier 3 |
| **Aleve LegalTech Ventures** (venture builder) | 4 anos de atuação | Portfólio avaliado em R$ 200M, 13 startups, meta de 20 até fim de 2025 | — | Venture builder dedicado a legaltech | sanpedrovalley.org.br, Tier 3 |

- Contexto global citado (não Brasil): "no 1º trimestre de 2026, legaltechs no mundo movimentaram US$ 1,42 bilhão em 35 rodadas" [Tier 3, sem fonte primária identificada — tratar como direcional].
- **Mapeamento para hipóteses:**
  - **[neutro/refuta parcial H6]**: o maior cheque (Enter, Sequoia/Founders Fund) mira **grandes empresas compradoras de defesa em massa (B2B enterprise)**, não advogados autônomos/pequenos escritórios — é evidência de que capital de risco está migrando para o segmento **oposto** ao do operador (não-advogado solo mirando pequeno escritório). Isso não refuta H6 diretamente (lacuna pode existir no segmento pequeno), mas mostra que o "buzz" de investimento não valida demanda no segmento-alvo do operador.
  - **[confirma parcialmente H1's antítese / AH2]**: Inspira migrando de "alto padrão" para autônomos/pequenos escritórios é sinal de que esse segmento é visto como expansão tardia, não como alvo primário de quem tem capital — pode indicar ARPU baixo lá (relevante a H2), mas é inferência, não fato direto.
  - Nenhuma fonte encontrada de captação específica mirando exclusivamente advogados autônomos/pequenos escritórios como tese central de investimento — **gap registrado**.

### 1.4 Tendências pós-LLM (2024-2026) — o achado mais forte da frente

- **Adoção de IA generativa por advogados no Brasil**: pesquisa **OAB-SP + Trybe + Jusbrasil + ITS Rio**, 1.500 respondentes: **55,1% já usam IA generativa** na rotina profissional; no recorte de escritórios, 28% usam ativamente e 58% avaliam/planejam adotar; 78% dos usuários frequentes usam ao menos 1x/semana. Principais usos: análise/resumo de documentos, elaboração de peças, pesquisa de jurisprudência/doutrina. [ConvergenciaDigital / Jusbrasil release, 2025, Tier 2 — nota: Jusbrasil é parte interessada como um dos realizadores, mas OAB-SP e ITS Rio dão peso institucional] → **[confirma H1]** (workflows citados = exatamente os candidatos da hipótese: análise de documentos, peças, jurisprudência) **e [confirma AH1]** (adoção já é maioria — "ter IA" deixou de ser diferencial, é tabela-stakes).
- **Barreiras de adoção declaradas**: 45% temem viés/subjetividade, 39% risco de privacidade/segurança, 32% resistência cultural. [mesma fonte, Tier 2] → relevante a H7 (confiança/limiar).
- **Marco regulatório**: em nov/2024, o Conselho Federal da OAB aprovou a **Recomendação 1/2024** permitindo e regulamentando uso de IA generativa, exigindo supervisão humana. [Tier 1 — ato normativo do órgão regulador, confirmado via múltiplas fontes de imprensa jurídica] → relevante primariamente à frente jurídica (H3), mas também emoldura H7 (a supervisão humana obrigatória é a válvula que torna "IA assistiva, não substitutiva" operacionalmente exigida — alinhado à síntese do P0).
- **Jusbrasil — Jus IA (o achado mais crítico da frente para H4/AH1):**
  - Lançado em **19/mar/2025**, copiloto de IA alimentado por acervo de **1,2 bilhão de documentos públicos** do Jusbrasil; funções: redigir/revisar peças, pesquisar e validar jurisprudência, analisar processos, estruturar teses. [ConJur, 19/mar/2025, Tier 2]
  - Em **abril/2026**, o Jusbrasil **integrou o Jus IA a TODOS os planos de assinatura, sem custo adicional**, disponível inclusive na experimentação gratuita, com **300 mil advogados usando mensalmente**. [ConJur, abr/2026, Tier 2]
  - **[REFUTA fortemente AH1 e ameaça diretamente H4]**: o maior incumbente com maior acervo de dados jurídicos proprietários do país já **comoditizou** IA generativa sobre jurisprudência/peças/documentos como feature gratuita embutida na assinatura básica, com escala de 300k usuários mensais. Qualquer produto de IA que compita no mesmo job-to-be-done ("analisar documentos", "pesquisar jurisprudência", "redigir peças" com RAG genérico) enfrenta um concorrente de distribuição + dados proprietários + preço zero incremental. Isso **eleva a barra de H4** (defensabilidade) drasticamente: não basta não ser "wrapper do ChatGPT" — é preciso não ser "wrapper do Jus IA" também.
- **Risco de alucinação já materializado em tribunais (relevante a H7):** múltiplos casos documentados de advogados multados por citar jurisprudência/leis inexistentes geradas por IA — TST, TJSC, TJPR, TRT-12 — multas de R$1.200 a 20 salários-mínimos + ofício à OAB para providências disciplinares, entre 2025-2026. [TST, ConJur, Migalhas, TJSC, TRT12 — múltiplas fontes institucionais/imprensa jurídica especializada, Tier 1 (decisões de tribunal) e Tier 2 (cobertura)] → **[confirma H7 como risco real, não hipotético]**: o limiar de confiabilidade é ativamente testado e falhando em casos reais; reforça que um produto no workflow de "geração de peça com citação" carrega risco de responsabilização documentado, não teórico. Fortalece a recomendação da H7 de escolher workflow tolerante a erro assistido.

### 1.5 Casos de sucesso e fracasso recentes

- **Sucesso (mas fora do segmento-alvo do operador):** Enter — Series A de US$35M liderada por Sequoia + Founders Fund, valuation R$2bi, clientes como Itaú/Santander/Nubank/Magalu, ganhos de causa 7-21% maiores com defesa via IA, meta de processar 250 mil ações em 2025. [Exame, Brazil Journal, abr/2025, Tier 2] — modelo é **B2B enterprise**, não B2B pequeno escritório/autônomo — **[neutro para H1/H2 do segmento-alvo, mas confirma que IA jurídica tem tração de mercado em algum segmento]**.
- **Sucesso citado em canal específico (menor escala, mais próximo do segmento-alvo):** caso de escritório de 12 advogados que migrou para "cloud jurídica" reduzindo custo mensal de R$4.800 para R$2.900 — citado em blog de fornecedor (BeansTech), **Tier 3, conflito de interesse explícito, sem verificação independente** → tratar como anedota de marketing, não evidência.
- **Fracasso:** **nenhum caso específico e nomeado de legaltech brasileira que fechou/faliu foi encontrado** nas buscas realizadas. As buscas retornaram apenas conteúdo promocional/institucional sobre legaltechs ativas. **Isso é, em si, um achado**: ou (a) não há cobertura de imprensa de fracassos no setor (assimetria de sobrevivência — só quem capta rodada vira notícia), ou (b) a pesquisa não foi funda o suficiente (Reddit, LinkedIn de fundadores, Crunchbase de shutdowns não foram consultados nesta leva). **Gap explícito, não conclusão.** Relevante porque a antítese do P0 presume "legaltechs que morreram no BR raramente morreram por falta de tecnologia" — essa afirmação **não pôde ser corroborada nem refutada** com as fontes encontradas nesta frente.

---

## 2. Tabela de fontes

| # | Fonte | URL | Data | Tier | Nota |
|---|---|---|---|---|---|
| 1 | AB2L (institucional) | https://ab2l.org.br/ | s/data exata | Tier 2 | Associação setorial, +1.000 membros |
| 2 | AB2L Radar (índice) | https://ab2l.org.br/ecossistema/radar-de-lawtechs-e-legaltechs/ | — | — | **404 no fetch — não acessado** |
| 3 | Empreendedor.com.br — Inspira/Wayra | https://empreendedor.com.br/tecnologia/startups/apos-investimento-da-wayra-brasil-legaltech-projeta-dobrar-de-tamanho-em-2025/ | 2025 | Tier 3 | Cobertura de imprensa de negócios |
| 4 | San Pedro Valley — Aleve LegalTech Ventures | https://sanpedrovalley.org.br/aleve-legaltech-ventures-completa-4-anos-com-13-startups-e-r-200-milhoes/ | 2025 | Tier 3 | |
| 5 | Startups.com.br — Inspira R$15M | https://startups.com.br/negocios/rodada-de-investimento/legaltech-inspira-capta-r-15m-para-expandir-base-de-clientes | 2025 | Tier 2 | Veículo especializado em startups |
| 6 | Portal Tela — Sequoia/Enter | https://www.portaltela.com/economia/negocios/2025/04/24/sequoia-investe-em-legaltech-brasileira-enter-e-ve-potencial-no-mercado-local | abr/2025 | Tier 2 | |
| 7 | Exame — Enter/Sequoia | https://exame.com/negocios/enter-como-uma-startup-brasileira-de-ia-atraiu-us-55-milhoes-da-sequoia/ | 2025 | Tier 2 | |
| 8 | Brazil Journal — Enter | https://braziljournal.com/enter-usa-ai-para-desafogar-acoes-trabalhistas-e-de-consumidores-e-ja-atraiu-o-sequoia/ | 2025 | Tier 2 | |
| 9 | Beyond the Law — Enter Series A | https://www.beyondthelaw.news/enter-series-a-2025/ | abr/2025 | Tier 2 | Valuation R$2bi confirmado |
| 10 | Gazeta do Povo — nº advogados | https://www.gazetadopovo.com.br/justica/numero-advogados-brasil-oab/ | — | Tier 2 | +1 milhão de advogados |
| 11 | FGV — 1º Estudo Demográfico da Advocacia | https://conhecimento.fgv.br/sites/default/files/2025-01/publicacoes/perfil_adv_1o-estudo_demografico_da_advocacia_brasileira.pdf | jan/2025 (dados coletados ago-out/2023) | **Tier 1** | Estudo encomendado pelo CFOAB, base 20.885 respondentes |
| 12 | Terra — "censo" OAB renda | https://www.terra.com.br/noticias/educacao/carreira/censo-da-oab-indica-que-64-dos-advogados-no-brasil-ganham-ate-r-66-mil,... | — | Tier 2 | 64% ganham até R$6,6mil/mês — relevante a H2 (teto de willingness-to-pay) |
| 13 | Migalhas — mercado jurídico R$50bi | https://www.migalhas.com.br/quentes/265702/mercado-juridico-movimenta-em-torno-de-r--50-bilhoes-ao-ano... | 2017 | Tier 2 | Dado desatualizado (8+ anos) |
| 14 | Grand View Research — Brazil Legal AI Market | https://www.grandviewresearch.com/horizon/outlook/legal-ai-market/brazil | 2025 (proj. 2025-2030) | Tier 2 | Página-teaser de relatório pago, metodologia não verificável |
| 15 | OpenPR — LatAm Legal Tech Market | https://www.openpr.com/news/4318912/latin-america-legal-tech-market-to-reach-usd-4-8-billion-by-2033 | 2025 | Tier 3 | Nota de imprensa de relatório pago |
| 16 | Aurum — Astrea planos e preços | https://www.aurum.com.br/astrea/planos-e-precos/ | corrente | Tier 3 | Fonte primária do próprio vendor — preço direto, mas conflito de interesse (marketing) |
| 17 | Projuris blog — preço a partir de R$49 | https://www.projuris.com.br/blog/software-juridico/ | corrente | Tier 3 | Vendor falando do próprio mercado |
| 18 | ConvergenciaDigital — OAB-SP 55% usam IA | https://convergenciadigital.com.br/inovacao/oab-sp-55-dos-advogados-usam-ia-generativa/ | 2025 | Tier 2 | |
| 19 | Jusbrasil release — pesquisa 55,1% | https://sobre.jusbrasil.com.br/releases/pesquisa-inedita-revela-que-55-1-dos-profissionais-de-direito-aplicam-ia-generativa-em-suas-atividades-diarias | 2025 | Tier 2 (parte interessada) | Jusbrasil é co-realizador da pesquisa — não é Tier 3 pois OAB-SP/ITS Rio são coautores institucionais, mas registrar possível viés |
| 20 | ConJur — Jusbrasil lança Jus IA | https://www.conjur.com.br/2025-mar-19/jusbrasil-lanca-ferramenta-de-ia-para-auxiliar-o-trabalho-de-advogados-e-juizes/ | 19/mar/2025 | Tier 2 | Veículo jurídico especializado, alta credibilidade |
| 21 | ConJur — Jus IA em todos os planos | https://www.conjur.com.br/2026-abr-13/ferramenta-de-ia-passa-a-integrar-todos-os-planos-do-jusbrasil/ | 13/abr/2026 | Tier 2 | 300 mil advogados/mês, custo zero incremental |
| 22 | TST — condenação por IA com citação falsa | https://www.tst.jus.br/en/-/empresa-e-advogado-sao-condenados-por-possivel-uso-de-ia-com-citacoes-falsas-de-jurisprudencia | — | **Tier 1** | Fonte oficial do tribunal |
| 23 | ConJur — multa por jurisprudência falsa | https://www.conjur.com.br/2026-fev-16/uso-de-jurisprudencia-criada-por-ia-gera-multa-por-ma-fe-e-oficio-a-oab/ | fev/2026 | Tier 2 | |
| 24 | TJSC — imprensa oficial, multa por IA | https://www.tjsc.jus.br/web/imprensa/-/tjsc-multa-autor-de-recurso-por-jurisprudencia-falsa-gerada-por-inteligencia-artificial | — | **Tier 1** | Fonte oficial do tribunal |
| 25 | TRT-12 — multa por jurisprudência inventada | https://portal.trt12.jus.br/noticias/autora-de-acao-e-multada-apos-advogada-inventar-jurisprudencia-e-desembargador | — | **Tier 1** | Fonte oficial do tribunal |
| 26 | Migalhas — TJ/PR multa por IA | https://www.migalhas.com.br/quentes/459252/tj-pr-ve-ma-fe-e-multa-advogado-por-julgado-confeccionado-por-ia | — | Tier 2 | |
| 27 | Inspire-se blog — tendências legaltech 2026, "~400 startups" | https://www.inspire-se.co/en/recursos/blog/tendencias-legaltech-2026 | 2025/2026 | Tier 3 | Vendor (Inspira) falando do próprio setor — conflito de interesse |
| 28 | BeansTech blog — caso Dr. Henrique | https://beanstech.com.br/blog/legaltech-software-advocacia-comparativo | 2026 | Tier 3 | Marketing de vendor, caso não verificado independentemente |

**Contagem por tier:** Tier 1 = 5 · Tier 2 = 16 · Tier 3 = 7 (total 28 fontes citadas; algumas URLs adicionais aparecidas nas buscas mas não usadas como evidência não estão listadas).

---

## 3. Mapa achado → hipótese

| Achado | H1 | H2 | H4 | H5 | H6 | H7 | AH1 | AH2 |
|---|---|---|---|---|---|---|---|---|
| 55,1% advogados já usam IA generativa; usos = doc/peça/jurisprudência | **confirma** (workflows validados como dor real e já-endereçada) | neutro | neutro | neutro | neutro | neutro | **confirma** (adoção já é maioria = commodity) | neutro |
| Jus IA gratuito em todos os planos Jusbrasil, 300k/mês | neutro | neutro | **refuta/ameaça fortemente** | neutro | **refuta parcialmente** (incumbente fecha a lacuna de IA rapidamente) | neutro | **confirma fortemente** | **confirma** (tamanho do incumbente não implica espaço para entrante) |
| Multas por alucinação de jurisprudência em tribunais (TST/TJSC/TJPR/TRT12) | neutro | neutro | neutro | neutro | neutro | **confirma** (risco real e documentado) | neutro | neutro |
| Recomendação 1/2024 CFOAB exige supervisão humana | neutro | neutro | neutro | neutro | neutro | **confirma** (janela regulatória para "assistivo, não autônomo") | neutro | neutro |
| Enter capta US$35M mirando grandes empresas (B2B enterprise) | neutro | neutro | neutro | neutro | **neutro** (lacuna no segmento pequeno não testada) | neutro | neutro | **confirma parcialmente** (capital vai para onde ARPU é alto, não para o segmento do operador) |
| Inspira migra de "alto padrão" para autônomos/pequenos — só agora | neutro | fraco sinal de ARPU baixo no segmento-alvo | neutro | neutro | neutro | neutro | neutro | **confirma** (segmento do operador é tratado como expansão tardia, não tese primária) |
| 64% dos advogados ganham até R$6,6mil/mês | neutro | **sinaliza teto de willingness-to-pay baixo** | neutro | neutro | neutro | neutro | neutro | neutro |
| Preço Astrea R$209-1.249/mês; Projuris a partir de R$49/mês | neutro | **fornece benchmark de ARPU** (compatível com faixa R$50-300 da H2, mas Astrea sobe rápido para R$379+) | neutro | neutro | neutro | neutro | neutro | neutro |
| Números de "quantas legaltechs existem" inconsistentes (400/1.000/1.500) | neutro | neutro | neutro | neutro | neutro | neutro | neutro | **confirma indiretamente** — "mercado mostra atividade" é usado como prova frouxa de oportunidade; a própria contagem não é confiável |
| Nenhum caso nomeado de fracasso de legaltech encontrado | — | — | — | — | — | — | — | gap — não confirma nem refuta a premissa da antítese do P0 |

---

## 4. Lacunas (o que NÃO foi encontrado)

1. **Nenhum dado TAM/SAM confiável e atualizado (Tier 1) para "mercado de software jurídico para advogados autônomos/pequenos escritórios no Brasil"** especificamente — todos os números encontrados são ou genéricos demais (mercado jurídico R$50bi, 2017) ou de relatórios pagos com metodologia opaca (Grand View, US$58,7M).
2. **PDF do Radar AB2L não foi acessado** (404 na página-índice) — o dado primário/oficial de contagem de legaltechs por categoria continua não verificado nesta leva.
3. **Nenhum caso nomeado de legaltech brasileira que fechou/faliu** foi encontrado — não valida nem invalida a suposição da antítese do P0 de que "legaltechs morrem por distribuição/economia, não por tecnologia". Fontes tentadas (busca genérica) não bastaram; provavelmente exigiria Crunchbase, LinkedIn de ex-fundadores, ou fóruns — fora do escopo desta leva de WebSearch.
4. **Nenhuma rodada de investimento identificada com tese explícita em "advogado autônomo/pequeno escritório" como segmento primário** — todo o capital de risco visível mira ou empresas grandes (Enter) ou não declara segmento (NetLex, Lexter.ai).
5. **CAC de canais de aquisição para o segmento-alvo não foi coberto nesta frente** (pertence mais à frente de distribuição/GTM, mas nenhum dado cruzado apareceu aqui).
6. **Churn e retenção de software jurídico brasileiro** — não encontrado nenhum benchmark numérico.

---

## 5. Sem fonte — impressão do coletor (não usar como evidência)

- A dispersão dos números de "quantas legaltechs existem" (400 vs 1.000 vs 1.500) tem cheiro de cada fonte contando coisas diferentes (membros de associação vs. startups formalmente registradas vs. menções de imprensa) — nenhuma reconciliação foi tentada pelas fontes, e nenhuma delas cita metodologia de contagem.
- A "corrida" de Jusbrasil para tornar IA generativa uma feature gratuita da base parece, por padrão de mercado observado em outros SaaS verticais (não verificado para o caso jurídico brasileiro especificamente), o movimento típico de incumbente com dados proprietários reagindo à ameaça de comoditização de LLM — coerente com a lógica da AH1 do P0, mas isso é inferência de padrão, não fato verificado nesta coleta.

---

## 6. Leitura consolidada para o Gate 1→2

Esta frente **não refuta nenhuma das 5 hipóteses decisórias diretamente por ausência de dado no segmento-alvo do operador (advogado autônomo/pequeno escritório)** — mas produz dois achados que **pressionam fortemente H4** (Jus IA gratuito e em escala) e **fortalecem H7 como risco ativo, não teórico** (multas documentadas por alucinação). O achado mais robusto (Tier 1/2, triangulado) é a adoção de IA generativa já majoritária (55,1%) nos workflows candidatos de H1 — o que confirma que a *dor pelo workflow* é real, mas ao mesmo tempo confirma a AH1: a capacidade de IA per se deixou de ser diferencial, porque o maior distribuidor de dados jurídicos do país já entrega isso de graça. O "tamanho de mercado" tradicionalmente citado (R$50bi, milhões de advogados) segue sendo, como a AH2 antecipa, um número que não sobrevive ao teste de granularidade — não há SAM verificável para o nicho do operador nesta coleta.

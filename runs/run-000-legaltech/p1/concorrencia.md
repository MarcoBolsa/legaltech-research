# P1 — Concorrência · Run #0 (LegalTech Brasil)

> Coletor P1 — frente **concorrencia**. Mapa competitivo: Jusbrasil, Projuris, players de IA jurídica pós-LLM (BR e internacionais), posicionamento, pricing público, diferenciais, gaps.
> Regra dura: toda afirmação com fonte (URL + data + tier). Ausência de dado é dado. Mapeado achado→hipótese (H1–H7).
> **Nota de coleta:** buscas via WebSearch (motor não permite fixar `after:`; datas de publicação abaixo são as exibidas nos resultados/URLs, todas 2026 salvo indicação contrária — refletem o estado do mercado na data desta coleta, 2026-07-04).

---

## 1. Achados organizados por bloco

### 1.1 Incumbentes de gestão processual (management software) — pré-IA-nativa

**Jusbrasil (Jus IA)**
- Modelo: assinatura em 3 planos (Essencial, Profissional, Premium), todos agora incluem "Jus IA" sem custo adicional — commoditização deliberada da IA como feature, não produto à parte.
- Preço: plano promocional de entrada R$1,90 no 1º mês; planos anuais a partir de 12x R$58,90; JusIA app separado também com entrada R$9,90 no 1º mês. [Tier 3 — página comercial, conflito de interesse] — https://www.jusbrasil.com.br/pro (acessado 2026-07-04); https://ia.jusbrasil.com.br/planos (acessado 2026-07-04)
- Limites de uso por plano: Essencial = 30 mensagens/mês no Jus IA + 10 uploads + 10 casos com memória; Profissional = 150 mensagens/mês + 50 uploads + Doutrina ilimitada. [Tier 3] — mesmas fontes acima.
- Cobertura de dados: >90 milhões de decisões de 96 tribunais (claim do próprio Jusbrasil). [Tier 3, conflito de interesse] — https://www.jusbrasil.com.br/pro
- Anúncio de expansão do Jus IA para todos os planos: matéria ConJur, 2026-04-13. [Tier 2 — imprensa jurídica especializada] — https://www.conjur.com.br/2026-abr-13/ferramenta-de-ia-passa-a-integrar-todos-os-planos-do-jusbrasil/
- **Mapeamento:** H4 [neutro/tende a refutar] — Jusbrasil empacota IA genérica sobre acervo próprio (dado proprietário real: jurisprudência agregada), o que é justamente o tipo de fosso que H4 exige — mas para um entrante não há como replicar esse acervo. H6 [refuta parcialmente] — ao colocar IA em todos os planos a R$58,90-118/mês, Jusbrasil fecha rapidamente a lacuna de preço baixo + IA para o segmento solo/pequeno, um dos nichos-alvo do operador.

**Projuris ADV**
- +5.000 escritórios clientes (claim próprio). Preço de entrada declarado "a partir de R$197/mês" em uma fonte, mas outra fonte do mesmo domínio (blog institucional) cita "a partir de R$49/mês" para advogado autônomo — **inconsistência de preço dentro da própria fonte**, sinal de que pricing é negociado/segmentado e não public list price confiável. [Tier 3, conflito de interesse] — https://www.projuris.com.br/adv/ ; https://www.projuris.com.br/blog/software-juridico/ (acessados 2026-07-04)
- Trial gratuito de 7 dias. Módulo de IA vendido separadamente na "Projuris Store" (produto "Inteligência Artificial - Projuris ADV"), não embutido no core — modelo de add-on, diferente do Jusbrasil. [Tier 3] — https://store.projuris.com.br/products/projuris-ia-1
- **Mapeamento:** H2 [neutro] — dá um ponto de referência de ARPU (R$49–197+/mês) para benchmarking de unit economics. H6 [confirma parcialmente] — IA como add-on pago à parte sugere que Projuris não entregou IA nativa de workflow ainda no core, possível lacuna de UX AI-native.

**Astrea (Aurum)**
- Plano gratuito "Light": até 40 processos, 1 usuário.
- Plano pago voltado a autônomo/pequeno escritório: R$199/mês, com automação de tarefas, captura de publicações e relatórios. [Tier 3, conflito de interesse] — https://www.aurum.com.br/astrea/planos-e-precos/ (acessado 2026-07-04)
- Pagamento mensal pré-pago; desconto e parcelamento em até 5x no plano anual. [Tier 3] — mesma fonte.
- Aurum também vende "Themis" (outro produto com IA) — não detalhado nesta coleta.
- **Mapeamento:** H2 [confirma faixa de preço] — R$199/mês está dentro da faixa H2 estimou (R$50–300/mês). H6 [neutro] — plano gratuito "Light" é isca de aquisição que um solo founder não consegue bancar (subsidiar grátis exige capital/escala).

**Legal One (Thomson Reuters) / SAJ ADV (Softplan)**
- Legal One: alvo é médio/grande escritório; inclui BPM, financeiro, gestão de contratos, BI, e integração com Westlaw/Checkpoint (pesquisa jurídica e tributária). Não é concorrente direto do segmento solo/pequeno-escritório que H1/H5 miram. [Tier 3] — achado consolidado em https://ialocus.com.br/blog/post-sistema-advocacia-lgpd-cpj-astrea-projuris-2026.html (acessado 2026-07-04)
- SAJ ADV: integração forte com o sistema SAJ usado pelos próprios tribunais (mesma empresa, Softplan) — vantagem de integração institucional que um entrante não replica. [Tier 3] — mesma fonte.
- **Achado crítico sobre IA nos incumbentes de gestão:** "nenhum [desses sistemas] entrega IA jurídica com sigilo profissional brasileiro — quando oferecem 'IA embutida', geralmente é ChatGPT/Claude/Gemini na nuvem sem um DPA específico em português para o Art. 34 do EOAB [Estatuto da OAB]." [Tier 3, mas é observação técnica específica e verificável, não puramente comercial] — https://ialocus.com.br/blog/post-sistema-advocacia-lgpd-cpj-astrea-projuris-2026.html
- **Mapeamento:** H4 [confirma possibilidade de fosso] — se verdadeiro, "IA com contrato de confidencialidade/DPA adequado ao sigilo profissional (Art. 34 EOAB)" é um ativo defensável real e não-trivial de replicar por wrapper de prompt — mas também não é exclusivo de um solo founder (qualquer wrapper bem feito pode assinar um DPA). H7 [neutro] — a menção de sigilo profissional aponta risco de responsabilização que H7 já cobre.

### 1.2 Ferramentas de IA jurídica pós-LLM nacionais (voltadas a advogado/pequeno escritório)

| Produto | Preço declarado | Posicionamento | Fonte / tier |
|---|---|---|---|
| **Jus IA** (Jusbrasil) | Incluído nos planos R$58,90+/mês | IA generalista sobre acervo jurisprudencial próprio | Tier 3 — jusbrasil.com.br/pro |
| **ChatADV** | R$97/mês (fonte recente) vs. R$19,90/mês (fonte mais antiga citada na mesma busca) | Assistente de IA jurídica com integração WhatsApp | Tier 3, conflito — https://chatadv.com.br/ |
| **Jurídico AI** | R$127/mês | Elaboração de documentos + pesquisa jurisprudencial + "análise preditiva" combinadas | Tier 3 — citado em https://ialocus.com.br/blog/post-melhor-ia-juridica-brasil-comparativo-2026.html |
| **MinutaIA** | Não divulgado (planos "a partir de 100 interações"); menção institucional de 90 mil usuários ativos, 10 milhões de minutas geradas em <12 meses, presença em 7 tribunais e 100 procuradorias | Geração de minutas/petições no estilo do advogado, aprende "voz jurídica" individual | Tier 3, conflito — minutaia.com.br; direitonews.com.br 2026-02 (Tier 2, imprensa) |
| **IMUTA** | R$149 por caso (preço fixo por caso, não assinatura) | Análise de caso + geração de petição + instruções de protocolo + acompanhamento + "Kit Audiência" | Tier 3 — https://imuta.ai/ |
| **Turivius / GPTuri** | Não divulgado publicamente (recomendação de demo) | IA generativa sobre base própria de jurisprudência e jurimetria; entrega "produtos estruturados" (pareceres, quadros comparativos, análises de risco) com citação auditável | Tier 3, conflito — turivius.com |
| **LinkLei** | Não divulgado nesta coleta | Software "feito para a advocacia autônoma" — Google Drive, assinatura DocuSign ilimitada, geração de documentos com IA, organização por caso | Tier 3 — linklei.com.br |

- Faixa consolidada de preço (blog terceiro, sem conflito comercial direto mas ainda promocional de categoria): "ferramentas na faixa de R$100–500/mês entregam o melhor custo-benefício para escritórios pequenos e médios." [Tier 3] — citado em múltiplas fontes agregadoras (ialocus.com.br)
- **Mapeamento:** H1 [confirma parcialmente] — a proliferação de players especificamente vendendo para "advocacia autônoma"/pequeno escritório (ChatADV, LinkLei, Jurídico AI) é evidência indireta de que existe demanda paga real nesse segmento — mas todos são Tier 3/comercial, nenhum dado independente de receita, retenção ou churn foi encontrado. H4 [tende a refutar] — a maioria descrita ("gera minuta", "responde no WhatsApp", "organiza por caso") é replicável com ChatGPT/Claude + prompt + upload de documento; o diferencial declarado (acervo próprio de jurisprudência com citação auditável) só aparece claramente em Jusbrasil e Turivius, que têm bases de dados proprietárias — não em ChatADV/Jurídico AI/LinkLei, que parecem wrappers de UX sobre LLM genérico.

### 1.3 Player nacional de IA jurídica que rompeu a categoria "pequeno/solo" — ENTER

- Fundada em 2023 por ex-founders de Wildlife Studios (Mateus Costa-Ribeiro, Michael Mac-Vicar, Henrique Vaz). Foco: **contencioso de massa** para grandes empresas/bancos (Latam, Mercado Livre, Magazine Luiza, Santander, Itaú citados como clientes). Não é concorrente direto do segmento solo/autônomo — é validação de mercado adjacente (grande empresa, não advogado autônomo). [Tier 2/3 misto] — https://www.getenter.ai/en ; https://exame.com/negocios/enter-como-uma-startup-brasileira-de-ia-atraiu-us-55-milhoes-da-sequoia/ (Tier 2, imprensa de negócios)
- Captação: Series A de R$200 milhões liderada por Founders Fund e Sequoia Capital (2025), valuation declarado de R$2 bilhões; fontes mais recentes (Forbes Brasil, 2026-05) citam nova rodada de US$100 milhões liderada por Founders Fund elevando a "unicórnio" (>US$1bi). Múltiplas fontes convergem no valor da rodada Series A mas divergem no valuation exato (R$2bi vs. "US$1,2 bilhão" citado por outra fonte) — **sinal de ruído/hype de imprensa, não dado auditado**. [Tier 2, mas divergência entre fontes = baixa confiabilidade do número exato] — https://forbes.com.br/forbes-money/2026/05/... ; https://businessmoment.com.br/...
- Tecnologia: "agentes autônomos de IA" que leem petições, analisam áudio/vídeo, interpretam documentos e escrevem defesas completas — não uma ferramenta de "assistência" (o modelo H3 do run pressupõe produto que assiste, não substitui).
- **Mapeamento:** H2 [confirma que capital de risco entra pesado no setor] — mas ENTER valida o segmento oposto ao do operador (contencioso de massa corporativo, capital intensivo, não fundador solo). H4 [confirma que fosso de dados/integração de workflow é o que atrai capital de risco pesado] — reforça que o "wrapper puro" não é o que capta capital. H6 [neutro para o segmento solo] — ENTER não compete no segmento-alvo do run (advogado autônomo/pequeno escritório), mas mostra o teto de sofisticação técnica que markets de nicho adjacente já atingiram, subindo a régua de expectativa de "IA jurídica boa" no imaginário do comprador.

### 1.4 Players internacionais operando/anunciando no Brasil

- **Harvey AI**: site em português (harveyai.com.br) com mensagem "a próxima evolução da inteligência jurídica brasileira" e lista de espera — ainda não é produto totalmente lançado/precificado publicamente no Brasil nesta coleta. [Tier 3] — https://www.harveyai.com.br/ (acessado 2026-07-04). Site institucional global (harvey.ai) foca em "legal and professional services" para grandes escritórios/empresas — não é produto para advogado autônomo.
- **CoCounsel (Thomson Reuters, ex-Casetext)**: Thomson Reuters pagou US$650 milhões pela aquisição da Casetext e rebrand para CoCounsel. [Tier 2 — valor de aquisição é fato de mercado amplamente noticiado, mas fonte específica desta busca era um agregador Tier 3] — citado em https://skywork.ai/skypage/pt/caseway-ai-law-analysis/... — **recomenda-se validação Tier 1/2 direta (imprensa financeira) antes de citar o valor em documento final.**
- Não foi encontrado pricing público de Harvey ou CoCounsel para o mercado brasileiro — ambos operam em modelo enterprise sales (cotação sob consulta), tipicamente inacessível a advogado autônomo/pequeno escritório tanto por preço quanto por modelo de venda (contrato corporativo, não self-serve).
- **Mapeamento:** H4 [confirma] — Harvey/CoCounsel competem no segmento oposto (grandes escritórios, contratos enterprise), não pressionam diretamente o segmento solo — mas definem o "estado da arte" que poderia comoditizar-se e descer de preço no futuro (risco futuro para o fosso do operador, não achado presente). H6 [confirma] — nenhum player internacional big-ticket está atendendo o segmento solo/pequeno no Brasil — lacuna aberta nesse extremo do mercado, mas ocupada por Jusbrasil/ChatADV/Jurídico AI/MinutaIA no lado nacional (ver 1.2).

### 1.5 Regulação — OAB e uso de IA (cruza com H3, mas achado é de concorrência/posicionamento, não jurídico puro)

- **Recomendação OAB nº 001/2024** (Conselho Federal da OAB), estrutura em 4 pilares: Legislação Aplicável, Confidencialidade e Privacidade, Prática Jurídica Ética, Comunicação sobre Uso de IA Generativa. Exige **formalização por escrito e consentimento expresso do cliente** antes de usar IA; advogado permanece integralmente responsável pelo conteúdo mesmo usando IA. [Tier 1 — documento oficial do CFOAB] — https://www.oab.org.br/noticia/62711/confira-versao-final-da-recomendacao-do-cfoab-sobre-o-uso-de-ia-na-pratica-juridica (aprovada nov/2024, buscada 2026-07-04)
- Uma fonte de imprensa (Tier 3, agregador) cita "recomendações aprovadas em fevereiro de 2025" — **não confirmado diretamente**; o documento oficial localizado é de nov/2024 (Recomendação 001/2024). Registrar como possível imprecisão de data em fonte secundária — recomenda-se ao pilar jurídico (H3) validar a data exata e se houve atualização posterior em 2025.
- **Mapeamento:** H3 [neutro para concorrência, mas achado-ponte relevante] — a recomendação já formaliza que **advogados** que usam IA precisam de consentimento do cliente e mantêm responsabilidade — isso não impede um não-advogado de vender a ferramenta B2A (o dever recai sobre quem contrata/usa, não sobre o fornecedor de software), mas cria fricção adicional de compliance que qualquer legaltech de IA vendendo para advogados terá de endereçar no produto (ex.: gerar termo de consentimento do cliente final como feature). Isso é achado de **produto/posicionamento** (nenhum concorrente mapeado divulga publicamente ter essa feature de compliance embutida) — possível diferencial de H6.

### 1.6 Adoção de mercado e satisfação — dados conflitantes (registrar a tensão, não resolver)

- Fonte A (Tier 3, agregador citando dado não identificado na origem): "47% dos escritórios de advocacia já adotaram soluções de IA... uso de IA generativa saltou de 37% em 2024 para 80% em 2025, entre escritórios com mais de 700 advogados o índice chegou a 100%." — https://andrebadini.com/legal-tech-em-2026-... (Tier 3, não cita fonte primária da pesquisa)
- Fonte B (Tier 3, outro agregador): "mais de 55% dos advogados brasileiros já usam alguma solução baseada em IA no dia a dia profissional." — fonte da mesma busca sobre Harvey/CoCounsel, sem citação primária.
- Fonte C (Tier 3, cita "pesquisa OAB/SP" mas sem link direto ao documento): "73% dos escritórios com mais de 5 advogados usam algum software de gestão, mas apenas 31% consideram que a ferramenta atende plenamente suas necessidades"; e, na mesma busca, "mais de 70% dos profissionais jurídicos no país nunca usaram [plataformas de legaltech]." — https://www.migalhas.com.br/depeso/264893/10-sinais-que-seu-software-juridico-nao-vai-bem e fontes agregadas da mesma busca.
- **Tensão relevante:** os números de adoção variam de "37-100% adotou IA generativa" (headline otimista, provavelmente puxada por escritórios grandes) a "70% nunca usou legaltech" (headline pessimista, sem fonte primária localizada). Nenhuma das duas foi confirmada contra fonte primária (survey original nomeado, metodologia, N amostral). **Tratar como não-confiável até验证 Tier 1/2 direto** (ex.: relatório original da AB2L, FGV ou OAB/SP citado por nome e link).
- **Mapeamento:** H1 [não resolve, registrar como lacuna] — a dispersão entre "quase todo mundo já usa IA" e "70% nunca usou nada de legaltech" é sintoma de que a pesquisa de mercado sobre adoção real no segmento solo/pequeno (o alvo do run) **não foi encontrada em fonte primária** nesta coleta. É a lacuna mais crítica para H1 — sem ela, "dor paga" fica só inferida pela existência de produtos pagos no mercado, não confirmada por dado de adoção populacional.

### 1.7 Falência/descontinuação de legaltechs — não encontrado

- Busca dedicada a legaltechs brasileiras que fecharam/faliram **não retornou nenhum caso nomeado**. Os resultados só trouxeram material institucional sobre o crescimento do setor (AB2L saltou de ~100 para +600 startups associadas em <6 anos; ~400 legaltechs estimadas no Brasil em 2025). [Tier 3] — https://ab2l.org.br/ e agregados.
- **Registrar como ausência de dado, não como "não existe mortalidade"** — o padrão de busca em português pode não capturar casos (fechamentos raramente viram notícia no Brasil); tentar em fontes Tier 2 mais direcionadas (Crunchbase, LinkedIn de founders, ou entrevistas específicas) fica como lacuna para P1 canal-de-aquisição (H5) ou pesquisa dedicada futura.
- **Mapeamento:** H6 [não resolve] — a hipótese H6 pergunta se há lacuna ocupável antes de os incumbentes fecharem; não encontrar casos de fechamento **não confirma nem refuta** — é ausência de evidência, não evidência de ausência. Registrar como gap.

---

## 2. Tabela de Fontes (URL · data · tier)

| # | Fonte | Data (acesso/publicação) | Tier | Conflito de interesse |
|---|---|---|---|---|
| 1 | jusbrasil.com.br/pro | 2026-07-04 (acesso) | 3 | Sim — página comercial própria |
| 2 | ia.jusbrasil.com.br/planos | 2026-07-04 (acesso) | 3 | Sim |
| 3 | conjur.com.br/2026-abr-13/... (Jus IA todos os planos) | 2026-04-13 (publicação) | 2 | Não (imprensa jurídica especializada) |
| 4 | projuris.com.br/adv/ | 2026-07-04 (acesso) | 3 | Sim |
| 5 | projuris.com.br/blog/software-juridico/ | 2026-07-04 (acesso) | 3 | Sim |
| 6 | store.projuris.com.br/products/projuris-ia-1 | 2026-07-04 (acesso) | 3 | Sim |
| 7 | aurum.com.br/astrea/planos-e-precos/ | 2026-07-04 (acesso) | 3 | Sim |
| 8 | ialocus.com.br/blog/post-sistema-advocacia-lgpd-cpj-astrea-projuris-2026.html | 2026 (não datado precisamente) | 3 | Parcial (blog agregador comercial de categoria) |
| 9 | ab2l.org.br | 2026-07-04 (acesso) | 2 | Não (associação setorial — fonte primária do próprio setor, mas com interesse institucional em mostrar crescimento) |
| 10 | ab2l.org.br/noticias/mercado-de-lawtechs-no-brasil/ | não datado precisamente | 2 | Idem acima |
| 11 | harveyai.com.br | 2026-07-04 (acesso) | 3 | Sim |
| 12 | skywork.ai/skypage/pt/caseway-ai-law-analysis/... (menção aquisição Casetext) | não datado precisamente | 3 | Não direto, mas fonte agregadora sem citação primária |
| 13 | getenter.ai/en | 2026-07-04 (acesso) | 3 | Sim |
| 14 | exame.com/negocios/enter-como-uma-startup... | não datado precisamente (2025 pelo conteúdo) | 2 | Não (imprensa de negócios) |
| 15 | forbes.com.br/forbes-money/2026/05/... (ENTER unicórnio) | 2026-05 (publicação) | 2 | Não |
| 16 | businessmoment.com.br/... (ENTER aporte US$1,2bi) | não datado precisamente | 3 | Não, mas fonte de menor rigor editorial, diverge de Forbes no valuation |
| 17 | minutaia.com.br | 2026-07-04 (acesso) | 3 | Sim |
| 18 | direitonews.com.br/2026/02/minutaia-atinge-10-milhoes... | 2026-02 (publicação) | 2 | Não (mas tom de release de imprensa da própria empresa) |
| 19 | imuta.ai | 2026-07-04 (acesso) | 3 | Sim |
| 20 | turivius.com | 2026-07-04 (acesso) | 3 | Sim |
| 21 | chatadv.com.br | 2026-07-04 (acesso) | 3 | Sim |
| 22 | linklei.com.br | 2026-07-04 (acesso) | 3 | Sim |
| 23 | oab.org.br/noticia/62711/... (Recomendação CFOAB 001/2024) | 2024-11 (aprovação) | 1 | Não — documento oficial do órgão regulador |
| 24 | migalhas.com.br/depeso/264893/10-sinais... | não datado precisamente | 3 | Não, mas cita estatística OAB/SP sem link primário — checar |
| 25 | andrebadini.com/legal-tech-em-2026-... | 2026 (não datado precisamente) | 3 | Não, mas sem fonte primária para os % de adoção citados |

---

## 3. Mapa achado → hipótese (síntese)

| Hipótese | Confirma | Refuta | Neutro/parcial |
|---|---|---|---|
| **H1** (dor paga específica) | Proliferação de produtos pagos mirando solo/pequeno (ChatADV, Jurídico AI, LinkLei, MinutaIA) sugere dor paga real | — | Dado de adoção populacional é conflitante e sem fonte primária (1.6) — não dá para confirmar tamanho/intensidade da dor |
| **H2** (economia fecha p/ solo) | Faixa de preço observada R$49–500/mês bate com a faixa H2 estimou; Astrea R$199/mês é dado concreto de ARPU alcançável | — | Nenhum dado de CAC real encontrado nesta frente (é escopo de outra frente do P1) |
| **H3** (permissão legal não-advogado) | Recomendação OAB 001/2024 recai sobre o *advogado-usuário*, não sobre o fornecedor de ferramenta — compatível com modelo B2A do run | — | Data exata (nov/2024 vs. fev/2025 citada por fonte secundária) precisa validação pelo pilar jurídico dedicado |
| **H4** (fosso além do LLM cru) | Jusbrasil e Turivius têm acervo jurisprudencial proprietário real (fosso genuíno); Harvey/CoCounsel mostram que capital pesado busca fosso de dado+integração, não wrapper | ChatADV/Jurídico AI/LinkLei parecem wrappers de UX sobre LLM genérico — replicáveis | — |
| **H5** (canal de aquisição outsider) | — | — | Nenhum achado direto nesta frente (fora de escopo — ver frente "canal/GTM" do P1) |
| **H6** (lacuna ocupável por solo) | Nenhum incumbente de gestão (Astrea/Projuris/Legal One/SAJ) mostrou IA nativa com compliance de consentimento do cliente (feature de produto ainda inexplorada); nenhum player internacional (Harvey/CoCounsel) atende o segmento solo no BR | Jusbrasil já colocou IA em **todos** os planos a partir de ~R$59/mês — fecha rapidamente a lacuna de "IA barata para autônomo" | Ausência de casos de fechamento de legaltech não confirma nem refuta ocupabilidade — é gap de dado |
| **H7** (limiar de confiabilidade aceito) | — | — | Menção a sigilo profissional e responsabilização (OAB 001/2024, Art. 34 EOAB) reforça que o risco de responsabilização já é reconhecido formalmente — cruza com H7 mas não foi o alvo desta frente |

---

## 4. Lacunas (o que NÃO foi encontrado)

1. **Nenhum dado primário/independente (Tier 1/2) de adoção real de IA no segmento solo/pequeno escritório** — todos os números de adoção (37-100%, 55%, 47%, 70% nunca usou) vêm de agregadores Tier 3 sem citação de survey original nomeado. Prioridade alta para P1 (frente "demanda"/H1).
2. **Nenhum caso nomeado de legaltech brasileira que fechou/faliu** — busca não retornou nenhum exemplo concreto, apesar de o mercado ter ~400+ players (estatisticamente improvável que zero tenha fechado). Sinal de que a busca em português não captura isso facilmente — recomenda-se tentar Crunchbase/LinkedIn ou entrevistas de fundadores na frente de canal (H5/H6).
3. **Pricing público de Harvey AI e CoCounsel no Brasil** — ambos operam em modelo enterprise/lista de espera, sem tabela de preço pública encontrada. Não dá para benchmarking direto de ARPU internacional aplicado ao BR.
4. **Dados de churn/retenção de qualquer concorrente** — nenhuma fonte (nem Tier 3) divulgou métricas de churn ou LTV. Necessário para H2, mas típico de não ser público — provavelmente só via entrevista de fundador (fora do escopo deste run, conforme §5 do P0).
5. **Confirmação da data exata da Recomendação OAB sobre IA** — documento oficial localizado é de nov/2024 (Recomendação 001/2024); uma fonte secundária cita "fevereiro de 2025" sem que se tenha encontrado um documento distinto dessa data. Repassar ao pilar jurídico (H3) para validação Tier 1 direta no diário eletrônico da OAB.
6. **Nenhum concorrente mapeado divulga publicamente feature de "consentimento do cliente para uso de IA" como parte do produto** — pode ser lacuna real de produto (H6) ou pode simplesmente não ser destacado em material de marketing; não dá para diferenciar com a evidência coletada.
7. **Valor exato da rodada/valuation da ENTER diverge entre fontes** (R$2bi vs. "US$1,2 bilhão"/">US$1bi") — nenhuma fonte Tier 1 (ex. registro CVM, press release oficial da própria ENTER) foi consultada nesta coleta; tratar os números como direcionais, não exatos.

---

## 5. Sem fonte — impressão do coletor (não usar como evidência)

- A concentração de players de IA jurídica brasileira em "gerar minuta/petição via chat" (ChatADV, Jurídico AI, MinutaIA, IMUTA) sugere que esse é o job-to-be-done mais fácil de vender e mais fácil de copiar — o que é coerente com a preocupação de AH1 do P0 (commoditização). Isso é leitura interpretativa do coletor, não um fato coletado — merece teste direto contra H4/H7 no P2.
- O fato de nenhum concorrente ter divulgado publicamente métricas de acurácia/alucinação em citação de jurisprudência (o risco central de H7) pode ser porque ninguém audita isso publicamente — ou porque é um ponto fraco que preferem não expor. Não dá para saber qual, com os dados coletados.

---

*P1 (frente concorrência) concluído. 25 fontes catalogadas — ver tabela §2 para contagem por tier.*

# P0 — Epistemologia · Run #0 (LegalTech Brasil)

> **Papel metodológico:** Sackett (hierarquia de evidência) + Creswell (desenho de pesquisa).
> Regra do pilar: **hipótese que não pode morrer não é hipótese** — é esperança. Cada H abaixo tem uma condição concreta de falseamento.
>
> **Operador:** empreendedor solo, **não-advogado**, avaliando *se* e *como* entrar no mercado legaltech brasileiro com um produto de IA.
> **Domínio:** Tecnologia jurídica (LegalTech) — Brasil.
> **Tiers de evidência (RILP):** Tier 1 = peer-reviewed, reguladores (OAB, CNJ), lei, jurisprudência, pesquisa independente · Tier 2 = analistas vendor-neutral, associações setoriais (AB2L, FGV), conferências · Tier 3 = blogs de fornecedor / material comercial (*tag obrigatória: conflito de interesse*).

---

## 1. Tese Central (falsificável como conjunto)

**Um empreendedor solo, não-advogado, consegue entrar no mercado brasileiro de tecnologia jurídica (legaltech) com um produto de inteligência artificial e construir um negócio viável? Especificamente: existe um problema jurídico recorrente e caro o suficiente — em advogados autônomos e pequenos escritórios — que eles já pagariam por uma ferramenta de IA que o resolva; é legalmente permitido a um não-advogado construir e vender essa ferramenta no Brasil; e é possível criar algo defensável e distribuível por um fundador solo, sem que grandes players (Jusbrasil, Thomson Reuters/Legal One, Softplan/SAJ, Projuris, Astrea) ou o próprio ChatGPT/Claude genérico tornem o produto irrelevante? Mapeie a demanda real, as barreiras regulatórias da OAB, os concorrentes e as lacunas, a economia do negócio (quanto o cliente paga, custo de aquisição, payback) e os canais de aquisição viáveis para um outsider — e conclua se e como vale a pena entrar.**

A tese só sobrevive se **as cinco hipóteses decisórias (H1–H5) forem confirmadas**. Basta **uma** decisória refutada para o conjunto cair — e o veredito vira "não entrar" ou "entrar apenas sob a condição que a refutação impõe".

---

## 2. Processo Dialético (tese → antítese → síntese)

| Momento | Conteúdo |
|---|---|
| **Tese** | "Tenho IA e o mercado jurídico brasileiro é gigante, litigioso e atrasado em tecnologia — logo há uma oportunidade óbvia para um produto de IA." |
| **Antítese** | O mercado grande não é servível por inteiro; a IA generativa está virando commodity (o cliente pode usar ChatGPT de graça); a OAB regula quem pode operar sobre serviço jurídico; os incumbentes já detêm distribuição e dados; e um não-advogado carrega desvantagem de credibilidade e canal. Legaltechs que morreram no BR raramente morreram por falta de tecnologia — morreram por falta de distribuição, por economia que não fechava, ou por resolver dor que ninguém pagava. |
| **Síntese** | A oportunidade real (se existir) **não está na IA em si**, e sim na interseção estreita de: (a) uma dor específica, recorrente e já-paga de um segmento alcançável; (b) um posicionamento regulatório legal para um não-advogado (ferramenta que *assiste*, não *substitui* o advogado); (c) um ativo defensável além do LLM (dados proprietários, integração com PJe/tribunais, lock-in de workflow); e (d) um canal de aquisição que não dependa de credibilidade de insider. O run testa se essa interseção existe e é grande o bastante — não se "há mercado". |

---

## 3. Hipóteses Falsificáveis (H1–H7)

> Legenda de criticidade: **Decisória** = se refutada, muda o veredito go/no-go do run. **Secundária** = molda produto/estratégia, mas não mata a entrada sozinha.

### H1 — Existe dor recorrente, específica e já-paga (não dor difusa)
**Enunciado:** Existe pelo menos **um** workflow jurídico específico e de alta frequência (candidatos: triagem/análise de documentos e contratos, elaboração de peças, gestão de prazos processuais, busca de jurisprudência) cuja dor, para advogados autônomos e pequenos escritórios (≈2–10 anos de atuação), é severa o bastante para que eles **já paguem por ferramentas** ou a citem espontaneamente entre suas 3 maiores dores.
**O que a REFUTA:** A pesquisa não encontra nenhum workflow em que o segmento-alvo (i) já pague por solução pontual **ou** (ii) verbalize a dor no top-3 — a dor aparece só como "seria bom ter", difusa, baixa frequência, ou resolvida a contento pelo estagiário/status quo.
**Critérios de evidência:** Tier 2 (surveys AB2L/FGV, reviews de ferramentas existentes com volume, job posts pedindo a solução) triangulado com Tier 1/2 (relatórios de mercado independentes) e vocabulário literal de fóruns/Reddit/grupos (sinal, não prova). Dor **paga** > dor **declarada**.
**Criticidade:** **Decisória** — sem dor paga não há mercado, só hipótese de mercado.

### H2 — A economia fecha para um fundador solo
**Enunciado:** O segmento-alvo paga um preço recorrente de SaaS (faixa a validar, ~R$50–300/mês) suficiente para que o LTV supere o CAC alcançável pelos canais disponíveis a um outsider, com payback em prazo tolerável para quem não tem capital de risco (indicativo: ≤12 meses).
**O que a REFUTA:** Benchmark mostra ARPU do segmento baixo demais e/ou CAC pelos canais viáveis (conteúdo/SEO, comunidades, parcerias) maior que o LTV; ou os incumbentes revelam teto de preço e churn que tornam a matemática de fundador solo impossível (queima até morrer — princípio §3 do RILP).
**Critérios de evidência:** Tier 2 (benchmarks de unit economics de SaaS B2B jurídico, ticket médio setorial) + Tier 3 tagueado (páginas de preço de concorrentes) + Tier 1/2 sobre CAC de canais no BR. Claim de economia exige triangulação — é gate bloqueador (G4→5) lá na frente.
**Criticidade:** **Decisória.**

### H3 — É legalmente permitido a um NÃO-advogado construir e vender a ferramenta
**Enunciado:** Um não-advogado pode legalmente desenvolver, ser dono e comercializar uma **ferramenta** de legaltech com IA para advogados no Brasil, sem configurar exercício ilegal da profissão (Lei 8.906/94) nem violar normas da OAB, desde que o produto **assista** o julgamento do advogado e não o **substitua** nem preste serviço jurídico ao consumidor final.
**O que a REFUTA:** OAB/estatuto/jurisprudência mostram que a categoria de produto pretendida exige titularidade/registro de advogado, ou que a entrega de output de IA como aconselhamento jurídico gera responsabilidade que um não-advogado não pode assumir; ou há precedente de enforcement (autuação, ação) contra ferramenta jurídica operada por não-advogado. Se a permissão depender de o produto ser B2A (para advogado) e nunca B2C (para leigo buscando direito), isso **restringe** o escopo — refutação parcial que redefine o produto.
**Critérios de evidência:** **Tier 1 obrigatório** — Estatuto da Advocacia (Lei 8.906/94), Provimentos da OAB (ex.: publicidade/205-2021), Resoluções do CNJ sobre IA no Judiciário, e jurisprudência (usar MCP Jurisprudências.ai). Nada de Tier 3 aqui.
**Criticidade:** **Decisória** — é um gate go/no-go jurídico, não um risco a mitigar depois.

### H4 — Existe defensabilidade além do LLM cru (não é wrapper)
**Enunciado:** É possível construir um fosso durável — dados proprietários, integração profunda com sistemas dos tribunais brasileiros (PJe, e-SAJ, Projudi), lock-in de workflow, ou distribuição — de modo que um usuário genérico de ChatGPT/Claude **não** consiga replicar o valor central com prompt + dados públicos.
**O que a REFUTA:** O job-to-be-done escolhido é integralmente atendido por LLM genérico + fontes públicas, e toda a "diferenciação" se reduz a engenharia de prompt copiável em uma tarde; nenhum ativo proprietário ou barreira de integração é identificável.
**Critérios de evidência:** Tier 2 (teardown de concorrentes, análise de fossos de dados em SaaS vertical) + Tier 1 sobre commoditização de LLM e valor de dados proprietários. Testar contra o baseline: o que o deep research nativo **já entrega** define o piso de commodity.
**Criticidade:** **Decisória** — wrapper de IA sem ativo próprio não sobrevive a um ciclo de preço dos provedores de modelo.

### H5 — Existe canal de aquisição alcançável por um outsider não-advogado
**Enunciado:** Há pelo menos **um** canal escalável e barato pelo qual um fundador de fora da advocacia consegue adquirir advogados-clientes (conteúdo/SEO jurídico, comunidades como AB2L/eventos OAB, parcerias com contadores/sistemas, marketplaces) sem que a credibilidade de insider seja bloqueador intransponível.
**O que a REFUTA:** A pesquisa mostra que a compra de software por advogados é fortemente gated por indicação/confiança entre pares e por status de insider, e nenhum outsider teve sucesso por canais frios; ou o CAC nesses canais abertos é proibitivo (conecta com H2).
**Critérios de evidência:** Tier 2/3 (estudos de caso de GTM de legaltechs brasileiras, entrevistas com fundadores, análise da base AB2L) triangulado. Casos de **falha** de distribuição valem tanto quanto os de sucesso.
**Criticidade:** **Decisória** — produto sem canal é hobby, não negócio; e o não-advogado carrega esse risco de forma aguda.

### H6 — Há lacuna deixada pelos incumbentes, ocupável por um solo antes de fechar
**Enunciado:** Os dominantes (Jusbrasil, Projuris, Astrea, Legal One/Thomson Reuters, SAJ/Softplan, ADVBOX) deixam uma lacuna real — segmento, workflow, faixa de preço ou UX AI-native — que um fundador solo consegue ocupar antes de os incumbentes a fecharem.
**O que a REFUTA:** Os incumbentes já entregam features de IA críveis cobrindo o workflow-alvo, no segmento e preço-alvo; ou fechar a lacuna exige capital/escala/integrações que um solo não consegue mobilizar (a lacuna existe mas não é ocupável por um solo).
**Critérios de evidência:** Tier 2/3 (mapa competitivo, changelogs, reviews de produto, roadmaps públicos). Distinguir "lacuna que existe" de "lacuna ocupável por solo".
**Criticidade:** **Secundária** — a lacuna é iterável e o posicionamento é ajustável; refuta o *como*, não o *se*.

### H7 — O limiar de confiabilidade de IA no workflow escolhido é tecnicamente atingível e aceito
**Enunciado:** Os advogados-alvo adotam output de IA no workflow escolhido apenas acima de um limiar de precisão/confiabilidade, e esse limiar é atingível com LLM + retrieval sobre corpora jurídicos brasileiros — sem que o risco de alucinação (ex.: citação de jurisprudência inexistente) ou a responsabilidade profissional inviabilizem o uso.
**O que a REFUTA:** O workflow exige acurácia que LLM+RAG atual não atinge de forma confiável (alucinação de citação é o caso crítico), **ou** advogados rejeitam IA naquele workflow independentemente da acurácia, por medo de responsabilização; ou o CNJ/OAB restringe o uso naquele contexto.
**Critérios de evidência:** Tier 1 (estudos sobre acurácia/alucinação de LLM em tarefas jurídicas, posição CNJ/OAB sobre IA) + Tier 2 (surveys de adoção de IA no setor jurídico BR).
**Criticidade:** **Secundária** — é risco de execução endereçável pela escolha do workflow (escolher tarefa tolerante a erro assistido, não tarefa que exige precisão absoluta autônoma).

---

## 4. Anti-Hipóteses — as 2 crenças mais perigosas a DERRUBAR primeiro

> São os priores que o operador provavelmente já carrega e que, se falsos e não confrontados cedo, contaminam todo o run. A pesquisa deve **atacá-las primeiro**, não confirmá-las.

### AH1 — "A IA é o meu diferencial" *(cegueira à commoditização)*
A crença de que *ter IA* já constitui vantagem competitiva. É perigosa porque a capacidade de IA está virando commodity distribuída de graça (o próprio cliente e qualquer concorrente têm acesso ao mesmo modelo). Se verdadeira, o fosso é o modelo; se falsa (hipótese de trabalho: **é falsa**), o fosso tem de estar em dados, integração, workflow ou distribuição — e o run precisa provar que esse fosso existe (**H4**). **Alvo primário de falseamento:** mostrar quanto do valor pretendido o baseline de deep research nativo / ChatGPT genérico **já entrega grátis**. O que sobra acima disso é o único produto real.

### AH2 — "O mercado é gigante e atrasado, logo a demanda é óbvia" *(falácia do TAM + insider-blindness)*
A crença de que tamanho de mercado (milhões de advogados, país hiperlitigioso) mais "atraso tecnológico" implicam demanda endereçável por um novo entrante. É perigosa por dois motivos: (1) TAM não é SAM — o servível é minúsculo perto do total, e willingness-to-pay + canal alcançável definem o negócio, não o tamanho bruto; (2) subestima que a compra jurídica é gated por confiança entre pares e que o operador, **por ser não-advogado**, começa em desvantagem de credibilidade, canal e leitura de dor. **Alvo primário de falseamento:** substituir "mercado grande" por *dor específica-paga em segmento alcançável* (**H1**) e por *canal viável para outsider* (**H5**). Se estes não fecharem, o tamanho do mercado é irrelevante.

---

## 5. Escopo Negativo — o que este run NÃO investiga

- **Não decide o produto/feature final.** O run mapeia demanda, regulação, concorrência, economia e canal; a escolha do workflow e do MVP é consequência dos artefatos do P2, não input do P0.
- **Não faz entrevistas de campo com ICP.** Isso é o gate G5→6 (P5). Aqui só evidência documental/secundária (Tiers 1–3). "Eu acho que eles querem X" e "5 advogados disseram Y" não pertencem a este run.
- **Não constrói nem prototipa software.** Nenhuma linha de código, integração PJe real ou teste técnico de acurácia de LLM próprio — apenas evidência publicada sobre viabilidade técnica (H7).
- **Não cobre mercados fora do Brasil.** LegalTech US/EU entra só como referência de padrão/benchmark, nunca como conclusão sobre o mercado-alvo. Sem generalização cross-domain (princípio §5 do RILP: não generalizar com N=1).
- **Não modela projeção financeira detalhada nem valuation.** Unit economics entram como *benchmark de viabilidade* (H2), não como plano financeiro do negócio.
- **Não avalia estrutura societária, tributária ou de captação.** Como constituir/financiar a empresa fica fora; só a *permissibilidade regulatória* da atividade para não-advogado (H3) é escopo.
- **Não investiga o segmento de grandes escritórios / departamentos jurídicos de grandes empresas** como alvo primário, salvo se a pesquisa apontar que o segmento solo/pequeno (foco default) é inviável — aí o run registra o pivô como achado, não o persegue.

---

*P0 concluído · aguarda GATE 0→1: hipóteses falsificáveis e síntese dialética articulada? → PASS avança para P1.*

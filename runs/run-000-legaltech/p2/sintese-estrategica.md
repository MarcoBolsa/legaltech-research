# Síntese Estratégica — Entrar (ou não) em LegalTech no Brasil como Fundador Solo Não-Advogado com IA

**Run #0 · RILP v2.0 · P2 — Síntese Estratégica · 2026-07-04**
Método: 5 frentes de coleta documental (mercado, ICP/dores, concorrência, regulação, pricing) → 3 filtros obrigatórios (Tier de fonte · triangulação · bias audit) → 10 claims com score de confiança auditável → gate bloqueador G2→3.
Escopo: evidência documental secundária (Tiers 1–3), sem entrevistas de campo, sem protótipo. ~80 fontes catalogadas nas 5 frentes.

> **Como ler este documento:** cada afirmação estratégica é um *claim* rastreável (C1–C9) com veredito de hipótese, bucket de confiança (Alto/Médio/Baixo) e fontes com tier. O que **não** sabemos está tão explícito quanto o que sabemos — é o que separa esta síntese de um resumo confiante. O detalhamento numérico está em `claims.yaml`.

---

## 1. Sumário Executivo — a resposta à tese

**Veredito honesto: entrada CONDICIONAL, com o gate de evidência REPROVADO no estado atual (score 63,4%).**

A tese do Run #0 era: *um solo não-advogado consegue entrar em legaltech com IA e construir negócio viável?* Ela só sobrevive se as **cinco** hipóteses decisórias (H1 dor paga, H2 economia, H3 legalidade, H4 fosso, H5 canal) forem confirmadas. O resultado após a coleta:

| Hipótese decisória | Veredito | Confiança |
|---|---|---|
| **H3** — legal p/ não-advogado | ✅ **Confirmada** (na forma B2B; B2C morre) | 🟢 Alto |
| **H4** — fosso além do LLM | ⚠️ **Refutada na forma ampla, confirmada só no nicho vertical** | 🟢 Alto |
| **H1** — dor recorrente já-paga | ✅ **Confirmada parcial** (dor/adoção sim; workflow exato inconclusivo) | 🟡 Médio |
| **H2** — economia fecha p/ solo | ❌ **INCONCLUSIVA** — dado central (CAC/LTV/churn) ausente | 🔴 Baixo |
| **H5** — canal p/ outsider | ❌ **INCONCLUSIVA** — regulação clara, mas CAC não medido | 🔴 Baixo |

**Três das cinco decisórias fecham com confiança suficiente. Duas — economia e canal — não fecham, e não por acaso: são exatamente as que exigem dado de campo que uma pesquisa documental não pode gerar.** O gate bloqueador G2→3 reprova (score < 70% *e* dois claims decisórios em Baixo). Isso **não é** "não entrar" — é "não dá para dar sinal verde sem antes fechar a economia e o canal com dado primário".

**A oportunidade real, se existir, é estreita e nítida:** um produto **B2B** vendido ao advogado, numa **vertical única** (ex.: previdenciário/BPC-LOAS, revisional bancário, trabalhista), cobrindo o **workflow completo** (não só "gerar a peça"), com **dados proprietários lícitos** (do próprio cliente/fluxo, não scraping) e **citação verificável**, distribuído por **conteúdo de nicho + comunidade** (não mídia paga pura, não marketplace de leads). Fora desse corredor — no "mais uma IA jurídica genérica" — o espaço já está comoditizado pelo Jusbrasil de graça e é terra de morte.

**O que este run entrega acima do "mercado é grande, entre": a régua de onde a tese REALMENTE trava.** Não é regulação (resolvida), não é se há dor (há), não é se IA funciona (funciona com ressalvas). É **unit economics** e **aquisição** — e este documento aponta o dedo exatamente para lá, em vez de mascarar com otimismo.

---

## 2. Os claims e seus scores — o que sustenta cada afirmação

Ordenados por criticidade. Cada um é auditável em `claims.yaml`.

### 🟢 C1 — É legal, se for B2B (H3 · Alto · decisório)
Um não-advogado pode construir, deter e vender a ferramenta **desde que**: (a) B2B — vendida ao advogado como instrumento, (b) nunca B2C ao leigo, (c) não estime resultado/chance de processo, (d) não faça matching remunerado de clientela. A responsabilidade ético-disciplinar recai sobre o **advogado-usuário**, não sobre o fornecedor — favorável ao solo.
**Por que Alto:** três fontes Tier 1 (Lei 8.906/94, Recomendação CFOAB 001/2024, CNJ 615/2025) + precedente judicial de set/2025 (2ª Vara Federal RJ proibiu plataforma que estimava êxito e direcionava clientes) + decisão do Tribunal de Ética OAB/SP. Triangulação forte, sem conflito de interesse.
**Ressalva temporal (não de confiança):** a OAB ainda não tem *provimento vinculante* sobre IA — só Recomendação + "Plano Nacional" em elaboração. A janela é favorável, mas **móvel**: um provimento futuro pode reapertar as regras.

### 🟢 C3 — "Ter IA" não é fosso; o fosso é vertical (H4/AH1 · Alto · decisório)
O maior incumbente (Jusbrasil) embutiu o **Jus IA de graça em todos os planos**, RAG sobre 1,2 bilhão de documentos próprios, **300 mil advogados/mês**. Qualquer produto que compita no genérico ("analise este documento", "pesquise jurisprudência", "redija esta peça") enfrenta um concorrente com dados proprietários + distribuição + preço zero incremental. Wrappers de LLM (ChatADV, LinkLei, Jurídico AI) são replicáveis numa tarde.
**Consequência dura:** não basta "não ser wrapper do ChatGPT" — é preciso **não ser wrapper do Jus IA** também. Defensabilidade só existe em: nicho vertical estreito + dados proprietários lícitos + workflow ponta-a-ponta + integração. **Por que Alto:** comoditização triangulada em Tier 2 (ConJur mar/2025 e abr/2026) + survey de adoção + direção do capital de risco (Enter, Harvey/CoCounsel buscam fosso de dados, não wrapper).

### 🟢 C4 — Alucinação é risco real e materializado, mas endereçável (H7 · Alto · secundário)
Multas documentadas em 2025–2026 no **TST, TJSC, TJPR, TRT-2 e TRT-12** por citação de jurisprudência inexistente gerada por IA (R$1.200 a 20 salários-mínimos) + ofício à OAB. **Por que Alto:** três fontes oficiais de tribunal (Tier 1) convergentes entre jurisdições. **Consequência de produto:** o workflow-alvo precisa de **citação verificável/rastreável** contra base primária e deve ser tolerante a erro assistido — nunca geração livre de texto com nomes de casos. Isso é design, não bloqueio.

### 🟡 C2 — A dor é real e paga, mas o "qual workflow" fica em aberto (H1 · Médio · decisório)
**55,1%** dos profissionais de direito já usam IA generativa nos exatos workflows candidatos (documentos, peças, jurisprudência); a FGV CEPI confirma ~80% de uso e aponta o **custo** — não o desinteresse — como a barreira. Existe mercado pago (R$40–700/mês) com troca de fornecedor documentada. **Por que só Médio:** a adoção é triangulada em 3 fontes Tier 2, mas o núcleo decisório de H1 — "dor JÁ-PAGA no workflow específico + top-3 espontâneo do segmento solo" — repousa em preços de vendor (Tier 3) e **falta um survey primário recente que ranqueie as dores**. Usável com ressalva.

### 🟡 C5a — Willingness-to-pay existe na faixa (H2 · Médio · relevante)
Faixa observada: gestão R$40–220/mês, IA jurídica R$149–350/mês. O hábito de compra está estabelecido — não é preciso criá-lo, só capturá-lo. Contextualizado por dado Tier 1 (64% dos advogados ganham até R$6,6mil/mês).

### 🟡 C7 — Há lacuna, mas só na vertical (H6 · Médio · secundário)
Incumbentes de gestão + Jusbrasil cobrem o horizontal; nenhum internacional (Harvey/CoCounsel) atende o solo no BR; ninguém entrega workflow vertical completo + IA com compliance de consentimento embutido. **Mas** a lacuna **não** é ocupável no horizontal (Jusbrasil fecha "IA barata genérica" a ~R$59/mês). O pivô do Jusbrasil para B2B/B2G pode abrir espaço no solo — ou sinalizar que o solo é ruim de monetizar (ambíguo).

### 🟡 C8 — TAM não é SAM (AH2 · Médio · relevante)
1,3 milhão de advogados e "mercado jurídico de R$50bi" **não** são demanda endereçável. Legal AI BR estimado em ~US$58,7M (2030); o capital de risco mira o segmento oposto (Enter/enterprise); contagens de legaltechs são inconsistentes (400/1.000/1.500). "Mercado grande e atrasado" é prova frouxa.

### 🟡 C9 — O fosso de dados fácil (scraping) é minado pela LGPD (H4 · Médio · relevante)
A ANPD classificou web scraping como tratamento sujeito à LGPD, com fiscalização prevista; a tensão publicidade processual × LGPD é zona cinzenta (CNJ 647/2025). Fosso de dados defensável deve vir do **próprio workflow/cliente**, não de scraping massivo de PJe/diários.

### 🔴 C5b — A economia do solo NÃO está provada (H2 · Baixo · decisório) ⛔
Três pressões documentadas: (1) ticket de R$150–350 = 2–5% da renda de 64% dos advogados; (2) incumbentes praticam preço de entrada quase-gratuito (R$1,90/R$9,90/grátis-1-ano) = race-to-the-bottom; (3) **ZERO dado de CAC, churn ou LTV** do setor jurídico BR em nenhuma das 5 frentes. **Por que Baixo:** o núcleo de H2 — LTV > CAC com payback ≤12m — não tem lastro nenhum. Rebaixar para Médio seria contaminar o gate.

### 🔴 C6 — O canal para outsider NÃO foi testado (H5 · Baixo · decisório) ⛔
A regulação delimita bem o permitido (conteúdo/SEO/comunidade/diretório passivo OK; marketplace de matching perseguido pela OAB). **Mas** a viabilidade econômica — CAC real, conversão, caso de GTM frio de um não-advogado — é **não testada**; o único número de conversão (freemium ~1,4%, N=1, consultoria manual) pesa contra. O componente que mata ou salva a tese não foi medido.

---

## 3. O que foi REFUTADO — tão importante quanto o confirmado

Um deep research que só confirma é propaganda. Estas são as crenças que a coleta derrubou:

1. **"A IA é o meu diferencial" (AH1) — REFUTADA com força.** O Jusbrasil entrega IA generativa jurídica de graça a 300k advogados/mês. Ter IA é tabela-stakes, não vantagem. Quem entra vendendo "IA que escreve petição" compete contra preço zero de um incumbente com dados que não se replicam.

2. **"Mercado gigante e atrasado = demanda óbvia" (AH2) — REFUTADA.** TAM de R$50bi e 1,3M de advogados não viram SAM. O mercado de Legal AI BR é pequeno (~US$58,7M) e o capital foge do segmento solo para o enterprise.

3. **"É só fazer um wrapper de ChatGPT com prompt jurídico" — REFUTADA.** É replicável numa tarde e não sobrevive a um ciclo de preço dos provedores de modelo nem à comoditização do Jusbrasil.

4. **"Faço fosso raspando os dados públicos dos tribunais" — REFUTADA como atalho fácil (C9).** A ANPD já sinalizou fiscalização; scraping massivo é risco LGPD, não vantagem livre.

5. **"A economia fecha, com margem apertada" (afirmação do baseline de deep research nativo) — RECUSADA por falta de lastro.** O baseline nativo afirmou isso sobre **zero dado de CAC**. Este run se recusa a afirmar o que não pode provar — e essa recusa é o valor. Assumir que "fecha" é o erro que quebra fundadores solo.

6. **"Marketplace conectando advogado e cliente é o canal" — REFUTADA no plano regulatório.** É a categoria que a OAB mais persegue (20+ ações). O canal seguro é conteúdo/comunidade passiva, mais lento.

---

## 4. Recomendação estratégica acionável

**Se — e somente se — você fechar a economia e o canal com dado primário, entre. Caso contrário, não entre no genérico.**

### O corredor viável (o "bolo pronto" em t0, construído em fatias)
- **Segmento:** UMA vertical de alto volume e dor cara/repetitiva. Candidatos de maior aderência ao que a coleta sustenta: previdenciário/BPC-LOAS, revisional bancário, trabalhista de justa causa. Escolher pela combinação volume + repetibilidade + tolerância a erro assistido.
- **Produto:** workflow **completo** da vertical (captação de contexto → triagem → produção assistida → protocolo/acompanhamento), não "a peça". A defensabilidade está no fluxo inteiro + dados que se acumulam com o uso.
- **Fosso:** dados proprietários **lícitos** (do próprio cliente e do fluxo), integração e lock-in de workflow — **não** scraping. Citação sempre verificável (evita o risco H7/multa).
- **Posicionamento regulatório:** B2B explícito, "ferramenta que assiste o advogado", termos de uso que jogam a responsabilidade de supervisão para o advogado (alinhado à Recomendação OAB) e feature de consentimento do cliente embutida (lacuna de produto identificada em C7).
- **Canal:** conteúdo de nicho + comunidade + parceria com advogados-influenciadores da vertical. Nunca marketplace de leads. Nunca só mídia paga.

### Antes de escrever uma linha de código — fechar os dois decisórios abertos
Este é o próximo passo obrigatório (o gate reprovado exige):
1. **Unit economics (H2):** obter CAC/LTV/churn reais de SaaS jurídico BR — via entrevista de 2–3 fundadores do setor, ou dado privado. Meta de sobrevivência do solo: ~R$15–20k MRR = ~100–200 clientes a R$100–200/mês. Se o CAC via canal viável estourar o payback de 12m, a tese cai.
2. **Teste de canal (H5):** custo real de adquirir os 10 primeiros advogados de UMA vertical por conteúdo/comunidade. Um experimento barato antes do produto.

Fechados os dois, o score recalcula e o gate G2→3 reavalia. **Sem isso, qualquer "vá em frente" é fé, não evidência.**

---

## 5. Lacunas honestas — o que este run NÃO sabe

Estas ausências são a razão do gate reprovado. Não são notas de rodapé — são o mapa do próximo trabalho.

| Lacuna | Impacto | Hipótese afetada |
|---|---|---|
| **Zero dado de CAC/LTV/churn** de qualquer legaltech BR | Impede provar que a economia fecha | H2 (decisória) — bloqueador |
| **Zero dado de CAC de canal** para outsider no segmento solo | Impede provar que a aquisição é viável/barata | H5 (decisória) — bloqueador |
| Nenhum **survey primário recente** rankeando as 3 dores espontâneas do solo | "Dor paga por workflow" fica inferida, não medida | H1 |
| Nenhum **caso nomeado de legaltech BR que faliu** | Não valida a premissa "morrem por distribuição, não tecnologia" | contexto/H6 |
| Nenhum **número real de assinantes pagantes** de nenhum concorrente | Impede dimensionar o SAM bottom-up | AH2/H2 |
| Contradição de adoção não resolvida (55% usam IA vs. 70% nunca usaram legaltech) | Sinaliza que o campo carece de fonte de consenso pós-ChatGPT | H1 |
| Conteúdo da Res. CNJ 647/2025 (LGPD nos tribunais) não extraído; MCP Jurisprudências.ai não usado | Precedente primário sobre exercício ilegal por software fica em cobertura de imprensa | H3/H4 |
| Estimativas de mercado (Grand View US$58,7M) são teasers de relatório pago, metodologia opaca | SAM não é auditável | AH2 |

---

## 6. Por que esta síntese vence o baseline de deep research nativo

O baseline nativo (`baseline/baseline-deep-research.md`) chegou a um veredito **quase idêntico no rumo** — "entre numa vertical estreita, B2B, não no genérico". A diferença que justifica o RILP não é a conclusão; é o **rigor da fundamentação**:

1. **Auditabilidade por claim.** Cada afirmação aqui tem bucket, peso, fontes com tier e a conta do score exposta. O baseline afirma em prosa corrida; aqui cada frase decisória é rastreável a `claims.yaml`.
2. **Recusa calibrada ao invés de otimismo.** O baseline afirmou *"a economia fecha, mas com margem apertada"* — sobre **zero dado de CAC**. Este run marca H2 como **Baixo/inconclusiva** e reprova o gate. Para um comprador que vai apostar capital, saber que a economia está **não provada** (e não "apertada mas OK") é a diferença entre due diligence e torcida.
3. **O gate bloqueador força a honestidade.** Um relatório nativo sempre "conclui". O RILP pode dizer **NÃO PASSA** e apontar exatamente os dois dados que faltam — transformando o próximo passo em algo cirúrgico (dois experimentos), não em "continue pesquisando".
4. **Refutações explícitas com peso igual às confirmações** (§3), incluindo refutar o próprio baseline.
5. **Sensibilidade do score exposta** (em `claims.yaml`): mostramos que o NÃO PASSA não é knife-edge manipulado — é ancorado na ausência estrutural de dois dados decisórios.

**O que o comprador leva:** não "existe oportunidade" (isso o ChatGPT dá grátis), mas **onde exatamente a tese trava, com que confiança cada peça se sustenta, e os dois experimentos baratos que decidem o go/no-go** — antes de gastar um centavo em produto.

---

*P2 concluído · GATE 2→3: **NÃO PASSA** (score 63,4% < 70%; C5b/H2 e C6/H5 decisórios em Baixo) · veredito: entrada condicional a fechar H2 (economia) e H5 (canal) com dado primário no próximo pilar.*

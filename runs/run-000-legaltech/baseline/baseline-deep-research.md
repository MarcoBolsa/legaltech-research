# Legaltech no Brasil para um Fundador Solo Não-Advogado com Produto de IA

**Relatório de Deep Research — Estado da Arte**
Data: 04/07/2026 · Idioma: pt-BR · Método: fan-out de buscas web + fetch dirigido + verificação adversarial de afirmações · ~30 fontes consultadas

---

## 1. Sumário Executivo

**Veredito: SIM, é viável — mas apenas dentro de um corredor estreito e bem definido.** Um empreendedor solo não-advogado pode legalmente construir e vender uma ferramenta de IA para o mercado jurídico brasileiro, desde que o produto seja vendido **B2B para advogados** (como instrumento de trabalho) e **nunca B2C como serviço jurídico** para o consumidor final. A fronteira regulatória da OAB é clara e favorável: "atividades meramente instrumentais ou automatizadas" são livres; "consultoria, assessoria e direção jurídicas com interpretação individualizada aplicada a caso concreto" são privativas de advogado. Uma ferramenta de software cai do lado permitido.

**A demanda é real e paga.** O Brasil tem ~1,37 milhão de advogados, dos quais **72% são autônomos** e **64% ganham até 5 salários mínimos** — uma base gigante, pulverizada, sensível a preço e carente de produtividade. Já existe mercado provado: advogados pagam R$ 40–140/mês por ferramentas de IA de geração de peças (Cria.AI, Jus IA, Jurídico AI, Redizz) e R$ 40–300/mês por software de gestão (Projuris, Astrea, ADVBox). O comportamento de compra está estabelecido; não é preciso criar o hábito, apenas capturá-lo.

**O risco competitivo é o ponto mais duro.** O espaço horizontal ("IA que escreve petição genérica") já está lotado e é comoditizável pelo próprio ChatGPT/Claude. O incumbente Jusbrasil tem ~30 milhões de usuários/mês e >80% dos advogados na base, além de já ter lançado a Jus IA. A Enter levantou Série A de US$ 35 mi (valuation R$ 2 bi) atacando o topo (grandes empresas/bancos). Um solo **não vence no genérico** — vence em um **nicho vertical estreito** (ex.: previdenciário/BPC-LOAS, revisional bancário, trabalhista de justa causa) onde o workflow completo, os dados proprietários e a integração ponta-a-ponta criam defensabilidade que nem o incumbente horizontal nem o LLM genérico entregam.

**A economia fecha, mas com margem apertada.** Ticket realista de R$ 80–200/mês; para um solo, a meta mínima de sobrevivência (~R$ 15–20 mil MRR) exige ~100–200 clientes pagantes — alcançável, mas o CAC via tráfego pago numa vertical competitiva pode facilmente estourar o payback se a distribuição depender só de anúncios. **O canal decisivo para um outsider é conteúdo de nicho + comunidade + parcerias com influenciadores-advogados**, não mídia paga pura.

**Recomendação em uma linha:** Entrar, mas **não** como "mais uma IA jurídica". Escolher **uma** dor cara e repetitiva de **uma** vertical, construir o fluxo de trabalho inteiro (não só a peça), instrumentar dados proprietários desde o dia 1, e distribuir por conteúdo/comunidade. Se não houver nicho definido, **não entrar** — o meio-termo genérico é terra de morte.

---

## 2. A Pergunta Real e Como Este Relatório a Responde

A questão do fundador tem quatro sub-perguntas, respondidas por seção:

1. **Existe dor cara e recorrente que já é paga?** → §3 (Demanda)
2. **É legal um não-advogado construir e vender isso?** → §4 (Regulatório OAB)
3. **Dá para ser defensável contra incumbentes e contra o ChatGPT genérico?** → §5 (Concorrência e Lacunas)
4. **A economia e os canais fecham para um solo?** → §6 (Economia) e §7 (Canais)

E fecha em §8 (Veredito e Playbook) e §9 (Riscos) e §10 (Fontes).

---

## 3. Demanda: Existe Dor Cara e Recorrente — e Ela Já É Paga

### 3.1 O tamanho e o formato do mercado

- **~1,37 milhão de advogados inscritos** na OAB (Perfil ADV / OAB-FGV, amostra de 20.885). É um dos maiores contingentes de advogados do mundo — 1 advogado para cada ~164 habitantes.
- **72% são autônomos**; apenas ~29% estão vinculados a empresas ou sociedades. O comprador-alvo do solo (advogado individual / escritório de 1–3 pessoas) **é a maioria absoluta do mercado**, não um nicho.
- **51% dos autônomos trabalham em home office** — perfil digital-nativo, acostumado a comprar SaaS sozinho, sem comitê de compras.

Este é o formato ideal para um fundador solo: **milhões de compradores individuais, decisão de compra self-service, ticket baixo e alto volume** — o oposto de vender enterprise para bancos (onde Enter e Legal One dominam e um solo não compete).

### 3.2 A dor é econômica e mensurável

- **64% dos advogados ganham até 5 salários mínimos** (34% até 2 SM ≈ R$ 2.824/mês; 30% de 2 a 5 SM). É uma base **sensível a preço e desesperada por produtividade**: cada hora economizada em tarefa repetitiva é hora convertível em faturamento ou em mais casos.
- A proposta de valor que já vende hoje é literalmente **tempo**: a Cria.AI comunica "economia de ~3 horas por petição". Para quem ganha por volume, isso é ROI direto e legível.
- **Áreas com dor repetitiva e escalável** (nichos de sustentação apontados pelo mercado em 2025–2026): **previdenciário** (BPC-LOAS, revisão de benefício), **trabalhista** (reversão de justa causa), **consumidor/bancário** (negativa de plano de saúde, revisional). São áreas de **alto volume + peças padronizáveis + urgência do cliente** — exatamente onde IA gera valor e onde a repetição paga a automação.

### 3.3 O comportamento de compra já existe (não é preciso educar o mercado)

Preços praticados e aceitos hoje (evidência de willingness-to-pay):

| Categoria | Produto | Preço praticado |
|---|---|---|
| IA geração de peças | Cria.AI | R$ 49,90 (5 docs) → R$ 139,90 (40 docs)/mês |
| IA geração de peças | Jus IA (Jusbrasil) | +~R$ 40 sobre o plano; completo ~R$ 138,90/mês |
| IA geração de peças | Redizz | a partir de R$ 39,90/mês |
| IA geração de peças | JusDocs | R$ 99,90/mês (plano avançado) |
| Gestão + IA | Projuris ONE / ADV | R$ 39,90 → R$ 169,00/mês |
| Gestão | Astrea, ADVBox, EasyJur (solo/1-3 adv) | R$ 50–300/mês |

**Conclusão da demanda:** a dor é real, cara (tempo = dinheiro numa base de baixa renda), recorrente (peças e prazos são diários) e **já monetizada**. O fundador não precisa provar que advogado paga por IA — isso está provado. Precisa provar que **a sua** solução resolve melhor uma dor específica do que o genérico.

### 3.4 A ressalva: adoção real ainda é rasa (bom e ruim)

As pesquisas divergem e devem ser lidas com cautela (amostras autosselecionadas):
- Um lado: **55,1%** dos advogados já usariam/usam IA generativa; **58,2%** "certamente usariam" serviços jurídicos automatizados; 91% percebem melhora na qualidade técnica.
- Outro lado: **>70% nunca usaram** plataformas dedicadas; a utilização real chega a **~15% do potencial**; só **34% das organizações** têm orçamento dedicado a IA.

Leitura estratégica: **o mercado está no início da curva de adoção** — o que é ao mesmo tempo oportunidade (espaço para crescer) e risco (educação de mercado custa CAC). Reforça a tese de **nicho**: é mais fácil converter 100% de uma vertical faminta do que 5% do mercado inteiro.

---

## 4. Regulatório: É Legal um Não-Advogado Construir e Vender Isso? — SIM, com Corredor Claro

Este é o ponto onde a intuição costuma errar por excesso de medo. **A OAB não proíbe empresas de tecnologia de venderem ferramentas para advogados.** O que ela proíbe é o **exercício da advocacia** por quem não é advogado. A distinção é operacional e foi cristalizada em decisão judicial recente.

### 4.1 A linha que separa o permitido do proibido

Da decisão judicial (caso Migalhas, empresa multada por consultoria sem OAB), a Justiça diferenciou explicitamente:

- **PRIVATIVO de advogado (proibido ao não-advogado):** "consultoria, assessoria e direção jurídicas" que envolvam **"interpretação jurídica individualizada aplicada a caso concreto"** — aconselhar um cliente específico sobre o direito dele, redigir parecer para o caso dele, representá-lo.
- **LIVRE (permitido a empresa de tecnologia):** **"atividades meramente instrumentais ou automatizadas"** que **não** envolvam interpretação de normas aplicada à situação concreta de um cliente final.

**Uma ferramenta de IA vendida a um advogado, que a usa como instrumento e assume a responsabilidade profissional pela peça, cai inequivocamente do lado LIVRE.** O advogado é o profissional; o software é a ferramenta — como um editor de texto, um sistema de gestão ou uma base de jurisprudência. Jusbrasil, Softplan/Projuris, Thomson Reuters e as próprias IAs (Cria.AI etc.) operam exatamente assim, muitas fundadas/operadas por não-advogados.

### 4.2 As três regras de ouro para ficar do lado certo

1. **Venda para o advogado (B2B), nunca dê conselho ao consumidor final (B2C).** No momento em que o produto passar a dizer ao cidadão comum "você tem direito a X, faça Y", entra em zona de exercício ilegal (detenção de até 2 anos + multa, art. 47 LCP; e ações civis públicas movidas pela OAB-SP/OAB-ES contra empresas que "advogam" sem registro). O usuário-cliente precisa ser o advogado, que supervisiona e assina.
2. **Não capte clientela nem ofereça serviço jurídico na publicidade.** O Provimento 205/2021 (publicidade na advocacia) restringe o *advogado*; mas uma empresa que anuncia "resolvemos seu processo" ou intermedeia captação para escritórios pode ser enquadrada. A comunicação deve posicionar o produto como **ferramenta de produtividade para advogados**, não como oferta de solução jurídica ao público.
3. **A responsabilidade e a supervisão são do advogado — e diga isso.** A Recomendação OAB nº 001/2024 (primeira norma da OAB sobre IA generativa) exige que o advogado supervisione o uso de IA, garanta a veracidade, mantenha o sigilo e informe o cliente. Isso é **a favor** do produto: reforça que a ferramenta é auxiliar e que o profissional é o responsável — desde que o design não induza o advogado a confiar cegamente (ver §9, risco de alucinação).

### 4.3 O regulatório como vento a favor, não contra

O ambiente normativo 2024–2026 está **legitimando** IA jurídica, não a barrando:
- **Recomendação OAB 001/2024** + **Plano Nacional de IA da OAB (2025)**: a Ordem decidiu integrar IA à advocacia, com estrutura, prazos e responsáveis — sinal institucional de que IA é bem-vinda quando bem usada.
- **Resolução CNJ 615/2025**: diretrizes de IA no Judiciário — o ecossistema inteiro está se formalizando.

Para o fundador, isso significa: **a conformidade é uma feature vendável.** Um produto que embute rastreabilidade de fontes, trilha de supervisão e avisos de conferência está **mais** alinhado à OAB do que o ChatGPT cru — e isso é um diferencial de confiança, não um custo.

---

## 5. Concorrência e Lacunas: Onde um Solo Pode Ser Defensável

### 5.1 O mapa dos players (e por que o solo não deve enfrentá-los de frente)

| Player | Território | Por que o solo NÃO compete de frente |
|---|---|---|
| **Jusbrasil** | Horizontal de massa: busca, processos, diretório. ~30M usuários/mês, >80% dos advogados na base, Warburg Pincus (Série D US$ 86,1M). Já lançou **Jus IA**. | Distribuição imbatível. Competir em "busca + IA genérica" é suicídio. |
| **Softplan / Projuris (ADV, ex-SAJ)** | Gestão de escritório (ERP jurídico). Consolidou SAJ ADV + Projuris. | Dono do sistema de gestão (dado transacional). Competir em ERP é caro e lento. |
| **Thomson Reuters / Legal One** | Enterprise: pesquisa + contratos + gestão para grandes operações. Preço premium. | Vende para departamentos jurídicos e grandes bancas. Não é o mesmo comprador. |
| **Astrea, ADVBox, EasyJur** | Gestão para solo/pequeno (R$ 50–300/mês). EasyJur captou R$ 1,4M. | Já ocupam o "sistema de gestão do advogado pequeno". |
| **Enter** | IA agêntica ponta-a-ponta para **grandes empresas** (Itaú, Santander, Nubank, Magalu). Série A US$ 35M, valuation R$ 2B, ~250 mil casos/ano. | Topo do mercado, capital pesado, contencioso de massa corporativo. Fora do alcance do solo. |
| **Cria.AI, Jurídico AI, Redizz, JusDocs, LawX** | IA de geração de peças **horizontal** para advogado individual. Cria.AI >20 mil usuários. | **Esta é a zona lotada.** É onde o solo NÃO deve entrar como "mais um". |
| **ChatGPT / Claude genérico** | Substituto de fato para redação de peça. | O verdadeiro concorrente do "genérico". Comoditiza qualquer wrapper de LLM sem dado ou workflow proprietário. |

### 5.2 A tese central de defensabilidade

O erro fatal seria construir **um wrapper de LLM que gera petição genérica**. Isso é: (a) já feito por 5+ players; (b) replicável pelo ChatGPT em minutos; (c) sem moat. A defensabilidade para um solo vem de **três camadas que o genérico e o horizontal não têm**:

1. **Profundidade vertical (workflow completo, não só a peça).** Numa vertical (ex.: previdenciário BPC-LOAS), o valor não é "escrever a inicial" — é o **fluxo inteiro**: triagem de elegibilidade → cálculo do benefício → montagem do dossiê documental → geração da peça específica daquele rito → controle de prazos → acompanhamento. O ChatGPT faz o parágrafo; ele não faz o **sistema do caso**. Um horizontal (Jusbrasil/Cria) não vai construir o fluxo específico de uma vertical estreita porque otimiza para o mercado inteiro.

2. **Dados proprietários acumulados (data moat).** Cada caso processado numa vertical alimenta modelos de padrões: quais teses vencem em qual vara, quais documentos o INSS/banco exige, quais argumentos o juiz X aceita. Isso é **jurimetria de nicho** que só se constrói operando na vertical — e que melhora com escala. O genérico nunca terá esse dado; o horizontal tê-lo-ia diluído demais.

3. **Confiança e conformidade embutidas.** Rastreabilidade de fonte (a peça cita o dispositivo/jurisprudência real e conferível), trilha de supervisão, prevenção ativa de alucinação (§9). Isso ataca o **medo nº 1** do advogado hoje — ser multado por jurisprudência inventada (casos reais 2025–2026, multas de R$ 1.200 a 20 SM, ofício à OAB). Um produto que **garante** que não inventa vale mais que um que só gera texto.

### 5.3 As lacunas concretas (onde há espaço)

- **Verticais estreitas mal servidas:** previdenciário, revisional bancário, trabalhista de justa causa, consumidor/planos de saúde, multas/CNH, superendividamento. Alto volume + peças padronizáveis + comprador faminto.
- **O "depois da peça":** a maioria dos players para na geração do documento. Prazos, protocolo, acompanhamento processual e triagem de leads qualificados são menos servidos.
- **Análise de documentos de entrada** (não só saída): ler o processo/contrato/laudo do cliente e extrair o que importa para o caso — trabalho instrumental, permitido, e onde LLM + dado de nicho brilha.
- **Confiabilidade auditável como produto**, não como afterthought.

---

## 6. Economia do Negócio: A Conta Fecha para um Solo?

### 6.1 Referências de receita

- **Ticket realista:** R$ 80–200/mês para uma ferramenta vertical com fluxo completo (acima do genérico de R$ 40–50, justificado por profundidade). Anual com desconto ~15% (padrão do mercado — Cria.AI pratica isso) melhora o caixa e reduz churn.
- **Metas de sobrevivência do solo:**
  - Piso (custeio próprio + reinvestimento): ~R$ 15–20 mil MRR → **~100–200 clientes** a R$ 100–150/mês.
  - Negócio saudável de um fundador: R$ 50–80 mil MRR → **~400–700 clientes**.
  - Numa base de 1,37M advogados (e centenas de milhares na vertical-alvo), **capturar algumas centenas é matematicamente trivial** — o gargalo é distribuição e retenção, não tamanho de mercado.

### 6.2 Custos

- **COGS de IA:** o principal custo variável é a chamada ao LLM. Peças longas consomem tokens; a R$ 100/mês com 40 docs, a margem bruta pode ficar apertada se o produto usar modelos caros para tudo. **Mitigação:** roteamento de modelo (tarefas mecânicas em modelo barato, raciocínio caro só no essencial), cache e RAG sobre base própria em vez de gerar do zero. É a diferença entre 30% e 80% de margem bruta.
- **CAC:** aqui mora o perigo. Tráfego pago para advogados é **caro e disputado** (Jusbrasil, Projuris e escolas de marketing jurídico inflam o CPC). Um CAC de R$ 300–600 via ads, contra um ticket de R$ 100/mês com churn mensal de 5–8%, dá **payback de 4–8 meses** — tolerável só se a retenção for boa. Se o churn for alto (comum em SaaS jurídico self-service de baixo ticket), o CAC pago **não fecha**.

### 6.3 A alavanca que faz a economia funcionar: retenção + canal barato

- **Retenção** é a variável mais importante e a mais negligenciada. Ferramenta de geração de peça avulsa tem churn alto (o advogado testa, usa 3x, cancela). **Fluxo de trabalho que vira o sistema operacional do caso** (com dados do cliente dentro, prazos, histórico) tem churn baixo — o custo de saída é perder o próprio operacional. **Profundidade vertical não é só moat competitivo; é a alavanca econômica que segura o LTV.**
- **CAC barato** só vem de canal orgânico/comunidade (§7). Se o negócio depender de ads, a matemática do solo raramente fecha. Se depender de conteúdo + indicação + comunidade, o CAC despenca e o payback vira 1–2 meses.

**Conclusão econômica:** fecha **se e somente se** (a) profundidade vertical segura a retenção, (b) COGS de IA for gerenciado com roteamento de modelo, e (c) o canal principal for orgânico. Com ticket genérico + ads + churn alto, **não fecha**.

---

## 7. Canais de Aquisição para um Outsider (Não-Advogado)

Um não-advogado tem uma desvantagem (não tem a rede natural de colegas de OAB) e precisa compensar com **estratégia de canal deliberada**. O que funciona:

1. **Conteúdo de nicho (motor principal).** Ser a melhor fonte de conteúdo prático da vertical escolhida (ex.: "como automatizar cálculos de BPC-LOAS", "checklist de revisional bancário"). SEO + YouTube + newsletter. Isso constrói autoridade sem precisar ser advogado — o produto e o conteúdo falam. Barato, cumulativo, gera CAC decrescente. O próprio ecossistema (Jusbrasil, blogs de legaltech) prova que conteúdo jurídico gera tráfego massivo.

2. **Comunidade e parcerias com advogados-influenciadores da vertical.** Cada nicho tem 5–20 advogados com audiência (Instagram, grupos de WhatsApp/Telegram, cursos). Parceria de co-marketing / afiliação / embaixador contorna a falta de rede própria do fundador e empresta credibilidade. É o canal de maior alavancagem para um outsider. **Atenção regulatória:** a parceria deve ser sobre a *ferramenta* (o advogado recomenda o software), não intermediação de captação de clientes.

3. **Product-led growth (freemium/trial).** O mercado já espera testar grátis (Cria.AI, Projuris, Jus IA oferecem trial/primeiro mês barato — "a partir de R$ 1,90 no 1º mês" da Jusbrasil). Um trial que entrega valor real na vertical converte sozinho e reduz CAC.

4. **Integração/distribuição via incumbente (avançado).** A longo prazo, um AI-native pode acelerar ARR "pegando carona" na distribuição de um incumbente (marketplace, integração com o ERP que o advogado já usa — Projuris tem store, Jusbrasil tem base). Não é o primeiro movimento, mas é uma rota de escala e até de saída (aquisição).

5. **Tráfego pago (secundário, não primário).** Usar ads para *amplificar* o que já converte organicamente e para retargeting — nunca como motor único, pelo custo (§6.2).

**Ordem recomendada para o solo:** conteúdo de nicho + trial (base) → parcerias com influenciadores da vertical (alavanca) → ads só para amplificar → integração com incumbente (escala futura).

---

## 8. Veredito e Playbook

### 8.1 Vale a pena entrar?

**Sim — condicionado a executar no corredor certo.** As quatro perguntas se respondem:

| Pergunta | Resposta | Confiança |
|---|---|---|
| Dor cara, recorrente, já paga? | **Sim.** Base de 1,37M advogados, 72% autônomos, sensíveis a preço; willingness-to-pay provado (R$ 40–200/mês). | Alta |
| Legal para não-advogado? | **Sim**, como ferramenta B2B para advogados (instrumental/automatizada), nunca serviço jurídico B2C. | Alta |
| Defensável vs. incumbentes e ChatGPT? | **Sim, mas só em nicho vertical** com workflow completo + data moat + confiabilidade. No genérico, **não**. | Média-alta |
| Economia e canais fecham para solo? | **Sim, se** retenção (via profundidade) + COGS gerenciado + canal orgânico. Com genérico/ads/churn alto, **não**. | Média |

### 8.2 Playbook de entrada (o "como")

1. **Escolher UMA vertical estreita e faminta.** Critérios: alto volume de casos repetitivos, peças padronizáveis, comprador de baixa renda mas alto volume, urgência. Candidatas fortes: **previdenciário (BPC-LOAS/revisões), revisional bancário, trabalhista de justa causa, consumidor/planos de saúde**. Escolher pela combinação de volume + dor + acesso a especialistas/dados.
2. **Construir o fluxo inteiro, não a peça.** Triagem → análise de documentos de entrada → montagem do caso → geração da peça específica → prazos/acompanhamento. É isso que segura retenção e que o horizontal/genérico não faz.
3. **Instrumentar dados proprietários desde o dia 1.** Capturar padrões de sucesso por vara/juiz/tese/documento — o data moat que melhora com escala.
4. **Confiabilidade como feature nº 1.** Citação rastreável e conferível, zero-alucinação por design (RAG sobre base real, não geração livre), trilha de supervisão. Vender "a IA que não te faz ser multado".
5. **Precificar em R$ 80–200/mês** com anual descontado; gerenciar COGS com roteamento de modelo.
6. **Distribuir por conteúdo de nicho + trial + parceria com advogados-influenciadores** da vertical. Ads só para amplificar.
7. **Posicionar juridicamente certo:** ferramenta para advogados (não serviço ao consumidor), advogado é o responsável, produto alinhado à Recomendação OAB 001/2024.

### 8.3 Quando NÃO entrar

- Se a ideia for **"IA que escreve petição"** genérica horizontal → **não entrar** (comoditizado, sem moat, ChatGPT + 5 incumbentes).
- Se não houver **nenhuma vertical definida** ou acesso a conhecimento/dados dela → **não entrar** (o meio-termo genérico é terra de morte).
- Se o plano de distribuição for **só tráfego pago** → refazer o plano antes de entrar (economia não fecha).

---

## 9. Riscos e Mitigações

| Risco | Gravidade | Mitigação |
|---|---|---|
| **Alucinação de IA** (jurisprudência inventada) — casos reais de advogados multados (R$ 1.200 a 20 SM) e ofícios à OAB em 2025–2026. Mata a confiança. | Alta | RAG sobre base jurisprudencial real e conferível; nunca geração livre de citações; aviso de conferência; trilha de fonte. Transformar o risco em diferencial. |
| **Comoditização pelo LLM genérico.** | Alta | Moat de vertical: workflow completo + dado proprietário. O wrapper puro morre; o sistema de caso não. |
| **Incumbente copia a vertical.** | Média | Velocidade + profundidade de nicho + dado acumulado. Jusbrasil/Cria otimizam para o mercado inteiro; dificilmente descem ao detalhe de uma vertical estreita cedo. |
| **CAC pago inviável.** | Média-alta | Canal orgânico/comunidade como motor; ads só amplificam. |
| **Churn alto de baixo ticket.** | Média-alta | Profundidade que vira o operacional do caso (custo de saída alto). |
| **Enquadramento como exercício ilegal** se derivar para B2C/captação. | Média | Manter estritamente B2B-ferramenta; advogado é o usuário e responsável; comunicação sem oferta de serviço jurídico ao público. |
| **Fundador não-advogado sem rede/credibilidade.** | Média | Parcerias com advogados-influenciadores; conselho consultivo jurídico; conteúdo que prova competência de domínio. |
| **Divergência de dados de adoção** (55% vs. >70% nunca usaram). | Baixa | Ler como mercado no início da curva; nicho concentra a demanda madura. |

---

## 10. Fontes (≈30 consultadas)

**Demanda / demografia da advocacia**
- Perfil ADV (OAB-FGV) via Conjur — https://www.conjur.com.br/2024-abr-30/mais-de-um-terco-dos-advogados-do-brasil-ganham-menos-de-r-3-mil/
- OAB — maioria dos advogados são autônomos — http://www.oab.org.br/noticia/62213/perfil-adv-maioria-dos-advogados-brasileiros-sao-autonomos
- Migalhas — 72% dos advogados são autônomos — https://www.migalhas.com.br/quentes/406378/72-dos-advogados-sao-autonomos
- Conjur — menos de 1/3 em sociedades — https://www.conjur.com.br/2024-mai-06/menos-de-um-terco-dos-advogados-trabalha-em-empresas-ou-escritorios/
- Nichos de sustentação da advocacia 2025–2026 — https://blog.landingpageadv.com.br/2026/01/22/nichos-de-sustentacao-advocacia-2026/
- Áreas com alta demanda e pouca concorrência 2026 — https://oab.estrategia.com/portal/areas-de-atuacao-na-advocacia-com-alta-demanda-e-pouca-concorrencia-em-2026/

**Regulatório OAB / exercício da profissão**
- OAB-ES — Quem pode "vender" serviços jurídicos — https://esa.oabes.org.br/artigos/quem-pode-vender-servicos-juridicos-25
- Migalhas — Justiça multa empresa sem OAB e proíbe consultoria (distinção instrumental x interpretação) — https://www.migalhas.com.br/quentes/450737/justica-multa-empresa-sem-registro-na-oab-e-proibe-venda-de-consultoria-juridica
- OAB-SP — ações civis públicas contra advocacia ilegal — https://www.oabsp.org.br/jornaldaadvocacia/24-08-20-1754-oab-sp-move-acoes-civis-publicas-contra-empresas-que-advogam-ilegalmente
- LUION — o que caracteriza exercício ilegal da advocacia — https://luion.com/o-que-caracteriza-o-exercicio-ilegal-da-advocacia/
- Recomendação OAB 001/2024 (Diário) — https://diario.oab.org.br/pages/materia/842347
- OAB — Plano Nacional de IA — https://www.oab.org.br/noticia/64268/conselho-federal-da-oab-anuncia-plano-nacional-para-integrar-inteligencia-artificial-a-advocacia
- OAB-SP — recomendações de uso de IA — https://www.oabsp.org.br/jornaldaadvocacia/24-11-27-1725-oab-divulga-recomendacoes-para-uso-da-inteligencia-artificial-ia-na-pratica-juridica
- Migalhas — supervisão de IA por sócios (OAB/SP) — https://www.migalhas.com.br/quentes/455537/advogados-socios-devem-garantir-supervisao-em-uso-de-ia
- Provimento 205/2021 (publicidade) — https://www.oab.org.br/leisnormas/legislacao/provimentos/205-2021

**Concorrentes / mercado**
- Jusbrasil (Wikipédia — escala/usuários) — https://pt.wikipedia.org/wiki/Jusbrasil
- Startups.com.br — Jusbrasil atrai Warburg Pincus (foco B2B) — https://startups.com.br/negocios/legaltech/exclusivo-jusbrasil-atrai-warburg-pincus-e-amplia-foco-no-b2b/
- Jus IA (Jusbrasil) planos — https://ia.jusbrasil.com.br/planos
- Cria.AI planos 2025 — https://lp.criaai.app.br/cria-ai-ia-juridica-2025-planos/
- InfoMoney — Cria.AI economia de 3h por petição — https://www.infomoney.com.br/business/cria-a-cria-documentos-juridicos-usando-ia-e-permite-economia-de-3-horas-por-peticao/
- Jurídico AI — https://juridico.ai/
- Projuris ADV (preços) — https://www.projuris.com.br/adv/
- Comparativo softwares jurídicos 2026 — https://asquadz.ai/blog/softwares-gestao-juridica-comparativo/
- Enter — Série A US$ 35M / valuation R$ 2B (Bloomberg Línea) — https://www.bloomberglinea.com.br/startups/rodadas-da-semana-startup-brasileira-enter-atrai-sequoia-e-capta-us-35-milhoes/
- InfoMoney — quem é a Enter — https://www.infomoney.com.br/mercados/startups-quem-e-a-enter-unicornio-brasileiro-de-ia-do-setor-juridico/
- EasyJur capta R$ 1,4M — https://startups.com.br/negocios/easyjur-capta-r-14m-com-saas-para-escritorios-de-advocacia/
- Startups.com.br — 13 legaltechs brasileiras — https://startups.com.br/negocios/dia-do-advogado-13-legaltechs-brasileiras-que-estao-transformando-o-setor-juridico/
- Jusbrasil — Oportunidades e desafios das legaltechs 2025 — https://www.jusbrasil.com.br/artigos/o-futuro-e-agora-oportunidades-e-desafios-das-legaltechs-no-brasil-em-2025/4351343404

**IA / risco de alucinação / adoção**
- Conjur — jurisprudência falsa por IA gera multa e ofício à OAB — https://www.conjur.com.br/2026-fev-16/uso-de-jurisprudencia-criada-por-ia-gera-multa-por-ma-fe-e-oficio-a-oab/
- TJSC — multa por jurisprudência falsa gerada por IA — https://www.tjsc.jus.br/web/imprensa/-/tjsc-multa-autor-de-recurso-por-jurisprudencia-falsa-gerada-por-ia
- Conjur — erros com IA irritam tribunais — https://www.conjur.com.br/2026-mar-17/ma-fe-em-uso-de-ia-irrita-tribunais-e-leva-a-condenacao-de-advogados/
- AB2L — área jurídica mais aberta a novas tecnologias (estudo) — https://lawinnovation.com.br/area-juridica-esta-mais-aberta-para-as-novas-tecnologias-aponta-estudo-da-ab2l/
- Migalhas — IA para advogados / futuro da profissão — https://www.migalhas.com.br/depeso/451616/ia-para-advogados-o-que-novo-estudo-revela-sobre-futuro-da-profissao

**Canais / fundador não-advogado**
- LinkedIn (J. Barbiero) — Legaltech no Brasil, fundador de marketing/produto (Lexly) — https://www.linkedin.com/pulse/intersection-law-technology-brazil-exploring-juliana-barbiero
- ADVBox — custo de captação de cliente — https://advbox.com.br/blog/custo-de-captacao-de-cliente/
- Guia de Investimento — CAC na advocacia — https://www.guiadeinvestimento.com.br/cac-na-advocacia/

---

## Nota Metodológica

Relatório produzido por fan-out de ~15 buscas web + fetch dirigido de fontes-chave (OAB-ES, decisão judicial via Migalhas, Cria.AI, Perfil ADV/Conjur), com verificação cruzada de afirmações falsificáveis. Onde as fontes divergem (ex.: taxa de adoção de IA), a divergência foi sinalizada em vez de resolvida artificialmente. Números de valuation/funding (Enter, Jusbrasil/Warburg) foram confirmados em 2+ fontes independentes. Datas de casos judiciais de 2025–2026 refletem a janela temporal das fontes indexadas.

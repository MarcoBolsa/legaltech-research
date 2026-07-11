# Radiografia RILP — LegalTech Run #1

> ## ⏱️ ADENDO 2026-07-11 — este documento é um retrato PRÉ-Run#0
>
> O corpo abaixo foi escrito em **2026-07-04 13:29, ANTES da Fase C**. Preservado intacto como registro honesto do diagnóstico daquele momento — **mas o fato central mudou naquela mesma tarde.** A recomendação-âncora da radiografia (H1: "rodar um Run #0 timeboxado" + o "teste lado-a-lado", nomeado como "a jogada de maior alavancagem do projeto inteiro") **foi executada.**
>
> **O que mudou (verificado no disco em 2026-07-11):**
> - **Execução não é mais zero.** `runs/run-000-legaltech/` contém P0→P2 real: `hypotheses.md`, 5 relatórios de P1, `claims.yaml` scoreado, síntese estratégica + bias-audit. O "mapa de território onde ninguém andou" foi andado no trecho P0→P2.
> - **O teste decisivo lado-a-lado aconteceu.** Há `baseline/baseline-deep-research.md` + `comparacao.md`. Resultado registrado: a síntese RILP supera o baseline de deep research nativo (média 9,1 vs 7,1) — o **kill criterion NÃO disparou** → CONTINUE.
> - **O score virou código executável e reproduzível.** Fase C entregou o `engine/` (RILP Engine, Python + pydantic, **69 testes verdes**), mergeado na `main` (PR #2, `3d43431`). `rilp run runs/run-000-legaltech` reproduz o veredito: **Score 63,4% · Gate G2→3 FAIL (< 70%) · Kill não disparado**. A "rubrica em prosa" da seção 3 agora é harness determinístico.
>
> **O que SOBREVIVE do diagnóstico abaixo (não foi invalidado):**
> - **n=1.** Só LegalTech rodou; o critério de replicabilidade (≥2 domínios) da seção 6/H3 continua aberto.
> - **Dado de campo ainda é o gate real.** O Gate FALHOU (63,4%) justamente porque os claims decisórios (C5b, C6) seguem em "Baixo" — faltam **H2 (unit economics real)** e **H5 (canal de aquisição)**, que são experimentos primários, não mais pesquisa de escrivaninha. O ponto de fundo da radiografia ("mais documentação não fecha a distância") permanece — só migrou de *"nunca rodou"* para *"rodou uma vez, e o próprio run diz que o próximo passo é campo, não doc"*.
> - **Tese de produto ainda não provada**; comprador ainda não identificado (seção 6/H3 intacta).
>
> **Fonte de verdade do estado ATUAL:** [`docs/OPERATIONAL-BLUEPRINT.md`](https://github.com/MarcoBolsa/legaltech-research/blob/main/docs/OPERATIONAL-BLUEPRINT.md) §7-§8 (atualizado pós-Fase C). Leia a radiografia abaixo como **história**, não como estado corrente.

## 1. Veredicto

**Abacaxi com sementes.** Hoje, sem eufemismo: é um abacaxi. 46 dias de vida, 989 linhas de protocolo (RILP-v2) + 421 de blueprint + DECISIONS + A-FAZER, e **zero linhas de pesquisa real** — `runs/`, `pesquisas/`, `sintese/`, `output/` contêm apenas `.gitkeep`. O sistema nunca rodou uma vez, nem no trecho mais barato (P0→P2, ~16-32h). Não existe produto, não existe prova de conceito, não existe um único artefato que um cliente pagaria para ler.

Mas não é abacaxi puro: há **sementes genuínas** — um núcleo de arquitetura correto (P0→P1→P2), uma rubrica de score auditável, e um kernel de Domain Pack (dado proprietário de execução real) que ferramentas genéricas não têm. Nenhuma germinou porque nenhuma foi plantada. **O veredicto não é sobre a qualidade das ideias — é sobre o fato de que a qualidade de qualquer sistema que nunca tocou runtime é não-falsificável.** Só um Run #0 real resolve o empate.

---

## 2. O que o sistema É hoje (estado real, sem marketing)

| Dimensão | Realidade verificada no disco |
|---|---|
| **Idade** | Iniciado 2026-05-19; hoje 2026-07-04 = **46 dias** |
| **Execução** | **Zero.** Nenhum run iniciado, nenhum pilar rodado, nenhuma pesquisa produzida |
| **Documentação** | Extensa e completa: RILP-v2.md (989 linhas), blueprint (421), DECISIONS (3 decisões), A-FAZER priorizado |
| **Padrão temporal** | 38 dias de silêncio pós-fundação → 1 sessão de pura reescrita de doutrina (v1→v2) → +8 dias travado |
| **Stories criadas** | **Zero.** `docs/stories/` não existe, apesar de Story-Driven ser "MUST" na Constitution (Art. III) |
| **Bloqueadores abertos** | 3 itens em "ATACAR AGORA" parados há 8 dias — nenhum executado, nem o mais barato (criar uma pasta + MANIFEST.yaml) |
| **Natureza dos bloqueadores** | 100% burocráticos: merge de branch, validação de doc, criação de story. **Nenhum é pesquisa.** |

**Tradução honesta:** o RILP é hoje um **documento coerente de arquitetura de processo**, não um sistema. É um mapa muito bem desenhado de um território onde ninguém andou. A infraestrutura (repo, agentes, MCPs, skills) existe e está pronta — o custo marginal de destravar é baixíssimo. O bloqueio é 100% decisão, 0% capacidade técnica.

---

## 3. O que sobreviveu à verificação adversarial (forças reais)

Cada dimensão passou por análise (Sonnet) e refutação (Opus). O que resta depois do crivo:

### Arquitetura do protocolo (3/10)
- **Sequenciamento P0→P1→P2 é design correto** — hipótese antes de pesquisa antes de síntese é a ordem certa. Sobrevive como *intenção de design sã*, não como mérito comprovado nem novidade (é Pesquisa-101).
- **Rubrica de Score por-claim é semi-determinística e auditável** — Alto = 3+ fontes Tier 1+2 trianguladas; Médio = 2 fontes ou 1 Tier 1; Baixo = 1 Tier 3. É o único mecanismo do protocolo que chega perto de ser reproduzível. Mais concreto do que a própria análise creditou.
- **Stage-gate por transição** é boa prática defensável — reduz retrabalho tardio *se aplicado*.

### Produto e mercado (2/10)
- **O kernel de dado proprietário do Domain Pack sobrevive** — ICP validado em campo, unit economics real, vocabulário literal de cliente, falhas pós-lançamento documentadas: é o único vetor que um LLM genérico de fato não tem. Mas é **prospectivo, n=1, e depende de operar um negócio real por 30-90 dias** para existir.
- **O mercado subjacente existe trivialmente** (PMEs/founders sem orçamento big-4) — verdade banal, não diferenciação.

### Diagnóstico operacional (1,5/10)
- **Custo marginal de destravar é baixo** — infra pronta, `runs/` vazio esperando. Um único comando geraria o Run #0 hoje.
- **O diagnóstico de over-engineering-como-procrastinação está verificado e sai mais forte** do escrutínio (ver seção 5).

### Domínio LegalTech (4/10 — a nota que subiu na refutação)
- **Abundância de dados públicos** (193 legaltechs, AB2L 600+, Cubo Legal) torna LegalTech um teste justo para uma camada de pesquisa que depende de triangulação.
- **A fricção OAB ESTÁ endereçada** no protocolo (heatmap regulatório A4, squad legal-analyst, workflow híbrido com advogado assinando) — a acusação de "omissão total" foi refutada como factualmente falsa.

### Framework AIOX (2/10)
- **O diagnóstico "o processo é o gargalo" sobrevive integralmente** e é a parte mais forte: os 3 itens do ATACAR AGORA são 100% burocráticos, nenhum é pesquisa. O framework virou obstáculo, não acelerador.
- **Recomendações de enxugamento sobrevivem** — rodar RILP fora do Story Development Cycle completo; MANIFEST.yaml leve em vez de story formal.

---

## 4. O que NÃO sobreviveu (ilusões desmontadas)

Importante para calibrar — estas são as coisas que soavam bem no documento e caíram na verificação:

| Ilusão | Por que caiu |
|---|---|
| **"Rastreabilidade artefato-a-artefato" P0→P2** | É uma frase dentro de um diagrama Mermaid, não um mecanismo instanciado. Nenhum `hypotheses.md`, nenhum `p1/`, nenhum `p2/` jamais existiu. Rastreabilidade nunca exercida é aspiração, não propriedade. |
| **"Funil de 3 filtros = metodologia de fato superior"** | Repete o table-stakes de systematic review (PRISMA). "Ioannidis + Kahneman" é branding: não há checklist operacional de bias-audit, nem inter-rater, nem fluxo com contagens. Vocabulário de rigor não é rigor. |
| **"Colapsa R$490K-1,65M de consultoria"** | O ancoramento é auto-marketing não-fontado. Pior: é o **mesmo pitch das big labs** (OpenAI/Anthropic/Google deep research). O README manda usar ChatGPT Deep Research como PASSO — o RILP é wrapper de orquestração *em cima* do deep research nativo, não concorrente. |
| **"Marketplace de Domain Packs + Venture Studio"** | Zero sinal de demanda, zero comprador identificado, n=1 domínio, n=1 operador. Moat teórico sobre um pack que não existe, num mercado que ninguém pediu. |
| **Potencial arquitetural = 7** | Fé, não avaliação. "Sólido e corrigível com poucas decisões" são afirmações não-falsificáveis sobre um doc que nunca tocou runtime. Em comitê de investimento, "potencial alto" sem um único run é a definição de wishful thinking. |
| **"Consórcios como piloto testa melhor o motor"** | Inverte o teste: Marco validar hipóteses contra o próprio conhecimento tácito é justamente o *confounder* que o protocolo quer evitar. Testa fricção-de-validação, não o motor autônomo. E ninguém compra domain pack de consórcios (o próprio Marco é o mercado). |
| **Forças do framework AIOX ("já provaram valor")** | Execução zero → nenhum elemento (roteamento de modelo, handoff, restrição de push) foi exercido *neste projeto*. Para operador solo, a restrição de push a @devops é cerimônia — o mesmo humano aprova; a proteção real é o classificador do harness, independente do AIOX. |

---

## 5. Diagnóstico da paralisia (causas raiz)

Verificado no disco, não especulação:

1. **Perfeccionismo documental como procrastinação estruturada.** A resposta a "38 dias sem execução" foi **reescrever o protocolo para v2** em vez de rodar a v1 que existia desde 19/mai. Desenhar o mapa em vez de andar o território — o sintoma clássico, documentado pela própria mão do dono.

2. **Nunca existiu conceito de "menor run viável".** Run #1 é definido como P0→P9 completo (52-92h, 9 gates, 7 camadas paralelas, 6 squads). É tudo-ou-nada — o que **garante que nunca começa**. Não há MVP dentro da própria arquitetura.

3. **O framework virou o obstáculo.** Os 3 bloqueadores são portões de processo auto-impostos (merge por @devops, validação de Marco, story por @sm) — nenhuma é barreira técnica real. O aparato criado para orquestrar agora funciona como anteparo contra o primeiro teste.

4. **Decisão ativa contra começar pequeno** (a descoberta que endurece tudo). DECISIONS.md registra que o Marco **rejeitou por escrito** as duas opções de escopo menor: "Opção A (pesquisa simples) — muito limitada, não captura o potencial" e "Opção C (RILP parcial) — dilui o diferencial". O bloqueio não é só inércia; é uma crença explícita de que **escopo pequeno não captura o potencial**. Qualquer recomendação de "rode menor" morre na segunda vez se não desmontar essa crença primeiro.

5. **Nenhum critério de kill jamais foi definido.** Grep dirigido não retorna critério de morte em RILP-v2, PROTOCOLO ou blueprint. Projeto sem critério de morte não tem pressão para provar valor — pode viver documentando para sempre.

6. **Sunk cost psicológico.** 989+421 linhas escritas geram resistência a cortar escopo — preferir manter o documento grande a admitir que precisa de uma versão 10x menor para validar.

> **A pergunta de fundo, direto:** o padrão de 46 dias sugere evitação do primeiro teste real. O disco mostra o oposto de "medo de escopo pequeno" — mostra preferência ativa por *mais* escopo. Vale nomear isso com o Marco: não falta clareza (há excesso de clareza documental); a questão é se há resistência a descobrir que o protocolo, como desenhado, pode ser caro/lento demais para valer a pena — e que o baseline nativo já entrega 80% do valor.

---

## 6. Plano de ação em 3 horizontes

### H1 — Destravar (próximos 7 dias): o menor run real possível

O objetivo **não é seguir o protocolo** — é gerar o primeiro artefato real e testável. Executável por 1 pessoa + agentes em dias.

| # | Ação | Como |
|---|---|---|
| 1 | **Desacoplar o merge da branch do caminho crítico** | Rodar o Run #0 numa branch de trabalho ou local. `refundacao/` é higiene de config AIOX, não pré-requisito de um documento de pesquisa. São dois projetos competindo pela mesma atenção. |
| 2 | **Rodar um Run #0 timeboxado (1 semana, timebox rígido)** | 1 domínio (LegalTech), foco em P0→P2 (o trecho mais coerente e barato). Usar a skill `deep-research` ou `tech-search` que já existe no repo. `@analyst` + Sonnet/medium para coleta, Opus/high só para bias audit. Output = síntese com 5-10 claims sourced + score por claim. |
| 3 | **TESTE DECISIVO: rodar o MESMO prompt em deep research nativo** | Claude/GPT/Gemini deep research, lado a lado com o output do RILP. **Este é o teste de mercado mais barato e honesto que existe.** Se a diferença não for gritante, o protocolo de 9 pilares não tem tese de produto — só tese de metodologia pessoal. O README já usa ChatGPT Deep Research como insumo, então o RILP *precisa* provar que triangulação+scoring+acumulação vencem o baseline. |
| 4 | **Escrever um critério de kill ANTES de começar** | Ex.: "Se em 3 sessões eu não tiver 1 artefato que eu mesmo pagaria R$500 para ler, E que seja visivelmente superior ao deep research nativo, o RILP como 9 pilares morre e vira só P0-P2 (research-as-a-service)." |
| 5 | **Congelar toda edição de doutrina** | Proibir mexer em RILP-v2, blueprint, P9, domain packs, venture studio até o Run #0 gerar 1 output real. Aplicar a própria §28 (anti-gold-plating) do CLAUDE.md ao protocolo — que é hoje seu maior violador. |

### H2 — Validar internamente (30 dias)

- **Decidir com dados reais** (não suposição) se os 9 pilares valem o tempo, ou se o valor de venda está só nas primeiras 2-3 camadas (pesquisa + síntese) e o resto (brand, GTM, squads) é excesso de escopo para research-as-a-service.
- **Resolver as inconsistências que qualquer domínio herda** — sem isso, todo run bate nos mesmos buracos:
  - Definir a agregação bucket→% do Score (o buraco real não é "criar algoritmo", é mapear Alto/Médio/Baixo → o "≥70%" do gate).
  - Explicitar quais gates são bloqueadores reais vs avisos (o documento se contradiz: "só P4" vs "todos contaminam se aceitos baixos").
  - Resolver a consolidação de Domain Pack (após 1 run vs após 2) — muda o que P9 deve produzir.
- **Definir o ICP do protocolo-como-produto** (não do negócio gerado): quem compra — agências de research, founders solo, VCs, consultorias? Se a resposta honesta for "ninguém compra o protocolo, só o Domain Pack final", então **é ferramenta interna de P&D, não produto** — e isso muda tudo na priorização.
- **Adicionar timeout/fallback ao gate 5→6** (as 5+ entrevistas humanas são o único ponto não-IA num pipeline "operado por IA" — sem fallback, trava o Run inteiro).

### H3 — Preparar venda (90 dias): critérios de go/no-go

O ativo defensável (Domain Pack com dados proprietários) só existe depois de operar um negócio real por 30-90 dias. Antes de investir em venda, checar:

| Critério | GO se… | NO-GO se… |
|---|---|---|
| **Superioridade vs baseline** | Output RILP é *visivelmente* superior ao deep research nativo em rigor/acionabilidade | Output é qualitativamente indistinguível → é overhead sobre capacidade que já existe grátis |
| **Domain Pack real** | Existe ≥1 pack com dado de execução real (ICP em campo, unit economics real) | Ainda é "promessa sobre promessa" |
| **Comprador identificado** | Alguém nomeável pagaria por pack OU pelo serviço-de-run | ICP-do-produto continua indefinido |
| **Replicabilidade** | Protocolo rodou end-to-end em ≥2 domínios (o próprio protocolo diz: "generalizar com 1 run mata o protocolo") | Só n=1 (LegalTech) — comprador sofisticado exige 3+ |
| **Formato de venda decidido** | SaaS / serviço / licença de pack, com pricing | Nunca foi decidido (red flag desde a v1) |

---

## 7. Ideias e oportunidades (o que os analistas viram)

Coisas que o Marco não pediu mas deveria considerar:

1. **O teste lado-a-lado é a jogada de maior alavancagem do projeto inteiro.** Custa 1 dia, e responde a pergunta que 989 linhas de doc não respondem: "isso é empresa ou é feature?". Faça antes de qualquer outra coisa.

2. **O RILP pode ser uma excelente ferramenta interna e um péssimo produto ao mesmo tempo** — e tudo bem. Se ele acelera o P&D pessoal do Marco (inclusive para o negócio de consórcios), tem valor real como processo interno, mesmo que ninguém compre o protocolo. Separar "ferramenta que uso" de "produto que vendo" destrava a decisão.

3. **Consórcios como domínio de valor imediato (não como teste de motor).** O piloto em consórcios é ruim para *validar o motor autônomo* (confounder de conhecimento tácito), mas pode ser ótimo para *gerar valor imediato ao negócio principal* — um Domain Pack de consórcios que o próprio Marco usa. Dois objetivos diferentes; não confundir.

4. **O framework AIOX está superdimensionado para 1 pessoa fazendo pesquisa.** 1149 arquivos, 22 agentes, 215 tasks, ciclo de 5 estados por story — desenhado para squad multi-pessoa entregando software com risco de regressão. Para research exploratório de operador solo: rodar fora do SDC completo, MANIFEST.yaml leve, e manter só 3 elementos (roteamento de modelo §32, handoff de contexto em pilar longo, restrição de push). Desligar o resto para este projeto.

5. **P6 (Brand+Plataforma) é 2-3x maior que os pilares vizinhos** sem justificativa — candidato óbvio a divisão, MAS só depois de um run revelar se de fato estoura o orçamento. Não é prioridade agora (seria bikeshedding de vaporware).

6. **Divergência epistemológica não resolvida:** P0 usa dialética hegeliana (Tese→Antítese→Síntese) para o processo, mas vocabulário popperiano (falsificável) para o output. Costura de tradições sem reconciliação — vale uma decisão explícita, mas não bloqueia o Run #0.

---

## 8. Scorecard consolidado

| Dimensão | Score atual | Score potencial | Score pós-refutação |
|---|:---:|:---:|:---:|
| Arquitetura do protocolo | 4 | 7 | **3** |
| Produto e mercado | 1,5 | 6 | **2** |
| Diagnóstico operacional | 2 | 7 | **1,5** |
| Escolha do domínio LegalTech | 3 | 5 | **4** |
| Framework AIOX (execução) | 2,5 | 7 | **2** |
| **Média** | **2,6** | **6,4** | **2,5** |

**Leitura do scorecard:** o "potencial" médio de 6,4 é largamente **fé** — depende de disciplina comportamental e de um run que nunca aconteceu. O score pós-refutação (2,5) é a nota honesta do *estado atual*: um sistema documentalmente coerente com execução literalmente zero. A única dimensão que *subiu* na refutação foi o domínio (3→4), porque o analista penalizou LegalTech por pecados que a evidência não sustenta (a fricção OAB *está* endereçada). Todas as outras *caíram* — porque a qualidade de qualquer coisa que nunca tocou runtime não se pontua acima do meio-termo por evidência.

**A distância entre 2,5 (real) e 6,4 (potencial) não se fecha com mais documentação. Fecha-se com um Run #0 de 1 semana.** Enquanto ele não rodar, o potencial permanece não-falsificável — e um comitê de investimento chama isso de wishful thinking, não de ativo.
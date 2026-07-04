# P2 — Bias Audit · Run #0 (LegalTech Brasil)

**Papel:** auditor de viés (Ioannidis — "why most published research findings are false" + Kahneman — vieses cognitivos).
**Data:** 2026-07-04 · **Auditor:** P2 bias-auditor (spawn isolado)
**Objeto auditado:** `p2/claims.yaml` (10 claims C1–C9, score_run, gate G2→3), `p2/sintese-estrategica.md`, contra `p0/hypotheses.md` e as 5 frentes `p1/*.md`.

---

## 0. Veredito da auditoria (TL;DR)

**O scoring do run SOBREVIVE à auditoria.** Nenhum claim está com bucket inflado na direção que esconderia fraqueza. O `claims.yaml` é, ao contrário do padrão que Ioannidis alerta, **conservador e auto-crítico**: rebaixa os próprios dois decisórios (C5b/H2, C6/H5) a Baixo por ausência de dado, e recusa explicitamente o overreach do baseline nativo ("a economia fecha"). O gate **NÃO PASSA** é epistemologicamente correto, não um artefato.

| Métrica | Antes da auditoria | Depois da auditoria |
|---|---|---|
| Claims rebaixados de bucket | — | **0** |
| Claims mantidos | — | **10 / 10** |
| Score do run | 63,4% | **63,4% (inalterado)** |
| Gate G2→3 | NÃO PASSA | **NÃO PASSA (confirmado)** |
| Correções aplicadas ao claims.yaml | — | **2** (tier + caveat; nenhuma afeta score) |

**Honestidade sobre a própria auditoria (§36):** eu vim procurando inflação — a instrução me primou para isso. Não achei bucket errado. Fabricar um rebaixamento para "parecer rigoroso" seria o viés oposto (divergência manufaturada). O resultado honesto é: o run acertou o scoring; encontrei 2 imprecisões de rotulagem que corrigi, e 1 nuance de triangulação que documento sem mudar bucket.

---

## 1. Recontagem manual do score_run (refeita à mão, sem confiar na planilha)

| Claim | Bucket | Pontos | Peso | Produto (verificado) |
|---|---|---|---|---|
| C1 | Alto | 90 | 3 | 270 ✓ |
| C2 | Médio | 65 | 3 | 195 ✓ |
| C3 | Alto | 90 | 3 | 270 ✓ |
| C4 | Alto | 90 | 2 | 180 ✓ |
| C5a | Médio | 65 | 2 | 130 ✓ |
| C5b | Baixo | 25 | 3 | 75 ✓ |
| C6 | Baixo | 25 | 3 | 75 ✓ |
| C7 | Médio | 65 | 2 | 130 ✓ |
| C8 | Médio | 65 | 2 | 130 ✓ |
| C9 | Médio | 65 | 2 | 130 ✓ |

- Σ produtos = 270+195+270+180+130+75+75+130+130+130 = **1585** ✓
- Σ pesos = 3+3+3+2+2+3+3+2+2+2 = **25** ✓
- Score = 1585 ÷ 25 = **63,4%** ✓
- Gate: 63,4% < 70% **E** dois decisórios (C5b/H2, C6/H5) em Baixo → **NÃO PASSA** ✓

**A aritmética está correta.** Nenhum erro de conta, nenhum peso trocado, nenhum bucket→pontos divergente da âncora (Alto=90/Médio=65/Baixo=25). A análise de sensibilidade do próprio arquivo (só passaria se AMBOS C5b e C6 subissem a Médio, exigindo dado de CAC/LTV que não existe) está correta e não é knife-edge manipulado.

---

## 2. Verificação de fontes (WebFetch/WebSearch real — 6+ fontes checadas na origem)

Regra: não aceitar a nota do claim; abrir a fonte e confirmar que diz o que o claim alega.

| # | Fonte (claim) | Método | Resultado | Diz o que o claim alega? |
|---|---|---|---|---|
| 1 | ConJur abr/2026 — Jus IA em todos os planos, 300k/mês (C3) | WebFetch | 200 OK | **SIM, verbatim.** "disponibiliza sua ferramenta de IA em todos os planos, sem custo adicional"; "usado todos os meses por 300 mil advogados"; 77% usam ≥1x/semana. |
| 2 | Convergência Digital — 55,1% usam IAGen (C2) | WebFetch | 200 OK | **SIM, mas com achado extra** (ver §3-A). Confirma 55,1%, OAB-SP/Trybe/Jusbrasil/ITS Rio, n=1.500, usos = doc/peça/jurisprudência. A matéria **declara amostra não representativa** (viés Sudeste + engajamento). |
| 3 | ConJur set/2025 — juíza proíbe plataforma B2C (C1) | WebFetch | 200 OK | **SIM.** 2ª Vara Federal RJ; plataforma dava "estimativas percentuais de êxito" e direcionava a escritórios; multa R$20k; fundamento art. 1º Lei 8.906/94; modelo B2C (OAB-RJ: "captação ilícita de clientela"). Confirma a linha que C1 traça (B2C morre, B2B fora do precedente). |
| 4 | FGV Direito SP/CEPI — ~80% usam IAGen, custo é a barreira (C2) | WebFetch | 200 OK | **SIM.** ~80% usam; 58% diariamente; n=495 + 40 entrevistas; "custo elevado limita a difusão" e "aprofunda assimetrias entre organizações de portes diferentes". |
| 5 | TST — condenação por citações falsas de IA (C4) | WebSearch (página JS-rendered vazia no fetch) | Confirmado por 6+ veículos independentes (TST oficial, Diário de Justiça, Jusbrasil, ConJur, LEX, Rota Jurídica) | **SIM.** 6ª Turma TST; multa 1% do valor da causa a empresa + advogado; jurisprudência inexistente em contrarrazões; ofício à OAB **e ao MPF**. Triangulação genuína entre fontes independentes. |
| 6 | Grand View Research — Legal AI BR US$58,7M (C8) | WebFetch | **HTTP 403 (paywall)** | **Não verificável na origem** — confirma que é teaser de relatório pago com metodologia fechada. Ver correção §3-B. |
| 7 | Lei 8.906/94 art. 1º (C1) | WebFetch | ECONNRESET (planalto bloqueia bot) | Não lido diretamente, mas **corroborado indiretamente**: a decisão ConJur set/2025 (fonte #3) cita e aplica o art. 1º definindo postulação + consultoria/assessoria/direção como privativas. Conteúdo da lei não está em disputa. |

**Conclusão da verificação:** todas as fontes de alto peso que sustentam os claims **Alto** (C1, C3, C4) checaram verdadeiras na origem ou por triangulação independente. Nenhuma citação encontrada dizendo coisa diferente do que o claim alega. O único "não verificável" (Grand View) é exatamente a perna que o run já rotulava como fraca — e que corrigi para Tier 3.

---

## 3. Achados de viés e correções aplicadas

### 3-A. Selection/survivorship bias no número de adoção 55,1% — NÃO flagueado (corrigido)

**Achado (Kahneman — WYSIATI / viés de disponibilidade + Ioannidis — bias de seleção da amostra):** a matéria da Convergência Digital, ao ser aberta na origem, **declara ela mesma** que a amostra de 55,1% "não é estatisticamente representativa nacionalmente" por **viés geográfico (concentração Sudeste)** e **viés de engajamento (respondentes já engajados com tecnologia)**. Ou seja, o headline de adoção é um **teto enviesado para cima**: quem respondeu a um survey de IA jurídica tende a ser justamente quem já usa IA — survivorship/self-selection clássico.

O `claims.yaml` tratava o 55,1% como uma perna sólida de triangulação Tier 2 para C2 (e corroboração de AH1/C3), sem registrar esse viés auto-declarado.

**Impacto no bucket:** **nenhum rebaixamento necessário.** C2 já está em **Médio** (não Alto) — e a razão do rebaixamento no run é o núcleo decisório de H1 ("dor JÁ-PAGA por workflow específico + top-3 espontâneo"), não a adoção. O viés reforça a decisão de **manter Médio** e **não** subir a Alto (a justificativa de C2 dizia "a adoção seria Alto sozinha" — este achado mostra que nem a adoção sozinha sustentaria Alto com rigor). AH1/C3 não dependem do 55,1%: sua prova é o fato verificado do Jus IA gratuito (fonte #1).

**Correção aplicada:** adicionada nota de bias-audit na fonte de C2 registrando o viés de amostra auto-declarado. Score inalterado.

### 3-B. Tier inflation: Grand View Research rotulado Tier 2, deveria ser Tier 3 (corrigido)

**Achado (viés de ancoragem — número de marketing/relatório pago tratado como fonte de analista neutro):** o número US$58,7M (mercado Legal AI BR 2030) estava rotulado **Tier 2** em C8 e em `mercado.md`. Na verificação, o fetch retornou **HTTP 403 (paywall)** — é uma **página-teaser de relatório pago com metodologia não auditável**. Pela definição de tiers do P0 (Tier 2 = "analistas vendor-neutral verificáveis"; Tier 3 = material comercial/não auditável), um teaser pago de metodologia fechada é **Tier 3**, não Tier 2.

**Impacto no bucket:** **nenhum.** C8 é **Médio** e seu bucket se ancora no **nº de advogados (Tier 1)** + **direção do capital para enterprise (Tier 2, múltiplas fontes: Exame, Brazil Journal)**. O número Grand View sempre foi explicitamente a perna fraca; o líquido "TAM≠SAM" sobrevive sem ele.

**Correção aplicada:** reclassificado tier 2→3 na fonte de C8 e ajustada a justificativa. Score inalterado.

### 3-C. Independência de triangulação em C3 — "eco da mesma origem" (documentado, sem mudança de bucket)

**Achado (Ioannidis — corroboração aparente que é a mesma fonte repetida):** o bucket **Alto** de C3 é justificado como "comoditização triangulada em Tier 2 (2 matérias ConJur) + survey + direção do capital". Auditoria da independência: as duas matérias ConJur (mar/2025 e abr/2026) são **o mesmo veículo** relatando **anúncios do próprio Jusbrasil**; o número "300k/mês" é de **origem-vendedor (Jusbrasil PR)** repassado. O Exame corrobora, mas é sobre **outra empresa** (Enter). Estritamente, não são "3 origens independentes do mesmo fato" — é uma cadeia ConJur/Jusbrasil + corroboração adjacente.

**Por que MANTER Alto mesmo assim:** o claim substantivo ("ter IA não é diferencial") é provado por **um único fato robusto e verificado na origem** (fonte #1): o incumbente dominante embutiu IA generativa jurídica **de graça em todos os planos**. Comoditização pelo líder de mercado dando o produto de graça é **decisiva por si só**, independente do número exato de usuários. O bucket Alto está correto **pela decisividade do fato-âncora**, não pela contagem de origens. Registro a nuance para que a linguagem "triangulada em 3 fontes" não seja lida como independência maior do que existe.

### 3-D. C7 (lacuna vertical) — o Médio mais frágil (auditado, mantido)

C7 (H6, secundário, peso 2) apoia-se majoritariamente em Tier 3 (páginas de vendor) + 1 Tier 2 (pivô B2B Jusbrasil). O sub-claim "nenhum concorrente entrega workflow vertical + compliance de consentimento" é **inferência de ausência** — a própria `concorrencia.md` admite: "pode ser lacuna real de produto ou simplesmente não ser destacado em marketing; não dá para diferenciar". Pela rubrica, essa sub-parte roçaria Baixo. **Mantido Médio** porque: (a) a parte load-bearing ("horizontal está fechado, Jusbrasil comoditiza o genérico a ~R$59") é robusta e verificada; (b) é secundário (peso 2) e já vem rotulado `confirmada_condicional` com hedge explícito; (c) rebaixar não mudaria o gate (já reprova) e seria over-correction sem ganho epistemológico. Registrado como o Médio de menor folga.

---

## 4. Vieses sistêmicos — a coleta buscou refutar ou só confirmar?

| Viés (Kahneman/Ioannidis) | Presente? | Evidência da auditoria |
|---|---|---|
| **Confirmação** (coletar só o que confirma a tese) | **NÃO** | As 5 frentes P1 são ativamente refutacionais: flagam gaps, dados conflitantes, "eco de marketing entre vendors", ausência-como-dado. `icp-dores.md` desconta os próprios blogs ("quase uma única voz repetida"). Baixo viés de confirmação — atípico e saudável. |
| **Sobrevivência** (só casos de sucesso) | **NÃO (reconhecido)** | `mercado.md` e `concorrencia.md` buscaram casos de legaltech que faliram, **não acharam nenhum**, e flagaram explicitamente como "assimetria de sobrevivência — só quem capta rodada vira notícia". O viés foi **nomeado, não cometido**. (Sub-achado 3-A adiciona: o 55,1% também tem selection bias — agora documentado.) |
| **Ancoragem** (número de marketing como Tier 1) | **PARCIAL, controlado** | Preços de vendor (R$40–700) rotulados Tier 3 com conflito; 300k/mês rotulado T2 (ConJur), não T1; 55,1% com caveat de parte interessada. Uma real derrapada: Grand View T2→3 (corrigido em 3-B). Nenhum número de marketing entrou como Tier 1. |
| **Overconfidence / narrative fallacy** | **NÃO** | O run recusa a conclusão confortável ("economia fecha") do baseline e marca H2/H5 como inconclusivos. É o oposto do viés de narrativa coerente. |

---

## 5. Anti-hipóteses do P0 — foram genuinamente atacadas?

O P0 exige atacar AH1 e AH2 **primeiro**, não confirmá-las. Auditoria:

- **AH1 ("a IA é o meu diferencial")** — **ATACADA GENUINAMENTE e refutada.** A coleta foi atrás do fato que mataria o prior do operador e o encontrou: Jus IA gratuito em todos os planos, 300k/mês (verificado na origem, fonte #1). C3 formaliza a refutação. Não é confirmação disfarçada — é o prior do operador sendo derrubado por evidência dura.
- **AH2 ("mercado gigante = demanda óbvia")** — **ATACADA e confirmada como falsa.** A coleta separou TAM (R$50bi, 1,3M advogados — Tier 1) de SAM (US$58,7M teaser + capital fugindo para enterprise). C8 formaliza. O run recusa "mercado grande = oportunidade".

**Ambas as anti-hipóteses foram alvos primários reais de falseamento, não caixas de checagem.** Este é o sinal mais forte de que o run não é confirmatório.

---

## 6. Score final pós-auditoria

- **Claims rebaixados:** 0
- **Claims mantidos:** 10 / 10 (buckets confirmados)
- **Correções aplicadas ao `claims.yaml`:** 2 (C2: caveat de selection bias no 55,1%; C8: Grand View tier 2→3 + justificativa) — **nenhuma altera pontos, pesos ou score**
- **Nuances documentadas sem mudança de bucket:** 2 (C3 independência de triangulação; C7 Médio de menor folga)
- **Score do run:** **63,4%** (inalterado — recontado à mão, aritmética correta)
- **Gate G2→3:** **NÃO PASSA** (< 70% E dois decisórios em Baixo) — **confirmado como veredito epistemologicamente correto**

**Leitura final do auditor:** o valor deste run não está em ter achado uma oportunidade — está em ter recusado dar sinal verde ao que a evidência não sustenta (H2/economia e H5/canal, ambos dependentes de CAC/LTV/churn que a coleta documental não pode gerar). A auditoria de viés **confirma** que essa recusa é honesta e bem-fundamentada, não pessimismo manufaturado. As duas correções aplicadas endurecem ainda mais o rigor (menos Tier 2 do que se alegava; um número de adoção com viés de amostra agora explícito) — e ambas empurram, se algo, na direção de **mais** cautela, nunca de inflar o score.

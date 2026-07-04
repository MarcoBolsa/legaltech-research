# Comparação — Baseline Deep Research (A) × Síntese Estratégica RILP (B)

**Run #0 · LegalTech Brasil · Juiz independente · 2026-07-04**

- **Documento A:** `baseline/baseline-deep-research.md` (deep research nativo, prosa corrida, ~30 fontes)
- **Documento B:** `p2/sintese-estrategica.md` + anexos `p2/claims.yaml` e `p2/bias-audit.md` (RILP v2.0, 10 claims com score auditável + gate + auditoria de viés)

> **Nota de método do juiz:** os dois documentos chegam ao MESMO corredor estratégico (entrar B2B numa vertical estreita, workflow completo, dados proprietários lícitos, canal orgânico; NÃO entrar no genérico). Isso é reconhecido pelo próprio B (§6). Portanto o julgamento NÃO é sobre a conclusão — é sobre **rigor, auditabilidade e honestidade epistêmica** do caminho até ela. Fiz spot-check REAL (WebFetch) de 4 fontes de cada documento.

---

## 1. Tabela de notas

| Critério | Doc A (baseline) | Doc B (RILP) |
|---|:---:|:---:|
| 1. Rigor de evidência | 7,5 | 9,0 |
| 2. Auditabilidade | 6,0 | 9,5 |
| 3. Honestidade epistêmica | 6,5 | 9,5 |
| 4. Acionabilidade | 8,5 | 8,5 |
| 5. Teste do comprador (R$500) | SIM | SIM |
| **Média (1-4)** | **7,1** | **9,1** |

---

## 2. Spot-checks reais (WebFetch)

### Documento A — 4 fontes

| # | Fonte | Afirmação no doc | Resultado |
|---|---|---|---|
| A1 | Migalhas — 72% autônomos | "72% são autônomos; 64% ganham até 5 SM" | ✅ **Sustenta.** "72% dos advogados atuam como autônomos"; "70% dos autônomos ganham entre 2 e 5 SM". Confere. |
| A2 | InfoMoney — Cria.AI 3h/petição | "Cria.AI comunica economia de ~3 horas por petição" | ✅ **Sustenta, verbatim.** "saving of three hours per document of the petition type". (Nota: a fonte diz 400 clientes pagantes / 5.000 testados; o doc cita ">20 mil usuários" da Cria em outro ponto — número não confirmado nesta fonte.) |
| A3 | Bloomberg Línea — Enter | "Série A US$ 35 mi, valuation R$ 2 bi" | ✅ **Sustenta.** US$ 35M, Sequoia + Founders Fund, valuation US$ 350M ≈ R$ 2 bi. Confere. |
| A4 | OAB Diário — Rec. 001/2024 | Conteúdo da Recomendação (supervisão, veracidade, sigilo, informar cliente) | ⚠️ **Não sustenta na origem.** A página renderiza só o cabeçalho "Diário Eletrônico OAB", sem o texto. A afirmação é verdadeira e corroborada por outras fontes (inclusive por B), mas ESTE link não a sustenta ao ser aberto. |

**Leitura de A:** 3/4 sólidos; 1 link que não renderiza conteúdo (falha de rastreabilidade, não fabricação — o fato é real). Não zera o critério, mas expõe a fraqueza estrutural de A: fontes citadas em bloco no fim, sem mapeamento claim→fonte, algumas Tier-3 (Wikipédia p/ escala do Jusbrasil) sem sinalização.

### Documento B — 4 fontes

| # | Fonte | Afirmação no doc | Resultado |
|---|---|---|---|
| B1 | ConJur abr/2026 — Jus IA | "Jus IA de graça em todos os planos, 300 mil advogados/mês" | ✅ **Sustenta, verbatim.** "disponibiliza sua ferramenta de IA em todos os seus planos, sem custo adicional"; "usado todos os meses por 300 mil advogados". |
| B2 | ConJur set/2025 — proibição B2C | "2ª Vara Federal RJ proibiu plataforma que estimava êxito e direcionava clientes; multa R$20k; art. 1º Lei 8.906/94; B2C = captação ilícita" | ✅ **Sustenta, integralmente.** Todos os elementos confirmados (juíza, R$20k, art. 1º, estimativa percentual de êxito, direcionamento, captação ilícita B2C). |
| B3 | FGV Direito SP — adoção | "~80% usam IAGen; custo é a barreira" | ✅ **Sustenta (nuance).** 80% usam, 58% diariamente, n=495 + 40 entrevistas. Ressalva: a fonte apresenta o custo como UMA barreira proeminente entre várias, não "A barreira central" — leve overstatement de B, não material. |
| B4 | Convergência Digital — 55,1% | "55,1%, n=1.500, OAB-SP/ITS Rio; amostra NÃO representativa (viés Sudeste + engajamento)" | ✅ **Sustenta + bônus.** Confirma 55,1%, n=1.500, e o próprio caveat de não-representatividade — que o **bias-audit de B já havia flagueado por conta própria** (§3-A). |

**Leitura de B:** 4/4 sustentam. E mais: a única nuance que eu, como auditor externo, encontraria (viés de amostra do 55,1%) B **já tinha encontrado e documentado** antes de mim. Isso é o teste mais duro de honestidade — e B passa.

---

## 3. Análise por critério

### 1. Rigor de evidência — A 7,5 · B 9,0
Ambos têm afirmações majoritariamente rastreáveis e os spot-checks sustentaram quase tudo. B ganha por: (a) tier explícito por fonte com regra de triangulação declarada; (b) marcação `GAP / tier 0` onde o dado NÃO existe (CAC/LTV/churn) em vez de preencher com prior; (c) 4/4 spot-checks limpos vs. 3/4 de A. A perde meio ponto pelo link OAB que não renderiza e por afirmações econômicas (CAC R$300–600, payback 4–8 meses) apresentadas com aparência de lastro quando não há fonte de CAC — são priors vestidos de dado.

### 2. Auditabilidade — A 6,0 · B 9,5
Diferença estrutural, não estilística. A é prosa com lista de fontes ao final e uma coluna de confiança grosseira (Alta/Média) em §8. B expõe a **conta inteira**: bucket→pontos→peso→produto→score (63,4%), fórmula, análise de sensibilidade ("só passaria se AMBOS C5b e C6 subissem"), mais um bias-audit independente que **recontou o score à mão**. Um terceiro consegue recalcular o veredito de B; em A, precisa confiar no autor.

### 3. Honestidade epistêmica — A 6,5 · B 9,5
Este é o eixo decisivo. A **sinaliza** divergências (adoção 55% vs 70%) e tem "quando NÃO entrar" — não é ingênuo. MAS A afirma **"a economia fecha, mas com margem apertada"** sobre zero dado de CAC. Essa é exatamente a afirmação que quebra um fundador solo. B **recusa-se** a afirmar isso: marca H2 (economia) e H5 (canal) como inconclusivos, REPROVA o próprio gate (NÃO PASSA, 63,4%), refuta explicitamente 6 crenças — incluindo a do próprio baseline — e roda uma auditoria de viés que foi *procurar* inflação e reporta honestamente ter achado pouco (2 correções, ambas empurrando para MAIS cautela). Atacar a própria tese (anti-hipóteses AH1/AH2 como alvos primários) é o padrão-ouro da §36 — e B o cumpre; A não estrutura isso.

### 4. Acionabilidade — A 8,5 · B 8,5 (empate, sabores diferentes)
A entrega o playbook de **execução** mais detalhado (7 passos, pricing R$80–200, roteamento de modelo, sequência de canais). B entrega a arquitetura de **decisão**: o mesmo corredor + a instrução cirúrgica "antes de escrever uma linha de código, feche H2/H5 com dois experimentos baratos (CAC/LTV via entrevista de 2–3 fundadores; teste de canal com 10 advogados)". Para um empreendedor que precisa DECIDIR e não queimar capital, a régua de B ("aqui é exatamente onde a tese trava") é tão acionável quanto a receita de A — por isso empatam. A é "como construir"; B é "decida se deve, e valide os 2 pontos que decidem".

### 5. Teste do comprador — ambos SIM
**A: SIM.** É um brief estratégico competente, bem-sourced, legível — vale R$500 como o relatório de um bom consultor.
**B: SIM, com valor diferenciado.** Vale R$500 especialmente para quem vai alocar capital: a auditabilidade permite entregar a um sócio/investidor, e a "recusa calibrada" evita o erro caro (entrar assumindo que a economia fecha). O que B entrega que o ChatGPT grátis não dá: *onde exatamente a tese trava, com que confiança cada peça se sustenta, e os dois experimentos que decidem o go/no-go*.

---

## 4. Veredito

**Vence o Documento B (RILP), com diferença CLARA (não gritante).**

- Não é gritante porque **A é um documento genuinamente bom** — não um baseline-palha. Chega ao mesmo corredor estratégico, é bem-sourced, e mais polido/digerível como peça única. Um leitor apressado pode até preferir A.
- É clara — e não marginal — porque a superioridade de B está nos eixos que **importam para uma aposta de capital**: auditabilidade (recomputável) e honestidade epistêmica (recusa calibrada). E no único ponto onde os dois divergem substantivamente — a economia — **B está certo e A cometeu overreach**. A afirmou "a economia fecha"; não há fonte de CAC que sustente isso. B identificou esse vazio como o crux e recusou-se a mascará-lo. Essa é a diferença load-bearing, não cerimônia em volta da mesma resposta.

A máquina extra do RILP (claims.yaml, tiers, gate, bias-audit) **não é enfeite**: ela entrega auditoria real e captura a honestidade que A deixou passar. O custo é que B exige ler 3 arquivos e é menos "me diga logo" — trade-off legítimo, mas favorável a B para o comprador-alvo (fundador/alocador de capital).

## 5. Recomendação contra o critério de kill (MANIFEST.yaml)

Kill exige: **NÃO valer R$500** OU **NÃO ser visivelmente superior ao baseline**.

- B vale R$500? **Sim.**
- B é visivelmente superior ao baseline? **Sim** — em rigor, auditabilidade e, sobretudo, honestidade epistêmica, com a diferença sendo material (corrige o overreach econômico de A) e não apenas de forma.

**Nenhuma das duas condições de kill é satisfeita → CONTINUE.** O RILP demonstrou valor incremental real sobre o deep research nativo neste run. Recomendação de melhoria para o próximo pilar: reduzir o custo de leitura de B (um sumário de 1 página que já entregue "trava em H2/H5 + 2 experimentos") para não perder o leitor apressado que hoje A retém melhor.

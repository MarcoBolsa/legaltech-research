# Plano YOLO — Cirurgia RILP + Run #0 (congelado 2026-07-04)

> **Plano congelado (§33).** Aprovado por Marco em 2026-07-04 ("concordo, siga com seu plano de ação").
> Origem: `docs/RADIOGRAFIA-2026-07-04.md` (veredicto: abacaxi-com-sementes; caminho: Run #0 antes de programar).
> Execução autônoma de ponta a ponta; paradas SOMENTE nas 5 legítimas do §33.5.

---

## Objetivo

Transformar o RILP de protocolo-nunca-executado em sistema com **1 output real + prova comparativa contra baseline**, na ordem: corrigir doutrina (cirurgia mínima) → rodar Run #0 (P0→P2) → só então programar (Fase C, mediante revisão de Marco).

## Critério de kill (escrito ANTES de começar — obrigatório)

> Se ao fim do Run #0 não existir **1 artefato de síntese que valeria R$500 para um comprador** E **visivelmente superior ao baseline de deep research nativo** (avaliação comparativa documentada), o RILP-9-pilares é descontinuado como produto e vira ferramenta interna P0→P2 (research-as-a-service pessoal). Sem terceira reescrita de doutrina.

## Congelamento de doutrina

Durante todo o plano, **nenhuma edição** em RILP-v2.md/blueprint além das 5 correções da Fase A. Gold-plating de protocolo = violação do plano (§28).

---

## Fase A — Cirurgia de doutrina (RILP-v2.md) · 1 sessão

**Story A.1** — Corrigir SÓ as 5 inconsistências confirmadas na radiografia:

| # | Correção | Fonte na radiografia |
|---|----------|---------------------|
| A.1.1 | Definir agregação do Score de Confiança: mapear buckets Alto/Médio/Baixo → o "≥70%" do gate 2→3 (fórmula explícita) | §6-H2 |
| A.1.2 | Explicitar quais gates são bloqueadores reais vs avisos (resolver contradição "só P4" vs "todos contaminam") | §6-H2 |
| A.1.3 | Resolver consolidação de Domain Pack: após 1 run ou 2 (decidir e alinhar P9) | §6-H2 |
| A.1.4 | Adicionar seção "Critério de Kill" ao protocolo (todo run nasce com condição de morte) | §6-H1 |
| A.1.5 | Adicionar seção "Run Mínimo Viável" (P0→P2 como unidade executável independente — o que o Run #0 exercita) | §5-causa-2 |

**Roteamento:** design das resoluções → Opus/high · aplicação dos edits → Sonnet/medium · verificação do diff → Opus/high. Sequencial (arquivo único — sem paralelismo por file-ownership).

**Gate da fase:** diff revisado e commitado. ~30-60 linhas alteradas, não reescrita.

---

## Fase B — Run #0 LegalTech (P0→P2 + baseline) · timebox 7 dias corridos, alvo 1-2 sessões

**Estrutura:** `runs/run-000-legaltech/` (MANIFEST.yaml, p0/, p1/, p2/, baseline/, comparacao.md)

| Story | Entrega | Executor | Modelo/Effort |
|-------|---------|----------|---------------|
| B.1 — Setup | Estrutura de pastas + MANIFEST.yaml | agente único | Haiku/low |
| B.2 — P0 Epistemologia | `p0/hypotheses.md`: tese + 5-8 hipóteses falsificáveis + critérios de evidência por hipótese | agente único | Opus/high |
| B.3 — P1 Coleta | `p1/{camada}.md` por frente de pesquisa (mercado, concorrência, regulação OAB, dores/ICP, pricing) — fontes com tier declarado | 5 coletores paralelos c/ WebSearch | Sonnet/medium (coleta com triagem de fonte exige julgamento — justificativa §32) |
| B.4 — P2 Síntese | `p2/sintese-estrategica.md` + `p2/claims.yaml`: 5-10 claims, cada um com score conforme rubrica corrigida na Fase A | agente único | Opus/high |
| B.5 — Bias audit | `p2/bias-audit.md`: auditoria adversarial dos claims (papel Ioannidis/Kahneman) | agente único | Opus/high |
| B.6 — Baseline | `baseline/baseline-deep-research.md`: MESMA tese, um agente one-shot estilo deep research nativo, SEM protocolo | agente único | Opus/medium |
| B.7 — Comparação | `comparacao.md`: julgamento lado-a-lado RILP vs baseline com rubrica explícita + recomendação kill/continue | juiz cego ao processo | Opus/high |

**Quadro de paralelismo (§31):**
- Frente 1: B.2 → B.3 (5 coletores ∥) → B.4 → B.5 — cadeia principal
- Frente 2: B.6 (baseline) — **paralela à Frente 1** desde o início (só depende da tese do B.2)
- B.7 — barreira final (precisa das duas frentes)
- File-ownership independente: cada agente escreve só seus arquivos em `runs/run-000-legaltech/` — zero conflito

**Gate da fase (parada legítima §33.5-d):** artefatos completos + comparação documentada → apresentar a Marco com recomendação kill/continue.

---

## Fase C — Programação (SÓ após revisão do Run #0 por Marco)

Escopo preliminar (especificação final virá da evidência do Run #0):
1. Score engine — claims como dados estruturados com trilha de auditoria
2. Schema de Domain Pack (YAML) acumulável entre runs
3. Benchmark harness — comparação vs baseline embutida em todo run
4. Runner P0→P2

**Não iniciar sem OK explícito de Marco no resultado da Fase B.**

---

## Paradas legítimas nesta maratona (§33.5)

(a) Risk Flag §4 · (b) decisão de produto nova fora deste plano · (c) recurso externo ausente · (d) FIM da Fase B = artefatos + comparação prontos · (e) merge→main via PR (não previsto neste plano — branch `run-000-legaltech` só recebe push)

## Persistência

Commit por leva (fim de Fase A; fim de cada story-grupo da Fase B). Push da branch via fluxo @devops ao encerrar. Merge → main fica FORA do caminho crítico (decisão registrada em DECISIONS.md 2026-07-04).

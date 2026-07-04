# Fase C — Especificação de Arquitetura (RILP Engine)

> Fase C do plano congelado (`PLANO-YOLO-RUN000.md`). Liberada por Marco em 2026-07-04.
> Fonte da especificação: evidência do Run #0 (`runs/run-000-legaltech/`).
> Stack: **Python 3.12** (pydantic 2, pyyaml, pytest, ruff — todos já no ambiente).

## Princípio arquitetural (o que a Fase C é e o que NÃO é)

O Run #0 provou que a vantagem competitiva do RILP sobre deep research nativo é **auditabilidade + honestidade epistêmica recomputáveis** (`comparacao.md` §2-3: B vence em auditabilidade 9,5×6,0 porque "um terceiro consegue recalcular o veredito"). A Fase C **materializa essa vantagem em código**: transforma o que hoje é cálculo-à-mão em YAML num motor determinístico que qualquer um roda e reproduz.

- **É:** um harness de validação/orquestração que torna score, gates e comparação **determinísticos e recomputáveis**.
- **NÃO é:** um pipeline que chama LLMs para fazer a pesquisa. A pesquisa (P0/P1/P2) continua sendo trabalho de agentes; o engine valida, pontua e audita os artefatos que eles produzem.

Isso está alinhado ao kill criterion (auditabilidade é o que vale R$500) e à §28 (anti-gold-plating: não construir pipeline de LLM especulativo).

## Componentes (escopo do plano congelado, Fase C)

| # | Componente | Arquivo | Responsabilidade |
|---|------------|---------|------------------|
| 1 | Score engine | `rilp/scoring.py` | Recomputar Score do run e gate G2→3 a partir de `claims.yaml`, com trilha de auditoria |
| 2 | Domain Pack | `rilp/domain_pack.py` | Schema YAML acumulável + builder do pack parcial a partir dos artefatos do run |
| 3 | Benchmark harness | `rilp/benchmark.py` | Rubrica RILP×baseline + kill check, reproduzível |
| 4 | Runner P0→P2 | `rilp/runner.py` + `rilp/cli.py` | Orquestra estrutura, valida artefatos por fase, aplica gates, dispara kill |
| — | Contrato de dados | `rilp/models.py` | Modelos pydantic compartilhados (fundação — leva 1) |

## Contrato de dados canônico (`models.py`) — fonte: `claims.yaml` + RILP §334

```
Bucket   = Enum: ALTO(90) · MEDIO(65) · BAIXO(25)          # pontos-âncora (RILP §340)
Peso     = Enum: DECISORIO(3) · RELEVANTE(2) · CONTEXTUAL(1)  # default CONTEXTUAL
Tier     = int 0..3   # 0 = GAP (dado ausente confirmado)
Source   = {url, tier, nota}
Claim    = {id, enunciado, hypothesis_refs[], verdict, bucket, pontos, peso,
            justificativa_bucket, fontes[Source]}
ClaimsDoc= {meta, claims[Claim], score_run?, gate_g2_3?}
ScoreResult = {tabela[{claim,bucket,pontos,peso,produto}], soma_produtos,
               soma_pesos, score_percent}
GateResult  = {cond1_score_ge_70: bool, cond2_no_decisorio_baixo: bool,
               decisorios_em_baixo[], resultado: PASS|FAIL, natureza}
```

## Fórmula canônica (RILP §348 — imutável, congelada Fase A)

```
pontos(bucket): Alto=90 · Médio=65 · Baixo=25
produto(claim) = pontos × peso
Score do run   = Σ produto ÷ Σ peso
Gate G2→3 PASSA sse:  Score ≥ 70  E  nenhum claim decisório(peso=3) em bucket Baixo
```

Teste de aceitação (integração contra o Run #0 real): score == **63.4**, gate == **NÃO PASSA**, decisórios em Baixo == **[C5b, C6]**.

## Rubrica de benchmark (fonte: `comparacao.md` §1)

4 critérios pontuados 0–10 (rigor de evidência · auditabilidade · honestidade epistêmica · acionabilidade) + teste do comprador (bool R$500) + veredito. Média = média dos 4 critérios.
Kill dispara se: **NÃO vale R$500** OU **NÃO é superior ao baseline**.
Aceitação (Run #0): A média 7,1 · B média 9,1 · vence B · kill NÃO dispara.

## Domain Pack — schema (fonte: RILP §699) + 2 estágios (§708)

Conteúdo: hypotheses_validated · icp_real · unit_econ_benchmark · vocabulario_cliente · failures_learned · heatmap_regulatorio · stack_validada.
`stage`: **parcial** (n_runs=1, uso interno — nasce no P9) · **vendável** (n_runs≥2, cross-domain). Validador REPROVA `vendavel` com n_runs<2 (§ Princípio 5 — não generalizar com N=1).
Builder gera `domain-packs/legaltech-v1.yaml` (stage=parcial) a partir de `claims.yaml` + `hypotheses.md`.

## Plano de levas (model routing §32)

| Leva | Entrega | Paralelismo | Modelo/Effort |
|------|---------|-------------|---------------|
| 1 — Fundação | `models.py` + `scoring.py` + testes | sequencial (contrato base) | Opus/high |
| 2 — Frentes | `domain_pack.py` ∥ `benchmark.py` + testes | 2 agentes paralelos (file-ownership distinto) | Sonnet/medium |
| 3 — Integração | `runner.py` + `cli.py` + teste e2e contra Run #0 | sequencial (depende de 1+2) | Opus/high |
| 4 — Verificação | pytest + ruff + validação adversarial do cálculo | sequencial | Opus/high |

Commit + quality gate verde por leva (§33 ponto 3). Verificação de coordenação de nomes entre levas (§33 ponto 4).

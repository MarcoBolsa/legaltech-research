# DECISIONS.md — legaltech-research

> Decisões arquiteturais e estratégicas. Append-only — nunca sobrescrever.

---

## [2026-06-26] — RILP v2.0: Expansão para 3 camadas + P9

**Contexto:** Sessão de reanálise global do projeto após 38 dias sem execução. Constatou-se que o PROTOCOLO.md v1 (9 pilares lineares) era insuficiente para capturar o potencial máximo do sistema.

**Decisão:** Expandir o RILP para v2.0 com:
- 3 camadas: Launch (P0-P8) + Learn (P9) + Scale (Domain Packs + Venture Studio)
- P9 Loop de Retroalimentação — obrigatório, fecha o ciclo de aprendizado
- Score de Confiança por claim nos artefatos do P2 (gate 2→3 exige ≥ 70%)
- Domain Packs como produto comercializável após cada run
- Venture Studio Mode — múltiplos runs em paralelo após Run #1 validar o protocolo

**Alternativas descartadas:**
- Opção A (pesquisa simples para workshop) — muito limitada, não captura o potencial do sistema
- Opção C (RILP parcial, só P0-P3) — dilui o diferencial competitivo sem ganho real de velocidade

**Consequências:**
- RILP-v2.md é o documento canônico daqui em diante
- PROTOCOLO.md (v1) mantido como referência histórica, não excluído
- README.md precisa ser atualizado para refletir a v2 (pendente — Marco decidirá)
- Execução do Run #1 só inicia após validação do RILP-v2.md por Marco

---

## [2026-06-26] — Posicionamento: democratização de inteligência estratégica

**Contexto:** Durante reanálise, identificou-se que o protocolo não articulava seu diferencial competitivo central.

**Decisão:** O RILP se posiciona como democratização de acesso a inteligência estratégica de primeiro nível — colapsando R$490K-1,65M em consultoria tradicional para semanas e custo de tokens. Os agentes são clones de especialistas reais (Sackett, Creswell, Ioannidis, Kahneman, Neumeier, Dunford, Brad Frost, etc.) — não "IA gerando texto".

**Consequências:** Esta narrativa deve estar presente em todos os documentos de apresentação do RILP, especialmente quando o sistema for comercializado.

---

## [2026-06-26] — Pré-requisito: branch refundacao/ deve ser mergeada antes de executar P0

**Contexto:** A branch `refundacao/dedup-aiox-claude-md` contém refatoração da config AIOX que afeta como os agentes operam no projeto. Executar P0 com configuração fragmentada (parte em branch, parte em main) pode gerar inconsistências.

**Decisão:** Fechar `refundacao/dedup-aiox-claude-md` → `main` via PR antes de criar qualquer story ou iniciar qualquer pilar do RILP.

**Consequências:** Bloqueia início da execução até o merge ser feito via @devops.

---

## [2026-07-04] — Radiografia multi-agente + aprovação do plano Cirurgia A → Run #0 → Programação

**Contexto:** Marco pediu radiografia completa do sistema ("diamante ou abacaxi?"). Workflow de 15 agentes (inventário Haiku → análise 5D Sonnet → refutação adversarial Opus → síntese Opus) produziu `docs/RADIOGRAFIA-2026-07-04.md`. Veredicto: **abacaxi-com-sementes** — protocolo coerente, execução zero em 46 dias, paralisia causada por over-engineering de processo e escopo tudo-ou-nada.

**Decisão:** Plano YOLO em 3 fases congelado em `docs/PLANO-YOLO-RUN000.md`: (A) cirurgia mínima de 5 inconsistências no RILP-v2.md; (B) Run #0 = P0→P2 em LegalTech, timeboxado, com teste lado-a-lado contra deep research nativo e critério de kill escrito antes de começar; (C) programação dos diferenciais (score engine, domain pack schema, benchmark harness) SÓ após Marco revisar o resultado da Fase B.

**Reversões explícitas de decisões de 2026-06-26 (aprovadas por Marco em 2026-07-04):**
1. ~~"Branch refundacao/ deve ser mergeada antes de executar P0"~~ → **REVERTIDA.** O merge é higiene de config, não pré-requisito de pesquisa. Run #0 roda na branch `run-000-legaltech`. O merge da `refundacao/` segue pendente, fora do caminho crítico.
2. ~~"Opção C (RILP parcial) dilui o diferencial"~~ → **SUPERADA.** O Run #0 (P0→P2) não é redução de escopo do produto — é geração da prova que o produto completo precisa para existir. A radiografia demonstrou que o tudo-ou-nada garantiu 46 dias de execução zero.

**Alternativas descartadas:**
- Proposta original de Marco (atualizar todos os docs + programar 100% antes de rodar) — repetiria o padrão v1→v2 de reescrita-como-procrastinação; programar antes do primeiro run especifica por especulação.
- Rodar Run #0 em consórcios — confounder de conhecimento tácito do operador; LegalTech testa o motor autônomo de verdade.

**Consequências:**
- Congelamento de doutrina: nenhuma edição em RILP-v2/blueprint além das 5 correções da Fase A até o Run #0 produzir output.
- Critério de kill vigente (ver PLANO-YOLO-RUN000.md) — se o output não superar visivelmente o baseline, RILP-9-pilares é descontinuado como produto e vira ferramenta interna P0→P2.
## [2026-07-04] — Fase C entregue: RILP Engine em Python (score/gates/benchmark/domain-pack executáveis)

**Contexto:** Marco liberou a Fase C do plano congelado (`PLANO-YOLO-RUN000.md`) após ler o resultado do Run #0. O run provou que a vantagem competitiva do RILP sobre deep research nativo é **auditabilidade + honestidade epistêmica recomputáveis** (comparacao.md: B vence em auditabilidade 9,5×6,0 porque "um terceiro consegue recalcular o veredito"). A Fase C materializa isso em código.

**Decisão (stack):** Implementar o RILP Engine em **Python 3.12 + pydantic 2 + pyyaml + pytest + ruff** (todos já no ambiente). Fundamento: a Fase C é processamento de YAML estruturado + validação de schema + cálculo auditável; pydantic dá exatamente o "claims como dados com trilha de auditoria" que o kill criterion recompensou. Greenfield de código (não havia stack de app no repo). Alternativa Node/TS descartada — o AIOX é Node, mas este projeto de research é isolado e não consome o runtime AIOX; Python tem menor cerimônia para o domínio de data/scoring.

**Decisão (arquitetura):** O engine é um **harness de validação/orquestração determinístico**, NÃO um pipeline que chama LLM. A pesquisa (P0/P1/P2) segue sendo trabalho de agentes; o engine valida, pontua e audita os artefatos. Módulos: `models.py` (contrato pydantic), `scoring.py` (score do run + gate G2→3 + trilha de auditoria), `domain_pack.py` (schema acumulável 2-estágios + builder), `benchmark.py` (rubrica RILP×baseline + kill check), `runner.py`+`cli.py` (Run Mínimo Viável P0→P2). Entregue em 4 levas com model routing §32 (Opus contrato/integração/QA · Sonnet frentes paralelas).

**Distinção arquitetural registrada (o que o Run #0 revelou):** Gate G2→3 (bloqueador de AVANÇO a P3: score≥70 E nenhum decisório em Baixo) e Kill criterion (decide se o PROTOCOLO morre: vale R$500 E vence baseline) são **ortogonais**. No Run #0: gate FAIL (63,4%, C5b/C6 em Baixo → não avança sem dado de campo) MAS kill não disparado (protocolo válido → CONTINUE). O engine modela os dois como campos separados; não os colapsa.

**Consequências:**
- `engine/` é o código canônico do RILP daqui em diante; 69 testes verdes, ruff limpo; e2e reproduz o Run #0 (63,4% / FAIL / CONTINUE).
- `domain-packs/legaltech-v1.yaml` (pack parcial, n_runs=1) gerado dos artefatos reais.
- QA adversarial corrigiu 1 bug HIGH de ponto-flutuante que quebrava o determinismo do benchmark (mascarado na 1ª suíte).
- **Dívida técnica p/ decisão de Marco:** (1) piso do gate usa Score arredondado (69,95→70,0 passa) — confirmar se piso é arredondado ou estrito; (2) adicionar `pytest-cov` ao CI para cobertura auditável (@devops).

**Alternativas descartadas:** Node/TS (isolamento do projeto vence o alinhamento com AIOX); pipeline com chamadas de LLM embutidas (violaria §28 anti-gold-plating — a pesquisa é dos agentes, não do engine).

---

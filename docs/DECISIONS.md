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

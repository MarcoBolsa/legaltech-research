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

# ✅ A-FAZER — legaltech-research

> **Documento #0 — abra este primeiro todo dia.** Diário operacional priorizado.
> Atualizado ao final de cada sessão: o que foi feito, o que falta (em prioridade) e o que entrou de novo.
> Não duplica os docs vivos do projeto — **referencia**.

**Última atualização:** 2026-07-11 · @orion (adendo pré-Run#0 na RADIOGRAFIA; avaliado e descartado Brownfield Discovery — docs vivos e frescos)
**Legenda prioridade:** 🔴 P0 (urgente/bloqueia) · 🟡 P1 (importante, esta semana) · 🟢 P2 (quando der)

---

## 🔥 ATACAR AGORA (topo da pilha — máx. 3)

| # | Item | Frente | Story/Doc | Prioridade | Bloqueio / Próximo passo |
|---|------|--------|-----------|-----------|--------------------------|
| 1 | **DECISÃO DE DIREÇÃO pós-NO-GO** — reposicionar up-market (wedge de due diligence M&A) vs ferramenta interna vs outra vertical | 🟥 produto | [`VEREDITO-quadro-fechado`](https://github.com/MarcoBolsa/legaltech-research/blob/run-000-legaltech/docs/research/2026-07-11-rilp-produto-validacao/VEREDITO-quadro-fechado.md) | 🔴 P0 | Marco (decisão de produto §37) |
| 2 | **Teste de campo barato (1 semana)** do wedge escolhido — validar demanda ANTES de PRD | 🟨 validação | (a criar após decisão) | 🟡 P1 | Depende do item 1 |
| 3 | **Dívidas técnicas do engine** — piso do gate (arredondado vs estrito) · `pytest-cov` no CI | 🟦 engine | [`FASE-C-SPEC`](https://github.com/MarcoBolsa/legaltech-research/blob/main/docs/FASE-C-SPEC.md) | 🟢 P2 | Só relevante se RILP seguir como produto |

**Recomendação:** atacar o **item 1** primeiro — as duas lentes de pesquisa (nosso time + Gemini) reprovaram o RILP como definido; sem a decisão de direção do Marco, itens 2-3 ficam sem alvo. Sugestão do Orion: direção "reposicionar up-market" + teste de campo antes do PRD.

## ✅ FEITO (sessão 2026-07-11)
- **Definição canônica do RILP fixada com Marco** — fábrica de negócios por IA, agnóstica de domínio, produto = negócio pronto pra rodar (legaltech = só o Run #1). Gravada em memória.
- **Escolhido Caminho A** (RILP como produto/plataforma) para dev.
- **Validação de mercado em 2 lentes** (nosso time de 4 agentes + Gemini Deep Research) → `docs/research/2026-07-11-rilp-produto-validacao/`. **VEREDITO: NO-GO** no formato agnóstico/self-serve; fatia que sobrevive = up-market/high-ticket. Decisão de pivô pendente (Marco). Ver [DECISIONS.md 2026-07-11](https://github.com/MarcoBolsa/legaltech-research/blob/main/docs/DECISIONS.md).
- **Avaliado Brownfield Discovery → descartado.** Docs vivos frescos e verificados. Rodar as 10 fases seria retrabalho e alimentaria o anti-padrão diagnosticado (doc em vez de execução).
- **Adendo pré-Run#0 na RADIOGRAFIA** (consolidado na main, PR #3) — corpo preservado como história; topo marca que Run #0 + teste lado-a-lado + engine aconteceram. Verificado: 69 testes verdes, `rilp run` reproduz 63,4%/FAIL/CONTINUE.

## ✅ FEITO (sessão 2026-07-04, tarde)
- **Fase C — RILP Engine executável** entregue em 4 levas (YOLO, model routing §32) e **mergeada na main** (PR #2, commit 3d43431). `engine/` Python: score/gate/trilha de auditoria, domain pack 2-estágios, benchmark harness, runner P0→P2 + CLI `rilp`. 69 testes verdes, ruff limpo. `rilp run` reproduz o Run #0 (63,4%/FAIL/CONTINUE). QA adversarial corrigiu bug HIGH de ponto-flutuante no benchmark.
- `.aiox/house/` e `squads/` gitignorados (tooling AIOX local).

---

## 📋 A FAZER (priorizado)

### 🔴 P0 — Urgente
- [ ] Merge branch `refundacao/dedup-aiox-claude-md` → `main` (@devops)
- [ ] Criar `runs/run-001-legaltech/` com `MANIFEST.yaml` + `domain-pack.yaml`
- [ ] Criar Story P0.1 — Epistemologia LegalTech (@sm) · status: InProgress
- [ ] Popular seção ATACAR AGORA com link da story P0.1 após criação
- [ ] Executar P0 com @analyst · Opus/high · modo YOLO → `hypotheses.md`

### 🟡 P1 — Esta semana
- [ ] Gate 0→1: hipóteses falsificáveis aprovadas por Marco
- [ ] Executar P1 — 7 camadas paralelas com `auto-dispatch` + Haiku/low
- [ ] Gate 1→2: 7 camadas completas aprovadas
- [ ] Atualizar README.md para refletir RILP-v2 (está na versão pré-RILP)

### 🟢 P2 — Quando der
- [ ] Planejar P2 com score de confiança — definir threshold por claim
- [ ] Mapear quais squads de outros projetos precisam ser integrados aqui
- [ ] Decidir destino de `.aiox/house/` e `squads/` (gitignore ou commitar)

---

## ⏸️ BLOQUEADO / ESPERANDO

| Item | Espera | Quem destrava |
|------|--------|---------------|
| Fase C (programação) | Revisão do Run #0 por Marco | Marco (decisão kill/continue) |
| Merge `refundacao/` → main | Fora do caminho crítico (D-2026-07-04) | @devops + OK Marco (§0-f) |
| Domain Pack LegalTech v1 | Run completo (P0-P9) — só se Run #0 passar no kill | Pipeline RILP |

---

## ✅ FEITO RECENTEMENTE

### 2026-07-04 — Radiografia + Fases A e B executadas (PRIMEIRO RUN DA HISTÓRIA DO PROJETO)
- ✅ Radiografia multi-agente (15 agentes, 4 fases) → `docs/RADIOGRAFIA-2026-07-04.md` — veredicto: abacaxi-com-sementes
- ✅ Plano YOLO congelado → `docs/PLANO-YOLO-RUN000.md` (Fases A/B/C + critério de kill)
- ✅ DECISIONS.md: decisão 2026-07-04 com 2 reversões explícitas (merge-first; tudo-ou-nada)
- ✅ **Fase A** (92a8a6b): 5 cirurgias no RILP-v2 — fórmula do score, gates 2-tier, domain pack 2 estágios, critério de kill, run mínimo viável
- ✅ **Fase B** (63ce814): Run #0 completo — 12 artefatos em `runs/run-000-legaltech/`; score 63,4%, gate G2→3 não passa (honesto); juiz: RILP vence baseline com diferença CLARA; kill NÃO disparado → CONTINUE

### 2026-06-26 — Sessão de reanálise e expansão RILP v2.0
- ✅ Auditoria global do projeto (workflow 6 agentes paralelos)
- ✅ RILP-v2.md criado — protocolo expandido, 3 camadas, P9 novo, score de confiança, domain packs, venture studio, 15+ diagramas Mermaid
- ✅ docs/OPERATIONAL-BLUEPRINT.md criado — blueprint operacional 8 seções obrigatórias
- ✅ docs/DECISIONS.md criado — 3 decisões estratégicas registradas
- ✅ Handoff `.aiox/handoffs/handoff-2026-06-26-1130.yaml` gerado
- ✅ Memória do projeto atualizada em `~/.claude/projects/.../memory/`

### 2026-05-19 — Sessão de fundação
- ✅ RILP v1 criado (PROTOCOLO.md) com 8 pilares
- ✅ Estrutura de diretórios criada
- ✅ Repo publicado: github.com/MarcoBolsa/legaltech-research

---

## 🆕 ENTROU NOVO (2026-06-26)
- RILP-v2.md — documento canônico expandido
- docs/OPERATIONAL-BLUEPRINT.md — blueprint operacional
- docs/DECISIONS.md — log de decisões
- P9 Loop de Retroalimentação — novo pilar do protocolo
- Score de Confiança — obrigatório nos artefatos do P2
- Domain Packs como produto — após cada run completo
- Venture Studio Mode — múltiplos runs em paralelo (pós Run #1)

---

*Padrão de manutenção (CLAUDE.md global §30): atualizar ao fim de cada sessão. Mover "A FAZER" → "FEITO" ao concluir; registrar novos em "ENTROU NOVO". Manter "ATACAR AGORA" com no máx. 3 itens. Commit + push via @devops.*

# ✅ A-FAZER — legaltech-research

> **Documento #0 — abra este primeiro todo dia.** Diário operacional priorizado.
> Atualizado ao final de cada sessão: o que foi feito, o que falta (em prioridade) e o que entrou de novo.
> Não duplica os docs vivos do projeto — **referencia**.

**Última atualização:** 2026-07-04 · @orion (plano YOLO Run #0 congelado)
**Legenda prioridade:** 🔴 P0 (urgente/bloqueia) · 🟡 P1 (importante, esta semana) · 🟢 P2 (quando der)

---

## 🔥 ATACAR AGORA (topo da pilha — máx. 3)

1. 🔴 **Fase A — Cirurgia RILP-v2.md** (5 correções, sem reescrita) · [PLANO-YOLO-RUN000.md](https://github.com/MarcoBolsa/legaltech-research/blob/run-000-legaltech/docs/PLANO-YOLO-RUN000.md) · em execução YOLO
2. 🔴 **Fase B — Run #0 LegalTech (P0→P2 + baseline + comparação)** · timebox 7 dias · critério de kill vigente
3. 🟡 **Marco revisar resultado do Run #0** → decide kill/continue e libera Fase C (programação)

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

### 2026-07-04 — Radiografia + plano YOLO Run #0
- ✅ Radiografia multi-agente (15 agentes, 4 fases) → `docs/RADIOGRAFIA-2026-07-04.md` — veredicto: abacaxi-com-sementes
- ✅ Plano YOLO congelado → `docs/PLANO-YOLO-RUN000.md` (Fases A/B/C + critério de kill)
- ✅ DECISIONS.md: decisão 2026-07-04 com 2 reversões explícitas (merge-first; tudo-ou-nada)
- ✅ Branch `run-000-legaltech` criada

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

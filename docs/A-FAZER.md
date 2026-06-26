# ✅ A-FAZER — legaltech-research

> **Documento #0 — abra este primeiro todo dia.** Diário operacional priorizado.
> Atualizado ao final de cada sessão: o que foi feito, o que falta (em prioridade) e o que entrou de novo.
> Não duplica os docs vivos do projeto — **referencia**.

**Última atualização:** 2026-06-26 · @orion (encerramento de sessão)
**Legenda prioridade:** 🔴 P0 (urgente/bloqueia) · 🟡 P1 (importante, esta semana) · 🟢 P2 (quando der)

---

## 🔥 ATACAR AGORA (topo da pilha — máx. 3)

1. 🔴 **Validar RILP-v2.md** — Marco lê e dá OK (ou ajusta) antes de qualquer execução · [RILP-v2.md](https://github.com/MarcoBolsa/legaltech-research/blob/refundacao/dedup-aiox-claude-md/RILP-v2.md)
2. 🔴 **Fechar branch `refundacao/` → `main`** — via @devops (`gh pr create + merge`) · bloqueia tudo abaixo
3. 🔴 **Criar Story P0.1 + estrutura `runs/run-001-legaltech/`** — via @sm + @orion · pré-requisito para iniciar P0

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
| Execução P0 | Merge branch + story P0.1 criada | @devops + Marco |
| Execução P1 | Gate 0→1 aprovado | Marco |
| Domain Pack LegalTech v1 | Run #1 completo (P0-P9) | Pipeline RILP |

---

## ✅ FEITO RECENTEMENTE

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

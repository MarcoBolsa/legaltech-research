# OPERATIONAL BLUEPRINT — legaltech-research / RILP

> Espinha dorsal visual do projeto. Atualizado a cada story concluída e a cada encerramento de sessão.

**Projeto:** legaltech-research · RILP Run #1 — LegalTech
**Última atualização:** 2026-06-26
**Branch ativa:** refundacao/dedup-aiox-claude-md

---

## 1. Espinha Dorsal — Funil Completo do Sistema

```mermaid
flowchart TD
    START(["🎯 Domínio + Tese"]):::startend

    subgraph RESEARCH["🔬 FASE DE PESQUISA"]
        P0["📐 P0\nEpistemologia\nTese · Antítese · Hipóteses"]:::ep
        P1["🌍 P1\nInteligência de Mercado\n7 camadas paralelas"]:::pesq
    end

    subgraph SYNTHESIS["⚗️ SÍNTESE"]
        P2["🧬 P2\nSíntese Estratégica\n7 Artefatos + Score"]:::sint
    end

    subgraph BUILD["🏗️ CONSTRUÇÃO"]
        P3["🔧 P3\nDesign Operacional\nWorkflow T0→TN"]:::des
        P4["💰 P4\nModelo de Negócio\nUnit Economics"]:::neg
    end

    subgraph GOMARKET["📣 GO-TO-MARKET"]
        P5["📢 P5\nGTM\nCanais + Conteúdo"]:::gtm
        P6["🖌️ P6\nBrand + Plataforma\nIdentidade + UX"]:::brand
    end

    subgraph LAUNCH["🚀 LANÇAMENTO + OPS"]
        P7["🛫 P7\nLançamento\nPré · Day · 72h"]:::launch
        P8["🤖 P8\nOperacionalização\nSquads + SOPs + KPIs"]:::ops
    end

    subgraph LOOP["🔄 APRENDIZADO"]
        P9["🔁 P9\nLoop de Retroalimentação\nDados reais → Domain Pack"]:::loop
    end

    START --> P0
    P0 -->|"Gate 0→1"| P1
    P1 -->|"Gate 1→2"| P2
    P2 -->|"Gate 2→3\nScore ≥ 70%"| P3
    P3 -->|"Gate 3→4"| P4
    P4 -->|"Gate 4→5\n⚠️ UNIT ECON"| P5
    P5 -->|"Gate 5→6\n5+ entrevistas"| P6
    P6 -->|"Gate 6→7"| P7
    P7 -->|"Gate 7→8"| P8
    P8 -->|"Gate 8→9"| P9
    P9 -->|"Domain Pack\natualizado"| END(["✅ Business Blueprint A-Z"]):::startend
    P9 -.->|"Run N+1\nmais inteligente"| START

    classDef ep fill:#6C63FF,stroke:#5A52D5,color:#fff,font-weight:bold
    classDef pesq fill:#4A90D9,stroke:#2E6DA4,color:#fff,font-weight:bold
    classDef sint fill:#9B59B6,stroke:#8E44AD,color:#fff,font-weight:bold
    classDef des fill:#27AE60,stroke:#1E8449,color:#fff,font-weight:bold
    classDef neg fill:#E67E22,stroke:#CA6F1E,color:#fff,font-weight:bold
    classDef gtm fill:#E74C3C,stroke:#C0392B,color:#fff,font-weight:bold
    classDef brand fill:#E91E8C,stroke:#C2185B,color:#fff,font-weight:bold
    classDef launch fill:#1ABC9C,stroke:#17A589,color:#fff,font-weight:bold
    classDef ops fill:#2C3E50,stroke:#1A252F,color:#fff,font-weight:bold
    classDef loop fill:#F39C12,stroke:#D68910,color:#fff,font-weight:bold
    classDef startend fill:#2ECC71,stroke:#27AE60,color:#fff,font-weight:bold
```

---

## 2. Sistema Operacional — Camadas

```mermaid
flowchart TB
    subgraph OWNER["👑 OWNER LAYER"]
        MARCO["👑 Marco Bolsa\nDecisões de produto · Guardian dos gates\nVisão estratégica"]:::owner
    end

    subgraph ORCH["🎛️ ORCHESTRATION LAYER"]
        ORION["👑 Orion (aiox-master)\nOrquestra todos os pilares\nRoteamento de modelo/agente"]:::master
        ARIA["🏛️ Aria (@architect)\nDecisões arquiteturais\nAnti-goldplating"]:::arch
    end

    subgraph RESEARCH_L["🔬 RESEARCH LAYER — P0 + P1"]
        ALEX["🔍 Alex (@analyst)"]:::an
        DR["🌐 deep-research squad\n11 especialistas"]:::dr
        LA["⚖️ legal-analyst squad\n+ Jurisprudências AI MCP"]:::la
    end

    subgraph SYNTHESIS_L["⚗️ SYNTHESIS LAYER — P2 + P3"]
        QUINN["🔬 Quinn (@qa)"]:::qa
        MORGAN["📋 Morgan (@pm)"]:::pm
        UMA["🎨 Uma (@ux)"]:::ux
    end

    subgraph BUSINESS_L["💼 BUSINESS LAYER — P4 + P5"]
        COPY["✍️ copy-chief"]:::cp
        TRAFFIC["📣 traffic-masters-chief"]:::tm
        SEO["🔍 seo squad"]:::seo
    end

    subgraph BRAND_L["🎨 BRAND + PLATFORM LAYER — P6"]
        BRAND["🎨 brand squad (6)"]:::bsq
        DESIGN["🖌️ design-chief\nbrad-frost · apex"]:::dc
    end

    subgraph OPS_L["⚙️ OPS LAYER — P7 + P8 + P9"]
        GAGE["⚙️ Gage (@devops)"]:::dv
        SQUAD["🤖 squad-chief\nsop-extractor · pedro-valerio"]:::sq
        KAIZEN["♾️ kaizen squad\ndata-chief"]:::kai
    end

    subgraph DATA_L["📊 DATA LAYER"]
        KB["🧠 Knowledge Base\nDomain Packs\nCross-domain patterns"]:::kb
    end

    MARCO --> ORION
    ORION --> ARIA
    ORION --> RESEARCH_L & SYNTHESIS_L & BUSINESS_L & BRAND_L & OPS_L
    OPS_L --> DATA_L
    DATA_L -.->|"Retroalimenta"| RESEARCH_L

    classDef owner fill:#F39C12,stroke:#D68910,color:#fff,font-weight:bold
    classDef master fill:#2C3E50,stroke:#1A252F,color:#fff,font-weight:bold
    classDef arch fill:#6C63FF,stroke:#5A52D5,color:#fff,font-weight:bold
    classDef an fill:#4A90D9,stroke:#2E6DA4,color:#fff,font-weight:bold
    classDef dr fill:#9B59B6,stroke:#8E44AD,color:#fff,font-weight:bold
    classDef la fill:#D0021B,stroke:#A80017,color:#fff,font-weight:bold
    classDef qa fill:#27AE60,stroke:#1E8449,color:#fff,font-weight:bold
    classDef pm fill:#E67E22,stroke:#CA6F1E,color:#fff,font-weight:bold
    classDef ux fill:#E91E8C,stroke:#C2185B,color:#fff,font-weight:bold
    classDef cp fill:#E74C3C,stroke:#C0392B,color:#fff,font-weight:bold
    classDef tm fill:#8E44AD,stroke:#6C3483,color:#fff,font-weight:bold
    classDef seo fill:#1ABC9C,stroke:#17A589,color:#fff,font-weight:bold
    classDef bsq fill:#E91E8C,stroke:#C2185B,color:#fff,font-weight:bold
    classDef dc fill:#6C63FF,stroke:#5A52D5,color:#fff,font-weight:bold
    classDef dv fill:#2C3E50,stroke:#1A252F,color:#fff,font-weight:bold
    classDef sq fill:#27AE60,stroke:#1E8449,color:#fff,font-weight:bold
    classDef kai fill:#F39C12,stroke:#D68910,color:#fff,font-weight:bold
    classDef kb fill:#16A085,stroke:#1A7A65,color:#fff,font-weight:bold
```

---

## 3. Costelas — Workflows Internos por Sub-sistema

### costela:research — P0 + P1

```mermaid
flowchart LR
    TESE["📌 Tese\n@analyst"] --> ANTI["⚔️ Antítese\n@analyst"]
    ANTI --> SINT["⚗️ Síntese\n@analyst + Opus/high"]
    SINT --> HIP["🎯 Hipóteses\nH1..Hn"]
    HIP --> G01{"Gate\n0→1"}

    G01 -->|PASS| F1["🌐 F1\nLandscape\nHaiku/low"]
    G01 -->|PASS| F2["⚖️ F2\nRegulação\nJurisprudências AI"]
    G01 -->|PASS| F3["🏆 F3\nCompetidores\nHaiku/low"]
    G01 -->|PASS| F4["📚 F4\nCasos\nHaiku/low"]
    G01 -->|PASS| F5["🛠️ F5\nFerramentas\nHaiku/low"]
    G01 -->|PASS| F6["🇧🇷 F6\nContexto BR\nHaiku/low"]
    G01 -->|PASS| F7["📊 F7\nUnit Econ\nHaiku/low"]

    F1 & F2 & F3 & F4 & F5 & F6 & F7 --> G12{"Gate\n1→2"}

    classDef h fill:#4A90D9,color:#fff,font-weight:bold
    classDef g fill:#FFF9C4,stroke:#F9A825,color:#333,font-weight:bold
    class F1,F2,F3,F4,F5,F6,F7 h
    class G01,G12 g
```

### costela:synthesis — P2 + Score

```mermaid
flowchart LR
    RAW["📦 Dados Brutos\n7 camadas"] --> TIER["🏆 Filtro Tier\nSonnet/medium"]
    TIER --> TRIANG["△ Triangulação\n3+ fontes"]
    TRIANG --> BIAS["🧠 Bias Audit\nIoannidis + Kahneman\nOpus/high"]
    BIAS --> SCORE["📊 Score\npor claim"]
    SCORE --> A1 & A2 & A3 & A4 & A5 & A6 & A7

    A1["① JTBD Matrix"]
    A2["② ICP"]
    A3["③ Mapa Comp."]
    A4["④ Heatmap Reg."]
    A5["⑤ Unit Econ"]
    A6["⑥ Vocabulário"]
    A7["⑦ Hipóteses MVP"]

    classDef art fill:#9B59B6,color:#fff,font-weight:bold
    class A1,A2,A3,A4,A5,A6,A7 art
```

### costela:brand — P6 Brand

```mermaid
flowchart LR
    B1["🧭 Brand Gap\n+ Onliness"] --> B2["🎯 Posicionamento\nObviously Awesome"]
    B2 --> B3["✏️ Naming\nSMILE/SCRATCH"]
    B3 --> B4["🎨 Visual\n5.5 Steps"]
    B4 --> B5["🔵 Logo\nCGH Process"]
    B5 --> B6["🔥 Ativação\nBrand Soul"]

    classDef b fill:#E91E8C,color:#fff,font-weight:bold
    class B1,B2,B3,B4,B5,B6 b
```

### costela:loop — P9 Retroalimentação

```mermaid
flowchart LR
    DADOS["📊 Dados Reais\n30/60/90 dias"] --> CMP["🔍 Comparar\nHipóteses P0\nvs Realidade"]
    CMP --> CONF["✅ Confirmadas"]
    CMP --> REFUT["❌ Refutadas"]
    CMP --> PARC["🟡 Parciais"]
    CONF & REFUT & PARC --> PACK["📦 Domain Pack\nAtualizado"]
    PACK --> NEXT["🧠 Run N+1\nmais inteligente"]

    classDef l fill:#F39C12,color:#fff,font-weight:bold
    class DADOS,CMP,PACK,NEXT l
```

---

## 4. Roadmap — Run #1 LegalTech

```mermaid
gantt
    title RILP Run #1 — LegalTech
    dateFormat  YYYY-MM-DD
    section Pré-execução
    Fechar branch refundacao → main     :done, pre1, 2026-06-26, 1d
    Criar runs/run-001-legaltech/       :pre2, 2026-06-26, 1d
    Story P0.1 criada + InProgress      :pre3, 2026-06-26, 1d
    section Pesquisa (P0 + P1)
    P0 — Epistemologia (Opus/high)      :p0, 2026-06-27, 3d
    Gate 0→1                            :milestone, g01, after p0, 0d
    P1 — 7 camadas paralelas (Haiku)    :p1, after g01, 7d
    Gate 1→2                            :milestone, g12, after p1, 0d
    section Síntese (P2)
    P2 — Síntese + Score (Sonnet)       :p2, after g12, 5d
    P2 — Bias Audit (Opus)              :p2b, after p2, 2d
    Gate 2→3                            :milestone, g23, after p2b, 0d
    section Design + Negócio (P3 + P4)
    P3 — Design Operacional             :p3, after g23, 4d
    Gate 3→4                            :milestone, g34, after p3, 0d
    P4 — Modelo de Negócio              :p4, after g34, 5d
    Gate 4→5 (Unit Econ — BLOQUEADOR)   :crit, g45, after p4, 2d
    section GTM + Brand (P5 + P6)
    P5 — Go-to-Market                   :p5, after g45, 5d
    Gate 5→6 (5+ entrevistas)           :milestone, g56, after p5, 0d
    P6 — Brand + Plataforma             :p6, after g56, 10d
    Gate 6→7                            :milestone, g67, after p6, 0d
    section Lançamento + Ops (P7 + P8)
    P7 — Lançamento                     :p7, after g67, 7d
    Gate 7→8                            :milestone, g78, after p7, 0d
    P8 — Operacionalização              :p8, after g78, 7d
    Gate 8→9                            :milestone, g89, after p8, 0d
    section Loop (P9)
    P9 — Retroalimentação 30d           :p9a, after g89, 30d
    Domain Pack LegalTech v1            :milestone, dp1, after p9a, 0d
```

---

## 5. Fluxo de Aprovação — Handoffs entre Agentes

```mermaid
sequenceDiagram
    actor Marco as 👑 Marco
    participant Orion as 👑 Orion
    participant Alex as 🔍 Alex (@analyst)
    participant DR as 🌐 deep-research
    participant Quinn as 🔬 Quinn (@qa)
    participant Morgan as 📋 Morgan (@pm)
    participant Gage as ⚙️ Gage (@devops)

    Marco->>Orion: Iniciar Run #1 LegalTech
    Orion->>Alex: Ativar P0 — formular tese + hipóteses
    Alex->>Orion: hypotheses.md (H1..Hn)
    Orion->>Marco: Gate 0→1 — hipóteses OK?
    Marco->>Orion: PASS
    Orion->>DR: Ativar P1 — 7 camadas em paralelo
    DR->>Orion: f1.md ... f7.md (síntese bruta)
    Orion->>Marco: Gate 1→2 — dados suficientes?
    Marco->>Orion: PASS
    Orion->>Alex: Ativar P2 — síntese + score
    Orion->>Quinn: Bias audit P2 (Ioannidis + Kahneman)
    Alex->>Orion: 7 artefatos com score
    Quinn->>Orion: Bias audit aprovado
    Orion->>Marco: Gate 2→3 — score ≥ 70%?
    Marco->>Orion: PASS
    Note over Orion,Morgan: P3 → P4 → P5 → P6 → P7 → P8
    Orion->>Morgan: P4 — unit economics
    Morgan->>Orion: Números fecham?
    Orion->>Marco: Gate 4→5 (BLOQUEADOR) — unit econ OK?
    Marco->>Orion: PASS
    Note over Orion,Gage: P8 concluído
    Orion->>Gage: Push + PR → main
    Gage->>Marco: Domain Pack LegalTech v1 publicado
```

---

## 6. Stack Técnica

```mermaid
flowchart TB
    subgraph INFRA["🏗️ INFRAESTRUTURA"]
        GH["🐙 GitHub\ngithub.com/MarcoBolsa/legaltech-research\nRepositório público"]:::infra
        CC["🤖 Claude Code\nCLI · agentes · workflows\nBypassed permissions"]:::infra
    end

    subgraph AI_LAYER["🧠 CAMADA DE IA"]
        subgraph MODELS["Modelos (§32)"]
            HAIKU["⚡ Haiku/low\nColeta P1\nalto volume"]:::haiku
            SONNET["🎵 Sonnet/medium\nImplementação\npadrão"]:::sonnet
            OPUS["👑 Opus/high\nArquitetura\nBias audit\nGates críticos"]:::opus
        end
        subgraph SKILLS["Skills Globais"]
            TECH["tech-search\nfan-out searches"]:::skill
            DEEP["deep-research\nadversarial verify"]:::skill
            DISPATCH["auto-dispatch\nrouting automático"]:::skill
        end
    end

    subgraph MCPS["🔌 MCPs"]
        JURIS["⚖️ Jurisprudências AI\npesquisa legal BR"]:::mcp
        EXA["🌐 Exa\nweb search"]:::mcp
        SUPABASE["🗄️ Supabase\n(futuro — dados de runs)"]:::mcp
    end

    subgraph SQUADS["🤖 SQUADS DE IA"]
        DR2["deep-research\n11 agentes"]:::squad
        BRAND2["brand squad\n6 especialistas"]:::squad
        SEO2["seo squad"]:::squad
        LEGAL["legal-analyst\nsquad"]:::squad
        KAIZEN2["kaizen squad"]:::squad
    end

    subgraph OUTPUT_LAYER["📤 OUTPUTS"]
        RUNS["runs/run-001-legaltech/\np0...p9 + gates + decisions"]:::out
        PACKS["domain-packs/\nlegaltech-v1.yaml"]:::out
        DOCS["docs/\nA-FAZER · Blueprint · Stories"]:::out
    end

    INFRA --> AI_LAYER
    AI_LAYER --> MCPS
    AI_LAYER --> SQUADS
    SQUADS --> OUTPUT_LAYER
    MCPS --> OUTPUT_LAYER

    classDef infra fill:#2C3E50,stroke:#1A252F,color:#fff,font-weight:bold
    classDef haiku fill:#F5A623,stroke:#D4891E,color:#1A1A1A,font-weight:bold
    classDef sonnet fill:#4A90D9,stroke:#2E6DA4,color:#fff,font-weight:bold
    classDef opus fill:#6C63FF,stroke:#5A52D5,color:#fff,font-weight:bold
    classDef skill fill:#27AE60,stroke:#1E8449,color:#fff,font-weight:bold
    classDef mcp fill:#E67E22,stroke:#CA6F1E,color:#fff,font-weight:bold
    classDef squad fill:#9B59B6,stroke:#8E44AD,color:#fff,font-weight:bold
    classDef out fill:#16A085,stroke:#1A7A65,color:#fff,font-weight:bold
```

---

## 7. Status Atual

| Componente | Status | Notas |
|---|---|---|
| RILP-v2.md | ✅ Done | Documento principal criado 2026-06-26 |
| PROTOCOLO.md (v1) | ✅ Done | Referência histórica — v2 é o canônico |
| docs/OPERATIONAL-BLUEPRINT.md | ✅ Done | Este arquivo |
| docs/A-FAZER.md | 🟡 Em progresso | Template criado, seção ATACAR AGORA vazia |
| Branch refundacao/ | 🔴 Bloqueado | Precisa fechar → main antes de executar |
| runs/run-001-legaltech/ | 🔴 Bloqueado | Estrutura não criada |
| docs/stories/ P0.1 | 🔴 Bloqueado | Story não criada |
| P0 — Epistemologia | 🔒 Aguardando gate | Dependência: story P0.1 + branch mergeada |
| P1 — Inteligência | 🔒 Aguardando gate | Dependência: P0 PASS |
| P2 → P9 | 🔒 Aguardando gate | Dependência: pipeline sequencial |
| Domain Pack LegalTech | 🔒 Aguardando gate | Dependência: P9 completo |

---

## 8. Próximos 30 dias

```mermaid
flowchart TD
    A["🔴 HOJE\nFechar branch refundacao/\n→ main via @devops PR"]:::urgent

    A --> B["🔴 HOJE\nCriar runs/run-001-legaltech/\n+ estrutura de pastas\n(p0...p9, gates, handoffs, decisions)"]:::urgent

    B --> C["🔴 HOJE\nCriar Story P0.1\n'Epistemologia LegalTech'\nStatus: InProgress"]:::urgent

    C --> D["🟡 PRÓXIMA SESSÃO\nExecutar P0\n@analyst + Opus/high\nYOLO mode"]:::next

    D --> E{"Gate 0→1\nHipóteses\nfalsificáveis?"}:::gate

    E -->|PASS| F["📋 P1 — 7 camadas\nparalelas\n@deep-research + Haiku/low\nauto-dispatch"]:::p1

    F --> G{"Gate 1→2\nDados\nsuficientes?"}:::gate

    G -->|PASS| H["⚗️ P2 — Síntese\nSonnet/medium\n+ Opus/high bias audit"]:::p2

    H --> I{"Gate 2→3\nScore ≥ 70%?"}:::gate

    I -->|PASS| END["🏁 Fim do\nhorizonte 30 dias\nP3 em andamento"]:::startend

    classDef urgent fill:#D0021B,stroke:#A80017,color:#fff,font-weight:bold
    classDef next fill:#F5A623,stroke:#D4891E,color:#1A1A1A,font-weight:bold
    classDef gate fill:#FFF9C4,stroke:#F9A825,color:#333,font-weight:bold
    classDef p1 fill:#4A90D9,stroke:#2E6DA4,color:#fff,font-weight:bold
    classDef p2 fill:#9B59B6,stroke:#8E44AD,color:#fff,font-weight:bold
    classDef startend fill:#2ECC71,stroke:#27AE60,color:#fff,font-weight:bold
```

---

*Blueprint atualizado em 2026-06-26 por Orion (aiox-master)*
*Fonte de verdade: https://github.com/MarcoBolsa/legaltech-research/blob/main/docs/OPERATIONAL-BLUEPRINT.md*
*(link ativo após merge da branch refundacao/ → main)*

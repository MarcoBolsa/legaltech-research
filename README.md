# LegalTech Research — Projeto de Pesquisa

## Contexto

Antes de desenhar o workflow do sistema jurídico com IA, precisamos entender o que
já existe no mundo — o que funcionou, o que falhou, quais modelos foram validados
em mercados mais maduros (EUA, UK, Europa) — para ancorar decisões em evidência
e não reinventar a roda.

Este projeto é separado do codebase do sistema jurídico. É um repositório de
conhecimento: documentos de pesquisa, sínteses, benchmarks e referências que
vão alimentar o workshop de workflow com o time jurídico, produto e técnico.

## Objetivo Final

Produzir um documento-base que responda:

> Como um escritório jurídico deve operar com IA — do T0 (captação) ao T5
> (encerramento) — com responsabilidades claras em cada etapa: o que é humano,
> o que é IA, como eles interagem?

---

## Estrutura do Projeto

```
legaltech-research/
├── README.md               # Este arquivo — visão geral e instruções
├── pesquisas/
│   ├── gemini/             # Resultados brutos do Gemini
│   ├── perplexity/         # Resultados brutos do Perplexity
│   └── outros/             # Outras fontes
├── sintese/
│   ├── workflow-modelos.md     # Modelos de operação com IA
│   ├── produtos-lideres.md     # Harvey, Clio, Luminance, Robin AI etc.
│   ├── custo-e-roi.md          # Benchmarks de custo e resultado
│   ├── resistencia-adocao.md   # O que advogados aceitam/recusam
│   └── contexto-brasil.md      # Especificidades do mercado brasileiro
└── output/
    └── workshop-base.md        # Documento final para o workshop
```

---

## Passo a Passo — Pesquisa Manual

### Passo 1 — Gemini

Acesse [gemini.google.com](https://gemini.google.com) e use o prompt abaixo.
Salve o resultado em `pesquisas/gemini/resultado-01.md`.

**Prompt:**

```
Faça uma pesquisa profunda sobre o uso de Inteligência Artificial em escritórios
de advocacia — foco em modelos operacionais, não em capacidade técnica da IA.

Quero entender:

1. WORKFLOW: Como escritórios que adotaram IA estruturaram o fluxo de trabalho
do caso — desde o primeiro contato com o cliente até o encerramento? Quais etapas
foram automatizadas, quais mantiveram humanas e por quê?

2. PRODUTOS LÍDERES: Como Harvey, Clio, Luminance, Robin AI e similares resolvem
o problema de interação advogado/IA? O que o advogado faz, o que a IA faz, como
eles se comunicam dentro do sistema?

3. MODELO DE CUSTO: Qual o custo por caso/etapa antes e depois da IA? Onde houve
redução real de custo vs. onde criou retrabalho ou resistência?

4. RESISTÊNCIA E ADOÇÃO: O que os advogados aceitam delegar para IA? O que
recusam? Quais foram os principais erros de produto nessa área?

5. CONTEXTO BRASIL: O que existe hoje no mercado brasileiro de LegalTech? Quais
as especificidades jurídicas brasileiras que impactam a adoção (responsabilidade
do advogado pela peça, sigilo, OAB)?

6. BENCHMARKS: Casos reais de escritórios (qualquer porte) que documentaram
resultados — tempo economizado, erros reduzidos, satisfação do cliente.

Formato de resposta: estruturado por tópico, com fontes citadas, destacando
o que foi validado empiricamente vs. o que é projeção/marketing.
```

---

### Passo 2 — Perplexity

Acesse [perplexity.ai](https://perplexity.ai) e use o mesmo prompt acima.
Salve o resultado em `pesquisas/perplexity/resultado-01.md`.

Perplexity é mais rápido em citar fontes verificáveis — preste atenção nas
referências que ele trouxer, são úteis para rastrear estudos originais.

---

### Passo 3 — Pesquisa Complementar (opcional mas recomendado)

Use o ChatGPT Deep Research com o prompt adaptado:

```
Pesquisa profunda: modelos operacionais de escritórios de advocacia que adotaram
IA. Foco em: (1) workflow passo a passo do caso, (2) divisão de tarefas humano/IA,
(3) produtos como Harvey e Clio — como funcionam na prática, (4) erros comuns de
adoção, (5) benchmarks quantitativos reais. Cite fontes primárias quando possível.
```

Salve em `pesquisas/outros/chatgpt-deep-research.md`.

---

### Passo 4 — Consolidação (Claude Code faz isso)

Depois de ter os resultados das pesquisas, traga-os aqui (cole o conteúdo ou
coloque os arquivos na pasta `pesquisas/`). O Claude vai:

1. Cruzar as fontes
2. Identificar consensos e contradições
3. Separar evidência empírica de marketing
4. Produzir os documentos de síntese em `sintese/`
5. Gerar o `output/workshop-base.md` para o workshop com o time

---

## N8N — Automação da Pesquisa (próxima fase)

Possibilidade de automatizar parte do processo via N8N:

- **Trigger**: manual (botão) ou agendado (toda semana)
- **Busca paralela**: Perplexity API + outros endpoints de pesquisa
- **Armazenamento**: salvar resultados em Google Drive ou Supabase
- **Notificação**: aviso via WhatsApp/email quando nova pesquisa estiver pronta
- **Atualização contínua**: monitorar novos produtos e estudos de LegalTech

Ver `n8n-workflow.md` quando essa fase for iniciada.

---

## Status

- [ ] Pesquisa Gemini
- [ ] Pesquisa Perplexity
- [ ] Pesquisa ChatGPT Deep Research (opcional)
- [ ] Consolidação e síntese
- [ ] Workshop-base gerado
- [ ] Workshop realizado com time jurídico + produto + técnico

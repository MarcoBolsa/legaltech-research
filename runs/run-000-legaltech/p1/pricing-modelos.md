# P1 — Pricing e Modelos de Negócio · Run #0 (LegalTech Brasil)

> Coletor: frente **pricing-modelos**. Objetivo: confirmar/refutar H1, H2, H4, H5 (e apoiar H6) com dados reais de preço, unit economics e modelos de monetização em legaltech BR + comparáveis internacionais.
> Método: 10 buscas web + 8 fetches de página. Nenhuma entrevista, nenhum dado privado — só evidência documental pública (Tiers 1–3), conforme escopo negativo do P0.

---

## 1. Achados organizados por modelo de negócio

### 1.1 SaaS por usuário/mensalidade fixa — gestão de escritório (o modelo dominante no BR)

| Ferramenta | Plano de entrada | Preço | Teto observado | O que inclui na entrada |
|---|---|---|---|---|
| Projuris ONE | Solo | **R$ 39,90/mês** | — | Controle de andamentos, gestão básica de processos |
| Projuris OFFICE | Escritório | R$ 169/mês | — | + módulo financeiro |
| Projuris ADV | Escritório maior | a partir de R$ 197/mês | variável (customizável) | Automação, redação, financeiro |
| Astrea (Aurum) | PlanoLight | **Grátis por 1 ano** (40 processos, 1 usuário) | Planovip R$ 1.249/mês (2000 processos, 30 usuários) | Monitoramento de processos, captura de publicações |
| Astrea | Planosmart (mais popular) | R$ 379/mês (R$ 4.548/ano) | 500 processos, 5 usuários | — |
| ADVBOX | Essencial | **R$ 220/mês** (2.000 processos) | Elite R$ 1.800/mês | Tarefas, prazos, automação de atendimento |
| ADVBOX | Banca Jurídica | R$ 450/mês | ilimitado processos | + contabilidade integrada |

**Fonte:** [ADVBOX Planos](https://advbox.com.br/planos) (fetch direto, 2026-07-04, **Tier 3** — página comercial do próprio fornecedor); [Astrea Planos e Preços](https://www.aurum.com.br/astrea/planos-e-precos/) (fetch direto, 2026-07-04, **Tier 3**); [Projuris — quanto custa](https://www.projuris.com.br/blog/software-juridico/) (**Tier 3**, conflito de interesse — blog do próprio Projuris avaliando "quanto custa software jurídico").

**Mapa → hipótese:**
- **[confirma H2 parcialmente]** Existe uma faixa de preço real e ampla (R$ 40–1.800/mês) com produto sênior/lock-in por volume de processos e usuários — sinaliza que o mercado aceita pagar recorrente, mas o ticket de entrada solo (R$ 40–220) é baixo, pressionando LTV.
- **[neutro/refuta parcialmente H2]** O modelo de precificação por "processos monitorados" (não por feature de IA) sugere que o valor percebido ainda é **monitoramento/gestão**, não IA — a IA aparece como add-on, não como eixo de precificação principal nesses incumbentes.

---

### 1.2 SaaS de "IA jurídica" — pricing específico de ferramentas de IA (mais direto para H4/H2)

Tabela consolidada de uma fonte agregadora (Tier 3, vendor com conflito de interesse — Locus é parte interessada no ranking):

| Ferramenta | Preço mensal | Observação |
|---|---|---|
| Jurídico AI | R$ 49 (entrada) / **R$ 127/mês** (plano citado em outra fonte) | Elaboração de peças, jurisprudência, análise preditiva |
| Jus IA (Jusbrasil) | ~R$ 149/mês | Plano profissional individual |
| Locus.IA Pro | R$ 249,90/mês | Análise de contratos + petições, RAG sobre base própria |
| Turivius | ~R$ 299/mês | Pesquisa jurisprudencial com IA |
| Judit | ~R$ 349/mês | Monitoramento processual via API |
| Locus.IA Individual+ | R$ 499/mês | Análise ilimitada |
| Locus.IA Elite | R$ 699/mês | Recursos avançados |
| Locus Local Air-Gapped | R$ 1.099/mês | 100% offline, requer GPU dedicada |

**Fonte:** [ialocus.com.br — Quanto custa uma IA jurídica em 2026](https://ialocus.com.br/blog/post-ia-juridica-preco.html) (fetch direto, 2026-07-04, **Tier 3 — conflito de interesse**: o autor é fornecedor concorrente/próprio produto Locus.IA aparece no ranking, valores de terceiros não auditados); complementado por [Jurídico AI R$127/mês](busca web, sem fetch direto — **Tier 3, não verificado na origem**).

**Mapa → hipótese:**
- **[confirma H2]** Existe uma faixa clara de "IA jurídica individual" entre **R$ 149–350/mês** — bate com a faixa indicativa da própria H2 (R$ 50–300/mês), com viés para o topo dessa faixa, não o piso.
- **[neutro H4]** Preço mais alto que gestão pura (R$ 40–220) sugere que o mercado *aceita pagar prêmio por IA* — mas não prova defensabilidade (H4): pode ser prêmio de novidade, não de fosso. Precisa cruzar com dado de churn/retenção que esta busca não encontrou.
- **Gap identificado:** nenhuma dessas fontes é o site oficial do fornecedor (fetches diretos ao chatadv.com.br e ia.jusbrasil.com.br/planos retornaram HTTP 403) — os números de Jurídico AI, Jus IA, Turivius, Judit vêm de um agregador terceiro, não confirmados na fonte primária. **Tratar como indicativo, não definitivo.**

---

### 1.3 Modelo Success Fee (comissão de êxito) — fora de gestão de escritório, direto ao consumidor

| Empresa | Modelo | Percentual/valor |
|---|---|---|
| Resolvvi | Success fee sobre indenização de voo atrasado/cancelado | **35% do valor da indenização**; zero custo upfront; "se não ganhar, não paga" |
| AirHelp, Liberfly | Mesmo modelo (comparáveis) | Não coletado percentual exato nesta busca |

**Valor médio de indenização por atraso de voo no Brasil:** ~R$ 4.500 (pode chegar a R$ 10.000).

**Fonte:** [topensandoemviajar.com — Experiência Resolvvi](https://www.topensandoemviajar.com/experiencia-real-resolvvi/) (**Tier 3** — blog de experiência de usuário, não é o próprio fornecedor nem imprensa especializada, mas também não tem conflito comercial direto com Resolvvi); [resolvvi.com — Voo atrasado](https://www.resolvvi.com/problema-com-voo/voo-atrasado/) (**Tier 3**, fonte primária comercial).

**Mapa → hipótese:**
- **[confirma H1 indiretamente]** Success fee funciona bem quando (a) o valor da causa é previsível e (b) o consumidor não quer risco de custo — é modelo B2C, não B2B (advogado), portanto **não testa diretamente H2/H5** (que miram advogados como cliente), mas mostra que **existe modelo de monetização legal-tech sem mensalidade** funcionando no BR.
- **[neutro H3]** Modelo success-fee direto ao consumidor tende a operar com **advogados parceiros por trás** (não achei confirmação explícita nesta busca de que Resolvvi seja operado só por não-advogados) — **gap relevante para H3**, não resolvido por esta frente (é escopo de "regulação", não "pricing").
- Nenhuma legaltech B2B (advogado como cliente) com success-fee foi encontrada nesta busca — sugere que success-fee é modelo B2C dominante, não B2B, no nicho jurídico brasileiro. **Ausência de dado é dado**: não há evidência de "SaaS + success fee híbrido" para advogados no mercado brasileiro pesquisado.

---

### 1.4 Freemium

- **Astrea PlanoLight**: grátis por 1 ano (40 processos, 1 usuário) — funciona como funil de entrada para planos pagos (upsell por volume de processos/usuários).
- **Nós 8**: consultoria jurídica freemium para empreendedores early-stage — 1.000+ atendidos, só 14 convertidos para acompanhamento contínuo pago. **Taxa de conversão implícita: ~1,4%** (14/1.000) — porém é modelo de consultoria humana, não SaaS puro, e a fonte não detalha se os 1.000 são todos "usuários freemium" no sentido SaaS.
- **LawX**: trial gratuito, sem dado de taxa de conversão encontrado.
- Nenhuma fonte encontrada com taxa de conversão freemium→pago específica de SaaS jurídico com IA no Brasil.

**Fonte:** [napratica.org.br — 3 legaltechs brasileiras](https://napratica.org.br/noticias/3-legaltechs-brasileiras) (fetch direto, 2026-07-04, **Tier 2** — veículo de conteúdo educacional/carreira, não é o próprio fornecedor, mas também não é analista de mercado formal).

**Mapa → hipótese:**
- **[refuta parcialmente H5]** O único dado de conversão freemium encontrado (~1,4%, Nós 8) é baixíssimo e vem de um modelo de consultoria manual, não escalável por IA — **não há evidência aqui de canal freemium eficiente e escalável** para um outsider. Isso é um dado fraco (N=1, modelo diferente) mas pesa contra a tese de "freemium resolve aquisição".

---

### 1.5 Benchmarks internacionais (referência de padrão, não conclusão sobre o mercado-alvo — conforme escopo negativo do P0)

| Ferramenta | Mercado | Preço |
|---|---|---|
| Clio (gestão de escritório) | EUA | US$ 49–159/usuário/mês (annual); +US$10/mês se mensal |
| Harvey AI (IA jurídica enterprise) | EUA/global, firms Am Law 100 | US$ 1.000–2.000/assento/mês (mid-market); US$ 100–200/assento em escala Am Law 100; mínimo 20 assentos + 12 meses = ~US$ 288.000/ano mínimo |

**Fonte:** [Clio Pricing](https://www.clio.com/pricing/) (via busca, não fetch direto — **Tier 3**, site oficial do fornecedor); [Harvey AI Pricing — eesel.ai](https://www.eesel.ai/blog/harvey-ai-pricing) (**Tier 3**, blog terceiro, dado "leaked", não oficial — Harvey não publica preço).

**Mapa → hipótese:**
- **[neutro, benchmark apenas]** Mostra que IA jurídica enterprise no exterior tem ticket 10-50x maior que o BR (US$1.000+ vs R$150-350) — a distância de preço reflete diferença de segmento (Am Law 100 vs. advogado solo BR), não diretamente comparável. Serve só como teto conceitual de "quanto IA jurídica pode valer quando o cliente tem orçamento", não como projeção para o operador solo/não-advogado mirando pequenos escritórios BR.

---

## 2. Dados de contexto de mercado (apoiam H1/H2 indiretamente)

- **1,3 milhão de advogados registrados na OAB no Brasil** — Fonte: [Perfil ADV — 1º Estudo Demográfico da Advocacia Brasileira](https://conhecimento.fgv.br/sites/default/files/2025-01/publicacoes/perfil_adv_1o-estudo_demografico_da_advocacia_brasileira.pdf), OAB Nacional + FGV Justiça, dados coletados ago-out/2023, publicado 2025. **Tier 1** (pesquisa institucional FGV/OAB).
- **64% dos advogados brasileiros ganham até R$ 6.600/mês** — citado a partir do mesmo estudo (fetch da matéria da Terra retornou 403; dado extraído via snippet de busca, **não confirmado na fonte primária PDF**, tratar como Tier 2 até validação direta do PDF).
- **Mercado jurídico brasileiro movimentou ~R$ 2 bilhões em investimentos nos últimos 18 meses** (legaltechs) — Fonte: artigo institucional AB2L/imprensa (via busca, **Tier 2**, sem link único verificado no fetch — necessário revalidar fonte primária).
- **Jusbrasil: 30+ milhões de usuários mensais ativos, cobertura de 80% dos advogados brasileiros, operação em breakeven, sem receita divulgada**, captou US$ 86,1 milhões em Series D (Warburg Pincus, out/2023), total de US$ 128 milhões captados. Pivotando para B2B/B2G (dobrar receita dessa linha). Fonte: [startups.com.br — Exclusivo: Jusbrasil atrai Warburg Pincus](https://startups.com.br/negocios/legaltech/exclusivo-jusbrasil-atrai-warburg-pincus-e-amplia-foco-no-b2b/) (fetch direto, 2026-07-04, **Tier 2** — imprensa especializada em startups).

**Mapa → hipótese:**
- **[refuta parcialmente H2]** Se 64% dos advogados ganham até R$ 6.600/mês, um SaaS de R$ 250-350/mês representa **4-5% da renda mensal** — ticket alto relativo à renda do segmento-alvo (autônomos/pequenos escritórios), o que pressiona conversão e sustenta a hipótese de que o preço de entrada real sustentável está mais perto de R$ 40-150/mês, não R$ 250+. Isso é sinal de alerta para H2, não confirmação — a economia do fundador solo pode não fechar nesse ticket mais baixo.
- **[confirma H6 indiretamente]** O próprio líder de mercado (Jusbrasil) está migrando o foco de B2C/advogado individual para **B2B/B2G** — sinaliza que o incumbente considera o segmento solo/pequeno menos lucrativo ou mais disputado, o que pode abrir espaço (lacuna) exatamente no segmento que H6 pergunta se é ocupável por um solo — mas também pode significar que esse segmento é ruim de monetizar (motivo do pivô), o que cortaria contra H2.

---

## 3. Lacunas (o que NÃO foi encontrado)

1. **Nenhum dado de churn/retenção publicado** para nenhuma legaltech brasileira (SaaS ou IA jurídica). Sem isso, não dá para calcular LTV real de nenhum concorrente citado — H2 fica sem triangulação de retenção, só de preço de lista.
2. **Nenhum benchmark de CAC específico do setor jurídico brasileiro** foi encontrado — apenas benchmarks genéricos de SaaS B2B Brasil (CAC R$ 3.000–15.000 para SMB, fonte não jurídica-específica, **Tier 3**, sem link de origem primária verificado no fetch do weehub — a fonte citada [Latitud LatAm Tech Report 2023] não foi acessada diretamente nesta coleta).
3. **Nenhuma taxa de conversão freemium→pago de SaaS jurídico de IA** foi encontrada (o único número, 1,4%, vem de consultoria manual, não SaaS de IA).
4. **Nenhum dado sobre número real de assinantes pagantes** de ADVBOX, Astrea, Projuris, ChatADV, Jurídico AI, Turivius, Judit — todos os incumbentes citados não divulgam volume de clientes publicamente (buscas não retornaram esse dado).
5. **Não foi possível acessar a fonte primária da Jusbrasil (jusbrasil.com.br/pro, ia.jusbrasil.com.br/planos)** — bloqueio HTTP 403 no fetch direto; os poucos números vieram de snippets de busca, não confirmados na origem.
6. **Nenhum modelo "success fee" B2B para advogados** (ex.: legaltech que cobra do escritório só em caso de recuperação de crédito bem-sucedida) foi encontrado — só exemplos B2C (Resolvvi/AirHelp). Se esse modelo existir no BR mirando escritórios como cliente, não apareceu nesta busca.
7. **Não foi encontrado dado consolidado e citável sobre "quanto do valor de uma ferramenta de IA jurídica paga já é entregue de graça pelo ChatGPT genérico"** — relevante para AH1/H4, mas é escopo mais de "concorrência" que de "pricing"; sinalizo o gap aqui pois cruza diretamente com H2 (o preço que o mercado aceita pagar hoje pode já embutir esse desconto competitivo do ChatGPT gratuito).

---

## 4. Sem fonte — impressão do coletor (não contam como evidência)

- Impressão: a compressão de preço entre "gestão pura" (R$ 40-220) e "IA jurídica" (R$ 150-700) sugere que o mercado brasileiro ainda trata IA como **add-on de precificação**, não como produto central — o que é coerente com a tese de que "ter IA" ainda não é, por si, o eixo de monetização dominante no BR (relevante para AH1, mas isso é opinião do coletor, não dado).
- Impressão: o fato de nenhuma legaltech pequena/de nicho ter dado de churn público é, em si, um padrão do setor (baixa maturidade de reporte), não necessariamente ausência real da métrica internamente.

---

## 5. Tabela consolidada de fontes

| # | Fonte | URL | Data de acesso | Tier | Nota |
|---|---|---|---|---|---|
| 1 | ADVBOX Planos | https://advbox.com.br/planos | 2026-07-04 | 3 | Fetch direto, fornecedor |
| 2 | Astrea Planos e Preços (Aurum) | https://www.aurum.com.br/astrea/planos-e-precos/ | 2026-07-04 | 3 | Fetch direto, fornecedor |
| 3 | Projuris — quanto custa software jurídico | https://www.projuris.com.br/blog/software-juridico/ | 2026-07-04 | 3 | Conflito de interesse — blog do próprio Projuris |
| 4 | ialocus.com.br — preço de IA jurídica 2026 | https://ialocus.com.br/blog/post-ia-juridica-preco.html | 2026-07-04 | 3 | Conflito de interesse — Locus é fornecedor concorrente citado no próprio ranking |
| 5 | Resolvvi — voo atrasado | https://www.resolvvi.com/problema-com-voo/voo-atrasado/ | 2026-07-04 | 3 | Fornecedor comercial primário |
| 6 | topensandoemviajar.com — experiência Resolvvi | https://www.topensandoemviajar.com/experiencia-real-resolvvi/ | 2026-07-04 | 3 | Blog de usuário, sem conflito comercial direto |
| 7 | napratica.org.br — 3 legaltechs brasileiras | https://napratica.org.br/noticias/3-legaltechs-brasileiras | 2026-07-04 | 2 | Veículo educacional/carreira |
| 8 | Clio Pricing | https://www.clio.com/pricing/ | 2026-07-04 (via busca) | 3 | Site oficial do fornecedor (EUA) |
| 9 | Harvey AI Pricing — eesel.ai | https://www.eesel.ai/blog/harvey-ai-pricing | 2026-07-04 (via busca) | 3 | Blog terceiro, dado "leaked" não oficial |
| 10 | Perfil ADV — 1º Estudo Demográfico da Advocacia Brasileira (OAB+FGV) | https://conhecimento.fgv.br/sites/default/files/2025-01/publicacoes/perfil_adv_1o-estudo_demografico_da_advocacia_brasileira.pdf | 2026-07-04 (via busca, PDF não fetchado diretamente) | 1 | Pesquisa institucional — mas dado de renda (64%/R$6.600) vem de snippet de reportagem terceira, não do PDF em si — **revalidar** |
| 11 | startups.com.br — Jusbrasil atrai Warburg Pincus | https://startups.com.br/negocios/legaltech/exclusivo-jusbrasil-atrai-warburg-pincus-e-amplia-foco-no-b2b/ | 2026-07-04 | 2 | Fetch direto, imprensa especializada em startups |
| 12 | weehub.com.br — benchmarking métricas SaaS 2026 | https://weehub.com.br/blog/benchmarking-metricas-saas-2026/ | 2026-07-04 | 3 | Blog comercial genérico, sem dado BR-específico confirmado; cita Latitud LatAm Tech Report 2023 sem fetch direto da fonte primária |
| 13 | AB2L Notícias — mercado de lawtechs no Brasil | https://ab2l.org.br/noticias/mercado-de-lawtechs-no-brasil/ | 2026-07-04 (via busca, não fetchado diretamente) | 2 | Associação setorial — fonte adequada para P0, mas não fetchada diretamente nesta coleta; revalidar |
| 14 | Jusbrasil Planos (pro) e JusIA planos | https://www.jusbrasil.com.br/pro / https://ia.jusbrasil.com.br/planos | tentativa 2026-07-04 | — | **Fetch falhou (HTTP 403)** — dados de preço não confirmados na origem |

---

## 6. Resumo do estado das hipóteses após esta frente

- **H1 (dor paga):** neutro/apoio indireto — existe pagamento real por ferramentas (R$40–700/mês), mas nenhuma evidência direta de que o workflow específico de IA seja o que gera esse pagamento vs. gestão processual tradicional.
- **H2 (economia fecha para solo):** **sinal de alerta, não confirmação nem refutação plena.** Ticket de IA jurídica (R$150-350) representa 2-5% da renda mensal de 64% dos advogados — margem apertada; ausência total de dados de CAC/churn específicos do setor impede conclusão robusta. Requer triangulação futura (P2+).
- **H4 (defensabilidade):** neutro — preço-prêmio de ferramentas de IA sobre gestão pura sugere alguma disposição a pagar por IA, mas não prova fosso; nenhum dado de retenção encontrado.
- **H5 (canal de aquisição):** enfraquecido — único dado de conversão freemium (1,4%) é fraco e de modelo diferente (consultoria manual); nenhum canal de aquisição escalável para outsider foi documentado nesta frente (é mais escopo de outra frente, mas cruza aqui via freemium).
- **H6 (lacuna ocupável):** leve apoio — pivô do Jusbrasil para B2B/B2G pode sinalizar lacuna no segmento solo/pequeno, mas é ambíguo (pode ser lacuna ruim de monetizar, não lacuna boa).

---

*P1 (frente pricing-modelos) — coleta concluída. 14 fontes citadas: 1 Tier 1 (dado parcialmente não confirmado na origem primária), 4 Tier 2, 9 Tier 3 (6 com conflito de interesse comercial explícito, tagueadas).*

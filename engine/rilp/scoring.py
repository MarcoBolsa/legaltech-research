"""Motor de score determinístico e gate G2→3 do RILP Engine (Fase C — leva 1).

Este módulo materializa a vantagem competitiva do RILP: **auditabilidade
recomputável**. Toda saída é reproduzível a partir de `claims.yaml` — um terceiro
recalcula o veredito com a mesma conta (comparacao.md §2).

Fórmula canônica (RILP §348, imutável):
    produto(claim) = pontos × peso
    Score do run   = Σ produto ÷ Σ peso
    Gate G2→3 PASSA sse: Score ≥ 70 E nenhum claim decisório (peso=3) em bucket Baixo
"""

from __future__ import annotations

from rilp.models import Bucket, ClaimsDoc, GateResult, ScoreResult, ScoreRow

#: Piso do Score do run para o gate G2→3 (RILP §352).
SCORE_FLOOR = 70


def compute_score(doc: ClaimsDoc) -> ScoreResult:
    """Recomputa o Score do run a partir dos claims — média ponderada por peso.

    Score = Σ(pontos × peso) ÷ Σ(peso), arredondado a 1 casa decimal.
    """
    tabela: list[ScoreRow] = []
    soma_produtos = 0
    soma_pesos = 0

    for claim in doc.claims:
        produto = claim.produto
        tabela.append(
            ScoreRow(
                claim=claim.id,
                bucket=claim.bucket,
                pontos=claim.pontos,
                peso=claim.peso,
                produto=produto,
            )
        )
        soma_produtos += produto
        soma_pesos += claim.peso

    score_percent = round(soma_produtos / soma_pesos, 1) if soma_pesos else 0.0

    return ScoreResult(
        tabela=tabela,
        soma_produtos=soma_produtos,
        soma_pesos=soma_pesos,
        score_percent=score_percent,
    )


def check_gate(doc: ClaimsDoc, score: ScoreResult) -> GateResult:
    """Avalia o gate bloqueador G2→3.

    PASSA sse: Score ≥ 70 (cond1) E nenhum claim decisório em Baixo (cond2).
    Um decisório em Baixo reprova mesmo com score ≥ 70 — mecanismo anti-contaminação.
    """
    cond1 = score.score_percent >= SCORE_FLOOR

    decisorios_em_baixo = [
        claim.id for claim in doc.claims if claim.decisorio and claim.bucket == Bucket.BAIXO
    ]
    cond2 = len(decisorios_em_baixo) == 0

    passou = cond1 and cond2
    resultado = "PASS" if passou else "FAIL"
    natureza = _gate_natureza(cond1, cond2, score.score_percent, decisorios_em_baixo)

    return GateResult(
        cond1_score_ge_70=cond1,
        cond2_no_decisorio_baixo=cond2,
        decisorios_em_baixo=decisorios_em_baixo,
        resultado=resultado,
        natureza=natureza,
    )


def _gate_natureza(
    cond1: bool, cond2: bool, score_percent: float, decisorios_em_baixo: list[str]
) -> str:
    """Frase legível explicando por que o gate passou ou reprovou."""
    if cond1 and cond2:
        return f"Aprova: score {score_percent}% ≥ {SCORE_FLOOR}% e nenhum decisório em Baixo."

    motivos: list[str] = []
    if not cond1:
        motivos.append(f"score {score_percent}% < {SCORE_FLOOR}%")
    if not cond2:
        motivos.append(f"decisórios em Baixo: {', '.join(decisorios_em_baixo)}")
    return "Reprova: " + "; ".join(motivos) + "."


def validate_consistency(doc: ClaimsDoc) -> list[str]:
    """Valida a integridade do artefato: pontos declarados vs. âncora do bucket.

    Retorna uma lista de warnings (vazia = artefato íntegro). Cada claim cujo
    `pontos` declarado divirja do ponto-âncora do bucket gera um warning.
    """
    warnings: list[str] = []
    for claim in doc.claims:
        ancora = claim.bucket.pontos
        if claim.pontos != ancora:
            warnings.append(
                f"{claim.id}: pontos declarados {claim.pontos} ≠ "
                f"ancora {ancora} do bucket {claim.bucket.value}"
            )
    return warnings


def audit_trail(doc: ClaimsDoc) -> str:
    """Gera o relatório markdown recomputável — a 'conta inteira' auditável.

    Contém: tabela claim|bucket|pontos|peso|produto, somas, score, resultado do
    gate e a lista de decisórios em Baixo. É o valor central do engine: qualquer
    um recalcula o veredito a partir daqui.
    """
    score = compute_score(doc)
    gate = check_gate(doc, score)

    lines: list[str] = []
    lines.append("# Trilha de auditoria — Score do run e Gate G2→3")
    lines.append("")
    run_id = doc.meta.get("run_id", "—")
    lines.append(f"**Run:** {run_id}")
    lines.append("")
    lines.append("## Score do run")
    lines.append("")
    lines.append("| Claim | Bucket | Pontos | Peso | Produto |")
    lines.append("|-------|--------|-------:|-----:|--------:|")
    for row in score.tabela:
        lines.append(
            f"| {row.claim} | {row.bucket.value} | {row.pontos} | {row.peso} | {row.produto} |"
        )
    lines.append(f"| **Σ** | | | **{score.soma_pesos}** | **{score.soma_produtos}** |")
    lines.append("")
    lines.append(
        f"**Score = Σprodutos ÷ Σpesos = {score.soma_produtos} ÷ {score.soma_pesos} "
        f"= {score.score_percent}%**"
    )
    lines.append("")
    lines.append("## Gate G2→3")
    lines.append("")
    lines.append(f"- Condição 1 (Score ≥ {SCORE_FLOOR}%): {_sim_nao(gate.cond1_score_ge_70)}")
    cond2_str = _sim_nao(gate.cond2_no_decisorio_baixo)
    lines.append(f"- Condição 2 (nenhum decisório em Baixo): {cond2_str}")
    if gate.decisorios_em_baixo:
        lines.append(f"- Decisórios em Baixo: {', '.join(gate.decisorios_em_baixo)}")
    else:
        lines.append("- Decisórios em Baixo: nenhum")
    lines.append("")
    lines.append(f"**Resultado: {gate.resultado}** — {gate.natureza}")
    lines.append("")

    warnings = validate_consistency(doc)
    if warnings:
        lines.append("## Warnings de consistência")
        lines.append("")
        for w in warnings:
            lines.append(f"- {w}")
        lines.append("")

    return "\n".join(lines)


def _sim_nao(valor: bool) -> str:
    return "✅ atende" if valor else "❌ falha"

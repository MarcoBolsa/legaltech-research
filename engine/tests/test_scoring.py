"""Testes do motor de score e gate G2→3 (Fase C — leva 1).

Inclui o TESTE DE ACEITAÇÃO de integração contra o claims.yaml real do Run #0:
score == 63.4, gate == FAIL, decisórios em Baixo == {C5b, C6}.
"""

from __future__ import annotations

from pathlib import Path

from rilp.models import Bucket, Claim, ClaimsDoc, Peso
from rilp.scoring import (
    audit_trail,
    check_gate,
    compute_score,
    validate_consistency,
)

# Caminho robusto ao claims.yaml real (independe do cwd de execução).
REAL_CLAIMS = (
    Path(__file__).parents[2] / "runs" / "run-000-legaltech" / "p2" / "claims.yaml"
)


def _claim(cid: str, bucket: Bucket, peso: int, pontos: int | None = None) -> Claim:
    """Fábrica de claim consistente (pontos = âncora do bucket por padrão)."""
    return Claim(
        id=cid,
        enunciado=f"claim {cid}",
        bucket=bucket,
        pontos=pontos if pontos is not None else bucket.pontos,
        peso=peso,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Enums e propriedades de domínio
# ─────────────────────────────────────────────────────────────────────────────


def test_bucket_pontos_ancora():
    assert Bucket.ALTO.pontos == 90
    assert Bucket.MEDIO.pontos == 65
    assert Bucket.BAIXO.pontos == 25


def test_peso_valores():
    assert Peso.DECISORIO == 3
    assert Peso.RELEVANTE == 2
    assert Peso.CONTEXTUAL == 1


def test_claim_produto_e_decisorio():
    c = _claim("Cx", Bucket.ALTO, peso=3)
    assert c.produto == 270
    assert c.decisorio is True
    assert _claim("Cy", Bucket.MEDIO, peso=2).decisorio is False


# ─────────────────────────────────────────────────────────────────────────────
# compute_score — exemplo à mão do RILP §350
# ─────────────────────────────────────────────────────────────────────────────


def test_compute_score_exemplo_a_mao():
    """6 claims peso 1 — 3 Alto, 2 Médio, 1 Baixo → 425 ÷ 6 = 70,8%."""
    doc = ClaimsDoc(
        meta={},
        claims=[
            _claim("A1", Bucket.ALTO, peso=1),
            _claim("A2", Bucket.ALTO, peso=1),
            _claim("A3", Bucket.ALTO, peso=1),
            _claim("M1", Bucket.MEDIO, peso=1),
            _claim("M2", Bucket.MEDIO, peso=1),
            _claim("B1", Bucket.BAIXO, peso=1),
        ],
    )
    result = compute_score(doc)
    assert result.soma_produtos == 425
    assert result.soma_pesos == 6
    assert result.score_percent == 70.8
    assert len(result.tabela) == 6


def test_compute_score_tabela_produtos():
    doc = ClaimsDoc(claims=[_claim("C1", Bucket.ALTO, peso=3)])
    result = compute_score(doc)
    assert result.tabela[0].produto == 270
    assert result.soma_produtos == 270
    assert result.soma_pesos == 3


def test_compute_score_sem_claims_nao_quebra():
    result = compute_score(ClaimsDoc(claims=[]))
    assert result.score_percent == 0.0
    assert result.soma_pesos == 0


# ─────────────────────────────────────────────────────────────────────────────
# check_gate
# ─────────────────────────────────────────────────────────────────────────────


def test_gate_pass_quando_score_alto_e_sem_decisorio_baixo():
    doc = ClaimsDoc(
        claims=[
            _claim("A1", Bucket.ALTO, peso=3),
            _claim("A2", Bucket.ALTO, peso=2),
        ]
    )
    score = compute_score(doc)
    gate = check_gate(doc, score)
    assert score.score_percent >= 70
    assert gate.resultado == "PASS"
    assert gate.cond1_score_ge_70 is True
    assert gate.cond2_no_decisorio_baixo is True
    assert gate.decisorios_em_baixo == []


def test_gate_fail_decisorio_em_baixo_mesmo_com_score_alto():
    """Mecanismo anti-contaminação: score ≥ 70 mas um decisório em Baixo → FAIL."""
    doc = ClaimsDoc(
        claims=[
            _claim("A1", Bucket.ALTO, peso=2),
            _claim("A2", Bucket.ALTO, peso=2),
            _claim("A3", Bucket.ALTO, peso=2),
            _claim("A4", Bucket.ALTO, peso=2),
            _claim("D1", Bucket.BAIXO, peso=3),  # decisório em Baixo
        ]
    )
    score = compute_score(doc)
    gate = check_gate(doc, score)
    assert score.score_percent >= 70  # a média sozinha passaria o piso
    assert gate.cond1_score_ge_70 is True
    assert gate.cond2_no_decisorio_baixo is False
    assert gate.resultado == "FAIL"
    assert gate.decisorios_em_baixo == ["D1"]
    assert "D1" in gate.natureza


def test_gate_fail_por_score_baixo():
    doc = ClaimsDoc(
        claims=[
            _claim("B1", Bucket.BAIXO, peso=1),
            _claim("M1", Bucket.MEDIO, peso=1),
        ]
    )
    score = compute_score(doc)
    gate = check_gate(doc, score)
    assert gate.cond1_score_ge_70 is False
    assert gate.resultado == "FAIL"


# ─────────────────────────────────────────────────────────────────────────────
# validate_consistency
# ─────────────────────────────────────────────────────────────────────────────


def test_validate_consistency_sem_warnings():
    doc = ClaimsDoc(claims=[_claim("C1", Bucket.ALTO, peso=3)])
    assert validate_consistency(doc) == []


def test_validate_consistency_detecta_divergencia():
    doc = ClaimsDoc(claims=[_claim("C1", Bucket.ALTO, peso=3, pontos=80)])
    warnings = validate_consistency(doc)
    assert len(warnings) == 1
    assert "C1" in warnings[0]
    assert "80" in warnings[0]
    assert "90" in warnings[0]


# ─────────────────────────────────────────────────────────────────────────────
# audit_trail
# ─────────────────────────────────────────────────────────────────────────────


def test_audit_trail_contem_conta_e_veredito():
    doc = ClaimsDoc(
        meta={"run_id": "test-run"},
        claims=[_claim("C1", Bucket.ALTO, peso=3)],
    )
    report = audit_trail(doc)
    assert "test-run" in report
    assert "270" in report  # produto
    assert "Score" in report
    assert "Gate G2→3" in report


# ─────────────────────────────────────────────────────────────────────────────
# TESTE DE ACEITAÇÃO — contra o Run #0 real
# ─────────────────────────────────────────────────────────────────────────────


def test_aceitacao_run000_score_e_gate_reais():
    """Carrega o claims.yaml REAL do Run #0 e reproduz score 63.4 / gate FAIL."""
    assert REAL_CLAIMS.exists(), f"claims.yaml real não encontrado em {REAL_CLAIMS}"

    doc = ClaimsDoc.from_yaml(REAL_CLAIMS)
    assert len(doc.claims) == 10  # C1..C9 com C5a/C5b

    score = compute_score(doc)
    assert score.soma_produtos == 1585
    assert score.soma_pesos == 25
    assert score.score_percent == 63.4

    gate = check_gate(doc, score)
    assert gate.resultado == "FAIL"
    assert gate.cond1_score_ge_70 is False
    assert gate.cond2_no_decisorio_baixo is False
    assert set(gate.decisorios_em_baixo) == {"C5b", "C6"}


def test_aceitacao_run000_artefato_integro():
    """O claims.yaml real deve ser internamente consistente (pontos = âncora)."""
    doc = ClaimsDoc.from_yaml(REAL_CLAIMS)
    assert validate_consistency(doc) == []


# ─────────────────────────────────────────────────────────────────────────────
# ENDURECIMENTO ADVERSARIAL (leva 4) — edge cases de cálculo/gate
# ─────────────────────────────────────────────────────────────────────────────


def test_peso_ausente_assume_default_contextual():
    """Contrato canônico (spec + docstring): peso omitido = CONTEXTUAL (1).

    Regressão do bug: o campo não tinha default e um claims.yaml sem peso
    quebrava com ValidationError, contradizendo o contrato documentado.
    """
    c = Claim(id="X", bucket=Bucket.ALTO, pontos=90)
    assert c.peso == Peso.CONTEXTUAL.value == 1
    assert c.decisorio is False
    assert c.produto == 90  # 90 × 1


def test_peso_fora_de_faixa_e_rejeitado():
    """peso deve ficar em 1..3 — valores 0 ou 4 são rejeitados na validação."""
    import pytest
    from pydantic import ValidationError

    for peso_invalido in (0, 4, -1):
        with pytest.raises(ValidationError):
            Claim(id="X", bucket=Bucket.ALTO, pontos=90, peso=peso_invalido)


def test_compute_score_usa_pontos_declarados_nao_ancora():
    """Determinismo: o score usa os `pontos` DECLARADOS, não o âncora do bucket.

    Claim marcado bucket=Alto mas pontos=25 contribui 25×peso — validate_consistency
    apenas AVISA da divergência; o cálculo respeita o declarado (contrato spec).
    """
    doc = ClaimsDoc(claims=[Claim(id="C1", bucket=Bucket.ALTO, pontos=25, peso=2)])
    result = compute_score(doc)
    assert result.soma_produtos == 50  # 25 × 2, não 90 × 2
    assert result.score_percent == 25.0
    warns = validate_consistency(doc)
    assert len(warns) == 1 and "C1" in warns[0]


def test_gate_score_exatamente_70_passa():
    """Knife-edge: Score == 70.0 satisfaz cond1 (>= 70), não > 70."""
    # 2 claims peso 1: Alto(90) + declarado 50 → 140 ÷ 2 = 70.0
    doc = ClaimsDoc(
        claims=[
            _claim("A1", Bucket.ALTO, peso=1),
            Claim(id="X1", bucket=Bucket.MEDIO, pontos=50, peso=1),
        ]
    )
    score = compute_score(doc)
    assert score.score_percent == 70.0
    gate = check_gate(doc, score)
    assert gate.cond1_score_ge_70 is True
    assert gate.resultado == "PASS"


def test_gate_fail_por_cond1_mesmo_com_todos_decisorios_alto():
    """cond1 sozinha reprova: decisórios todos em Alto, mas média < 70."""
    # Alto(90)×3 decisório = 270; Baixo(25)×3 = 75 → (270+75)/(3+3)? não.
    # Queremos score < 70 sem nenhum decisório em Baixo:
    doc = ClaimsDoc(
        claims=[
            _claim("D1", Bucket.ALTO, peso=3),  # decisório Alto
            _claim("B1", Bucket.BAIXO, peso=1),
            _claim("B2", Bucket.BAIXO, peso=1),
            _claim("B3", Bucket.BAIXO, peso=1),
            _claim("B4", Bucket.BAIXO, peso=1),
            _claim("B5", Bucket.BAIXO, peso=1),
        ]
    )
    score = compute_score(doc)
    assert score.score_percent < 70
    gate = check_gate(doc, score)
    assert gate.cond1_score_ge_70 is False
    assert gate.cond2_no_decisorio_baixo is True  # nenhum decisório em Baixo
    assert gate.resultado == "FAIL"  # reprova SÓ por cond1
    assert gate.decisorios_em_baixo == []


def test_gate_avalia_score_arredondado_documenta_knife_edge():
    """DOCUMENTADO (dívida técnica): o gate usa o Score ARREDONDADO/auditável.

    Σproduto=1399, Σpeso=20 → raw 69.95 (< 70 matematicamente), mas o Score
    exibido/auditado é round(69.95, 1) = 70.0, então o gate PASSA. É a mesma
    conta que um terceiro vê — auditável — mas um humano deve confirmar que 70
    é um piso arredondado, não estrito. Ver relatório de QA (leva 4).
    """
    claims = [Claim(id="c0", bucket=Bucket.ALTO, pontos=1399, peso=1)]
    claims += [Claim(id=f"c{i}", bucket=Bucket.BAIXO, pontos=0, peso=1) for i in range(1, 20)]
    doc = ClaimsDoc(claims=claims)
    score = compute_score(doc)
    assert score.soma_produtos == 1399
    assert score.soma_pesos == 20
    assert 1399 / 20 == 69.95  # raw < 70
    assert score.score_percent == 70.0  # exibido = arredondado
    gate = check_gate(doc, score)
    assert gate.cond1_score_ge_70 is True  # gate no valor exibido → PASS


# ─────────────────────────────────────────────────────────────────────────────
# META-TESTE DE AUDITABILIDADE — o diferencial de produto do RILP
# ─────────────────────────────────────────────────────────────────────────────


def test_auditabilidade_terceiro_recomputa_veredito_do_run000():
    """Prova o claim central de marketing: um TERCEIRO recomputa o veredito.

    A 'conta inteira' (Σprodutos=1585, Σpesos=25, Score=63.4 = 1585 ÷ 25) e o
    veredito FAIL com os decisórios C5b/C6 estão TODOS presentes e corretos no
    texto do audit_trail — sem precisar rodar o motor de novo (comparacao.md §2).
    """
    doc = ClaimsDoc.from_yaml(REAL_CLAIMS)
    trilha = audit_trail(doc)

    # A conta exposta na trilha, verificável a olho:
    assert "1585" in trilha  # Σ produtos
    assert "25" in trilha  # Σ pesos
    assert "63.4" in trilha  # Score
    assert "1585 ÷ 25" in trilha  # a divisão explícita
    assert "63.4%" in trilha

    # O veredito e os claims decisórios reprovados aparecem por extenso:
    assert "FAIL" in trilha
    assert "C5b" in trilha and "C6" in trilha

    # E os números batem com o cálculo independente:
    score = compute_score(doc)
    assert f"{score.soma_produtos} ÷ {score.soma_pesos} = {score.score_percent}%" in trilha

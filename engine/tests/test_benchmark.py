"""Testes do harness de benchmark RILP × baseline (Fase C — leva 2, frente B).

Inclui o TESTE DE ACEITAÇÃO que reproduz o veredito real do Run #0
(comparacao.md §1): média A = 7.1, média B = 9.1, vencedor B, kill NÃO dispara.
"""

from __future__ import annotations

from pathlib import Path

from rilp.benchmark import (
    CRITERIOS,
    BenchmarkInput,
    DocScore,
    evaluate,
    render_report,
)

FIXTURE = Path(__file__).parent / "fixtures" / "benchmark.yaml"


def _doc(nome: str, notas: tuple[float, float, float, float], vale_500: bool) -> DocScore:
    r, aud, hon, aci = notas
    return DocScore(
        nome=nome,
        rigor_evidencia=r,
        auditabilidade=aud,
        honestidade_epistemica=hon,
        acionabilidade=aci,
        vale_500=vale_500,
    )


# ─────────────────────────────────────────────────────────────────────────────
# CRITERIOS
# ─────────────────────────────────────────────────────────────────────────────


def test_criterios_tem_4_itens():
    assert len(CRITERIOS) == 4
    assert CRITERIOS == [
        "rigor_evidencia",
        "auditabilidade",
        "honestidade_epistemica",
        "acionabilidade",
    ]


# ─────────────────────────────────────────────────────────────────────────────
# DocScore.media
# ─────────────────────────────────────────────────────────────────────────────


def test_media_calcula_media_dos_4_criterios():
    doc = _doc("X", (8.0, 6.0, 10.0, 8.0), vale_500=True)
    assert doc.media == 8.0


def test_media_arredonda_a_1_casa():
    doc = _doc("X", (7.5, 6.0, 6.5, 8.5), vale_500=True)
    assert doc.media == 7.1


# ─────────────────────────────────────────────────────────────────────────────
# Kill check
# ─────────────────────────────────────────────────────────────────────────────


def test_kill_dispara_quando_doc_b_nao_vale_500():
    doc_a = _doc("A", (8.0, 8.0, 8.0, 8.0), vale_500=True)
    doc_b = _doc("B", (9.0, 9.0, 9.0, 9.0), vale_500=False)
    inp = BenchmarkInput(run_id="r1", doc_a=doc_a, doc_b=doc_b)
    result = evaluate(inp)
    assert result.kill_disparado is True
    assert "não vale R$500" in result.kill_motivo


def test_kill_dispara_quando_doc_b_nao_supera_baseline():
    doc_a = _doc("A", (8.0, 8.0, 8.0, 8.0), vale_500=True)
    doc_b = _doc("B", (7.0, 7.0, 7.0, 7.0), vale_500=True)
    inp = BenchmarkInput(run_id="r1", doc_a=doc_a, doc_b=doc_b)
    result = evaluate(inp)
    assert result.kill_disparado is True
    assert "superior ao baseline" in result.kill_motivo


def test_kill_dispara_quando_doc_b_empata_com_baseline():
    """media_b <= media_a dispara kill — empate também não é 'superior'."""
    doc_a = _doc("A", (8.0, 8.0, 8.0, 8.0), vale_500=True)
    doc_b = _doc("B", (8.0, 8.0, 8.0, 8.0), vale_500=True)
    inp = BenchmarkInput(run_id="r1", doc_a=doc_a, doc_b=doc_b)
    result = evaluate(inp)
    assert result.kill_disparado is True


def test_continue_quando_doc_b_vence_e_vale_500():
    doc_a = _doc("A", (6.0, 6.0, 6.0, 6.0), vale_500=True)
    doc_b = _doc("B", (9.0, 9.0, 9.0, 9.0), vale_500=True)
    inp = BenchmarkInput(run_id="r1", doc_a=doc_a, doc_b=doc_b)
    result = evaluate(inp)
    assert result.kill_disparado is False
    assert result.vencedor == "B"
    assert "CONTINUE" in result.veredito


def test_vencedor_empate_quando_diferenca_pequena():
    doc_a = _doc("A", (8.0, 8.0, 8.0, 8.0), vale_500=True)
    doc_b = _doc("B", (8.05, 8.05, 8.05, 8.0), vale_500=True)
    inp = BenchmarkInput(run_id="r1", doc_a=doc_a, doc_b=doc_b)
    result = evaluate(inp)
    assert result.vencedor == "empate"


# ─────────────────────────────────────────────────────────────────────────────
# render_report
# ─────────────────────────────────────────────────────────────────────────────


def test_render_report_contem_tabela_e_veredito():
    doc_a = _doc("Doc A", (7.5, 6.0, 6.5, 8.5), vale_500=True)
    doc_b = _doc("Doc B", (9.0, 9.5, 9.5, 8.5), vale_500=True)
    inp = BenchmarkInput(run_id="run-000-legaltech", doc_a=doc_a, doc_b=doc_b)
    result = evaluate(inp)
    report = render_report(inp, result)
    assert "Tabela de notas" in report
    assert "7.1" in report
    assert "9.1" in report
    assert "CONTINUE" in report


# ─────────────────────────────────────────────────────────────────────────────
# TESTE DE ACEITAÇÃO — reproduz o veredito real do Run #0 (comparacao.md §1)
# ─────────────────────────────────────────────────────────────────────────────


def test_aceitacao_run000_veredito_real():
    assert FIXTURE.exists(), f"fixture não encontrada em {FIXTURE}"

    inp = BenchmarkInput.from_yaml(FIXTURE)
    assert inp.run_id == "run-000-legaltech"

    result = evaluate(inp)
    assert result.media_a == 7.1
    assert result.media_b == 9.1
    assert result.vencedor == "B"
    assert result.kill_disparado is False

"""Testes do Domain Pack (Fase C — leva 2, frente A).

Inclui o TESTE DE ACEITAÇÃO de integração contra o claims.yaml + hypotheses.md
reais do Run #0: stage=="parcial", n_runs==1, 10 hipóteses (C1..C9 + C5a/C5b),
e unit_econ_benchmark sinalizando o GAP de CAC/LTV/churn (nunca inventado).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from rilp.domain_pack import (
    DomainPack,
    DomainPackMeta,
    build_partial_pack_from_run,
    validate_pack,
)

REAL_CLAIMS = Path(__file__).parents[2] / "runs" / "run-000-legaltech" / "p2" / "claims.yaml"
REAL_HYPOTHESES = Path(__file__).parents[2] / "runs" / "run-000-legaltech" / "p0" / "hypotheses.md"


def _minimal_pack(stage: str, n_runs: int) -> DomainPack:
    return DomainPack(
        meta=DomainPackMeta(
            domain="legaltech",
            version="1.0",
            stage=stage,
            run_ids=["run-000-legaltech"][:n_runs] or [],
            n_runs=n_runs,
        )
    )


# ─────────────────────────────────────────────────────────────────────────────
# Regra dos 2 estágios (RILP §708-710, Princípio 5)
# ─────────────────────────────────────────────────────────────────────────────


def test_validate_pack_vendavel_com_n_runs_1_reprova():
    pack = _minimal_pack("vendavel", 1)
    errors = validate_pack(pack)
    assert errors
    assert any("vendavel" in e for e in errors)


def test_validate_pack_parcial_com_n_runs_1_ok():
    pack = _minimal_pack("parcial", 1)
    assert validate_pack(pack) == []


def test_validate_pack_vendavel_com_n_runs_2_ok():
    pack = DomainPack(
        meta=DomainPackMeta(
            domain="legaltech",
            version="1.0",
            stage="vendavel",
            run_ids=["run-000-legaltech", "run-001-legaltech"],
            n_runs=2,
        )
    )
    assert validate_pack(pack) == []


def test_validate_pack_zero_runs_reprova():
    pack = _minimal_pack("parcial", 0)
    errors = validate_pack(pack)
    assert errors
    assert any("n_runs" in e for e in errors)


# ─────────────────────────────────────────────────────────────────────────────
# Roundtrip to_yaml / from_yaml
# ─────────────────────────────────────────────────────────────────────────────


def test_roundtrip_to_yaml_from_yaml_preserva_dados(tmp_path):
    pack = DomainPack(
        meta=DomainPackMeta(
            domain="legaltech",
            version="1.0",
            stage="parcial",
            run_ids=["run-000-legaltech"],
            n_runs=1,
            generated_at="2026-07-04",
        ),
        hypotheses_validated=[
            {
                "id": "C1",
                "enunciado": "x",
                "verdict": "confirmada",
                "bucket": "Alto",
                "confianca": 90,
            }
        ],
        icp_real={"status": "GAP"},
        unit_econ_benchmark={"status": "GAP — CAC ausente"},
        vocabulario_cliente=["prazo perdido"],
        failures_learned=["freemium não converteu"],
        heatmap_regulatorio=[{"claim_id": "C1", "url": "https://x", "tier": 1, "nota": "n"}],
        stack_validada=["PJe"],
    )

    out_path = tmp_path / "pack.yaml"
    pack.to_yaml(out_path)
    assert out_path.exists()

    loaded = DomainPack.from_yaml(out_path)
    assert loaded == pack


# ─────────────────────────────────────────────────────────────────────────────
# ACEITAÇÃO — build_partial_pack_from_run contra os artefatos reais do Run #0
# ─────────────────────────────────────────────────────────────────────────────


@pytest.fixture(scope="module")
def real_pack() -> DomainPack:
    return build_partial_pack_from_run(
        claims_yaml_path=REAL_CLAIMS,
        hypotheses_md_path=REAL_HYPOTHESES,
        domain="legaltech",
        run_id="run-000-legaltech",
    )


def test_build_partial_pack_stage_e_n_runs(real_pack: DomainPack):
    assert real_pack.meta.stage == "parcial"
    assert real_pack.meta.n_runs == 1
    assert real_pack.meta.run_ids == ["run-000-legaltech"]
    assert validate_pack(real_pack) == []


def test_build_partial_pack_10_hipoteses(real_pack: DomainPack):
    assert len(real_pack.hypotheses_validated) == 10
    ids = {h["id"] for h in real_pack.hypotheses_validated}
    assert ids == {"C1", "C2", "C3", "C4", "C5a", "C5b", "C6", "C7", "C8", "C9"}


def test_build_partial_pack_unit_econ_sinaliza_gap_sem_inventar(real_pack: DomainPack):
    status = real_pack.unit_econ_benchmark.get("status", "")
    assert "GAP" in status
    assert "CAC" in status
    # honestidade epistêmica: não inventa número de CAC/LTV/churn em lugar nenhum
    dump = str(real_pack.unit_econ_benchmark)
    assert "R$" not in dump


def test_build_partial_pack_heatmap_regulatorio_apenas_tier_1_2(real_pack: DomainPack):
    assert real_pack.heatmap_regulatorio
    for item in real_pack.heatmap_regulatorio:
        assert item["tier"] in (1, 2)
    claim_ids_no_heatmap = {item["claim_id"] for item in real_pack.heatmap_regulatorio}
    # C1 (H3) e C6 (H5) tocam regulação/canal — devem aparecer no heatmap.
    assert {"C1", "C6"}.issubset(claim_ids_no_heatmap)


def test_build_partial_pack_hypotheses_md_ausente_levanta_erro(tmp_path):
    with pytest.raises(FileNotFoundError):
        build_partial_pack_from_run(
            claims_yaml_path=REAL_CLAIMS,
            hypotheses_md_path=tmp_path / "nao-existe.md",
            domain="legaltech",
            run_id="run-000-legaltech",
        )

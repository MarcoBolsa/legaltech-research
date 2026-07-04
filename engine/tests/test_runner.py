"""Testes do runner P0→P2 e da CLI (Fase C — leva 3, integração).

Inclui o TESTE E2E que roda o Run Mínimo Viável contra o Run #0 REAL
(`runs/run-000-legaltech/`) e valida a DISTINÇÃO ARQUITETURAL central:
gate G2→3 (bloqueador de avanço) e kill criterion (valor do protocolo) são
ortogonais e reportados como campos separados — nunca colapsados.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from rilp.cli import main
from rilp.runner import (
    RunManifest,
    RunReport,
    init_run,
    run_gate_g2_3,
    run_kill_check,
    run_minimo_viavel,
    validate_artifacts,
)

#: Raiz do repo (engine/tests/test_runner.py → parents[2] = repo root).
REPO_ROOT = Path(__file__).parents[2]
RUN000 = REPO_ROOT / "runs" / "run-000-legaltech"

_KILL = "Se o artefato não valer R$500 nem vencer o baseline, descontinuar o protocolo."


# ─────────────────────────────────────────────────────────────────────────────
# RunManifest — condição de morte obrigatória (RILP §1008)
# ─────────────────────────────────────────────────────────────────────────────


def test_manifest_recusa_kill_criterion_vazio():
    with pytest.raises(ValueError):
        RunManifest(run_id="r1", domain="D", kill_criterion="")


def test_manifest_recusa_kill_criterion_so_espacos():
    with pytest.raises(ValueError):
        RunManifest(run_id="r1", domain="D", kill_criterion="   ")


def test_manifest_roundtrip_yaml(tmp_path: Path):
    manifest = RunManifest(run_id="r1", domain="Fintech", kill_criterion=_KILL)
    path = tmp_path / "MANIFEST.yaml"
    manifest.to_yaml(path)
    reloaded = RunManifest.from_yaml(path)
    assert reloaded.run_id == "r1"
    assert reloaded.domain == "Fintech"
    assert reloaded.kill_criterion == _KILL


# ─────────────────────────────────────────────────────────────────────────────
# init_run
# ─────────────────────────────────────────────────────────────────────────────


def test_init_run_cria_estrutura_e_manifest(tmp_path: Path):
    run_dir = init_run(tmp_path, "run-001-x", "LegalTech", _KILL)

    assert run_dir == tmp_path / "run-001-x"
    for sub in ("p0", "p1", "p2", "baseline"):
        assert (run_dir / sub).is_dir(), f"subpasta {sub} não criada"

    manifest_path = run_dir / "MANIFEST.yaml"
    assert manifest_path.is_file()
    manifest = RunManifest.from_yaml(manifest_path)
    assert manifest.run_id == "run-001-x"
    assert manifest.domain == "LegalTech"
    assert manifest.kill_criterion == _KILL


def test_init_run_recusa_kill_vazio_sem_efeito_no_disco(tmp_path: Path):
    with pytest.raises(ValueError):
        init_run(tmp_path, "run-002-x", "LegalTech", "")
    # A validação precede qualquer efeito colateral: nada foi criado.
    assert not (tmp_path / "run-002-x").exists()


# ─────────────────────────────────────────────────────────────────────────────
# validate_artifacts
# ─────────────────────────────────────────────────────────────────────────────


def test_validate_artifacts_detecta_fase_faltante(tmp_path: Path):
    run_dir = init_run(tmp_path, "run-003-x", "LegalTech", _KILL)
    # Recém-criado: subpastas existem, mas nenhum artefato → todas as fases faltam.
    result = validate_artifacts(run_dir)
    assert result == {"P0": False, "P1": False, "P2": False}

    # Preenche P0 e P1, deixa P2 faltando.
    (run_dir / "p0" / "hypotheses.md").write_text("# H1..H5", encoding="utf-8")
    (run_dir / "p1" / "mercado.md").write_text("frente", encoding="utf-8")
    result = validate_artifacts(run_dir)
    assert result == {"P0": True, "P1": True, "P2": False}


def test_validate_artifacts_completo(tmp_path: Path):
    run_dir = init_run(tmp_path, "run-004-x", "LegalTech", _KILL)
    (run_dir / "p0" / "hypotheses.md").write_text("# H", encoding="utf-8")
    (run_dir / "p1" / "a.md").write_text("x", encoding="utf-8")
    (run_dir / "p2" / "claims.yaml").write_text("claims: []", encoding="utf-8")
    assert validate_artifacts(run_dir) == {"P0": True, "P1": True, "P2": True}


# ─────────────────────────────────────────────────────────────────────────────
# run_kill_check — ausência de benchmark ⇒ None (nunca kill silencioso)
# ─────────────────────────────────────────────────────────────────────────────


def test_run_kill_check_none_sem_benchmark(tmp_path: Path):
    run_dir = init_run(tmp_path, "run-005-x", "LegalTech", _KILL)
    assert run_kill_check(run_dir) is None


# ─────────────────────────────────────────────────────────────────────────────
# run_gate_g2_3 — gate bloqueador recomputado a partir do claims.yaml
# ─────────────────────────────────────────────────────────────────────────────


def test_run_gate_g2_3_reprova_no_run000():
    gate = run_gate_g2_3(RUN000)
    assert gate.resultado == "FAIL"
    assert set(gate.decisorios_em_baixo) == {"C5b", "C6"}


# ─────────────────────────────────────────────────────────────────────────────
# TESTE E2E — Run Mínimo Viável contra o Run #0 REAL
# ─────────────────────────────────────────────────────────────────────────────


def test_e2e_run000_reproduz_veredito_real():
    assert RUN000.is_dir(), f"Run #0 não encontrado em {RUN000}"

    report = run_minimo_viavel(RUN000)

    assert isinstance(report, RunReport)
    assert report.run_id == "run-000-legaltech"

    # (a) Todas as fases do Run Mínimo Viável presentes.
    assert report.artifacts_ok == {"P0": True, "P1": True, "P2": True}
    assert all(report.artifacts_ok.values())

    # (b) Score recomputado bate com o veredito real (claims.yaml § score_run).
    assert report.score.score_percent == 63.4
    assert report.score.soma_produtos == 1585
    assert report.score.soma_pesos == 25

    # (c) Gate G2→3 REPROVA — decisórios C5b (H2) e C6 (H5) em Baixo.
    assert report.gate.resultado == "FAIL"
    assert report.gate.cond1_score_ge_70 is False
    assert report.gate.cond2_no_decisorio_baixo is False
    assert set(report.gate.decisorios_em_baixo) == {"C5b", "C6"}


def test_e2e_run000_kill_nao_disparado_ortogonal_ao_gate():
    """A distinção arquitetural: gate FAIL e kill NÃO disparado coexistem."""
    report = run_minimo_viavel(RUN000)

    # Kill check rodou (baseline/benchmark.yaml existe) e NÃO disparou:
    # o protocolo demonstrou valor (B vale R$500 e vence o baseline).
    assert report.kill is not None, "benchmark.yaml deveria alimentar o kill check"
    assert report.kill.kill_disparado is False
    assert report.kill.vencedor == "B"
    assert report.kill.media_a == 7.1
    assert report.kill.media_b == 9.1

    # gate e kill são CAMPOS SEPARADOS com semânticas distintas.
    assert report.gate.resultado == "FAIL"  # bloqueador de avanço
    assert report.kill.kill_disparado is False  # valor do protocolo


def test_e2e_run000_resumo_nao_colapsa_gate_e_kill():
    """O resumo deve expor gate FAIL e kill não disparado sem fundir os dois."""
    report = run_minimo_viavel(RUN000)
    resumo = report.resumo

    # Gate bloqueador aparece como FAIL, apontando as hipóteses abertas.
    assert "Gate G2→3: FAIL" in resumo
    assert "H2" in resumo and "H5" in resumo

    # Kill aparece separado, como não disparado (protocolo tem valor).
    assert "Kill: não disparado" in resumo
    assert "CONTINUE" in resumo

    # As duas frases são distintas — não há um único veredito "passou/reprovou".
    assert resumo.index("Gate G2→3") != resumo.index("Kill:")


def test_e2e_run000_render_markdown_tem_secoes_separadas():
    report = run_minimo_viavel(RUN000)
    md = report.render()
    assert "## Gate G2→3 (bloqueador de avanço a P3)" in md
    assert "## Kill criterion (decide se o protocolo morre)" in md
    assert "63.4" in md


# ─────────────────────────────────────────────────────────────────────────────
# CLI — pelo menos 1 subcomando via main() (exit codes)
# ─────────────────────────────────────────────────────────────────────────────


def test_cli_gate_retorna_exit_1_no_run000(capsys):
    # gate FAIL ⇒ exit 1 (o run não avança a P3).
    code = main(["gate", str(RUN000)])
    assert code == 1
    out = capsys.readouterr().out
    assert "FAIL" in out
    assert "C5b" in out and "C6" in out


def test_cli_run_retorna_exit_1_no_run000(capsys):
    code = main(["run", str(RUN000)])
    assert code == 1
    out = capsys.readouterr().out
    assert "Gate G2→3: FAIL" in out
    assert "Kill: não disparado" in out


def test_cli_init_via_main(tmp_path: Path, capsys):
    code = main(
        ["init", "run-009-cli", "--domain", "Fintech", "--kill", _KILL, "--base", str(tmp_path)]
    )
    assert code == 0
    run_dir = tmp_path / "run-009-cli"
    assert (run_dir / "MANIFEST.yaml").is_file()
    # MANIFEST escrito com o kill_criterion informado.
    data = yaml.safe_load((run_dir / "MANIFEST.yaml").read_text(encoding="utf-8"))
    assert data["kill_criterion"] == _KILL


def test_cli_init_kill_vazio_exit_2(tmp_path: Path):
    code = main(["init", "run-010-x", "--domain", "D", "--kill", "", "--base", str(tmp_path)])
    assert code == 2
    assert not (tmp_path / "run-010-x").exists()

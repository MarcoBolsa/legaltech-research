"""CLI do RILP Engine (Fase C — leva 3, integração). Entrypoint `rilp`.

Expõe o motor determinístico na linha de comando — qualquer um roda e reproduz
score, gate, benchmark e domain pack a partir dos artefatos de um run.

Subcomandos:
    rilp init <run-id> --domain D --kill "<criterio>" [--base runs/]
    rilp score <run-dir>                # imprime a trilha de auditoria
    rilp gate  <run-dir>                # imprime o gate G2→3 (exit 1 se FAIL)
    rilp benchmark <run-dir>            # imprime o relatório de benchmark/kill
    rilp pack  <run-dir> --domain D [--hyp p0/hypotheses.md]
    rilp run   <run-dir>               # Run Mínimo Viável consolidado
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rilp.benchmark import render_report
from rilp.domain_pack import build_partial_pack_from_run
from rilp.models import ClaimsDoc
from rilp.runner import (
    BenchmarkInput,
    init_run,
    run_gate_g2_3,
    run_kill_check,
    run_minimo_viavel,
)
from rilp.scoring import audit_trail

_CLAIMS_REL = "p2/claims.yaml"
_HYP_REL = "p0/hypotheses.md"
_BENCHMARK_REL = "baseline/benchmark.yaml"
_MANIFEST_REL = "MANIFEST.yaml"


# ─────────────────────────────────────────────────────────────────────────────
# Handlers (retornam exit code)
# ─────────────────────────────────────────────────────────────────────────────


def _cmd_init(args: argparse.Namespace) -> int:
    try:
        run_dir = init_run(args.base, args.run_id, args.domain, args.kill)
    except ValueError as exc:
        print(f"erro: {exc}", file=sys.stderr)
        return 2
    print(f"Run criado: {run_dir}")
    print("Subpastas: p0/ p1/ p2/ baseline/ · MANIFEST.yaml escrito.")
    return 0


def _cmd_score(args: argparse.Namespace) -> int:
    claims_path = Path(args.run_dir) / _CLAIMS_REL
    if not claims_path.is_file():
        print(f"erro: claims.yaml não encontrado em {claims_path}", file=sys.stderr)
        return 2
    doc = ClaimsDoc.from_yaml(claims_path)
    print(audit_trail(doc))
    return 0


def _cmd_gate(args: argparse.Namespace) -> int:
    try:
        gate = run_gate_g2_3(args.run_dir)
    except FileNotFoundError as exc:
        print(f"erro: {exc}", file=sys.stderr)
        return 2
    print(f"Gate G2→3: {gate.resultado}")
    print(f"  Condição 1 (score ≥ 70%): {'atende' if gate.cond1_score_ge_70 else 'falha'}")
    cond2 = "atende" if gate.cond2_no_decisorio_baixo else "falha"
    print(f"  Condição 2 (nenhum decisório em Baixo): {cond2}")
    if gate.decisorios_em_baixo:
        print(f"  Decisórios em Baixo: {', '.join(gate.decisorios_em_baixo)}")
    print(f"  {gate.natureza}")
    # Exit 1 quando o gate REPROVA — o run não avança a P3.
    return 1 if gate.resultado == "FAIL" else 0


def _cmd_benchmark(args: argparse.Namespace) -> int:
    benchmark_path = Path(args.run_dir) / _BENCHMARK_REL
    if not benchmark_path.is_file():
        print(
            f"erro: benchmark não encontrado em {benchmark_path} "
            "(kill check não avaliável)",
            file=sys.stderr,
        )
        return 2
    inp = BenchmarkInput.from_yaml(benchmark_path)
    result = run_kill_check(args.run_dir)
    assert result is not None  # arquivo existe → evaluate rodou
    print(render_report(inp, result))
    return 0


def _cmd_pack(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    claims_path = run_dir / _CLAIMS_REL
    hyp_path = run_dir / args.hyp
    if not claims_path.is_file():
        print(f"erro: claims.yaml não encontrado em {claims_path}", file=sys.stderr)
        return 2
    run_id = _resolve_run_id(run_dir)
    try:
        pack = build_partial_pack_from_run(claims_path, hyp_path, args.domain, run_id)
    except FileNotFoundError as exc:
        print(f"erro: {exc}", file=sys.stderr)
        return 2
    out_path = run_dir / f"domain-pack-{args.domain}.yaml"
    pack.to_yaml(out_path)
    print(f"Domain pack (stage={pack.meta.stage}, n_runs={pack.meta.n_runs}) escrito: {out_path}")
    return 0


def _cmd_run(args: argparse.Namespace) -> int:
    try:
        report = run_minimo_viavel(args.run_dir)
    except FileNotFoundError as exc:
        print(f"erro: {exc}", file=sys.stderr)
        return 2
    print(report.render())
    # Exit 1 quando o gate bloqueador reprova (avanço barrado); o kill é ortogonal.
    return 1 if report.gate.resultado == "FAIL" else 0


def _resolve_run_id(run_dir: Path) -> str:
    """run_id do MANIFEST se existir, senão o nome do diretório."""
    manifest = run_dir / _MANIFEST_REL
    if manifest.is_file():
        try:
            from rilp.runner import RunManifest

            return RunManifest.from_yaml(manifest).run_id
        except Exception:  # noqa: BLE001 — fallback benigno para nome do dir
            pass
    return run_dir.name


# ─────────────────────────────────────────────────────────────────────────────
# Parser
# ─────────────────────────────────────────────────────────────────────────────


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rilp",
        description="RILP Engine — score, gates, benchmark e domain packs determinísticos.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="cria a estrutura de um run novo + MANIFEST")
    p_init.add_argument("run_id", help="identificador do run (ex.: run-001-fintech)")
    p_init.add_argument("--domain", required=True, help="domínio do run")
    p_init.add_argument("--kill", required=True, help="critério de kill (obrigatório, não vazio)")
    p_init.add_argument("--base", default="runs", help="diretório base (default: runs/)")
    p_init.set_defaults(func=_cmd_init)

    p_score = sub.add_parser("score", help="imprime a trilha de auditoria do score")
    p_score.add_argument("run_dir", help="diretório do run")
    p_score.set_defaults(func=_cmd_score)

    p_gate = sub.add_parser("gate", help="avalia o gate G2→3 (exit 1 se FAIL)")
    p_gate.add_argument("run_dir", help="diretório do run")
    p_gate.set_defaults(func=_cmd_gate)

    p_bench = sub.add_parser("benchmark", help="relatório de benchmark + kill check")
    p_bench.add_argument("run_dir", help="diretório do run")
    p_bench.set_defaults(func=_cmd_benchmark)

    p_pack = sub.add_parser("pack", help="gera o domain pack parcial do run")
    p_pack.add_argument("run_dir", help="diretório do run")
    p_pack.add_argument("--domain", required=True, help="domínio do pack")
    p_pack.add_argument("--hyp", default=_HYP_REL, help="caminho de hypotheses.md relativo ao run")
    p_pack.set_defaults(func=_cmd_pack)

    p_run = sub.add_parser("run", help="Run Mínimo Viável consolidado (exit 1 se gate FAIL)")
    p_run.add_argument("run_dir", help="diretório do run")
    p_run.set_defaults(func=_cmd_run)

    return parser


def main(argv: list[str] | None = None) -> int:
    """Ponto de entrada da CLI. Retorna o exit code (usado por sys.exit)."""
    parser = _build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

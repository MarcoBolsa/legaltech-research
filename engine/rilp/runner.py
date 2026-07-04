"""Runner do Run Mínimo Viável P0→P2 (Fase C — leva 3, integração).

Fonte da verdade: `docs/FASE-C-SPEC.md` §"Princípio arquitetural" +
RILP-v2.md §990 ("Run Mínimo Viável"), §953 (gate G2→3 bloqueador) e
§1008 ("todo run nasce com condição de morte").

O runner NÃO chama LLM e NÃO faz pesquisa. Ele orquestra ESTRUTURA, VALIDA os
artefatos que os agentes produziram e aplica GATES de forma determinística —
materializando a vantagem competitiva do RILP (auditabilidade recomputável).

DISTINÇÃO ARQUITETURAL (o que o Run #0 revelou — não confundir):
    1. Gate G2→3 (bloqueador de AVANÇO): score>=70 E nenhum decisório em Baixo.
       FAIL ⇒ o run NÃO avança a P3 (design) sem fechar os decisórios.
    2. Kill criterion (decide se o PROTOCOLO morre): dispara se o artefato NÃO
       vale R$500 OU NÃO vence o baseline.
Os dois são ORTOGONAIS: um run pode ter gate FAIL (precisa de mais evidência
para avançar) e ao mesmo tempo kill NÃO disparado (o protocolo provou valor).
O RunReport expõe os dois campos separadamente — nunca colapsa em "passou/reprovou".
"""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, field_validator

from rilp.benchmark import BenchmarkInput, BenchmarkResult, evaluate
from rilp.models import ClaimsDoc, GateResult, ScoreResult
from rilp.scoring import check_gate, compute_score

# ─────────────────────────────────────────────────────────────────────────────
# Layout canônico do Run Mínimo Viável (RILP §990)
# ─────────────────────────────────────────────────────────────────────────────

#: Subpastas de fase criadas em todo run.
_SUBDIRS = ("p0", "p1", "p2", "baseline")

#: Artefato mínimo esperado por fase do Run Mínimo Viável.
#:   P0 = hipóteses declaradas · P1 = ao menos 1 frente de coleta · P2 = claims pontuados.
_ARTIFACT_P0 = "p0/hypotheses.md"
_ARTIFACT_P2 = "p2/claims.yaml"
_P1_DIR = "p1"

#: Nome do manifesto do run e do input de benchmark (kill check).
_MANIFEST_NAME = "MANIFEST.yaml"
_BENCHMARK_INPUT = "baseline/benchmark.yaml"


# ─────────────────────────────────────────────────────────────────────────────
# Manifesto do run (condição de morte obrigatória — RILP §1008)
# ─────────────────────────────────────────────────────────────────────────────


class RunManifest(BaseModel):
    """Manifesto de um run. Todo run nasce com uma condição de morte (RILP §1008).

    `kill_criterion` vazio é proibido: um run sem critério de kill não pode
    provar (nem refutar) valor, então o construtor recusa explicitamente.
    Campos extras do MANIFEST real (started, timebox…) são tolerados.
    """

    model_config = ConfigDict(extra="ignore")

    run_id: str
    domain: str
    scope: str = "Run Mínimo Viável (P0→P2)"
    kill_criterion: str
    status: str = "initialized"
    protocol_version: str = "RILP v2.0"
    branch: str = ""

    @field_validator("kill_criterion")
    @classmethod
    def _kill_criterion_nao_vazio(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError(
                "kill_criterion não pode ser vazio — todo run nasce com condição "
                "de morte (RILP §1008)."
            )
        return v

    def to_yaml(self, path: str | Path) -> None:
        """Serializa o manifesto para YAML (UTF-8, ordem estável, sem aliases)."""
        data = self.model_dump(mode="json")
        Path(path).write_text(
            yaml.safe_dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False),
            encoding="utf-8",
        )

    @classmethod
    def from_yaml(cls, path: str | Path) -> RunManifest:
        """Carrega e valida um MANIFEST.yaml do disco, tolerando campos extras."""
        raw = Path(path).read_text(encoding="utf-8")
        data = yaml.safe_load(raw) or {}
        return cls.model_validate(data)


# ─────────────────────────────────────────────────────────────────────────────
# Relatório consolidado (gate e kill SEMPRE separados)
# ─────────────────────────────────────────────────────────────────────────────


class RunReport(BaseModel):
    """Relatório consolidado do Run Mínimo Viável.

    `gate` (bloqueador de avanço a P3) e `kill` (decide se o protocolo morre)
    são campos SEPARADOS por design — a semântica do Run #0 exige não colapsar
    "precisa de mais evidência para avançar" com "o protocolo provou/não provou
    valor". `kill` é None quando não há benchmark estruturado para avaliar.
    """

    run_id: str
    artifacts_ok: dict[str, bool]
    score: ScoreResult
    gate: GateResult
    kill: BenchmarkResult | None = None
    resumo: str

    def render(self) -> str:
        """Gera o relatório markdown recomputável do run."""
        lines: list[str] = []
        lines.append(f"# Relatório do Run Mínimo Viável — {self.run_id}")
        lines.append("")

        lines.append("## Artefatos por fase")
        lines.append("")
        for fase, ok in self.artifacts_ok.items():
            lines.append(f"- {fase}: {'✅ presente' if ok else '❌ ausente'}")
        lines.append("")

        lines.append("## Score do run")
        lines.append("")
        lines.append("| Claim | Bucket | Pontos | Peso | Produto |")
        lines.append("|-------|--------|-------:|-----:|--------:|")
        for row in self.score.tabela:
            lines.append(
                f"| {row.claim} | {row.bucket.value} | {row.pontos} | "
                f"{row.peso} | {row.produto} |"
            )
        lines.append(
            f"| **Σ** | | | **{self.score.soma_pesos}** | **{self.score.soma_produtos}** |"
        )
        lines.append("")
        lines.append(
            f"**Score = {self.score.soma_produtos} ÷ {self.score.soma_pesos} "
            f"= {self.score.score_percent}%**"
        )
        lines.append("")

        lines.append("## Gate G2→3 (bloqueador de avanço a P3)")
        lines.append("")
        lines.append(f"**{self.gate.resultado}** — {self.gate.natureza}")
        lines.append("")

        lines.append("## Kill criterion (decide se o protocolo morre)")
        lines.append("")
        if self.kill is None:
            lines.append(
                "Não avaliado — sem `baseline/benchmark.yaml` estruturado para o kill check."
            )
        else:
            estado = "DISPARADO" if self.kill.kill_disparado else "não disparado"
            lines.append(f"**{estado}** — {self.kill.veredito}")
        lines.append("")

        lines.append("## Resumo")
        lines.append("")
        lines.append(self.resumo)
        lines.append("")

        return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# Orquestração
# ─────────────────────────────────────────────────────────────────────────────


def init_run(
    base_dir: str | Path,
    run_id: str,
    domain: str,
    kill_criterion: str,
) -> Path:
    """Cria a estrutura de um run novo e escreve o MANIFEST.yaml.

    Cria `base_dir/<run_id>/` com subpastas p0/ p1/ p2/ baseline/. Recusa
    (ValueError) se `kill_criterion` for vazio — todo run nasce com condição de
    morte (RILP §1008). A validação acontece ANTES de qualquer efeito colateral
    no disco, via o construtor do RunManifest.
    """
    manifest = RunManifest(run_id=run_id, domain=domain, kill_criterion=kill_criterion)

    run_dir = Path(base_dir) / run_id
    for sub in _SUBDIRS:
        (run_dir / sub).mkdir(parents=True, exist_ok=True)

    manifest.to_yaml(run_dir / _MANIFEST_NAME)
    return run_dir


def validate_artifacts(run_dir: str | Path) -> dict[str, bool]:
    """Checa a presença dos artefatos mínimos por fase do Run Mínimo Viável.

    P0 = p0/hypotheses.md · P1 = ao menos 1 arquivo em p1/ · P2 = p2/claims.yaml.
    Retorna {fase: presente?} — presença estrutural, não validade de conteúdo.
    """
    run_dir = Path(run_dir)

    p1_dir = run_dir / _P1_DIR
    p1_tem_arquivo = p1_dir.is_dir() and any(f.is_file() for f in p1_dir.iterdir())

    return {
        "P0": (run_dir / _ARTIFACT_P0).is_file(),
        "P1": p1_tem_arquivo,
        "P2": (run_dir / _ARTIFACT_P2).is_file(),
    }


def _load_claims(run_dir: Path) -> ClaimsDoc:
    """Carrega o claims.yaml do P2, com erro claro se ausente."""
    claims_path = run_dir / _ARTIFACT_P2
    if not claims_path.is_file():
        raise FileNotFoundError(f"claims.yaml não encontrado: {claims_path}")
    return ClaimsDoc.from_yaml(claims_path)


def run_gate_g2_3(run_dir: str | Path) -> GateResult:
    """Aplica o gate BLOQUEADOR G2→3 a partir de p2/claims.yaml (RILP §953).

    Recomputa o score e avalia o gate — não confia no gate declarado no artefato.
    """
    run_dir = Path(run_dir)
    doc = _load_claims(run_dir)
    score = compute_score(doc)
    return check_gate(doc, score)


def run_kill_check(run_dir: str | Path) -> BenchmarkResult | None:
    """Roda o kill check SE existir baseline/benchmark.yaml — senão None.

    O kill check é SEPARADO do gate G2→3 (ver docstring do módulo): decide se o
    PROTOCOLO demonstrou valor (vale R$500 e vence o baseline), não se o run
    pode avançar. Ausência de benchmark estruturado ⇒ None (não avaliado), nunca
    um kill silencioso.
    """
    run_dir = Path(run_dir)
    benchmark_path = run_dir / _BENCHMARK_INPUT
    if not benchmark_path.is_file():
        return None
    inp = BenchmarkInput.from_yaml(benchmark_path)
    return evaluate(inp)


def _hipoteses_dos_decisorios(doc: ClaimsDoc, claim_ids: list[str]) -> list[str]:
    """Coleta as hipóteses tocadas pelos claims decisórios reprovados (ordem estável)."""
    alvo = set(claim_ids)
    hyps: list[str] = []
    for claim in doc.claims:
        if claim.id in alvo:
            for ref in claim.hypothesis_refs:
                if ref not in hyps:
                    hyps.append(ref)
    return hyps


def _build_resumo(
    artifacts_ok: dict[str, bool],
    gate: GateResult,
    kill: BenchmarkResult | None,
    hipoteses_abertas: list[str],
) -> str:
    """Monta o resumo textual mantendo gate e kill ORTOGONAIS (nunca colapsados)."""
    partes: list[str] = []

    faltando = [fase for fase, ok in artifacts_ok.items() if not ok]
    if faltando:
        partes.append(f"Artefatos: FALTAM {', '.join(faltando)}.")
    else:
        partes.append("Artefatos: P0/P1/P2 presentes.")

    # Gate G2→3 — bloqueador de AVANÇO (não fala de valor do protocolo).
    if gate.resultado == "PASS":
        partes.append("Gate G2→3: PASS — avança a P3 (design).")
    else:
        alvo = f" ({'/'.join(hipoteses_abertas)})" if hipoteses_abertas else ""
        partes.append(
            f"Gate G2→3: FAIL — não avança a P3 sem dado de campo{alvo}."
        )

    # Kill criterion — decide se o PROTOCOLO morre (ortogonal ao gate).
    if kill is None:
        partes.append("Kill: não avaliado — sem benchmark estruturado.")
    elif kill.kill_disparado:
        partes.append(f"Kill: DISPARADO — {kill.kill_motivo}; protocolo descontinuado.")
    else:
        partes.append("Kill: não disparado — protocolo demonstrou valor, CONTINUE.")

    return " ".join(partes)


def run_minimo_viavel(run_dir: str | Path) -> RunReport:
    """Orquestra o Run Mínimo Viável e consolida um RunReport.

    Sequência: valida artefatos → recomputa score → aplica gate G2→3 (bloqueador)
    → roda kill check (se houver benchmark) → monta o resumo com gate e kill
    SEPARADOS. É o ponto de entrada do `rilp run`.
    """
    run_dir = Path(run_dir)

    artifacts_ok = validate_artifacts(run_dir)
    doc = _load_claims(run_dir)
    score = compute_score(doc)
    gate = check_gate(doc, score)
    kill = run_kill_check(run_dir)

    hipoteses_abertas = _hipoteses_dos_decisorios(doc, gate.decisorios_em_baixo)
    resumo = _build_resumo(artifacts_ok, gate, kill, hipoteses_abertas)

    run_id = str(doc.meta.get("run_id") or run_dir.name)

    return RunReport(
        run_id=run_id,
        artifacts_ok=artifacts_ok,
        score=score,
        gate=gate,
        kill=kill,
        resumo=resumo,
    )

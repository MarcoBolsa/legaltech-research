"""Harness de benchmark RILP × baseline (Fase C — leva 2, frente B).

Fonte da verdade: `docs/FASE-C-SPEC.md` §"Rubrica de benchmark" +
`runs/run-000-legaltech/comparacao.md` §1 e §5.

Torna a comparação Documento A (baseline) × Documento B (RILP) um processo
repetível e o kill check determinístico: qualquer um recomputa o veredito
a partir das 4 notas + do teste do comprador (R$500) de cada documento.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field

#: Nomes canônicos dos 4 critérios da rubrica (comparacao.md §1).
CRITERIOS = [
    "rigor_evidencia",
    "auditabilidade",
    "honestidade_epistemica",
    "acionabilidade",
]

#: Diferença mínima de média para declarar um vencedor (abaixo disso: empate).
EMPATE_EPSILON = 0.1


class DocScore(BaseModel):
    """Notas de um documento na rubrica de benchmark (0..10 por critério)."""

    model_config = ConfigDict(extra="ignore")

    nome: str
    rigor_evidencia: float = Field(ge=0, le=10)
    auditabilidade: float = Field(ge=0, le=10)
    honestidade_epistemica: float = Field(ge=0, le=10)
    acionabilidade: float = Field(ge=0, le=10)
    vale_500: bool

    @property
    def media(self) -> float:
        """Média dos 4 critérios, arredondada a 1 casa decimal."""
        soma = (
            self.rigor_evidencia
            + self.auditabilidade
            + self.honestidade_epistemica
            + self.acionabilidade
        )
        return round(soma / len(CRITERIOS), 1)


class BenchmarkInput(BaseModel):
    """Entrada do benchmark: run avaliado + notas dos dois documentos."""

    model_config = ConfigDict(extra="ignore")

    run_id: str
    doc_a: DocScore
    doc_b: DocScore

    @classmethod
    def from_yaml(cls, path: str | Path) -> BenchmarkInput:
        """Carrega e valida um benchmark.yaml do disco."""
        raw = Path(path).read_text(encoding="utf-8")
        data = yaml.safe_load(raw) or {}
        return cls.model_validate(data)


class BenchmarkResult(BaseModel):
    """Resultado recomputável do benchmark: médias, vencedor e kill check."""

    media_a: float
    media_b: float
    vencedor: str  # "A" | "B" | "empate"
    kill_disparado: bool
    kill_motivo: str
    veredito: str


def _vencedor(media_a: float, media_b: float) -> str:
    """Vencedor = maior média; empate se |diferença| < EMPATE_EPSILON.

    A diferença é arredondada a 1 casa ANTES do teste de epsilon — as médias já
    são round(_, 1), mas a subtração de floats introduz erro (ex.: 8.1 - 8.0 =
    0.0999…96, que seria < 0.1 espúrio e classificaria uma vitória real de 0.1
    como 'empate'). Sem o round, 54% dos pares adjacentes de 0.1 quebravam o
    determinismo da comparação — o valor central do produto.
    """
    diff = round(media_b - media_a, 1)
    if abs(diff) < EMPATE_EPSILON:
        return "empate"
    return "B" if diff > 0 else "A"


def evaluate(inp: BenchmarkInput) -> BenchmarkResult:
    """Avalia o benchmark e aplica o kill check (MANIFEST `kill_criterion`).

    Kill dispara se: NÃO doc_b.vale_500 OU doc_b NÃO é superior ao baseline
    (media_b <= media_a). Se nenhuma condição se satisfaz: CONTINUE.
    """
    media_a = inp.doc_a.media
    media_b = inp.doc_b.media
    vencedor = _vencedor(media_a, media_b)

    nao_vale_500 = not inp.doc_b.vale_500
    # "Visivelmente superior" = ser o vencedor B pela mesma régua de epsilon do
    # `_vencedor`. Amarrar ao vencedor (em vez de `media_b <= media_a` cru) mantém
    # kill e vencedor SEMPRE coerentes: empate nunca é 'superior' → dispara kill.
    nao_superior = vencedor != "B"

    kill_disparado = nao_vale_500 or nao_superior

    motivos: list[str] = []
    if nao_vale_500:
        motivos.append(f"{inp.doc_b.nome} não vale R$500")
    if nao_superior:
        motivos.append(
            f"{inp.doc_b.nome} não é superior ao baseline "
            f"(média {media_b} vs {media_a}, vencedor: {vencedor})"
        )
    kill_motivo = (
        "; ".join(motivos)
        if motivos
        else (
            f"{inp.doc_b.nome} vale R$500 e é superior ao baseline "
            f"(média {media_b} > {media_a})"
        )
    )

    veredito = (
        f"KILL — {kill_motivo}."
        if kill_disparado
        else f"CONTINUE — {kill_motivo}. Vencedor: {vencedor}."
    )

    return BenchmarkResult(
        media_a=media_a,
        media_b=media_b,
        vencedor=vencedor,
        kill_disparado=kill_disparado,
        kill_motivo=kill_motivo,
        veredito=veredito,
    )


def render_report(inp: BenchmarkInput, result: BenchmarkResult) -> str:
    """Gera o relatório markdown recomputável, na estrutura de comparacao.md."""
    a, b = inp.doc_a, inp.doc_b
    lines: list[str] = []
    lines.append(f"# Benchmark — {a.nome} × {b.nome}")
    lines.append("")
    lines.append(f"**Run:** {inp.run_id}")
    lines.append("")
    lines.append("## 1. Tabela de notas")
    lines.append("")
    lines.append(f"| Critério | {a.nome} | {b.nome} |")
    lines.append("|---|:---:|:---:|")
    rotulos = {
        "rigor_evidencia": "1. Rigor de evidência",
        "auditabilidade": "2. Auditabilidade",
        "honestidade_epistemica": "3. Honestidade epistêmica",
        "acionabilidade": "4. Acionabilidade",
    }
    for campo, rotulo in rotulos.items():
        lines.append(f"| {rotulo} | {getattr(a, campo)} | {getattr(b, campo)} |")
    sim_nao_a = "SIM" if a.vale_500 else "NÃO"
    sim_nao_b = "SIM" if b.vale_500 else "NÃO"
    lines.append(f"| 5. Teste do comprador (R$500) | {sim_nao_a} | {sim_nao_b} |")
    lines.append(f"| **Média (1-4)** | **{result.media_a}** | **{result.media_b}** |")
    lines.append("")
    lines.append("## 2. Veredito")
    lines.append("")
    lines.append(f"**Vencedor: {result.vencedor}**")
    lines.append("")
    lines.append("## 3. Recomendação contra o critério de kill (MANIFEST.yaml)")
    lines.append("")
    lines.append(
        "Kill exige: **NÃO valer R$500** OU **NÃO ser visivelmente superior ao baseline**."
    )
    lines.append("")
    lines.append(f"- {b.nome} vale R$500? **{'Sim' if b.vale_500 else 'Não'}.**")
    superior = result.vencedor == "B"
    lines.append(
        f"- {b.nome} é superior ao baseline? **{'Sim' if superior else 'Não'}** "
        f"(média {result.media_b} × {result.media_a})."
    )
    lines.append("")
    # `veredito` já começa com "KILL —"/"CONTINUE —"; não reprefixar (evita
    # "CONTINUE — CONTINUE"). Ele carrega o veredito completo e auditável.
    lines.append(f"**{result.veredito}**")
    lines.append("")

    return "\n".join(lines)

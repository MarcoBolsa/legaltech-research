"""Contrato de dados canônico do RILP Engine (Fase C — leva 1, fundação).

Fonte da verdade: `docs/FASE-C-SPEC.md` §"Contrato de dados canônico" +
RILP-v2.md §334-352 (pontos-âncora, pesos e fórmula do gate G2→3).

Estes modelos são compartilhados pelas levas seguintes (scoring, domain_pack,
benchmark, runner). Alterações aqui são mudança de contrato — trate como tal.
"""

from __future__ import annotations

from enum import Enum, StrEnum
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field

# ─────────────────────────────────────────────────────────────────────────────
# Enums de domínio (RILP §340, §346)
# ─────────────────────────────────────────────────────────────────────────────

#: Pontos-âncora por bucket (ponto médio-alto de cada banda de confiança).
_BUCKET_PONTOS: dict[str, int] = {"Alto": 90, "Médio": 65, "Baixo": 25}


class Bucket(StrEnum):
    """Banda qualitativa de confiança de um claim. `pontos` = ponto-âncora RILP §340."""

    ALTO = "Alto"
    MEDIO = "Médio"
    BAIXO = "Baixo"

    @property
    def pontos(self) -> int:
        """Pontos-âncora do bucket: Alto=90 · Médio=65 · Baixo=25."""
        return _BUCKET_PONTOS[self.value]


class Peso(int, Enum):
    """Peso por criticidade do claim para a tese (RILP §346). Default = CONTEXTUAL."""

    DECISORIO = 3
    RELEVANTE = 2
    CONTEXTUAL = 1


# ─────────────────────────────────────────────────────────────────────────────
# Modelos de entrada (parseados de claims.yaml)
# ─────────────────────────────────────────────────────────────────────────────


class Source(BaseModel):
    """Fonte de evidência de um claim. tier 0..3 (0 = GAP, dado ausente confirmado)."""

    model_config = ConfigDict(extra="ignore")

    url: str
    tier: int = Field(ge=0, le=3)
    nota: str = ""


class Claim(BaseModel):
    """Afirmação estratégica pontuada por bucket e peso.

    `pontos` é o valor DECLARADO no artefato (deve casar com o âncora do bucket —
    validado por `scoring.validate_consistency`). `peso` aceita 1/2/3.
    """

    model_config = ConfigDict(extra="ignore")

    id: str
    enunciado: str = ""
    hypothesis_refs: list[str] = Field(default_factory=list)
    verdict: str = ""
    bucket: Bucket
    pontos: int
    peso: int = Field(ge=1, le=3)
    justificativa_bucket: str = ""
    fontes: list[Source] = Field(default_factory=list)

    @property
    def decisorio(self) -> bool:
        """True se o claim é decisório (peso == 3) — gate go/no-go."""
        return self.peso == Peso.DECISORIO.value

    @property
    def produto(self) -> int:
        """Contribuição do claim para o score: pontos declarados × peso."""
        return self.pontos * self.peso


class ClaimsDoc(BaseModel):
    """Documento P2 completo. Campos extras (score_run, gate_g2_3) são ignorados."""

    model_config = ConfigDict(extra="ignore")

    meta: dict = Field(default_factory=dict)
    claims: list[Claim] = Field(default_factory=list)

    @classmethod
    def from_yaml(cls, path: str | Path) -> ClaimsDoc:
        """Carrega e valida um claims.yaml do disco, tolerando campos extras."""
        raw = Path(path).read_text(encoding="utf-8")
        data = yaml.safe_load(raw) or {}
        return cls.model_validate(data)


# ─────────────────────────────────────────────────────────────────────────────
# Modelos de saída (produzidos por scoring.py)
# ─────────────────────────────────────────────────────────────────────────────


class ScoreRow(BaseModel):
    """Uma linha da tabela de auditoria do score."""

    claim: str
    bucket: Bucket
    pontos: int
    peso: int
    produto: int


class ScoreResult(BaseModel):
    """Resultado recomputável do Score do run (média ponderada dos claims)."""

    tabela: list[ScoreRow]
    soma_produtos: int
    soma_pesos: int
    score_percent: float


class GateResult(BaseModel):
    """Resultado do gate bloqueador G2→3 (RILP §352)."""

    cond1_score_ge_70: bool
    cond2_no_decisorio_baixo: bool
    decisorios_em_baixo: list[str]
    resultado: str  # "PASS" | "FAIL"
    natureza: str

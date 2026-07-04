"""Domain Pack — conhecimento acumulável entre runs (Fase C — leva 2, frente A).

Fonte da verdade: `docs/FASE-C-SPEC.md` §"Domain Pack" + RILP-v2.md §670-712
("Domain Packs — O Conhecimento como Produto").

Um Domain Pack condensa o que um run aprendeu sobre um domínio (hipóteses
validadas, ICP real, unit economics, vocabulário do cliente, falhas, heatmap
regulatório, stack validada) para que o PRÓXIMO run do mesmo domínio (ou,
eventualmente, um comprador no marketplace) comece de um patamar mais alto —
não do zero.

Regra dos 2 estágios (RILP §708-710 + Princípio 5 "não generalizar com N=1"):
    - stage="parcial"  (n_runs>=1): uso interno, nasce no P9 do próprio run.
    - stage="vendavel" (n_runs>=2): cross-domain, só após >=2 runs completos.
`validate_pack` reprova (retorna erros) um pack "vendavel" com n_runs<2 — é o
mecanismo que impede vender/generalizar conhecimento de um único domínio.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field

from rilp.models import ClaimsDoc

#: Refs de hipótese cujo conteúdo é regulatório (RILP H3 jurídico, H5 canal) —
#: usadas para popular o heatmap regulatório a partir dos claims do run.
_HEATMAP_HYPOTHESIS_REFS = frozenset({"H3", "H5"})

#: Tiers de fonte aceitos no heatmap regulatório (Tier 1/2 — nunca Tier 3/vendor).
_HEATMAP_TIER_MAX = 2


class DomainPackMeta(BaseModel):
    """Metadados do pack: domínio, versão, estágio e proveniência (runs)."""

    model_config = ConfigDict(extra="ignore")

    domain: str
    version: str
    stage: Literal["parcial", "vendavel"]
    run_ids: list[str] = Field(default_factory=list)
    n_runs: int = 0
    generated_at: str = ""


class DomainPack(BaseModel):
    """Domain Pack completo — seções acumuláveis entre runs (RILP §670-699).

    Todas as seções têm defaults honestos (lista/dict vazios) — um pack
    parcial de 1 run pode legitimamente deixar seções como stub/GAP quando o
    escopo do run não coletou aquele dado (ex.: unit economics sem CAC real).
    """

    model_config = ConfigDict(extra="ignore")

    meta: DomainPackMeta
    hypotheses_validated: list[dict] = Field(default_factory=list)
    icp_real: dict = Field(default_factory=dict)
    unit_econ_benchmark: dict = Field(default_factory=dict)
    vocabulario_cliente: list[str] = Field(default_factory=list)
    failures_learned: list[str] = Field(default_factory=list)
    heatmap_regulatorio: list[dict] = Field(default_factory=list)
    stack_validada: list[str] = Field(default_factory=list)

    def to_yaml(self, path: str | Path) -> None:
        """Serializa o pack para YAML (UTF-8, ordem estável, sem aliases)."""
        data = self.model_dump(mode="json")
        Path(path).write_text(
            yaml.safe_dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False),
            encoding="utf-8",
        )

    @classmethod
    def from_yaml(cls, path: str | Path) -> DomainPack:
        """Carrega e valida um domain pack do disco."""
        raw = Path(path).read_text(encoding="utf-8")
        data = yaml.safe_load(raw) or {}
        return cls.model_validate(data)


def validate_pack(pack: DomainPack) -> list[str]:
    """Valida a regra dos 2 estágios (RILP §708-710, Princípio 5).

    Retorna lista de erros (vazia = pack válido). Um pack "vendavel" com
    `n_runs < 2` é generalização precoce a partir de um único domínio/run —
    reprovado explicitamente, mesmo que o conteúdo em si esteja bem formado.
    """
    errors: list[str] = []
    if pack.meta.stage == "vendavel" and pack.meta.n_runs < 2:
        errors.append(
            "stage='vendavel' exige n_runs >= 2 (Princípio 5 — não generalizar "
            f"com N=1); pack atual tem n_runs={pack.meta.n_runs}."
        )
    if pack.meta.n_runs < 1:
        errors.append("n_runs deve ser >= 1 — pack sem nenhum run associado.")
    return errors


def _summarize_enunciado(enunciado: str, max_len: int = 160) -> str:
    """Resumo curto e honesto do enunciado do claim (primeira frase/trecho)."""
    flat = " ".join(enunciado.split())
    if len(flat) <= max_len:
        return flat
    return flat[: max_len - 1].rstrip() + "…"


def _build_heatmap_regulatorio(claims_doc: ClaimsDoc) -> list[dict]:
    """Extrai o heatmap regulatório dos claims que tocam H3/H5 (regulação/canal).

    Só usa fontes Tier 1/2 (nunca material de vendor/Tier 3) — o heatmap
    regulatório precisa de lastro em lei/regulador/imprensa jurídica, não em
    página de fornecedor.
    """
    heatmap: list[dict] = []
    for claim in claims_doc.claims:
        if not _HEATMAP_HYPOTHESIS_REFS.intersection(claim.hypothesis_refs):
            continue
        for fonte in claim.fontes:
            if fonte.tier == 0 or fonte.tier > _HEATMAP_TIER_MAX:
                continue
            heatmap.append(
                {
                    "claim_id": claim.id,
                    "hypothesis_refs": list(claim.hypothesis_refs),
                    "url": fonte.url,
                    "tier": fonte.tier,
                    "nota": fonte.nota,
                }
            )
    return heatmap


def build_partial_pack_from_run(
    claims_yaml_path: str | Path,
    hypotheses_md_path: str | Path,
    domain: str,
    run_id: str,
) -> DomainPack:
    """Constrói o Domain Pack PARCIAL (stage="parcial", n_runs=1) de um run.

    Extrai `hypotheses_validated` diretamente dos claims (id, enunciado
    resumido, verdict, bucket, confiança=pontos-âncora do bucket) e o
    `heatmap_regulatorio` dos claims que tocam H3/H5 com fontes Tier 1/2.

    `hypotheses_md_path` é aceito para uso futuro (cross-check título/H-refs
    contra o P0) — hoje o builder não precisa reabrir o markdown para montar
    o pack a partir do claims.yaml, que já carrega hypothesis_refs por claim.
    As seções sem dado de campo no escopo P0→P2 (icp_real, unit_econ_benchmark,
    vocabulario_cliente, stack_validada) ficam como stub honesto de GAP — nunca
    inventado (Constitution Art. IV — No Invention).
    """
    hypotheses_md_path = Path(hypotheses_md_path)
    if not hypotheses_md_path.exists():
        raise FileNotFoundError(f"hypotheses.md não encontrado: {hypotheses_md_path}")

    claims_doc = ClaimsDoc.from_yaml(claims_yaml_path)

    hypotheses_validated = [
        {
            "id": claim.id,
            "enunciado": _summarize_enunciado(claim.enunciado),
            "verdict": claim.verdict,
            "bucket": claim.bucket.value,
            "confianca": claim.bucket.pontos,
        }
        for claim in claims_doc.claims
    ]

    heatmap_regulatorio = _build_heatmap_regulatorio(claims_doc)

    unit_econ_benchmark = {
        "status": "GAP — CAC/LTV/churn ausentes no escopo documental P0→P2",
        "detalhe": (
            "Nenhuma frente do run encontrou dado de CAC/churn/LTV do setor "
            "jurídico brasileiro (ver claim C5b/C6). Unit economics de fundador "
            "solo permanece NÃO PROVADA — não inventamos número aqui."
        ),
    }

    return DomainPack(
        meta=DomainPackMeta(
            domain=domain,
            version="1.0",
            stage="parcial",
            run_ids=[run_id],
            n_runs=1,
        ),
        hypotheses_validated=hypotheses_validated,
        icp_real={
            "status": "GAP — ICP validado em campo requer dado primário (fora do escopo P0→P2)",
        },
        unit_econ_benchmark=unit_econ_benchmark,
        vocabulario_cliente=[],
        failures_learned=[],
        heatmap_regulatorio=heatmap_regulatorio,
        stack_validada=[],
    )

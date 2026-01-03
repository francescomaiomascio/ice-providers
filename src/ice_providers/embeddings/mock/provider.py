from __future__ import annotations

from typing import Any, List, Sequence, Optional

# IMPORT CONTRATTI (ENGINE)
from engine.representations.model import EmbeddingModel, EmbeddingResult


class MockEmbeddingModel(EmbeddingModel):
    """
    Mock embedding provider.

    Genera vettori deterministici e semplici.
    Serve esclusivamente per:
    - test
    - sviluppo offline
    - bootstrap senza dipendenze esterne
    """

    def __init__(self, dim: int = 8) -> None:
        self.dim = dim

    def encode(
        self,
        texts: Sequence[str],
        *,
        model: Optional[str] = None,
        **kwargs: Any,
    ) -> List[EmbeddingResult]:
        if not texts:
            return []

        results: List[EmbeddingResult] = []
        model_name = model or "mock-embeddings"

        for idx, text in enumerate(texts):
            # Vettore deterministico semplice
            vec = [
                (float((ord(c) + idx) % 53) / 53.0)
                for c in text
            ][: self.dim]

            if len(vec) < self.dim:
                vec.extend([0.0] * (self.dim - len(vec)))

            results.append(
                EmbeddingResult(
                    vector=vec,
                    dim=self.dim,
                    model=model_name,
                    raw={
                        "provider": "mock",
                        "text": text,
                    },
                    usage={},
                )
            )

        return results

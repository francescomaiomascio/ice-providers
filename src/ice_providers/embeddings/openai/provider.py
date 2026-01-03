from __future__ import annotations

import os
from typing import Any, List, Sequence, Optional

try:
    import openai
except ImportError:  # pragma: no cover
    openai = None

from ice_providers.embeddings.model import EmbeddingModel, EmbeddingResult
from ice_providers.embeddings.base import normalize_texts


class OpenAIEmbeddingModel(EmbeddingModel):
    """
    Embedding provider basato sull'API ufficiale OpenAI.
    """

    def __init__(
        self,
        *,
        default_model: str,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        organization: Optional[str] = None,
    ) -> None:
        if openai is None:
            raise RuntimeError(
                "Dipendenza mancante: installa 'openai' per usare OpenAIEmbeddingModel."
            )

        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY non impostata.")

        self._client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url,
            organization=organization,
        )
        self._default_model = default_model

    def encode(
        self,
        texts: Sequence[str],
        *,
        model: Optional[str] = None,
        **kwargs: Any,
    ) -> List[EmbeddingResult]:
        texts = normalize_texts(texts)
        if not texts:
            return []

        model_name = model or self._default_model

        response = self._client.embeddings.create(
            model=model_name,
            input=texts,
            **kwargs,
        )

        usage = getattr(response, "usage", {}) or {}
        results: List[EmbeddingResult] = []

        for item in response.data:
            vector = list(item.embedding)
            results.append(
                EmbeddingResult(
                    vector=vector,
                    dim=len(vector),
                    model=model_name,
                    raw=item,
                    usage=usage,
                )
            )

        return results

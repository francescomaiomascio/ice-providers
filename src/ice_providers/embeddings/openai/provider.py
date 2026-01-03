from __future__ import annotations

import os
from typing import Any, List, Sequence, Optional

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

from ice_providers.embeddings.model import EmbeddingModel, EmbeddingResult
from ice_providers.embeddings.base import normalize_texts


class OpenAIEmbeddingModel(EmbeddingModel):
    """
    Provider embedding via API OpenAI ufficiale.
    """

    def __init__(
        self,
        *,
        default_model: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        organization: Optional[str] = None,
    ) -> None:
        if OpenAI is None:
            raise RuntimeError("Installare `openai>=1.0.0`")

        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY non impostata")

        self._client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            organization=organization,
        )

        self._default_model = default_model or os.getenv(
            "OPENAI_EMBEDDINGS_MODEL",
            "text-embedding-3-large",
        )

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

        resp = self._client.embeddings.create(
            model=model_name,
            input=texts,
            **kwargs,
        )

        usage = getattr(resp, "usage", {}) or {}
        results: List[EmbeddingResult] = []

        for item in resp.data:
            vec = list(item.embedding)
            results.append(
                EmbeddingResult(
                    vector=vec,
                    dim=len(vec),
                    model=model_name,
                    raw=item,
                    usage=usage,
                )
            )

        return results

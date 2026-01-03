from __future__ import annotations

import os
from typing import Any, Dict, List, Sequence, Optional

import requests

from ice_providers.embeddings.model import EmbeddingModel, EmbeddingResult
from ice_providers.embeddings.base import normalize_texts


class LlamaCppEmbeddingModel(EmbeddingModel):
    """
    Embedding provider per llama.cpp server (OpenAI-compatible).

    Richiede:
        llama-server --embeddings --api-key <key>

    Endpoint:
        POST /v1/embeddings
    """

    def __init__(
        self,
        *,
        base_url: Optional[str] = None,
        default_model: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: int = 120,
    ) -> None:
        self._base_url = (
            base_url
            or os.getenv(
                "ICE_EMBEDDINGS_LLAMACPP_URL",
                "http://127.0.0.1:8000/v1",
            )
        ).rstrip("/")

        self._default_model = default_model or os.getenv(
            "ICE_EMBEDDINGS_LLAMACPP_MODEL",
            "local-embedding-model",
        )

        self._api_key = api_key or os.getenv("ICE_EMBEDDINGS_LLAMACPP_API_KEY")
        self._timeout = timeout

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

        payload: Dict[str, Any] = {
            "model": model_name,
            "input": texts,
        }
        payload.update(kwargs)

        headers = {"Content-Type": "application/json"}
        if self._api_key:
            headers["Authorization"] = f"Bearer {self._api_key}"

        response = requests.post(
            f"{self._base_url}/embeddings",
            json=payload,
            headers=headers,
            timeout=self._timeout,
        )
        response.raise_for_status()
        data = response.json()

        items = data.get("data", [])
        usage = data.get("usage", {}) or {}

        results: List[EmbeddingResult] = []
        for item in items:
            vec = list(item.get("embedding", []))
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

from __future__ import annotations

import os
from typing import Any, Dict, List, Sequence, Optional

import requests

from ice_providers.embeddings.model import EmbeddingModel, EmbeddingResult
from ice_providers.embeddings.base import normalize_texts


class OllamaEmbeddingModel(EmbeddingModel):
    """
    Embedding provider via Ollama.

    Endpoint:
        POST {base_url}/api/embeddings

    Payload:
        {
            "model": "...",
            "input": "text" | ["t1", "t2"]
        }

    Risposta:
        { "embedding": [...] }
        oppure
        { "embeddings": [[...], [...]] }
    """

    def __init__(
        self,
        *,
        base_url: Optional[str] = None,
        default_model: Optional[str] = None,
        timeout: int = 120,
    ) -> None:
        self._base_url = (
            base_url
            or os.getenv(
                "ICE_EMBEDDINGS_OLLAMA_URL",
                "http://127.0.0.1:11434",
            )
        ).rstrip("/")

        self._default_model = default_model or os.getenv(
            "ICE_EMBEDDINGS_OLLAMA_MODEL",
            "nomic-embed-text",
        )

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

        response = requests.post(
            f"{self._base_url}/api/embeddings",
            json=payload,
            timeout=self._timeout,
        )
        response.raise_for_status()
        data = response.json()

        # Ollama può restituire embedding singolo o multiplo
        if "embeddings" in data:
            embeddings = data["embeddings"]
        elif "embedding" in data:
            embeddings = [data["embedding"]]
        else:
            raise RuntimeError(
                f"Ollama embeddings response unexpected: {list(data.keys())}"
            )

        # Robustezza: allineamento minimo
        results: List[EmbeddingResult] = []
        for vec in embeddings:
            vec_list = list(vec)
            results.append(
                EmbeddingResult(
                    vector=vec_list,
                    dim=len(vec_list),
                    model=model_name,
                    raw=data,
                    usage={},
                )
            )

        return results

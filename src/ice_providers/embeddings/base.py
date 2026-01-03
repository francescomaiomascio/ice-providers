from __future__ import annotations

from typing import Sequence, List


def normalize_texts(texts: Sequence[str]) -> List[str]:
    """
    Normalizza l'input per i provider di embedding.

    - converte in lista
    - filtra stringhe vuote
    - garantisce tipo str
    """
    if not texts:
        return []

    normalized: List[str] = []

    for t in texts:
        if not t:
            continue
        if not isinstance(t, str):
            t = str(t)
        normalized.append(t)

    return normalized


def ensure_non_empty(texts: Sequence[str]) -> None:
    """
    Solleva errore se l'input è vuoto dopo normalizzazione.
    Usabile dai provider che non accettano batch vuoti.
    """
    if not texts:
        raise ValueError("No texts provided for embedding.")

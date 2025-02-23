"""Shared embeddable content functionality."""
from dataclasses import dataclass
from typing import Dict, Any, Optional, List

@dataclass
class Embeddable:
    image_base_url: Optional[str] = None
    variants: Optional[List[str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Embeddable":
        embeddables = data.get("_aEmbeddables", {})
        return cls(
            image_base_url=embeddables.get("_sEmbeddableImageBaseUrl"),
            variants=embeddables.get("_aVariants")
        )
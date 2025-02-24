"""Shared embeddable content functionality."""
from dataclasses import dataclass
from typing import Dict, Any, Optional, List

@dataclass
class Embeddable:
    image_base_url: str = ""
    variants: List[str] = None

    def __post_init__(self):
        if self.variants is None:
            self.variants = []

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Embeddable":
        if isinstance(data, str):
            # Handle case where data is just the image base URL
            return cls(image_base_url=data or "")
            
        return cls(
            image_base_url=data.get("_sEmbeddableImageBaseUrl", "") or "",
            variants=data.get("_aVariants", []) or []
        )
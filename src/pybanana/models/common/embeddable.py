"""Shared embeddable content functionality."""
from dataclasses import dataclass
from typing import Dict, Any, Optional, List

@dataclass
class Embeddable:
    image_base_url: str = ""
    variants: List[str] | None = None

    def __post_init__(self):
        if self.variants is None:
            self.variants = []

    def __init__(self, data: Dict[str, Any]):
        if isinstance(data, str):
            # Handle case where data is just the image base URL
            self.image_base_url = data or ""
        else:
            self.image_base_url = data.get("_sEmbeddableImageBaseUrl", "") or ""
            self.variants = data.get("_aVariants", []) or []

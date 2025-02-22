"""Shared embeddable content functionality."""
from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class Embeddable:
    image_base_url: Optional[str] = None
    url: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Embeddable":
        return cls(
            image_base_url=data.get("_sEmbeddableImageBaseUrl"),
            url=data.get("url"),
            name=data.get("name"),
            description=data.get("description")
        )
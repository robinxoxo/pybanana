"""Preview media related shared components."""
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

@dataclass
class PreviewMediaImage:
    """An image in preview media."""
    url: str = ""
    width: int = 0
    height: int = 0
    caption: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PreviewMediaImage":
        if not isinstance(data, dict):
            return cls()
            
        return cls(
            url=data.get("_sUrl", "") or "",
            width=data.get("_nWidth", 0) or 0,
            height=data.get("_nHeight", 0) or 0,
            caption=data.get("_sCaption", "") or ""
        )

@dataclass
class PreviewMedia:
    """Preview media information."""
    images: List[PreviewMediaImage] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PreviewMedia":
        if not isinstance(data, dict):
            return cls()

        images = []
        image_data = data.get("_aImages", []) or []
        if isinstance(image_data, list):
            images = [PreviewMediaImage.from_dict(img) for img in image_data]

        metadata = data.get("_aMetadata", {})
        if not isinstance(metadata, dict):
            metadata = {}

        return cls(
            images=images,
            metadata=metadata
        )
"""Preview media related shared components."""
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

@dataclass
class PreviewMediaImage:
    """A preview media image."""
    url: str = ""
    caption: str = ""
    dimensions: Dict[str, int] = field(default_factory=dict)
    width: Optional[int] = None
    height: Optional[int] = None
    file_size: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PreviewMediaImage":
        return cls(
            url=data.get("_sUrl", "") or "",
            width=data.get("_nWidth") or None,
            height=data.get("_nHeight") or None,
            file_size=data.get("_nFilesize") or None
        )

@dataclass
class PreviewMedia:
    images: List[PreviewMediaImage] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PreviewMedia":
        if not isinstance(data, dict):
            data = {}
        images = data.get("_aImages") or []
        if not isinstance(images, list):
            images = []
        return cls(
            images=[PreviewMediaImage.from_dict(img) for img in images],
            metadata=data.get("_aMetadata", {}) or {}
        )
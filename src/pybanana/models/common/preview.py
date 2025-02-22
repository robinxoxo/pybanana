"""Preview media related shared components."""
from dataclasses import dataclass
from typing import Dict, Any, List, Optional

@dataclass
class PreviewMediaImage:
    """A preview media image."""
    url: str
    width: Optional[int] = None
    height: Optional[int] = None
    file_size: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PreviewMediaImage":
        return cls(
            url=data.get("_sUrl") or data.get("_sFile", ""),
            width=data.get("_nWidth"),
            height=data.get("_nHeight"),
            file_size=data.get("_nFilesize")
        )

@dataclass
class PreviewMedia:
    images: List[PreviewMediaImage]
    metadata: Dict[str, Any]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PreviewMedia":
        return cls(
            images=[PreviewMediaImage.from_dict(img) for img in data.get("_aImages", [])],
            metadata=data.get("_aMetadata", {})
        )
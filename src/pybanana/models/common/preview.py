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
    file_size: int = 0

    def __init__(self, data: Dict[str, Any]):
        if not isinstance(data, dict):
            return

        self.url = data.get("_sUrl", "")
        self.width = data.get("_nWidth", 0)
        self.height = data.get("_nHeight", 0)
        self.caption = data.get("_sCaption", "")
        self.file_size = data.get("_nFileSize", 0)


@dataclass
class PreviewMedia:
    """Preview media information."""
    images: List[PreviewMediaImage] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __init__(self, data: Dict[str, Any]):
        if not isinstance(data, dict):
            return

        images = []
        image_data = data.get("_aImages", [])
        if isinstance(image_data, list):
            images = [PreviewMediaImage(img) for img in image_data]

        metadata = data.get("_aMetadata", {})
        if not isinstance(metadata, dict):
            metadata = {}

        self.images = images
        self.metadata = metadata

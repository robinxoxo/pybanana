"""Category-related shared components."""
from dataclasses import dataclass
from typing import Dict, Optional, Any

@dataclass
class ModCategory:
    id: int = 0
    name: str = ""
    item_count: int = 0
    category_count: int = 0
    url: str = ""

    def __init__(self, data: Dict[str, Any]):
        if not isinstance(data, dict):
            return

        self.id = data.get("_idRow", 0)
        self.name = data.get("_sName", "")
        self.item_count = data.get("_nItemCount", 0)
        self.category_count = data.get("_nCategoryCount", 0)
        self.url = data.get("_sUrl", "")

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

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ModCategory":
        return cls(
            id=data.get("_idRow", 0) or 0,
            name=data.get("_sName", "") or "",
            item_count=data.get("_nItemCount", 0) or 0,
            category_count=data.get("_nCategoryCount", 0) or 0,
            url=data.get("_sUrl", "") or ""
        )
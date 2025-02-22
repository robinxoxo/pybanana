"""Bio entry related shared components."""
from dataclasses import dataclass, field
from typing import Dict, Optional

@dataclass
class Bio:
    title: str
    value: str
    custom_title: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "Bio":
        return cls(
            title=data["_sTitle"],
            value=data["_sValue"],
            custom_title=data.get("_sCustomTitle")
        )
"""Bio entry related shared components."""
from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class BioEntry:
    title: str
    value: str
    custom_title: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "BioEntry":
        return cls(
            title=data["_sTitle"],
            value=data["_sValue"],
            custom_title=data.get("_sCustomTitle")
        )

@dataclass
class Bio:
    entries: List[BioEntry] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, List[Dict[str, str]]]) -> "Bio":
        entries = [BioEntry.from_dict(entry) for entry in data["_aBio"]]
        return cls(entries=entries)
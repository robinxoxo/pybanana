"""Bio entry related shared components."""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union, Any

@dataclass
class BioEntry:
    title: str = ""
    value: str = ""
    custom_title: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "BioEntry":
        if isinstance(data, dict):
            return cls(
                title=data.get('_sTitle', "") or "",
                value=data.get('_sValue', "") or "",
                custom_title=data.get("_sCustomTitle") or ""
            )
        return cls()

@dataclass
class Bio:
    entries: List[BioEntry] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Union[Dict[str, Any], List[Dict[str, Any]]]) -> "Bio":
        if isinstance(data, list):
            return cls(entries=[])
            
        # Handle direct bio entry format
        if all(key in data for key in ["_sTitle", "_sValue"]):
            return cls(entries=[BioEntry.from_dict(data)])
            
        # Handle wrapped bio entries format
        bio_entries = data.get("_aBio", []) or []
        entries = [BioEntry.from_dict(entry) for entry in bio_entries]
        return cls(entries=entries)
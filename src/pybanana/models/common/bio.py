"""Bio entry related shared components."""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union, Any

@dataclass
class BioEntry:
    title: str = ""
    value: str = ""
    custom_title: str = ""

    def __init__(self, data: Dict[str, str]):
        if not isinstance(data, dict):
            return

        self.title = data.get("_sTitle", "")
        self.value = data.get("_sValue", "")
        self.custom_title = data.get("_sCustomTitle", "")


@dataclass
class Bio:
    entries: List[BioEntry] = field(default_factory=list)

    def __init__(self, data: Union[Dict[str, Any], List[Dict[str, Any]]]):
        if not isinstance(data, (dict, list)):
            return

        if isinstance(data, list):
            return

        # Handle direct bio entry format
        if all(key in data for key in ["_sTitle", "_sValue"]):
            self.entries = [BioEntry(data)]
            return

        # Handle wrapped bio entries format
        bio_entries = data.get("_aBio", []) or []
        if not isinstance(bio_entries, list):
            bio_entries = []
            return

        self.entries = [BioEntry(entry) for entry in bio_entries]

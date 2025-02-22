"""License-related shared components."""
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class LicenseChecklist:
    """License checklist information."""
    yes: List[str]
    ask: List[str]
    no: List[str]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "LicenseChecklist":
        return cls(
            yes=data.get("yes", []),
            ask=data.get("ask", []),
            no=data.get("no", [])
        )
"""License-related shared components."""
from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class LicenseChecklist:
    """License checklist information."""
    yes: List[str] = field(default_factory=list)
    ask: List[str] = field(default_factory=list)
    no: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "LicenseChecklist":
        return cls(
            yes=data.get("yes", []) or [],
            ask=data.get("ask", []) or [],
            no=data.get("no", []) or []
        )
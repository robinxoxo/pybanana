"""License-related shared components."""
from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class LicenseChecklist:
    """License checklist information."""
    yes: List[str] = field(default_factory=list)
    ask: List[str] = field(default_factory=list)
    no: List[str] = field(default_factory=list)

    def __init__(self, data: Dict[str, Any]) -> None:

        self.yes = data.get("yes", [])
        self.ask = data.get("ask", [])
        self.no = data.get("no", [])

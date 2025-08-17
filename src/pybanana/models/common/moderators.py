"""Moderator-related shared components."""
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

from ..member import Member


@dataclass
class Moderator(Member):
    modgroups: List[str] = field(default_factory=list)
    staff_bio: str = ""

    def __init__(self, data: Dict[str, Any]):
        if not isinstance(data, dict):
            return
        super().__init__(data)

        self.modgroups = data.get("_aModgroups", [])
        self.staff_bio = data.get("_sStaffBio", "")

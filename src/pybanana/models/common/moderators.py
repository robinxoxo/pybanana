"""Moderator-related shared components."""
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

from ..member import Member

@dataclass
class ModeratorRecord:
    member: Member  # Required field
    modgroups: List[str] = field(default_factory=list)
    staff_bio: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Optional['ModeratorRecord']:
        if not isinstance(data, dict):
            return None

        member = Member.from_dict(data.get('_aMember', {}))
        if member is None:
            return None

        return cls(
            member=member,
            modgroups=data.get('_aModgroups', []) or [],
            staff_bio=data.get('_sStaffBio', "") or ""
        )
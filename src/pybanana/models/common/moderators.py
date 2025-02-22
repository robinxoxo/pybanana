"""Moderator-related shared components."""
from dataclasses import dataclass
from typing import Dict, Any, List

from ..member import Member

@dataclass
class ModeratorRecord:
    member: Member
    staff_bio: str
    modgroups: List[str]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ModeratorRecord':
        return cls(
            member=Member.from_dict(data['_aMember']),
            staff_bio=data['_sStaffBio'],
            modgroups=data['_aModgroups']
        )
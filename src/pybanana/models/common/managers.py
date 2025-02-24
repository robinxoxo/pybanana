"""Manager-related shared components."""
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

from ..member import Member

@dataclass
class ManagerRecord:
    member: Member  # Required field
    modgroups: List[str] = field(default_factory=list)
    date_added: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Optional['ManagerRecord']:
        member = Member.from_dict(data.get('_aMember', {}))
        if member is None:
            return None
        return cls(
            member=member,
            modgroups=data.get('_aModgroups', []) or [],
            date_added=data.get('_tsDateAdded')
        )

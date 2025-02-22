"""Manager-related shared components."""
from dataclasses import dataclass
from typing import Optional

from ..member import Member

@dataclass
class ManagerRecord:
    member: Member
    modgroups: list[str]
    date_added: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'ManagerRecord':
        return cls(
            member=Member.from_dict(data.get('_aMember', {})),
            modgroups=data.get('_aModgroups', []),
            date_added=data.get('_tsDateAdded')
        )
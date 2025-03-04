"""Online status related shared components."""
from dataclasses import dataclass
from typing import Dict, Any, Optional
from datetime import datetime

from ..member import Member

@dataclass
class OnlineStatus:
    is_online: bool = False
    location: str = ""
    last_seen_time: Optional[datetime] = None
    session_creation_time: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OnlineStatus":
        return cls(
            is_online=data.get("_bIsOnline", False) or False,
            location=data.get("_sLocation", "") or "",
            last_seen_time=datetime.fromtimestamp(data.get("_tsLastSeenTime", 0) or 0),
            session_creation_time=datetime.fromtimestamp(data.get("_tsSessionCreationTime", 0) or 0)
        )
    
@dataclass
class OnlineRecord:
    member: Member
    status: OnlineStatus
    title: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OnlineRecord":
        member = Member.from_dict(data.get('_aMember', {}))
        if member is None:
            return None
        return cls(
            member=member,
            status=OnlineStatus.from_dict(data.get('_aOnlineStatus', {})),
            title=data.get('_sOnlineTitle', "") or ""
        )

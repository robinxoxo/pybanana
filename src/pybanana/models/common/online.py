"""Online status related shared components."""
from dataclasses import dataclass
from typing import Dict, Any, Optional
from datetime import datetime

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
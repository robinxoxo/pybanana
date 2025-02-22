"""Online status related shared components."""
from dataclasses import dataclass
from typing import Dict, Any
from datetime import datetime

@dataclass
class OnlineStatus:
    is_online: bool
    location: str
    last_seen_time: datetime
    session_creation_time: datetime

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OnlineStatus":
        return cls(
            is_online=data["_bIsOnline"],
            location=data["_sLocation"],
            last_seen_time=datetime.fromtimestamp(data["_tsLastSeenTime"]),
            session_creation_time=datetime.fromtimestamp(data["_tsSessionCreationTime"])
        )
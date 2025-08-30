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

    def __init__(self, data: Dict[str, Any]):
        self.is_online = data.get("_bIsOnline", False) or False
        self.location = data.get("_sLocation", "") or ""
        self.last_seen_time = datetime.fromtimestamp(
            data.get("_tsLastSeenTime", 0) or 0
        )
        self.session_creation_time = datetime.fromtimestamp(
            data.get("_tsSessionCreationTime", 0)
        )


@dataclass
class Online(Member):
    status: OnlineStatus | None = None
    title: Optional[str] = None

    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        self.status = OnlineStatus(data.get("_aOnlineStatus", {}))
        self.title = data.get("_sOnlineTitle", "")

"""Member profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..common.bio import Bio
from ..common.profile import Profile
from ..common.stats import CoreStats
from ..common.online import OnlineStatus

@dataclass
class MemberProfile:
    base: Profile
    user_title: str = ""
    join_date: datetime = field(default_factory=lambda: datetime.fromtimestamp(0))
    avatar_url: str = ""
    points_url: str = ""
    medals_url: str = ""
    is_online: bool = False
    online_title: str = ""
    offline_title: str = ""
    points: int = 0
    points_rank: int = 0
    bio_entries: List[Bio] = field(default_factory=list)
    is_banned: bool = False
    online_status: Optional[OnlineStatus] = None
    core_stats: Optional[CoreStats] = None
    honorary_title: Optional[str] = None
    signature_url: Optional[str] = None
    clearance_levels: List[str] = field(default_factory=list)
    responsibilities: List[str] = field(default_factory=list)
    modgroups: List[str] = field(default_factory=list)

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MemberProfile":
        base = Profile.from_dict(data)
        responsibilities = data.get("_aResponsibilities", {})
        return cls(
            base=base,
            user_title=data.get("_sUserTitle", ""),
            join_date=datetime.fromtimestamp(data.get("_tsJoinDate", 0)),
            avatar_url=data.get("_sAvatarUrl", ""),
            points_url=data.get("_sPointsUrl", ""),
            medals_url=data.get("_sMedalsUrl", ""),
            is_online=data.get("_bIsOnline", False),
            online_title=data.get("_sOnlineTitle", ""),
            offline_title=data.get("_sOfflineTitle", ""),
            points=data.get("_nPoints", 0),
            points_rank=data.get("_nPointsRank", 0),
            bio_entries=[Bio.from_dict(bio) for bio in data.get("_aBio", [])],
            online_status=OnlineStatus.from_dict(data["_aOnlineStatus"]) if "_aOnlineStatus" in data else None,
            core_stats=CoreStats.from_dict(data.get("_aCoreStats", {})),
            is_banned=data.get("_bIsBanned", False),
            honorary_title=data.get("_sHonoraryTitle"),
            signature_url=data.get("_sSigUrl"),
            clearance_levels=data.get("_aClearanceLevels", []),
            responsibilities=responsibilities,
            modgroups=responsibilities.get("_aModgroups", [])
        )
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
    user_title: str
    join_date: datetime
    avatar_url: str
    points_url: str
    medals_url: str
    is_online: bool
    online_title: str
    offline_title: str
    points: int
    points_rank: int
    bio_entries: List[Bio]
    is_banned: bool
    online_status: Optional[OnlineStatus] = None
    core_stats:  Optional[CoreStats] = None
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
            user_title=data["_sUserTitle"],
            join_date=datetime.fromtimestamp(data["_tsJoinDate"]),
            avatar_url=data["_sAvatarUrl"],
            points_url=data["_sPointsUrl"],
            medals_url=data["_sMedalsUrl"],
            is_online=data["_bIsOnline"],
            online_title=data["_sOnlineTitle"],
            offline_title=data["_sOfflineTitle"],
            points=data["_nPoints"],
            points_rank=data["_nPointsRank"],
            bio_entries=[Bio.from_dict(bio) for bio in data["_aBio"]],
            online_status=OnlineStatus.from_dict(data["_aOnlineStatus"]) if "_aOnlineStatus" in data else None,
            core_stats=CoreStats.from_dict(data["_aCoreStats"]),
            is_banned=data["_bIsBanned"],
            honorary_title=data.get("_sHonoraryTitle"),
            signature_url=data.get("_sSigUrl"),
            clearance_levels=data.get("_aClearanceLevels", []),
            responsibilities=responsibilities,
            modgroups=responsibilities.get("_aModgroups", [])
        )
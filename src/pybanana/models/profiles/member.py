"""Member profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..common.bio import Bio
from ..common.profile import Profile
from ..common.stats import CoreStats
from ..common.online import OnlineStatus
from ..common.buddy import Buddy
from ..common.field import ProfileField
from ..common.medals import Medals

@dataclass
class MemberProfile:
    base: Profile
    user_title: str = ""
    honorary_title: Optional[str] = None
    join_date: datetime = field(default_factory=lambda: datetime.fromtimestamp(0))
    avatar_url: str = ""
    upic_url: str = ""
    hd_avatar_url: str = ""
    hd_hovatar_url: str = ""
    points_url: str = ""
    medals_url: str = ""
    is_online: bool = False
    online_title: str = ""
    offline_title: str = ""
    points: int = 0
    points_rank: int = 0
    staff_profile: Optional[str] = None
    bio: List[Bio] = field(default_factory=list)
    profile_modules: List[str] = field(default_factory=list)
    is_banned: bool = False
    online_status: Optional[OnlineStatus] = None
    core_stats: Optional[CoreStats] = None
    signature_url: Optional[str] = None
    clearance_levels: List[str] = field(default_factory=list)
    responsibilities: List[str] = field(default_factory=list)
    modgroups: List[str] = field(default_factory=list)
    buddies: List[Buddy] = field(default_factory=list)
    contact_info: Optional[List[ProfileField]] = field(default_factory=list)
    pc_specs: Optional[List[ProfileField]] = field(default_factory=list)
    software_kit: Optional[List[ProfileField]] = field(default_factory=list)
    gaming_devices: Optional[List[ProfileField]] = field(default_factory=list)
    medals: List[Medals] = field(default_factory=list)

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MemberProfile":
        base = Profile.from_dict(data)
        responsibilities = data.get("_aResponsibilities", {})   
        return cls(
            base=base,
            user_title=data.get("_sUserTitle", "") or "",
            honorary_title=data.get("_sHonoraryTitle", "") or "",
            join_date=datetime.fromtimestamp(data.get("_tsJoinDate", 0)),
            avatar_url=data.get("_sAvatarUrl", "") or "",
            upic_url=data.get("_sUpicUrl", "") or "",
            hd_avatar_url=data.get("_sHdAvatarUrl", "") or "",
            hd_hovatar_url=data.get("_sHdHovatarUrl", "") or "",
            points_url=data.get("_sPointsUrl", "") or "",
            medals_url=data.get("_sMedalsUrl", "") or "",
            is_online=data.get("_bIsOnline", False) or False,
            online_title=data.get("_sOnlineTitle", "") or "",
            offline_title=data.get("_sOfflineTitle", "") or "",
            points=data.get("_nPoints", 0) or 0,
            points_rank=data.get("_nPointsRank", 0) or 0,
            staff_profile=data.get("_sStaffProfile", "") or "",
            bio=[Bio.from_dict(bio) for bio in data.get("_aBio", [])],
            profile_modules=data.get("_aProfileModules", []),
            online_status=OnlineStatus.from_dict(data["_aOnlineStatus"]) if "_aOnlineStatus" in data else None,
            core_stats=CoreStats.from_dict(data["_aCoreStats"]) if "_aCoreStats" in data else None,
            is_banned=data.get("_bIsBanned", False) or False,
            signature_url=data.get("_sSigUrl", "") or "",
            clearance_levels=data.get("_aClearanceLevels", {}),
            responsibilities=responsibilities,
            modgroups=responsibilities.get("_aModgroups", []),
            buddies=[Buddy.from_dict(buddy) for buddy in data.get("_aBuddies", [])],
            contact_info=[ProfileField.from_dict(field) for field in data.get("_aContactInfo", [])],
            pc_specs=[ProfileField.from_dict(field) for field in data.get("_aPcSpecs", [])],
            software_kit=[ProfileField.from_dict(field) for field in data.get("_aSoftwareKit", [])],
            gaming_devices=[ProfileField.from_dict(field) for field in data.get("_aGamingDevices", [])],
            medals=[Medals.from_dict(medal) for medal in data.get("_aMedals", [])]
        )
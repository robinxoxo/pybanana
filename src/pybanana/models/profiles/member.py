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
class Member(Profile):
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
        return getattr(self, name)

    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        responsibilities = data.get("_aResponsibilities", {})
        self.responsibilities = responsibilities
        self.user_title = data.get("_sUserTitle", "") or ""
        self.honorary_title = data.get("_sHonoraryTitle", "") or ""
        self.join_date = datetime.fromtimestamp(data.get("_tsJoinDate", 0))
        self.avatar_url = data.get("_sAvatarUrl", "") or ""
        self.upic_url = data.get("_sUpicUrl", "") or ""
        self.hd_avatar_url = data.get("_sHdAvatarUrl", "") or ""
        self.hd_hovatar_url = data.get("_sHdHovatarUrl", "") or ""
        self.points_url = data.get("_sPointsUrl", "") or ""
        self.medals_url = data.get("_sMedalsUrl", "") or ""
        self.is_online = data.get("_bIsOnline", False) or False
        self.online_title = data.get("_sOnlineTitle", "") or ""
        self.offline_title = data.get("_sOfflineTitle", "") or ""
        self.points = data.get("_nPoints", 0) or 0
        self.points_rank = data.get("_nPointsRank", 0) or 0
        self.staff_profile = data.get("_sStaffProfile", "") or ""
        self.bio = [Bio(bio) for bio in data.get("_aBio", [])]
        self.profile_modules = data.get("_aProfileModules", [])
        self.online_status = (
            OnlineStatus(data["_aOnlineStatus"]) if "_aOnlineStatus" in data else None
        )
        self.core_stats = (
            CoreStats(data["_aCoreStats"]) if "_aCoreStats" in data else None
        )
        self.is_banned = data.get("_bIsBanned", False) or False
        self.signature_url = data.get("_sSigUrl", "") or ""
        self.clearance_levels = data.get("_aClearanceLevels", {})
        self.responsibilities = responsibilities
        self.modgroups = responsibilities.get("_aModgroups", [])
        self.buddies = [Buddy(buddy) for buddy in data.get("_aBuddies", [])]
        self.contact_info = [
            ProfileField(field) for field in data.get("_aContactInfo", [])
        ]

        self.pc_specs = [ProfileField(field) for field in data.get("_aPcSpecs", [])]
        self.software_kit = [
            ProfileField(field) for field in data.get("_aSoftwareKit", [])
        ]

        self.gaming_devices = [
            ProfileField(field) for field in data.get("_aGamingDevices", [])
        ]
        self.medals = [Medals(medal) for medal in data.get("_aMedals", [])]

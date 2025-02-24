"""App profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any

from ..common.bio import Bio
from ..common.profile import Profile
from ..common.credits import Credits
from ..common.category import ModCategory
from ..common.stats import CoreStats

@dataclass
class AppFeatures:
    """App features."""
    profile_module_url: str = ""
    navigator_tab_url: str = ""
    main_url: str = ""
    settings_url: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AppFeatures":
        return cls(
            profile_module_url=data.get("_sProfileModuleUrl", "") or "",
            navigator_tab_url=data.get("_sNavigatorTabUrl", "") or "",
            main_url=data.get("_sMainUrl", "") or "",
            settings_url=data.get("_sSettingsUrl", "") or ""
        )

@dataclass
class AppProfile:
    """App profile."""
    base: Profile
    description: str = ""
    include_variable_name: str = ""
    version: str = ""
    state: str = ""
    type: str = ""
    user_count: int = 0
    is_safe: bool = False
    accepts_donations: bool = False
    accessor_has_app: bool = False
    features: Optional[AppFeatures] = None
    credits: Optional[Credits] = None
    sticker_url: str = ""
    categories: List[ModCategory] = field(default_factory=list)
    bio: Optional[Bio] = None
    stats: Optional[CoreStats] = None

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AppProfile":
        return cls(
            base=Profile.from_dict(data),
            description=data.get("_sDescription", "") or "",
            include_variable_name=data.get("_sIncludeVariableName", "") or "",
            version=data.get("_sVersion", "") or "",
            state=data.get("_sState", "") or "",
            type=data.get("_sType", "") or "",
            user_count=data.get("_nUserCount", 0) or 0,
            is_safe=data.get("_sbIsSafe", "") == "true",
            accepts_donations=data.get("_bAcceptsDonations", False),
            accessor_has_app=data.get("_bAccessorHasApp", False),
            features=AppFeatures.from_dict({} if isinstance(data.get("_aFeatures", {}), list) else data.get("_aFeatures", {})),
            credits=Credits.from_dict({} if isinstance(data.get("_aCredits", {}), list) else data.get("_aCredits", {})),
            sticker_url=data.get("_sStickerUrl", "") or "",
            categories=[ModCategory.from_dict(c) for c in data.get("_aCategories", {})],
            bio=Bio.from_dict({} if isinstance(data.get("_aBio", {}), list) else data.get("_aBio", {})),
            stats=CoreStats.from_dict({} if isinstance(data.get("_aStats"), list) else data.get("_aStats", {}))
        )

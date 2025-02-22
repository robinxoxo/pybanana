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
    profile_module_url: Optional[str] = None
    navigator_tab_url: Optional[str] = None
    main_url: Optional[str] = None
    settings_url: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AppFeatures":
        return cls(
            profile_module_url=data.get("_sProfileModuleUrl"),
            navigator_tab_url=data.get("_sNavigatorTabUrl"),
            main_url=data.get("_sMainUrl"),
            settings_url=data.get("_sSettingsUrl")
        )

@dataclass
class AppProfile:
    """App profile."""
    base: Profile
    description: str
    include_variable_name: str
    version: str
    state: str
    type: str
    user_count: int
    is_safe: bool
    accepts_donations: bool
    accessor_has_app: bool
    features: Optional[AppFeatures] = None
    credits: Optional[Credits] = None
    sticker_url: Optional[str] = None
    categories: List[ModCategory] = field(default_factory=list)
    bio: Optional[Bio] = None
    stats: Optional[CoreStats] = None

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AppProfile":
        base = Profile.from_dict(data)
        return cls(
            base=base,
            description=data["_sDescription"],
            include_variable_name=data["_sIncludeVariableName"],
            version=data["_sVersion"],
            state=data["_sState"],
            type=data["_sType"],
            user_count=data["_nUserCount"],
            is_safe=data["_sbIsSafe"] == "true",
            features=AppFeatures.from_dict(data["_aFeatures"]) if "_aFeatures" in data else None,
            accepts_donations=data["_bAcceptsDonations"],
            credits=Credits.from_dict(data["_aCredits"]) if "_aCredits" in data else None,
            sticker_url=data.get("_sStickerUrl"),
            accessor_has_app=data["_bAccessorHasApp"],
            categories=[ModCategory.from_dict(c) for c in data.get("_aCategories", [])],
            bio=Bio.from_dict(data["_aBio"]) if "_aBio" in data else None,
            stats=CoreStats.from_dict(data["_aStats"]) if "_aStats" in data else None
        )

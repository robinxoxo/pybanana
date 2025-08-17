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

    def __init__(self, data: Dict[str, Any]):
        self.profile_module_url = data.get("_sProfileModuleUrl", "")
        self.navigator_tab_url = data.get("_sNavigatorTabUrl", "")
        self.main_url = data.get("_sMainUrl", "")
        self.settings_url = data.get("_sSettingsUrl", "")


@dataclass
class App(Profile):
    """App profile."""

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
        return getattr(self, name)

    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        self.description = data.get("_sDescription", "") or ""
        self.include_variable_name = data.get("_sIncludeVariableName", "") or ""
        self.version = data.get("_sVersion", "") or ""
        self.state = data.get("_sState", "") or ""
        self.type = data.get("_sType", "") or ""
        self.user_count = data.get("_nUserCount", 0) or 0
        self.is_safe = data.get("_sbIsSafe", "") == "true"
        self.accepts_donations = data.get("_bAcceptsDonations", False)
        self.accessor_has_app = data.get("_bAccessorHasApp", False)
        self.features = AppFeatures(
            {}
            if isinstance(data.get("_aFeatures", {}), list)
            else data.get("_aFeatures", {})
        )
        self.credits = Credits(
            {}
            if isinstance(data.get("_aCredits", {}), list)
            else data.get("_aCredits", {})
        )
        self.sticker_url = data.get("_sStickerUrl", "")
        self.categories = [ModCategory(c) for c in data.get("_aCategories", {})]
        self.bio = Bio(
            {} if isinstance(data.get("_aBio", {}), list) else data.get("_aBio", {})
        )
        self.stats = CoreStats(
            {} if isinstance(data.get("_aStats"), list) else data.get("_aStats", {})
        )

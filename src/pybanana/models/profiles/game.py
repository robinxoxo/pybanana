"""Game profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..common.profile import Profile
from ..common.category import ModCategory
from ..common.managers import ManagerRecord

@dataclass
class GameSection:
    """Game section information."""
    model_name: str = ""
    plural_title: str = ""
    item_count: int = 0
    category_count: int = 0
    url: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GameSection":
        return cls(
            model_name=data.get("_sModelName", "") or "",
            plural_title=data.get("_sPluralTitle", "") or "",
            item_count=data.get("_nItemCount", 0) or 0,
            category_count=data.get("_nCategoryCount", 0) or 0,
            url=data.get("_sUrl", "") or ""
        )

@dataclass
class GameProfile:
    """Game profile information."""
    base: Profile  # Required field - no default
    homepage: str = ""
    is_approved: bool = False 
    sections: List[GameSection] = field(default_factory=list)
    mod_categories: List[ModCategory] = field(default_factory=list)
    managers: List[ManagerRecord] = field(default_factory=list)
    abbreviation: Optional[str] = None
    release_date: Optional[datetime] = None
    welcome_message: Optional[str] = None
    description: Optional[str] = None

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GameProfile":
        base = Profile.from_dict(data)     
        release_date = None
        if "_tsReleaseDate" in data and data["_tsReleaseDate"]:
            release_date = datetime.fromtimestamp(data["_tsReleaseDate"])
                
        return cls(
            base=base,
            homepage=data.get("_sHomepage", ""),
            is_approved=data.get("_bIsApproved", False),
            sections=[GameSection.from_dict(section) for section in data.get("_aSections", [])],
            mod_categories=[ModCategory.from_dict(cat) for cat in data.get("_aModCategories", [])],
            managers=[ManagerRecord.from_dict(m) for m in data.get("_aManagers", [])],
            abbreviation=data.get("_sAbbreviation", "") or None,
            release_date=release_date,
            welcome_message=data.get("_sWelcomeMessage", "") or "",
            description=data.get("_sDescription", "") or ""
        )
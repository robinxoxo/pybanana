"""Game profile and related functionality."""
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..common.profile import Profile
from ..common.category import ModCategory
from ..common.managers import ManagerRecord

@dataclass
class GameSection:
    """Game section information."""
    model_name: str
    plural_title: str
    item_count: int
    category_count: int
    url: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GameSection":
        return cls(
            model_name=data["_sModelName"],
            plural_title=data["_sPluralTitle"],
            item_count=data["_nItemCount"],
            category_count=data["_nCategoryCount"],
            url=data["_sUrl"]
        )

@dataclass
class GameProfile:
    base: Profile
    homepage: str
    is_approved: bool
    sections: List[GameSection]
    mod_categories: List[ModCategory]
    managers: List[ManagerRecord]
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
        return cls(
            base=base,
            abbreviation=data.get("_sAbbreviation"),
            homepage=data.get("_sHomepage", ""),
            is_approved=data.get("_bIsApproved", False),
            sections=[GameSection.from_dict(section) for section in data.get("_aSections", [])],
            mod_categories=[ModCategory.from_dict(cat) for cat in data.get("_aModRootCategories", [])],
            managers=[ManagerRecord.from_dict(manager) for manager in data.get("_aManagers", [])],
            release_date=datetime.strptime(data["_dsReleaseDate"], "%Y-%m-%d") if "_dsReleaseDate" in data else None,
            welcome_message=data.get("_sWelcomeMessage"),
            description=data.get("_sDescription")
        )
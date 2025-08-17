"""Game profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..common.profile import Profile
from ..common.category import ModCategory
from ..common.managers import Manager

@dataclass
class GameSection:
    """Game section information."""
    model_name: str = ""
    plural_title: str = ""
    item_count: int = 0
    category_count: int = 0
    url: str = ""

    def __init__(self, data: Dict[str, Any]):
        self.model_name = data.get("_sModelName", "")
        self.plural_title = data.get("_sPluralTitle", "")
        self.item_count = data.get("_nItemCount", 0)
        self.category_count = data.get("_nCategoryCount", 0)
        self.url = data.get("_sUrl", "")


@dataclass
class Game(Profile):
    """Game profile information."""

    homepage: str = ""
    is_approved: bool = False 
    sections: List[GameSection] = field(default_factory=list)
    mod_categories: List[ModCategory] = field(default_factory=list)
    managers: List[Manager] = field(default_factory=list)
    abbreviation: Optional[str] = None
    release_date: Optional[datetime] = None
    welcome_message: Optional[str] = None
    description: Optional[str] = None

    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        self.homepage = data.get("_sHomepage", "")
        self.is_approved = data.get("_bIsApproved", False)
        self.sections = [GameSection(section) for section in data.get("_aSections", [])]
        self.mod_categories = [
            ModCategory(cat) for cat in data.get("_aModCategories", [])
        ]
        self.managers = [Manager(m) for m in data.get("_aManagers", [])]
        self.abbreviation = data.get("_sAbbreviation", "") or None
        self.release_date = (
            datetime.fromtimestamp(data["_tsReleaseDate"])
            if "_tsReleaseDate" in data
            else None
        )
        self.welcome_message = data.get("_sWelcomeMessage", "") or None
        self.description = data.get("_sDescription", "") or None

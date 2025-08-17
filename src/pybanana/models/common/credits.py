"""Credit-related shared components."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class AffiliatedStudio:
    profile_url: str = ""
    name: str = ""
    flag_url: str = ""
    banner_url: str = ""

    def __init__(self, data: Dict[str, Any]):
        if not isinstance(data, dict):
            return

        self.profile_url = data.get("_sProfileUrl", "")
        self.name = data.get("_sName", "")
        self.flag_url = data.get("_sFlagUrl", "")
        self.banner_url = data.get("_sBannerUrl", "")


@dataclass
class Author:
    role: str = ""
    name: str = ""
    id: Optional[int] = None
    upic_url: str = ""
    profile_url: str = ""
    is_online: bool = False
    affiliated_studio: Optional[AffiliatedStudio] = None

    def __init__(self, data: Dict[str, Any]):
        if not isinstance(data, dict):
            return

        affiliated_studio = None
        studio_data = data.get("_aAffiliatedStudio")
        if isinstance(studio_data, dict):
            affiliated_studio = AffiliatedStudio(studio_data)

        self.name = data.get("_sName", "")
        self.id = data.get("_idRow", 0)
        self.profile_url = data.get("_sProfileUrl", "")
        self.is_online = bool(data.get("_bIsOnline", False))
        self.affiliated_studio = affiliated_studio


@dataclass
class CreditGroup:
    group_name: str = ""
    authors: List[Author] = field(default_factory=list)

    def __init__(self, data: Dict[str, Any]):
        if not isinstance(data, dict):
            return

        authors = []
        author_data = data.get("_aAuthors", [])
        if isinstance(author_data, list):
            authors = [Author(author) for author in author_data]

        self.group_name = data.get("_sGroupName", "")
        self.authors = authors


@dataclass
class Credits:
    groups: List[CreditGroup] = field(default_factory=list)

    def __init__(self, data: Dict[str, Any]):
        if not isinstance(data, dict):
            return

        groups = []
        groups_data = data.get("_aCredits", [])
        if isinstance(groups_data, list):
            groups = [CreditGroup(group) for group in groups_data]

        self.groups = groups

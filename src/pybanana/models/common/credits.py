"""Credit-related shared components."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class AffiliatedStudio:
    profile_url: str = ""
    name: str = ""
    flag_url: str = ""
    banner_url: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AffiliatedStudio":
        if not isinstance(data, dict):
            return cls()
            
        return cls(
            profile_url=data.get("_sProfileUrl", "") or "",
            name=data.get("_sName", "") or "",
            flag_url=data.get("_sFlagUrl", "") or "",
            banner_url=data.get("_sBannerUrl", "") or ""
        )

@dataclass
class Author:
    role: str = ""
    name: str = ""
    id: Optional[int] = None
    upic_url: str = ""
    profile_url: str = ""
    is_online: bool = False
    affiliated_studio: Optional[AffiliatedStudio] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Author":
        if not isinstance(data, dict):
            return cls()
            
        affiliated_studio = None
        studio_data = data.get("_aAffiliatedStudio")
        if isinstance(studio_data, dict):
            affiliated_studio = AffiliatedStudio.from_dict(studio_data)

        return cls(
            role=data.get("_sRole", "") or "",
            name=data.get("_sName", "") or "",
            id=data.get("_idRow") or 0,
            upic_url=data.get("_sUpicUrl", "") or "",
            profile_url=data.get("_sProfileUrl", "") or "",
            is_online=bool(data.get("_bIsOnline", False)),
            affiliated_studio=affiliated_studio
        )

@dataclass
class CreditGroup:
    group_name: str = ""
    authors: List[Author] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CreditGroup":
        if not isinstance(data, dict):
            return cls()

        authors = []
        author_data = data.get("_aAuthors", []) or []
        if isinstance(author_data, list):
            authors = [Author.from_dict(author) for author in author_data]

        return cls(
            group_name=data.get("_sGroupName", "") or "",
            authors=authors
        )

@dataclass
class Credits:
    groups: List[CreditGroup] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Credits":
        if not isinstance(data, dict):
            return cls()

        groups = []
        groups_data = data.get("_aGroups", []) or []
        if isinstance(groups_data, list):
            groups = [CreditGroup.from_dict(group) for group in groups_data]

        return cls(groups=groups)
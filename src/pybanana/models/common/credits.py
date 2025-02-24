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
        return cls(
            role=data.get("_sRole", "") or "",
            name=data.get("_sName", "") or "",
            id=data.get("_idRow") or 0,
            upic_url=data.get("_sUpicUrl", "") or "",
            profile_url=data.get("_sProfileUrl", "") or "",
            is_online=data.get("_bIsOnline", False),
            affiliated_studio=AffiliatedStudio.from_dict(data["_aAffiliatedStudio"]) if "_aAffiliatedStudio" in data and data["_aAffiliatedStudio"] else None
        )

@dataclass
class CreditGroup:
    group_name: str = ""
    authors: List[Author] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CreditGroup":
        return cls(
            group_name=data.get("_sGroupName", "") or "",
            authors=[Author.from_dict(author) for author in data.get("_aAuthors", [])]
        )

@dataclass
class Credits:
    groups: List[CreditGroup] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Optional[Dict[str, Any] | List[Dict[str, Any]]]) -> "Credits":
        if data is None:
            return cls()
        if isinstance(data, list):
            return cls(groups=[CreditGroup.from_dict(group) for group in data])
        return cls(groups=[CreditGroup.from_dict(group) for group in data.get("_aGroups", [])])
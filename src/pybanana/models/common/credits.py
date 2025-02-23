"""Credit-related shared components."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class AffiliatedStudio:
    profile_url: str
    name: str
    flag_url: str
    banner_url: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AffiliatedStudio":
        return cls(
            profile_url=data["_sProfileUrl"],
            name=data["_sName"],
            flag_url=data["_sFlagUrl"],
            banner_url=data["_sBannerUrl"]
        )

@dataclass
class Author:
    role: str
    name: str
    id: Optional[int] = None
    upic_url: Optional[str] = None
    profile_url: Optional[str] = None
    is_online: Optional[bool] = None
    affiliated_studio: Optional[AffiliatedStudio] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Author":
        return cls(
            role=data["_sRole"],
            name=data["_sName"],
            id=data.get("_idRow"),
            upic_url=data.get("_sUpicUrl"),
            profile_url=data.get("_sProfileUrl"),
            is_online=data.get("_bIsOnline"),
            affiliated_studio=AffiliatedStudio.from_dict(data["_aAffiliatedStudio"]) if "_aAffiliatedStudio" in data else None
        )

@dataclass
class CreditGroup:
    group_name: str
    authors: List[Author]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CreditGroup":
        return cls(
            group_name=data["_sGroupName"],
            authors=[Author.from_dict(author) for author in data["_aAuthors"]]
        )

@dataclass
class Credits:
    """Credits section."""
    groups: List[CreditGroup] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Credits":
        if not data or "_aCredits" not in data:
            return cls([])
        return cls(
            groups=[CreditGroup.from_dict(group) for group in data["_aCredits"]]
        )
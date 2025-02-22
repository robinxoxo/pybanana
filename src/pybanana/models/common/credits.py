"""Credit-related shared components."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class Author:
    role: str
    id: int
    name: str
    upic_url: Optional[str]
    profile_url: str
    is_online: bool

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Author":
        return cls(
            role=data["_sRole"],
            id=data["_idRow"],
            name=data["_sName"],
            upic_url=data.get("_sUpicUrl"),
            profile_url=data["_sProfileUrl"],
            is_online=data["_bIsOnline"]
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
class Credit:
    """A credit entry."""
    member_id: int
    name: str
    role: str
    link: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Credit":
        return cls(
            member_id=data.get("_idMember"),
            name=data.get("_sName", ""),
            role=data.get("_sRole", ""),
            link=data.get("_sLink")
        )

@dataclass
class Credits:
    """Credits section."""
    entries: List[Credit] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Credits":
        if not data:
            return cls([])
        return cls(
            entries=[Credit.from_dict(credit) for credit in data]
        )
from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class Member:
    """A GameBanana member."""
    id: int = 0
    name: str = ""
    is_online: bool = False
    has_ripe: bool = False
    profile_url: str = ""
    avatar_url: str = ""
    
    @classmethod
    def from_dict(cls, data: Any) -> Optional["Member"]:
        if not isinstance(data, dict):
            return None
            
        return cls(
            id=data.get("_idRow", 0) or 0,
            name=data.get("_sName", "") or "",
            is_online=bool(data.get("_bIsOnline", False)),
            has_ripe=bool(data.get("_bHasRipe", False)),
            profile_url=data.get("_sProfileUrl", "") or "",
            avatar_url=data.get("_sAvatarUrl", "") or ""
        )

@dataclass
class Moderator(Member):
    """Inherits base member attributes from Member class"""
    pass

@dataclass
class Manager(Member):
    """Inherits base member attributes from Member class"""
    pass


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

    def __init__(self, data: dict[str, Any]):
        self.id = data.get("_idRow", 0) or 0
        self.name = data.get("_sName", "") or ""
        self.is_online = bool(data.get("_bIsOnline", False))
        self.has_ripe = bool(data.get("_bHasRipe", False))
        self.profile_url = data.get("_sProfileUrl", "") or ""
        self.avatar_url = data.get("_sAvatarUrl", "") or ""


@dataclass
class Moderator(Member):
    """Inherits base member attributes from Member class"""
    pass

@dataclass
class Manager(Member):
    """Inherits base member attributes from Member class"""
    pass

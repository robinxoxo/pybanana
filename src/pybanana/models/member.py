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
    def from_dict(cls, data: Optional[Any]) -> Optional["Member"]:
        
        # Return None if input is None or empty list
        if data is None or (isinstance(data, list) and not data):
            return None
            
        # Convert list to dict if needed
        if isinstance(data, list):
            data = {}
            
        return cls(
            id=data.get("_idRow", 0),
            name=data.get("_sName", ""),
            is_online=data.get("_bIsOnline", False),
            has_ripe=data.get("_bHasRipe", False),
            profile_url=data.get("_sProfileUrl", ""),
            avatar_url=data.get("_sAvatarUrl", "")
        )

@dataclass
class Moderator(Member):
    """Inherits base member attributes from Member class"""
    pass

@dataclass
class Manager(Member):
    """Inherits base member attributes from Member class"""
    pass


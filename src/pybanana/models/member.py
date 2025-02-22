from dataclasses import dataclass
from typing import List, Optional, Any

@dataclass
class Member:
    """A GameBanana member."""
    id: int
    name: str
    is_online: bool
    has_ripe: bool
    profile_url: str
    avatar_url: str
    
    @classmethod
    def from_dict(cls, data: Optional[dict]) -> "Member":
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

@dataclass
class Cooltip:
    border_style: Optional[str] = None
    font: Optional[str] = None
    box_border_style: Optional[str] = None
    font_color: Optional[str] = None
    background_color: Optional[str] = None
    text_color: Optional[str] = None
    border_color: Optional[str] = None
    link_color: Optional[str] = None
    link_hover_color: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Cooltip":
        return cls(
            border_style=data.get("_sBorderStyle"),
            font=data.get("_sFont"), 
            box_border_style=data.get("_sBoxBorderStyle"),
            font_color=data.get("_sFontColor"),
            background_color=data.get("_sBackgroundColor"),
            text_color=data.get("_sTextColor"),
            border_color=data.get("_sBorderColor"),
            link_color=data.get("_sLinkColor"),
            link_hover_color=data.get("_sLinkHoverColor")
        )


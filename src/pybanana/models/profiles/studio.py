"""Studio profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..member import Member
from ..common.profile import Profile
from ..common.preview import PreviewMedia
from ..common.category import ModCategory

@dataclass
class OpenPosition:
    """Open position in a studio."""
    skill_id: str = ""
    skill: str = ""
    game_id: str = ""
    game: Dict[str, str] = field(default_factory=lambda: {"name": "", "url": ""})
    notes: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OpenPosition":
        return cls(
            skill_id=data.get("_idSkillRow", "") or "",
            skill=data.get("_sSkill", "") or "",
            game_id=data.get("_idGameRow", "") or "",
            game=data.get("_aGame") or {"name": "", "url": ""},
            notes=data.get("_sNotes", "") or ""
        )

@dataclass
class StudioProfile:
    """Studio profile information."""
    base: Profile
    motto: Optional[str] = None
    join_mode: str = ""
    flag_url: Optional[str] = None
    banner_url: Optional[str] = None
    member_count: int = 0
    post_count: int = 0
    social_links: List[Dict[str, str]] = field(default_factory=list)
    profile_template: str = ""
    profile_modules: List[str] = field(default_factory=list)
    open_positions: List[OpenPosition] = field(default_factory=list)
    leadership: List[Member] = field(default_factory=list)
    accessor_is_in_guild: bool = False
    accessor_has_pending_join_request: bool = False
    game: Dict[str, str] = field(default_factory=dict)  # Changed to use field(default_factory=dict)

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StudioProfile":
        base = Profile.from_dict(data)
        return cls(
            base=base,
            motto=data.get("_sMotto"),
            join_mode=data.get("_sJoinMode", ""),
            flag_url=data.get("_sFlagUrl"),
            banner_url=data.get("_sBannerUrl"),
            member_count=data.get("_iMemberCount", 0),  # Added default
            post_count=data.get("_nPostCount", 0),  # Added default
            social_links=data.get("_aSocialLinks", []),
            profile_template=data.get("_sProfileTemplate", ""),
            profile_modules=data.get("_aProfileModules", []),
            open_positions=[OpenPosition.from_dict(pos) for pos in data.get("_aOpenPositions", [])],
            leadership=[member for member in (Member.from_dict(m) for m in data.get("_aLeadership", [])) if member is not None],
            accessor_is_in_guild=data.get("_bAccessorIsInGuild", False),
            accessor_has_pending_join_request=data.get("_bAccessorHasPendingJoinRequest", False)
        )
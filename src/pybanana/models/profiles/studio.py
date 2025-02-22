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
    skill_id: str
    skill: str
    game_id: str
    game: Dict[str, str]
    notes: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OpenPosition":
        return cls(
            skill_id=data["_idSkillRow"],
            skill=data["_sSkill"],
            game_id=data["_idGameRow"],
            game=data["_aGame"],
            notes=data["_sNotes"]
        )

@dataclass
class StudioProfile:
    """Studio profile information."""
    base: Profile
    motto: Optional[str]
    join_mode: str
    flag_url: Optional[str]
    banner_url: Optional[str]
    member_count: int
    post_count: int
    social_links: List[Dict[str, str]]
    profile_template: str
    profile_modules: List[str]
    open_positions: List[OpenPosition]
    leadership: List[Member]
    accessor_is_in_guild: bool
    accessor_has_pending_join_request: bool

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StudioProfile":
        base = Profile.from_dict(data)
        return cls(
            base=base,
            motto=data.get("_sMotto", None),
            join_mode=data.get("_sJoinMode", ""),
            flag_url=data.get("_sFlagUrl"),
            banner_url=data.get("_sBannerUrl"),
            member_count=data.get("_iMemberCount"),
            post_count=data.get("_nPostCount"),
            social_links=data.get("_aSocialLinks", []),
            profile_template=data.get("_sProfileTemplate", ""),
            profile_modules=data.get("_aProfileModules", []),
            open_positions=[OpenPosition.from_dict(pos) for pos in data.get("_aOpenPositions", [])],
            leadership=[Member.from_dict(member) for member in data.get("_aLeadership", [])],
            accessor_is_in_guild=data.get("_bAccessorIsInGuild", False),
            accessor_has_pending_join_request=data.get("_bAccessorHasPendingJoinRequest", False)
        )
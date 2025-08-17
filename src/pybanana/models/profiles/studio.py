"""Studio profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

from ..member import Member
from ..common.profile import Profile

@dataclass
class OpenPosition:
    """Open position in a studio."""
    skill_id: str = ""
    skill: str = ""
    game_id: str = ""
    game: Dict[str, str] = field(default_factory=lambda: {"name": "", "url": ""})
    notes: str = ""

    def __init__(self, data: Dict[str, Any]):
        self.skill_id = data.get("_idSkillRow", "")
        self.skill = data.get("_sSkill", "")
        self.game_id = data.get("_idGameRow", "")
        self.game = data.get("_aGame", {"name": "", "url": ""})
        self.notes = data.get("_sNotes", "")


@dataclass
class Studio(Profile):
    """Studio profile information."""

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
        return getattr(self, name)

    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        self.motto = data.get("_sMotto", "")
        self.join_mode = data.get("_sJoinMode", "")
        self.flag_url = data.get("_sFlagUrl", "")
        self.banner_url = data.get("_sBannerUrl", "")
        self.member_count = data.get("_iMemberCount", 0)
        self.post_count = data.get("_nPostCount", 0)
        self.social_links = data.get("_aSocialLinks", [])
        self.profile_template = data.get("_sProfileTemplate", "")
        self.profile_modules = data.get("_aProfileModules", [])
        self.open_positions = [
            OpenPosition(pos) for pos in data.get("_aOpenPositions", [])
        ]
        self.leadership = [
            member
            for member in (Member(m) for m in data.get("_aLeadership", []))
            if member is not None
        ]
        self.accessor_is_in_guild = data.get("_bAccessorIsInGuild", False)
        self.accessor_has_pending_join_request = data.get(
            "_bAccessorHasPendingJoinRequest", False
        )

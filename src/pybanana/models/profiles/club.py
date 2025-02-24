"""Club profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..member import Member
from ..common.profile import Profile
from ..common.preview import PreviewMedia
from ..common.managers import ManagerRecord

@dataclass
class ClubProfile:
    """Club profile information."""
    base: Profile
    status: int = 0
    is_private: bool = False
    date_modified: Optional[datetime] = None
    date_added: Optional[datetime] = None
    preview_media: Optional[PreviewMedia] = None
    accessor_is_submitter: bool = False
    is_trashed: bool = False
    name: str = ""
    post_count: int = 0
    initial_visibility: str = ""
    has_files: bool = False
    text: str = ""
    member_count: int = 0
    last_activity_date: Optional[datetime] = None
    show_ripe_promo: bool = False
    submitter: Optional[Member] = None
    flag_url: str = ""
    banner_url: str = ""
    motto: str = ""
    join_mode: str = ""
    social_links: List[str] = field(default_factory=list)
    profile_template: str = ""
    profile_modules: List[str] = field(default_factory=list)
    accessor_is_in_guild: bool = False
    accessor_has_pending_join_request: bool = False
    leadership: List[ManagerRecord] = field(default_factory=list)

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClubProfile":
        base = Profile.from_dict(data)

        return cls(
            base=base,
            status=int(data.get("_nStatus", 0)),
            is_private=data.get("_bIsPrivate", False),
            date_modified=datetime.fromtimestamp(data.get("_tsDateModified", 0)),
            date_added=datetime.fromtimestamp(data.get("_tsDateAdded", 0)),
            preview_media=PreviewMedia.from_dict(data.get("_aPreviewMedia", []) or []),
            accessor_is_submitter=data.get("_bAccessorIsSubmitter", False),
            is_trashed=data.get("_bIsTrashed", False),
            name=data.get("_sName", "") or "",
            post_count=data.get("_nPostCount", 0) or 0,
            initial_visibility=data.get("_sInitialVisibility", "") or "",
            has_files=data.get("_bHasFiles", False),
            text=data.get("_sText", "") or "",
            member_count=data.get("_nMemberCount", 0) or 0,
            last_activity_date=datetime.fromtimestamp(data.get("_tsLastActivityDate", 0)),
            show_ripe_promo=data.get("_bShowRipePromo", False),
            submitter=Member.from_dict(data.get("_aMember", {})) if data.get("_aMember") else None,
            flag_url=data.get("_sFlagUrl", "") or "",
            banner_url=data.get("_sBannerUrl", "") or "",
            motto=data.get("_sMotto", "") or "",
            join_mode=data.get("_sJoinMode", "") or "",
            social_links=data.get("_aSocialLinks", []),
            profile_template=data.get("_sProfileTemplate", "") or "",
            profile_modules=data.get("_aProfileModules", []),
            accessor_is_in_guild=data.get("_bAccessorIsInGuild", False),
            accessor_has_pending_join_request=data.get("_bAccessorHasPendingJoinRequest", False),
            leadership=[ManagerRecord.from_dict(leader) for leader in data.get("_aLeadership", [])]
        )
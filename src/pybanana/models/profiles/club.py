"""Club profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..member import Member
from ..common.profile import Profile
from ..common.preview import PreviewMedia
from ..common.managers import Manager


@dataclass
class Club(Profile):
    """Club profile information."""

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
    leadership: List[Manager] = field(default_factory=list)

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self, name)

    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)

        self.status = int(data.get("_nStatus", 0))
        self.is_private = data.get("_bIsPrivate", False)
        self.date_modified = datetime.fromtimestamp(data.get("_tsDateModified", 0))
        self.date_added = datetime.fromtimestamp(data.get("_tsDateAdded", 0))
        self.preview_media = PreviewMedia(
            {}
            if isinstance(data.get("_aPreviewMedia", {}), list)
            else data.get("_aPreviewMedia", {})
        )
        self.accessor_is_submitter = data.get("_bAccessorIsSubmitter", False)
        self.is_trashed = data.get("_bIsTrashed", False)
        self.name = data.get("_sName", "") or ""
        self.post_count = data.get("_nPostCount", 0) or 0
        self.initial_visibility = data.get("_sInitialVisibility", "") or ""
        self.has_files = data.get("_bHasFiles", False)
        self.text = data.get("_sText", "") or ""
        self.member_count = data.get("_nMemberCount", 0) or 0
        self.last_activity_date = datetime.fromtimestamp(
            data.get("_tsLastActivityDate", 0)
        )
        self.show_ripe_promo = data.get("_bShowRipePromo", False)
        self.submitter = (
            Member(data.get("_aMember", {})) if data.get("_aMember") else None
        )
        self.flag_url = data.get("_sFlagUrl", "") or ""
        self.banner_url = data.get("_sBannerUrl", "") or ""
        self.motto = data.get("_sMotto", "") or ""
        self.join_mode = data.get("_sJoinMode", "") or ""
        self.social_links = data.get("_aSocialLinks", [])
        self.profile_template = data.get("_sProfileTemplate", "") or ""
        self.profile_modules = data.get("_aProfileModules", [])
        self.accessor_is_in_guild = data.get("_bAccessorIsInGuild", False)
        self.accessor_has_pending_join_request = data.get(
            "_bAccessorHasPendingJoinRequest", False
        )
        self.leadership = [Manager(leader) for leader in data.get("_aLeadership", [])]

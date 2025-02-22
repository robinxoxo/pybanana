"""Club profile and related functionality."""
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..member import Member
from ..common.profile import Profile
from ..common.preview import PreviewMedia

@dataclass
class ClubProfile:
    """Club profile information."""
    base: Profile
    status: int
    is_private: bool
    date_modified: datetime
    date_added: datetime
    preview_media: PreviewMedia
    accessor_is_submitter: bool
    is_trashed: bool
    name: str
    post_count: int
    initial_visibility: str
    has_files: bool
    text: str
    member_count: int
    last_activity_date: datetime
    show_ripe_promo: bool
    submitter: Member
    flag_url: Optional[str]
    banner_url: Optional[str]
    motto: str
    join_mode: str
    social_links: List[str]
    profile_template: str
    profile_modules: List[str]
    accessor_is_in_guild: bool
    accessor_has_pending_join_request: bool
    leadership: List[Member]

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClubProfile":
        base = Profile.from_dict(data)
        return cls(
            base=base,
            status=int(data["_nStatus"]),
            is_private=data["_bIsPrivate"],
            date_modified=datetime.fromtimestamp(data["_tsDateModified"]),
            date_added=datetime.fromtimestamp(data["_tsDateAdded"]),
            preview_media=PreviewMedia.from_dict(data["_aPreviewMedia"]),
            accessor_is_submitter=data["_bAccessorIsSubmitter"],
            is_trashed=data["_bIsTrashed"],
            name=data["_sName"],
            post_count=data["_nPostCount"],
            initial_visibility=data["_sInitialVisibility"],
            has_files=data["_bHasFiles"],
            text=data["_sText"],
            member_count=data["_nMemberCount"],
            last_activity_date=datetime.fromtimestamp(data["_tsLastActivityDate"]),
            show_ripe_promo=data["_bShowRipePromo"],
            submitter=Member.from_dict(data["_aMember"]),
            flag_url=data.get("_sFlagUrl"),
            banner_url=data.get("_sBannerUrl"),
            motto=data["_sMotto"],
            join_mode=data["_sJoinMode"],
            social_links=data["_aSocialLinks"],
            profile_template=data["_sProfileTemplate"],
            profile_modules=data["_aProfileModules"],
            accessor_is_in_guild=data["_bAccessorIsInGuild"],
            accessor_has_pending_join_request=data["_bAccessorHasPendingJoinRequest"],
            leadership=[Member.from_dict(member) for member in data["_aLeadership"]]
        )
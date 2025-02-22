"""Bug profile and related functionality."""
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List
from datetime import datetime

from ..member import Member
from ..common.profile import Profile
from ..common.preview import PreviewMedia
from ..common.embeddable import Embeddable

@dataclass
class BugProfile:
    """Bug profile information."""
    base: Profile
    status: int
    is_private: bool
    date_modified: datetime
    date_added: datetime
    preview_media: PreviewMedia
    accessor_is_submitter: bool
    is_trashed: bool
    post_count: int
    thanks_count: int
    initial_visibility: str
    has_files: bool
    subscriber_count: int
    text: str
    resolution: str
    resolution_key: str
    priority: str
    priority_key: str
    source_url: str
    show_ripe_promo: bool
    embeddables: List[Embeddable]
    submitter: Optional[Member]
    accessor_subscription_row_id: int = 0
    accessor_is_subscribed: bool = False
    accessor_has_thanked: bool = False

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BugProfile":
        base = Profile.from_dict(data)
        return cls(
            base=base,
            status=int(data.get("_nStatus", 0)),
            is_private=data.get("_bIsPrivate", False),
            date_modified=datetime.fromtimestamp(data.get("_tsDateModified", 0)),
            date_added=datetime.fromtimestamp(data.get("_tsDateAdded", 0)),
            preview_media=PreviewMedia.from_dict(data.get("_aPreviewMedia", {})),
            accessor_is_submitter=data.get("_bAccessorIsSubmitter", False),
            is_trashed=data.get("_bIsTrashed", False),
            post_count=data.get("_nPostCount", 0),
            thanks_count=data.get("_nThanksCount", 0),
            initial_visibility=data.get("_sInitialVisibility", ""),
            has_files=data.get("_bHasFiles", False),
            subscriber_count=data.get("_nSubscriberCount", 0),
            text=data.get("_sText", ""),
            resolution=data.get("_sResolution", ""),
            resolution_key=data.get("_sResolutionKey", ""),
            priority=data.get("_sPriority", ""),
            priority_key=data.get("_sPriorityKey", ""), 
            source_url=data.get("_sSourceUrl", ""),
            show_ripe_promo=data.get("_bShowRipePromo", False),
            embeddables=data.get("_aEmbeddables", []),
            submitter=Member.from_dict(data.get("_aMember")),
            accessor_subscription_row_id=data.get("_idAccessorSubscriptionRow", 0),
            accessor_is_subscribed=data.get("_bAccessorIsSubscribed", False),
            accessor_has_thanked=data.get("_bAccessorHasThanked", False)
        )
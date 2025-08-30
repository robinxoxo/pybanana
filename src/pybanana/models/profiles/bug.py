"""Bug profile and related functionality."""
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List
from datetime import datetime

from ..member import Member
from ..common.profile import Profile
from ..common.preview import PreviewMedia
from ..common.embeddable import Embeddable
from ..common.file import File  # Added missing import


@dataclass
class Bug(Profile):
    """Bug profile information."""

    status: int = 0
    is_private: bool = False
    date_modified: Optional[datetime] = None
    date_added: Optional[datetime] = None
    preview_media: Optional[PreviewMedia] = None
    accessor_is_submitter: bool = False
    is_trashed: bool = False
    post_count: int = 0
    thanks_count: int = 0
    initial_visibility: str = ""
    has_files: bool = False
    subscriber_count: int = 0
    text: str = ""
    resolution: str = ""
    resolution_key: str = ""
    priority: str = ""
    priority_key: str = ""
    source_url: str = ""
    show_ripe_promo: bool = False
    embeddables: List[Embeddable] = field(default_factory=list)
    submitter: Optional[Member] = None
    attachments: List[File] = field(default_factory=list)
    accessor_subscription_row_id: int = 0
    accessor_is_subscribed: bool = False
    accessor_has_thanked: bool = False

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self, name)

    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        preview_media_data = data.get("_aPreviewMedia", {})
        if isinstance(preview_media_data, list):
            preview_media_data = {}

            self.status = int(data.get("_nStatus", 0))
            self.is_private = data.get("_bIsPrivate", False)
            self.date_modified = datetime.fromtimestamp(data.get("_tsDateModified", 0))

            self.date_added = datetime.fromtimestamp(data.get("_tsDateAdded", 0))
            self.preview_media = PreviewMedia(preview_media_data)
            self.accessor_is_submitter = data.get("_bAccessorIsSubmitter", False)
            self.is_trashed = data.get("_bIsTrashed", False)
            self.post_count = data.get("_nPostCount", 0) or 0
            self.thanks_count = data.get("_nThanksCount", 0) or 0
            self.initial_visibility = data.get("_sInitialVisibility", "") or ""
            self.has_files = data.get("_bHasFiles", False) or False
            self.subscriber_count = data.get("_nSubscriberCount", 0) or 0
            self.text = data.get("_sText", "") or ""
            self.resolution = data.get("_sResolution", "") or ""
            self.resolution_key = data.get("_sResolutionKey", "") or ""
            self.priority = data.get("_sPriority", "") or ""
            self.priority_key = data.get("_sPriorityKey", "") or ""
            self.source_url = data.get("_sSourceUrl", "") or ""
            self.show_ripe_promo = data.get("_bShowRipePromo", False) or False
            self.embeddables = [
                Embeddable(embed) for embed in data.get("_aEmbeddables", [])
            ]
            self.submitter = (
                Member(data.get("_aMember", {})) if data.get("_aMember") else None
            )
            self.attachments = [File(file) for file in data.get("_aAttachments", [])]
            self.accessor_subscription_row_id = (
                data.get("_idAccessorSubscriptionRow", 0) or 0
            )
            self.accessor_is_subscribed = (
                data.get("_bAccessorIsSubscribed", False) or False
            )
            self.accessor_has_thanked = data.get("_bAccessorHasThanked", False) or False

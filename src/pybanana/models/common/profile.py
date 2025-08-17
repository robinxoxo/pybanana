"""Base profile functionality shared by all profile types."""
from dataclasses import dataclass, field
from typing import Dict, Any, Optional
from datetime import datetime
from .preview import PreviewMedia

@dataclass
class Profile:
    """Base profile class."""
    id: Optional[int] = None
    status: Optional[int] = None
    is_private: Optional[bool] = None
    date_modified: Optional[datetime] = None
    date_added: Optional[datetime] = None
    profile_url: Optional[str] = None
    preview_media: Optional[PreviewMedia] = None
    name: Optional[str] = None
    initial_visibility: Optional[str] = None
    has_files: Optional[bool] = None
    subscriber_count: Optional[int] = None
    show_ripe_promo: Optional[bool] = None
    accessor_subscription_row: Optional[int] = None
    accessor_is_subscribed: Optional[bool] = None

    def __init__(self, data: Dict[str, Any]):
        preview_media_data = data.get("_aPreviewMedia", {})
        if not isinstance(preview_media_data, dict):
            preview_media_data = {}
        self.id = data.get("_idRow")
        self.status = (
            int(data.get("_nStatus", 0)) if data.get("_nStatus") is not None else None
        )
        self.is_private = data.get("_bIsPrivate")
        self.date_modified = (
            datetime.fromtimestamp(data["_tsDateModified"])
            if "_tsDateModified" in data
            else None
        )
        self.date_added = (
            datetime.fromtimestamp(data["_tsDateAdded"])
            if "_tsDateAdded" in data
            else None
        )
        self.profile_url = data.get("_sProfileUrl")
        self.preview_media = PreviewMedia(preview_media_data)
        self.name = data.get("_sName")
        self.initial_visibility = data.get("_sInitialVisibility")
        self.has_files = data.get("_bHasFiles")
        self.subscriber_count = data.get("_nSubscriberCount")
        self.show_ripe_promo = data.get("_bShowRipePromo")
        self.accessor_subscription_row = data.get("_idAccessorSubscriptionRow")
        self.accessor_is_subscribed = data.get("_bAccessorIsSubscribed")

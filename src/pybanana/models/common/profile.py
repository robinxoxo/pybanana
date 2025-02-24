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

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Profile":
        preview_media_data = data.get("_aPreviewMedia")
        return cls(
            id=data.get("_idRow"),
            status=int(data.get("_nStatus", 0)) if data.get("_nStatus") is not None else None,
            is_private=data.get("_bIsPrivate"),
            date_modified=datetime.fromtimestamp(data["_tsDateModified"]) if "_tsDateModified" in data else None,
            date_added=datetime.fromtimestamp(data["_tsDateAdded"]) if "_tsDateAdded" in data else None,
            profile_url=data.get("_sProfileUrl"),
            preview_media=PreviewMedia.from_dict(preview_media_data) if preview_media_data else None,
            name=data.get("_sName"),
            initial_visibility=data.get("_sInitialVisibility"),
            has_files=data.get("_bHasFiles"),
            subscriber_count=data.get("_nSubscriberCount"),
            show_ripe_promo=data.get("_bShowRipePromo"),
            accessor_subscription_row=data.get("_idAccessorSubscriptionRow"),
            accessor_is_subscribed=data.get("_bAccessorIsSubscribed")
        )
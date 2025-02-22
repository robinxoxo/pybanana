"""Result models for GameBanana."""
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from .common.preview import PreviewMedia
from .member import Member

@dataclass
class Result:
    """Result information for a search query."""
    id_row: int
    model_name: str
    singular_title: str
    icon_classes: str
    name: str
    profile_url: str
    date_added: int
    date_modified: int
    has_files: bool
    preview_media: Optional[PreviewMedia] = None
    submitter: Optional[Member] = None
    initial_visibility: Optional[str] = None
    has_content_ratings: bool = False
    is_owned_by_accessor: bool = False

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Result':
        """Create a Result instance from a dictionary."""
        return cls(
            id_row=data["_idRow"],
            model_name=data["_sModelName"],
            singular_title=data["_sSingularTitle"],
            icon_classes=data["_sIconClasses"],
            name=data["_sName"],
            profile_url=data["_sProfileUrl"],
            date_added=data["_tsDateAdded"],
            date_modified=data["_tsDateModified"],
            has_files=data["_bHasFiles"],
            preview_media=PreviewMedia.from_dict(data["_aPreviewMedia"]) if "_aPreviewMedia" in data and data["_aPreviewMedia"] else None,
            submitter=Member.from_dict(data["_aSubmitter"]) if "_aSubmitter" in data and data["_aSubmitter"] else None,
            initial_visibility=data.get("_sInitialVisibility"),
            has_content_ratings=data.get("_bHasContentRatings", False),
            is_owned_by_accessor=data.get("_bIsOwnedByAccessor", False)
        )
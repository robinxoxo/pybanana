"""Result models for GameBanana."""
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from .common.preview import PreviewMedia
from .member import Member
from .common.file import File

@dataclass
class Result:
    """Result information for a search query."""
    id: Optional[int]
    model_name: Optional[str]
    singular_title: Optional[str] 
    icon_classes: Optional[str]
    name: Optional[str]
    url: Optional[str]
    date_added: Optional[int]
    date_modified: Optional[int]
    has_files: Optional[bool]
    preview_media: Optional[PreviewMedia] = None
    submitter: Optional[Member] = None
    initial_visibility: Optional[str] = None
    has_content_ratings: bool = False
    is_owned_by_accessor: bool = False
    files: List[File] = field(default_factory=list)
    accepts_donations: bool = False
    is_trashed: bool = False
    is_withheld: bool = False

    def __init__(self, data: Dict[str, Any]):
        """Create a Result instance from a dictionary."""
        # Handle both search results and download page formats
        files = [File(f) for f in data.get("_aFiles", [])] if "_aFiles" in data else []
        self.id = data.get("_idRow")
        self.model_name = data.get("_sModelName")
        self.singular_title = data.get("_sSingularTitle")
        self.icon_classes = data.get("_sIconClasses")
        self.name = data.get("_sName")
        self.url = data.get("_sProfileUrl")
        self.date_added = data.get("_tsDateAdded")
        self.date_modified = data.get("_tsDateModified")
        self.has_files = data.get("_bHasFiles")
        self.preview_media = (
            PreviewMedia(data["_aPreviewMedia"])
            if "_aPreviewMedia" in data and data["_aPreviewMedia"]
            else None
        )
        self.submitter = (
            Member(data["_aSubmitter"])
            if "_aSubmitter" in data and data["_aSubmitter"]
            else None
        )
        self.initial_visibility = data.get("_sInitialVisibility")
        self.has_content_ratings = data.get("_bHasContentRatings", False)
        self.is_owned_by_accessor = data.get("_bIsOwnedByAccessor", False)
        self.files = files
        self.accepts_donations = data.get("_bAcceptsDonations", False)
        self.is_trashed = data.get("_bIsTrashed", False)
        self.is_withheld = data.get("_bIsWithheld", False)

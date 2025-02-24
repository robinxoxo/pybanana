"""Result models for GameBanana."""
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from .common.preview import PreviewMedia
from .member import Member
from .common.file import File

@dataclass
class Result:
    """Result information for a search query."""
    id_row: Optional[int]
    model_name: Optional[str]
    singular_title: Optional[str] 
    icon_classes: Optional[str]
    name: Optional[str]
    profile_url: Optional[str]
    date_added: Optional[int]
    date_modified: Optional[int]
    has_files: Optional[bool]
    preview_media: Optional[PreviewMedia] = None
    submitter: Optional[Member] = None
    initial_visibility: Optional[str] = None
    has_content_ratings: bool = False
    is_owned_by_accessor: bool = False
    files: List[File] = None
    accepts_donations: bool = False
    is_trashed: bool = False
    is_withheld: bool = False

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Result':
        """Create a Result instance from a dictionary."""
        # Handle both search results and download page formats
        files = [File.from_dict(f) for f in data.get("_aFiles", [])] if "_aFiles" in data else []
        
        return cls(
            id_row=data.get("_idRow"),
            model_name=data.get("_sModelName"),
            singular_title=data.get("_sSingularTitle"),
            icon_classes=data.get("_sIconClasses"),
            name=data.get("_sName"),
            profile_url=data.get("_sProfileUrl"),
            date_added=data.get("_tsDateAdded"),
            date_modified=data.get("_tsDateModified"), 
            has_files=data.get("_bHasFiles"),
            preview_media=PreviewMedia.from_dict(data["_aPreviewMedia"]) if "_aPreviewMedia" in data and data["_aPreviewMedia"] else None,
            submitter=Member.from_dict(data["_aSubmitter"]) if "_aSubmitter" in data and data["_aSubmitter"] else None,
            initial_visibility=data.get("_sInitialVisibility"),
            has_content_ratings=data.get("_bHasContentRatings", False),
            is_owned_by_accessor=data.get("_bIsOwnedByAccessor", False),
            files=files,
            accepts_donations=data.get("_bAcceptsDonations", False),
            is_trashed=data.get("_bIsTrashed", False),
            is_withheld=data.get("_bIsWithheld", False)
        )
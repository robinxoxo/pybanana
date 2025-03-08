"""Discussion record models."""
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

from ..member import Member
from .profile import Profile
from .category import ModCategory
from ..profiles.game import GameSection

@dataclass
class Submission:
    """Submission information in a discussion record."""
    base: Profile
    model_name: Optional[str] = None
    singular_title: Optional[str] = None
    icon_classes: Optional[str] = None
    date_updated: Optional[int] = None
    submitter: Optional[Member] = None
    game: Optional[GameSection] = None
    root_category: Optional[ModCategory] = None
    version: Optional[str] = None
    is_obsolete: bool = False
    has_content_ratings: bool = False
    like_count: int = 0
    post_count: int = 0
    was_featured: bool = False
    view_count: int = 0
    is_owned_by_accessor: bool = False

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Submission":
        if not data:
            return None
        
        return cls(
            base=Profile.from_dict(data),
            model_name=data.get("_sModelName"),
            singular_title=data.get("_sSingularTitle"),
            icon_classes=data.get("_sIconClasses"),
            date_updated=data.get("_tsDateUpdated"),
            submitter=Member.from_dict(data.get("_aSubmitter")) if data.get("_aSubmitter") else None,
            game=GameSection.from_dict(data.get("_aGame")) if data.get("_aGame") else None,
            root_category=ModCategory.from_dict(data.get("_aRootCategory")) if data.get("_aRootCategory") else None,
            version=data.get("_sVersion"),
            is_obsolete=data.get("_bIsObsolete", False),
            has_content_ratings=data.get("_bHasContentRatings", False),
            like_count=data.get("_nLikeCount", 0) or 0,
            post_count=data.get("_nPostCount", 0) or 0,
            was_featured=data.get("_bWasFeatured", False),
            view_count=data.get("_nViewCount", 0) or 0,
            is_owned_by_accessor=data.get("_bIsOwnedByAccessor", False)
        )

@dataclass
class Post:
    """Post information in a discussion record."""
    id: Optional[int] = None
    date_added: Optional[int] = None
    text: Optional[str] = None
    poster: Optional[Member] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Post":
        if not data:
            return None
        return cls(
            id=data.get("_idRow", 0) or 0,
            date_added=data.get("_tsDateAdded", 0) or 0,
            text=data.get("_sText", "") or "",
            poster=Member.from_dict(data.get("_aPoster", {})) if data.get("_aPoster") else None
        )

@dataclass
class DiscussionRecord:
    """A discussion record containing a submission and a post."""
    submission: Optional[Submission] = None
    post: Optional[Post] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DiscussionRecord":
        """Create a DiscussionRecord from dictionary data."""
        if not data:
            return cls()
            
        return cls(
            submission=Submission.from_dict(data.get("_aSubmission")) if data.get("_aSubmission") else None,
            post=Post.from_dict(data.get("_aPost")) if data.get("_aPost") else None
        )

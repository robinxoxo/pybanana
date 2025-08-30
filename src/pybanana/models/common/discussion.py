"""Discussion record models."""
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

from ..member import Member
from .profile import Profile
from .category import ModCategory
from ..profiles.game import GameSection


@dataclass
class Submission(Profile):
    """Submission information in a discussion record."""

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

    def __init__(self, data: Dict[str, Any]):
        if not data:
            return None

        super().__init__(data)
        self.model_name = data.get("_sModelName")
        self.singular_title = data.get("_sSingularTitle")
        self.icon_classes = data.get("_sIconClasses")
        self.date_updated = data.get("_tsDateUpdated")
        self.submitter = (
            Member(data.get("_aSubmitter")) if data.get("_aSubmitter") else None
        )
        self.game = GameSection(data.get("_aGame")) if data.get("_aGame") else None
        self.root_category = (
            ModCategory(data.get("_aRootCategory"))
            if data.get("_aRootCategory")
            else None
        )
        self.version = data.get("_sVersion")
        self.is_obsolete = data.get("_bIsObsolete", False)
        self.has_content_ratings = data.get("_bHasContentRatings", False)
        self.like_count = data.get("_nLikeCount", 0) or 0
        self.post_count = data.get("_nPostCount", 0) or 0
        self.was_featured = data.get("_bWasFeatured", False)
        self.view_count = data.get("_nViewCount", 0) or 0
        self.is_owned_by_accessor = data.get("_bIsOwnedByAccessor", False)


@dataclass
class Post:
    """Post information in a discussion record."""
    id: Optional[int] = None
    date_added: Optional[int] = None
    text: Optional[str] = None
    poster: Optional[Member] = None

    def __init__(self, data: Dict[str, Any]):
        if not data:
            return

        self.id = data.get("_idRow", 0)
        self.date_added = data.get("_tsDateAdded", 0)
        self.text = data.get("_sText", "")
        self.poster = Member(data.get("_aPoster", {})) if data.get("_aPoster") else None


@dataclass
class Discussion:
    """A discussion record containing a submission and a post."""
    submission: Optional[Submission] = None
    post: Optional[Post] = None

    def __init__(self, data: Dict[str, Any]):
        """Create a DiscussionRecord from dictionary data."""
        if not data:
            return

        self.submission = (
            Submission(data.get("_aSubmission")) if data.get("_aSubmission") else None
        )
        self.post = Post(data.get("_aPost")) if data.get("_aPost") else None

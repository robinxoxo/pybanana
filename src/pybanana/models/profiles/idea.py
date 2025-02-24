"""Idea profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..common.profile import Profile
from ..common.ratings import RatingsSummary
from ..common.embeddable import Embeddable

@dataclass
class IdeaProfile:
    base: Profile  # Required field
    text: str = ""
    post_count: int = 0
    has_revisions: bool = False
    has_changelog: bool = False
    is_private: bool = False
    is_shared: bool = False
    sorting_priority: int = 0
    supports_downvoting: bool = False
    ratings_summary: Optional[RatingsSummary] = None
    embeddables: List[Embeddable] = field(default_factory=list)

    def __post_init__(self):
        if self.ratings_summary is None:
            self.ratings_summary = RatingsSummary.from_dict({})

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "IdeaProfile":
        base = Profile.from_dict(data)
        # Wrap the ratings data in the expected structure
        ratings_data = {"_aRatingsSummary": data.get("_aRatingsSummary", {})} if "_aRatingsSummary" in data else {}
        
        return cls(
            base=base,
            text=data.get("_sText", "") or "",
            post_count=data.get("_nPostCount", 0) or 0,
            has_revisions=data.get("_bHasRevisions", False),
            has_changelog=data.get("_bHasChangelog", False),
            is_private=data.get("_bIsPrivate", False),
            is_shared=data.get("_bIsShared", False),
            sorting_priority=data.get("_nSortingPriority", 0) or 0,
            supports_downvoting=data.get("_bSupportsDownvoting", False),
            ratings_summary=RatingsSummary.from_dict(ratings_data),
            embeddables=[Embeddable.from_dict(embed) for embed in data.get("_aEmbeddables", [])]
        )
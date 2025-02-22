"""Idea profile and related functionality."""
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..common.profile import Profile
from ..common.ratings import RatingsSummary
from ..common.embeddable import Embeddable

@dataclass
class IdeaProfile:
    base: Profile
    text: str
    post_count: int
    has_revisions: bool
    has_changelog: bool
    is_private: bool
    is_shared: bool
    sorting_priority: int
    supports_downvoting: bool
    ratings_summary: RatingsSummary
    embeddables: List[Embeddable]

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "IdeaProfile":
        base = Profile.from_dict(data)
        return cls(
            base=base,
            text=data["_sText"],
            post_count=data["_nPostCount"],
            has_revisions=data["_bHasRevisions"],
            has_changelog=data["_bHasChangelog"],
            is_private=data["_bIsPrivate"],
            is_shared=data["_bIsShared"],
            sorting_priority=data["_nSortingPriority"],
            supports_downvoting=data["_bSupportsDownvoting"],
            ratings_summary=RatingsSummary.from_dict(data["_aRatingsSummary"]),
            embeddables=[Embeddable.from_dict(embed) for embed in data["_aEmbeddables"]]
        )
"""Idea profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..common.profile import Profile
from ..common.ratings import RatingsSummary
from ..common.embeddable import Embeddable


@dataclass
class Idea(Profile):
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
            self.ratings_summary = RatingsSummary({})

    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        # Wrap the ratings data in the expected structure
        ratings_data = {"_aRatingsSummary": data.get("_aRatingsSummary", {})} if "_aRatingsSummary" in data else {}

        self.text = data.get("_sText", "")
        self.post_count = data.get("_nPostCount", 0)
        self.has_revisions = data.get("_bHasRevisions", False)
        self.has_changelog = data.get("_bHasChangelog", False)
        self.is_private = data.get("_bIsPrivate", False)
        self.is_shared = data.get("_bIsShared", False)
        self.sorting_priority = data.get("_nSortingPriority", 0)
        self.supports_downvoting = data.get("_bSupportsDownvoting", False)
        self.ratings_summary = RatingsSummary(ratings_data)
        self.embeddables = [
            Embeddable(embed) for embed in data.get("_aEmbeddables", [])
        ]

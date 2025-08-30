"""Rating-related shared components."""
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class RatingBreakdownItem:
    count: int = 0
    negativity: int = 0
    positivity: int = 0
    weight: int = 0

    def __init__(self, data: Dict[str, Any]):
        if not isinstance(data, dict):
            return

        self.count = data.get("_nCount", 0)
        self.negativity = data.get("_nNegativity", 0)
        self.positivity = data.get("_nPositivity", 0)
        self.weight = data.get("_nWeight", 0)


@dataclass
class RatingsSummary:
    ratings_count: int = 0
    cumulative_rating: int = 0
    cumulative_positivity: int = 0
    cumulative_negativity: int = 0
    ratings_breakdown: Dict[str, RatingBreakdownItem] = field(default_factory=dict)

    def __post_init__(self):
        if self.ratings_breakdown is None:
            self.ratings_breakdown = {}

    def __init__(self, data: Dict[str, Any]):
        if not isinstance(data, dict):
            return

        breakdown = {}
        breakdown_data = data.get("_aRatingsBreakdown", {}) or {}
        if isinstance(breakdown_data, dict):
            for rating_key, rating_data in breakdown_data.items():
                breakdown[rating_key] = RatingBreakdownItem(rating_data)

        self.ratings_count = data.get("_nRatingsCount", 0)
        self.cumulative_rating = data.get("_nCumulativeRating", 0)
        self.cumulative_positivity = data.get("_nCumulativePositivity", 0)
        self.cumulative_negativity = data.get("_nCumulativeNegativity", 0)
        self.ratings_breakdown = breakdown

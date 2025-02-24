"""Rating-related shared components."""
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class RatingBreakdownItem:
    count: int = 0
    title: str = ""
    verb: str = ""
    icon_url: str = ""
    icon_classes: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RatingBreakdownItem":
        return cls(
            count=data.get("_nCount", 0) or 0,
            title=data.get("_sTitle", "") or "",
            verb=data.get("_sVerb", "") or "",
            icon_url=data.get("_sIconUrl", "") or "",
            icon_classes=data.get("_sIconClasses", "") or ""
        )

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

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RatingsSummary":
        if not isinstance(data, dict):
            data = {}
            
        # Extract the ratings summary data from the nested structure
        ratings_data = data.get("_aRatingsSummary", {}) or {}
        breakdown_data = ratings_data.get("_aRatingsBreakdown", {}) or {}
        breakdown = {
            k: RatingBreakdownItem.from_dict(v) 
            for k, v in breakdown_data.items()
        }
        
        return cls(
            ratings_count=ratings_data.get("_nRatingsCount", 0) or 0,
            cumulative_rating=ratings_data.get("_iCumulativeRating", 0) or 0,
            cumulative_positivity=ratings_data.get("_iCumulativePositivity", 0) or 0,
            cumulative_negativity=ratings_data.get("_iCumulativeNegativity", 0) or 0,
            ratings_breakdown=breakdown
        )

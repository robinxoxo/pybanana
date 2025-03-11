"""Rating-related shared components."""
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class RatingBreakdownItem:
    count: int = 0
    negativity: int = 0
    positivity: int = 0
    weight: int = 0
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RatingBreakdownItem":
        if not isinstance(data, dict):
            return cls()
            
        return cls(
            count=data.get("_nCount", 0) or 0,
            negativity=data.get("_nNegativity", 0) or 0,
            positivity=data.get("_nPositivity", 0) or 0,
            weight=data.get("_nWeight", 0) or 0
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
            return cls()
            
        breakdown = {}
        breakdown_data = data.get("_aRatingsBreakdown", {}) or {}
        if isinstance(breakdown_data, dict):
            for rating_key, rating_data in breakdown_data.items():
                breakdown[rating_key] = RatingBreakdownItem.from_dict(rating_data)
                
        return cls(
            ratings_count=data.get("_nRatingsCount", 0) or 0,
            cumulative_rating=data.get("_nCumulativeRating", 0) or 0,
            cumulative_positivity=data.get("_nCumulativePositivity", 0) or 0,
            cumulative_negativity=data.get("_nCumulativeNegativity", 0) or 0,
            ratings_breakdown=breakdown
        )

"""Rating-related shared components."""
from dataclasses import dataclass
from typing import Optional
from typing import Dict, Any

@dataclass
class RatingsSummary:
    total_votes: int
    average_rating: float
    current_user_rating: Optional[int]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RatingsSummary":
        return cls(
            total_votes=data["total_votes"],
            average_rating=data["average_rating"],
            current_user_rating=data.get("current_user_rating")
        )
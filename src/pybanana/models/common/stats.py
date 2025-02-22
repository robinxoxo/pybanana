"""Stats-related shared components."""
from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class CoreStats:
    account_age: str
    current_submissions: int
    current_subscribers: int
    thanks_received: int
    points: int
    submissions_featured: int
    medals_count: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CoreStats":
        return cls(
            account_age=data["_sAccountAge"],
            current_submissions=data["_nCurrentSubmissions"],
            current_subscribers=data["_nCurrentSubscribers"],
            thanks_received=data["_nThanksReceived"],
            points=data["_nPoints"],
            submissions_featured=data["_nSubmissionsFeatured"],
            medals_count=data["_nMedalsCount"]
        )
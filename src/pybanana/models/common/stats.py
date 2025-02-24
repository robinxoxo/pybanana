"""Stats-related shared components."""
from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class CoreStats:
    account_age: str = ""
    current_submissions: int = 0
    current_subscribers: int = 0
    thanks_received: int = 0
    points: int = 0
    submissions_featured: int = 0
    medals_count: int = 0

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CoreStats":
        return cls(
            account_age=data.get("_sAccountAge", "") or "",
            current_submissions=data.get("_nCurrentSubmissions", 0) or 0,
            current_subscribers=data.get("_nCurrentSubscribers", 0) or 0,
            thanks_received=data.get("_nThanksReceived", 0) or 0,
            points=data.get("_nPoints", 0) or 0,
            submissions_featured=data.get("_nSubmissionsFeatured", 0) or 0,
            medals_count=data.get("_nMedalsCount", 0) or 0
        )
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

    def __init__(self, data: Dict[str, Any]):
        self.account_age = data.get("_sAccountAge", "")
        self.current_submissions = data.get("_nCurrentSubmissions", 0)
        self.current_subscribers = data.get("_nCurrentSubscribers", 0)
        self.thanks_received = data.get("_nThanksReceived", 0)
        self.points = data.get("_nPoints", 0)
        self.submissions_featured = data.get("_nSubmissionsFeatured", 0)
        self.medals_count = data.get("_nMedalsCount", 0)

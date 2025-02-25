from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Medals:
    """A GameBanana achievement medal."""
    id: int
    image_url: str
    name: str
    grade: str
    grade_title: str
    date_added: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Medals":
        """Create a Medals instance from a dictionary."""

        timestamp = data.get("_tsDateAdded", 0)
        try:
            date_added = datetime.fromtimestamp(timestamp) if timestamp > 0 else None
        except (OSError, ValueError):
            date_added = None

        return cls(
            id=data["_idRow"],
            image_url=data["_sImage"],
            name=data["_sName"],
            grade=data["_sGrade"],
            grade_title=data["_sGradeTitle"],
            date_added=date_added
        )
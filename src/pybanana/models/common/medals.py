from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Medals:
    """A GameBanana achievement medal."""
    id: int = 0
    image_url: str = ""
    name: str = ""
    grade: str = ""
    grade_title: str = ""
    date_added: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Medals":
        """Create a Medals instance from a dictionary."""
        if not isinstance(data, dict):
            return cls()

        try:
            timestamp = data.get("_tsDateAdded", 0)
            date_added = datetime.fromtimestamp(timestamp) if timestamp else None
        except (ValueError, OSError):
            date_added = None

        return cls(
            id=data.get("_idRow", 0) or 0,
            image_url=data.get("_sImage", "") or "",
            name=data.get("_sName", "") or "",
            grade=data.get("_sGrade", "") or "",
            grade_title=data.get("_sGradeTitle", "") or "",
            date_added=date_added
        )
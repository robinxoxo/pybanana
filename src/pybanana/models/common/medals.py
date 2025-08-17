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

    def __init__(self, data: dict):
        """Create a Medals instance from a dictionary."""
        if not isinstance(data, dict):
            return

        try:
            timestamp = data.get("_tsDateAdded", 0)
            date_added = datetime.fromtimestamp(timestamp) if timestamp else None
        except (ValueError, OSError):
            date_added = None

        self.id = data.get("_idRow", 0)
        self.image_url = data.get("_sImage", "")
        self.name = data.get("_sName", "")
        self.grade = data.get("_sGrade", "")
        self.grade_title = data.get("_sGradeTitle", "")
        self.date_added = date_added

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from dataclasses import dataclass, field
from ..member import Member

@dataclass
class SubjectShaper:
    """A GameBanana subject shaper configuration."""
    border_style: str = ""
    font: str = ""
    text_color: str = ""
    text_hover_color: str = ""
    border_color: str = ""
    border_hover_color: str = ""

    def __init__(self, data: dict):
        self.border_style = data.get("_sBorderStyle", "")
        self.font = data.get("_sFont", "")
        self.text_color = data.get("_sTextColor", "")
        self.text_hover_color = data.get("_sTextHoverColor", "")
        self.border_color = data.get("_sBorderColor", "")
        self.border_hover_color = data.get("_sBorderHoverColor", "")


@dataclass
class Buddy(Member):
    """A GameBanana buddy relationship."""
    clearance_levels: List[str] = field(default_factory=list)
    hd_avatar_url: str = ""
    upic_url: str = ""
    subject_shaper: Optional[SubjectShaper] = None
    subject_shaper_css_code: str = ""
    date_added: Optional[datetime] = None

    def __init__(self, data: dict):
        buddy_data: dict = data.get("_aBuddy", {})
        member_data = super().__init__(buddy_data).__dict__
        timestamp = data.get("_tsDateAdded", 0)
        try:
            date_added = datetime.fromtimestamp(timestamp) if timestamp > 0 else None
        except (OSError, ValueError):
            date_added = None
        self.id = member_data["id"]
        self.name = member_data["name"]
        self.is_online = member_data["is_online"]
        self.has_ripe = member_data["has_ripe"]
        self.profile_url = member_data["profile_url"]
        self.avatar_url = member_data["avatar_url"]
        self.clearance_levels = buddy_data.get("_aClearanceLevels", [])
        self.hd_avatar_url = buddy_data.get("_sHdAvatarUrl", "")
        self.upic_url = buddy_data.get("_sUpicUrl", "")
        self.subject_shaper = SubjectShaper(buddy_data.get("_aSubjectShaper", {}))
        self.subject_shaper_css_code = buddy_data.get("_sSubjectShaperCssCode", "")
        self.date_added = date_added

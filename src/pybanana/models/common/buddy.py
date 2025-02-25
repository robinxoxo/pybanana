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
    
    @classmethod
    def from_dict(cls, data: dict) -> "SubjectShaper":
        return cls(
            border_style=data.get("_sBorderStyle", ""),
            font=data.get("_sFont", ""),
            text_color=data.get("_sTextColor", ""),
            text_hover_color=data.get("_sTextHoverColor", ""),
            border_color=data.get("_sBorderColor", ""),
            border_hover_color=data.get("_sBorderHoverColor", "")
        )

@dataclass
class Buddy(Member):
    """A GameBanana buddy relationship."""
    clearance_levels: List[str] = field(default_factory=list)
    hd_avatar_url: str = ""
    upic_url: str = ""
    subject_shaper: Optional[SubjectShaper] = None
    subject_shaper_css_code: str = ""
    date_added: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Buddy":
        buddy_data = data.get("_aBuddy", {})
        member_data = super().from_dict(buddy_data).__dict__
        timestamp = data.get("_tsDateAdded", 0)
        try:
            date_added = datetime.fromtimestamp(timestamp) if timestamp > 0 else None
        except (OSError, ValueError):
            date_added = None
            
        return cls(
            id=member_data['id'],
            name=member_data['name'],
            is_online=member_data['is_online'],
            has_ripe=member_data['has_ripe'],
            profile_url=member_data['profile_url'],
            avatar_url=member_data['avatar_url'],
            clearance_levels=buddy_data.get("_aClearanceLevels", []),
            hd_avatar_url=buddy_data.get("_sHdAvatarUrl", ""),
            upic_url=buddy_data.get("_sUpicUrl", ""),
            subject_shaper=SubjectShaper.from_dict(buddy_data.get("_aSubjectShaper", {})),
            subject_shaper_css_code=buddy_data.get("_sSubjectShaperCssCode", ""),
            date_added=date_added
        )

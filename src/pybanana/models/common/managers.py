"""Manager-related shared components."""
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from datetime import datetime

from ..member import Member


@dataclass
class Manager:
    member: Member  # Required field
    modgroups: List[str] = field(default_factory=list)
    date_added: Optional[datetime] = None

    def __init__(self, data: Dict[str, Any]):
        self.member = Member(data.get("_aMember", {}))
        self.modgroups = data.get("_aModgroups", []) or []
        timestamp = data.get("_tsDateAdded", 0)
        self.date_added = datetime.fromtimestamp(timestamp) if timestamp else None

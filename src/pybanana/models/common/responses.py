"""API response models for GameBanana endpoints."""
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from ..result import Result
from .moderators import ModeratorRecord
from .managers import ManagerRecord

@dataclass
class ModeratorResponse:
    """Response from the moderators endpoint."""
    records: List[ModeratorRecord] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ModeratorResponse':
        records = [rec for rec in (ModeratorRecord.from_dict(record) for record in data.get('_aRecords', [])) if rec is not None]
        return cls(records=records)

@dataclass
class GameManagerResponse:
    """Response from the game managers endpoint."""
    metadata: Optional[Dict[str, Any]] = None
    records: List[ManagerRecord] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: List[Dict[str, Any]] | Dict[str, Any]) -> 'GameManagerResponse':
        """Create a GameManagerResponse instance from either a list or object format."""
        if isinstance(data, list):
            records = [rec for rec in (ManagerRecord.from_dict(record) for record in data) if rec is not None]
            return cls(metadata=None, records=records)
        
        records = [rec for rec in (ManagerRecord.from_dict(record) for record in data.get('_aRecords', [])) if rec is not None]
        return cls(
            metadata=data.get('_aMetadata'),
            records=records
        )

@dataclass
class ResultResponse:
    """Container for search results that matches the GameBanana API response structure."""
    records: List[Result] = field(default_factory=list)
    record_count: int = 0

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ResultResponse':
        """Create a ResultList instance from a dictionary."""
        return cls(
            records=[Result.from_dict(record) for record in data["_aRecords"]],
            record_count=data.get('_nRecordCount', 0)
        )
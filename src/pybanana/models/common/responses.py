"""API response models for GameBanana endpoints."""
from dataclasses import dataclass
from typing import Dict, Any, List
from ..result import Result

@dataclass
class ModeratorResponse:
    """Response from the moderators endpoint."""
    records: List[Dict[str, Any]]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ModeratorResponse':
        return cls(records=data['_aRecords'])

@dataclass
class GameManagerResponse:
    """Response from the game managers endpoint."""
    metadata: Dict[str, Any]
    records: List[Dict[str, Any]]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'GameManagerResponse':
        return cls(
            metadata=data['_aMetadata'],
            records=data['_aRecords']
        )

@dataclass
class ResultResponse:
    """Container for search results that matches the GameBanana API response structure."""
    records: List[Result]
    record_count: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ResultResponse':
        """Create a ResultList instance from a dictionary."""
        return cls(
            records=[Result.from_dict(record) for record in data["_aRecords"]],
            record_count=data["_nRecordCount"]
        )
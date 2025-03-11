"""API response models for GameBanana endpoints."""
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from ..result import Result
from .moderators import ModeratorRecord
from .managers import ManagerRecord
from .online import OnlineRecord
from .discussion import DiscussionRecord

@dataclass
class ModeratorResponse:
    """Response from the moderators endpoint."""
    metadata: Dict[str, Any] = field(default_factory=dict)
    records: List[ModeratorRecord] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ModeratorResponse':
        records = [rec for rec in (ModeratorRecord.from_dict(record) for record in data.get('_aRecords', [])) if rec is not None]
        return cls(
            metadata=data.get("_aMetadata", {}),
            records=records
        )

@dataclass
class GameManagerResponse:
    """Response from the game managers endpoint."""
    metadata: Dict[str, Any] = field(default_factory=dict)
    records: List[ManagerRecord] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: List[Dict[str, Any]] | Dict[str, Any]) -> 'GameManagerResponse':
        """Create a GameManagerResponse instance from either a list or object format."""
        if isinstance(data, list):
            records = [rec for rec in (ManagerRecord.from_dict(record) for record in data) if rec is not None]
            return cls(records=records)
        
        records = [rec for rec in (ManagerRecord.from_dict(record) for record in data.get('_aRecords', [])) if rec is not None]
        return cls(
            metadata=data.get("_aMetadata", {}),
            records=records
        )

@dataclass
class ResultResponse:
    """Container for search results that matches the GameBanana API response structure."""
    metadata: Dict[str, Any] = field(default_factory=dict)
    records: List[Result] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ResultResponse':
        """Create a ResultList instance from a dictionary."""
        return cls(
            metadata=data.get("_aMetadata", {}),
            records=[Result.from_dict(record) for record in data["_aRecords"]],
        )
    
@dataclass
class OnlineResponse:
    """Container for online status that matches the GameBanana API response structure."""
    metadata: Dict[str, Any] = field(default_factory=dict)
    records: List[OnlineRecord] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'OnlineResponse':
        """Create an OnlineResponse instance from a dictionary."""
        records = [rec for rec in (OnlineRecord.from_dict(record) for record in data.get('_aRecords', [])) if rec is not None]
        return cls(
            metadata=data.get("_aMetadata", {}),
            records=records
        )
    
@dataclass
class DiscussionResponse:
    """Container for discussion records that matches the GameBanana API response structure."""
    metadata: Dict[str, Any] = field(default_factory=dict)
    records: List[DiscussionRecord] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DiscussionResponse':
        """Create a DiscussionResponse instance from a dictionary."""
        records = [rec for rec in (DiscussionRecord.from_dict(record) for record in data.get('_aRecords', [])) if rec is not None]
        return cls(
            metadata=data.get("_aMetadata", {}),
            records=records
        )
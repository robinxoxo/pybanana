"""API response models for GameBanana endpoints."""
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from ..result import Result
from .moderators import Moderator
from .managers import Manager
from .online import Online
from .discussion import Discussion

@dataclass
class ModeratorResponse:
    """Response from the moderators endpoint."""
    metadata: Dict[str, Any] = field(default_factory=dict)
    records: List[Moderator] = field(default_factory=list)

    def __init__(self, data: Dict[str, Any]):
        records = [
            rec
            for rec in (Moderator(record) for record in data.get("_aRecords", []))
            if rec is not None
        ]
        self.metadata = data.get("_aMetadata", {})
        self.records = records


@dataclass
class GameManagerResponse:
    """Response from the game managers endpoint."""
    metadata: Dict[str, Any] = field(default_factory=dict)
    records: List[Manager] = field(default_factory=list)

    def __init__(self, data: List[Dict[str, Any]] | Dict[str, Any]):
        """Create a GameManagerResponse instance from either a list or object format."""
        if isinstance(data, list):
            records = [
                rec for rec in (Manager(record) for record in data) if rec is not None
            ]
        else:

            records = [
                rec
                for rec in (Manager(record) for record in data.get("_aRecords", []))
                if rec is not None
            ]

        self.metadata = data.get("_aMetadata", {})
        self.records = records


@dataclass
class ResultResponse:
    """Container for search results that matches the GameBanana API response structure."""
    metadata: Dict[str, Any] = field(default_factory=dict)
    records: List[Result] = field(default_factory=list)

    def __init__(self, data: Dict[str, Any]):
        """Create a ResultList instance from a dictionary."""
        self.metadata = data.get("_aMetadata", {})
        self.records = [Result(record) for record in data["_aRecords"]]


@dataclass
class OnlineResponse:
    """Container for online status that matches the GameBanana API response structure."""
    metadata: Dict[str, Any] = field(default_factory=dict)
    records: List[Online] = field(default_factory=list)

    def __init__(self, data: Dict[str, Any]):
        """Create an OnlineResponse instance from a dictionary."""
        records = [
            rec
            for rec in (Online(record) for record in data.get("_aRecords", []))
            if rec is not None
        ]
        self.metadata = data.get("_aMetadata", {})
        self.records = records


@dataclass
class DiscussionResponse:
    """Container for discussion records that matches the GameBanana API response structure."""
    metadata: Dict[str, Any] = field(default_factory=dict)
    records: List[Discussion] = field(default_factory=list)

    def __init__(self, data: Dict[str, Any]):
        """Create a DiscussionResponse instance from a dictionary."""
        records = [
            rec
            for rec in (Discussion(record) for record in data.get("_aRecords", []))
            if rec is not None
        ]
        self.metadata = data.get("_aMetadata", {})
        self.records = records

"""
PyBanana - A Python wrapper for the GameBanana API.
"""

# Package metadata
__version__ = "0.4.5"
__author__ = "robin"
__license__ = "MIT"

# Main API class
from .api import PyBanana

# Import all models from the models package
from .models import (
    # Base models
    Member, Moderator, Manager,
    Buddy, SubjectShaper,
    Profile,
    PreviewMedia, PreviewMediaImage,
    ModCategory,
    
    # Common components
    Author, CreditGroup, AffiliatedStudio, Credits,
    Embeddable,
    RatingsSummary, RatingBreakdownItem,
    CoreStats,
    Bio, BioEntry,
    ProfileField, ContactInfo, PcSpecs, SoftwareKit, GamingDevices,
    File,
    LicenseChecklist,
    Medals,
    OnlineStatus,
    ManagerRecord, 
    ModeratorRecord,
    DiscussionRecord,
    
    # Profile models
    MemberProfile,
    ModProfile,
    GameProfile, GameSection,
    AppProfile, AppFeatures,
    StudioProfile, OpenPosition,
    ClubProfile,
    BugProfile,
    IdeaProfile,
    
    # Response models
    ModeratorResponse,
    GameManagerResponse,
    ResultResponse,
    OnlineResponse,
    DiscussionResponse
)

from .models.result import Result

# Define what should be imported with "from pybanana import *"
__all__ = [
    "PyBanana",
    # Base models
    "Member", "Moderator", "Manager",
    "Buddy", "SubjectShaper",
    "Profile",
    "PreviewMedia", "PreviewMediaImage",
    "ModCategory",
    
    # Common components
    "Author", "CreditGroup", "AffiliatedStudio", "Credits",
    "Embeddable",
    "RatingsSummary", "RatingBreakdownItem",
    "CoreStats",
    "Bio", "BioEntry",
    "ProfileField", "ContactInfo", "PcSpecs", "SoftwareKit", "GamingDevices",
    "File",
    "LicenseChecklist",
    "Medals",
    "OnlineStatus",
    "ManagerRecord", 
    "ModeratorRecord",
    "DiscussionRecord",
    
    # Profile models
    "MemberProfile",
    "ModProfile",
    "GameProfile", "GameSection",
    "AppProfile", "AppFeatures",
    "StudioProfile", "OpenPosition",
    "ClubProfile", 
    "BugProfile",
    "IdeaProfile",
    
    # Response models
    "ModeratorResponse",
    "GameManagerResponse",
    "ResultResponse",
    "OnlineResponse",
    "DiscussionResponse",
    
    # Additional models
    "Result",
]
"""GameBanana API models."""
# Base models
from .member import Member, Moderator, Manager
from .common.buddy import Buddy, SubjectShaper
from .common.profile import Profile
from .common.preview import PreviewMedia, PreviewMediaImage
from .common.category import ModCategory

# Common components
from .common.credits import Author, CreditGroup, Credits, AffiliatedStudio
from .common.embeddable import Embeddable
from .common.ratings import RatingsSummary, RatingBreakdownItem
from .common.stats import CoreStats
from .common.bio import Bio, BioEntry
from .common.field import ProfileField, ContactInfo, PcSpecs, SoftwareKit, GamingDevices
from .common.file import File
from .common.license import LicenseChecklist
from .common.medals import Medals
from .common.online import OnlineStatus
from .common.managers import Manager
from .common.moderators import Moderator
from .common.discussion import Discussion, Post, Submission
from .common.responses import (
    ModeratorResponse,
    GameManagerResponse,
    ResultResponse,
    OnlineResponse,
    DiscussionResponse
)

# Profile models
from .profiles.game import Game, GameSection
from .profiles.app import App, AppFeatures
from .profiles.bug import Bug
from .profiles.idea import Idea
from .profiles.member import Member
from .profiles.mod import Mod
from .profiles.studio import Studio, OpenPosition
from .profiles.club import Club

__all__ = [
    # Base models
    "Member",
    "Moderator",
    "Manager",
    "Buddy",
    "SubjectShaper",
    "Profile",
    "PreviewMedia",
    "PreviewMediaImage",
    "ModCategory",
    # Common components
    "Author",
    "CreditGroup",
    "Credits",
    "AffiliatedStudio",
    "Embeddable",
    "RatingsSummary",
    "RatingBreakdownItem",
    "CoreStats",
    "Bio",
    "BioEntry",
    "ProfileField",
    "ContactInfo",
    "PcSpecs",
    "SoftwareKit",
    "GamingDevices",
    "File",
    "LicenseChecklist",
    "Medals",
    "OnlineStatus",
    "Manager",
    "Moderator",
    "Discussion",
    "Post",
    "Submission",
    # Response models
    "ModeratorResponse",
    "GameManagerResponse",
    "ResultResponse",
    "OnlineResponse",
    "DiscussionResponse",
    # Profile models
    "Game",
    "GameSection",
    "App",
    "AppFeatures",
    "Bug",
    "Idea",
    "Member",
    "Mod",
    "Studio",
    "OpenPosition",
    "Club",
]

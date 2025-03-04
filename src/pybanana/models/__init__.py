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
from .common.managers import ManagerRecord
from .common.moderators import ModeratorRecord
from .common.responses import (
    ModeratorResponse,
    GameManagerResponse,
    ResultResponse,
    OnlineResponse
)

# Profile models
from .profiles.game import GameProfile, GameSection
from .profiles.app import AppProfile, AppFeatures
from .profiles.bug import BugProfile
from .profiles.idea import IdeaProfile
from .profiles.member import MemberProfile
from .profiles.mod import ModProfile
from .profiles.studio import StudioProfile, OpenPosition
from .profiles.club import ClubProfile

__all__ = [
    # Base models
    'Member', 'Moderator', 'Manager',
    'Buddy', 'SubjectShaper',
    'Profile',
    'PreviewMedia', 'PreviewMediaImage',
    'ModCategory',
    
    # Common components
    'Author', 'CreditGroup', 'Credits', 'AffiliatedStudio',
    'Embeddable',
    'RatingsSummary', 'RatingBreakdownItem',
    'CoreStats',
    'Bio', 'BioEntry',
    'ProfileField', 'ContactInfo', 'PcSpecs', 'SoftwareKit', 'GamingDevices',
    'File',
    'LicenseChecklist',
    'Medals',
    'OnlineStatus',
    'ManagerRecord',
    'ModeratorRecord',
    
    # Response models
    'ModeratorResponse',
    'GameManagerResponse',
    'ResultResponse',
    'OnlineResponse',
    
    # Profile models
    'GameProfile', 'GameSection',
    'AppProfile', 'AppFeatures',
    'BugProfile',
    'IdeaProfile',
    'MemberProfile',
    'ModProfile',
    'StudioProfile', 'OpenPosition',
    'ClubProfile',
]
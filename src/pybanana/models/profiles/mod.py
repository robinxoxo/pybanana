"""Mod profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

from ..member import Member
from ..common.profile import Profile
from ..common.credits import Credits
from ..common.category import ModCategory
from ..common.embeddable import Embeddable
from ..common.file import File
from ..common.license import LicenseChecklist
from .studio import Studio
from .game import Game


@dataclass
class Mod(Profile):
    """Mod profile information."""
    game: Game | None = None
    feedback_instructions: str = ""
    accessor_is_submitter: bool = False
    is_trashed: bool = False
    is_withheld: bool = False
    name: str = ""
    updates_count: int = 0
    has_updates: bool = False
    all_todos_count: int = 0
    has_todos: bool = False
    post_count: int = 0
    attributes: Dict[str, List[str]] = field(default_factory=dict)
    tags: List[Dict[str, str]] = field(default_factory=list)
    created_by_submitter: bool = False
    is_ported: bool = False
    thanks_count: int = 0
    initial_visibility: str = ""
    download_url: str = ""
    download_count: int = 0
    files: List[File] = field(default_factory=list)
    subscriber_count: int = 0
    studio: Optional[Studio] = None
    contributing_studios: List[Any] = field(default_factory=list)
    license: str = ""
    license_checklist: Optional[LicenseChecklist] = None
    description: str = ""
    generate_table_of_contents: bool = False
    text: str = ""
    like_count: int = 0
    view_count: int = 0
    is_mapped: bool = False
    is_textured: bool = False
    is_animated: str = ""
    accepts_donations: bool = False
    show_ripe_promo: bool = False
    embeddables: List[Embeddable] = field(default_factory=list)
    submitter: Optional[Member] = None
    category: Optional[ModCategory] = None
    credits: Optional[Credits] = None
    advanced_requirements_exist: bool = False
    requirements: List[List[str]] = field(default_factory=list)
    accessor_subscription_row_id: int = 0
    accessor_is_subscribed: bool = False
    accessor_has_thanked: bool = False
    accessor_has_unliked: bool = False
    accessor_has_liked: bool = False

    def __getattr__(self, name):
        """Delegate attribute access to base Profile."""
        return getattr(self, name)

    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        self.game = Game(data["_aGame"]) if "_aGame" in data else None
        self.feedback_instructions = data.get("_sFeedbackInstructions", "")
        self.accessor_is_submitter = data.get("_bAccessorIsSubmitter", False)
        self.is_trashed = data.get("_bIsTrashed", False)
        self.is_withheld = data.get("_bIsWithheld", False)
        self.name = data.get("_sName", "")
        self.updates_count = data.get("_nUpdatesCount", 0)
        self.has_updates = data.get("_bHasUpdates", False)
        self.all_todos_count = data.get("_nAllTodosCount", 0)
        self.has_todos = data.get("_bHasTodos", False)
        self.post_count = data.get("_nPostCount", 0)
        self.attributes = data.get("_aAttributes", {})
        self.tags = data.get("_aTags", [])
        self.created_by_submitter = data.get("_bCreatedBySubmitter", False)
        self.is_ported = data.get("_bIsPorted", False)
        self.thanks_count = data.get("_nThanksCount", 0)
        self.initial_visibility = data.get("_sInitialVisibility", "")
        self.download_url = data.get("_sDownloadUrl", "")
        self.download_count = data.get("_nDownloadCount", 0)
        self.files = [File(f) for f in data.get("_aFiles", [])]
        self.subscriber_count = data.get("_nSubscriberCount", 0)
        self.studio = Studio(data["_aStudio"]) if "_aStudio" in data else None
        self.contributing_studios = data.get("_aContributingStudios", [])
        self.license = data.get("_sLicense", "")
        self.license_checklist = (
            LicenseChecklist(data["_aLicenseChecklist"])
            if "_aLicenseChecklist" in data
            else None
        )
        self.description = data.get("_sDescription", "")
        self.generate_table_of_contents = data.get("_bGenerateTableOfContents", False)
        self.text = data.get("_sText", "")
        self.like_count = data.get("_nLikeCount", 0)
        self.view_count = data.get("_nViewCount", 0)
        self.is_mapped = data.get("_bIsMapped", False)
        self.is_textured = data.get("_bIsTextured", False)
        self.is_animated = data.get("_xIsAnimated", "")
        self.accepts_donations = data.get("_bAcceptsDonations", False)
        self.show_ripe_promo = data.get("_bShowRipePromo", False)
        self.embeddables = [Embeddable(item) for item in data.get("_aEmbeddables", [])]
        self.submitter = Member(data["_aSubmitter"]) if "_aSubmitter" in data else None
        self.category = (
            ModCategory(data["_aCategory"]) if "_aCategory" in data else None
        )
        self.credits = Credits(data) if "_aCredits" in data else None
        self.advanced_requirements_exist = data.get(
            "_bAdvancedRequirementsExist", False
        )
        self.requirements = data.get("_aRequirements", [])
        self.accessor_subscription_row_id = data.get("_idAccessorSubscriptionRow", 0)
        self.accessor_is_subscribed = data.get("_bAccessorIsSubscribed", False)
        self.accessor_has_thanked = data.get("_bAccessorHasThanked", False)
        self.accessor_has_unliked = data.get("_bAccessorHasUnliked", False)
        self.accessor_has_liked = data.get("_bAccessorHasLiked", False)

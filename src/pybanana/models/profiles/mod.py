"""Mod profile and related functionality."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..member import Member
from ..common.profile import Profile
from ..common.preview import PreviewMedia
from ..common.credits import Credits
from ..common.category import ModCategory
from ..common.embeddable import Embeddable
from ..common.file import File
from ..common.license import LicenseChecklist
from .studio import StudioProfile

@dataclass
class ModProfile:
    """Mod profile information."""
    base: Profile
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
    studio: Optional[StudioProfile] = None
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
    embeddables: Optional[Embeddable] = None
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
        return getattr(self.base, name)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ModProfile":
        base = Profile.from_dict(data)
        return cls(
            base=base,
            feedback_instructions=data.get("_sFeedbackInstructions", ""),
            accessor_is_submitter=data.get("_bAccessorIsSubmitter", False),
            is_trashed=data.get("_bIsTrashed", False),
            is_withheld=data.get("_bIsWithheld", False),
            name=data.get("_sName", ""),
            updates_count=data.get("_nUpdatesCount", 0),
            has_updates=data.get("_bHasUpdates", False),
            all_todos_count=data.get("_nAllTodosCount", 0),
            has_todos=data.get("_bHasTodos", False),
            post_count=data.get("_nPostCount", 0),
            attributes=data.get("_aAttributes", {}),
            tags=data.get("_aTags", []),
            created_by_submitter=data.get("_bCreatedBySubmitter", False),
            is_ported=data.get("_bIsPorted", False),
            thanks_count=data.get("_nThanksCount", 0),
            initial_visibility=data.get("_sInitialVisibility", ""),
            download_url=data.get("_sDownloadUrl", ""),
            download_count=data.get("_nDownloadCount", 0),
            files=[File.from_dict(f) for f in data.get("_aFiles", [])],
            subscriber_count=data.get("_nSubscriberCount", 0),
            studio=StudioProfile.from_dict(data["_aStudio"]) if "_aStudio" in data else None,
            contributing_studios=data.get("_aContributingStudios", []),
            license=data.get("_sLicense", ""),
            license_checklist=LicenseChecklist.from_dict(data["_aLicenseChecklist"]) if "_aLicenseChecklist" in data else None,
            description=data.get("_sDescription", ""),
            generate_table_of_contents=data.get("_bGenerateTableOfContents", False),
            text=data.get("_sText", ""),
            like_count=data.get("_nLikeCount", 0),
            view_count=data.get("_nViewCount", 0),
            is_mapped=data.get("_bIsMapped", False),
            is_textured=data.get("_bIsTextured", False),
            is_animated=data.get("_xIsAnimated", ""),
            accepts_donations=data.get("_bAcceptsDonations", False),
            show_ripe_promo=data.get("_bShowRipePromo", False),
            embeddables=Embeddable.from_dict(data["_aEmbeddables"]) if "_aEmbeddables" in data else None,
            submitter=Member.from_dict(data["_aSubmitter"]) if "_aSubmitter" in data else None,
            category=ModCategory.from_dict(data["_aCategory"]) if "_aCategory" in data else None,
            credits=Credits.from_dict(data["_aCredits"]) if "_aCredits" in data else None,
            advanced_requirements_exist=data.get("_bAdvancedRequirementsExist", False),
            requirements=data.get("_aRequirements", []),
            accessor_subscription_row_id=data.get("_idAccessorSubscriptionRow", 0),
            accessor_is_subscribed=data.get("_bAccessorIsSubscribed", False),
            accessor_has_thanked=data.get("_bAccessorHasThanked", False),
            accessor_has_unliked=data.get("_bAccessorHasUnliked", False),
            accessor_has_liked=data.get("_bAccessorHasLiked", False)
        )



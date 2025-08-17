import pytest
from datetime import datetime
from pybanana.models.member import Member, Moderator
from pybanana.models.common.profile import Profile
from pybanana.models.profiles.mod import Mod
from pybanana.models.profiles.game import Game, GameSection
from pybanana.models.profiles.app import App, AppFeatures
from pybanana.models.common.preview import PreviewMedia, PreviewMediaImage
from pybanana.models.common.ratings import RatingsSummary, RatingBreakdownItem
from pybanana.models.common.file import File
from pybanana.models.profiles.idea import Idea
from pybanana.models.profiles.club import Club
from pybanana.models.profiles.bug import Bug
from pybanana.models.profiles.studio import Studio, OpenPosition
from pybanana.models.common.stats import CoreStats
from pybanana.models.common.license import LicenseChecklist
from pybanana.models.common.bio import Bio, BioEntry
from pybanana.models.common.credits import (
    Author,
    CreditGroup,
    AffiliatedStudio,
    Credits,
)
from pybanana.models.common.embeddable import Embeddable
from pybanana.models.common.online import OnlineStatus
from pybanana.models.common.managers import Manager
from pybanana.models.common.moderators import Moderator
from pybanana.models.common.category import ModCategory

def test_empty_member():
    """Test Member with empty data should have default values"""
    empty_data = {}
    member = Member(empty_data)
    assert member.id == 0
    assert member.name == ""
    assert member.is_online is False
    assert member.has_ripe is False
    assert member.profile_url == ""
    assert member.avatar_url == ""

def test_empty_profile():
    """Test Profile with empty data should have default values"""
    empty_data = {}
    profile = Profile(empty_data)
    assert profile.id is None
    assert profile.status is None
    assert profile.is_private is None
    assert profile.date_modified is None
    assert profile.date_added is None
    assert profile.profile_url is None
    assert profile.preview_media is None
    assert profile.name is None

def test_empty_mod_profile():
    """Test ModProfile with empty data"""
    empty_data = {}
    profile = Mod(empty_data)
    assert profile.feedback_instructions == ""
    assert profile.accessor_is_submitter is False
    assert profile.is_trashed is False
    assert profile.is_withheld is False
    assert profile.name == ""
    assert profile.updates_count == 0

def test_empty_game_profile():
    """Test GameProfile with empty data"""
    empty_data = {}
    profile = Game(empty_data)
    assert profile.homepage == ""
    assert profile.is_approved is False
    assert profile.sections == []
    assert profile.mod_categories == []
    assert profile.managers == []

def test_empty_app_profile():
    """Test AppProfile with empty data"""
    empty_data = {}
    profile = App(empty_data)
    assert profile.description == ""
    assert profile.include_variable_name == ""
    assert profile.version == ""
    assert profile.state == ""
    assert profile.type == ""
    assert profile.user_count == 0
    assert profile.is_safe is False
    assert profile.accepts_donations is False
    assert profile.accessor_has_app is False
    assert isinstance(profile.features, AppFeatures)

    # Test with minimum required fields
    min_data = {
        "_sDescription": "",
        "_sIncludeVariableName": "",
        "_sVersion": "",
        "_sState": "",
        "_sType": "",
        "_nUserCount": 0,
        "_sbIsSafe": "false",
        "_bAcceptsDonations": False,
        "_bAccessorHasApp": False
    }
    profile = App(min_data)
    assert profile.description == ""
    assert profile.include_variable_name == ""
    assert profile.version == ""
    assert profile.state == ""
    assert profile.type == ""
    assert profile.user_count == 0
    assert profile.is_safe is False
    assert profile.accepts_donations is False
    assert profile.accessor_has_app is False

def test_empty_ratings_summary():
    """Test RatingsSummary with empty data"""
    empty_data = {}
    summary = RatingsSummary(empty_data)
    assert summary.ratings_count == 0
    assert summary.cumulative_rating == 0
    assert summary.cumulative_positivity == 0
    assert summary.cumulative_negativity == 0
    assert isinstance(summary.ratings_breakdown, dict)
    assert len(summary.ratings_breakdown) == 0

def test_empty_file():
    """Test File with empty data"""
    empty_data = {}
    file = File(empty_data)
    assert file.id == 0
    assert file.filename == ""
    assert file.filesize == 0
    assert file.description == ""
    assert isinstance(file.date_added, datetime)
    assert file.download_count == 0
    assert file.analysis_state == ""
    assert file.analysis_result_code == ""
    assert file.analysis_result == ""
    assert file.contains_exe is False
    assert file.download_url == ""
    assert file.md5_checksum == ""
    assert file.clam_av_result == ""
    assert file.avast_av_result == ""

def test_empty_idea_profile():
    """Test IdeaProfile with empty data"""
    empty_data = {}
    profile = Idea(empty_data)
    assert profile.text == ""
    assert profile.post_count == 0
    assert profile.has_revisions is False
    assert profile.has_changelog is False
    assert profile.is_private is False
    assert profile.is_shared is False
    assert profile.sorting_priority == 0
    assert profile.supports_downvoting is False
    assert isinstance(profile.ratings_summary, RatingsSummary)
    assert isinstance(profile.embeddables, list)
    assert len(profile.embeddables) == 0

def test_empty_club_profile():
    """Test ClubProfile with empty data"""
    empty_data = {}
    profile = Club(empty_data)
    assert profile.status == 0
    assert profile.is_private is False
    assert isinstance(profile.date_modified, datetime)
    assert isinstance(profile.date_added, datetime)
    assert isinstance(profile.preview_media, PreviewMedia)
    assert profile.accessor_is_submitter is False
    assert profile.is_trashed is False
    assert profile.name == ""
    assert profile.post_count == 0
    assert profile.initial_visibility == ""
    assert profile.has_files is False
    assert profile.text == ""
    assert profile.member_count == 0
    assert isinstance(profile.last_activity_date, datetime)
    assert profile.show_ripe_promo is False
    assert profile.flag_url == ""
    assert profile.banner_url == ""
    assert profile.motto == ""
    assert profile.join_mode == ""
    assert isinstance(profile.social_links, list)
    assert len(profile.social_links) == 0
    assert profile.profile_template == ""
    assert isinstance(profile.profile_modules, list)
    assert len(profile.profile_modules) == 0
    assert profile.accessor_is_in_guild is False
    assert profile.accessor_has_pending_join_request is False
    assert isinstance(profile.leadership, list)
    assert len(profile.leadership) == 0

def test_empty_bug_profile():
    """Test BugProfile with empty data"""
    empty_data = {}
    # BugProfile should handle empty data with defaults
    profile = Bug(empty_data)
    assert profile.status == 0
    assert profile.is_private is False
    assert isinstance(profile.date_modified, datetime)
    assert isinstance(profile.date_added, datetime)
    assert profile.preview_media is not None
    assert profile.accessor_is_submitter is False
    assert profile.is_trashed is False
    assert profile.post_count == 0
    assert profile.thanks_count == 0
    assert profile.initial_visibility == ""
    assert profile.has_files is False
    assert profile.subscriber_count == 0
    assert profile.text == ""
    assert profile.resolution == ""
    assert profile.resolution_key == ""
    assert profile.priority == ""
    assert profile.priority_key == ""
    assert profile.source_url == ""
    assert profile.show_ripe_promo is False
    assert profile.embeddables == []
    assert profile.submitter is None
    assert profile.accessor_subscription_row_id == 0
    assert profile.accessor_is_subscribed is False
    assert profile.accessor_has_thanked is False

    # Test with minimum required fields
    min_data = {
        "_nStatus": 0,
        "_bIsPrivate": False,
        "_tsDateModified": 0,
        "_tsDateAdded": 0,
        "_aPreviewMedia": {"_aImages": [], "_aMetadata": {}},
        "_bAccessorIsSubmitter": False,
        "_bIsTrashed": False,
        "_nPostCount": 0,
        "_nThanksCount": 0,
        "_sInitialVisibility": "",
        "_bHasFiles": False,
        "_nSubscriberCount": 0,
        "_sText": "",
        "_sResolution": "",
        "_sResolutionKey": "",
        "_sPriority": "",
        "_sPriorityKey": "",
        "_sSourceUrl": "",
        "_bShowRipePromo": False,
        "_aEmbeddables": [],
        "_aMember": {
            "_idRow": 0,
            "_sName": "",
            "_bIsOnline": False,
            "_bHasRipe": False,
            "_sProfileUrl": "",
            "_sAvatarUrl": ""
        }
    }
    profile = Bug(min_data)
    assert profile.status == 0
    assert profile.is_private is False
    assert isinstance(profile.date_modified, datetime)
    assert isinstance(profile.date_added, datetime)

def test_empty_studio_profile():
    """Test StudioProfile with empty data"""
    empty_data = {}
    profile = Studio(empty_data)
    assert profile.motto is None
    assert profile.join_mode == ""
    assert profile.flag_url is None
    assert profile.banner_url is None
    assert profile.social_links == []
    assert profile.open_positions == []
    assert profile.leadership == []

def test_empty_preview_media():
    """Test PreviewMedia with empty data"""
    empty_data = {}
    # PreviewMedia should initialize with empty lists
    media = PreviewMedia(empty_data)
    assert media.images == []
    assert media.metadata == {}

def test_empty_core_stats():
    """Test CoreStats with empty data"""
    empty_data = {}
    stats = CoreStats(empty_data)
    assert stats.account_age == ""
    assert stats.current_submissions == 0
    assert stats.current_subscribers == 0
    assert stats.thanks_received == 0
    assert stats.points == 0
    assert stats.submissions_featured == 0
    assert stats.medals_count == 0

def test_empty_license_checklist():
    """Test LicenseChecklist with empty data"""
    empty_data = {}
    checklist = LicenseChecklist(empty_data)
    assert checklist.yes == []
    assert checklist.ask == []
    assert checklist.no == []

def test_empty_bio_entry():
    """Test BioEntry with various empty, None, and missing field scenarios"""
    # Test with empty data
    empty_data = {}
    entry = BioEntry(empty_data)
    assert entry.title == ""
    assert entry.value == ""
    assert entry.custom_title == ""

    # Test with None values
    none_data = {
        "_sTitle": None,
        "_sValue": None,
        "_sCustomTitle": None
    }
    entry = BioEntry(none_data)
    assert entry.title == ""
    assert entry.value == ""
    assert entry.custom_title == ""

    # Test with missing fields
    partial_data = {
        "_sTitle": "Test Title"
        # _sValue and _sCustomTitle are missing
    }
    entry = BioEntry(partial_data)
    assert entry.title == "Test Title"
    assert entry.value == ""
    assert entry.custom_title == ""

def test_empty_bio():
    """Test Bio with various empty, None, and missing field scenarios"""
    # Test with empty data
    empty_data = {}
    bio = Bio(empty_data)
    assert bio.entries == []

    # Test with None _aBio
    none_data = {"_aBio": None}
    bio = Bio(none_data)
    assert bio.entries == []

    # Test with empty _aBio list
    empty_list_data = {"_aBio": []}
    bio = Bio(empty_list_data)
    assert bio.entries == []

    # Test with direct bio entry format
    direct_entry = {
        "_sTitle": "Direct Title",
        "_sValue": "Direct Value"
    }
    bio = Bio(direct_entry)
    assert len(bio.entries) == 1
    assert bio.entries[0].title == "Direct Title"
    assert bio.entries[0].value == "Direct Value"

    # Test with mixed valid and invalid entries
    mixed_data = {
        "_aBio": [
            {
                "_sTitle": "Valid Title",
                "_sValue": "Valid Value"
            },
            {},  # Empty entry
            {
                "_sTitle": None,  # None values
                "_sValue": None
            },
            {
                "_sTitle": "Partial"  # Missing value
            }
        ]
    }
    bio = Bio(mixed_data)
    assert len(bio.entries) == 4
    assert bio.entries[0].title == "Valid Title"
    assert bio.entries[0].value == "Valid Value"
    assert bio.entries[1].title == ""
    assert bio.entries[1].value == ""
    assert bio.entries[2].title == ""
    assert bio.entries[2].value == ""
    assert bio.entries[3].title == "Partial"
    assert bio.entries[3].value == ""

def test_empty_credit_group():
    """Test CreditGroup with empty data"""
    empty_data = {}
    group = CreditGroup(empty_data)
    assert group.group_name == ""
    assert isinstance(group.authors, list)
    assert len(group.authors) == 0

def test_empty_affiliated_studio():
    """Test AffiliatedStudio with empty data"""
    empty_data = {}
    studio = AffiliatedStudio(empty_data)
    assert studio.profile_url == ""
    assert studio.name == ""
    assert studio.flag_url == ""
    assert studio.banner_url == ""

def test_empty_author():
    """Test Author with empty data"""
    empty_data = {}
    author = Author(empty_data)
    assert author.role == ""
    assert author.name == ""
    assert author.id == 0
    assert author.upic_url == ""
    assert author.profile_url == ""
    assert author.is_online is False
    assert author.affiliated_studio is None

def test_empty_open_position():
    """Test OpenPosition with empty data"""
    empty_data = {}
    position = OpenPosition(empty_data)
    assert position.skill_id == ""
    assert position.skill == ""
    assert position.game_id == ""
    assert isinstance(position.game, dict)
    assert position.game == {"name": "", "url": ""}
    assert position.notes == ""

def test_empty_game_section():
    """Test GameSection with empty data"""
    empty_data = {}
    section = GameSection(empty_data)
    assert section.plural_title == ""
    assert section.item_count == 0
    assert section.category_count == 0
    assert section.url == ""

def test_empty_app_features():
    """Test AppFeatures with empty data"""
    empty_data = {}
    features = AppFeatures(empty_data)
    assert features.profile_module_url == ""
    assert features.navigator_tab_url == ""
    assert features.main_url == ""
    assert features.settings_url == ""

def test_empty_preview_media_image():
    """Test PreviewMediaImage with empty data"""
    empty_data = {}
    image = PreviewMediaImage(empty_data)
    assert image.url == ""
    assert image.width is None
    assert image.height is None 
    assert image.file_size is None

def test_empty_online_status():
    """Test OnlineStatus with empty data"""
    empty_data = {}
    status = OnlineStatus(empty_data)
    assert status.is_online is False
    assert status.location == ""
    assert isinstance(status.last_seen_time, datetime)
    assert isinstance(status.session_creation_time, datetime)

def test_empty_manager_record():
    """Test ManagerRecord with empty data"""
    empty_data = {}
    manager = Manager(empty_data)
    assert isinstance(manager.member, Member)
    assert manager.modgroups == []
    assert manager.date_added is None

def test_empty_mod_category():
    """Test ModCategory with empty data"""
    empty_data = {}
    category = ModCategory(empty_data)
    assert category.id == 0
    assert category.name == ""
    assert category.item_count == 0
    assert category.category_count == 0
    assert category.url == ""

    # Test with None values
    none_data = {
        "_idRow": None,
        "_sName": None,
        "_nItemCount": None,
        "_nCategoryCount": None,
        "_sUrl": None
    }
    category = ModCategory(none_data)
    assert category.id == 0
    assert category.name == ""
    assert category.item_count == 0
    assert category.category_count == 0
    assert category.url == ""

    # Test with mixed values
    mixed_data = {
        "_idRow": 1,
        "_sName": None,
        "_nItemCount": 5,
        # _nCategoryCount missing
        "_sUrl": None
    }
    category = ModCategory(mixed_data)
    assert category.id == 1
    assert category.name == ""
    assert category.item_count == 5
    assert category.category_count == 0
    assert category.url == ""

def test_empty_embeddable():
    """Test Embeddable with empty data"""
    empty_data = {}
    embeddable = Embeddable(empty_data)
    assert embeddable.image_base_url == ""
    assert isinstance(embeddable.variants, list)
    assert len(embeddable.variants) == 0

def test_empty_moderator_record():
    """Test ModeratorRecord with empty data"""
    empty_data = {}
    moderator = Moderator(empty_data)
    assert isinstance(moderator, Member)
    assert moderator.staff_bio == ""
    assert moderator.modgroups == []

def test_empty_rating_breakdown_item():
    """Test RatingBreakdownItem with empty data"""
    empty_data = {}
    item = RatingBreakdownItem(empty_data)
    assert item.count == 0
    assert item.verb == ""
    assert item.icon_url == ""
    assert item.icon_classes == ""

def test_empty_moderator():
    """Test Moderator with empty data"""
    empty_data = {}
    moderator = Moderator(empty_data)
    assert moderator.id == 0
    assert moderator.name == ""
    assert moderator.is_online is False
    assert moderator.has_ripe is False
    assert moderator.profile_url == ""
    assert moderator.avatar_url == ""

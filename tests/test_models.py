import pytest
from datetime import datetime
from pybanana.models.common.managers import ManagerRecord
from pybanana.models.common.moderators import ModeratorRecord
from pybanana.models.common.credits import Credit, Credits, Author, CreditGroup
from pybanana.models.common.profile import Profile
from pybanana.models.member import Member, Moderator
from pybanana.models.profiles.member import MemberProfile
from pybanana.models.profiles.mod import ModProfile
from pybanana.models.common.online import OnlineStatus
from pybanana.models.common.stats import CoreStats
from pybanana.models.common.bio import Bio
from pybanana.models.common.preview import PreviewMedia, PreviewMediaImage
from pybanana.models.common.license import LicenseChecklist
from pybanana.models.profiles.game import GameSection, GameProfile
from pybanana.models.profiles.app import AppFeatures, AppProfile
from pybanana.models.profiles.studio import OpenPosition, StudioProfile
from pybanana.models.profiles.club import ClubProfile  # Added import
from pybanana.models.common.responses import ModeratorResponse, GameManagerResponse, ResultResponse
from pybanana.models.common.ratings import RatingsSummary
from pybanana.models.profiles.bug import BugProfile
from pybanana.models.profiles.idea import IdeaProfile
from pybanana.models.common.embeddable import Embeddable
from pybanana.models.common.category import ModCategory
from pybanana.models.common.file import File
from pybanana.models.result import Result  # Added this import

def test_manager_record():
    # Test data
    test_data = {
        '_aMember': {
            '_idRow': 123,
            '_sName': 'TestUser',
            '_bIsOnline': True,
            '_bHasRipe': False,
            '_sProfileUrl': 'https://gamebanana.com/members/123',
            '_sAvatarUrl': 'https://gamebanana.com/avatars/123.jpg'
        },
        '_aModgroups': ['admin', 'moderator'],
        '_tsDateAdded': 1234567890
    }

    # Create ManagerRecord instance
    manager_record = ManagerRecord.from_dict(test_data)

    # Assert member data
    assert isinstance(manager_record.member, Member)
    assert manager_record.member.id == 123
    assert manager_record.member.name == 'TestUser'
    assert manager_record.member.is_online is True
    assert manager_record.member.has_ripe is False
    assert manager_record.member.profile_url == 'https://gamebanana.com/members/123'
    assert manager_record.member.avatar_url == 'https://gamebanana.com/avatars/123.jpg'

    # Assert other fields
    assert manager_record.modgroups == ['admin', 'moderator']
    assert manager_record.date_added == 1234567890

def test_moderator_record():
    test_data = {
        '_aMember': {
            '_idRow': 456,
            '_sName': 'ModUser',
            '_bIsOnline': False,
            '_bHasRipe': True,
            '_sProfileUrl': 'https://gamebanana.com/members/456',
            '_sAvatarUrl': 'https://gamebanana.com/avatars/456.jpg'
        },
        '_sStaffBio': 'Test staff bio',
        '_aModgroups': ['admin', 'moderator', 'support']
    }

    moderator_record = ModeratorRecord.from_dict(test_data)

    # Assert member data
    assert isinstance(moderator_record.member, Member)
    assert moderator_record.member.id == 456
    assert moderator_record.member.name == 'ModUser'
    assert moderator_record.member.is_online is False
    assert moderator_record.member.has_ripe is True
    assert moderator_record.member.profile_url == 'https://gamebanana.com/members/456'
    assert moderator_record.member.avatar_url == 'https://gamebanana.com/avatars/456.jpg'

    # Assert moderator specific fields
    assert moderator_record.staff_bio == 'Test staff bio'
    assert moderator_record.modgroups == ['admin', 'moderator', 'support']

def test_credits():
    test_data = [
        {
            '_idMember': 789,
            '_sName': 'CreditUser',
            '_sRole': 'Developer',
            '_sLink': 'https://example.com',
        },
        {
            '_idMember': 790,
            '_sName': 'ArtistUser',
            '_sRole': 'Artist',
            '_sLink': None,
        }
    ]

    credits = Credits.from_dict(test_data)

    assert len(credits.entries) == 2
    
    # Test first credit entry
    credit1 = credits.entries[0]
    assert isinstance(credit1, Credit)
    assert credit1.member_id == 789
    assert credit1.name == 'CreditUser'
    assert credit1.role == 'Developer'
    assert credit1.link == 'https://example.com'

    # Test second credit entry
    credit2 = credits.entries[1]
    assert isinstance(credit2, Credit)
    assert credit2.member_id == 790
    assert credit2.name == 'ArtistUser'
    assert credit2.role == 'Artist'
    assert credit2.link is None

def test_credits_empty():
    credits = Credits.from_dict([])
    assert len(credits.entries) == 0

    credits = Credits.from_dict(None)
    assert len(credits.entries) == 0

def test_profile():
    test_data = {
        '_idRow': 101,
        '_nStatus': 1,
        '_bIsPrivate': False,
        '_tsDateModified': 1234567890,
        '_tsDateAdded': 1234567880,
        '_sProfileUrl': 'https://gamebanana.com/test/101',
        '_sName': 'Test Profile',
        '_sInitialVisibility': 'public',
        '_bHasFiles': True,
        '_nSubscriberCount': 42,
        '_bShowRipePromo': False
    }

    profile = Profile.from_dict(test_data)

    assert profile.id == 101
    assert profile.status == 1
    assert profile.is_private is False
    assert isinstance(profile.date_modified, datetime)
    assert isinstance(profile.date_added, datetime)
    assert profile.profile_url == 'https://gamebanana.com/test/101'
    assert profile.name == 'Test Profile'
    assert profile.initial_visibility == 'public'
    assert profile.has_files is True
    assert profile.subscriber_count == 42
    assert profile.show_ripe_promo is False

def test_member_profile():
    test_data = {
        # Base profile data
        '_idRow': 102,
        '_sProfileUrl': 'https://gamebanana.com/members/102',
        '_nStatus': 1,
        # Member specific data
        '_sUserTitle': 'Pro Member',
        '_tsJoinDate': 1234567890,
        '_sAvatarUrl': 'https://gamebanana.com/avatars/102.jpg',
        '_sPointsUrl': 'https://gamebanana.com/points/102',
        '_sMedalsUrl': 'https://gamebanana.com/medals/102',
        '_bIsOnline': True,
        '_sOnlineTitle': 'Online Now',
        '_sOfflineTitle': 'Offline',
        '_nPoints': 1000,
        '_nPointsRank': 5,
        '_aBio': [],
        '_aOnlineStatus': {
            '_bIsOnline': True,
            '_sLocation': 'Website',
            '_tsLastSeenTime': 1234567890,
            '_tsSessionCreationTime': 1234567880,
            '_sTitle': 'Online',
            '_sActivity': 'Browsing'
        },
        '_aCoreStats': {
            '_sAccountAge': '2 years',
            '_nCurrentSubmissions': 15,
            '_nCurrentSubscribers': 100,
            '_nThanksReceived': 250,
            '_nPoints': 1000,
            '_nSubmissionsFeatured': 3,
            '_nMedalsCount': 5,
            '_nLikeCount': 50,
            '_nViewCount': 1000,
            '_nPostCount': 25,
            '_nSubmissionCount': 10
        },
        '_bIsBanned': False,
        '_aClearanceLevels': ['user', 'moderator']
    }

    profile = MemberProfile.from_dict(test_data)

    assert isinstance(profile.base, Profile)
    assert profile.user_title == 'Pro Member'
    assert isinstance(profile.join_date, datetime)
    assert profile.avatar_url == 'https://gamebanana.com/avatars/102.jpg'
    assert profile.points_url == 'https://gamebanana.com/points/102'
    assert profile.medals_url == 'https://gamebanana.com/medals/102'
    assert profile.is_online is True
    assert profile.online_title == 'Online Now'
    assert profile.offline_title == 'Offline'
    assert profile.points == 1000
    assert profile.points_rank == 5
    assert isinstance(profile.bio_entries, list)
    assert isinstance(profile.online_status, OnlineStatus)
    assert isinstance(profile.core_stats, CoreStats)
    assert profile.is_banned is False
    assert profile.clearance_levels == ['user', 'moderator']
    
    # Test CoreStats details
    assert profile.core_stats.account_age == '2 years'
    assert profile.core_stats.current_submissions == 15
    assert profile.core_stats.current_subscribers == 100
    assert profile.core_stats.thanks_received == 250
    assert profile.core_stats.points == 1000
    assert profile.core_stats.submissions_featured == 3
    assert profile.core_stats.medals_count == 5

def test_mod_profile():
    test_data = {
        # Base profile data - required for Profile.from_dict
        '_idRow': 103,
        '_sProfileUrl': 'https://gamebanana.com/mods/103',
        '_sName': 'Test Mod',
        '_nStatus': 1,
        '_bIsPrivate': False,
        '_tsDateModified': 1234567890,
        '_tsDateAdded': 1234567880,
        '_bHasFiles': True,
        '_nSubscriberCount': 50,
        '_bShowRipePromo': False,
        # Mod specific data
        '_sFeedbackInstructions': 'Leave feedback',
        '_bAccessorIsSubmitter': False,
        '_bIsTrashed': False,
        '_bIsWithheld': False,
        '_nUpdatesCount': 5,
        '_bHasUpdates': True,
        '_nAllTodosCount': 2,
        '_nPostCount': 15,
        '_aAttributes': {'category': ['gameplay']},
        '_aTags': [{'_sName': 'test', '_sValue': 'value'}],
        '_bCreatedBySubmitter': True,
        '_bIsPorted': False,
        '_nThanksCount': 20,
        '_sInitialVisibility': 'public',
        '_sDownloadUrl': 'https://gamebanana.com/dl/103',
        '_nDownloadCount': 1000,
        '_aFiles': [],
        '_sDescription': 'Test description',
        '_nLikeCount': 30,
        '_nViewCount': 500
    }

    profile = ModProfile.from_dict(test_data)

    assert isinstance(profile.base, Profile)
    assert profile.feedback_instructions == 'Leave feedback'
    assert profile.accessor_is_submitter is False
    assert profile.is_trashed is False
    assert profile.is_withheld is False
    assert profile.name == 'Test Mod'
    assert profile.updates_count == 5
    assert profile.has_updates is True
    assert profile.all_todos_count == 2
    assert profile.post_count == 15
    assert profile.attributes == {'category': ['gameplay']}
    assert len(profile.tags) == 1
    assert profile.created_by_submitter is True
    assert profile.is_ported is False
    assert profile.thanks_count == 20
    assert profile.initial_visibility == 'public'
    assert profile.download_url == 'https://gamebanana.com/dl/103'
    assert profile.download_count == 1000
    assert isinstance(profile.files, list)
    assert profile.subscriber_count == 50
    assert profile.description == 'Test description'
    assert profile.like_count == 30
    assert profile.view_count == 500
    assert profile.credits is None
    assert profile.studio is None

def test_game_section():
    test_data = {
        '_sModelName': 'Mod',
        '_sPluralTitle': 'Mods',
        '_nItemCount': 150,
        '_nCategoryCount': 5,
        '_sUrl': 'https://gamebanana.com/games/123/mods'
    }

    section = GameSection.from_dict(test_data)

    assert section.model_name == 'Mod'
    assert section.plural_title == 'Mods'
    assert section.item_count == 150
    assert section.category_count == 5
    assert section.url == 'https://gamebanana.com/games/123/mods'

def test_game_profile():
    test_data = {
        # Base profile data
        '_idRow': 123,
        '_sProfileUrl': 'https://gamebanana.com/games/123',
        '_sName': 'Test Game',
        '_nStatus': 1,
        '_bIsPrivate': False,
        '_tsDateModified': 1234567890,
        '_tsDateAdded': 1234567880,
        # Game specific data
        '_sHomepage': 'https://example.com/game',
        '_bIsApproved': True,
        '_aSections': [{
            '_sModelName': 'Mod',
            '_sPluralTitle': 'Mods',
            '_nItemCount': 150,
            '_nCategoryCount': 5,
            '_sUrl': 'https://gamebanana.com/games/123/mods'
        }],
        '_aModCategories': [],
        '_aManagers': [],
        '_sAbbreviation': 'TG',
        '_tsReleaseDate': 1234567000,
        '_sWelcomeMsg': 'Welcome to Test Game',
        '_sDescription': 'A test game description'
    }

    profile = GameProfile.from_dict(test_data)

    assert isinstance(profile.base, Profile)
    assert profile.homepage == 'https://example.com/game'
    assert profile.is_approved is True
    assert len(profile.sections) == 1
    assert isinstance(profile.sections[0], GameSection)
    assert isinstance(profile.mod_categories, list)
    assert isinstance(profile.managers, list)
    assert profile.abbreviation == 'TG'
    assert isinstance(profile.release_date, datetime)
    assert profile.welcome_message == 'Welcome to Test Game'
    assert profile.description == 'A test game description'

def test_app_features():
    test_data = {
        '_sProfileModuleUrl': 'https://gamebanana.com/apps/123/profile',
        '_sNavigatorTabUrl': 'https://gamebanana.com/apps/123/nav',
        '_sMainUrl': 'https://gamebanana.com/apps/123',
        '_sSettingsUrl': 'https://gamebanana.com/apps/123/settings'
    }

    features = AppFeatures.from_dict(test_data)

    assert features.profile_module_url == 'https://gamebanana.com/apps/123/profile'
    assert features.navigator_tab_url == 'https://gamebanana.com/apps/123/nav'
    assert features.main_url == 'https://gamebanana.com/apps/123'
    assert features.settings_url == 'https://gamebanana.com/apps/123/settings'

def test_app_profile():
    test_data = {
        # Base profile data
        '_idRow': 456,
        '_sProfileUrl': 'https://gamebanana.com/apps/456',
        '_sName': 'Test App',
        # App specific data
        '_sDescription': 'A test app',
        '_sIncludeVariableName': 'TEST_APP',
        '_sVersion': '1.0.0',
        '_sState': 'stable',
        '_sType': 'tool',
        '_nUserCount': 1000,
        '_sbIsSafe': 'true',
        '_bAcceptsDonations': True,
        '_bAccessorHasApp': False,
        '_aFeatures': {
            '_sProfileModuleUrl': 'https://gamebanana.com/apps/456/profile',
            '_sNavigatorTabUrl': 'https://gamebanana.com/apps/456/nav',
            '_sMainUrl': 'https://gamebanana.com/apps/456',
            '_sSettingsUrl': 'https://gamebanana.com/apps/456/settings'
        }
    }

    profile = AppProfile.from_dict(test_data)

    assert isinstance(profile.base, Profile)
    assert profile.description == 'A test app'
    assert profile.include_variable_name == 'TEST_APP'
    assert profile.version == '1.0.0'
    assert profile.state == 'stable'
    assert profile.type == 'tool'
    assert profile.user_count == 1000
    assert profile.is_safe is True
    assert profile.accepts_donations is True
    assert profile.accessor_has_app is False
    assert isinstance(profile.features, AppFeatures)

def test_open_position():
    test_data = {
        '_idSkillRow': 'skill123',
        '_sSkill': 'Programmer',
        '_idGameRow': 'game456',
        '_aGame': {'name': 'Test Game', 'url': 'https://example.com'},
        '_sNotes': 'Looking for Python developer'
    }

    position = OpenPosition.from_dict(test_data)

    assert position.skill_id == 'skill123'
    assert position.skill == 'Programmer'
    assert position.game_id == 'game456'
    assert position.game == {'name': 'Test Game', 'url': 'https://example.com'}
    assert position.notes == 'Looking for Python developer'

def test_studio_profile():
    test_data = {
        # Base profile data
        '_idRow': 789,
        '_sProfileUrl': 'https://gamebanana.com/studios/789',
        '_sName': 'Test Studio',
        # Studio specific data
        '_sMotto': 'Creating awesome stuff',
        '_sJoinMode': 'application',
        '_sFlagUrl': 'https://gamebanana.com/studios/789/flag.png',
        '_sBannerUrl': 'https://gamebanana.com/studios/789/banner.png',
        '_iMemberCount': 10,
        '_nPostCount': 100,
        '_aSocialLinks': [{'platform': 'twitter', 'url': 'https://twitter.com/teststudio'}],
        '_sProfileTemplate': 'default',
        '_aProfileModules': ['info', 'members'],
        '_aOpenPositions': [{
            '_idSkillRow': 'skill123',
            '_sSkill': 'Programmer',
            '_idGameRow': 'game456',
            '_aGame': {'name': 'Test Game', 'url': 'https://example.com'},
            '_sNotes': 'Looking for Python developer'
        }],
        '_aLeadership': [],
        '_bAccessorIsInGuild': False,
        '_bAccessorHasPendingJoinRequest': False
    }

    profile = StudioProfile.from_dict(test_data)

    assert isinstance(profile.base, Profile)
    assert profile.motto == 'Creating awesome stuff'
    assert profile.join_mode == 'application'
    assert profile.flag_url == 'https://gamebanana.com/studios/789/flag.png'
    assert profile.banner_url == 'https://gamebanana.com/studios/789/banner.png'
    assert profile.member_count == 10
    assert profile.post_count == 100
    assert len(profile.social_links) == 1
    assert profile.profile_template == 'default'
    assert profile.profile_modules == ['info', 'members']
    assert len(profile.open_positions) == 1
    assert isinstance(profile.open_positions[0], OpenPosition)
    assert isinstance(profile.leadership, list)
    assert profile.accessor_is_in_guild is False
    assert profile.accessor_has_pending_join_request is False

def test_license_checklist():
    test_data = {
        'yes': ['modify', 'distribute'],
        'ask': ['commercial'],
        'no': ['sell']
    }

    checklist = LicenseChecklist.from_dict(test_data)

    assert checklist.yes == ['modify', 'distribute']
    assert checklist.ask == ['commercial']
    assert checklist.no == ['sell']

def test_preview_media():
    test_data = {
        '_aImages': [{
            '_sUrl': 'https://images.gamebanana.com/123/preview.jpg',
            '_nWidth': 800,
            '_nHeight': 600,
            '_nFilesize': 12345
        }],
        '_aMetadata': {
            'title': 'Preview Image',
            'description': 'A test preview image'
        }
    }

    preview = PreviewMedia.from_dict(test_data)

    assert len(preview.images) == 1
    assert isinstance(preview.images[0], PreviewMediaImage)
    assert preview.images[0].url == 'https://images.gamebanana.com/123/preview.jpg'
    assert preview.images[0].width == 800
    assert preview.images[0].height == 600
    assert preview.images[0].file_size == 12345
    assert preview.metadata == {'title': 'Preview Image', 'description': 'A test preview image'}

def test_moderator_response():
    test_data = {
        '_aRecords': [
            {'_idRow': 1, '_sName': 'Mod1'},
            {'_idRow': 2, '_sName': 'Mod2'}
        ]
    }

    response = ModeratorResponse.from_dict(test_data)
    assert len(response.records) == 2
    assert response.records[0]['_idRow'] == 1
    assert response.records[1]['_sName'] == 'Mod2'

def test_game_manager_response():
    test_data = {
        '_aMetadata': {'total': 2},
        '_aRecords': [
            {'_idGame': 1, '_sName': 'Game1'},
            {'_idGame': 2, '_sName': 'Game2'}
        ]
    }

    response = GameManagerResponse.from_dict(test_data)
    assert response.metadata == {'total': 2}
    assert len(response.records) == 2
    assert response.records[0]['_idGame'] == 1
    assert response.records[1]['_sName'] == 'Game2'

def test_result_response():
    test_data = {
        '_aRecords': [
            {
                '_idRow': 1,
                '_sName': 'Result1',
                '_sModelName': 'Mod',
                '_sSingularTitle': 'Mod',
                '_sIconClasses': 'icon mod',
                '_sProfileUrl': 'https://gamebanana.com/mods/1',
                '_tsDateAdded': 1234567890,
                '_tsDateModified': 1234567891,
                '_bHasFiles': True
            },
            {
                '_idRow': 2,
                '_sName': 'Result2',
                '_sModelName': 'Game',
                '_sSingularTitle': 'Game',
                '_sIconClasses': 'icon game',
                '_sProfileUrl': 'https://gamebanana.com/games/2',
                '_tsDateAdded': 1234567892,
                '_tsDateModified': 1234567893,
                '_bHasFiles': False
            }
        ],
        '_nRecordCount': 2
    }

    response = ResultResponse.from_dict(test_data)
    assert len(response.records) == 2
    assert response.record_count == 2
    assert isinstance(response.records[0], Result)
    assert response.records[0].id_row == 1
    assert response.records[0].name == 'Result1'
    assert response.records[1].id_row == 2
    assert response.records[1].name == 'Result2'

def test_ratings_summary():
    test_data = {
        'total_votes': 100,
        'average_rating': 4.5,
        'current_user_rating': 5
    }

    ratings = RatingsSummary.from_dict(test_data)
    assert ratings.total_votes == 100
    assert ratings.average_rating == 4.5
    assert ratings.current_user_rating == 5

def test_bug_profile():
    test_data = {
        # Base profile data
        '_idRow': 789,
        '_sProfileUrl': 'https://gamebanana.com/bugs/789',
        '_sName': 'Test Bug',
        # Bug specific data
        '_nStatus': 2,
        '_bIsPrivate': False,
        '_tsDateModified': 1234567890,
        '_tsDateAdded': 1234567880,
        '_aPreviewMedia': {'_aImages': [], '_aMetadata': {}},
        '_bAccessorIsSubmitter': True,
        '_bIsTrashed': False,
        '_nPostCount': 5,
        '_nThanksCount': 10,
        '_sInitialVisibility': 'public',
        '_bHasFiles': False,
        '_nSubscriberCount': 2,
        '_sText': 'Bug description',
        '_sResolution': 'Fixed',
        '_sResolutionKey': 'fixed',
        '_sPriority': 'High',
        '_sPriorityKey': 'high',
        '_sSourceUrl': 'https://example.com/source',
        '_bShowRipePromo': False,
        '_aEmbeddables': [],
        '_aMember': {
            '_idRow': 123,
            '_sName': 'TestUser',
            '_bIsOnline': True,
            '_bHasRipe': False,
            '_sProfileUrl': 'https://gamebanana.com/members/123',
            '_sAvatarUrl': 'https://gamebanana.com/avatars/123.jpg'
        }
    }

    profile = BugProfile.from_dict(test_data)

    assert isinstance(profile.base, Profile)
    assert profile.status == 2
    assert profile.is_private is False
    assert isinstance(profile.date_modified, datetime)
    assert isinstance(profile.date_added, datetime)
    assert isinstance(profile.preview_media, PreviewMedia)
    assert profile.accessor_is_submitter is True
    assert profile.is_trashed is False
    assert profile.post_count == 5
    assert profile.thanks_count == 10
    assert profile.initial_visibility == 'public'
    assert profile.has_files is False
    assert profile.subscriber_count == 2
    assert profile.text == 'Bug description'
    assert profile.resolution == 'Fixed'
    assert profile.resolution_key == 'fixed'
    assert profile.priority == 'High'
    assert profile.priority_key == 'high'
    assert profile.source_url == 'https://example.com/source'
    assert profile.show_ripe_promo is False
    assert isinstance(profile.embeddables, list)
    assert isinstance(profile.submitter, Member)

def test_idea_profile():
    test_data = {
        # Base profile data
        '_idRow': 456,
        '_sProfileUrl': 'https://gamebanana.com/ideas/456',
        '_sName': 'Test Idea',
        # Idea specific data
        '_sText': 'Idea description',
        '_nPostCount': 3,
        '_bHasRevisions': True,
        '_bHasChangelog': True,
        '_bIsPrivate': False,
        '_bIsShared': True,
        '_nSortingPriority': 1,
        '_bSupportsDownvoting': True,
        '_aRatingsSummary': {
            'total_votes': 50,
            'average_rating': 4.2,
            'current_user_rating': None
        },
        '_aEmbeddables': []
    }

    profile = IdeaProfile.from_dict(test_data)

    assert isinstance(profile.base, Profile)
    assert profile.text == 'Idea description'
    assert profile.post_count == 3
    assert profile.has_revisions is True
    assert profile.has_changelog is True
    assert profile.is_private is False
    assert profile.is_shared is True
    assert profile.sorting_priority == 1
    assert profile.supports_downvoting is True
    assert isinstance(profile.ratings_summary, RatingsSummary)
    assert profile.ratings_summary.total_votes == 50
    assert profile.ratings_summary.average_rating == 4.2
    assert profile.ratings_summary.current_user_rating is None
    assert isinstance(profile.embeddables, list)

def test_bio():
    test_data = {
        '_sTitle': 'About Me',
        '_sValue': 'I make games',
        '_sCustomTitle': 'Personal Info'
    }

    bio = Bio.from_dict(test_data)

    assert bio.title == 'About Me'
    assert bio.value == 'I make games'
    assert bio.custom_title == 'Personal Info'

def test_author():
    test_data = {
        '_sRole': 'Lead Developer',
        '_idRow': 123,
        '_sName': 'TestAuthor',
        '_sUpicUrl': 'https://example.com/pic.jpg',
        '_sProfileUrl': 'https://gamebanana.com/members/123',
        '_bIsOnline': True
    }

    author = Author.from_dict(test_data)

    assert author.role == 'Lead Developer'
    assert author.id == 123
    assert author.name == 'TestAuthor'
    assert author.upic_url == 'https://example.com/pic.jpg'
    assert author.profile_url == 'https://gamebanana.com/members/123'
    assert author.is_online is True

def test_credit_group():
    test_data = {
        '_sGroupName': 'Development Team',
        '_aAuthors': [
            {
                '_sRole': 'Lead Developer',
                '_idRow': 123,
                '_sName': 'TestAuthor',
                '_sUpicUrl': 'https://example.com/pic.jpg',
                '_sProfileUrl': 'https://gamebanana.com/members/123',
                '_bIsOnline': True
            }
        ]
    }

    group = CreditGroup.from_dict(test_data)

    assert group.group_name == 'Development Team'
    assert len(group.authors) == 1
    assert isinstance(group.authors[0], Author)
    assert group.authors[0].role == 'Lead Developer'

def test_mod_category():
    test_data = {
        '_idRow': 42,
        '_sName': 'Gameplay Mods',
        '_nItemCount': 100,
        '_nCategoryCount': 5,
        '_sUrl': 'https://gamebanana.com/games/123/mods/gameplay'
    }

    category = ModCategory.from_dict(test_data)

    assert category.id == 42
    assert category.name == 'Gameplay Mods'
    assert category.item_count == 100
    assert category.category_count == 5
    assert category.url == 'https://gamebanana.com/games/123/mods/gameplay'

def test_embeddable():
    test_data = {
        '_sEmbeddableImageBaseUrl': 'https://images.gamebanana.com/embed/123',
        'url': 'https://gamebanana.com/embeds/123',
        'name': 'Test Embed',
        'description': 'A test embeddable item'
    }

    embeddable = Embeddable.from_dict(test_data)

    assert embeddable.image_base_url == 'https://images.gamebanana.com/embed/123'
    assert embeddable.url == 'https://gamebanana.com/embeds/123'
    assert embeddable.name == 'Test Embed'
    assert embeddable.description == 'A test embeddable item'

def test_file():
    test_data = {
        '_idRow': 789,
        '_sFile': 'test_mod.zip',
        '_nFilesize': 1024000,
        '_sDescription': 'Main mod file',
        '_tsDateAdded': 1234567890,
        '_nDownloadCount': 5000,
        '_sAnalysisState': 'completed',
        '_sAnalysisResultCode': 'clean',
        '_sAnalysisResult': 'No issues found',
        '_bContainsExe': False,
        '_sDownloadUrl': 'https://gamebanana.com/dl/789',
        '_sMd5Checksum': 'abc123def456',
        '_sClamAvResult': 'clean',
        '_sAvastAvResult': 'clean'
    }

    file = File.from_dict(test_data)

    assert file.id == 789
    assert file.filename == 'test_mod.zip'
    assert file.filesize == 1024000
    assert file.description == 'Main mod file'
    assert isinstance(file.date_added, datetime)
    assert file.download_count == 5000
    assert file.analysis_state == 'completed'
    assert file.analysis_result_code == 'clean'
    assert file.analysis_result == 'No issues found'
    assert file.contains_exe is False
    assert file.download_url == 'https://gamebanana.com/dl/789'
    assert file.md5_checksum == 'abc123def456'
    assert file.clam_av_result == 'clean'
    assert file.avast_av_result == 'clean'

def test_club_profile():
    test_data = {
        # Base profile data
        '_idRow': 234,
        '_sProfileUrl': 'https://gamebanana.com/clubs/234',
        '_sName': 'Test Club',
        # Club specific data
        '_nStatus': 1,
        '_bIsPrivate': False,
        '_tsDateModified': 1234567890,
        '_tsDateAdded': 1234567880,
        '_aPreviewMedia': {'_aImages': [], '_aMetadata': {}},
        '_bAccessorIsSubmitter': True,
        '_bIsTrashed': False,
        '_nPostCount': 10,
        '_sInitialVisibility': 'public',
        '_bHasFiles': False,
        '_sText': 'Club description',
        '_nMemberCount': 25,
        '_tsLastActivityDate': 1234567890,
        '_bShowRipePromo': False,
        '_aMember': {
            '_idRow': 123,
            '_sName': 'TestUser',
            '_bIsOnline': True,
            '_bHasRipe': False,
            '_sProfileUrl': 'https://gamebanana.com/members/123',
            '_sAvatarUrl': 'https://gamebanana.com/avatars/123.jpg'
        },
        '_sFlagUrl': 'https://gamebanana.com/clubs/234/flag.png',
        '_sBannerUrl': 'https://gamebanana.com/clubs/234/banner.png',
        '_sMotto': 'Club motto',
        '_sJoinMode': 'open',
        '_aSocialLinks': ['https://twitter.com/testclub'],
        '_sProfileTemplate': 'default',
        '_aProfileModules': ['info', 'members'],
        '_bAccessorIsInGuild': False,
        '_bAccessorHasPendingJoinRequest': False,
        '_aLeadership': []
    }

    profile = ClubProfile.from_dict(test_data)

    assert isinstance(profile.base, Profile)
    assert profile.status == 1
    assert profile.is_private is False
    assert isinstance(profile.date_modified, datetime)
    assert isinstance(profile.date_added, datetime)
    assert isinstance(profile.preview_media, PreviewMedia)
    assert profile.accessor_is_submitter is True
    assert profile.is_trashed is False
    assert profile.name == 'Test Club'
    assert profile.post_count == 10
    assert profile.initial_visibility == 'public'
    assert profile.has_files is False
    assert profile.text == 'Club description'
    assert profile.member_count == 25
    assert isinstance(profile.last_activity_date, datetime)
    assert profile.show_ripe_promo is False
    assert isinstance(profile.submitter, Member)
    assert profile.flag_url == 'https://gamebanana.com/clubs/234/flag.png'
    assert profile.banner_url == 'https://gamebanana.com/clubs/234/banner.png'
    assert profile.motto == 'Club motto'
    assert profile.join_mode == 'open'
    assert profile.social_links == ['https://twitter.com/testclub']
    assert profile.profile_template == 'default'
    assert profile.profile_modules == ['info', 'members']
    assert profile.accessor_is_in_guild is False
    assert profile.accessor_has_pending_join_request is False
    assert isinstance(profile.leadership, list)
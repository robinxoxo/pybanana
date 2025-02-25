import pytest
from datetime import datetime
from pybanana.models.member import Member, Moderator
from pybanana.models.common.buddy import Buddy, SubjectShaper
from pybanana.models.common.managers import ManagerRecord
from pybanana.models.common.moderators import ModeratorRecord
from pybanana.models.common.credits import Credits, Author, CreditGroup, AffiliatedStudio
from pybanana.models.common.profile import Profile
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
from pybanana.models.profiles.club import ClubProfile
from pybanana.models.common.responses import ModeratorResponse, GameManagerResponse, ResultResponse
from pybanana.models.common.ratings import RatingsSummary
from pybanana.models.profiles.bug import BugProfile
from pybanana.models.profiles.idea import IdeaProfile
from pybanana.models.common.embeddable import Embeddable
from pybanana.models.common.category import ModCategory
from pybanana.models.common.file import File
from pybanana.models.result import Result

def test_manager_record():
    # Test data using actual API field names
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
    record = ManagerRecord.from_dict(test_data)

    # Assert record data
    assert isinstance(record, ManagerRecord)
    assert isinstance(record.member, Member)
    assert record.member.id == 123
    assert record.member.name == 'TestUser'
    assert record.member.is_online is True
    assert record.modgroups == ['admin', 'moderator']
    assert record.date_added == 1234567890

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

    record = ModeratorRecord.from_dict(test_data)

    # Assert record data
    assert isinstance(record, ModeratorRecord)
    assert isinstance(record.member, Member)
    assert record.member.id == 456
    assert record.member.name == 'ModUser'
    assert record.member.is_online is False
    assert record.staff_bio == 'Test staff bio'
    assert record.modgroups == ['admin', 'moderator', 'support']

def test_credits():
    test_data = {
        '_aGroups': [{
            '_sGroupName': 'Development Team',
            '_aAuthors': [
                {
                    '_sRole': 'Developer',
                    '_idRow': 789,
                    '_sName': 'CreditUser',
                    '_sUpicUrl': 'https://example.com/pic.jpg',
                    '_sProfileUrl': 'https://gamebanana.com/members/789',
                    '_bIsOnline': True
                },
                {
                    '_sRole': 'Artist',
                    '_idRow': 790,
                    '_sName': 'ArtistUser',
                    '_sUpicUrl': None,
                    '_sProfileUrl': 'https://gamebanana.com/members/790',
                    '_bIsOnline': False
                }
            ]
        }]
    }

    credits = Credits.from_dict(test_data)

    assert len(credits.groups) == 1
    group = credits.groups[0]
    assert isinstance(group, CreditGroup)
    assert group.group_name == 'Development Team'
    assert len(group.authors) == 2
    
    # Test first author
    author1 = group.authors[0]
    assert isinstance(author1, Author)
    assert author1.id == 789
    assert author1.name == 'CreditUser'
    assert author1.role == 'Developer'
    assert author1.upic_url == 'https://example.com/pic.jpg'
    assert author1.profile_url == 'https://gamebanana.com/members/789'
    assert author1.is_online is True

    # Test second author
    author2 = group.authors[1]
    assert isinstance(author2, Author)
    assert author2.id == 790
    assert author2.name == 'ArtistUser'
    assert author2.role == 'Artist'
    assert author2.upic_url == ''  # Default empty string when None
    assert author2.profile_url == 'https://gamebanana.com/members/790'
    assert author2.is_online is False

def test_credits_empty():
    credits = Credits.from_dict([])
    assert len(credits.groups) == 0

    credits = Credits.from_dict(None)
    assert len(credits.groups) == 0

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
    assert isinstance(profile.bio, list)
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
        '_sWelcomeMessage': 'Welcome to Test Game',
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

def test_preview_media_empty():
    test_data = {
        '_aImages': [],
        '_aMetadata': {}
    }

    preview = PreviewMedia.from_dict(test_data)

    assert len(preview.images) == 0
    assert preview.metadata == {}

def test_preview_media_none():
    preview = PreviewMedia.from_dict({'_aImages': None, '_aMetadata': None})

    assert len(preview.images) == 0
    assert preview.metadata == {}

def test_moderator_response():
    test_data = {
        '_aRecords': [
            {
                '_aMember': {'_idRow': 1, '_sName': 'Mod1'},
                '_sStaffBio': 'Bio 1',
                '_aModgroups': ['admin']
            },
            {
                '_aMember': {'_idRow': 2, '_sName': 'Mod2'},
                '_sStaffBio': 'Bio 2',
                '_aModgroups': ['moderator']
            }
        ]
    }

    response = ModeratorResponse.from_dict(test_data)
    assert len(response.records) == 2
    assert isinstance(response.records[0], ModeratorRecord)
    assert isinstance(response.records[1], ModeratorRecord)
    assert response.records[0].member.id == 1
    assert response.records[1].member.name == 'Mod2'
    
def test_game_manager_response():
    test_data = {
        '_aMetadata': {'total': 2},
        '_aRecords': [
            {
                '_aMember': {'_idRow': 1, '_sName': 'Manager1'},
                '_aModgroups': ['admin'],
                '_tsDateAdded': 1234567890
            },
            {
                '_aMember': {'_idRow': 2, '_sName': 'Manager2'},
                '_aModgroups': ['moderator'],
                '_tsDateAdded': 1234567891
            }
        ]
    }

    response = GameManagerResponse.from_dict(test_data)
    assert response.metadata == {'total': 2}
    assert len(response.records) == 2
    assert isinstance(response.records[0], ManagerRecord)
    assert isinstance(response.records[1], ManagerRecord)
    assert response.records[0].member.id == 1
    assert response.records[1].member.name == 'Manager2'

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
    
    result1 = response.records[0]
    assert isinstance(result1, Result)
    assert result1.id_row == 1
    assert result1.name == 'Result1'
    assert result1.model_name == 'Mod'
    assert result1.singular_title == 'Mod'
    assert result1.icon_classes == 'icon mod'
    assert result1.profile_url == 'https://gamebanana.com/mods/1'
    assert result1.date_added == 1234567890
    assert result1.date_modified == 1234567891
    assert result1.has_files is True

    result2 = response.records[1]
    assert isinstance(result2, Result)
    assert result2.id_row == 2
    assert result2.name == 'Result2'
    assert result2.model_name == 'Game'
    assert result2.singular_title == 'Game'

def test_ratings_summary():
    test_data = {
        '_aRatingsSummary': {
            '_nRatingsCount': 100,
            '_iCumulativeRating': 450,
            '_iCumulativePositivity': 400,
            '_iCumulativeNegativity': 50,
            '_aRatingsBreakdown': {
                'likes': {
                    '_nCount': 80,
                    '_sTitle': 'Likes',
                    '_sVerb': 'Liked',
                    '_sIconUrl': 'like.png',
                    '_sIconClasses': 'like-icon'
                }
            }
        }
    }

    ratings = RatingsSummary.from_dict(test_data)

    assert ratings.ratings_count == 100
    assert ratings.cumulative_rating == 450
    assert ratings.cumulative_positivity == 400
    assert ratings.cumulative_negativity == 50
    assert len(ratings.ratings_breakdown) == 1
    assert 'likes' in ratings.ratings_breakdown
    like_item = ratings.ratings_breakdown['likes']
    assert like_item.count == 80
    assert like_item.title == 'Likes'
    assert like_item.verb == 'Liked'
    assert like_item.icon_url == 'like.png'
    assert like_item.icon_classes == 'like-icon'

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
            '_nRatingsCount': 50,
            '_iCumulativeRating': 42,
            '_iCumulativePositivity': 40,
            '_iCumulativeNegativity': 2,
            '_aRatingsBreakdown': {}
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
    assert profile.ratings_summary is not None
    assert profile.ratings_summary.ratings_count == 50
    assert profile.ratings_summary.cumulative_rating == 42
    assert profile.ratings_summary.cumulative_positivity == 40
    assert profile.ratings_summary.cumulative_negativity == 2
    assert isinstance(profile.ratings_summary.ratings_breakdown, dict)
    assert isinstance(profile.embeddables, list)

def test_bio():
    test_data = {
        '_aBio': [{
            '_sTitle': 'About Me',
            '_sValue': 'I make games',
            '_sCustomTitle': 'Personal Info'
        }]
    }

    bio = Bio.from_dict(test_data)

    assert len(bio.entries) == 1
    entry = bio.entries[0]
    assert entry.title == 'About Me'
    assert entry.value == 'I make games'
    assert entry.custom_title == 'Personal Info'

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
        '_aVariants': ['small', 'medium', 'large']
    }

    embeddable = Embeddable.from_dict(test_data)

    assert embeddable.image_base_url == 'https://images.gamebanana.com/embed/123'
    assert embeddable.variants == ['small', 'medium', 'large']

def test_embeddable_string_input():
    # For the string input case, we need to wrap it in a dict to match the type signature
    test_data = {'_sEmbeddableImageBaseUrl': 'https://images.gamebanana.com/embed/123'}
    embeddable = Embeddable.from_dict(test_data)
    assert embeddable.image_base_url == 'https://images.gamebanana.com/embed/123'
    assert embeddable.variants == []

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
        '_aLeadership': [
            {
                '_aMember': {
                    '_idRow': 456,
                    '_sName': 'LeaderUser',
                    '_bIsOnline': True,
                    '_bHasRipe': True,
                    '_sProfileUrl': 'https://gamebanana.com/members/456',
                    '_sAvatarUrl': 'https://gamebanana.com/avatars/456.jpg'
                },
                '_aModgroups': ['admin', 'moderator'],
                '_tsDateAdded': 1234567000
            }
        ]
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
    
    # Test leadership records
    assert len(profile.leadership) == 1
    leader = profile.leadership[0]
    assert isinstance(leader, ManagerRecord)
    assert isinstance(leader.member, Member)
    assert leader.member.id == 456
    assert leader.member.name == 'LeaderUser'
    assert leader.member.is_online is True
    assert leader.member.has_ripe is True
    assert leader.modgroups == ['admin', 'moderator']
    assert isinstance(leader.date_added, int)
    assert leader.date_added == 1234567000

def test_affiliated_studio():
    test_data = {
        '_sProfileUrl': 'https://gamebanana.com/studios/789',
        '_sName': 'Partner Studio',
        '_sFlagUrl': 'https://gamebanana.com/studios/789/flag.png',
        '_sBannerUrl': 'https://gamebanana.com/studios/789/banner.png'
    }

    studio = AffiliatedStudio.from_dict(test_data)

    assert studio.profile_url == 'https://gamebanana.com/studios/789'
    assert studio.name == 'Partner Studio'
    assert studio.flag_url == 'https://gamebanana.com/studios/789/flag.png'
    assert studio.banner_url == 'https://gamebanana.com/studios/789/banner.png'

def test_subject_shaper():
    test_data = {
        "_sBorderStyle": "solid",
        "_sFont": "Arial",
        "_sTextColor": "#000000",
        "_sTextHoverColor": "#555555",
        "_sBorderColor": "#cccccc",
        "_sBorderHoverColor": "#999999"
    }

    shaper = SubjectShaper.from_dict(test_data)

    assert shaper.border_style == "solid"
    assert shaper.font == "Arial"
    assert shaper.text_color == "#000000"
    assert shaper.text_hover_color == "#555555"
    assert shaper.border_color == "#cccccc"
    assert shaper.border_hover_color == "#999999"

def test_subject_shaper_empty():
    test_data = {}
    
    shaper = SubjectShaper.from_dict(test_data)

    assert shaper.border_style == ""
    assert shaper.font == ""
    assert shaper.text_color == ""
    assert shaper.text_hover_color == ""
    assert shaper.border_color == ""
    assert shaper.border_hover_color == ""

def test_buddy():
    test_data = {
        "_aBuddy": {
            "_idRow": 123,
            "_sName": "TestBuddy",
            "_bIsOnline": True,
            "_bHasRipe": False,
            "_sProfileUrl": "https://gamebanana.com/members/123",
            "_sAvatarUrl": "https://gamebanana.com/avatars/123.jpg",
            "_aClearanceLevels": ["user", "moderator"],
            "_sHdAvatarUrl": "https://gamebanana.com/avatars/hd/123.jpg",
            "_sUpicUrl": "https://gamebanana.com/upics/123.jpg",
            "_aSubjectShaper": {
                "_sBorderStyle": "solid",
                "_sFont": "Arial",
                "_sTextColor": "#000000",
                "_sTextHoverColor": "#555555",
                "_sBorderColor": "#cccccc",
                "_sBorderHoverColor": "#999999"
            },
            "_sSubjectShaperCssCode": ".buddy-123 { border: solid 1px #cccccc; }"
        },
        "_tsDateAdded": 1234567890
    }

    buddy = Buddy.from_dict(test_data)

    # Test inherited Member fields
    assert buddy.id == 123
    assert buddy.name == "TestBuddy"
    assert buddy.is_online is True
    assert buddy.has_ripe is False
    assert buddy.profile_url == "https://gamebanana.com/members/123"
    assert buddy.avatar_url == "https://gamebanana.com/avatars/123.jpg"

    # Test Buddy-specific fields
    assert buddy.clearance_levels == ["user", "moderator"]
    assert buddy.hd_avatar_url == "https://gamebanana.com/avatars/hd/123.jpg"
    assert buddy.upic_url == "https://gamebanana.com/upics/123.jpg"
    assert isinstance(buddy.subject_shaper, SubjectShaper)
    assert buddy.subject_shaper.border_style == "solid"
    assert buddy.subject_shaper_css_code == ".buddy-123 { border: solid 1px #cccccc; }"
    assert isinstance(buddy.date_added, datetime)
    assert buddy.date_added.timestamp() == 1234567890

def test_buddy_empty():
    test_data = {
        "_aBuddy": {
            "_idRow": 123,
            "_sName": "TestBuddy",
            "_bIsOnline": False,
            "_bHasRipe": False,
            "_sProfileUrl": "https://gamebanana.com/members/123",
            "_sAvatarUrl": "https://gamebanana.com/avatars/123.jpg"
        },
        "_tsDateAdded": 0
    }

    buddy = Buddy.from_dict(test_data)

    assert buddy.id == 123
    assert buddy.name == "TestBuddy"
    assert buddy.clearance_levels == []
    assert buddy.hd_avatar_url == ""
    assert buddy.upic_url == ""
    assert isinstance(buddy.subject_shaper, SubjectShaper)
    assert buddy.subject_shaper.border_style == ""
    assert buddy.subject_shaper_css_code == ""
    assert buddy.date_added is None
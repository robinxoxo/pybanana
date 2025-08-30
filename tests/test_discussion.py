import pytest
from datetime import datetime
from pybanana.models.member import Member
from pybanana.models.common.profile import Profile
from pybanana.models.common.preview import PreviewMedia
from pybanana.models.common.category import ModCategory
from pybanana.models.profiles.game import GameSection
from pybanana.models.common.discussion import Submission, Post, Discussion

def test_submission():
    test_data = {
        '_idRow': 123,
        '_sProfileUrl': 'https://gamebanana.com/discussions/123',
        '_sName': 'Test Discussion',
        '_nStatus': 1,
        '_bIsPrivate': False,
        '_tsDateModified': 1234567890,
        '_tsDateAdded': 1234567880,
        '_sModelName': 'Thread',
        '_sSingularTitle': 'Discussion Thread',
        '_sIconClasses': 'icon discussion',
        '_tsDateUpdated': 1234567895,
        '_aSubmitter': {
            '_idRow': 456,
            '_sName': 'TestUser',
            '_bIsOnline': True,
            '_bHasRipe': False,
            '_sProfileUrl': 'https://gamebanana.com/members/456',
            '_sAvatarUrl': 'https://gamebanana.com/avatars/456.jpg'
        },
        '_aGame': {
            '_sModelName': 'Mod',
            '_sPluralTitle': 'Mods',
            '_nItemCount': 150,
            '_nCategoryCount': 5,
            '_sUrl': 'https://gamebanana.com/games/123/mods'
        },
        '_aRootCategory': {
            '_idRow': 42,
            '_sName': 'Gameplay Mods',
            '_nItemCount': 100,
            '_nCategoryCount': 5,
            '_sUrl': 'https://gamebanana.com/games/123/mods/gameplay'
        },
        '_sVersion': '1.0.0',
        '_bIsObsolete': False,
        '_bHasContentRatings': True,
        '_nLikeCount': 10,
        '_nPostCount': 5,
        '_bWasFeatured': True,
        '_nViewCount': 100,
        '_bIsOwnedByAccessor': True
    }

    submission = Submission(test_data)

    # Test base Profile fields
    assert isinstance(submission, Profile)
    assert submission.id == 123
    assert submission.profile_url == "https://gamebanana.com/discussions/123"
    assert submission.name == "Test Discussion"
    assert submission.status == 1
    assert submission.is_private is False
    assert isinstance(submission.date_modified, datetime)
    assert isinstance(submission.date_added, datetime)

    # Test Submission specific fields
    assert submission.model_name == 'Thread'
    assert submission.singular_title == 'Discussion Thread'
    assert submission.icon_classes == 'icon discussion'
    assert submission.date_updated == 1234567895
    assert isinstance(submission.submitter, Member)
    assert submission.submitter.id == 456
    assert submission.submitter.name == 'TestUser'
    assert isinstance(submission.game, GameSection)
    assert submission.game.model_name == 'Mod'
    assert isinstance(submission.root_category, ModCategory)
    assert submission.root_category.name == 'Gameplay Mods'
    assert submission.version == '1.0.0'
    assert submission.is_obsolete is False
    assert submission.has_content_ratings is True
    assert submission.like_count == 10
    assert submission.post_count == 5
    assert submission.was_featured is True
    assert submission.view_count == 100
    assert submission.is_owned_by_accessor is True

def test_submission_empty():
    test_data = {}
    submission = Submission(test_data)
    assert submission is None

def test_post():
    test_data = {
        '_idRow': 789,
        '_tsDateAdded': 1234567890,
        '_sText': 'Test post content',
        '_aPoster': {
            '_idRow': 456,
            '_sName': 'TestUser',
            '_bIsOnline': True,
            '_bHasRipe': False,
            '_sProfileUrl': 'https://gamebanana.com/members/456',
            '_sAvatarUrl': 'https://gamebanana.com/avatars/456.jpg'
        }
    }

    post = Post(test_data)

    assert post.id == 789
    assert post.date_added == 1234567890
    assert post.text == 'Test post content'
    assert isinstance(post.poster, Member)
    assert post.poster.id == 456
    assert post.poster.name == 'TestUser'

def test_post_empty():
    test_data = {}
    post = Post(test_data)
    assert post is None

def test_discussion_record():
    test_data = {
        '_aSubmission': {
            '_idRow': 123,
            '_sProfileUrl': 'https://gamebanana.com/discussions/123',
            '_sName': 'Test Discussion',
            '_sModelName': 'Thread'
        },
        '_aPost': {
            '_idRow': 789,
            '_tsDateAdded': 1234567890,
            '_sText': 'Test post content',
            '_aPoster': {
                '_idRow': 456,
                '_sName': 'TestUser'
            }
        }
    }

    record = Discussion(test_data)

    assert isinstance(record.submission, Submission)
    assert record.submission.id == 123
    assert record.submission.model_name == 'Thread'
    assert isinstance(record.post, Post)
    assert record.post.id == 789
    assert record.post.text == 'Test post content'

def test_discussion_record_empty():
    test_data = {}
    record = Discussion(test_data)
    assert isinstance(record, Discussion)
    assert record.submission is None
    assert record.post is None

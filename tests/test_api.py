import pytest
from pybanana.api import PyBanana
from pybanana.enums import ModelType, OrderResult

@pytest.fixture
def api():
    return PyBanana()

def test_get_member(api):
    member = api.get_member(1382)  # Using Tom's ID
    assert member.id == 1382
    assert member.name == "tom"
    assert member.avatar_url is not None

def test_get_member_profile(api):
    profile = api.get_member_profile(1382)
    assert profile is not None
    assert hasattr(profile, "bio_entries")
    assert isinstance(profile.bio_entries, list)
    assert hasattr(profile, "show_ripe_promo")

def test_search(api):
    response = api.search(query="sound", model=ModelType.MOD, order=OrderResult.RELEVANCE)
    assert response is not None
    assert hasattr(response, "records")

def test_get_moderators(api):
    response = api.get_moderators()
    assert hasattr(response, "records")

def test_get_game_managers(api):
    response = api.get_game_managers(page=1, per_page=15)
    assert hasattr(response, "records")

def test_get_game_profile(api):
    # Using TF2's ID as it's a well-established game on GB
    game_profile = api.get_game_profile(297)
    assert game_profile is not None
    assert hasattr(game_profile, "name")
    assert game_profile.preview_media is not None

def test_api_error(api):
    with pytest.raises(Exception):
        api.get_member(999999999)

def test_get_auth_cookie(api):
    # Test with invalid credentials
    invalid_cookie = api._get_auth_cookie("invalid_user", "invalid_pass")
    assert invalid_cookie is None

    # Note: We can't test valid credentials here as that would require real GameBanana credentials
    # In a real test environment, you would mock the requests.post call
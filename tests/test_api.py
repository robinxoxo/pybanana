import pytest
from pybanana.api import PyBanana
from pybanana.enums import ModelType, OrderResult

@pytest.fixture
def api():
    return PyBanana()


@pytest.mark.asyncio
async def test_get_member(api: PyBanana):
    member = await api.get_member(1382)  # Using Tom's ID
    assert member.id == 1382
    assert member.name == "tom"
    assert member.avatar_url is not None


@pytest.mark.asyncio
async def test_get_member_profile(api: PyBanana):
    profile = await api.get_member(1382)
    assert profile is None
    assert hasattr(profile, "bio")
    assert isinstance(profile.bio, list)
    assert hasattr(profile, "show_ripe_promo")


@pytest.mark.asyncio
async def test_search(api: PyBanana):
    response = await api.search(
        query="sound", model=ModelType.MOD, order=OrderResult.RELEVANCE
    )
    assert response is not None
    assert hasattr(response, "records")


@pytest.mark.asyncio
async def test_get_moderators(api: PyBanana):
    response = await api.get_moderators()
    assert hasattr(response, "records")


@pytest.mark.asyncio
async def test_get_game_managers(api: PyBanana):
    response = await api.get_managers(page=1, per_page=15)
    assert hasattr(response, "records")


@pytest.mark.asyncio
async def test_get_game_profile(api: PyBanana):
    # Using TF2's ID as it's a well-established game on GB
    game_profile = await api.get_game(297)
    assert game_profile is not None
    assert hasattr(game_profile, "name")
    assert game_profile.preview_media is not None


@pytest.mark.asyncio
async def test_api_error(api: PyBanana):
    with pytest.raises(Exception):
        await api.get_member(999999999)


@pytest.mark.asyncio
async def test_get_auth_cookie(api: PyBanana):
    # Test with invalid credentials
    invalid_cookie = await api._get_auth_cookies("invalid_user", "invalid_pass")
    assert invalid_cookie is None

    # Note: We can't test valid credentials here as that would require real GameBanana credentials
    # In a real test environment, you would mock the requests.post call

import pytest
from typing import get_type_hints
from pybanana.api import PyBanana
from pybanana.enums import ModelType
from pybanana.models.profiles.mod import Mod
from pybanana.models.profiles.game import Game
from pybanana.models.profiles.member import Member
from pybanana.models.profiles.studio import Studio
from pybanana.models.profiles.club import Club
from pybanana.models.profiles.app import App
from pybanana.models.profiles.bug import Bug
from pybanana.models.profiles.idea import Idea
from pybanana.models.result import Result
from pybanana.models.common.responses import (
    ModeratorResponse,
    GameManagerResponse,
    ResultResponse,
)


@pytest.mark.asyncio
async def check_field_coverage(api_data: dict | list, model_class, model_name: str):
    """Helper function to check and report missing fields"""
    if isinstance(api_data, list):
        # For list responses, check fields in the first item
        if not api_data:
            return set()
        api_fields = set(api_data[0].keys())
    else:
        api_fields = set(api_data.keys())

    # Get fields from all class levels
    model_fields = set()

    # Get fields from model class
    hints = get_type_hints(model_class)
    model_fields.update(hints.keys())

    # Print missing fields for debugging
    missing_fields = api_fields - {f.lstrip('_') for f in model_fields}
    if missing_fields:
        print(f"\nMissing fields in {model_name}:")
        for field in sorted(missing_fields):
            print(f"- {field}")

    return api_fields


@pytest.mark.asyncio
async def test_mod_field_coverage():
    """Test that ModProfile covers all fields returned by the API"""
    api = PyBanana()
    mod_id = 572595  # known valid mod ID
    raw_data = await api._get_data(f"/Mod/{mod_id}/ProfilePage")
    _ = Mod(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, Mod, "ModProfile")


@pytest.mark.asyncio
async def test_game_field_coverage():
    """Test that GameProfile covers all fields returned by the API"""
    api = PyBanana()
    game_id = 297  # Team Fortress 2
    raw_data = await api._get_data(f"/Game/{game_id}/ProfilePage")
    _ = Game(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, Game, "GameProfile")


@pytest.mark.asyncio
async def test_member_field_coverage():
    """Test that MemberProfile covers all fields returned by the API"""
    api = PyBanana()
    member_id = 1382  # Tom
    raw_data = await api._get_data(f"/Member/{member_id}/ProfilePage")
    _ = Member(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, Member, "MemberProfile")


@pytest.mark.asyncio
async def test_studio_field_coverage():
    """Test that StudioProfile covers all fields returned by the API"""
    api = PyBanana()
    studio_id = 38059
    raw_data = await api._get_data(f"/Studio/{studio_id}/ProfilePage")
    _ = Studio(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, Studio, "StudioProfile")


@pytest.mark.asyncio
async def test_club_field_coverage():
    """Test that ClubProfile covers all fields returned by the API"""
    api = PyBanana()
    club_id = 28
    raw_data = await api._get_data(f"/Club/{club_id}/ProfilePage")
    _ = Club(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, Club, "ClubProfile")


@pytest.mark.asyncio
async def test_app_field_coverage():
    """Test that AppProfile covers all fields returned by the API"""
    api = PyBanana()
    app_id = 794
    raw_data = await api._get_data(f"/App/{app_id}/ProfilePage")
    _ = App(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, App, "AppProfile")


@pytest.mark.asyncio
async def test_bug_field_coverage():
    """Test that BugProfile covers all fields returned by the API"""
    api = PyBanana()
    bug_id = 4886
    raw_data = await api._get_data(f"/Bug/{bug_id}/ProfilePage")
    _ = Bug(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, Bug, "BugProfile")


@pytest.mark.asyncio
async def test_idea_field_coverage():
    """Test that IdeaProfile covers all fields returned by the API"""
    api = PyBanana()
    idea_id = 7079
    raw_data = await api._get_data(f"/Idea/{idea_id}/ProfilePage")
    _ = Idea(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, Idea, "IdeaProfile")


@pytest.mark.asyncio
async def test_result_field_coverage():
    """Test that Result covers all fields returned by the API"""
    api = PyBanana()
    mod_id = 572595  # Use same valid mod ID
    raw_data = await api._get_data(f"/Mod/{mod_id}/DownloadPage")
    _ = Result(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, Result, "Result")


@pytest.mark.asyncio
async def test_moderator_response_field_coverage():
    """Test that ModeratorResponse covers all fields returned by the API"""
    api = PyBanana()
    raw_data = await api._get_data(
        "/Member/Moderators"
    )  # Changed to ModeratorList endpoint
    _ = ModeratorResponse(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, ModeratorResponse, "ModeratorResponse")


@pytest.mark.asyncio
async def test_game_manager_response_field_coverage():
    """Test that GameManagerResponse covers all fields returned by the API"""
    api = PyBanana()
    game_id = 297  # Team Fortress 2
    raw_data = await api._get_data(f"/Game/{game_id}/Managers")
    _ = GameManagerResponse(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, GameManagerResponse, "GameManagerResponse")


@pytest.mark.asyncio
async def test_result_response_field_coverage():
    """Test that ResultResponse covers all fields returned by the API"""
    api = PyBanana()
    raw_data = await api._get_data(
        "/Util/Search/Results", params={"_sSearchString": "test"}
    )  # Search endpoint
    _ = ResultResponse(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, ResultResponse, "ResultResponse")

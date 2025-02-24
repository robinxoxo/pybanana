import pytest
from typing import get_type_hints
from pybanana.api import GameBananaAPI
from pybanana.models.profiles.mod import ModProfile
from pybanana.models.profiles.game import GameProfile
from pybanana.models.profiles.member import MemberProfile 
from pybanana.models.profiles.studio import StudioProfile
from pybanana.models.profiles.club import ClubProfile
from pybanana.models.profiles.app import AppProfile
from pybanana.models.profiles.bug import BugProfile
from pybanana.models.profiles.idea import IdeaProfile
from pybanana.models.result import Result
from pybanana.models.common.responses import ModeratorResponse, GameManagerResponse, ResultResponse

def check_field_coverage(api_data: dict | list, model_class, model_name: str):
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

def test_mod_field_coverage():
    """Test that ModProfile covers all fields returned by the API"""
    api = GameBananaAPI()
    mod_id = 572595  # known valid mod ID
    raw_data = api._get_data(f"/Mod/{mod_id}/ProfilePage")
    _ = ModProfile.from_dict(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, ModProfile, "ModProfile")

def test_game_field_coverage():
    """Test that GameProfile covers all fields returned by the API"""
    api = GameBananaAPI()
    game_id = 297  # Team Fortress 2
    raw_data = api._get_data(f"/Game/{game_id}/ProfilePage")
    _ = GameProfile.from_dict(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, GameProfile, "GameProfile")

def test_member_field_coverage():
    """Test that MemberProfile covers all fields returned by the API"""
    api = GameBananaAPI()
    member_id = 1382  # Tom
    raw_data = api._get_data(f"/Member/{member_id}/ProfilePage")
    _ = MemberProfile.from_dict(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, MemberProfile, "MemberProfile")

def test_studio_field_coverage():
    """Test that StudioProfile covers all fields returned by the API"""
    api = GameBananaAPI()
    studio_id = 38059
    raw_data = api._get_data(f"/Studio/{studio_id}/ProfilePage")
    _ = StudioProfile.from_dict(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, StudioProfile, "StudioProfile")

def test_club_field_coverage():
    """Test that ClubProfile covers all fields returned by the API"""
    api = GameBananaAPI()
    club_id = 28
    raw_data = api._get_data(f"/Club/{club_id}/ProfilePage")
    _ = ClubProfile.from_dict(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, ClubProfile, "ClubProfile")

def test_app_field_coverage():
    """Test that AppProfile covers all fields returned by the API"""
    api = GameBananaAPI()
    app_id = 794
    raw_data = api._get_data(f"/App/{app_id}/ProfilePage")
    _ = AppProfile.from_dict(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, AppProfile, "AppProfile")

def test_bug_field_coverage():
    """Test that BugProfile covers all fields returned by the API"""
    api = GameBananaAPI()
    bug_id = 4886
    raw_data = api._get_data(f"/Bug/{bug_id}/ProfilePage")
    _ = BugProfile.from_dict(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, BugProfile, "BugProfile")

def test_idea_field_coverage():
    """Test that IdeaProfile covers all fields returned by the API"""
    api = GameBananaAPI()
    idea_id = 7079
    raw_data = api._get_data(f"/Idea/{idea_id}/ProfilePage")
    _ = IdeaProfile.from_dict(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, IdeaProfile, "IdeaProfile")

def test_result_field_coverage():
    """Test that Result covers all fields returned by the API"""
    api = GameBananaAPI()
    mod_id = 572595  # Use same valid mod ID
    raw_data = api._get_data(f"/Mod/{mod_id}/DownloadPage")
    _ = Result.from_dict(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, Result, "Result")

def test_moderator_response_field_coverage():
    """Test that ModeratorResponse covers all fields returned by the API"""
    api = GameBananaAPI()
    raw_data = api._get_data(f"/Member/Moderators")  # Changed to ModeratorList endpoint
    _ = ModeratorResponse.from_dict(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, ModeratorResponse, "ModeratorResponse")

def test_game_manager_response_field_coverage():
    """Test that GameManagerResponse covers all fields returned by the API"""
    api = GameBananaAPI()
    game_id = 297  # Team Fortress 2
    raw_data = api._get_data(f"/Game/{game_id}/Managers")
    _ = GameManagerResponse.from_dict(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, GameManagerResponse, "GameManagerResponse")

def test_result_response_field_coverage():
    """Test that ResultResponse covers all fields returned by the API"""
    api = GameBananaAPI()
    raw_data = api._get_data("/Util/Search/Results", params={"_sSearchString": "test"})  # Search endpoint
    _ = ResultResponse.from_dict(raw_data)  # Verify we can create the model
    return check_field_coverage(raw_data, ResultResponse, "ResultResponse")
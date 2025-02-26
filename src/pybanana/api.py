# Standard library imports
from typing import Any, Dict, List, Optional

# Third party imports
import requests

# Local imports
from .enums import ContentType, OrderResult
from .models import (
    AppProfile,
    BugProfile,
    ClubProfile,
    GameManagerResponse,
    GameProfile,
    IdeaProfile,
    Member,
    MemberProfile,
    ModeratorResponse,
    ModProfile,
    ResultResponse,
    StudioProfile,
)

class GameBananaAPI:
    """GameBanana API client."""
    
    def __init__(self):
        self.base_url = "https://gamebanana.com/apiv11"
        self.headers = {"Accept": "application/json", "User-Agent": "Python/GameBananaAPI"}

    def _get_data(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Make a GET request to the GameBanana API."""
        url = f"{self.base_url}{endpoint}"
        if params is None:
            params = {}
        params["format"] = "json"  # Ensure JSON response
        response = requests.get(url, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_member(self, user_id: int) -> Member:
        """Get information about a specific user by ID."""
        data = self._get_data(f"/Member/{user_id}")
        return Member.from_dict(data)

    def get_member_profile(self, user_id: int) -> MemberProfile:
        """Get detailed profile information about a specific user."""
        data = self._get_data(f"/Member/{user_id}/ProfilePage")
        return MemberProfile.from_dict(data)

    def get_game_profile(self, game_id: int) -> GameProfile:
        """Get information about a specific game by ID."""
        data = self._get_data(f"/Game/{game_id}/ProfilePage")
        return GameProfile.from_dict(data)

    def get_app_profile(self, app_id: int) -> AppProfile:
        """Get information about a specific app by ID."""
        data = self._get_data(f"/App/{app_id}/ProfilePage")
        return AppProfile.from_dict(data)

    def get_bug_profile(self, bug_id: int) -> BugProfile:
        """Get information about a specific bug report by ID."""
        data = self._get_data(f"/Bug/{bug_id}/ProfilePage")
        return BugProfile.from_dict(data)

    def get_idea_profile(self, idea_id: int) -> IdeaProfile:
        """Get information about a specific idea by ID."""
        data = self._get_data(f"/Idea/{idea_id}/ProfilePage")
        return IdeaProfile.from_dict(data)
    
    def get_mod_profile(self, submission_id: int) -> ModProfile:
        """Get detailed information about a specific submission."""
        data = self._get_data(f"/Mod/{submission_id}/ProfilePage")
        return ModProfile.from_dict(data)
    
    def get_studio_profile(self, studio_id: int) -> StudioProfile:
        """Get information about a specific studio by ID."""
        data = self._get_data(f"/Studio/{studio_id}/ProfilePage")
        return StudioProfile.from_dict(data)
    
    def get_club_profile(self, club_id: int) -> ClubProfile:
        """Get information about a specific club by ID."""
        data = self._get_data(f"/Club/{club_id}/ProfilePage")
        return ClubProfile.from_dict(data)

    def get_moderators(self) -> ModeratorResponse:
        """Get a list of moderators."""
        data = self._get_data("/Member/Moderators")
        return ModeratorResponse.from_dict(data)

    def get_managers(self, page: int = 1, per_page = 15) -> GameManagerResponse:
        """Get a list of game managers with pagination."""
        params = { "_nPage": page, "_nPerpage": per_page } # only 15 seems tow work.
        data = self._get_data("/Member/GameManagers", params)
        return GameManagerResponse.from_dict(data)

    def get_download_url(self, model_name: ContentType, item_id: int, file_id: int) -> str:
        """Get the download URL for a specific file."""
        data = self._get_data(f"/{model_name}/{item_id}/ProfilePage")
        return data.get("_sDownloadUrl", "")

    def get_categories(self, model_name: ContentType) -> List[Dict[str, Any]]:
        """Get available categories for a specific model type."""
        data = self._get_data(f"/{model_name}/Categories")
        return data.get("_aRecords", [])
     
    def search(
        self,
        query: str,
        model: ContentType,
        order: OrderResult = OrderResult.RELEVANCE,
        page: int = 1,
        per_page: int = 15,
        fields: Optional[str] = None,
    ) -> ResultResponse:
        """Search for content across GameBanana."""
        params = {
            "_sSearchString": query,
            "_sModelName": model.value,
            "_sOrder": order.value,
            "_nPage": page,
            "_nPerpage": per_page,
            "_csvFields": "name,description,article,attribs,studio,owner,credits" or fields
        }
        
        data = self._get_data("/Util/Search/Results", params)
        return ResultResponse.from_dict(data)


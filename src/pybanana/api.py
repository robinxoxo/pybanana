# Standard library imports
import json
import traceback
from types import TracebackType
from typing import Any, Dict, List, Optional

# Third party imports
import requests
import aiohttp

# Local imports
from .enums import ModelType, OrderResult
from .models import (
    App,
    Bug,
    Club,
    GameManagerResponse,
    Game,
    Idea,
    Member,
    Member,
    ModeratorResponse,
    Mod,
    ResultResponse,
    Studio,
    OnlineResponse,
    DiscussionResponse,
)

class PyBanana:
    """GameBanana API client."""

    def __init__(self):
        self.base_url = "https://gamebanana.com/apiv11"
        self.headers = {"Accept": "application/json", "User-Agent": "Python/PyBanana"}

    async def _get_data(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Make a GET request to the GameBanana API."""
        url = f"{self.base_url}{endpoint}"
        if params is None:
            params = {}
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, params=params, headers=self.headers
            ) as response:
                response.raise_for_status()
                if response.content_type != "application/json":
                    data = json.loads(await response.text())
                else:
                    data = await response.json()
                return data

    async def _get_auth_cookies(self, username: str, password: str):
        """Authenticate with GameBanana and get session cookie."""   
        url = "https://gamebanana.com/apiv11/Member/Authenticate"
        json_data = { "_sUsername": username, "_sPassword": password }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, json=json_data, headers=self.headers
            ) as response:
                response.raise_for_status()
                return response.cookies

    async def get_member(self, user_id: int) -> Optional[Member]:
        """Get detailed profile information about a specific user."""
        try:
            data = await self._get_data(f"/Member/{user_id}/ProfilePage")
            return Member(data)
        except Exception as e:
            return None

    async def get_game(self, game_id: int) -> Optional[Game]:
        """Get information about a specific game by ID."""
        try:
            data = await self._get_data(f"/Game/{game_id}/ProfilePage")
            return Game(data)
        except Exception as e:
            return None

    async def get_app(self, app_id: int) -> Optional[App]:
        """Get information about a specific app by ID."""
        try:
            data = await self._get_data(f"/App/{app_id}/ProfilePage")
            return App(data)
        except Exception as e:
            return None

    async def get_bug(self, bug_id: int) -> Optional[Bug]:
        """Get information about a specific bug report by ID."""
        try:
            data = await self._get_data(f"/Bug/{bug_id}/ProfilePage")
            return Bug(data)
        except Exception as e:
            return None

    async def get_idea(self, idea_id: int) -> Optional[Idea]:
        """Get information about a specific idea by ID."""
        try:
            data = await self._get_data(f"/Idea/{idea_id}/ProfilePage")
            return Idea(data)
        except Exception as e:
            return None

    async def get_mod(self, submission_id: int) -> Optional[Mod]:
        """Get detailed information about a specific submission."""
        try:
            data = await self._get_data(f"/Mod/{submission_id}/ProfilePage")
            return Mod(data)
        except Exception as e:
            return None

    async def get_studio(self, studio_id: int) -> Optional[Studio]:
        """Get information about a specific studio by ID."""
        try:
            data = await self._get_data(f"/Studio/{studio_id}/ProfilePage")
            return Studio(data)
        except Exception as e:
            return None

    async def get_club(self, club_id: int) -> Optional[Club]:
        """Get information about a specific club by ID."""
        try:
            data = await self._get_data(f"/Club/{club_id}/ProfilePage")
            return Club(data)
        except Exception as e:
            return None

    async def get_moderators(self) -> Optional[ModeratorResponse]:
        """Get a list of moderators."""
        try:
            data = await self._get_data("/Member/Moderators")
            return ModeratorResponse(data)
        except Exception as e:
            return None

    async def get_managers(
        self, page: int = 1, per_page: int = 15
    ) -> Optional[GameManagerResponse]:
        """Get a list of game managers with pagination."""
        try:
            params = { "_nPage": page, "_nPerpage": per_page }
            data = await self._get_data("/Member/GameManagers", params=params)
            return GameManagerResponse(data)
        except Exception as e:
            return None

    async def get_online_members(
        self, page: int = 1, per_page: int = 15
    ) -> Optional[OnlineResponse]:
        """Get a list of currently online members."""
        try:
            params = {"_nPage": page, "_nPerpage": per_page}
            data = await self._get_data("/Member/Online", params=params)
            return OnlineResponse(data)
        except Exception as e:
            return None

    async def get_discussions(
        self, page: int = 1, per_page: int = 15
    ) -> Optional[DiscussionResponse]:
        """Get a list of recent discussions."""
        try:
            params = { "_nPage": page, "_nPerpage": per_page }
            data = await self._get_data("/Util/Generic/Discussions", params=params)
            return DiscussionResponse(data)
        except Exception as e:
            return None

    async def get_download_url(
        self, model_name: ModelType, item_id: int
    ) -> Optional[str]:
        """Get the download URL for a specific file."""
        try:
            data = await self._get_data(f"/{model_name}/{item_id}/ProfilePage")
            return data.get("_sDownloadUrl", "")
        except Exception as e:
            return None

    async def search(
        self,
        query: str,
        model: ModelType,
        order: OrderResult = OrderResult.RELEVANCE,
        page: int = 1,
        per_page: int = 15,
        fields: Optional[str] = None,
    ) -> Optional[ResultResponse]:
        """Search for content across GameBanana."""
        try:
            params = {
                "_sSearchString": query,
                "_sModelName": model.value,
                "_sOrder": order.value,
                "_nPage": page,
                "_nPerpage": per_page,
                "_csvFields": fields if fields is not None else "name,description,article,attribs,studio,owner,credits"
            }

            data = await self._get_data("/Util/Search/Results", params=params)
            return ResultResponse(data)
        except Exception as e:
            return None

# API Reference

## GameBananaAPI Class

The main interface for interacting with the GameBanana API.

### Core Methods

#### `__init__()`
Initializes a new GameBanana API client instance.

#### `search(query: str, model: ContentType, order: OrderResult = OrderResult.RELEVANCE, page: int = 1, per_page: int = 20, fields: Optional[str] = None) -> ResultResponse`
Search for content across GameBanana.

**Parameters:**
- `query` (str): The search query
- `model` (ContentType): Type of content to search for (e.g., MOD, GAME, MEMBER)
- `order` (OrderResult): How to order the results
- `page` (int): Page number for pagination
- `per_page` (int): Number of results per page
- `fields` (str): Comma-separated list of search fields

**Returns:**
- `ResultResponse` object containing search results and metadata

#### `get_member(user_id: int) -> Member`
Get basic information about a specific user.

**Parameters:**
- `user_id` (int): The ID of the user to retrieve

**Returns:**
- `Member` object with basic user information

#### `get_member_profile(user_id: int) -> MemberProfile`
Get detailed profile information about a specific user.

**Parameters:**
- `user_id` (int): The ID of the user to retrieve

**Returns:**
- `MemberProfile` object containing detailed user information

#### `get_game_profile(game_id: int) -> GameProfile`
Get information about a specific game.

**Parameters:**
- `game_id` (int): The ID of the game to retrieve

**Returns:**
- `GameProfile` object containing game information

#### `get_mod_profile(submission_id: int) -> ModProfile`
Get detailed information about a specific mod.

**Parameters:**
- `submission_id` (int): The ID of the mod to retrieve

**Returns:**
- `ModProfile` object containing detailed mod information

#### `get_studio_profile(studio_id: int) -> StudioProfile`
Get information about a specific studio.

**Parameters:**
- `studio_id` (int): The ID of the studio to retrieve

**Returns:**
- `StudioProfile` object containing studio information

#### `get_club_profile(club_id: int) -> ClubProfile`
Get information about a specific club.

**Parameters:**
- `club_id` (int): The ID of the club to retrieve

**Returns:**
- `ClubProfile` object containing club information

### Additional Methods

#### `get_categories(model_name: ContentType) -> List[Dict[str, Any]]`
Get available categories for a specific model type.

**Parameters:**
- `model_name` (ContentType): The type of content to get categories for

**Returns:**
- List of category dictionaries

### Response Objects

#### `ResultResponse`
Contains search results and metadata.
- `records`: List of matching records
- `record_count`: Total number of matching records

#### `ModeratorResponse`
Contains moderator information.
- `records`: List of moderator records

#### `GameManagerResponse`
Contains game manager information.
- `metadata`: Additional metadata about the response
- `records`: List of game manager records
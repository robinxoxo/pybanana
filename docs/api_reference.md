# 🍌 PyBanana API Reference

- [📚 Overview](#overview)
- [⚡ Installation](#installation)
- [🔧 Core API Client](#core-api-client)
  - [🚀 Initialization](#initialization)
  - [🔍 Search Operations](#search-operations)
  - [👤 Profile Methods](#profile-methods)
  - [🌐 Community Methods](#community-methods)
  - [🛠️ Utility Methods](#utility-methods)
- [📦 Response Objects](#response-objects)

## 📚 Overview

PyBanana provides a simple and intuitive interface to interact with the GameBanana API. This reference documents all available methods and their usage.

## ⚡ Installation

```bash
pip install pybanana
``` 

## 🔧 Core API Client

### 🚀 Initialization

```python
from pybanana import GameBananaAPI

api = GameBananaAPI()
```

### 🔍 Search Operations

#### Search Content
```python
search(
    query: str,
    model: ContentType,
    order: OrderResult = OrderResult.RELEVANCE,
    page: int = 1,
    per_page: int = 15,
    fields: Optional[str] = None
) -> ResultResponse
```

Search across GameBanana's content.

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `query` | str | Search query text | Required |
| `model` | ContentType | Content type to search (MOD, GAME, etc.) | Required |
| `order` | OrderResult | Result ordering | RELEVANCE |
| `page` | int | Page number | 1 |
| `per_page` | int | Results per page | 15 |
| `fields` | str | Comma-separated fields to include | None |

### 👤 Profile Methods

All profile methods return detailed information about specific GameBanana entities.

| Method | Description | Parameters |
|--------|-------------|------------|
| `get_member(user_id: int)` | Get basic user info | `user_id`: User's ID |
| `get_member_profile(user_id: int)` | Get detailed user profile | `user_id`: User's ID |
| `get_game_profile(game_id: int)` | Get game details | `game_id`: Game's ID |
| `get_mod_profile(submission_id: int)` | Get mod details | `submission_id`: Mod's ID |
| `get_app_profile(app_id: int)` | Get app details | `app_id`: App's ID |
| `get_bug_profile(bug_id: int)` | Get bug report | `bug_id`: Bug's ID |
| `get_idea_profile(idea_id: int)` | Get idea details | `idea_id`: Idea's ID |
| `get_studio_profile(studio_id: int)` | Get studio info | `studio_id`: Studio's ID |
| `get_club_profile(club_id: int)` | Get club details | `club_id`: Club's ID |

### 🌐 Community Methods

#### 👮 Get Moderators
```python
get_moderators() -> ModeratorResponse
```
Returns a list of GameBanana moderators.

#### 👑 Get Game Managers
```python
get_managers(
    page: int = 1,
    per_page: int = 15
) -> GameManagerResponse
```
Returns a paginated list of game managers.

### 🛠️ Utility Methods

#### 📥 Get Download URL
```python
get_download_url(
    model_name: ContentType,
    item_id: int,
    file_id: int
) -> str
```

Generate a download URL for a specific file.

#### 📑 Get Categories
```python
get_categories(
    model_name: ContentType
) -> List[Dict[str, Any]]
```

Retrieve available categories for a content type.

## 📦 Response Objects

### 🔍 ResultResponse
Container for search results that matches the GameBanana API response structure.

**Attributes:**
- `records`: List[Result] - List of Result objects containing the matching records
- `record_count`: int - Total number of matching records

**Usage:**
```python
response = api.search("query", ContentType.MOD)
for result in response.records:
    print(f"Found: {result}")
    print(f"Total results: {response.record_count}")
```

### 👮 ModeratorResponse
Container for moderator information from the moderators endpoint.

**Attributes:**
- `records`: List[ModeratorRecord] - List of ModeratorRecord objects containing moderator information

**Usage:**
```python
mods = api.get_moderators()
for mod in mods.records:
    print(f"Moderator: {mod}")
```

### 👑 GameManagerResponse
Container for game manager information from the game managers endpoint.

**Attributes:**
- `metadata`: Dict[str, Any] - Additional metadata about the response
- `records`: List[ManagerRecord] - List of ManagerRecord objects containing game manager information

**Usage:**
```python
managers = api.get_managers()
print(f"Metadata: {managers.metadata}")

for manager in managers.records:
    print(f"Manager: {manager}")
```

---

For more examples and detailed usage, check out the [Examples](../examples/) directory. 🚀
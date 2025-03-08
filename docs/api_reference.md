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
from pybanana.api import PyBanana

api = PyBanana()
```

### 🔍 Search Operations

#### Search Content
```python
search(
    query: str,
    model: ModelType,
    order: OrderResult = OrderResult.RELEVANCE,
    page: int = 1,
    per_page: int = 15,
    fields: Optional[str] = None
) -> Optional[ResultResponse]
```

Search across GameBanana's content. Returns `None` if the operation fails.

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `query` | str | Search query text | Required |
| `model` | ModelType | Content type to search (MOD, GAME, etc.) | Required |
| `order` | OrderResult | Result ordering | RELEVANCE |
| `page` | int | Page number | 1 |
| `per_page` | int | Results per page | 15 |
| `fields` | str | Comma-separated fields to include | None |

### 👤 Profile Methods

All profile methods return detailed information about specific GameBanana entities. Each method returns `None` if the operation fails.

| Method | Description | Return Type | Parameters |
|--------|-------------|-------------|------------|
| `get_member(user_id: int)` | Get basic user info | Optional[Member] | `user_id`: User's ID |
| `get_member_profile(user_id: int)` | Get detailed user profile | Optional[MemberProfile] | `user_id`: User's ID |
| `get_game_profile(game_id: int)` | Get game details | Optional[GameProfile] | `game_id`: Game's ID |
| `get_mod_profile(submission_id: int)` | Get mod details | Optional[ModProfile] | `submission_id`: Mod's ID |
| `get_app_profile(app_id: int)` | Get app details | Optional[AppProfile] | `app_id`: App's ID |
| `get_bug_profile(bug_id: int)` | Get bug report | Optional[BugProfile] | `bug_id`: Bug's ID |
| `get_idea_profile(idea_id: int)` | Get idea details | Optional[IdeaProfile] | `idea_id`: Idea's ID |
| `get_studio_profile(studio_id: int)` | Get studio info | Optional[StudioProfile] | `studio_id`: Studio's ID |
| `get_club_profile(club_id: int)` | Get club details | Optional[ClubProfile] | `club_id`: Club's ID |

### 🌐 Community Methods

#### 👮 Get Moderators
```python
get_moderators() -> Optional[ModeratorResponse]
```
Returns a list of GameBanana moderators. Returns `None` if the operation fails.

#### 👑 Get Game Managers
```python
get_managers(
    page: int = 1,
    per_page: int = 15
) -> Optional[GameManagerResponse]
```
Returns a paginated list of game managers. Returns `None` if the operation fails.

### 🛠️ Utility Methods

#### 📥 Get Download URL
```python
get_download_url(
    model_name: ModelType,
    item_id: int,
    file_id: int
) -> Optional[str]
```

Generate a download URL for a specific file. Returns `None` if the operation fails.

## 📦 Response Objects

### 🔍 ResultResponse
Container for search results that matches the GameBanana API response structure.

**Attributes:**
- `records`: List[Result] - List of Result objects containing the matching records
- `record_count`: int - Total number of matching records

**Usage:**
```python
response = api.search("query", ModelType.MOD)
if response:
    for result in response.records:
        print(f"Found: {result}")
    print(f"Total results: {response.record_count}")
else:
    print("Search failed or no results found")
```

### 👮 ModeratorResponse
Container for moderator information from the moderators endpoint.

**Attributes:**
- `records`: List[ModeratorRecord] - List of ModeratorRecord objects containing moderator information

**Usage:**
```python
mods = api.get_moderators()
if mods:
    for mod in mods.records:
        print(f"Moderator: {mod}")
else:
    print("Failed to retrieve moderators")
```

### 💬 DiscussionResponse
Container for discussion thread information.

**Attributes:**
- `metadata`: Dict[str, Any] - Additional metadata about the discussion
- `records`: List[DiscussionRecord] - List of DiscussionRecord objects containing thread information

**Usage:**
```python
discussions = api.get_discussions()
if discussions:
    print(f"Metadata: {discussions.metadata}")
    for record in discussions.records:
        print(f"Post Id: {record.post.id}")
else:
    print("Failed to retrieve discussions")
```

### 👥 OnlineResponse
Container for currently online users information.

**Attributes:**
- `records`: List[OnlineRecord] - List of OnlineRecord objects containing online user data
- `total_count`: int - Total number of users currently online

**Usage:**
```python
online = api.get_online_users()
if online:
    print(f"Total online: {online.total_count}")
    for user in online.records:
        print(f"User: {user}")
else:
    print("Failed to retrieve online users")
```

### 👑 GameManagerResponse
Container for game manager information from the game managers endpoint.

**Attributes:**
- `metadata`: Dict[str, Any] - Additional metadata about the response
- `records`: List[ManagerRecord] - List of ManagerRecord objects containing game manager information

**Usage:**
```python
managers = api.get_managers()
if managers:
    print(f"Metadata: {managers.metadata}")
    for manager in managers.records:
        print(f"Manager: {manager}")
else:
    print("Failed to retrieve game managers")
```

---

For more examples and detailed usage, check out the [Examples](../examples/) directory. 🚀
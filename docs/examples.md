# Examples

This document provides practical examples of using the PyBanana API client.

## Getting Game Information

```python
from pybanana.api import GameBananaAPI

api = GameBananaAPI()

# Get information about Half-Life 2 (ID: 9)
game = api.get_game_profile(9)

print(f"Game: {game.name}")
print(f"Description: {game.description}")
print(f"Game URL: {game.profile_url}")
print(f"Release Date: {game.release_date}")

# Print sections information
if game.sections:
    print("\nGame Sections:")
    for section in game.sections:
        print(f"- {section.plural_title} ({section.item_count} items)")
        print(f"  URL: {section.url}")

# Get available categories for mods
if game.mod_categories:
    print("\nMod Categories:")
    for category in game.mod_categories:
        print(f"- {category.name}")
```

## Working with Mods

```python
# Search for mods
results = api.search(
    query="texture pack",
    model=ContentType.MOD,
    order=OrderResult.DOWNLOADS  # Sort by most downloaded
)

# Get information about a specific mod
mod = api.get_mod_profile(572595)

print(f"Mod: {mod.name}")
print(f"Author: {mod.submitter.name}")
print(f"Views: {mod.stats.views:,}")
print(f"Downloads: {mod.stats.downloads:,}")
print(f"Description: {mod.description}")

# Get file information
if mod.files:
    print("\nFiles:")
    for file in mod.files:
        print(f"- {file.filename}")
        print(f"  Size: {file.filesize:,} bytes")
        print(f"  Downloads: {file.download_count:,}")
        print(f"  Download URL: {file.download_url}")

# Get studio information if available
if mod.studio:
    print(f"\nStudio: {mod.studio.name}")
    print(f"Studio URL: {mod.studio.profile_url}")
```

## User Profiles

```python
# Get basic member information
member = api.get_member(1382)
print(f"Username: {member.name}")
print(f"Profile URL: {member.profile_url}")

# Get detailed profile information
profile = api.get_member_profile(1382)
print(f"Member since: {profile.joined_date}")
print(f"Bio: {profile.bio}")
print(f"Reputation: {profile.reputation}")

if profile.stats:
    print("\nStats:")
    print(f"Submissions: {profile.stats.submissions}")
    print(f"Comments: {profile.stats.comments}")
```

## Working with Studios and Clubs

```python
# Get studio information
studio = api.get_studio_profile(12345)
print(f"Studio: {studio.name}")
print(f"Member count: {studio.member_count}")
print(f"Join mode: {studio.join_mode}")

if studio.open_positions:
    print("\nOpen positions:")
    for position in studio.open_positions:
        print(f"- {position.title}")

# Get club information
club = api.get_club_profile(67890)
print(f"Club: {club.name}")
print(f"Members: {club.member_count}")
print(f"Motto: {club.motto}")
```

## Advanced Usage

```python
# Get game managers
managers = api.get_game_managers(page=1, per_page=15)
for manager in managers.records:
    print(f"Manager: {manager['_sName']}")

# Get available categories for a content type
mod_categories = api.get_categories(ContentType.MOD)
for category in mod_categories:
    print(f"Category: {category['_sName']}")
```

For more detailed information about the available methods and data models, refer to the [API Reference](api_reference.md) and [Models](models.md) documentation.
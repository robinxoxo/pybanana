# 🍌 Getting Started with PyBanana

## 🚀 Introduction

PyBanana is a Python client library that provides a simple interface to interact with the GameBanana platform's API. It allows you to access various GameBanana features programmatically, including searching for mods, retrieving user profiles, and accessing game information.

## ⚡ Installation

You can install the package using pip:

```bash
pip install pybanana
```

## 📋 Requirements

- Python 3.7 or higher
- `requests` package (>=2.25.0)
- `python-dateutil` package (>=2.8.2)

## 🎮 Basic Usage

Here's a simple example to get you started:

```python
from pybanana.api import GameBananaAPI
from pybanana.enums import ContentType, OrderResult

# Initialize the API client
api = GameBananaAPI()

# Search for content
results = api.search(
    query="texture pack",
    model=ContentType.MOD,
    order=OrderResult.RELEVANCE,
    page=1,
    per_page=15
)

# Print search results
for result in results.records:
    print(f"Found: {result.name}")

# Get game information
game = api.get_game_profile(297)  # Team Fortress 2
print(f"Game: {game.name}")
print(f"Description: {game.description}")

# Get mod details
mod = api.get_mod_profile(572595)  # Example mod ID
print(f"Mod: {mod.name}")
print(f"Author: {mod.submitter.name}")
print(f"Downloads: {mod.stats.downloads}")

# Get user information
member = api.get_member_profile(1382)  # Example user ID
print(f"Username: {member.name}")
print(f"Member Since: {member.join_date}")
```

## ⚠️ Error Handling

The API client will raise exceptions when encountering errors. It's recommended to handle these appropriately:

```python
try:
    mod = api.get_mod_profile(999999999)  # Non-existent ID
except Exception as e:
    print(f"Error: {str(e)}")
```

## 📦 Content Types

The library supports various content types through the `ContentType` enum:

- 🎮 `ContentType.MOD` - Game modifications
- 🕹️ `ContentType.GAME` - Games
- 👤 `ContentType.MEMBER` - User profiles
- 🏢 `ContentType.STUDIO` - Game development studios
- 👥 `ContentType.CLUB` - Community clubs
- 💻 `ContentType.APP` - Applications
- 🐛 `ContentType.BUG` - Bug reports
- 💡 `ContentType.IDEA` - Game ideas and concepts

## 📄 Pagination

Many methods support pagination to handle large result sets:

```python
# Get first page of search results
page1 = api.search(query="map", model=ContentType.MOD, page=1, per_page=15)

# Get next page
page2 = api.search(query="map", model=ContentType.MOD, page=2, per_page=15)
```

## 📚 Next Steps

For more detailed examples and usage information, check out:

- [🔨 Examples](examples.md) - More code examples and use cases
- [📖 API Reference](api_reference.md) - Complete API documentation
- [🏗️ Models](models.md) - Data model documentation
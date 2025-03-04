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
from pybanana.api import PyBanana
from pybanana.enums import ModelType, OrderResult

# Initialize the API client
api = PyBanana()

# Search for content
results = api.search(
    query="texture pack",
    model=ModelType.MOD,
    order=OrderResult.RELEVANCE,
    page=1,
    per_page=15
)

# Check if search was successful and print results
if results:
    for result in results.records:
        print(f"Found: {result.name}")
else:
    print("Search failed or returned no results")

# Get game information
game = api.get_game_profile(297)  # Team Fortress 2
if game:
    print(f"Game: {game.name}")
    print(f"Description: {game.description}")

# Get mod details
mod = api.get_mod_profile(572595)  # Example mod ID
if mod:
    print(f"Mod: {mod.name}")
    print(f"Author: {mod.submitter.name}")
    print(f"Downloads: {mod.stats.downloads}")

# Get user information
member = api.get_member_profile(1382)  # Example user ID
if member:
    print(f"Username: {member.name}")
    print(f"Member Since: {member.join_date}")
```

## ⚠️ Error Handling

All API methods now return `None` when they fail, so you should always check if the returned value exists:

```python
# Try to get a mod with a non-existent ID
mod = api.get_mod_profile(999999999)
if mod:
    print(f"Found mod: {mod.name}")
else:
    print("Mod not found or an error occurred")
```

## 📦 Model Types

The library supports various model types through the `ModelType` enum:

- 🎮 `ModelType.MOD` - Game modifications
- 🕹️ `ModelType.GAME` - Games
- 👤 `ModelType.MEMBER` - User profiles
- 🏢 `ModelType.STUDIO` - Game development studios
- 👥 `ModelType.CLUB` - Community clubs
- 💻 `ModelType.APP` - Applications
- 🐛 `ModelType.BUG` - Bug reports
- 💡 `ModelType.IDEA` - Game ideas and concepts

## 📄 Pagination

Many methods support pagination to handle large result sets:

```python
# Get first page of search results
page1 = api.search(query="map", model=ModelType.MOD, page=1, per_page=15)

# If first page was successful, get next page
if page1:
    page2 = api.search(query="map", model=ModelType.MOD, page=2, per_page=15)
```

## 📚 Next Steps

For more detailed examples and usage information, check out:

- [🔨 Examples](examples.md) - More code examples and use cases
- [📖 API Reference](api_reference.md) - Complete API documentation
- [🏗️ Models](models.md) - Data model documentation
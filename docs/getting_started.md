# Getting Started with PyBanana

## Introduction

PyBanana is a Python client library that provides a simple interface to interact with the GameBanana platform's API. It allows you to access various GameBanana features programmatically, including searching for mods, retrieving user profiles, and accessing game information.

## Installation

You can install the package using pip:

```bash
pip install pybanana
```

## Requirements

- Python 3.7 or higher
- `requests` package (>=2.25.0)
- `python-dateutil` package (>=2.8.2)

## Basic Usage

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
    per_page=20
)

# Get game information
game = api.get_game_profile(297)  # Team Fortress 2
print(f"Game: {game.name}")
print(f"Description: {game.description}")

# Get mod details
mod = api.get_mod_profile(12345)  # Replace with actual mod ID
print(f"Mod: {mod.name}")
print(f"Author: {mod.submitter.name}")
print(f"Downloads: {mod.stats.downloads}")

# Get user information
member = api.get_member_profile(1382)
print(f"Username: {member.name}")
print(f"Member Since: {member.joined_date}")
print(f"Profile URL: {member.profile_url}")
```

For more detailed examples and usage information, check out the [API Reference](api_reference.md) and [Examples](examples.md) sections.
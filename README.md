# 🍌 PyBanana
A powerful and intuitive Python client library for interacting with the GameBanana API. This library provides easy access to GameBanana's extensive modding platform, allowing you to search, retrieve, and interact with mods, users, games, and more.

> **Note**: This library is currently a Work in Progress (WIP). Features and APIs may change.

## Features
- 🔍 **Comprehensive API Coverage**
  - Search for mods across GameBanana
  - Fetch detailed mod information
  - Access user profiles and statistics
  - Get game information and categories
  - Browse mod sections and categories
- 🛠 **Developer-Friendly**
  - Full type hints support with Optional return types
  - Intuitive object-oriented models
  - Robust error handling with graceful failure (returns None)
  - Well-documented API methods
- 🚀 **Easy to Use**
  - Simple and clean API
  - Pythonic interface
  - Extensive examples provided

## Quick Start

```python
from pybanana.api import PyBanana
from pybanana.enums import ModelType

# Initialize the client
api = PyBanana()

# Get a member's profile
member = api.get_member(1382)  # Tom's ID
if member:
    print(f"Name: {member.name}")
    print(f"Online: {member.is_online}")

# Search for mods
results = api.search("sound effects", ModelType.MOD)
if results:
    for mod in results.records:
        print(f"Mod: {mod.name} - {mod.description}")
```

## Installation
```bash
pip install pybanana
```

## Documentation
For detailed documentation and examples, check out:
- [Getting Started](docs/getting_started.md)
- [API Reference](docs/api_reference.md)
- [Models Reference](docs/models.md)

## Requirements

### Runtime Dependencies
- Python 3.10+
- `aiohttp` >= 3.12.0

### Development Dependencies
- `pytest` >= 8.0.0
- `pytest-asyncio` >= 1.1.0

## Error Handling
All public API methods now return `Optional` types and include built-in error handling. When an API call fails, methods return `None` instead of raising exceptions, allowing for more resilient code:

```python
# Safe API usage with None check
mod = api.get_mod_profile(12345)
if mod:
    print(f"Found mod: {mod.name}")
else:
    print("Mod not found or API error occurred")
```

## Contributing
Contributions are welcome! Here's how you can help:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to GameBanana for providing the API
- All contributors who help improve this library
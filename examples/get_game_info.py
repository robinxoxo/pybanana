from pybanana.api import PyBanana

def main():
    api = PyBanana()

    id = 9  # Half-Life 2
    # Example game ID for Half-Life 2
    try:
        game = api.get_game(id)

        if game:
            print(f"Game: {game.name}")
            print(f"Description: {game.description}")
            print(f"Game URL: {game.profile_url}")
            print(f"Release Date: {game.release_date}")
            print(f"Welcome Message: {game.welcome_message}")

            # Print sections information
            if game.sections:
                print("\nGame Sections:")
                for section in game.sections:
                    print(f"- {section.plural_title} ({section.item_count} items)")
                    print(f"  URL: {section.url}")

            # Get available categories for mods in this game
            if game.mod_categories:
                print("\nMod Categories:")
                for category in game.mod_categories:
                    print(f"- {category.name}")
        else:
            print(f"Could not find game with ID {id}")

    except Exception as e:
        print(f"Error fetching game info: {str(e)}")
        raise  # Show full traceback for debugging

if __name__ == "__main__":
    main()

from pybanana.api import PyBanana
from pybanana.enums import ModelType
import json

def main():
    mod_id = 572595  # Example mod ID
    file_id = 123456  # Example file ID

    api = PyBanana()

    try:
        # Get the mod profile first
        mod = api.get_mod(mod_id)

        print(f"\nMod: {mod.name}")
        print(f"Views: {mod.view_count:,}")
        print(f"Likes: {mod.like_count:,}")
        print(f"Description: {mod.description}")

        # Get file information
        if mod.files and len(mod.files) > 0:
            print("\nFiles:")
            for file in mod.files:
                print(f"- {file.filename}")
                print(f"  Size: {file.filesize:,} bytes")
                print(f"  Downloads: {file.download_count:,}")
                print(f"  Download URL: {file.download_url}")
        else:
            print("\nNo files found for this mod")

        # If the mod is from a studio, get studio information
        if mod.studio:
            print(f"\nStudio Information:")
            studio_attrs = {
                'name': 'Studio name',
                'profile_url': 'Studio URL',
                'id': 'Studio Id',
                'description': 'Studio description',
                'member_count': 'Studio members'
            }

            for attr, label in studio_attrs.items():
                try:
                    value = getattr(mod.studio, attr)
                    if value is not None:
                        print(f"{label}: {value}")
                except AttributeError:
                    continue  # Skip attributes that don't exist

    except Exception as e:
        print(f"Error fetching mod information: {e}")

if __name__ == "__main__":
    main()

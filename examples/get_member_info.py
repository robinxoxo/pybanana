from pybanana.api import GameBananaAPI

def main():
    # Initialize the API client
    api = GameBananaAPI()
    
    # Get basic member information
    id = 1382 # Example member ID
    member = api.get_member(id)
    print(f"Member name: {member.name}")
    print(f"Member ID: {member.id}")
    print(f"Member is online: {member.is_online}")
    print(f"Member avatar URL: {member.avatar_url}")
    print(f"Member profile URL: {member.profile_url}")

    profile_data = api.get_member_profile(id)
    print("Clearance levels:")
    for level in profile_data.clearance_levels:
        print(f"- {level}")

    # Get detailed profile information
    profile = api.get_member_profile(id)
    print(f"Member profile URL: {profile.profile_url}")
    print(f"Member points: {profile.points}")
    print(f"Member points rank: {profile.points_rank}")
    print(f"Member join date: {profile.join_date}")
    print(f"Member user title: {profile.user_title}")
    print(f"Member is banned: {profile.is_banned}")

if __name__ == "__main__":
    main()
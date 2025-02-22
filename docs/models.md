# Models Reference

This document describes the data models used in PyBanana.

## Core Models

### Member
Basic member information model.
- `id`: Member ID
- `name`: Username
- `profile_url`: URL to member's profile
- `avatar_url`: URL to member's avatar
- `online_status`: Current online status

### Profile
Base profile model inherited by specific profile types.
- `id`: Profile ID
- `name`: Profile name
- `description`: Profile description
- `profile_url`: URL to the profile

## Profile Models

### GameProfile
Game information model.
- `name`: Game name
- `description`: Game description
- `release_date`: Game release date
- `sections`: List of game sections
- `mod_categories`: Available mod categories
- `preview_media`: Game media assets
- `stats`: Game statistics

### ModProfile
Mod information model.
- `name`: Mod name
- `description`: Mod description
- `submitter`: Member who submitted the mod
- `files`: List of downloadable files
- `preview_media`: Mod screenshots and media
- `stats`: Download and rating statistics
- `studio`: Associated studio (if any)

### MemberProfile
Detailed member profile model.
- `name`: Username
- `bio`: Member's biography
- `joined_date`: Registration date
- `reputation`: Member reputation
- `stats`: Activity statistics
- `preview_media`: Member's avatar and images

### StudioProfile
Studio information model.
- `name`: Studio name
- `description`: Studio description
- `member_count`: Number of members
- `join_mode`: Studio joining policy
- `open_positions`: Available positions

### ClubProfile
Club information model.
- `name`: Club name
- `description`: Club description
- `member_count`: Number of members
- `motto`: Club motto

## Common Components

### PreviewMedia
Media assets model.
- `images`: List of preview images
- `audio`: List of audio files
- `videos`: List of video files

### CoreStats
Basic statistics model.
- `views`: View count
- `downloads`: Download count
- `likes`: Like count
- `comments`: Comment count

### RatingsSummary
Rating statistics model.
- `total_ratings`: Number of ratings
- `average_rating`: Average rating score
- `rating_breakdown`: Rating distribution

### Author
Content creator information.
- `id`: Author ID
- `name`: Author name
- `role`: Author's role
- `profile_url`: URL to author's profile

### CreditGroup
Group credit information.
- `name`: Group name
- `authors`: List of authors
- `description`: Credit description

## Response Models

### ResultResponse
Search results container.
- `records`: List of matching records
- `record_count`: Total number of matches

### ModeratorResponse
Moderator list container.
- `records`: List of moderator records

### GameManagerResponse
Game manager list container.
- `metadata`: Response metadata
- `records`: List of manager records
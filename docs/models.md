# 🏗️ Models Reference

This document describes the data models used in PyBanana.

## 🔮 Core Models

### 👤 Member
Basic member information.
```python
class Member:
    id: int
    name: str
    is_online: bool
    has_ripe: bool
    profile_url: str
    avatar_url: str
```

### 📋 Profile
Base profile class shared by all profile types.
```python
class Profile:
    id: Optional[int]
    status: Optional[int]
    is_private: Optional[bool]
    date_modified: Optional[datetime]
    date_added: Optional[datetime]
    profile_url: Optional[str]
    preview_media: Optional[PreviewMedia]
    name: Optional[str]
    initial_visibility: Optional[str]
    has_files: Optional[bool]
    subscriber_count: Optional[int]
    show_ripe_promo: Optional[bool]
    accessor_subscription_row: Optional[int]
    accessor_is_subscribed: Optional[bool]
```

### 👥 MemberProfile
Detailed member profile information.
```python
class MemberProfile:
    base: Profile
    user_title: str
    join_date: datetime
    avatar_url: str
    points_url: str
    medals_url: str
    is_online: bool
    online_title: str
    offline_title: str
    points: int
    points_rank: int
    bio_entries: List[Bio]
    is_banned: bool
    online_status: Optional[OnlineStatus]
    core_stats: Optional[CoreStats]
    honorary_title: Optional[str]
    signature_url: Optional[str]
    clearance_levels: List[str]
    responsibilities: List[str]
    modgroups: List[str]
```

### 🎮 ModProfile
Detailed mod information.
```python
class ModProfile:
    base: Profile
    feedback_instructions: str
    accessor_is_submitter: bool
    is_trashed: bool
    is_withheld: bool
    name: str
    updates_count: int
    has_updates: bool
    all_todos_count: int
    has_todos: bool
    post_count: int
    attributes: Dict[str, List[str]]
    tags: List[Dict[str, str]]
    created_by_submitter: bool
    is_ported: bool
    thanks_count: int
    initial_visibility: str
    download_url: str
    download_count: int
    files: List[File]
    subscriber_count: int
    studio: Optional[StudioProfile]
    contributing_studios: List[Any]
    license: str
    license_checklist: Optional[LicenseChecklist]
    description: str
    generate_table_of_contents: bool
    text: str
    like_count: int
    view_count: int
    is_mapped: bool
    is_textured: bool
    is_animated: str
    accepts_donations: bool
    show_ripe_promo: bool
    embeddables: Optional[Embeddable]
    submitter: Optional[Member]
    category: Optional[ModCategory]
    credits: Optional[Credits]
    advanced_requirements_exist: bool
    requirements: List[List[str]]
    accessor_subscription_row_id: int
    accessor_is_subscribed: bool
    accessor_has_thanked: bool
    accessor_has_unliked: bool
    accessor_has_liked: bool
```

### 🎯 GameProfile
Game information.
```python
class GameProfile:
    base: Profile
    homepage: str
    is_approved: bool
    sections: List[GameSection]
    mod_categories: List[ModCategory]
    managers: List[ManagerRecord]
    abbreviation: Optional[str]
    release_date: Optional[datetime]
    welcome_message: Optional[str]
    description: Optional[str]
```

### 🏢 StudioProfile
Studio information.
```python
class StudioProfile:
    base: Profile
    motto: Optional[str]
    join_mode: str
    flag_url: Optional[str]
    banner_url: Optional[str]
    member_count: int
    post_count: int
    social_links: List[Dict[str, str]]
    profile_template: str
    profile_modules: List[str]
    open_positions: List[OpenPosition]
    leadership: List[Member]
    accessor_is_in_guild: bool
    accessor_has_pending_join_request: bool
    game: Dict[str, str]
```

### 👥 ClubProfile
Club information.
```python
class ClubProfile:
    base: Profile
    status: int
    is_private: bool
    date_modified: Optional[datetime]
    date_added: Optional[datetime]
    preview_media: Optional[PreviewMedia]
    accessor_is_submitter: bool
    is_trashed: bool
    name: str
    post_count: int
    initial_visibility: str
    has_files: bool
    text: str
    member_count: int
    last_activity_date: Optional[datetime]
    show_ripe_promo: bool
    submitter: Optional[Member]
    flag_url: str
    banner_url: str
    motto: str
    join_mode: str
    social_links: List[str]
    profile_template: str
    profile_modules: List[str]
    accessor_is_in_guild: bool
    accessor_has_pending_join_request: bool
    leadership: List[ManagerRecord]
```

### 💻 AppProfile
App information.
```python
class AppProfile:
    base: Profile
    description: str
    include_variable_name: str
    version: str
    state: str
    type: str
    user_count: int
    is_safe: bool
    accepts_donations: bool
    accessor_has_app: bool
    features: Optional[AppFeatures]
    credits: Optional[Credits]
    sticker_url: str
    categories: List[ModCategory]
    bio: Optional[Bio]
    stats: Optional[CoreStats]
```

### 🐛 BugProfile
Bug report information.
```python
class BugProfile:
    base: Profile
    status: int
    is_private: bool
    date_modified: Optional[datetime]
    date_added: Optional[datetime]
    preview_media: Optional[PreviewMedia]
    accessor_is_submitter: bool
    is_trashed: bool
    post_count: int
    thanks_count: int
    initial_visibility: str
    has_files: bool
    subscriber_count: int
    text: str
    resolution: str
    resolution_key: str
    priority: str
    priority_key: str
    source_url: str
    show_ripe_promo: bool
    embeddables: List[Embeddable]
    submitter: Optional[Member]
    attachments: List[File]
    accessor_subscription_row_id: int
    accessor_is_subscribed: bool
    accessor_has_thanked: bool
```

### 💡 IdeaProfile
Idea information.
```python
class IdeaProfile:
    base: Profile
    text: str
    post_count: int
    has_revisions: bool
    has_changelog: bool
    is_private: bool
    is_shared: bool
    sorting_priority: int
    supports_downvoting: bool
    ratings_summary: Optional[RatingsSummary]
    embeddables: List[Embeddable]
```

## 🧩 Common Components

### 🖼️ PreviewMedia
Media preview information.
```python
class PreviewMedia:
    images: List[PreviewMediaImage]
    videos: List[str]
```

### 📁 File
File information.
```python
class File:
    id: int
    filename: str
    filesize: int
    description: str
    date_added: datetime
    download_count: int
    analysis_state: str
    analysis_result_code: str
    analysis_result: str
    contains_exe: bool
    download_url: str
    md5_checksum: str
    clam_av_result: str
    avast_av_result: str
```

### 📊 CoreStats
Basic statistics.
```python
class CoreStats:
    account_age: str
    current_submissions: int
    current_subscribers: int
    thanks_received: int
    points: int
    submissions_featured: int
    medals_count: int
```

### 🌐 OnlineStatus
Online status information.
```python
class OnlineStatus:
    is_online: bool
    location: str
    last_seen_time: Optional[datetime]
    session_creation_time: Optional[datetime]
```

### 📝 Bio
Biography information container.
```python
class Bio:
    entries: List[BioEntry]
```

### 📌 BioEntry
Individual biography entry.
```python
class BioEntry:
    title: str
    value: str
    custom_title: Optional[str]
```

### ⭐ Credits
Credits section container.
```python
class Credits:
    groups: List[CreditGroup]
```

### 👥 CreditGroup
Group of authors in credits.
```python
class CreditGroup:
    group_name: str
    authors: List[Author]
```

### ✍️ Author
Credit author information.
```python
class Author:
    role: str
    name: str
    id: Optional[int]
    upic_url: Optional[str]
    profile_url: Optional[str]
    is_online: Optional[bool]
    affiliated_studio: Optional[AffiliatedStudio]
```

### 🏢 AffiliatedStudio
Studio affiliation information.
```python
class AffiliatedStudio:
    profile_url: str
    name: str
    flag_url: str
    banner_url: str
```

### 🔌 Embeddable
Embeddable content information.
```python
class Embeddable:
    image_base_url: Optional[str]
    variants: Optional[List[str]]
```

### 🎯 GameSection
Game section information.
```python
class GameSection:
    model_name: str
    plural_title: str
    item_count: int
    category_count: int
    url: str
```

### 📂 ModCategory
Category information.
```python
class ModCategory:
    id: int
    name: str
    item_count: int
    category_count: int
    url: str
```

### 🎯 OpenPosition
Open position information in a studio.
```python
class OpenPosition:
    skill_id: str
    skill: str
    game_id: str
    game: Dict[str, str]
    notes: str
```

### 📱 AppFeatures
App features information.
```python
class AppFeatures:
    profile_module_url: str
    navigator_tab_url: str
    main_url: str
    settings_url: str
```

## 📦 Response Models

### 🔍 ResultResponse
Container for search results.
```python
class ResultResponse:
    records: List[Result]
    record_count: int
```

### 👮 ModeratorResponse
Response from moderators endpoint.
```python
class ModeratorResponse:
    records: List[ModeratorRecord]
```

### 👑 GameManagerResponse 
Response from game managers endpoint.
```python
class GameManagerResponse:
    records: List[ManagerRecord]
```

### 👥 ModeratorRecord
Individual moderator record.
```python
class ModeratorRecord:
    member: Member
    modgroups: List[str]
    staff_bio: str
```

### 👥 ManagerRecord
Individual manager record.
```python
class ManagerRecord:
    member: Member
    modgroups: List[str]
    date_added: Optional[int]
```

## 🔄 Enums

### 📁 ContentType
Available content types.
```python
class ContentType(str, Enum):
    APP = "App"
    ARTICLE = "Article" 
    BUG = "Bug"
    BLOG = "Blog"
    CLUB = "Club"
    CONTEST = "Contest"
    CONCEPT = "Concept"
    EVENT = "Event"
    GAME = "Game"
    IDEA = "Idea"
    INITIATIVE = "Initiative"
    JAM = "Jam"
    MOD = "Mod"
    MODEL = "Model"
    MEMBER = "Member"
    NEWS = "News"
    POLL = "Poll"
    PROJECT = "Project"
    QUESTION = "Question"
    REVIEW = "Review"
    REQUEST = "Request"
    SCRIPT = "Script"
    SOUND = "Sound"
    SPRAY = "Spray"
    STUDIO = "Studio"
    THREAD = "Thread"
    TOOL = "Tool"
    TUTORIAL = "Tutorial"
    WIKI = "Wiki"
    WIP = "Wip"
```

### 📋 OrderResult
Search result ordering options.
```python
class OrderResult(Enum):
    RELEVANCE = "relevancy"
    DATE = "date"
    LIKES = "likes"
    VIEWS = "views"
    DOWNLOADS = "downloads"
```

📝 Note: All datetime fields are provided as Python `datetime` objects. The library handles the conversion from GameBanana's timestamp format automatically.
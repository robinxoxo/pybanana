@dataclass
class CheckpointCreator:
    username: str
    details: CheckpointCreatorDetails

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CheckpointCreator":
        return cls(
            username=data["_sUsername"],
            details=CheckpointCreatorDetails.from_dict(data["_aCheckpointCreatorDetails"])
        )
    
@dataclass
class CheckpointCreatorDetails:
    avatar_url: str
    details_url: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CheckpointCreatorDetails":
        return cls(
            avatar_url=data["_sAvatarUrl"],
            details_url=data["_sDetailsUrl"]
        )

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ProfileField:
    """Base class for formatted profile field entries."""
    title: str
    value: str
    input_type: Optional[str] = None
    icon_classes: Optional[str] = None
    value_template: Optional[str] = None
    formatted_value: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "ProfileField":
        """Create a ProfileField instance from a dictionary."""
        return cls(
            title=data["_sTitle"],
            value=data["_sValue"],
            input_type=data.get("_sInputType", ""),
            icon_classes=data.get("_sIconClasses", ""),
            value_template=data.get("_sValueTemplate", ""),
            formatted_value=data.get("_sFormattedValue", "")
        )
    
@dataclass
class ContactInfo(ProfileField):
    """A GameBanana contact information entry."""
    pass

@dataclass
class PcSpecs(ProfileField):
    """A GameBanana PC specification entry."""
    pass

@dataclass
class SoftwareKit(ProfileField):
    """A GameBanana software kit entry."""
    pass

@dataclass
class GamingDevices(ProfileField):
    """A GameBanana gaming devices entry."""
    pass
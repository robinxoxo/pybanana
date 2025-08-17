from dataclasses import dataclass
from typing import Any, List, Optional

@dataclass
class ProfileField:
    """Base class for formatted profile field entries."""
    title: str
    value: str
    input_type: Optional[str] = None
    icon_classes: Optional[str] = None
    value_template: Optional[str] = None
    formatted_value: Optional[str] = None

    def __init__(self, data: dict[str, list]):
        """Create a ProfileField instance from a dictionary."""
        self.title = data["_sTitle"]
        self.value = data["_sValue"]
        self.input_type = data.get("_sInputType", "")
        self.icon_classes = data.get("_sIconClasses", "")
        self.value_template = data.get("_sValueTemplate", "")
        self.formatted_value = data.get("_sFormattedValue", "")


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

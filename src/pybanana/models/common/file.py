"""File-related shared components."""
from dataclasses import dataclass
from typing import Dict, Any, Optional
from datetime import datetime

@dataclass
class File:
    """File information for a mod."""
    id: int = 0
    filename: str = ""
    filesize: int = 0
    description: str = ""
    date_added: Optional[datetime] = None
    download_count: int = 0
    analysis_state: str = ""
    analysis_result_code: str = ""
    analysis_result: str = ""
    contains_exe: bool = False
    download_url: str = ""
    md5_checksum: str = ""
    clam_av_result: str = ""
    avast_av_result: str = ""

    def __post_init__(self):
        if self.date_added is None:
            self.date_added = datetime.fromtimestamp(0)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "File":
        try:
            timestamp = data.get("_tsDateAdded", 0)
            date_added = datetime.fromtimestamp(timestamp) if timestamp else None
        except (ValueError, OSError):
            date_added = None

        return cls(
            id=data.get("_idRow", 0) or 0,
            filename=data.get("_sFile", "") or "",
            filesize=data.get("_nFilesize", 0) or 0,
            description=data.get("_sDescription", "") or "",
            date_added=date_added,
            download_count=data.get("_nDownloadCount", 0) or 0,
            analysis_state=data.get("_sAnalysisState", "") or "",
            analysis_result_code=data.get("_sAnalysisResultCode", "") or "",
            analysis_result=data.get("_sAnalysisResult", "") or "",
            contains_exe=data.get("_bContainsExe", False),
            download_url=data.get("_sDownloadUrl", "") or "",
            md5_checksum=data.get("_sMd5Checksum", "") or "",
            clam_av_result=data.get("_sClamAvResult", "") or "",
            avast_av_result=data.get("_sAvastAvResult", "") or ""
        )
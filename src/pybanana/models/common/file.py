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

    def __init__(self, data: Dict[str, Any]):
        try:
            timestamp = data.get("_tsDateAdded", 0)
            date_added = datetime.fromtimestamp(timestamp) if timestamp else None
        except (ValueError, OSError):
            date_added = None

        self.id = data.get("_idRow", 0)
        self.filename = data.get("_sFile", "")
        self.filesize = data.get("_nFilesize", 0)
        self.date_added = date_added
        self.download_count = data.get("_nDownloadCount", 0)
        self.analysis_state = data.get("_sAnalysisState", "")
        self.analysis_result_code = data.get("_sAnalysisResultCode", "")
        self.analysis_result = data.get("_sAnalysisResult", "")
        self.contains_exe = data.get("_bContainsExe", False)
        self.download_url = data.get("_sDownloadUrl", "")
        self.md5_checksum = data.get("_sMd5Checksum", "")
        if self.date_added is None:
            self.date_added = datetime.fromtimestamp(0)

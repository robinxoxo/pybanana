"""File-related shared components."""
from dataclasses import dataclass
from typing import Dict, Any
from datetime import datetime

@dataclass
class File:
    """File information for a mod."""
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

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "File":
        return cls(
            id=data["_idRow"],
            filename=data["_sFile"],
            filesize=data["_nFilesize"],
            description=data["_sDescription"],
            date_added=datetime.fromtimestamp(data["_tsDateAdded"]),
            download_count=data["_nDownloadCount"],
            analysis_state=data["_sAnalysisState"],
            analysis_result_code=data["_sAnalysisResultCode"],
            analysis_result=data["_sAnalysisResult"],
            contains_exe=data["_bContainsExe"],
            download_url=data["_sDownloadUrl"],
            md5_checksum=data["_sMd5Checksum"],
            clam_av_result=data["_sClamAvResult"],
            avast_av_result=data["_sAvastAvResult"]
        )
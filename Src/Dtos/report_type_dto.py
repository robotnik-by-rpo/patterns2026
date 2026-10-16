from enum import Enum
from Src.Core.exception import arguments_exception

"""
Type a report
"""
class report_type_enum(Enum):
    """
    Text format
    """
    TXT = "TXT"
    CSV = "CSV"
    MD = "MD"
    XML = "XML"
    HTML = "HTML"

    @classmethod
    def from_string(cls, value: str) -> "report_type_enum":
        key = str(value).strip().upper()
        aliases = {"MARKDOWN": cls.MD}
        if key in aliases:
            return aliases[key]
        try:
            return cls(key)
        except ValueError:
            raise arguments_exception(
                "response_format",
                f"unsupported format: {value}"
            )
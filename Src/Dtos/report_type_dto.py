from enum import Enum

"""
Type a report
"""
class report_type_enum(Enum):
    """
    Text format
    """
    TXT = 1
    CSV = 2
    MD = 3 # markdown
    XML = 4
    HTML = 5
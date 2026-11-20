from enum import Enum
from Src.Core.exception import not_exist_exception

"""
Class for filter
"""
class filter_type_enum(Enum):
    EQUALS = "EQUALS"
    LIKE = "LIKE" 

    @classmethod
    def from_string(cls, value: str) -> "filter_type_enum":
        """Method for getting type"""
        try:
            return cls(value.strip().upper())
        except:
            raise not_exist_exception("value don't exist in enum")
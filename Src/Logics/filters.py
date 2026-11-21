from Src.Dtos.filter_type_dto import filter_type_enum
from Src.Core.abstract_filter import abstract_filter

"""
Class for strict filtration
"""
class equals_filter(abstract_filter):
    def match(self, actual: str, expected: str) -> bool:
        return actual == expected

"""
Class for filter by entry
"""    
class like_filter(abstract_filter):
    def match(self, actual: str, expected: str) -> bool:
        return expected in actual
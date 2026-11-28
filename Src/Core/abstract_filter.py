from abc import ABC, abstractmethod

"""
Abstract class for filter
"""
class abstract_filter(ABC):
    @abstractmethod
    def match(self, actual: str, expected: str) -> bool:
        ...

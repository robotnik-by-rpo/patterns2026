from abc import ABC, abstractmethod

"""
Abstract class for observer's subscriber 
"""
class abstract_observation(ABC):
    @abstractmethod
    def handler(self, event_types: str, params: object) -> None:
        ...
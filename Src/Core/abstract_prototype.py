from abc import ABC, abstractmethod
from Src.Dtos.filter_dto import filter_dto
"""
Abstract class for prototypes
"""
class abstract_prototype(ABC):
    __data: list = []
    
    def __init__(self, data: list | None = None):
        self.__data = list(data) if data is not None else []

    @abstractmethod
    def clone(self, filter_dto: filter_dto = None) -> "abstract_prototype":
        ...
        
    @property
    def data(self) -> list:
        """Getter for data"""
        return self.__data
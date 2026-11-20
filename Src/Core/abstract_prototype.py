from abc import ABC, abstractmethod
from Src.Dtos.filter_dto import filter_dto
"""
Abstract class for prototypes
"""
class abstract_prototype(ABC):
    __data: list = []
    
    @abstractmethod
    def clone(self, filter_dto: filter_dto = None) -> "abstract_prototype":
        ...
        
    @property
    def data(self) -> list:
        """Getter for data"""
        return self.__data
    
    @data.setter
    def data(self, new_data: list) -> None:
        """Setter for data"""
        self.__data = new_data
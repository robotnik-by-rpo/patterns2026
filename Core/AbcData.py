from abc import ABC, abstractmethod
import uuid

class unit(ABC):
    @abstractmethod
    def __init__(self):
        """init attribute"""
        self.__id = uuid.uuid4()
        self.__name = ""

    @abstractmethod
    def get_id(self) -> uuid.UUID:
        """Method for getting id"""
        return self.__id

    @abstractmethod
    def get_name(self)->str:
        """Method for getting name"""
        return self.__name

    @abstractmethod
    def set_name(self, new_name: str)->None:
        """Method for setting new name"""
        if new_name is not None and new_name:
            self.__name = new_name
        else:
            raise ValueError("Empty name")

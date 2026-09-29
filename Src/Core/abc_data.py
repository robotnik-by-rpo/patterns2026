from abc import ABC
import uuid
from Src.Core.exception import arguments_exception
class unit(ABC):

    def __init__(self):
        """init attribute"""
        self.__id = uuid.uuid4().hex
        self.__name = ""

    @property
    def id(self) -> str:
        """Method for getting id"""
        return self.__id
    
    @id.setter
    def id(self,new_id: str) -> None:
        if new_id is not None and new_id:
            self.__id = new_id
        else:
            raise arguments_exception(new_id,"Empty id")

    @property
    def name(self)->str:
        """Method for getting name"""
        return self.__name

    @name.setter
    def name(self, new_name: str)->None:
        """Method for setting new name"""
        if new_name is not None and new_name:
            self.__name = new_name
        else:
            raise arguments_exception(new_name,"Empty name")

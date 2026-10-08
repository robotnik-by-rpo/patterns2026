from abc import ABC
import uuid
from Src.Core.exception import arguments_exception
from Src.Core.validate import validate
class unit(ABC):
    """abstract class for other classes. Class has id and name"""
    def __init__(self):
        """init attribute"""
        self.id = uuid.uuid4().hex
        self.__name = ""

    @property
    def id(self) -> str:
        """Method for getting id"""
        return self.__id
    
    @id.setter
    def id(self,new_id: str) -> None:
        """Getter for id"""
        self.__id = validate.validated_null_empty_obj(new_id,
                                                      "Empty id",
                                                      "New id must be not None or empty value",
                                                      arguments_exception)

    @property
    def name(self)->str:
        """Method for getting name"""
        return self.__name

    @name.setter
    def name(self, new_name: str)->None:
        """Method for setting new name"""
        self.__name = validate.validated_null_empty_obj(new_name,
                                                        "Empty name",
                                                        "New name be not None or empty value",
                                                        arguments_exception)

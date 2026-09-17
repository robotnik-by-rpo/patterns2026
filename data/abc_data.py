from abc import ABC
import uuid

class Unit(ABC):
    def __init__(self, name):
        """
            __id: UUID
            __name: str
        """
        self.__id = uuid.uuid4()
        self.__name = name

    def get_id(self):
        """ 
            Method for getting id
            Return:
                __id: uuid4
        """
        return self.__id

    def get_name(self):
        """
            Method for getting name

            Return:
                __name: str    
        """
        return self.__name

    def set_name(self, new_name):
        """
            Method for setting new name

            Args: 
                - new_name: str
                  This variable for init new name for attribute
            Return: None    
        """
        if new_name is not None and new_name:
            self.__name = new_name
        else:
            raise ValueError("Empty name")

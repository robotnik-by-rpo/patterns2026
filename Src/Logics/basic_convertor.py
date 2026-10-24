from Src.Core.abstract_convert import abstract_convertor
from typing import Callable
from Src.Core.exception import not_exist_exception

"""
Convertor for basic objects in Python
"""
class basic_convertor(abstract_convertor):
    __mapping: dict[type, Callable[[any], dict]] = {}

    def __init__(self):
        self.__mapping[str] = self.__convert_str
        self.__mapping[int] = self.__convert_int
        self.__mapping[float] = self.__convert_float
        self.__mapping[bool] = self.__convert_bool

    def convert(self, object: str | float | int) -> dict:
        """Convert basic types into dict"""
        type_object = type(object)
        if type_object in self.__mapping:
            return self.__mapping[type_object](object) 
        raise not_exist_exception("type of object", "type of object must be exist")

    def __convert_str(self, object: str) -> dict:
        """Convert str object into dict"""
        return {"line": object}

    def __convert_int(self, object: int) -> dict:
        """Convert int object into dict"""
        return {"value_integer": object}
    
    def __convert_float(self, object: float) -> dict:
        """Convert float object into dict"""
        return {"value_float": object}
    
    def __convert_bool(self, object: bool) -> dict:
        """Convert bool object into dict"""
        return {"value_bool": object}
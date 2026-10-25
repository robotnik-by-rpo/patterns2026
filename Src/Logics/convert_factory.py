from datetime import datetime
from typing import  Callable

from Src.Core.abc_data import unit
from Src.Core.exception import not_exist_exception
from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.Logics.reference_convertor import reference_convertor

"""
Factory for convertor
"""
class convert_factory:

    __mapping: dict[type, Callable[[any], any]] = {}

    def __init__(self) -> None:
        self.__basic = basic_convertor()
        self.__datetime = datetime_convertor()
        self.__reference = reference_convertor(self.convert)    
        self.__init_mapping()

    def __init_mapping(self)->None:
        """Initing mapping"""
        self.__mapping[bool] = self.__basic.convert
        self.__mapping[str] = self.__basic.convert
        self.__mapping[int] = self.__basic.convert
        self.__mapping[float] = self.__basic.convert
        self.__mapping[datetime] = self.__datetime.convert
        self.__mapping[unit] = self.__convert_unit
        self.__mapping[list] = self.__convert_container
        self.__mapping[set] = self.__convert_container
        self.__mapping[tuple] = self.__convert_container
        self.__mapping[dict] = self.__convert_dict

    def __convert_container(self, object: list | tuple | set) -> list:
        """Converting items from container"""
        return [self.convert(item) for item in object]
    
    def __convert_dict(self, object: dict) -> dict:
        """Converting items from dict"""
        return {key: self.convert(value) for key, value in object.items()}

    def convert(self, object: any) -> any:
        """Method for converting object"""
        if object is None:
            return None

        type_object = type(object)
        if type_object in self.__mapping:
            return self.__mapping[type_object](object)

        if hasattr(object, "__dict__") and not callable(object):
            return self.__reference.convert(object)

        raise not_exist_exception(
            "type convert",
            f"unsupported type: {type(object).__name__}"
        )
    
    def __convert_unit(self, object: unit) -> dict:
        """Delegate unit-model conversion to reference_convertor"""
        return self.__reference.convert(object)
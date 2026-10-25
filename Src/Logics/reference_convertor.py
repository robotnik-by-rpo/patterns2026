import inspect
from enum import Enum
from typing import Callable

from Src.Core.abstract_convert import abstract_convertor
from Src.Core.exception import not_exist_exception

"""
Reflects public fields of an object and converts each via
an externally provided field convertor
"""
class reference_convertor(abstract_convertor):
    __field_convertor: Callable[[any], any]
    __mapping_field: dict = {}

    def __init__(self, field_convertor: Callable[[any], any]) -> None:
        self.__field_convertor = field_convertor
        self.__init_mapping()

    def __init_mapping(self) -> None:
        """Method for initing mapping"""
        self.__mapping_field[bool] =  self.__get_field_basic_field
        self.__mapping_field[int] = self.__get_field_basic_field
        self.__mapping_field[float] = self.__get_field_basic_field
        self.__mapping_field[str] = self.__get_field_basic_field
        self.__mapping_field[dict] = self.__get_field_dict
        self.__mapping_field[list] = self.__get_field_container
        self.__mapping_field[tuple] = self.__get_field_container
        self.__mapping_field[set] = self.__get_field_container

    def convert(self, object: any) -> dict:
        """convert any object from project"""
        if not hasattr(object, "__dict__") or callable(object):
            raise not_exist_exception(
                "type of object",
                f"unsupported type: {type(object).__name__}"
            )
        return self.__convert_object(object)

    def __convert_object(self, object: any) -> dict:
        """Method for getting fields and creating dict"""
        fields = self.__collect_fields(object)
        return {name: self.__convert_field(value) for name, value in fields.items()}

    def __get_field_basic_field(self, value: bool | str | int | float) -> any:
        """Convert value base object in Python"""
        return value
    
    def __get_field_container(self, value: list | tuple | set) -> list:
        """Convert items from container"""
        return [self.__convert_field(item) for item in value]
    
    def __get_field_dict(self, value: dict) -> dict:
        """Convert items from dict"""
        return {key: self.__convert_field(item) for key, item in value.items()}

    def __convert_field(self, value: any) -> any:
        """Method for flat conversion: scalars stay scalars, composite -> factory."""
        if value is None:
            return None
        
        if isinstance(value, Enum):
            return value.value
        
        type_value = type(value)

        if type_value in self.__mapping_field:
            return self.__mapping_field[type_value](value)

        return self.__field_convertor(value)

    def __collect_fields(self, object: any) -> dict[str, any]:
        """Method for collecting fields object"""
        names: set[str] = set()
        for name in vars(object):
            if not name.startswith("_"):
                names.add(name)
        for name, member in inspect.getmembers(type(object)):
            if isinstance(member, property) and not name.startswith("_"):
                names.add(name)

        fields: dict[str, any] = {}
        for name in names:
            try:
                value = getattr(object, name)
            except Exception:
                continue
            if callable(value):
                continue
            fields[name] = value
        return fields
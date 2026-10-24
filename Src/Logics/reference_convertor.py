from Src.Core.abstract_convert import abstract_convertor
from Src.Core.exception import not_exist_exception
from Src.Logics.datetime_convertor import datetime_convertor

import inspect
from enum import Enum
from datetime import datetime
from Src.Logics.basic_convertor import basic_convertor
from Src.Core.abc_data import unit


"""
Convertor for DIY classes in project
"""
class reference_convertor(abstract_convertor):
    
    __basic: basic_convertor
    __datetime: datetime_convertor

    def __init__(self):
      self.__basic = basic_convertor()
      self.__datetime = datetime_convertor()

    def convert(self, object: any) -> dict:
       """Public method for converting any object"""
       return self.__convert_any(object)
    
    def __convert_any(self, object: any) -> any:
        """Method for converting any object"""
        if object is None:
           return None
        
        if isinstance(object, (str, int, float, bool)):
            return self.__basic.convert(object)

        if isinstance(object, datetime):
            return self.__datetime.convert(object)
        
        if isinstance(object, Enum):
            return object.value
        
        if isinstance(object, (list, tuple, set)):
            return [self.__convert_any(item) for item in object]
        
        if isinstance(object, dict):
            return {key: self.__convert_any(value) for key, value in object.items()}
        
        if isinstance(object, unit):
            return self.__convert_unit_type(object)
        
        if hasattr(object, "__dict__") and not callable(object):
            return self.__convert_object(object)

        raise not_exist_exception(
            "type of object",
            f"unsupported type: {type(object).__name__}"
        )
    

    def __convert_unit_type(self, object: unit) -> dict:
        """Convert a unit-based model into a dict of public fields"""
        fields = self.__collect_fields(object)
        result = {}
        for name, value in fields.items():
            result[name] = self.__convert_field(value)
        return result

    def __collect_fields(self, object: unit) -> dict:
        """Collect public fields of object"""
        type_object = type(object)
        names = set()
        for name in vars(object):
            if not name.startswith("_"):
                names.add(name)

        for name, member in inspect.getmembers(type_object):
            if isinstance(member, property) and not name.startswith("_"):
                names.add(name)
        
        fields = {}

        for name in names:
            try:
                value = getattr(object, name)
            except Exception:
                continue

            if callable(value):
                continue

            fields[name] = value
        return fields

    def __convert_field(self, value: any) -> any:
        """Convert a single field value inside a domain model"""
        if value is None:
            return None

        if isinstance(value, (bool, str, int, float)):
            return value
        
        if isinstance(value, Enum):
            return value.value
        
        if isinstance(value, datetime):
            return self.__datetime.convert(value)
        
        if isinstance(value, (list, tuple, set)):
            return [self.__convert_field(item) for item in value]
        
        if isinstance(value, dict):
            return {k: self.__convert_field(v) for k, v in value.items()}
        
        if isinstance(value, unit):
            return self.__convert_unit_type(value)
        
        raise not_exist_exception(
            "type of field",
            f"unsupported field type: {type(value).__name__}"
        )
    
    def __convert_object(self, obj: any) -> dict:
        """Method for reflect public fields of any object (unit or not)."""
        fields = self.__collect_fields(obj)
        return {name: self.__convert_field(value) for name, value in fields.items()}
from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.reference_convertor import reference_convertor
from  Src.Logics.datetime_convertor import datetime_convertor
from datetime import datetime
from Src.Core.exception import not_exist_exception
from Src.Core.abc_data import unit

"""
Factory for convert any object
"""
class convert_factory:

    __basic_convertor: basic_convertor = None
    __reference_convertor: reference_convertor = None
    __datetime_convertor: datetime_convertor = None

    def __init__(self):
        self.__init__convertors()

    def __init__convertors(self):
        """Method for initing convertors"""
        self.__basic_convertor = basic_convertor()
        self.__reference_convertor = reference_convertor()
        self.__datetime_convertor = datetime_convertor()

    def convert(self, object: any) -> dict:
        """Method for call convert method from convertors"""
        if isinstance(object, (bool, str, int, float)):
            return self.__basic_convertor.convert(object)
        
        if isinstance(object, datetime):
            return self.__datetime_convertor.convert(object)
        
        if isinstance(object, unit):
            return self.__reference_convertor.convert(object)
        
        if isinstance(object, (list, tuple, set)):
            return [self.convert(item) for item in object]

        if isinstance(object, dict):
            return {key: self.convert(value) for key, value in object.items()}

        if hasattr(object, "__dict__") and not callable(object):
            return self.__reference_convertor.convert(object)

        raise not_exist_exception(
            "type convert",
            f"unsupported type: {type(object).__name__}"
        )

from datetime import datetime
from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.Logics.reference_convertor import reference_convertor
from Src.Core.abstract_convert import abstract_convertor
from enum import Enum

"""
Factory for convertors
"""
class convert_factory:

    __mapping: dict[type, abstract_convertor] = {}
    __basic_convertor: basic_convertor = None
    __date_convertor: datetime_convertor = None
    __reference_convertor: reference_convertor = None

    def __init__(self) -> None:
        self.__initing_convertors()
        self.__initing_mapping()

    def __initing_mapping(self)->None:
        """Initing mapping"""
        self.__mapping[bool] = self.__basic_convertor
        self.__mapping[int] = self.__basic_convertor
        self.__mapping[float] = self.__basic_convertor
        self.__mapping[str] = self.__basic_convertor
        self.__mapping[datetime] = self.__date_convertor

    def __initing_convertors(self) -> None:
        """Initing convertors"""
        self.__basic_convertor = basic_convertor()
        self.__date_convertor = datetime_convertor()
        self.__reference_convertor = reference_convertor()

    def convert(self, obj: any) -> any:
        """Method for converting objects"""
        if obj is None:
            return None

        if isinstance(obj, Enum):
            return obj.value
        
        if isinstance(obj, (list, tuple, set)):
            return [self.convert(i) for i in obj]
        
        if isinstance(obj, dict):
            return {k: self.convert(v) for k, v in obj.items()}

        conv = self.__mapping.get(type(obj))
        if conv is not None:
            return conv.convert(obj)
        
        raw = self.__reference_convertor.convert(obj)
        return {name: self.convert(value) for name, value in raw.items()}

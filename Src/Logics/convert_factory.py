from datetime import datetime
from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.Logics.reference_convertor import reference_convertor
from Src.Core.abstract_convert import abstract_convertor
from enum import Enum

from Src.Core.exception import not_exist_exception

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

    def get_serializer(self, obj: any) -> abstract_convertor:
        """Getting convertor for serialize"""
        conv = self.__mapping.get(type(obj))
        if conv is not None:
            return conv
        if self.__reference_convertor.can_serialize(obj):
            return self.__reference_convertor
        raise not_exist_exception(
            "type of object",
            f"type of object is unsupported {type(obj).__name__}"
        )

    def get_deserializer(self, obj: any) -> abstract_convertor:
        """Getting convertor for deserialization"""
        conv = self.__mapping.get(type(obj))
        if conv is not None:
            return conv
        
        if self.__reference_convertor.can_deserialize(obj):
            return self.__reference_convertor
        
        if self.__date_convertor.can_deserialize(obj):
            return self.__date_convertor

        raise not_exist_exception(
            "type of object",
            f"type of object is unsupported {type(obj).__name__}"        )

    def convert(self, obj: any) -> any:
        """Method for converting objects"""
        return self.serialize(obj)

    def serialize(self, obj: any) -> any:
        "Method for serilizing classes"
        if obj is None:
            return None
        
        if isinstance(obj, Enum):
            return obj.value
        
        if isinstance(obj, (list, tuple, set)):
            return [self.serialize(i) for i in obj]
        
        if isinstance(obj, dict):
            return {k: self.serialize(v) for k, v in obj.items()}

        conv = self.get_serializer(obj)
        raw = conv.serialize(obj)

        if isinstance(raw, dict):
            return {k: self.serialize(v) for k, v in raw.items()}
        
        return raw

    def deserialize(self, obj: dict) -> any:
        "Method for deserilizing classes"

        if isinstance(obj, (list, tuple, set)):
            return [self.deserialize(i) for i in obj]
        
        if not isinstance(obj, dict):
            return obj

        try:
            conv = self.get_deserializer(obj)
        except not_exist_exception:
            return {k: self.deserialize(v) for k, v in obj.items()}

        prepared = {
            k: self.deserialize(v)
            for k, v in obj.items()
            if k != "__class__"
        }

        if "__class__" in obj:
            prepared["__class__"] = obj["__class__"]
        return conv.deserialize(prepared)

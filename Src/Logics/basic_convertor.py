from Src.Core.abstract_convert import abstract_convertor
from Src.Core.exception import not_exist_exception


"""
Convertor for basic objects in Python
"""
class basic_convertor(abstract_convertor):
    def serialize(self, obj: any) -> any:
        """Method for returning basic value"""
        if isinstance(obj, (bool, int, float, str)):
            return obj
        raise not_exist_exception("type of object" ,f"type of object is unsupported {type(obj).__name__}")
    
    def deserialize(self, object: dict) -> any:
        """Method for deserializing"""
        return object
    
    def can_serialize(self, object: any) -> bool:
        """Method for check possibility for serialize"""
        return isinstance(object, (bool, int, float, str))

    def can_deserialize(self, object: any) -> bool:
        """Method for check possibility for deserialize"""
        return isinstance(object, (bool, int, float, str))
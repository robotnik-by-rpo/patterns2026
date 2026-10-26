from Src.Core.abstract_convert import abstract_convertor
from Src.Core.exception import not_exist_exception

"""
Convertor for basic objects in Python
"""
class basic_convertor(abstract_convertor):
    def convert(self, obj: any) -> any:
        """Method for returning basic value"""
        if isinstance(obj, (bool, int, float, str)):
            return obj
        raise not_exist_exception("type of object" ,f"type of object is unsupported {type(obj).__name__}")
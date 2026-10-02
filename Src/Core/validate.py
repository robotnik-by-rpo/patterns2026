from typing import TypeVar, Type
from Src.Core.exception import arguments_exception
T = TypeVar("T", bound=arguments_exception)

class validate():
    @staticmethod
    def validated_name( obj:str, 
                        size: int,
                        value: str,
                        error: type[T]) -> str:
        """Check, name on lenght and type"""
        if obj is None or not obj:
            raise error(value, f"{value} mustn't be empty or None")

        if len(obj) > size or type(obj) != str :
            raise error(value, f"{value} must be shorter than {size} letters")
        return obj

    @staticmethod
    def validated_null_empty_str(obj: str,
                                 value: str,
                                 msg: str,
                                 error: type[T]) -> str:
        """Check line for None value and empty line"""
        if obj is None or not obj:
            raise error(value, msg)
        return obj 
    
    @staticmethod
    def validated_filename_settings(filename: str, 
                                    value: str, 
                                    msg: str, 
                                    error: type[T])->str:
        """Check filename on correct form"""
        if filename is None or "." not in filename or filename.split('.')[1]!="json" or not filename:
            raise error(value, msg)
        return filename
    
    @staticmethod
    def validated_null_value(obj: any, 
                             value: str, 
                             msg: str,
                             error: type[T])->any:
        """Check object on None value"""
        if obj is None:
            raise error(value, msg)
        return obj
    
    @staticmethod
    def validated_value_exist(key: str, 
                              types: dict[str,bool], 
                              value: str, 
                              msg: str,
                              error: type[T]) -> str:
        """Check key on existing"""
        if not types.get(key,False):
            raise error(value, msg)
        return key
    
    @staticmethod
    def validated_certain_size(unique_code: str, 
                               size: int, 
                               name_code:str,
                               error: type[T]) -> str:
        """Check unique code, which have size"""
        if unique_code is not None:
            len_inn = len(unique_code)
            if (len_inn < size or len_inn > size):
                raise error(name_code, f"{name_code} must have correct lenght")
        else: 
            raise error(name_code, f"{name_code} must be exist")

        return unique_code    

    @staticmethod
    def validated_null_and_zero_value(num: int, 
                                      value: str, 
                                      msg: str,
                                      error: type[T]) -> int:
        """Check zero and null value"""
        if num is None or num <= 0:
            raise error(value, msg)
        return num
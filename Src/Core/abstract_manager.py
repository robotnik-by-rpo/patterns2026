from abc import ABC
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception

"""
Abstract class for init uploading and processing
"""
class abstract_manager(ABC):
    # Full path to file
    __file_name: str = ""
    # Flag. Uploaded - data is ready
    __is_loaded: bool = False
    # 
    __data: dict = {}


    """Uploading data"""
    def load(self, file_name:str = "") -> None:
        ...

    """Processing upload data"""
    def convert(self) -> bool:
        return len(self.__data) != 0
    
    """Flag. Data is ready"""
    @property
    def is_loaded(self) -> bool:
        """Getter for flag"""
        return self.__is_loaded
    
    @is_loaded.setter
    def is_loaded(self, new_flag: bool) -> None:
        """Setter for flag"""
        self.__is_loaded = validate.validated_type(validate.validated_null_value(new_flag,
                                                         "new flag",
                                                         "flag must be not None value",
                                                         arguments_exception),
                                                         bool,
                                                         "new flag",
                                                         "flag must be bool type",
                                                         arguments_exception)

    @property
    def data(self)->dict:
        """Getter for data"""
        return self.__data
    
    @data.setter
    def data(self, new_data:dict)->None:
        """Setter for data"""
        self.__data = validate.validated_type(validate.validated_null_value(new_data,
                                                    "data",
                                                    "data must be not None value",
                                                    arguments_exception),
                                                    dict,
                                                    "data",
                                                    "data must be dict type",
                                                    arguments_exception)
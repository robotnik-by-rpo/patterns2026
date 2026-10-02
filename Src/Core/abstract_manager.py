from abc import ABC

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
        return self.__is_loaded
    
    @is_loaded.setter
    def is_loaded(self, new_flag: bool) -> None:
        self.__is_loaded = new_flag

    @property
    def data(self)->dict:
        return self.__data
    
    @data.setter
    def data(self, new_data)->None:
        self.__data = new_data
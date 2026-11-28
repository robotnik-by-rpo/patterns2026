from Src.Dtos.filter_type_dto import filter_type_enum
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception

"""
Class for condition
"""
class filter_item_dto:
    __field_name: str = ""
    __filter_type: filter_type_enum = filter_type_enum.EQUALS
    __value: str = ""

    @property
    def field_name(self) -> str:
        """Getter for field name"""
        return self.__field_name
    
    @field_name.setter
    def field_name(self, value: str) -> None:
        """Setter for field name"""
        self.__field_name = value.strip()

    @property
    def filter_type(self) -> filter_type_enum:
        """Getter for filter type"""
        return self.__filter_type
    
    @filter_type.setter
    def filter_type(self, new_value: str | filter_type_enum) -> None:
        """Setter for filter type"""
        if isinstance(new_value, str):
            self.__filter_type = filter_type_enum.from_string(new_value)
        else:
            self.__filter_type = new_value
        
    @property
    def value(self) -> str:
        """Getter for value"""
        return self.__value
    
    @value.setter
    def value(self, value: str) -> None:
        """Setter for value"""
        validate.validated_type(value, 
                                str, 
                                "new value",
                                "new value must be str", 
                                arguments_exception)
        self.__value = value.strip()

"""
Class container for filter_item_dto
"""
class filter_dto:
    __filters: list[filter_item_dto] = []

    @property
    def filters(self) -> list[filter_item_dto]:
        """Getter for filters"""
        return self.__filters
    
    @filters.setter
    def filters(self, value: list[filter_item_dto]):
        """Setter for filters"""
        self.__filters = value
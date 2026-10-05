from Src.Core.abc_data import unit
from Src.Models.organization_model import organization_model
from Src.Core.exception import arguments_exception
from Src.Core.validate import validate

class settings_model(unit):
    """Settings from json file"""
    # Information about company
    __company: organization_model = None
    __boss_name: str = ""
    __accounter_name: str = ""
    __is_first: bool = True

    @property
    def company(self)->organization_model:
        """Getter for company"""
        return self.__company
    
    @company.setter
    def company(self, new_company: organization_model) -> None:
        """Setter for company"""
        self.__company = validate.validated_null_value(new_company,
                                                     "company in settings",
                                                     "company must be not None value",
                                                     arguments_exception)

    @property
    def boss_name(self) -> str:
        """Getter for boss name"""
        return self.__boss_name
   
    @boss_name.setter
    def boss_name(self, new_name)->None:
        """Setter for boss name"""
        self.__boss_name = validate.validated_null_empty_str(new_name,
                                                        "boss name",
                                                        "boss name must be not empty line",
                                                        arguments_exception)

    @property
    def accounter_name(self) -> str:
        """Getter for accounter name"""
        return self.__accounter_name
    
    @accounter_name.setter
    def accounter_name(self, new_name: str) -> None:
        """Setter for accounter name"""
        self.__accounter_name = validate.validated_null_empty_str(new_name,
                                                        "accounter name",
                                                        "accounter name must be not empty line",
                                                        arguments_exception)

    @property    
    def is_first(self)->bool:
        """Getter for flag is_first"""
        return self.__is_first
    
    @is_first.setter
    def is_first(self, new_flag:bool)->None:
        """Setter for flag is_first"""
        self.__is_first = new_flag
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
    __response_format: str = "TXT"

    __EXIST_FORMAT: dict[str, bool] = {
        "CSV": True,
        "Markdown": True,
        "MD": True,          
        "XML": True,
        "TXT": True,
        "HTML": True,
    }

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
        self.__boss_name = validate.validated_null_empty_obj(new_name,
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
        self.__accounter_name = validate.validated_null_empty_obj(new_name,
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

    @property
    def response_format(self) -> str:
        """Getter for response format"""
        return self.__response_format

    @response_format.setter
    def response_format(self, new_format: str) -> None:
        """Setter for response format"""
        self.__response_format = validate.validated_value_exist(
            new_format,
            self.__EXIST_FORMAT,
            "response format",
            "response format must be one of: CSV, Markdown, XML, TXT, HTML",
            arguments_exception
        )
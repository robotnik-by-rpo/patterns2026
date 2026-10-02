from Src.Core.abc_data import unit
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception

class building_model(unit):
    """It's common class for all buildings in the system"""
    __square: float = 0
    __address: str = ""
    __base_unit: unit_of_measurement_model = None
    def __init__(self, name: str, square: float, base_unit: unit_of_measurement_model, address: str):
        super().__init__()
        self.name = name
        self.__square = validate.validated_null_and_zero_value(square,
                                                               "square", 
                                                               "square must be bigger than 0",
                                                               arguments_exception)
        self.__base_unit = validate.validated_null_value(base_unit,
                                                         "unit of measurement of square", 
                                                         "square must have unit of measurement",
                                                         arguments_exception)
        self.__address = validate.validated_null_empty_str(address,
                                                           "address",
                                                           "address mustn't be empty",
                                                           arguments_exception)
        
    @property
    def square(self) ->float:
        """Getting square of building"""
        return self.__square
    
    @square.setter
    def square(self, new_square: float)->None:
        """Setting new square of building"""
        self.__square = validate.validated_null_and_zero_value(new_square,
                                                               "square", 
                                                               "square must be bigger than 0",
                                                               arguments_exception)

    @property
    def base_unit(self) -> unit_of_measurement_model:
        """Getting base unit of measurement for square"""
        return self.__base_unit
    
    @base_unit.setter
    def base_unit(self, new_base_unit: unit_of_measurement_model)->None:
        """Setting base unit of measurement for square"""
        self.__base_unit = validate.validated_null_value(new_base_unit,
                                                         "unit of measurement of square", 
                                                         "square must have unit of measurement",
                                                         arguments_exception)
    @property
    def address(self)->str:
        """Getting address of building"""
        return self.__address
    
    @address.setter
    def address(self, new_address:str)->None:
        """Setting adddress of building"""
        self.__address = validate.validated_null_empty_str(new_address,
                                                           "address",
                                                           "address mustn't be empty",
                                                           arguments_exception)


 
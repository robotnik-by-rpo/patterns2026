from Src.Core.abc_data import unit
from Src.Core.exception import arguments_exception
from Src.Models.unit_of_measurement_model import unit_of_measurement_model

class building_model(unit):
    """It's common class for all buildings in the system"""
    __square: float = 0
    __address: str = ""
    __base_unit: unit_of_measurement_model = None
    def __init__(self, name: str, square: float, base_unit: unit_of_measurement_model, address: str):
        super().__init__()
        self.name = name
        self.__square = self.__validated_zero_square(square)
        self.__base_unit = self.__validated_not_null_base_unit(base_unit)
        self.__address = self.__validated_empty_address(address)

    def __validated_zero_square(self, square: float) -> float:
        """Method for validating zero value and None value"""
        if square is None or square <= 0:
            raise arguments_exception("square", "square must be bigger than 0")

        return square
    
    def __validated_not_null_base_unit(self, 
                                       base_unit: unit_of_measurement_model) -> unit_of_measurement_model:
        """Method for validating None value for base unit"""
        if base_unit is None:
            raise arguments_exception("unit of measurement of square", "square must have unit of measurement")
        
        return base_unit

    def __validated_empty_address(self, address: str) -> str:
        """Method for validating empty string for address"""
        if address is None or not address:
            raise arguments_exception("address","address mustn't be empty")
        
        return address

    @property
    def square(self) ->float:
        """Getting square of building"""
        return self.__square
    
    @square.setter
    def square(self, new_square: float)->None:
        """Setting new square of building"""
        self.__square = self.__validated_zero_square(new_square)

    @property
    def base_unit(self) -> unit_of_measurement_model:
        """Getting base unit of measurement for square"""
        return self.__base_unit
    
    @base_unit.setter
    def base_unit(self, new_base_unit: unit_of_measurement_model)->None:
        """Setting base unit of measurement for square"""
        self.__base_unit = self.__validated_not_null_base_unit(new_base_unit)

    @property
    def address(self)->str:
        """Getting address of building"""
        return self.__address
    
    @address.setter
    def address(self, new_address:str)->None:
        """Setting adddress of building"""
        self.__address = self.__validated_empty_address(new_address)


 
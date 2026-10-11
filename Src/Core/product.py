from Src.Core.abc_data import unit
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception
from Src.Core.exception import operation_exception
from Src.Models.unit_of_measurement_model import unit_of_measurement_model

"""class for init product"""
class product(unit):
    __brand: str = ""
    __unit: unit_of_measurement_model = None
    __brutto: float = None
    __netto: float = 0.0
    __waste: float = 0.0

    def __calc_netto(self):
        """Method for calculating netto"""
        return self.brutto *((100-self.__waste)/100)

    @property
    def brand(self) -> str:
        """Getter for brand"""
        return self.__brand
    
    @brand.setter
    def brand(self, new_brand: str) -> None:
        """Setter for brand"""
        self.__brand = validate.validated_null_empty_obj(new_brand,
                                                         "brand",
                                                         "brand must be not None or zero value",
                                                         arguments_exception)
    @property
    def unit(self) -> unit_of_measurement_model:
        """Getter for unit"""
        return self.__unit
    
    @unit.setter
    def unit(self, new_unit: unit_of_measurement_model) -> None:
        """Setter for unit"""
        self.__unit = validate.validated_null_value(new_unit,
                                                    "new unit",
                                                    "new unit must be not None value",
                                                    arguments_exception)


    @property
    def brutto(self) -> float:
        """Getter for brutto"""
        return self.__brutto
    
    @brutto.setter
    def brutto(self, new_brutto: float) -> None:
        """Setter for brutto"""

        new_brutto = validate.validated_null_value(new_brutto,
                                                   "new brutto",
                                                    "new brutto must be not None",
                                                    arguments_exception)
        self.__brutto = validate.validated_positive_value(new_brutto,
                                                        "new brutto",
                                                        "new brutto must be not None and not zero value",
                                                        arguments_exception)
        self.__netto = validate.validated_positive_value(self.__calc_netto(),
                                                             "new netto",
                                                             "new netto must be bigger than 0",
                                                             operation_exception)

    @property
    def netto(self) -> float:
        """Getter for netto"""
        return self.__netto
    
    @property
    def waste(self) -> float:
        """Getter for waste"""
        return self.__waste
    
    @waste.setter
    def waste(self, new_waste: float) -> None:
        """Setter for waste"""
        new_waste = validate.validated_null_value(new_waste,
                                                  "new waste",
                                                  "new waste must be None value",
                                                  arguments_exception)
        self.__waste = validate.validated_rangу_values(new_waste, 
                                                       0, 
                                                       100, 
                                                       "new waste", 
                                                       "new waste must be enter the gap [0;100]",
                                                       arguments_exception)
        if self.brutto is None:
            raise operation_exception("brutto","Brutto must be not None value")
        self.__netto = validate.validated_positive_value(self.__calc_netto(),
                                                        "netto",
                                                        "netto must be bigger than 0",
                                                        operation_exception)
        
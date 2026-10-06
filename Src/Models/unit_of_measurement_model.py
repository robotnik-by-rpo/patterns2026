from Src.Core.abc_data import unit
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception

class unit_of_measurement_model(unit):
    """It's class for implementation unit of measurement model"""

    __coef: int
    __base: "unit_of_measurement_model" = None

    def __init__(self,name: str, k: int=1, base: "unit_of_measurement_model"=None):
        super().__init__()
        self.name = name
        self.coef = k
        self.__base = base

    @property
    def base(self)->"unit_of_measurement_model":
        """Getting base unit of measurement"""
        return self.__base
    
    @base.setter
    def base(self, value: "unit_of_measurement_model")->None:
        """Setting base unit of measurement"""
        self.__base = value

    @property
    def coef(self)->int:
        """Getting coeffcient"""
        return self.__coef
    
    @coef.setter
    def coef(self, value: int)->None:
        """Setting coefficient"""
        self.__coef = validate.validated_null_and_zero_value(value,
                                                             "coefficient", 
                                                             "Coefficient must be bigger 0",
                                                             arguments_exception)

    @property
    def common_coef(self) -> int:
        """Getting coefficient"""
        if self.__base is None:
            return self.coef
        return self.coef * self.__base.common_coef
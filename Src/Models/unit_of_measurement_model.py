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
    
    @classmethod
    def create_kg(cls) -> "unit_of_measurement_model":
        """Factory method for creating kilogram"""
        return cls("kilogram", 1000, cls.create_g())
    
    @classmethod
    def create_g(cls) -> "unit_of_measurement_model":
        """Factory method for creating gram"""
        return cls("gram",1)
    
    @classmethod
    def create_ton(cls) -> "unit_of_measurement_model":
        "Factory method for creating ton"
        return cls("ton",1000,cls.create_kg())
    
    @classmethod
    def create_ml(cls) -> "unit_of_measurement_model":
        "Factory method for creating mililiter"
        return cls("milliliter",1)
    
    @classmethod
    def create_l(cls) -> "unit_of_measurement_model":
        "Factory method for creating liter"
        return cls("liter",1000,cls.create_ml())
    
    @classmethod
    def create_m3(cls) -> "unit_of_measurement_model":
        "Factory method for creating cuber meter"
        return cls("cubic meter",1000,cls.create_l())
    
    @classmethod
    def create_mm2(cls) -> "unit_of_measurement_model":
        "Factory method for creating square milimeter"
        return cls("square millimeter",1)
    
    @classmethod
    def create_sm2(cls) -> "unit_of_measurement_model":
        "Factory method for creating square centimeter"
        return cls("square centimeter",100,cls.create_mm2())
    
    @classmethod
    def create_m2(cls) -> "unit_of_measurement_model":
        "Factory method for creating square meter"
        return cls("square meter",10000,cls.create_sm2())
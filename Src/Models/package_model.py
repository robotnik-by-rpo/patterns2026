from Src.Core.abc_data import unit
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception

"""Class for package"""
class package_model(unit):
    __TYPE_PACKAGE: dict[str, True] = {"box": True,
                                       "film": True,
                                       "paper": True}
    __measure: float #(square or volume)
    __unit: unit_of_measurement_model = None

    def __init__(self, 
                 name: str, 
                 measure: float, 
                 unit: unit_of_measurement_model):
        super().__init__()
        self.name = validate.validated_value_exist(name,
                                                   self.__TYPE_PACKAGE,
                                                   "name",
                                                   "name must be exist",
                                                   arguments_exception)
    
        self.measure = measure
        self.unit = unit
    @property
    def measure(self) -> float:
        """Getter for measure"""
        return self.__measure
    
    @measure.setter
    def measure(self, new_value: float) -> None:
        """Setter for measure"""
        self.__measure = validate.validated_null_and_zero_value(new_value,
                                                               "new measure",
                                                               "new measure must be bigger 0 and not None",
                                                               arguments_exception)
    @property
    def unit(self) -> unit_of_measurement_model:
        """Getter for unit of measurement"""
        return self.__unit
    
    @unit.setter
    def unit(self, new_unit: unit_of_measurement_model) -> None:
        """Setter for unit of measurement"""
        self.__unit = validate.validated_null_value(new_unit,
                                                    "unit of measurement",
                                                    "unit of measurement must be units of square, not None value",
                                                    arguments_exception)
        
    @classmethod
    def create_package_paper(cls):
        """Factory method for creating package paper"""
        return cls("paper",
                   3.5,
                   unit_of_measurement_model.create_l())
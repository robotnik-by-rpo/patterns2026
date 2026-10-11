from Src.Core.product import product
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception


class package_model(product):
    """Class for any package"""

    __TYPE_PACKAGE: dict[str, bool] = {"box": True,
                                       "film": True,
                                       "paper": True}
    __measure: float  # (square or volume)

    def __init__(self,
                 name: str,
                 measure: float,
                 unit: unit_of_measurement_model,
                 brutto: float = 1.0,
                 brand: str = "package"):
        super().__init__()
        self.name = validate.validated_value_exist(
            name,
            self.__TYPE_PACKAGE,
            "name",
            "name must be exist",
            arguments_exception
        )
        self.brand = brand
        self.unit = unit
        self.brutto = brutto
        self.waste = 0.0
        self.measure = measure

    @property
    def measure(self) -> float:
        """Getter for measure"""
        return self.__measure

    @measure.setter
    def measure(self, new_value: float) -> None:
        """Setter for measure"""
        self.__measure = validate.validated_null_and_zero_value(
            new_value,
            "new measure",
            "new measure must be bigger 0 and not None",
            arguments_exception
        )

    @classmethod
    def create_package_paper(cls) -> "package_model":
        """Factory method for creating package paper"""
        return cls("paper",
                   3.5,
                   unit_of_measurement_model.create_l(),
                   3.5)
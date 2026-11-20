from Src.Core.abc_data import unit
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Core.validate import validate
import datetime
from Src.Core.exception import arguments_exception
from Src.Core.abc_data import unit

"""
Class for transactions
"""
class transaction_model(unit):
    __nomenclature: nomenclature_model = None
    __unit: unit_of_measurement_model = None
    __value: float = 0.0
    __period: datetime.datetime = None

    def __init__(self, 
                    name: str,
                    nomenclature: nomenclature_model,
                    unit: unit_of_measurement_model,
                    value: float,
                    period: datetime.datetime):
            super().__init__()
            self.name = name
            self.nomenclature = nomenclature
            self.unit = unit
            self.value = value
            self.period = period

    @property
    def nomenclature(self) -> nomenclature_model:
        """Getter for nomenclature"""
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, source: nomenclature_model) -> None:
        """Setter for nomenclature"""
        self.__nomenclature = validate.validated_null_value(
            source, "nomenclature", "nomenclature must be not None",
            arguments_exception
        )

    @property
    def unit(self) -> unit_of_measurement_model:
        """Getter for unit of measurement"""
        return self.__unit

    @unit.setter
    def unit(self, source: unit_of_measurement_model) -> None:
        """Setter for unit of measurement"""
        self.__unit = validate.validated_null_value(
            source, "unit", "unit must be not None",
            arguments_exception
        )

    @property
    def value(self) -> float:
        """Getter for value"""
        return self.__value

    @value.setter
    def value(self, source: float) -> None:
        """Setter for value"""
        self.__value = validate.validated_null_value(
            source, "value", "value must be not None",
            arguments_exception
        )

    @property
    def period(self) -> datetime.datetime:
        """Getter for period"""
        return self.__period

    @period.setter
    def period(self, source: datetime.datetime) -> None:
        """Setter for period"""
        self.__period = validate.validated_null_value(
            source, "period", "period must be not None",
            arguments_exception
        )
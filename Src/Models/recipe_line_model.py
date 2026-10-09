from Src.Core.validate import validate
from Src.Core.exception import arguments_exception


class recipe_line_model:
    """Line of recipe - component + quantity + share"""

    def __init__(self, component, quantity: float, share: float = 1.0):
        self.component = component
        self.quantity = quantity
        self.share = share

    @property
    def component(self):
        """Getter for component"""
        return self.__component

    @component.setter
    def component(self, new_component) -> None:
        """Setter for component"""
        self.__component = validate.validated_null_value(
            new_component,
            "component",
            "component must be not None",
            arguments_exception
        )

    @property
    def quantity(self) -> float:
        """Getter for quantity"""
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity: float) -> None:
        """Setter for quantity"""
        self.__quantity = validate.validated_null_and_zero_value(
            new_quantity,
            "quantity",
            "quantity must be bigger than zero",
            arguments_exception
        )

    @property
    def share(self) -> float:
        """Getter for share (0 < share <= 1)"""
        return self.__share

    @share.setter
    def share(self, new_share: float) -> None:
        """Setter for share"""
        self.__share = validate.validated_rangу_values(
            new_share,
            0.0001,
            1.0,
            "share",
            "share must be in range (0; 1]",
            arguments_exception
        )

    @property
    def brutto(self) -> float:
        """Брутто строки = брутто компонента * доля"""
        return self.component.brutto * self.share

    @property
    def netto(self) -> float:
        """Нетто строки = нетто компонента * доля"""
        return self.component.netto * self.share
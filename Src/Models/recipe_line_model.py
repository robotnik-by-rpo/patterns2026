from Src.Core.validate import validate
from Src.Core.exception import arguments_exception
from Src.Core.product import product


class recipe_line_model:
    """Line of recipe - component + quantity + share"""

    def __init__(self, component: product, quantity: float, share: float = 1.0):
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
        new_component = validate.validated_null_value(
            new_component,
            "component",
            "component must be not None",
            arguments_exception
        )
        if not hasattr(new_component, "brutto") or not hasattr(new_component, "netto"):
            raise arguments_exception(
                "component",
                "component must have 'brutto' and 'netto' attributes"
            )
        self.__component = new_component

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
        """Brutto line = brutto compoment multiply share
        
        Точка рекурсии: если `component` — это technical_map_model
        (или другой продукт с собственным рецептом), то обращение
        к component.brutto уходит в его рецепт, а тот суммирует
        свои строки — и так далее по дереву.
        """
        if self.__component is None:
            raise arguments_exception(
                "component", "component is not set, cannot calculate brutto"
            )
        return self.__component.brutto * self.share

    @property
    def netto(self) -> float:
        """Netto line = netto compoment multiply share
        
        Рекурсия аналогична методу brutto: см. пояснение выше.
        """
        if self.__component is None:
            raise arguments_exception(
                "component", "component is not set, cannot calculate brutto"
            )
        return self.component.netto * self.share
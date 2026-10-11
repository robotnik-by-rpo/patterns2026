from Src.Core.product import product
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception
from Src.Models.unit_of_measurement_model import unit_of_measurement_model

"""class """
class prepack_model(product):
    __CATEGORY: dict[str:True] = {"А": True,
                                  "Б": True,
                                  "В": True,
                                  "Г": True,
                                  "Д": True}
    __category: str = ""
    
    def __init__(self, 
                 name: str, 
                 brutto: float, 
                 brand: str, 
                 category: str,
                 unit: unit_of_measurement_model,
                 waste: float):
        super().__init__()
        self.name = name
        self.brutto = brutto
        self.brand = brand
        self.category = category
        self.unit = unit
        self.waste = waste
        
    @property
    def category(self) -> str:
        """Getter for category"""
        return self.__category
    
    @category.setter
    def category(self, new_category: str) -> None:
        """Setter for category"""
        self.__category = validate.validated_value_exist(new_category,
                                                        self.__CATEGORY,
                                                        "category",
                                                        "category must be exist",
                                                        arguments_exception)

    @staticmethod
    def create_prepack() -> list[product]:
        """Factory method for creating ingredisent for French baguette"""
        ingredients = []
        names = ["nuggets","dumpligs"]
        bruttos = [200, 200]
        wastes = [20,20]
        g = unit_of_measurement_model.create_g()
        brands = ["The Golden Cockerel","We sculpt and cook"]
        categories = ["А","Б"]
        for n, brutto, w, brand, c in zip(names, bruttos, wastes, brands, categories):
            ingredients.append(prepack_model(n, brutto, brand, c, g, w))
        return ingredients

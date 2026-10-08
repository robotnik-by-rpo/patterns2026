from Src.Core.product import product
from Src.Models.unit_of_measurement_model import unit_of_measurement_model

"""Class for store information about ingredient"""
class ingredient_model(product):

    def __init__(self, 
                 name: str,  
                 brutto: float, 
                 waste: float,
                 brand: str,
                 unit: unit_of_measurement_model):
        super().__init__()
        self.name = name
        self.brutto = brutto
        self.brand = brand
        self.unit = unit
        self.waste = waste

    @staticmethod
    def create_ingredients() -> list[product]:
        """Factory method for creating ingredisent for French baguette"""
        ingredients = []
        names = ["flour","water","yeast","salt"]
        bruttos = [187.5,150,3,3.5]
        wastes = [0,0,0,0]
        brands = ["Makfa","Baical","Saf-Levure","Tchaikovsky"]
        g = unit_of_measurement_model.create_g()
        ml = unit_of_measurement_model.create_ml()
        units = [g, ml, g, g]
        for n, brutto, w, brand, u in zip(names, bruttos, wastes, brands, units):
            ingredients.append(ingredient_model(n, brutto, w, brand,u))
        return ingredients
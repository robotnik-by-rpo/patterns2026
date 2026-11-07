from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.ingredient_model import  ingredient_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.organization_model import organization_model
from Src.Models.package_model import package_model
from Src.Models.prepack_model import prepack_model
from Src.Models.recipe_line_model import recipe_line_model
from Src.Models.settings_model import settings_model
from Src.Models.technical_map_model import technical_map_model
from Src.Models.warehouse_model import  warehouse_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.recipe_model import recipe_model
from Src.Core.building import building 

"""
Registry with domains
"""
class classes_registry:
    __mapping: dict[str, type] = None

    def __new__(cls):
        if not hasattr(cls, '_class_registry__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.__initing_classes()
        return cls.__instance
    
    def __initing_classes(self):
        """Method for initing mapping"""
        self.__mapping = {
            domain.__name__: domain 
            for domain in (
                group_nomenclature_model,
                ingredient_model,
                nomenclature_model,
                organization_model,
                package_model,
                prepack_model,
                recipe_line_model,
                settings_model,
                technical_map_model,
                warehouse_model,
                unit_of_measurement_model,
                recipe_model,
                building)}
        
    def get(self, name: str) -> type | None:
        """Method for getting domain model"""
        return self.__mapping.get(name)
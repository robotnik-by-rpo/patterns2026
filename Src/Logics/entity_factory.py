from Src.Core.abc_data import unit
from Src.Core.exception import not_exist_exception
from Src.Logics.storage_manager import storage_manager
from Src.Models.technical_map_model import technical_map_model

"""
Factory for getting domains by type and identifier
"""
class entity_factory:
    
    __TYPE_ALIASES = {
        "nomenclature": "find_nomenclature",
        "unit": "find_unit",
        "unit_of_measurement": "find_unit",
        "recipe": "find_recipe",
        "tech_map": "find_recipe",
    }

    __tech_map: technical_map_model = None
    def __init__(self):
        self.__storage = storage_manager()
        if self.__tech_map is None:
            self.__tech_map = technical_map_model.create_technical_map()
    
    def create(self, entity_type: str, code: str) -> unit:
        """Method for getting necessary object"""
        method = self.__TYPE_ALIASES.get(entity_type.strip().lower())
        if method is None:
            raise not_exist_exception("entity_type", f"unsupported: {entity_type}")
        return getattr(self.__storage, method)(code)

    
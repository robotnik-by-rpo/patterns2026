from Src.Core.abc_data import unit
from Src.Core.exception import not_exist_exception
from Src.Logics.storage_manager import storage_manager
from Src.Models.technical_map_model import technical_map_model

"""
Factory for getting domains by type and identifier
"""
class entity_factory:
    
    __TYPE_ALIASES = {
        "nomenclature": "nomenclature",
        "unit": "unit",
        "unit_of_measurement": "unit",
        "recipe": "recipe",
        "tech_map": "recipe",
    }

    __tech_map: technical_map_model = None
    def __init__(self):
        self.__storage = storage_manager()
        if self.__tech_map is None:
            self.__tech_map = technical_map_model.create_technical_map()

    def create(self, entity_type: str, code: str) -> unit:
        """Method for getting necessary object"""
        key = self.__TYPE_ALIASES.get(entity_type.strip().lower())
        if key is None:
            raise not_exist_exception(
                "entity_type",
                f"unsupported entity type: {entity_type}"
            )
        finder = getattr(self, f"_find_{key}")
        return finder(code)
    
    def _find_nomenclature(self, code: str) -> unit:
        """Method for finding object nomenclature from storage"""
        for _, items in self.__storage.nomenclatures.items():
            for _, nom in items.items():
                if nom.id == code or nom.name == code:
                    return nom
        raise not_exist_exception("nomenclature", f"not found: {code}")
    
    def _find_unit(self, code: str) -> unit:
        """Method for finding object of unit of measurement from storage"""
        for _, units in self.__storage.units_of_measurement.items():
            for _, u in units.items():
                if u.id == code or u.name == code:
                    return u
        raise not_exist_exception("unit", f"not found: {code}")
    
    def _find_recipe(self, code: str) -> unit:
        """Method for finding object of tech map"""
        if self.__tech_map.id == code or self.__tech_map.name == code:
            return self.__tech_map
        raise not_exist_exception("recipe", f"not found: {code}")

    
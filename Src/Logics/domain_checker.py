from Src.Logics.storage_manager import storage_manager

"""
Class for check object references
"""
class domain_checker:
    __storage: storage_manager = None

    def __new__(cls):
        """Singletone"""
        if not hasattr(cls, '_reference_checker__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.__storage = storage_manager()
        return cls.__instance
    
    def is_referenced(self, target) -> bool:
        """Method for checking object references"""
        target_id = target.id

        def same(obj) -> bool:
            return obj is target or getattr(obj, "id", None) == target_id

        for nom in (n for items in self.__storage.nomenclatures.values()
                    for n in items.values()):
            if same(getattr(nom, "group_of_nomenclature", None)):
                return True
            if same(getattr(nom, "base_unit", None)):
                return True

        for unit in (u for units in self.__storage.units_of_measurement.values()
                     for u in units.values()):
            if same(getattr(unit, "base", None)):
                return True

        for wh in (w for lst in self.__storage.warehouses.values() for w in lst):
            if same(getattr(wh, "warehouse_owner", None)):
                return True
            if same(getattr(wh, "description_of_building", None)):
                return True

        for tm in self.__storage.tech_maps.values():
            if same(getattr(tm, "company", None)):
                return True
            if same(getattr(tm, "package", None)):
                return True
            recipe = getattr(tm, "recipe", None)
            if recipe is not None:
                for line in recipe.lines:
                    if same(getattr(line, "component", None)):
                        return True
        return False

    
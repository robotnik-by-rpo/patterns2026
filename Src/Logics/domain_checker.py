import inspect
from Src.Logics.storage_manager import storage_manager
from Src.Core.abc_data import unit

"""
Class for check object references using reference counting
"""
class domain_checker:
    __storage: storage_manager = None
    __data: dict = {}
    __counts: dict = {}

    def __new__(cls):
        """Singletone"""
        if not hasattr(cls, '_domain_checker__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.__storage = storage_manager()
        return cls.__instance

    def _get_id(self, obj: unit) -> str:
        """Getting id of object"""
        if hasattr(obj, 'id'):
            return obj.id
        return None

    def _get_fields(self, source) -> list[str]:
        """Getting all fields"""
        names = set()
        for name in vars(source):
            if not name.startswith("_"):
                names.add(name)
        for name, member in inspect.getmembers(type(source)):
            if isinstance(member, property) and not name.startswith("_"):
                names.add(name)
        
        ignore = {"id", "name"}
        return list(names - ignore)

    def _registry(self, source) -> None:
        """Recursive registration object and his links"""
        if source is None:
            return
            
        if not isinstance(source, unit):
            return

        code = self._get_id(source)
        if not code:
            return

        if code in self.__data:
            return

        self.__data[code] = source
        self.__counts[code] = 0

        fields = self._get_fields(source)
        for field in fields:
            try:
                value = getattr(source, field, None)
            except Exception:
                continue
                
            if isinstance(value, unit):
                self._registry(value)
                nested_code = self._get_id(value)
                if nested_code in self.__counts:
                    self.__counts[nested_code] += 1
            elif isinstance(value, (list, tuple)):
                for item in value:
                    if isinstance(item, unit):
                        self._registry(item)
                        nested_code = self._get_id(item)
                        if nested_code in self.__counts:
                            self.__counts[nested_code] += 1

    def _rebuild(self) -> None:
        """Full rebuild index on base current stirage_manager"""
        self.__data.clear()
        self.__counts.clear()

        for items in self.__storage.nomenclatures.values():
            for nom in items.values():
                self._registry(nom)
        
        for units in self.__storage.units_of_measurement.values():
            for u in units.values():
                self._registry(u)

        for group in self.__storage.groups_nomenclature.values():
            self._registry(group)

        if self.__storage.company is not None:
            self._registry(self.__storage.company)

        for lst in self.__storage.warehouses.values():
            for wh in lst:
                self._registry(wh)

        for tm in self.__storage.tech_maps.values():
            self._registry(tm)

    def is_referenced(self, target) -> bool:
        """Check if there are references to an object"""
        self._rebuild()
        
        code = self._get_id(target)
        if not code or code not in self.__counts:
            return False
            
        return self.__counts[code] > 0
from Src.Core.exception import arguments_exception, not_exist_exception, operation_exception
from Src.Logics.storage_manager import storage_manager
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.organization_model import organization_model
from Src.Models.warehouse_model import warehouse_model
from Src.Models.technical_map_model import technical_map_model
from Src.Core.validate import validate

class domain_restapi_factory:
    __storage: storage_manager = None
    __instance = None
    __mapping_add: dict[str, any] = {}
    __mapping_remove: dict[str, any] = {}

    def __new__(cls):
        """Singletone"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__storage = storage_manager()
            cls.__instance.__initing_mapping()
        return cls.__instance

    def __initing_mapping_add(self):
        """
        Mapping for adding

        key: str type of domain
        value: method for adding
        """
        self.__mapping_add["nomenclature_model"] = self.__add_nomenclature
        self.__mapping_add["unit_of_measurement_model"] = self.__add_unit
        self.__mapping_add["group_nomenclature_model"] = self.__add_group
        self.__mapping_add["organization_model"] = self.__add_organization
        self.__mapping_add["warehouse_model"] = self.__add_warehouse
        self.__mapping_add["technical_map_model"] = self.__add_tech_map

    def __initing_mapping_remove(self):
        """
        Mapping for removing
        
        key: str type of domain
        value: method for removing
        """
        self.__mapping_remove["nomenclature_model"] = self.__remove_nomenclature
        self.__mapping_remove["unit_of_measurement_model"] = self.__remove_unit
        self.__mapping_remove["group_nomenclature_model"] = self.__remove_group
        self.__mapping_remove["organization_model"] = self.__remove_organization
        self.__mapping_remove["warehouse_model"] = self.__remove_warehouse
        self.__mapping_remove["technical_map_model"] = self.__remove_tech_map

    def __initing_mapping(self):
        """Initing all mapping"""
        self.__initing_mapping_add()
        self.__initing_mapping_remove()

    
    def create(self, obj) -> any:
        """Method for adding a new domain"""
        validate.validated_null_value(obj, 
                                      "object", 
                                      "object must be not None",
                                      arguments_exception)
        if getattr(obj, "id", None) and self.find_or_none(obj.id) is not None:
            raise operation_exception(
                "id", f"object with id {obj.id} already exists"
            )
        
        if getattr(obj, "name", None) and self.find_or_none(obj.name) is not None:
            raise operation_exception(
                "name", f"object with name {obj.name!r} already exists"
            )
        
        self.__dispatch_add(obj)
        return obj

    def read(self, code: str) -> any:
        """Method for reading by id or name"""
        return self.find(code)

    def update(self, code: str, new_obj: any) -> any:
        """Method for replacing domain"""
        validate.validated_null_value(new_obj,
                                      "object", 
                                      "object must be not None",
                                      arguments_exception)
        current = self.find(code)

        if self.__is_referenced(current):
            raise operation_exception(
                "domain",
                f"cannot update {code}: entity is referenced by another entity",
            )
        new_id = getattr(new_obj, "id", None)
        if new_id is not None and new_id != current.id:
            raise arguments_exception("id", "id cannot be changed on update")
        new_obj.id = current.id

        self.__dispatch_remove(current)
        self.__dispatch_add(new_obj)
        return new_obj

    def delete(self, code: str, force: bool = False) -> None:
        """
        Method for deleting domain with check link
        
        force:
        - flag for forced deletion
        """
        target = self.find(code)
        if not force and self.__is_referenced(target):
            raise operation_exception(
                "domain",
                f"cannot delete {code}: entity is referenced by another entity",
            )
        self.__dispatch_remove(target)

    def find(self, code: str) -> any:
        """Method for finding domain"""
        obj = self.find_or_none(code)
        if obj is None:
            raise not_exist_exception("domain", f"not found: {code}")
        return obj

    def find_or_none(self, code: str) -> any:
        """Method for finding domain, if domain doen't exist return None"""
        if not code:
            return None
        for obj in self.__iter_all():
            if getattr(obj, "id", None) == code or getattr(obj, "name", None) == code:
                return obj
        return None

    def list_all(self) -> dict:
        """Method for getting all storage"""
        return self.__storage

    def __dispatch_add(self, obj) -> None:
        """Method for adding domain"""
        type_target = type(obj).__name__
        
        handler = self.__mapping_add.get(type_target)
        
        if handler is None:
            raise arguments_exception(
                "object", f"unsupported type {type_target}"
            )
            
        handler(obj)
        return

    def __dispatch_remove(self, target: any) -> None:
        """Method for removing domain"""
        type_target = type(target).__name__
        if self.__mapping_remove.get(type_target, False):
            if self.__mapping_remove[type_target](target):
                return
            
        raise not_exist_exception(
            "domain", f"cannot find container for {target.name!r}"
        )

    def __add_nomenclature(self, obj: nomenclature_model) -> None:
        """Method for adding nomenclature"""
        group_name = obj.group_of_nomenclature.name
        bucket = self.__storage.nomenclatures.setdefault(group_name, {})
        bucket[obj.name] = obj

    def __remove_nomenclature(self, target: nomenclature_model) -> bool:
        """Method for removing nomenclature"""
        for bucket in self.__storage.nomenclatures.values():
            for name, nom in list(bucket.items()):
                if nom is target:
                    del bucket[name]
                    return True
        return False

    def __add_unit(self, obj: unit_of_measurement_model) -> None:
        """Method for adding unit"""
        category = self.__unit_category(obj)
        self.__storage.units_of_measurement.setdefault(category, {})[obj.name] = obj

    def __remove_unit(self, target: unit_of_measurement_model) -> bool:
        """Method for removing unit"""
        for bucket in self.__storage.units_of_measurement.values():
            for name, unit in list(bucket.items()):
                if unit is target:
                    del bucket[name]
                    return True
        return False

    @staticmethod
    def __unit_category(obj: unit_of_measurement_model) -> str:
        """Method for defining category of unit"""
        root = obj
        while root.base is not None:
            root = root.base
        if root.name in ("gram", "kilogram", "ton"):
            return "weight"
        if root.name in ("milliliter", "liter", "cubic meter"):
            return "volume"
        if root.name.startswith("square"):
            return "square"
        return "weight"

    def __add_group(self, obj: group_nomenclature_model) -> None:
        """Method for adding group"""
        self.__storage.groups_nomenclature[obj.name] = obj

    def __remove_group(self, target: group_nomenclature_model) -> bool:        
        """Method for removing group"""
        groups = self.__storage.groups_nomenclature
        for name, group in list(groups.items()):
            if group is target:
                del groups[name]
                return True
        return False

    def __add_organization(self, obj: organization_model) -> None:
        """Method for adding organization"""
        self.__storage.company = obj

    def __remove_organization(self, target: organization_model) -> bool:
        """Method for removing organization"""
        if self.__storage.company is target:
            self.__storage.company = None
            return True
        return False

    def __add_warehouse(self, obj: warehouse_model) -> None:
        """Method for adding warehouse"""
        prefix = self.__warehouse_prefix(obj.name)
        bucket = self.__storage.warehouses.setdefault(prefix, [])
        
        for existing in bucket:
            if existing.name == obj.name:
                raise operation_exception(
                    "name", f"warehouse {obj.name!r} already exists"
                )
                
        bucket.append(obj)

    def __remove_warehouse(self, target: warehouse_model) -> bool:
        """Method for removing warehouse"""
        for lst in self.__storage.warehouses.values():
            for wh in list(lst):
                if wh is target:
                    lst.remove(wh)
                    return True
        return False

    @staticmethod
    def __warehouse_prefix(name: str) -> str:
        """Method for parse group from name warehouses"""
        head = name.split("0")[0].rstrip("+")
        return head or name

    def __add_tech_map(self, obj: technical_map_model) -> None:
        """Method for adding tech map"""
        self.__storage.tech_maps[obj.name] = obj

    def __remove_tech_map(self, target: technical_map_model) -> bool:
        """Method for removing tech map"""
        maps = self.__storage.tech_maps
        for name, tm in list(maps.items()):
            if tm is target:
                del maps[name]
                return True
        return False

    def __iter_all(self):
        """Method for itering in all storage"""
        for items in self.__storage.nomenclatures.values():
            yield from items.values()
        for units in self.__storage.units_of_measurement.values():
            yield from units.values()
        yield from self.__storage.groups_nomenclature.values()
        if self.__storage.company is not None:
            yield self.__storage.company
        for lst in self.__storage.warehouses.values():
            yield from lst
        yield from self.__storage.tech_maps.values()

    def __is_referenced(self, target) -> bool:
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
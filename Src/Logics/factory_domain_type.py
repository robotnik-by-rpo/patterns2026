from Src.Logics.storage_manager import storage_manager
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.technical_map_model import technical_map_model
from Src.Models.transaction_model import transaction_model

"""
Factory for formations list domain from storage manager
"""
class factory_domain_type:
    __mapping: dict[str, any] = {}
    __storage: storage_manager = None

    def __new__(cls):
        """Singletone"""
        if not hasattr(cls, '_factory_domain_type__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.__storage = storage_manager()
            cls.__instance.__initing_mapping()
        return cls.__instance
    
    def __contains__(self, domain_type: str) -> bool:
        return domain_type in self.__mapping
    
    def __initing_mapping(self):
        """Initing mapping"""
        self.__mapping["nomenclature_model"] = self.__get_items_nomenclature
        self.__mapping["group_nomenclature_model"] = self.__get_items_group
        self.__mapping["unit_of_measurement_model"] = self.__get_items_unit
        self.__mapping["technical_map_model"] = self.__get_tech_map
        self.__mapping["transaction_model"] = self.__get_items_transaction

    def convert(self, domain_type: str) -> list[any]:
        """Getting list domains in depending on the type"""
        return self.__mapping[domain_type]()
    
    def __get_items_nomenclature(self) -> list[nomenclature_model]:
        """Collecting list object by nomenclature model"""
        items = []
        for group_items in self.__storage.nomenclatures.values():
            items.extend(group_items.values())

        return items
    
    def __get_items_group(self) -> list[group_nomenclature_model]:
        """Collecting list object by group nomenclature model"""
        return list(self.__storage.groups_nomenclature.values())

    def __get_items_unit(self) -> list[unit_of_measurement_model]:
        """Collecting list object by unit of measurement model"""
        items = []
        for units in self.__storage.units_of_measurement.values():
            items.extend(units.values())
        return items 
    
    def __get_tech_map(self) -> list[technical_map_model]:
        """Collecting list object by technical map model"""
        return list(self.__storage.tech_maps.values())
    
    def __get_items_transaction(self) -> list[transaction_model]:
        """Collecting list object by transaction model"""
        return list(self.__storage.transactions.values())
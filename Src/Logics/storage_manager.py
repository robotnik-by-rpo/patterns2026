from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.organization_model import organization_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.warehouse_model import warehouse_model
from Src.Core.abstract_manager import abstract_manager
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception
from Src.Factories.settings_storage_factory import base_data_setting_storage
from Src.Factories.settings_storage_factory import settings_storage_factory

class storage_manager(abstract_manager):
    """Class storing units, nomenclatures, company, warehouses, groups"""  
    __units: dict[str, dict[str, unit_of_measurement_model]] = {}

    # dict{name_group_nomenclature, dict[name_of_nomenclature, nomenclature]}
    __nomenclatures: dict[str,dict[str,nomenclature_model]] = {}
    __company: organization_model = None
    __warehouses: dict[str, list[warehouse_model]] = {}
    __groups: dict[str, group_nomenclature_model] = {}
    __is_first : bool = True

    def __new__(cls):
        """Singletone"""
        if not hasattr(cls, '_storage_manager__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.__is_first = cls.__instance.convert()
        return cls.__instance

    def convert(self) -> bool:
        """Check, if data create at first so they will creat base data"""
        if self.__is_first: 
            self.__create_data(settings_storage_factory.create_all())
        return False
    
    def __create_data(self, data_settings: base_data_setting_storage) -> None:
        """Creating a base data"""
        self.__units = data_settings["units"]
        self.__groups = data_settings["groups"]
        self.__company = data_settings["company"]
        self.__nomenclatures = data_settings["nomenclatures"]
        self.__warehouses = data_settings["warehouses"]
    
    @property
    def groups_nomenclature(self) -> list[group_nomenclature_model]:
        """It's getter for groups of nomenclature"""
        return self.__groups

    @groups_nomenclature.setter
    def groups_nomenclature(self, 
                            new_groups_nomenclatures: list[group_nomenclature_model]) -> None:
        """It's setter for groups of nomenclature"""
        self.__groups = validate.validated_null_empty_obj(new_groups_nomenclatures,
                                                          "new groups nomenclatures",
                                                          "new groups nomenclatures must be not None and not empty list",
                                                          arguments_exception)

    @property
    def nomenclatures(self) -> dict[str,list[nomenclature_model]]:
        """It's getter for nomenclature"""
        return self.__nomenclatures
    
    @nomenclatures.setter
    def nomenclatures(self, new_nomenclatures: dict[str,list[nomenclature_model]])-> None:
        """It's setter for nomenclature"""
        self.__nomenclatures = validate.validated_null_empty_obj(new_nomenclatures,
                                                                 "new nomenclatures",
                                                                 "new nomeclature must be not None and not empty list",
                                                                 arguments_exception)
    
    @property
    def warehouses(self) -> list[warehouse_model]:
        """It's getter for warehouses"""
        return self.__warehouses
    
    @warehouses.setter
    def warehouses(self, new_warehouses) -> None:
        """It's setter for warehouses"""
        self.__warehouses = validate.validated_null_empty_obj(new_warehouses,
                                                              "new warehouses",
                                                              "new warehouses must be not None and not empty list",
                                                              arguments_exception)

    @property
    def company(self) -> organization_model:
        """It's getter for company"""
        return self.__company 
    
    @company.setter
    def company(self, new_company: organization_model) -> None:
        """It's setter for company"""
        self.__company = validate.validated_null_value(new_company,
                                                       "new company",
                                                       "new company must be not None",
                                                       arguments_exception)

    @property
    def is_first(self) -> bool:
        """It's getter for flag"""
        return self.__is_first
    
    @is_first.setter
    def is_first(self, new_flag: bool) -> None:
        """It's setter for flag"""
        self.__is_first = validate.validated_null_value(new_flag,
                                                        "new flag",
                                                        "new flag must be bool, not None value",
                                                        arguments_exception)

    @property
    def units_of_measurement(self) -> dict[str, dict[str, unit_of_measurement_model]]:
        """It's getter for unit of measurement"""
        return self.__units
    
    @units_of_measurement.setter
    def units_of_measurement(self, new_units):
        """It's setter for unit of measurement"""
        self.__units = validate.validated_null_value(new_units)

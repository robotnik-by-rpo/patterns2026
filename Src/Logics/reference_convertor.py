from Src.Core.abstract_convert import abstract_convertor
from Src.Core.exception import not_exist_exception
from Src.Logics.datetime_convertor import datetime_convertor
from Src.Core.product import product
from typing import Callable

from Src.Logics.storage_manager import storage_manager
from Src.Core.building import building
from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.ingredient_model import ingredient_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.organization_model import organization_model
from Src.Models.package_model import package_model
from Src.Models.prepack_model import prepack_model
from Src.Models.recipe_line_model import recipe_line_model
from Src.Models.recipe_model import recipe_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.technical_map_model import technical_map_model
from Src.Models.warehouse_model import warehouse_model
from Src.Models.settings_model import settings_model

"""
Convertor for DIY classes in project
"""
class reference_convertor(abstract_convertor):
    # Pull of classes for converting in project
    __EXIST_MODEL_TO_JSON: dict= {group_nomenclature_model: True,
                                  ingredient_model: True,
                                  nomenclature_model: True,
                                  organization_model: True,
                                  package_model: True,
                                  prepack_model: True,
                                  recipe_line_model: True,
                                  recipe_model: True,
                                  unit_of_measurement_model: True,
                                  technical_map_model: True,
                                  warehouse_model: True,
                                  settings_model: True,
                                  building: True,
                                  storage_manager: True}
    __mapping: dict = {}

    __COMPONENT_PRODUCT: dict = {}

    # Method signatures
    # Initing dicts
    def __init__(self) -> None: ...

    # Initing 
    def __init__component(self) -> None: ...
    def __init__mapping(self) -> None: ...

    # Public call convert
    def convert(self, object: any) -> dict: ...

    # Help method
    def __find_component_convertor(self, component: product) -> Callable[[any], dict]: ...

    # Class converters
    def __convert_group_nomenclature_model(self, object: group_nomenclature_model) -> dict: ...
    def __convert_ingredient_model(self, object: ingredient_model) -> dict: ...
    def __convert_unit_model(self, object: unit_of_measurement_model) -> dict: ...
    def __convert_organization_model(self, object: organization_model) -> dict: ...
    def __convert_nomenclature_model(self, object: nomenclature_model) -> dict: ...
    def __convert_package_model(self, object: package_model) -> dict: ...
    def __convert_prepack_model(self, object: prepack_model) -> dict: ...
    def __convert_recipe_line_model(self, object: recipe_line_model) -> dict: ...
    def __convert_recipe_model(self, object: recipe_model) -> dict: ...
    def __convert_technical_map_model(self, object: technical_map_model) -> dict: ...
    def __convert_building(self, object: building) -> dict: ...
    def __convert_warehouse_model(self, object: warehouse_model) -> dict: ...
    def __convert_settings_model(self, object: settings_model) -> dict: ...
    def __convert_storage_manager(self, object: storage_manager) -> dict: ...


    def __init__(self):
        self.__init__component()
        self.__init__mapping()

    def __init__mapping(self):
        """Initialization method for mapping transformations"""
        self.__mapping[group_nomenclature_model] = self.__convert_group_nomenclature_model
        self.__mapping[ingredient_model] = self.__convert_ingredient_model
        self.__mapping[nomenclature_model] = self.__convert_nomenclature_model
        self.__mapping[organization_model] = self.__convert_organization_model
        self.__mapping[package_model] = self.__convert_package_model
        self.__mapping[prepack_model] = self.__convert_prepack_model
        self.__mapping[recipe_line_model] = self.__convert_recipe_line_model
        self.__mapping[recipe_model] = self.__convert_recipe_model
        self.__mapping[unit_of_measurement_model] = self.__convert_unit_model
        self.__mapping[technical_map_model] = self.__convert_technical_map_model
        self.__mapping[warehouse_model] = self.__convert_warehouse_model
        self.__mapping[settings_model] = self.__convert_settings_model
        self.__mapping[storage_manager] = self.__convert_storage_manager

    def __init__component(self):
        """Initialization method for mapping heirs by product"""
        self.__COMPONENT_PRODUCT[ingredient_model] = self.__convert_ingredient_model
        self.__COMPONENT_PRODUCT[prepack_model] = self.__convert_prepack_model
        self.__COMPONENT_PRODUCT[package_model] = self.__convert_package_model

    def convert(self, object: any) -> dict:
        """Method for public call converting object"""
        type_object = type(object)
        exist = self.__EXIST_MODEL_TO_JSON.get(type_object, False)
        if exist:
            return self.__mapping[type_object](object)
        raise not_exist_exception("type of object", "type of object must be exist")

    def __convert_group_nomenclature_model(self, object: group_nomenclature_model) -> dict:
        """Method for creating dict from group nomenclature model"""
        return {"id": object.id,
                "name": object.name}

    def __convert_ingredient_model(self, object: ingredient_model) -> dict:
        """Method for creating dict from ingredient_model"""
        return {"id": object.id,
                "name": object.name,
                "brutto": object.brutto,
                "netto": object.netto,
                "unit": self.__convert_unit_model(object.unit) ,
                "waste": object.waste}
    
    def __convert_unit_model(self, object: unit_of_measurement_model) -> dict:
        """Method for creating dict from unit model"""
        return {"id": object.id,
                "name": object.name,
                "coef": object.coef,
                "unit": self.__convert_unit_model(object.base) if object.base is not None else None}
    
    def __convert_organization_model(self, object: organization_model) -> dict:
        """Method for creating dict from organization model"""
        return {"id": object.id,
                "name": object.name,
                "inn": object.inn,
                "bic": object.bic,
                "current_account": object.current_account,
                "form_of_ownership": object.form_of_ownership}
    
    def __convert_nomenclature_model(self, object: nomenclature_model) -> dict:
        """Method for creating dict from nomenclature model"""
        return {"id": object.id,
                "name": object.name,
                "full_name": object.full_name,
                "group_of_nomenclature": self.__convert_group_nomenclature_model(object.group_of_nomenclature),
                "base_unit": self.__convert_unit_model(object.base_unit),
                "type_of_pos": object.type_of_pos}
    
    def __convert_package_model(self, object: package_model) -> dict:
        """Method for creating dict from package model"""
        return {"id": object.id,
                "name": object.name,
                "brand": object.brand,
                "unit": self.__convert_unit_model(object.unit),
                "brutto": object.brutto,
                "waste": object.waste,
                "measure": object.measure}
    
    def __convert_prepack_model(self, object: prepack_model) -> dict:
        """Method for creating dict from prepack model"""
        return {"id": object.id,
                "name": object.name,
                "brand": object.brand,
                "category": object.category,
                "unit": self.__convert_unit_model(object.unit),
                "waste": object.waste}
    
    def __find_component_convertor(self, component: product) -> ingredient_model | package_model | prepack_model:
        """Method for definitions implement class by product"""
        for cls, func in self.__COMPONENT_PRODUCT.items():
            if isinstance(component, cls):
                return func
        raise not_exist_exception("component",
                                    f"unsupported component type: {cls}")

    def __convert_recipe_line_model(self, object: recipe_line_model) -> dict:
        """Method for creating dict from recipe line model"""
        convertor = self.__find_component_convertor(object.component)
        return {"component": convertor(object.component),
                "quantity": object.quantity,
                "share": object.share,
                "brutto": object.brutto,
                "netto": object.netto}
    
    def __convert_recipe_model(self, object: recipe_model) -> dict:
        """Method for creating dict from recipe model"""
        lines = []
        for l in object.lines:
            lines.append(self.__convert_recipe_line_model(l))
        
        return {"id": object.id,
                "name": object.name,
                "lines": lines,
                "instruction": object.instruction,
                "brutto": object.brutto,
                "netto": object.netto}

    def __convert_technical_map_model(self, object: technical_map_model) -> dict:
        """Method for creating dict from convert technical map model"""
        convertor = datetime_convertor()
        return {"id": object.id,
                "name": object.name,
                "unit": self.__convert_unit_model(object.unit),
                "recipe": self.__convert_recipe_model(object.recipe),
                "source": object.source,
                "date": convertor.convert(object.date_of_approval),
                "general_manager": object.general_manager,
                "company": self.__convert_organization_model(object.company),
                "package": self.__convert_package_model(object.package),
                "brutto": object.brutto,
                "netto": object.netto}
    
    def __convert_building(self, object: building) -> dict:
        """Method for creating dict from building"""
        return {"id": object.id,
                "name": object.name,
                "square": object.square,
                "address": object.address,
                "unit": self.__convert_unit_model(object.base_unit)}

    def __convert_warehouse_model(self, object: warehouse_model) -> dict:
        """Method for creating dict from warehouse model"""
        return {"id": object.id,
                "name": object.name,
                "warehouse_owner": self.__convert_organization_model(object.warehouse_owner),
                "description": self.__convert_building(object.description_of_building)}
    
    def __convert_settings_model(self, object: settings_model) -> dict:
        """Method for creating dict from settings model"""
        return {"id": object.id,
                "name": object.name,
                "company": self.__convert_organization_model(object.company),
                "boss_name": object.boss_name,
                "accounter_name": object.accounter_name,
                "is_first": object.is_first,
                "response_format": object.response_format.value}

    def __convert_storage_manager(self, object: storage_manager) -> dict:
        """Method for creating dict from storage manager"""
        units: dict[str, dict[str, unit_of_measurement_model]] = {}
        nomenclatures: dict[str,dict[str,nomenclature_model]] = {}
        warehouses: dict[str, list[warehouse_model]] = {}
        groups: dict[str, group_nomenclature_model] = {}
        tech_maps: dict[str, technical_map_model] = {}

        for unit_group, unit_items in object.units_of_measurement.items():
            bucket = units.setdefault(unit_group, {})
            for unit_name, unit_obj in unit_items.items():
                bucket[unit_name] = self.__convert_unit_model(unit_obj)

        for nom_group, nom_items in object.nomenclatures.items():
            bucket = nomenclatures.setdefault(nom_group, {})
            for nom_name, nom_obj in nom_items.items():
                bucket[nom_name] = self.__convert_nomenclature_model(nom_obj)

        for wh_group, wh_items in object.warehouses.items():
            bucket = warehouses.setdefault(wh_group, [])
            for ws in wh_items:
                bucket.append(self.__convert_warehouse_model(ws))

        for group_name, group_obj in object.groups_nomenclature.items():
            groups[group_name] = self.__convert_group_nomenclature_model(group_obj)

        for tm_name, tm_obj in object.tech_maps.items():
            tech_maps[tm_name] = self.__convert_technical_map_model(tm_obj)

        return {
            "units": units,
            "nomenclatures": nomenclatures,
            "company": self.__convert_organization_model(object.company),
            "warehouses": warehouses,
            "groups": groups,
            "is_first": object.is_first,
            "tech_maps": tech_maps,
        }

from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.reference_convertor import reference_convertor
from  Src.Logics.datetime_convertor import datetime_convertor
from datetime import datetime
from Src.Core.exception import not_exist_exception

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
Factory for convert any object
"""
class convert_factory:
    # Basic types in Python
    __BASIC_TYPE: dict = {str: True,
                          int: True,
                          float: True}
    
    # Datetime type
    __DATETIME_TYPE: dict = {datetime: True}

    # DIY class in this project (models, managers)
    __REFERENCE_CONVERTOR: dict = {storage_manager: True,
                                   building: True,
                                   group_nomenclature_model: True,
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
                                   settings_model: True}

    __basic_convertor: basic_convertor = None
    __reference_convertor: reference_convertor = None
    __datetime_convertor: datetime_convertor = None

    def __init__(self):
        self.__init__convertors()

    def __init__convertors(self):
        """Method for initing convertors"""
        self.__basic_convertor = basic_convertor()
        self.__reference_convertor = reference_convertor()
        self.__datetime_convertor = datetime_convertor()

    def __type__convert(self, object: any) -> dict:
        """Method for find method and call convert method"""
        type_object = type(object)
        if type_object in self.__DATETIME_TYPE:
            return self.__datetime_convertor.convert(object)
        
        if type_object in self.__BASIC_TYPE:
            return self.__basic_convertor.convert(object)
        
        if type_object in self.__REFERENCE_CONVERTOR:
            return self.__reference_convertor.convert(object)
        
        raise not_exist_exception("type convert", "type convert must be exist")

    def convert(self, object: any) -> dict:
        """Method for call convert method from convertors"""
        return self.__type__convert(object)

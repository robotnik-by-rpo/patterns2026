from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Core.abc_data import unit
from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception

class nomenclature_model(unit):
    """It's class for initing good, material or service"""
    _MAX_SIZE_NAME = 50
    _FULL_MAX_SIZE_NAME = 255

    __full_name: str
    __group_of_nomenclature: group_nomenclature_model
    __base_unit: unit_of_measurement_model = None
    __existing_type_of_pos: dict[str,bool] = {"crude":True,
                                              "product":True,
                                              "prepack":True,
                                              "dish": True}
    __type_of_pos: str

    def __init__(self, name:str, 
                 full_name: str, 
                 group: group_nomenclature_model,
                 base_unit: unit_of_measurement_model, 
                 type_of_pos: str):
        super().__init__()
        self.name = validate.validated_name(name,
                                            self._MAX_SIZE_NAME,
                                            "name",
                                            arguments_exception)
       
        self.__full_name = validate.validated_name(full_name,
                                                   self._FULL_MAX_SIZE_NAME,
                                                    "full name",
                                                    arguments_exception)
        self.__group_of_nomenclature = validate.validated_null_value(group, 
                                                                     "group", 
                                                                     "group must be not None",
                                                                     arguments_exception)
        self.__base_unit = validate.validated_null_value(base_unit,
                                                         "base unit of measurement",
                                                         "base unit of measurement must be not None",
                                                         arguments_exception)

        self.__type_of_pos = validate.validated_value_exist(type_of_pos,
                                                            self.__existing_type_of_pos,
                                                            "type of position",
                                                            "undefine position of type",
                                                            arguments_exception)
    @property
    def full_name(self)->str:
        """Getting full name"""
        return self.__full_name
    
    @full_name.setter
    def full_name(self, new_full_name: str) -> None:
        """Setting full name"""
        self.__full_name = validate.validated_name(new_full_name,
                                                   self._FULL_MAX_SIZE_NAME,
                                                   "full name",
                                                   arguments_exception)

    @property 
    def group_of_nomenclature(self) -> group_nomenclature_model:
        """Getting group of nomenclature"""
        return self.__group_of_nomenclature
    
    @group_of_nomenclature.setter
    def group_of_nomenclature(self, new_group_of_nomenclature: group_nomenclature_model) -> None:
        """Setting group of nomenclature"""
        self.__group_of_nomenclature = validate.validated_null_value(new_group_of_nomenclature,
                                                                     "group",
                                                                     "group must be not None",
                                                                     arguments_exception)

    @property
    def base_unit(self)->unit_of_measurement_model:
        """Getting base unit of measurement"""
        return self.__base_unit
    
    @base_unit.setter
    def base_unit(self, new_base_unit: unit_of_measurement_model)->None:
        """Setting base unit of measurement"""
        self.__base_unit = validate.validated_null_value(new_base_unit,
                                                        "base unit of measurement",
                                                        "base unit of measurement must be not None",
                                                        arguments_exception)

    @property
    def type_of_pos(self) -> str:
        """Getting type of position"""
        return self.__type_of_pos
    
    @type_of_pos.setter
    def type_of_pos(self, new_type_of_pos) -> None:
        """Setting type of position"""
        self.__type_of_pos = validate.validated_value_exist(new_type_of_pos,
                                                            self.__existing_type_of_pos,
                                                            "type of position",
                                                            "undefine position of type",
                                                            arguments_exception)
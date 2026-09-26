from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Core.abc_data import unit
from Src.Core.exception import arguments_exception
from Src.Models.group_nomenclature_model import group_nomenclature_model

class nomenclature_model(unit):
    """It's class for initing good, material or service"""
    _MAX_SIZE_NAME = 50
    _FULL_MAX_SIZE_NAME = 255

    __full_name: str
    __group_of_nomenclature: group_nomenclature_model
    __base_unit: unit_of_measurement_model = None
    __existing_type_of_pos: dict[str,bool] = {"сырьё":True,
                                              "товар":True,
                                              "полуфабрикат":True,
                                              "блюдо": True}
    __type_of_pos: str

    def __init__(self, name:str, 
                 full_name: str, 
                 group: group_nomenclature_model,
                 base_unit: unit_of_measurement_model, 
                 type_of_pos: str):
        super().__init__()
        self.name = self.__validated_name(name)
        self.__full_name = self.__validated_full_name(full_name)
        self.__group_of_nomenclature = self.__validated_group(group)
        self.__base_unit = self.__validated_base_unit(base_unit)
        self.__type_of_pos = self.__validated_type_of_pos(type_of_pos)

    def __validated_group(self, group: group_nomenclature_model) -> group_nomenclature_model:
        """Method for validating group of nomaneclature"""
        if group is None:
            raise arguments_exception("group","group must be not None")
        return group

    def __validated_base_unit(self, base: unit_of_measurement_model) -> unit_of_measurement_model:
        """Method for validating base unit of measurement of nomaneclature"""
        if base is None:
            raise arguments_exception("base unit of measurement", "base unit of measurement must be not None")
        return base

    def __validated_type_of_pos(self, type_of_pos: str)-> str :
        """Method for validating existing of type of position"""
        if not self.__existing_type_of_pos.get(type_of_pos,False):
            raise arguments_exception("type of position","undefine position of type")
        
        return type_of_pos
    
    def __validated_full_name(self, full_name: str) -> str:
        """Method for validating full name of type of position"""
        if full_name is None or not full_name:
            raise arguments_exception("full name", "full name mustn't be empty or None") 
        
        if len(full_name) > self._FULL_MAX_SIZE_NAME:
            raise arguments_exception("full name", "full name must be shorter than 255 letters")
                   
        return full_name
    
    def __validated_name(self, name: str) -> str:
        """Method for validating name of type of position"""
        if name is None or not name:
            raise arguments_exception("name", "name mustn't be empty or None")  
        if len(name) > self._MAX_SIZE_NAME:
            raise arguments_exception("name", "name must be shorter than 50 letters")
        
        return name
    
    @property
    def full_name(self)->str:
        """Getting full name"""
        return self.__full_name
    
    @full_name.setter
    def full_name(self, new_full_name: str) -> None:
        """Setting full name"""
        self.__full_name = self.__validated_full_name(new_full_name)

    @property 
    def group_of_nomenclature(self)->group_nomenclature_model:
        """Getting group of nomenclature"""
        return self.__group_of_nomenclature
    
    @group_of_nomenclature.setter
    def group_of_nomenclature(self, new_group_of_nomenclature: group_nomenclature_model) -> None:
        """Setting group of nomenclature"""
        self.__group_of_nomenclature = self.__validated_group(new_group_of_nomenclature)

    @property
    def base_unit(self)->unit_of_measurement_model:
        """Getting base unit of measurement"""
        return self.__base_unit
    
    @base_unit.setter
    def base_unit(self, new_base_unit: unit_of_measurement_model)->None:
        """Setting base unit of measurement"""
        self.__base_unit = self.__validated_base_unit(new_base_unit)

    @property
    def type_of_pos(self) -> str:
        """Getting type of position"""
        return self.__type_of_pos
    
    @type_of_pos.setter
    def type_of_pos(self, new_type_of_pos) -> None:
        """Setting type of position"""
        self.__type_of_pos=self.__validated_type_of_pos(new_type_of_pos)
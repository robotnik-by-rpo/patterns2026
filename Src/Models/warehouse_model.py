from Src.Core.abc_data import unit
from Src.Core.building_model import building_model
from Src.Models.organization_model import organization_model
from Src.Core.exception import arguments_exception
from Src.Core.validate import validate

class warehouse_model(unit):
    """It's class for implementation warehouse model"""
    __warehouse_owner: organization_model
    __description_of_building: building_model

    def __init__(self, 
                 name: str, 
                 warehouse_owner: organization_model, 
                 description: building_model):
        
        super().__init__()
        self.name = name
        self.__warehouse_owner = validate.validated_null_value(warehouse_owner,
                                                               "owner",
                                                               "owner must be not None",
                                                               arguments_exception)

        self.__description_of_building = validate.validated_null_value(description,
                                                                       "description",
                                                                       "description must be not None",
                                                                       arguments_exception)
    
    @property 
    def warehouse_owner(self) -> organization_model:
        """Getting warehouse owner"""
        return self.__warehouse_owner
    
    @warehouse_owner.setter
    def warehouse_owner(self, new_warehouse_owner: organization_model) -> None:
        """Setting warehouse owner"""
        self.__warehouse_owner = validate.validated_null_value(new_warehouse_owner,
                                                               "owner",
                                                               "owner must be not None",
                                                               arguments_exception)

    @property
    def description_of_building(self)->building_model:
        """Getting description of building"""
        return self.__description_of_building
    
    @description_of_building.setter
    def description_of_building(self, new_description_of_building: building_model) -> None:
        """Setting description of building"""
        self.__description_of_building = validate.validated_null_value(new_description_of_building,
                                                                       "description",
                                                                       "description must be not None",
                                                                       arguments_exception)
    
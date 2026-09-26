from Src.Core.abc_data import unit
from Src.Core.exception import arguments_exception
from Src.Models.building_model import building_model
from Src.Models.organization_model import organization_model

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
        self.__warehouse_owner = self.__validated_not_null(warehouse_owner,"owner")
        self.__description_of_building = self.__validated_not_null(description,"description")

    def __validated_not_null(self,
                             object_cls: organization_model | building_model, 
                             value: str) -> organization_model | building_model:
        """Method for validating None value"""
        if object_cls is None:
            raise arguments_exception(value, f"{value} must be not None")
        
        return object_cls
    
    @property 
    def warehouse_owner(self) -> organization_model:
        """Getting warehouse owner"""
        return self.__warehouse_owner
    
    @warehouse_owner.setter
    def warehouse_owner(self, new_warehouse_owner: organization_model) -> None:
        """Setting warehouse owner"""
        self.__warehouse_owner = self.__validated_not_null(new_warehouse_owner,"owner")

    @property
    def description_of_building(self)->building_model:
        """Getting description of building"""
        return self.__description_of_building
    
    @description_of_building.setter
    def description_of_building(self, new_description_of_building: building_model) -> None:
        """Setting description of building"""
        self.__description_of_building = self.__validated_not_null(new_description_of_building,"description")
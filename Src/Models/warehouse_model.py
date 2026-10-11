from Src.Core.abc_data import unit
from Src.Core.building import building
from Src.Models.organization_model import organization_model
from Src.Core.exception import arguments_exception
from Src.Core.validate import validate
from Src.Models.unit_of_measurement_model import unit_of_measurement_model

class warehouse_model(unit):
    """It's class for implementation warehouse model"""
    __warehouse_owner: organization_model
    __description_of_building: building

    def __init__(self, 
                 name: str, 
                 warehouse_owner: organization_model, 
                 description: building):
        
        super().__init__()
        self.name = name
        self.warehouse_owner = warehouse_owner

        self.description_of_building = description
    
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
    def description_of_building(self)->building:
        """Getting description of building"""
        return self.__description_of_building
    
    @description_of_building.setter
    def description_of_building(self, new_description_of_building: building) -> None:
        """Setting description of building"""
        self.__description_of_building = validate.validated_null_value(new_description_of_building,
                                                                       "description",
                                                                       "description must be not None",
                                                                       arguments_exception)

    @classmethod
    def __template_create(cls,
                          address: list[str],
                          names: list[str],
                          squares: list[float],
                          company: organization_model,
                          unit_measurement: unit_of_measurement_model)->list["warehouse_model"]:
        warehouses = []
        for n,a,s in zip(names, address,squares):
            desc = cls(n,
                        company,
                        building("warehouse",s,unit_measurement,a))
            warehouses.append(desc)

        return warehouses

    @classmethod
    def create_warehouses_A(cls, 
                            company: organization_model,
                            unit_measurement:unit_of_measurement_model ) -> list["warehouse_model"]:
        address = ["Moscow, Pushkina St. 35",
                   "Saint Petersburg, Repina St. 75"]
        names = ["A01",
                 "A02"]
        squares = [183.0,
                   1891.0]
        return cls.__template_create(address,
                                     names,
                                     squares,
                                     company,unit_measurement)

    @classmethod
    def create_warehouses_Ap(cls, 
                             company: organization_model,
                             unit_measurement: unit_of_measurement_model) -> list["warehouse_model"]:
        address = ["Saint Petersburg, Sofia St. 92",
                   "Moscow, Volkhonka St. 24",
                   "Voronezh, 25th October St. 45"]
        
        names = ["A+03",
                 "A+07",
                 "A+10"]
        squares = [889.0,
                  712.0,
                  142.0]

        return cls.__template_create(address,
                                     names,
                                     squares,
                                     company,
                                     unit_measurement)

    @classmethod
    def create_warehouses_B(cls, 
                            company: organization_model,
                            unit_measurement: unit_of_measurement_model) -> list["warehouse_model"]:
        
        address = ["Saint Petersburg, Sofia St. 12",
            "Moscow, Volkhonka St. 10",
            "Voronezh, 25th October St. 15"]

        names = ["B03",
                 "B09",
                 "B11"]
        squares = [81289.0,
                  71241.0,
                  14224.0]

        return cls.__template_create(address,
                                     names,
                                     squares,
                                     company,
                                     unit_measurement)

    @classmethod
    def create_warehouses_Bp(cls, 
                             company: organization_model,
                             unit_measurement: unit_of_measurement_model) -> list["warehouse_model"]:
        address = ["Saint Petersburg, Sofia St. 12",
                "Moscow, Volkhonka St. 24A",
                "Voronezh, 25th October St. 5"]
    
        names = ["B+01",
                 "B+02",
                 "B+11"]
        squares = [889.0,
                  712.0,
                  142.0]

        return cls.__template_create(address,
                                     names,
                                     squares,
                                     company,
                                     unit_measurement)

    @classmethod
    def create_warehouses_C(cls, 
                            company: organization_model,
                            unit_measurement: unit_of_measurement_model) -> list["warehouse_model"]:
        address = ["Saint Petersburg, Sofia St. 92",
                   "Moscow, Volkhonka St. 24",
                   "Voronezh, 25th October St. 45"]
        
        names = ["C01",
                 "C02"]
        squares = [889.0,
                  712.0]

        return cls.__template_create(address,
                                     names,
                                     squares,
                                     company,
                                     unit_measurement)

    @classmethod
    def create_warehouses_D(cls, 
                            company: organization_model,
                            unit_measurement: unit_of_measurement_model) -> list["warehouse_model"]:
        address = ["Saint Petersburg, Sofia St. 192",
                   "Moscow, Volkhonka St. 14",
                   "Voronezh, 25th October St. 25"]
        
        names = ["D03",
                 "D07",
                 "D10"]
        squares = [81.0,
                  712.0,
                  119.0]

        return cls.__template_create(address,
                                     names,
                                     squares,
                                     company,
                                     unit_measurement)
    
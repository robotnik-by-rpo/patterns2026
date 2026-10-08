from Src.Core.abc_data import unit
from Src.Core.validate import validate
from Src.Core.product import product
from Src.Models.recipe_model import recipe_model
from Src.Models.organization_model import organization_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Core.exception import arguments_exception
from datetime import datetime
from Src.Models.package_model import package_model
from Src.Models.ingredient_model import ingredient_model
from Src.Models.prepack_model import prepack_model
from Src.Core.exception import operation_exception

"""
Class for store information about dish
Source: https://t-secrets.ru/documents/tehnologicheskaya-karta-bliuda/
"""
class technical_map_model(unit):
    __foodstuffs: list[product] = []
    __recipe: recipe_model = None
    __source: str = ""
    __date_of_approval: datetime = None
    __general_manager: str = ""
    __company: organization_model = None
    __package: package_model = None
    __unit: unit_of_measurement_model = unit_of_measurement_model.create_g()

    __total_weight: float = 0

    def __init__(self, 
                 name: str, 
                 recipe: recipe_model, 
                 foodstuffs: list[product],  
                 source: str, 
                 date: datetime, 
                 general_manager: str, 
                 company: organization_model,
                 package: package_model):
        super().__init__()
        self.name = name
        self.recipe = recipe
        self.foodstuffs = foodstuffs
        self.source = source
        self.date_of_approval = date
        self.general_manager = general_manager
        self.company = company
        self.package = package

    def __total_weight_dish(self):
        """Method for calculating total value from foodstuffs"""
        total = 0
        for p in self.foodstuffs:
            if isinstance(p, ingredient_model):
                total += p.netto * p.unit.common_coef
            if isinstance(p, prepack_model):
                total += p.weight * p.unit.common_coef
        return total

    @property
    def package(self)->package_model:
        """Getter for package"""
        return self.__package
    
    @package.setter
    def package(self, new_package: package) -> None:
        """Setter for package"""
        self.__package = new_package
   
    @property
    def unit(self)->unit_of_measurement_model:
        """Getter for unit of measurement"""
        return self.__unit
    
    @property
    def foodstuffs(self) -> list[product]:
        """Getter for foodstuffs"""
        return self.__foodstuffs
    
    @foodstuffs.setter
    def foodstuffs(self, new_foodstuffs: list[product]) -> None:
        """Setter for foodstuffs"""
        self.__foodstuffs = validate.validated_null_empty_obj(new_foodstuffs,
                                                              "new foodstuffs",
                                                              "new foodstuffs must have food products, not None or empty value",
                                                              arguments_exception)
        self.__total_weight = validate.validated_null_and_zero_value(self.__total_weight_dish(),
                                                                     "total weight",
                                                                     "total weight must bigger than zero, foodstuff must be not empty or not None",
                                                                     operation_exception)
        
    @property
    def recipe(self) -> recipe_model:
        """Getter for recipe"""
        return self.__recipe
    
    @recipe.setter
    def recipe(self, new_recipe: recipe_model) -> None:
        """Setter for recipe"""
        self.__recipe = validate.validated_null_value(new_recipe,
                                                      "new recipe",
                                                      "new recipe must have instructions step by step for cooking, not None or empty value",
                                                      arguments_exception)
    
    @property
    def source(self) -> str:
        """Getter for source"""
        return self.__source
    
    @source.setter
    def source(self, new_source: str):
        """Setter for source"""
        self.__source = validate.validated_null_empty_obj(new_source,
                                                          "new source",
                                                          "new source must be not None or not empty value",
                                                          arguments_exception)
        
    @property
    def general_manager(self) -> str:
        """Getter for general manager"""
        return self.__general_manager
    
    @general_manager.setter
    def general_manager(self, new_general_manager: str) -> None:
        """Setter for general maanger"""
        self.__general_manager = validate.validated_null_empty_obj(new_general_manager,
                                                                   "new general manager",
                                                                   "new general manager must be have name and fullname of general manager, not None or not empty",
                                                                   arguments_exception)
        
    @property
    def company(self) -> organization_model:
        """Getter for company"""
        return self.__company
    
    @company.setter
    def company(self, new_company: organization_model) -> None:
        """Setter for company"""
        self.__company = validate.validated_null_value(new_company,
                                                       "new company",
                                                       "new company must be object of organization, not None value",
                                                       arguments_exception)
        
    @property
    def date_of_approval(self) -> datetime:
        """Getter for date of approval"""
        return self.__date_of_approval
    
    @date_of_approval.setter
    def date_of_approval(self, new_date: datetime) -> None:
        """Setter for date of approval"""
        self.__date_of_approval = validate.validated_null_value(new_date,
                                                                "new date",
                                                                "new date must be not None value",
                                                                arguments_exception)
    @property
    def total_weight(self) -> float:
        """Getter for total weight of dish"""
        return self.__total_weight
    
    @classmethod
    def create_technical_map(cls) -> "technical_map_model":
        """Factory method for creating technical map"""
        return cls("French baguette",
                   recipe_model.create_recipe(),
                   ingredient_model.create_ingredients(),
                   "M. P. Mogilny 2nd edition DeLi plus, 2016, - 888 p.",
                   datetime.strptime("08.09.25","%d.%m.%y"),
                   "Lavrenov O.S.",
                   organization_model.create_organization(),
                   package_model.create_package_paper())
    
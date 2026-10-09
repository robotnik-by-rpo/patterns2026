from Src.Core.product import product
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception
from Src.Models.recipe_model import recipe_model
from Src.Models.organization_model import organization_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.package_model import package_model
from datetime import datetime

"""
Class for store information about dish
Source: https://t-secrets.ru/documents/tehnologicheskaya-karta-bliuda/
"""
class technical_map_model(product):
    __recipe: recipe_model = None
    __source: str = ""
    __date_of_approval: datetime = None
    __general_manager: str = ""
    __company: organization_model = None
    __package: package_model = None

    def __init__(self,
                 name: str,
                 recipe: recipe_model,
                 source: str,
                 date: datetime,
                 general_manager: str,
                 company: organization_model,
                 package: package_model,
                 unit: unit_of_measurement_model = None):
        super().__init__()
        self.name = name
        self.brand = "tech_map"
        self.unit = unit if unit is not None else unit_of_measurement_model.create_g()

        self.recipe = recipe
        self.source = source
        self.date_of_approval = date
        self.general_manager = general_manager
        self.company = company
        self.package = package

    @property
    def brutto(self) -> float:
        """Brutto = sum of brutto of recipe"""
        if self.__recipe is None:
            return 0.0
        return self.__recipe.brutto

    @property
    def netto(self) -> float:
        """Netto = sum of netto of recipe"""
        if self.__recipe is None:
            return 0.0
        return self.__recipe.netto

    @property
    def package(self) -> package_model:
        """Getter for package"""
        return self.__package

    @package.setter
    def package(self, new_package: package_model) -> None:
        """Setter for package"""
        self.__package = validate.validated_null_value(
            new_package,
            "new package",
            "new package must be not None",
            arguments_exception
        )

    @property
    def recipe(self) -> recipe_model:
        """Getter for recipe"""
        return self.__recipe

    @recipe.setter
    def recipe(self, new_recipe: recipe_model) -> None:
        """Setter for recipe"""
        self.__recipe = validate.validated_null_value(
            new_recipe,
            "new recipe",
            "new recipe must be not None",
            arguments_exception
        )

    @property
    def source(self) -> str:
        """Getter for source"""
        return self.__source

    @source.setter
    def source(self, new_source: str) -> None:
        """Setter for source"""
        self.__source = validate.validated_null_empty_obj(
            new_source,
            "new source",
            "new source must be not None or empty",
            arguments_exception
        )

    @property
    def general_manager(self) -> str:
        """Getter for general manager"""
        return self.__general_manager

    @general_manager.setter
    def general_manager(self, new_general_manager: str) -> None:
        """Setter for general manager"""
        self.__general_manager = validate.validated_null_empty_obj(
            new_general_manager,
            "new general manager",
            "new general manager must be not None or empty",
            arguments_exception
        )

    @property
    def company(self) -> organization_model:
        """Getter for company"""
        return self.__company

    @company.setter
    def company(self, new_company: organization_model) -> None:
        """Setter for company"""
        self.__company = validate.validated_null_value(
            new_company,
            "new company",
            "new company must be not None",
            arguments_exception
        )

    @property
    def date_of_approval(self) -> datetime:
        """Getter for date of approval"""
        return self.__date_of_approval

    @date_of_approval.setter
    def date_of_approval(self, new_date: datetime) -> None:
        """Setter for date of approval"""
        self.__date_of_approval = validate.validated_null_value(
            new_date,
            "new date",
            "new date must be not None",
            arguments_exception
        )

    @classmethod
    def create_technical_map(cls) -> "technical_map_model":
        """Factory method for creating technical map model"""
        return cls(
            "French baguette",
            recipe_model.create_recipe(),
            "M. P. Mogilny 2nd edition DeLi plus, 2016, - 888 p.",
            datetime.strptime("08.09.25", "%d.%m.%y"),
            "Lavrenov O.S.",
            organization_model.create_organization(),
            package_model.create_package_paper(),
            unit_of_measurement_model.create_g()
        )
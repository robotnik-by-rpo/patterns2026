from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.organization_model import organization_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.warehouse_model import warehouse_model
from typing import TypedDict
from collections.abc import Callable

"""Class for store base objects like caches"""
class base_data_setting_storage(TypedDict):
    create_units: dict[str, dict[str, unit_of_measurement_model]]
    groups: dict[str, group_nomenclature_model]
    company: organization_model
    nomenclatures: dict[str, list[nomenclature_model]]
    warehouses: dict[str, list[warehouse_model]]


"""Class for call method for creating objects"""
class settings_storage_factory:
    @staticmethod
    def __create_units() -> dict[str,dict[str,unit_of_measurement_model]]:
        """Factory method for creating base units"""
        return {"weight":{'gram': unit_of_measurement_model.create_g(),
                          'kilogram': unit_of_measurement_model.create_kg(),
                          'ton': unit_of_measurement_model.create_ton()},
                "volume":{'milliliter': unit_of_measurement_model.create_ml(),
                          'liter': unit_of_measurement_model.create_l(),
                          'cubic meter': unit_of_measurement_model.create_m3()},
                "square":{'square millimete': unit_of_measurement_model.create_mm2(),
                           'square centimeter': unit_of_measurement_model.create_sm2(),
                           'square meter': unit_of_measurement_model.create_m2()}}
    @staticmethod
    def __create_groups() -> dict[str, group_nomenclature_model]:
        """Factory method for creating base organization"""
        return group_nomenclature_model.create_groups()

    @staticmethod
    def __create_company() -> organization_model:
        """Factory method for creating base company"""
        return organization_model("Ромашка",
                                "1350791749",
                                "782189947",
                                "78328490185897461647",
                                "ООО")
    
    @staticmethod
    def __create_nomenclature( 
        groups: dict[str, group_nomenclature_model],
        units: dict[str, dict[str, unit_of_measurement_model]]
    ) -> dict[str, list[nomenclature_model]]:
        """Factory method for creating nomenclatures"""
        kg = units["weight"]["kilogram"]
        return {"ingredients": nomenclature_model.create_crude_ingredients(groups["ingredients"],kg),
                "blanks": nomenclature_model.create_crude_blanks(groups["blanks"],kg),
                "prepark": nomenclature_model.create_prepark_prepark(groups["prepark"],kg),
                "order": {},
                "finished products": nomenclature_model.create_dish_finished_products(groups["finished products"],kg),
                "consumables": nomenclature_model.create_product_consumables(groups["consumables"],kg)}
    
    @staticmethod
    def __create_warehouses(
        company: organization_model, 
        units: dict[str, dict[str, unit_of_measurement_model]],
    ) -> dict[str, list[warehouse_model]]:
        """Factory method foe creating warehouses"""
        m2 = units["square"]["square meter"]
        return {"A": warehouse_model.create_warehouses_A(company, m2),
                "A+": warehouse_model.create_warehouses_Ap(company, m2),
                "B": warehouse_model.create_warehouses_B(company, m2),
                "B+": warehouse_model.create_warehouses_Bp(company, m2),
                "C": warehouse_model.create_warehouses_C(company, m2),
                "D": warehouse_model.create_warehouses_D(company, m2)} 
    
    @classmethod
    def create_all(cls) -> base_data_setting_storage:
        """Factory for call all factoies methods for creating caches"""
        units = cls.__create_units()
        groups = cls.__create_groups()
        company = cls.__create_company()

        return base_data_setting_storage(
            units=units,
            groups=groups,
            company=company,
            nomenclatures=cls.__create_nomenclature(groups,units),
            warehouses=cls.__create_warehouses(company, units)
        )



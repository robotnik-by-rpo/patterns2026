from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.organization_model import organization_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.warehouse_model import warehouse_model
from Src.Models.technical_map_model import technical_map_model
from Src.Models.transaction_model import transaction_model
import datetime
from Src.Core.event_type import event_type
from Src.Logics.observer import observer

class initial_domain:
    def __new__(cls):
        if not hasattr(cls, '_initial_domain__instance'):
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def init_domain_into_storage(self) -> None:
        """Initing domains into storage"""
        from Src.Logics.storage_manager import storage_manager
        
        self.__storage: storage_manager = storage_manager()
        self.__init_units()        
        self.__init_groups()        
        self.__init_company() 
        self.__init_nomenclatures()
        self.__init_warehouses()
        self.__init_tech_map()
        self.__init_transactions()
    

    def __init_tech_map(self) -> None:
        """Init tech map into storage manager"""
        observer.create(event_type.init_tech_map())
        self.__storage.tech_maps["French baguette"] = technical_map_model.create_technical_map()

    def __init_company(self) -> None:
        """Init company into storage manager"""
        observer.create(event_type.init_company())
        self.__storage.company = organization_model("Ромашка", "1350791749", "782189947", 
                                        "78328490185897461647", "ООО")
    def __init_groups(self) -> None:
        """Init groups into storage manager"""
        observer.create(event_type.init_groups())
        self.__storage.groups_nomenclature = group_nomenclature_model.create_groups() 

    def __init_nomenclatures(self) -> None:
        """Creates and sets nomenclatures"""
        observer.create(event_type.init_nomenclatures())
        kg = self.__storage.units_of_measurement["weight"]["kilogram"]
        groups = self.__storage.groups_nomenclature

        self.__storage.nomenclatures = {
            "ingredients": nomenclature_model.create_crude_ingredients(groups["ingredients"], kg),
            "blanks": nomenclature_model.create_crude_blanks(groups["blanks"], kg),
            "prepack": nomenclature_model.create_prepack_prepack(groups["prepack"], kg),
            "order": {},
            "finished products": nomenclature_model.create_dish_finished_products(groups["finished products"], kg),
            "consumables": nomenclature_model.create_product_consumables(groups["consumables"], kg)
        }

    def __init_warehouses(self) -> None:
        """Creates and sets warehouses"""

        observer.create(event_type.init_warehouses())

        m2 = self.__storage.units_of_measurement["square"]["square meter"]
        company = self.__storage.company

        self.__storage.warehouses = {
            "A": warehouse_model.create_warehouses_A(company, m2),
            "A+": warehouse_model.create_warehouses_Ap(company, m2),
            "B": warehouse_model.create_warehouses_B(company, m2),
            "B+": warehouse_model.create_warehouses_Bp(company, m2),
            "C": warehouse_model.create_warehouses_C(company, m2),
            "D": warehouse_model.create_warehouses_D(company, m2)
        }

    def __init_units(self) -> None:
            """Creates and sets units of measurement"""
            observer.create(event_type.init_units())

            g = unit_of_measurement_model.create_g()
            ml = unit_of_measurement_model.create_ml()
            mm2 = unit_of_measurement_model.create_mm2()

            kg = unit_of_measurement_model("kilogram", 1000, g)
            ton = unit_of_measurement_model("ton", 1000, kg)

            l = unit_of_measurement_model("liter", 1000, ml)
            m3 = unit_of_measurement_model("cubic meter", 1000, l)

            c2 = unit_of_measurement_model("square centimeter", 100, mm2)
            m2 = unit_of_measurement_model("square meter", 10000, c2)

            self.__storage.units_of_measurement = {
                "weight": {g.name: g, kg.name: kg, ton.name: ton},
                "volume": {ml.name: ml, l.name: l, m3.name: m3},
                "square": {mm2.name: mm2, c2.name: c2, m2.name: m2}
            }

    def __init_transactions(self) -> None:
        """Method for creating transactions"""
        observer.create(event_type.init_transactions())

        storage = self.__storage
        kg = storage.units_of_measurement["weight"]["kilogram"]
        
        flour = storage.nomenclatures["ingredients"]["flour"]
        salt = storage.nomenclatures["ingredients"]["salt"]
        
        transactions = [
            transaction_model("Приход муки", flour, kg, 100.0, datetime.datetime(2025, 1, 1)),
            transaction_model("Приход муки", flour, kg, 50.0, datetime.datetime(2025, 2, 1)),
            transaction_model("Расход муки", flour, kg, -30.0, datetime.datetime(2025, 3, 1)),
            transaction_model("Приход соли", salt, kg, 10.0, datetime.datetime(2025, 1, 1)),
            transaction_model("Расход соли", salt, kg, -5.0, datetime.datetime(2025, 2, 1)),
        ]
        
        for t in transactions:
            storage.transactions[t.id] = t

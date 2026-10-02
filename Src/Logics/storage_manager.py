from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.organization_model import organization_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.warehouse_model import warehouse_model
from Src.Core.building import building
from Src.Core.abstract_manager import abstract_manager

class storage_manager(abstract_manager):
    """Class storing units, nomenclatures, company, warehouses, groups"""  
    __units: dict[str, dict[str, unit_of_measurement_model]]
    __nomenclatures: dict[str,list[nomenclature_model]]
    __company: organization_model
    __warehouses: list[warehouse_model]
    __groups: list[group_nomenclature_model]
    __is_first : bool

    def __new__(cls):
        """Singletone"""
        if not hasattr(cls, '_storage_manager__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.__units = {}
            cls.__instance.__nomenclatures = {}
            cls.__instance.__company = None
            cls.__instance.__warehouses = []
            cls.__instance.__groups = []
            cls.__instance.__is_first = True
            cls.__instance.__is_first = cls.__instance.convert()
        return cls.__instance

    def convert(self) -> bool:
        """Check, if data create at first so they will creat base data"""
        if self.__is_first: 
            self.__create_data()
        return False
    
    def __create_data(self) -> None:
        """Creating a base data"""
        self.__units = self.__create_unit_of_measure()
        self.__groups = self.__create_groups()
        self.__company = self.__create_company()
        self.__nomenclatures = self.__create_nomenclature()
        self.__warehouses = self.__create_warehouses()

    def __create_unit_of_measure(self) -> dict[str, dict[str, unit_of_measurement_model]]:
        """Uniting base of measurements for storage"""
        # weight
        g = unit_of_measurement_model("gram",1)
        kg = unit_of_measurement_model("kilogram",1000,g)
        t = unit_of_measurement_model("ton", 1000, kg)

        # volume
        ml = unit_of_measurement_model("milliliter",1)
        l = unit_of_measurement_model("liter",1000, ml)
        m3 = unit_of_measurement_model("cubic meter",1000,l)

        # square
        ml2 = unit_of_measurement_model("square millimete",1)
        sm2 = unit_of_measurement_model("square centimeter",100,ml2)
        m2 = unit_of_measurement_model("square meter",10000,sm2)

        return {"weight":{'gram':g,'kilogram':kg,'ton':t},
                "volume":{'milliliter':ml,'liter':l,'cubic meter':m3},
                "square":{'square millimete':ml2, 'square centimeter': sm2, 'square meter':m2}}

    def __create_groups(self) -> list[group_nomenclature_model]:
        """Uniting base groups of nomenclatures"""
        groups = []
        name_groups = ["order", 
                       "ingredients", 
                       "blanks",
                       "semimanufactures",
                       "finished products",
                       "consumables"]

        for n in name_groups:
            groups.append(group_nomenclature_model(n))

        return groups


    def __create_nomenclature(self) -> dict[str,list[nomenclature_model]]:
        """Uniting base nomenclature"""
        nomenclatures = []
        
        names_liquid = ["water","olive oil"]
        full_names_liquid = ["water Aqua Holding","olive oil Borges"]
        type_liquid = ["crude","crude"]

        for n, f, t in zip(names_liquid, full_names_liquid, type_liquid):
            nom = nomenclature_model(n,
                                     f,
                                     self.__groups[1], 
                                     self.__units["volume"]["milliliter"],
                                     t)
            nomenclatures.append(nom)
        
        names_solid = ["flour","sugar","yeast"]
        full_names_solid = ["flour MAKFA","sugar Tchaikovsky", "yeast Saf-Levure"]
        type_solid = ["crude","crude","crude"]
        
        for n, f, t in zip(names_solid, full_names_solid, type_solid):
            nom = nomenclature_model(n,
                                     f,
                                     self.__groups[1], 
                                     self.__units["weight"]["kilogram"],
                                     t)
            nomenclatures.append(nom)

        return {"ingredients":nomenclatures}


    def __create_warehouses(self) -> list[warehouse_model]:
        """Uniting base warehouses"""
        address = ["Moscow, Pushkina St. 35",
                   "Saint Petersburg, Repina St. 75",
                   "Saint Petersburg, Sofia St. 92",
                   "Moscow, Volkhonka St. 24",
                   "Voronezh, 25th October St. 45"]
        names = ["A01",
                 "A02",
                 "B01",
                 "A03",
                 "B02"]
        square = [183,1891,889,712,142]
        warehouses = []

        for n,a,s in zip(names, address,square):
            desc = warehouse_model(n,
                                   self.__company,
                                   building("warehouse",s,self.__units["square"]["square meter"],a))
            warehouses.append(desc)

        return warehouses

    def __create_company(self) -> organization_model:
        """Uniting base company"""
        return organization_model("Ромашка",
                                  "1350791749",
                                  "782189947",
                                  "78328490185897461647",
                                  "ООО")
    
    @property
    def groups_nomenclature(self) -> list[group_nomenclature_model]:
        """It's getter for groups of nomenclature"""
        return self.__groups

    @groups_nomenclature.setter
    def groups_nomenclature(self, 
                            new_groups_nomenclatures: list[group_nomenclature_model]) -> None:
        """It's setter for groups of nomenclature"""
        self.__groups = new_groups_nomenclatures

    @property
    def nomenclatures(self) -> dict[str,list[nomenclature_model]]:
        """It's getter for nomenclature"""
        return self.__nomenclatures
    
    @nomenclatures.setter
    def nomenclatures(self, new_nomenclatures: dict[str,list[nomenclature_model]])-> None:
        """It's setter for nomenclature"""
        self.__nomenclatures = new_nomenclatures
    
    @property
    def warehouses(self) -> list[warehouse_model]:
        """It's getter for warehouses"""
        return self.__warehouses
    
    @warehouses.setter
    def warehouses(self, new_warehouses) -> None:
        """It's setter for warehouses"""
        self.__warehouses = new_warehouses

    @property
    def company(self) -> organization_model:
        """It's getter for company"""
        return self.__company 
    
    @company.setter
    def company(self, new_company: organization_model) -> None:
        """It's setter for company"""
        self.__company = new_company

    @property
    def is_first(self) -> bool:
        """It's getter for flag"""
        return self.__is_first
    
    @is_first.setter
    def is_first(self, new_flag: bool) -> None:
        """It's setter for flag"""
        self.__is_first = new_flag

    @property
    def units_of_measurement(self)->dict[str, dict[str, unit_of_measurement_model]]:
        return self.__units
    
    @units_of_measurement.setter
    def units_of_measurement(self, new_units):
        self.__units = new_units

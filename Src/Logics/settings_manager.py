from Src.Core.abstract_manager import abstract_manager
import json
from Src.Models.organization_model import organization_model
from Src.Core.exception import operation_exception
from Src.Models.settings_model import settings_model
from Src.Core.validate import validate
from Src.Core.exception import not_exist_exception

class setting_manager(abstract_manager):
    """Class storing settings"""
    __default_file: str = "settings.json"
    __KEYS_FROM_FILE: list[str] = ["accounter_name",
                                   "name_organization",
                                   "boss_name",
                                   "inn",
                                   "bic",
                                   "current_accounter",
                                   "form_of_ownership",
                                   "is_first"]
    
    __default_inn: str = "1829111559"
    __default_bic: str = "124125513"
    __default_current_accounter: str = "18291112593229111559"
    __default_form_of_ownership: str = "ООО"
    __default_is_first: bool = True
    __default_boss_name: str = "boss"
    __default_accounter_name: str = "accounter"
    __default_company_name: str = "Ромашка"
    __settings: settings_model = None

    def __init__(self):
        """Initing new settings"""
        if self.__settings is None:
            self.__settings = settings_model()

    def __new__(cls):
        """singletone"""
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            cls.instance.__settings = settings_model()
        return cls.instance

    def load(self, file_name = ""):
        """Upload new data from json file"""
        inner_file_name = file_name.strip() if file_name.strip() else self.__default_file
        inner_file_name = validate.validated_filename_settings(inner_file_name,
                                                               "file name",
                                                               "file name must be correct and be json",
                                                               operation_exception)
        try:
            with open(inner_file_name, "r", encoding="utf-8") as file:
                self.data = json.load(file)
                self.is_loaded = self.convert()
        except Exception as ex:
            raise operation_exception("load","Error uploading file and processing file")
        
    def convert(self):
        """Convert data from json file"""
        missing = [key for key in self.__KEYS_FROM_FILE if key not in self.data]
        if missing:
            print(f"keys weren't got from json, missing keys: {','.join(missing)}")
        accounter_name = self.data.get("accounter_name",self.__default_accounter_name)
        boss_name = self.data.get("boss_name",self.__default_boss_name)
        company = organization_model(
            self.data.get("name_organization",self.__default_company_name),
            self.data.get("inn",self.__default_inn),
            self.data.get("bic",self.__default_bic),
            self.data.get("current_accounter",self.__default_current_accounter),
            self.data.get("form_of_ownership",self.__default_form_of_ownership),
        )
        is_first = self.data.get("is_first",self.__default_is_first)
        self.__settings.accounter_name = accounter_name
        self.__settings.boss_name = boss_name
        self.__settings.company = company
        self.__settings.is_first = is_first
        return True

    @property
    def settings(self) -> settings_model:
        """Getter for settings"""
        return self.__settings

    @settings.setter
    def settings(self, new_settings) -> None:
        """Setter for settings"""
        self.__settings = new_settings
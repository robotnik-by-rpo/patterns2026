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
        try:
            self.__settings.accounter_name = self.data["accounter_name"]
            self.__settings.boss_name = self.data["boss_name"]
            self.__settings.company = organization_model(self.data["name_organization"],
                                                        self.data["inn"],
                                                        self.data["bic"],
                                                        self.data["current_accounter"],
                                                        self.data["form_of_ownership"])
            self.__settings.is_first = self.data["is_first"]
            return True
        except KeyError as e:
            raise not_exist_exception("convert", "Error getting data by key from json") from e
        

    @property
    def settings(self) -> settings_model:
        """Getter for settings"""
        return self.__settings

    @settings.setter
    def settings(self, new_settings) -> None:
        """Setter for settings"""
        self.__settings = new_settings
from Src.Core.abstract_manager import abstract_manager
import json
from Src.Models.organization_model import organization_model
from Src.Core.exception import operation_exception
from Src.Models.settings_model import settings_model
from Src.Core.validate import validate
from Src.Dtos.report_type_dto import report_type_enum
from Src.Core.exception import arguments_exception
from Src.Logics.convert_factory import convert_factory
from Src.Core.abstract_observation import abstract_observation
from Src.Core.event_type import event_type
from Src.Logics.observer import observer

class setting_manager(abstract_manager, abstract_observation):
    """Class storing settings"""
    __default_file: str = "settings.json"
    __settings: settings_model = None

    __event_type: event_type = None
    def __init__(self):
        """Initing new settings"""
        super().__init__()
        if self.__settings is None:
            self.__settings = settings_model()
            observer.add(self)

    def __new__(cls):
        """singletone"""
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            cls.instance.__settings = settings_model()
        return cls.instance

    def load(self, file_name = ""):
        """Upload new data from json file"""


        inner_file_name = file_name.strip() if file_name.strip() else self.__default_file
        inner_file_name = validate.validated_filename_settings(
            inner_file_name,
            "file name",
            "file name must be correct and be json",
            operation_exception,
        )
        try:
            with open(inner_file_name, "r", encoding="utf-8") as file:
                observer.create(event_type.load_settings(), {"file": inner_file_name})

                raw = json.load(file)
        except Exception:
            raise operation_exception("load", "Error uploading file and processing file")

        if isinstance(raw, dict) and "__class__" not in raw:
            raw["__class__"] = "settings_model"

        try:
            deserialized = convert_factory().deserialize(raw)

            observer.create(event_type.change_settings(), {"settings": "loaded"})
        except Exception as ex:
            raise operation_exception("deserialize", f"cannot deserialize settings: {ex}")

        if not isinstance(deserialized, settings_model):
            raise operation_exception(
                "deserialize",
                f"expected settings_model, got {type(deserialized).__name__}",
            )

        self.__settings = deserialized
        self.data = raw
        self.is_loaded = True

    @property
    def settings(self) -> settings_model:
        """Getter for settings"""
        return self.__settings

    @settings.setter
    def settings(self, new_settings) -> None:
        """Setter for settings"""
        self.__settings = validate.validated_null_value(new_settings,
                                                        "new settings",
                                                        "new settings must be not None",
                                                        arguments_exception)
        observer.create(event_type.change_settings(), {"settings": "updated"})
        
    
    def handler(self, event_types: str, params: object):
        """Processing meassges"""
        if event_types == event_type.change_settings():
            print("Changed settings")
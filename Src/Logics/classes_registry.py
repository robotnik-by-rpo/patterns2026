import importlib
import pkgutil
from Src.Core.abc_data import unit
from Src.Core.abstract_manager import abstract_manager
import Src.Models as models_pkg
import Src.Logics as managers_pkg

"""
Registry with domains
"""
class classes_registry:
    __mapping: dict[str, type] = None
    __DOMAIN_PACKAGE: str = "Src.Models"

    def __new__(cls):
        if not hasattr(cls, '_class_registry__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.__initing_domains()
            cls.__instance.__initing_managers()
        return cls.__instance
    
    def __initing_domains(self) -> None:
        """Method for initing domains model into mapping"""
        for module_info in pkgutil.walk_packages(
            models_pkg.__path__, prefix=models_pkg.__name__ + "."
        ):
            importlib.import_module(module_info.name)

        self.__mapping = {
            cls.__name__: cls 
            for cls in self.__all_subclasses(unit)
            if cls.__module__.startswith(self.__DOMAIN_PACKAGE + ".")
        }
        
    def get(self, name: str) -> type | None:
        """Method for getting domain model"""
        return self.__mapping.get(name)
    
    def __all_subclasses(self, cls: type) -> set[type]:
        """Method for collecting subclasses"""
        result: set[str] = set()
        for sub in cls.__subclasses__():
            result.add(sub)
            result |= self.__all_subclasses(sub)
        return result

    def __initing_managers(self) -> None:
        """Method for initing managers into mapping"""
        for manager_info in pkgutil.walk_packages(
            managers_pkg.__path__, prefix=managers_pkg.__name__ + "."
        ):
            importlib.import_module(manager_info.name)

        self.__mapping.update({
            cls.__name__: cls
            for cls in self.__all_subclasses(abstract_manager)
            if "manager" in cls.__name__
        })
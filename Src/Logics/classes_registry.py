import importlib
import pkgutil
from Src.Core.abc_data import unit
from Src.Core.abstract_manager import abstract_manager
import Src.Models as models_pkg
import Src.Logics as managers_pkg
import Src.Dtos as dtos_pkg
from enum import Enum

"""
Registry with domains
"""
class classes_registry:
    __mapping: dict[str, type] = {}
    __DOMAIN_PACKAGE: str = "Src.Models"
    __DTOS: str = "Src.Dtos"

    def __new__(cls):
        if not hasattr(cls, '_class_registry__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.__initing_domains()
            cls.__instance.__initing_managers()
            cls.__instance.__initing_dtos()
        return cls.__instance
    
    def __initing_dtos(self) -> None:
        """Method for initing dtos in registry"""
        self.__load_pkg(dtos_pkg, self.__DTOS, Enum)
        for module_info in pkgutil.walk_packages(
            dtos_pkg.__path__, prefix=dtos_pkg.__name__ + "."
        ):
            mod = importlib.import_module(module_info.name)
            for name in dir(mod):
                obj = getattr(mod, name)
                if (
                    isinstance(obj, type)
                    and obj.__module__.startswith(self.__DTOS + ".")
                    and not name.startswith("_")
                ):
                    self.__mapping[name] = obj

    def __load_pkg(self, pkg, directory: str, sub_class: any):
        """Method for loading classes in package"""
        for module_info in pkgutil.walk_packages(
            pkg.__path__, prefix=pkg.__name__ + "."
        ):
            importlib.import_module(module_info.name)

        self.__mapping.update({
            cls.__name__: cls 
            for cls in self.__all_subclasses(sub_class)
            if cls.__module__.startswith(directory + ".")
        })

    def __initing_domains(self) -> None:
        """Method for initing domains model into mapping"""
        self.__load_pkg(models_pkg, self.__DOMAIN_PACKAGE, unit)
        
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
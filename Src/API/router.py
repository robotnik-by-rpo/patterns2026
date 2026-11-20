from fastapi import APIRouter
import Src.Routers as routers_pkg
import importlib
import pkgutil
from Src.Core.abstract_router import abstract_router

class server_API:
    __API: APIRouter = None
    __instance = None
    __ROUTER_PACKAGE: str = "Src.Routers"
    __routers: list[abstract_router] = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__API = APIRouter(prefix="/api")
            cls.__instance.__initing_routers()
        return cls.__instance
    
    def __initing_routers(self) -> None:
        """Initing routers"""
        self.__get_routers_from_package()
        for router_cls in self.__routers:
            self.__API.include_router(router_cls().router)

    def __all_subclasses(self, cls: type) -> set[type]:
            """Method for collecting subclasses"""
            result: set[str] = set()
            for sub in cls.__subclasses__():
                result.add(sub)
                result |= self.__all_subclasses(sub)
            return result

    def __get_routers_from_package(self) -> None:
        """Method for getting routers from directory"""
        for module_info in pkgutil.walk_packages(
            routers_pkg.__path__, prefix=routers_pkg.__name__ + "."
        ):
            importlib.import_module(module_info.name)

        self.__routers = [
            cls 
            for cls in self.__all_subclasses(abstract_router)
            if cls.__module__.startswith(self.__ROUTER_PACKAGE + ".")
        ]

    @property
    def api(self) -> APIRouter:
        return self.__API
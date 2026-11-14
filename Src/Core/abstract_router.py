from abc import ABC, abstractmethod
from fastapi import HTTPException, APIRouter

class abstract_router(ABC):
    
    __prefix: str = ""
    __router:  APIRouter = None

    @abstractmethod
    def _initing_paths(self):
        """Abstract method for initing paths into router"""
        ...

    @property
    def router(self) -> APIRouter:
        """Getter for router"""
        return self.__router
    
    @router.setter
    def router(self, new_router: APIRouter) -> None:
        """Setter for router"""
        self.__router = new_router


    @property
    def prefix(self) -> str:
        """Getter for router"""
        return self.__prefix
    
    @prefix.setter
    def prefix(self, new_prefix: str) -> None:
        """Setter for router"""
        self.__prefix = new_prefix

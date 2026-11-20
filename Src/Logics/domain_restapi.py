from Src.Core.exception import arguments_exception, not_exist_exception, operation_exception
from Src.Logics.domain_checker import domain_checker
from Src.Logics.domain_factory import domain_factory
from Src.Core.validate import validate

"""
Class restapi for domains 
"""
class domain_restapi:
    __checker: domain_checker = None
    __factory: domain_factory = None

    def __new__(cls):
        """Singletone"""
        if not hasattr(cls, '_domain_service__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.__initing_service()
        return cls.__instance
    
    def __initing_service(self):
        self.__checker = domain_checker()
        self.__factory = domain_factory()

    def create(self, obj) -> any:
        """Method for adding a new domain"""
        validate.validated_null_value(obj, 
                                      "object", 
                                      "object must be not None",
                                      arguments_exception)
        if getattr(obj, "id", None) and self.__factory.find_or_none(obj.id) is not None:
            raise operation_exception(
                "id", f"object with id {obj.id} already exists"
            )
        
        if getattr(obj, "name", None) and self.__factory.find_or_none(obj.name) is not None:
            raise operation_exception(
                "name", f"object with name {obj.name!r} already exists"
            )
        
        self.__factory.dispatch_add(obj)
        return obj

    def read(self, code: str) -> any:
        """Method for reading by id or name"""
        return self.__factory.find(code)

    def update(self, code: str, new_obj: any) -> any:
        """Method for replacing domain"""
        validate.validated_null_value(new_obj,
                                      "object", 
                                      "object must be not None",
                                      arguments_exception)
        current = self.__factory.find(code)

        if self.__checker.is_referenced(current):
            raise operation_exception(
                "domain",
                f"cannot update {code}: entity is referenced by another entity",
            )
        new_id = getattr(new_obj, "id", None)
        if new_id is not None and new_id != current.id:
            raise arguments_exception("id", "id cannot be changed on update")
        new_obj.id = current.id

        self.__factory.dispatch_remove(current)
        self.__factory.dispatch_add(new_obj)
        return new_obj

    def delete(self, code: str, force: bool = False) -> None:
        """
        Method for deleting domain with check link
        
        force:
        - flag for forced deletion
        """
        target = self.__factory.find(code)
        if not force and self.__checker.is_referenced(target):
            raise operation_exception(
                "domain",
                f"cannot delete {code}: entity is referenced by another entity",
            )
        self.__factory.dispatch_remove(target)

    
from Src.Core.abstract_filter import abstract_filter
from Src.Dtos.filter_type_dto import filter_type_enum
from Src.Logics.filters import like_filter
from Src.Logics.filters import equals_filter
from Src.Core.exception import not_exist_exception

"""
Class factory fot filters
"""
class filter_factory:
    __mapping: dict[filter_type_enum, abstract_filter] = {}

    def __new__(cls):
        """Singletone"""
        if not hasattr(cls, '_filter_factory__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.__initing_mapping()
        return cls.__instance
    
    def __initing_mapping(self):
        """Method for initing mapping"""
        self.__mapping[filter_type_enum.EQUALS] = equals_filter()
        self.__mapping[filter_type_enum.LIKE] = like_filter()

    @classmethod
    def create(cls, filter_type: filter_type_enum) -> abstract_filter:
        """Method for creating filter"""
        filter = cls.__mapping.get(filter_type)
        if filter is None:
            raise not_exist_exception("filter type", f"filter {filter_type} doesn't exist")
        return filter
    


from Src.Dtos.filter_dto import filter_dto
from Src.Dtos.filter_dto import filter_item_dto
from Src.Dtos.filter_type_dto import filter_type_enum
from Src.Core.abstract_prototype import abstract_prototype

"""
Class for cloning a list of domain objects using a filter
"""
class prototype(abstract_prototype):

    def __init__(self, data: list):
        super().__init__()
        self.data = data

    def clone(self, filter_dto: filter_dto = None) -> "prototype":
        """Method for cloning with filter"""
        if filter_dto is None or not filter_dto.filters:
            return prototype(list(self.data))

        filtered_data = [
            item for item in self.data
            if self._match_filter(item, filter_dto.filters)
        ]

        return prototype(filtered_data)
    
    def _match_filter(self, item: any, filters: list[filter_type_enum]) -> bool:
        """Method for checking on correspondence all filters"""
        for f in filters:
            if not self._match_alone_filter(item, f):
                return False
        return True
    
    def _match_alone_filter(self, item: any, f: filter_item_dto) -> bool:
        """Method for checking a one filter with taking into account nesting"""
        value = self._get_linked_value(item, f.field_name)
        if value is None:
            return False

        str_value = str(value).lower()
        filter_value = str(f.value).lower()

        if f.filter_type == filter_type_enum.EQUALS:
            return str_value == filter_value
        elif f.filter_type == filter_type_enum.LIKE:
            return filter_value in str_value

        return False

    def _get_linked_value(self, obj: any, field_path:   str) -> any:
        """Method for checking recursive value by path"""
        if obj is None:
            return None
        
        parts = field_path.split(".")
        current = obj

        for part in parts:
            if current is None:
                return None
            
            if hasattr(current, part):
                current = getattr(current, part, None)
        return current
            

        


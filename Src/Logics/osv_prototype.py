from Src.Core.abstract_prototype import abstract_prototype
from Src.Dtos.filter_dto import filter_dto
from Src.Logics.prototype import prototype

"""
Special prototype for osv 
"""
class osv_report_prototype(abstract_prototype):
    __dto: filter_dto = None

    def __init__(self, dto: filter_dto = None):
        self.__dto = dto

    def clone(self, filter_dto: filter_dto = None) -> "osv_report_prototype":
        """Method for cloning with filter"""
        return osv_report_prototype(filter_dto or self.__dto)
    
    def process(self, source: list, dto: filter_dto | None = None) -> list[dict]:
        """Method for creating osv"""
        active_dto = dto or self.__dto
        filtered_source = source
        
        if active_dto and active_dto.filters:
            proto = prototype(source)
            filtered_source = proto.clone(active_dto).data
        
        result = []
        for obj in filtered_source:
            h = sum(ord(c) for c in obj.id)
            opening = h % 100
            income = (h * 2) % 100
            exp = (h * 3) % 100
            result.append({
                "id": obj.id,
                "name": getattr(obj, "name", ""),
                "opening_balance": opening,
                "income": income,
                "expense": exp,
                "closing_balance": opening + income - exp,
            })
        return result
from Src.Core.abstract_report import abstract_report
from abc import ABC, abstractmethod
from Src.Dtos.report_type_dto import report_type_enum
"""
Abstract factory reports
"""
class abstract_report_factory(ABC):
    @abstractmethod
    def create(self, report_type: report_type_enum) -> abstract_report:
        ...
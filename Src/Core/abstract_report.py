from abc import ABC, abstractmethod
from Src.Dtos.report_result_dto import report_result_dto
from Src.Core.abc_data import unit

"""
Abstract class for generating a report
"""
class abstract_report(ABC):
    """
    Generate report
    """
    mime_type: str = "text/plain"
    file_extension: str = "txt"
    is_binary: bool = False

    @abstractmethod
    def build(self, source: unit) -> report_result_dto:
        ...
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
    @abstractmethod
    def build(self, source: unit) -> report_result_dto:
        ...

    @property
    @abstractmethod
    def mime_type(self) -> str:
        ...

    @property
    @abstractmethod
    def file_extension(self) -> str:
        ...

    @property
    @abstractmethod
    def is_binary(self) -> bool:
        ...
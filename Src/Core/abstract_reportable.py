from abc import ABC, abstractmethod

class abstract_reportable(ABC):
    @abstractmethod
    def report_header(self) -> list[str]:
        ...

    @abstractmethod
    def report_rows(self) -> list[list]:
        ...
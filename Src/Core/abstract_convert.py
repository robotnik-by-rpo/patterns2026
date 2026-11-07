from abc import ABC, abstractmethod

"""
Abstract class for convert object
"""
class abstract_convertor(ABC):
    @abstractmethod
    def convert(self, object: any)->dict:
        ...

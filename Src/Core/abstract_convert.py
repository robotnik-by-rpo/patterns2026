from abc import ABC, abstractmethod

"""
Abstract class for convert object
"""
class abstract_convertor(ABC):
    @abstractmethod
    def serialize(self, object: any)->dict:
        """Abstract method for serialization"""
        ...

    @abstractmethod
    def deserialize(self, object: any) -> any:
        """Abstract method for deserialization"""
        ...

    @abstractmethod
    def can_deserialize(self, object: any)->bool:
        """Abstract method for possibility serialization"""
        ...

    @abstractmethod
    def can_serialize(self, object: any) -> bool:
        """Abstract method for possibility deserialization"""
        ...
from Src.Core.abstract_convert import abstract_convertor
from Src.Core.validate import validate
from datetime import datetime
from Src.Core.exception import arguments_exception

"""
Convertor for converting datetime
"""
class datetime_convertor(abstract_convertor):
    def serialize(self, object: datetime) -> dict:
        """Convert datetime to iso format and split on parts"""
        return {"datetime": (validate.validated_type(object,
                                                     datetime,
                                                     "datetime", 
                                                     "wrong type, not datetime", 
                                                     arguments_exception)).isoformat(),
                "day": object.day,
                "month": object.month,
                "year": object.year,
                "hour": object.hour,
                "minute": object.minute,
                "second": object.second,
                "microsecond": object.microsecond}
    
    def deserialize(self, object: dict) -> any:
        """Method for deserializing"""
        if not isinstance(object, dict):
            raise arguments_exception("datetime", "datetime dict expected")
        iso = object.get("datetime")
        if not iso:
            raise arguments_exception("datetime", "key 'datetime' is missing")
        try:
            return datetime.fromisoformat(iso)
        except ValueError as ex:
            raise arguments_exception("datetime", f"wrong iso: {iso}") from ex
        
    def can_serialize(self, object: any) -> bool:
        """Method for check possibility for serialize"""
        return isinstance(object, datetime)

    def can_deserialize(self, object: any) -> bool:
        """Method for check possibility for serialize"""
        return isinstance(object, dict) and "datetime" in object